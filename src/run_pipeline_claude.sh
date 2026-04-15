#!/bin/bash
#BSD 3-Clause License
#
#Copyright (c) 2026, ASU-VDA-Lab
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################
# Orchestrates the full evaluation pipeline using KLayout DRC for one model.
#
# Usage:
#   bash src/run_pipeline_claude.sh [--agent-only|--score-only] <info.json>
#
# Phase flags (detection tasks only):
#   --agent-only   Run only prompt formatting and agent call (no scoring)
#   --score-only   Run only scoring, CSV, and logging (agent must have run first)
#
# Each invocation runs exactly one model and stores results under
# result/<model_name>/<design_type>/<task_type>/<case_name>/ and
# score/<model_name>/<design_type>/<task_type>/.

set -euo pipefail

# Compute workspace/src_dir early (needed for helper scripts)
workspace="${WORKSPACE:-/workspace}"
src_dir="${workspace}/src"

# ---------------------------------------------------------------------------
# 1. Parse arguments
# ---------------------------------------------------------------------------
phase="full"  # full | agent | score

# Check for phase flags
while [[ "${1:-}" == --* ]]; do
    case "$1" in
        --agent-only) phase="agent"; shift ;;
        --score-only) phase="score"; shift ;;
        *) echo "Error: unknown flag '$1'" >&2; exit 1 ;;
    esac
done

if [[ "$#" -ne 1 ]]; then
    echo "Usage: bash src/run_pipeline_claude.sh [--agent-only|--score-only] <info.json>" >&2
    exit 1
fi

input_json="$1"
if [[ ! -f "${input_json}" ]]; then
    echo "Error: info.json not found: ${input_json}" >&2
    exit 1
fi
eval "$(python3 "${src_dir}/parse_info_json.py" "${input_json}")"

if [[ -z "${task_type}" || -z "${model_name}" || -z "${case_name}" || -z "${design_type}" ]]; then
    echo "Error: missing required fields (task_type, model_name, case_name, design_type)." >&2
    exit 1
fi

if [[ "${task_type}" != "repair" && "${task_type}" != "detection" ]]; then
    echo "Error: task_type must be 'repair' or 'detection', got '${task_type}'." >&2
    exit 1
fi

if [[ "${design_type}" != "cell" && "${design_type}" != "polygon" && "${design_type}" != "block" ]]; then
    echo "Error: design_type must be 'cell', 'polygon', or 'block', got '${design_type}'." >&2
    exit 1
fi

# Phase flags only make sense for detection
if [[ "${phase}" != "full" && "${task_type}" == "repair" ]]; then
    echo "Error: --agent-only / --score-only flags are only supported for detection tasks." >&2
    exit 1
fi

# ---------------------------------------------------------------------------
# 2. Paths setup
# ---------------------------------------------------------------------------
testcase_base="${workspace}/testcase/asap7"
case_testcase_dir="${testcase_base}/${design_type}"

# ---------------------------------------------------------------------------
# Budget suffix on all output files so parallel runs with different
# AGENT_INITIAL_BUDGET values don't overwrite each other.
# ---------------------------------------------------------------------------
initial_budget="${AGENT_INITIAL_BUDGET:-1800}"
reminder_budget="${AGENT_REMINDER_BUDGET:-120}"
budget_suffix="${initial_budget}"

# ---------------------------------------------------------------------------
# Log all stdout+stderr to a file while still printing to the terminal
# ---------------------------------------------------------------------------
log_dir="${workspace}/logs"
mkdir -p "${log_dir}"
log_file="${log_dir}/${model_name}_${design_type}_${task_type}_${case_name}_${budget_suffix}.log"
exec > >(tee "${log_file}") 2>&1

# Golden DRC report: check drc_report/ (may be injected via docker cp)
golden_json="${case_testcase_dir}/drc_report/${case_name}.drc.json"
golden_lyrpt="${case_testcase_dir}/drc_report/${case_name}.lyrpt"
if [[ -f "${golden_json}" ]]; then
    golden_report="${golden_json}"
elif [[ -f "${golden_lyrpt}" ]]; then
    golden_report="${golden_lyrpt}"
else
    golden_report=""
fi

# For repair, golden report must be present before agent runs
if [[ "${task_type}" == "repair" && -z "${golden_report}" ]]; then
    echo "WARNING: Golden DRC report not found for ${case_name}. Scoring may fail." >&2
fi

# Prompt template selection: design-type-specific for repair, generic for detection
if [[ "${task_type}" == "repair" && -f "${src_dir}/prompt_repair_${design_type}.md" ]]; then
    prompt_template="${src_dir}/prompt_repair_${design_type}.md"
elif [[ -f "${src_dir}/prompt_${task_type}.md" ]]; then
    prompt_template="${src_dir}/prompt_${task_type}.md"
else
    prompt_template="${src_dir}/prompt.md"
fi

# Skill file for KLayout DRC
skill_file="${src_dir}/skill.md"

# DRC rule file (.lydrc for KLayout)
if [[ "${design_type}" == "cell" ]]; then
    design_rule="${testcase_base}/asap7_cell.lydrc"
else
    design_rule="${testcase_base}/asap7.lydrc"
fi

# ---------------------------------------------------------------------------
# 3. Agent script (Claude Code CLI) & global time budget
# ---------------------------------------------------------------------------
AGENT_SCRIPT="${src_dir}/agent_claude.py"
claude_effort="${CLAUDE_EFFORT:-}"

# initial_budget / reminder_budget / budget_suffix already defined earlier.

echo "============================================="
echo "  DRC Benchmark Pipeline (KLayout)"
echo "============================================="
echo "  task_type   : ${task_type}"
echo "  model_name  : ${model_name}"
echo "  case_name   : ${case_name}"
echo "  design_type : ${design_type}"
echo "  phase       : ${phase}"
echo "  workspace   : ${workspace}"
if [[ -n "${claude_effort}" ]]; then
echo "  effort      : ${claude_effort}"
fi
echo ""

# ---------------------------------------------------------------------------
# Helper: write score dict from JSON to CSV
# ---------------------------------------------------------------------------
write_score_csv() {
    local score_json="$1"
    local score_csv="$2"
    local case="$3"

    python3 "${src_dir}/write_score_csv.py" "${score_json}" "${score_csv}" "${case}"
}

# ---------------------------------------------------------------------------
# 4. Set up result/score directories (needed before prompt formatting)
# ---------------------------------------------------------------------------
result_dir="${workspace}/result/${model_name}/${design_type}/${task_type}/${case_name}"
score_dir="${workspace}/score/${model_name}/${design_type}/${task_type}"
temp_dir="${workspace}/temp/${model_name}_${design_type}_${task_type}_${case_name}_${budget_suffix}_$$"
mkdir -p "${result_dir}" "${score_dir}" "${temp_dir}"

max_iterations="${MAX_ITERATIONS:-5}"

if [[ "${task_type}" == "repair" ]]; then
    agent_output="${result_dir}/${case_name}_repaired_${budget_suffix}.py"
else
    agent_output="${result_dir}/${case_name}_detection_${budget_suffix}.json"
fi

# ---------------------------------------------------------------------------
# 5. Format prompt (build processed info.json with container paths)
# ---------------------------------------------------------------------------
echo "[Step 1] Formatting prompt..."

task_dir="${workspace}/task/${model_name}/${design_type}/${task_type}"
mkdir -p "${task_dir}"

case_info_json="${task_dir}/${case_name}_${budget_suffix}_info.json"

# Post-process the input JSON with container paths
python3 "${src_dir}/postprocess_info_json.py" \
    --input "${input_json}" \
    --output "${case_info_json}" \
    --skill_file "${skill_file}" \
    --testcase_dir "${case_testcase_dir}" \
    --case_name "${case_name}" \
    --golden_report "${golden_report}" \
    --design_rule "${design_rule}" \
    --drm_jpg "${testcase_base}/drm_jpg" \
    --output_path "${agent_output}" \
    --temp_dir "${temp_dir}" \
    --task_type "${task_type}" \
    --agent_initial_budget "${initial_budget}" \
    --agent_reminder_budget "${reminder_budget}"

formatted_prompt_path="${task_dir}/${case_name}_${task_type}_${budget_suffix}_prompt.md"

python3 "${src_dir}/prompt_format.py" \
    "${case_info_json}" \
    "${prompt_template}" \
    > "${formatted_prompt_path}"

# Format the reminder prompt template
if [[ "${task_type}" == "repair" ]]; then
    reminder_template="${src_dir}/prompt_reminder_repair.md"
else
    reminder_template="${src_dir}/prompt_reminder_detection.md"
fi
formatted_reminder_path="${task_dir}/${case_name}_${task_type}_${budget_suffix}_reminder.md"

python3 "${src_dir}/prompt_format.py" \
    "${case_info_json}" \
    "${reminder_template}" \
    > "${formatted_reminder_path}"

echo "  Formatted prompt: ${formatted_prompt_path}"
echo "  Formatted reminder: ${formatted_reminder_path}"
echo ""

# ---------------------------------------------------------------------------
# 6. Iteration loop (repair) or single-shot (detection)
# ---------------------------------------------------------------------------
original_script="${case_testcase_dir}/layout_script/${case_name}.py"
pipeline_start="${SECONDS}"

if [[ "${task_type}" == "repair" ]]; then

    # ===================================================================
    # REPAIR: multi-iteration loop with global agent time budget
    #
    # The agent gets a total of INITIAL_BUDGET seconds (default 600 = 10 min)
    # across ALL iterations. The timer is paused during KLayout DRC, scoring,
    # and other intermediate processing -- only agent_claude.py execution counts.
    #
    # When the budget is exhausted, a reminder is sent giving the agent
    # REMINDER_BUDGET seconds (default 120 = 2 min) to produce its final
    # output. The reminder ends when time runs out or the agent finishes
    # (whichever comes first). No further iterations run after a reminder.
    # ===================================================================
    actual_iterations=0
    # Intermediate DRC reports go into temp/; final best goes into result_dir
    iter_temp_dir="${result_dir}/temp_${budget_suffix}"
    mkdir -p "${iter_temp_dir}"

    cumulative_agent_seconds=0
    reminder_triggered=false

    echo "[Step 2] Starting repair iterations (max=${max_iterations})..."
    echo "  Agent time budget: ${initial_budget}s initial + ${reminder_budget}s reminder"
    echo ""

    for iter in $(seq 1 "${max_iterations}"); do
        actual_iterations="${iter}"
        echo "--- Iteration ${iter} of ${max_iterations} ---"

        # ---------------------------------------------------------------
        # Check remaining agent time budget
        # ---------------------------------------------------------------
        remaining_initial=$(python3 "${src_dir}/shell_math.py" --op max "${initial_budget}" "${cumulative_agent_seconds}")
        remaining_total=$(python3 "${src_dir}/shell_math.py" --op sub "${initial_budget}" "${reminder_budget}" "${cumulative_agent_seconds}")

        if [[ "${remaining_total}" -le 0 ]]; then
            echo "  Agent time budget fully exhausted (${cumulative_agent_seconds}s used). Stopping iterations."
            break
        fi

        if [[ "${remaining_initial}" -le 0 ]]; then
            # Initial budget exhausted -- give remainder as final reminder
            echo "  Initial budget exhausted (${cumulative_agent_seconds}s used). Sending final reminder (${remaining_total}s left)..."
            iter_reminder_timeout=1
            iter_final_timeout="${remaining_total}"
            reminder_triggered=true
        else
            # Compute how much reminder budget would remain if this iteration exhausts initial
            iter_reminder_timeout="${remaining_initial}"
            _spent=$(python3 "${src_dir}/shell_math.py" --op add "${cumulative_agent_seconds}" "${remaining_initial}")
            iter_final_timeout=$(python3 "${src_dir}/shell_math.py" --op sub "${initial_budget}" "${reminder_budget}" "${_spent}")
        fi

        echo "  Time remaining: ${remaining_initial}s initial + ${iter_final_timeout}s reminder"

        # ---------------------------------------------------------------
        # Determine the prompt file for this iteration
        # ---------------------------------------------------------------
        if [[ "${iter}" -eq 1 ]]; then
            prompt_file="${task_dir}/${case_name}_${task_type}_${budget_suffix}_prompt.md"
        else
            prev_iter=$((iter - 1))
            prev_drc_json="${iter_temp_dir}/${case_name}_iter${prev_iter}.drc.json"
            prev_script="${result_dir}/${case_name}_repaired_${budget_suffix}.py"
            iter_prompt="${iter_temp_dir}/${case_name}_iter${iter}_prompt.md"

            {
                echo "## Iteration ${iter} — Repair Remaining Violations"
                echo ""
                echo "Your previous repair (iteration ${prev_iter}) still has violations."
                echo ""
                if [[ -f "${prev_drc_json}" ]]; then
                    echo "The DRC report from your previous repair is at: ${prev_drc_json}"
                    echo "Read this JSON report to see exactly which rules are still violated,"
                    echo "their violation counts, and the per-violation geometry locations."
                    echo ""
                    echo "Summary:"
                    echo '```'
                    python3 "${src_dir}/summarize_drc_report.py" "${prev_drc_json}" 2>/dev/null || echo "(could not read DRC report)"
                    echo '```'
                    echo ""
                fi
                echo "Your previous repaired script is at: ${prev_script}"
                echo "Read it carefully to understand what you already changed."
                echo ""
                echo "Identify why violations persist, and produce a corrected version."
                echo ""
                echo "Save the corrected script to: ${agent_output}"
                echo ""
                echo "---"
                echo ""
                cat "${task_dir}/${case_name}_${task_type}_${budget_suffix}_prompt.md"
            } > "${iter_prompt}"

            prompt_file="${iter_prompt}"
        fi

        # Per-iteration output filenames
        iter_agent_output="${result_dir}/${case_name}_repaired_${budget_suffix}.py"
        iter_gds="${iter_temp_dir}/${case_name}_iter${iter}.gds"
        iter_render="${iter_temp_dir}/${case_name}_iter${iter}_render.py"
        iter_lyrpt="${iter_temp_dir}/${case_name}_iter${iter}.lyrpt"
        iter_repaired_json="${iter_temp_dir}/${case_name}_iter${iter}.drc.json"
        iter_connectivity_json="${iter_temp_dir}/${case_name}_iter${iter}_connectivity.json"
        iter_score_json="${score_dir}/${case_name}_score_${budget_suffix}_iter${iter}.json"

        agent_output="${iter_agent_output}"

        # ---------------------------------------------------------------
        # Run iteration in subshell
        # ---------------------------------------------------------------
        iter_success=true
        (
            set -e

            # --- Call LLM agent (timer running) ---
            agent_start="$(date +%s%N)"

            agent_stderr_tmp="$(mktemp)"
            python3 "${AGENT_SCRIPT}" \
                "${prompt_file}" \
                "${agent_output}" \
                --model "${model_name}" \
                --task_type "repair" \
                --reminder_timeout "${iter_reminder_timeout}" \
                --final_timeout "${iter_final_timeout}" \
                --temp_dir "${temp_dir}" \
                --fallback "${original_script}" \
                --reminder_prompt_file "${formatted_reminder_path}" \
                ${claude_effort:+--effort "${claude_effort}"} \
                2>"${agent_stderr_tmp}" \
            || {
                cat "${agent_stderr_tmp}" >&2
                echo "  WARNING: Agent failed for iteration ${iter}. Continuing with fallback." >&2
            }

            cat "${agent_stderr_tmp}" >&2

            agent_end="$(date +%s%N)"
            agent_runtime_ns=$(( agent_end - agent_start ))
            agent_runtime_seconds=$(python3 "${src_dir}/shell_math.py" --op div "${agent_runtime_ns}" 1000000000)

            reported_runtime="$(grep -oP 'RUNTIME_SECONDS=\K[0-9.]+' "${agent_stderr_tmp}" | tail -1 || true)"
            if [[ -n "${reported_runtime}" ]]; then
                agent_runtime_seconds="${reported_runtime}"
            fi
            rm -f "${agent_stderr_tmp}"

            echo "  Agent output    : ${agent_output}"
            _cum_display=$(python3 "${src_dir}/shell_math.py" --op add "${cumulative_agent_seconds}" "${agent_runtime_seconds}")
            _cum_display=$(python3 "${src_dir}/shell_math.py" --op fmt "${_cum_display}")
            echo "  Agent runtime   : ${agent_runtime_seconds}s (cumulative: ${_cum_display}s)"

            # Persist agent runtime before any potentially-failing steps
            echo "${agent_runtime_seconds}" > "${iter_temp_dir}/.iter${iter}_agent_rt"

            # --- Timer paused: KLayout DRC, scoring, etc. ---

            # --- Render GDS ---
            echo "  [Iter ${iter}] Rendering GDS..."
            python3 "${src_dir}/prepare_render_script.py" \
                "${agent_output}" "${iter_render}" "${iter_gds}"

            klayout -b -r "${iter_render}" \
            || { echo "  WARNING: KLayout render failed for iteration ${iter}." >&2; exit 1; }
            echo "  Rendered GDS: ${iter_gds}"

            # --- Run KLayout DRC (intermediates saved in temp/) ---
            if [[ "${SKIP_DRC:-0}" != "1" ]]; then
                echo "  [Iter ${iter}] Running KLayout DRC..."
                python3 "${src_dir}/run_klayout_drc.py" "${iter_gds}" "${design_rule}" "${iter_lyrpt}" \
                || echo "  (KLayout DRC returned non-zero for iter ${iter}.)"

                if [[ -f "${iter_lyrpt}" ]]; then
                    echo "  KLayout DRC report: ${iter_lyrpt}"
                    echo "  [Iter ${iter}] Converting DRC report to JSON..."
                    python3 "${src_dir}/process_klayout_reports.py" \
                        --lyrpt "${iter_lyrpt}" \
                        --output "${iter_repaired_json}" \
                        --case_name "${case_name}" \
                        --design_type "${design_type}" \
                        --layout-script "${agent_output}" \
                    || echo "  WARNING: Failed to convert DRC report for iter ${iter}."
                fi
            fi

            # --- Sanity check ---
            if [[ -f "${src_dir}/sanity_check.py" ]]; then
                klayout -b -r "${src_dir}/sanity_check.py" \
                    -rd "original_gds_path=${case_testcase_dir}/gds/${case_name}.gds" \
                    -rd "modified_gds_path=${iter_gds}" \
                    -rd "original_script_path=${original_script}" \
                    -rd "modified_script_path=${agent_output}" \
                    -rd "design_type=${design_type}" \
                || echo "  WARNING: Sanity check failed for iter ${iter}."
            fi

            # --- Score this iteration ---
            echo "  [Iter ${iter}] Scoring..."
            if [[ -f "${iter_repaired_json}" ]]; then
                python3 "${src_dir}/score_repair.py" \
                    "${golden_report}" \
                    "${iter_repaired_json}" \
                    > "${iter_score_json}"
            elif [[ -f "${iter_lyrpt}" ]]; then
                python3 "${src_dir}/score_repair.py" \
                    "${golden_report}" \
                    "${iter_lyrpt}" \
                    > "${iter_score_json}"
            else
                echo '{"repair_rate":0,"new_violation_rate":"inf","original_violations":0,"final_violations":0,"removed_violations":0,"new_violations":0,"original_rules_violated":0,"final_rules_violated":0}' > "${iter_score_json}"
            fi

            # --- Connectivity check (after scoring) ---
            connectivity_json_path=""
            if [[ "${design_type}" == "cell" || "${design_type}" == "block" ]]; then
                echo "  [Iter ${iter}] Checking connectivity..."
                golden_json="${original_script/\/layout_script\//\/connectivity\/}"
                golden_json="${golden_json%.py}.json"
                python3 "${src_dir}/check_connectivity.py" \
                    "${golden_json}" \
                    "${agent_output}" \
                    "${design_type}" \
                    > "${iter_connectivity_json}" || true
                connectivity_json_path="${iter_connectivity_json}"
            fi

            # Merge connectivity fields into iter score
            if [[ -n "${connectivity_json_path}" && -f "${connectivity_json_path}" ]]; then
                python3 "${src_dir}/merge_score_connectivity.py" \
                    "${iter_score_json}" "${connectivity_json_path}"
            fi

            # --- Unify per-iteration result ---
            python3 "${src_dir}/unify_iteration_score.py" \
                "${iter_score_json}" "${connectivity_json_path}" \
                "${design_type}" "${iter}" "${agent_runtime_seconds}"

            echo "  [Iter ${iter}] Score saved: ${iter_score_json}"

        ) || {
            # Subshell failed — write placeholder using real agent runtime if available
            iter_success=false
            iter_rt_file="${iter_temp_dir}/.iter${iter}_agent_rt"
            fail_rt=0
            if [[ -f "${iter_rt_file}" ]]; then
                fail_rt=$(cat "${iter_rt_file}")
            fi
            echo "WARNING: Iteration ${iter} failed."
            echo "{\"iteration\": ${iter}, \"final_violations\": 999999, \"connectivity_preserved\": false, \"repair_rate\": 0, \"runtime_seconds\": ${fail_rt}}" > "${iter_score_json}"
        }

        # --- Update cumulative agent time (timer resumes tracking) ---
        # Read agent runtime from the persisted file (written before KLayout/scoring)
        iter_rt_file="${iter_temp_dir}/.iter${iter}_agent_rt"
        if [[ -f "${iter_rt_file}" ]]; then
            iter_agent_rt=$(cat "${iter_rt_file}")
        else
            iter_agent_rt="0"
        fi
        cumulative_agent_seconds=$(python3 "${src_dir}/shell_math.py" --op add "${cumulative_agent_seconds}" "${iter_agent_rt}")
        echo "  Cumulative agent time: ${cumulative_agent_seconds}s / ${initial_budget}s"

        # --- Check if reminder was triggered (budget exhausted) ---
        if [[ "${reminder_triggered}" == "true" ]]; then
            echo "  Reminder iteration complete. No further iterations."
            break
        fi

        budget_exceeded=$(python3 "${src_dir}/shell_math.py" --op gte "${cumulative_agent_seconds}" "${initial_budget}")
        if [[ "${budget_exceeded}" == "yes" ]]; then
            echo "  Agent time budget exhausted (${cumulative_agent_seconds}s >= ${initial_budget}s)."
            echo "  Reminder was sent during this iteration. No further iterations."
            reminder_triggered=true
            # Don't break yet — the current iteration's results are valid
        fi

        # --- Check break condition ---
        # Polygon: break when DRC-clean.
        # Cell/block: break when DRC-clean AND connectivity preserved.
        if [[ -f "${iter_score_json}" ]]; then
            remaining=$(python3 "${src_dir}/read_score_field.py" "${iter_score_json}" final_violations --default 999999)
            conn_ok=$(python3 "${src_dir}/read_score_field.py" "${iter_score_json}" connectivity_preserved --default False)

            if [[ "${remaining}" == "0" ]]; then
                if [[ "${design_type}" == "polygon" ]]; then
                    echo "  All violations repaired (polygon). Stopping at iteration ${iter}."
                    break
                elif [[ "${conn_ok}" == "True" ]]; then
                    echo "  All violations repaired + connectivity preserved. Stopping at iteration ${iter}."
                    break
                else
                    echo "  All violations repaired but connectivity broken. Continuing to seek connectivity-preserving repair."
                fi
            fi
        fi

        # Break after reminder (checked after scoring so results are captured)
        if [[ "${reminder_triggered}" == "true" ]]; then
            break
        fi

        echo ""
    done

    # ===================================================================
    # Best-iteration selection (Showstopper 3)
    # ===================================================================
    echo "[Step 6] Selecting best iteration..."

    python3 "${src_dir}/select_best_iteration.py" \
        "${score_dir}" "${case_name}" "${actual_iterations}" \
        --budget "${initial_budget}"

    score_json="${score_dir}/${case_name}_score_${budget_suffix}.json"

    # Copy best iteration artifacts as the canonical "repaired" output
    best_iter=$(python3 "${src_dir}/read_score_field.py" "${score_json}" best_iteration --default 1)

    echo "  Best iteration: ${best_iter}"

    # Copy best iteration's DRC reports from temp/ to result_dir/ as final output
    best_lyrpt="${iter_temp_dir}/${case_name}_iter${best_iter}.lyrpt"
    best_drc_json="${iter_temp_dir}/${case_name}_iter${best_iter}.drc.json"
    if [[ -f "${best_lyrpt}" ]]; then
        cp "${best_lyrpt}" "${result_dir}/${case_name}_repaired_${budget_suffix}.lyrpt"
        echo "  Final .lyrpt: ${result_dir}/${case_name}_repaired_${budget_suffix}.lyrpt"
    fi
    if [[ -f "${best_drc_json}" ]]; then
        cp "${best_drc_json}" "${result_dir}/${case_name}_repaired_${budget_suffix}.drc.json"
        echo "  Final .drc.json: ${result_dir}/${case_name}_repaired_${budget_suffix}.drc.json"
    fi

    score_csv="${score_dir}/${case_name}_score_${budget_suffix}.csv"
    write_score_csv "${score_json}" "${score_csv}" "${case_name}"

    agent_runtime_seconds=$(python3 "${src_dir}/read_score_field.py" "${score_json}" total_runtime_seconds --default 0)

else

    # ===================================================================
    # DETECTION: single-shot (no iteration loop)
    # ===================================================================

    if [[ "${phase}" != "score" ]]; then
        # ----- Agent phase -----
        echo "[Step 2] Calling LLM agent..."

        agent_start="$(date +%s%N)"

        agent_stderr_tmp="$(mktemp)"
        python3 "${AGENT_SCRIPT}" \
            "${formatted_prompt_path}" \
            "${agent_output}" \
            --model "${model_name}" \
            --task_type "${task_type}" \
            --temp_dir "${temp_dir}" \
            --reminder_prompt_file "${formatted_reminder_path}" \
            ${claude_effort:+--effort "${claude_effort}"} \
            2>"${agent_stderr_tmp}" \
        || {
            cat "${agent_stderr_tmp}" >&2
            echo "  WARNING: Agent failed for model=${model_name}. Skipping." >&2
            rm -f "${agent_stderr_tmp}"
            exit 1
        }

        cat "${agent_stderr_tmp}" >&2

        agent_end="$(date +%s%N)"
        agent_runtime_ns=$(( agent_end - agent_start ))
        agent_runtime_seconds=$(python3 "${src_dir}/shell_math.py" --op div "${agent_runtime_ns}" 1000000000)

        reported_runtime="$(grep -oP 'RUNTIME_SECONDS=\K[0-9.]+' "${agent_stderr_tmp}" | tail -1 || true)"
        if [[ -n "${reported_runtime}" ]]; then
            agent_runtime_seconds="${reported_runtime}"
        fi
        rm -f "${agent_stderr_tmp}"

        echo "  Agent output    : ${agent_output}"
        echo "  Agent runtime   : ${agent_runtime_seconds}s"
        echo ""

        # Persist agent runtime for score-only phase
        echo "${agent_runtime_seconds}" > "${result_dir}/.agent_runtime_${budget_suffix}"
    fi

    if [[ "${phase}" == "agent" ]]; then
        # Agent-only mode: stop here
        echo "  Agent-only phase complete. Exiting."
        # Clean up temp
        if [[ -d "${temp_dir}" ]]; then
            rm -rf "${temp_dir}"
        fi
        exit 0
    fi

    # ----- Score phase -----

    # Re-locate golden report (may have been injected after agent phase)
    if [[ -z "${golden_report}" || ! -f "${golden_report}" ]]; then
        golden_json="${case_testcase_dir}/drc_report/${case_name}.drc.json"
        golden_lyrpt="${case_testcase_dir}/drc_report/${case_name}.lyrpt"
        if [[ -f "${golden_json}" ]]; then
            golden_report="${golden_json}"
        elif [[ -f "${golden_lyrpt}" ]]; then
            golden_report="${golden_lyrpt}"
        fi
    fi

    if [[ -z "${golden_report}" || ! -f "${golden_report}" ]]; then
        echo "ERROR: Golden DRC report not found for ${case_name}. Cannot score." >&2
        exit 1
    fi

    # Recover agent runtime from persisted file (score-only mode)
    if [[ "${phase}" == "score" ]]; then
        if [[ -f "${result_dir}/.agent_runtime_${budget_suffix}" ]]; then
            agent_runtime_seconds=$(cat "${result_dir}/.agent_runtime_${budget_suffix}")
        else
            echo "WARNING: No agent runtime found. Using 0." >&2
            agent_runtime_seconds="0"
        fi
    fi

    llm_detection="${agent_output}"

    echo "[Step 3] Scoring detection results..."
    score_json="${score_dir}/${case_name}_score_${budget_suffix}.json"

    # Score against golden .drc.json (preferred) or .lyrpt fallback
    python3 "${src_dir}/score_detection.py" \
        "${llm_detection}" \
        "${golden_report}" \
        > "${score_json}"

    score_csv="${score_dir}/${case_name}_score_${budget_suffix}.csv"
    write_score_csv "${score_json}" "${score_csv}" "${case_name}"

fi

# ---------------------------------------------------------------------------
# 8. Append runtime_seconds to score JSON
# ---------------------------------------------------------------------------
total_runtime_seconds="${SECONDS}"
python3 "${src_dir}/append_runtime.py" \
    "${score_json}" "${agent_runtime_seconds}" "${total_runtime_seconds}"

# ---------------------------------------------------------------------------
# 9. Append to logs/runtime.csv
# ---------------------------------------------------------------------------
log_dir="${workspace}/logs"
mkdir -p "${log_dir}"
runtime_csv="${log_dir}/runtime.csv"
timestamp_now="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

python3 "${src_dir}/log_runtime.py" \
    "${runtime_csv}" "${model_name}" "${task_type}" "${design_type}" \
    "${case_name}" "${agent_runtime_seconds}" "${total_runtime_seconds}" \
    "${initial_budget}" "${timestamp_now}"

echo "  Score: ${score_json}"
echo ""

# ---------------------------------------------------------------------------
# 10. Clean up temp directory
# ---------------------------------------------------------------------------
if [[ -d "${temp_dir}" ]]; then
    rm -rf "${temp_dir}"
    echo "  Temp directory cleaned: ${temp_dir}"
fi

echo "============================================="
echo "  Pipeline complete"
echo "  Model  : ${model_name}"
echo "  Case   : ${case_name}"
echo "  Results: ${result_dir}/"
echo "  Scores : ${workspace}/score/${model_name}/${design_type}/${task_type}/"
echo "============================================="
