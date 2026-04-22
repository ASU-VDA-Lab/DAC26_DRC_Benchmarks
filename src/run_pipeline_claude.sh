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
# Effort + run identifier (run_id = "${model_name}-${claude_effort}" so
# different effort tiers produce distinct output folders / files).
# ---------------------------------------------------------------------------
claude_effort="${CLAUDE_EFFORT:-}"
if [[ -z "${claude_effort}" ]]; then
    echo "Error: CLAUDE_EFFORT env var is required (e.g. 'medium', 'high')." >&2
    exit 1
fi
run_id="${model_name}-${claude_effort}"

# ---------------------------------------------------------------------------
# Log all stdout+stderr to a file while still printing to the terminal
# ---------------------------------------------------------------------------
log_dir="${workspace}/logs"
mkdir -p "${log_dir}"
log_file="${log_dir}/${run_id}_${design_type}_${task_type}_${case_name}.log"
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
# 3. Agent script (Claude Code CLI)
# ---------------------------------------------------------------------------
AGENT_SCRIPT="${src_dir}/agent_claude.py"

echo "============================================="
echo "  DRC Benchmark Pipeline (KLayout)"
echo "============================================="
echo "  task_type   : ${task_type}"
echo "  model_name  : ${model_name}"
echo "  case_name   : ${case_name}"
echo "  design_type : ${design_type}"
echo "  phase       : ${phase}"
echo "  workspace   : ${workspace}"
echo "  effort      : ${claude_effort}"
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
result_dir="${workspace}/result/${run_id}/${design_type}/${task_type}/${case_name}"
score_dir="${workspace}/score/${run_id}/${design_type}/${task_type}"
temp_dir="${workspace}/temp/${run_id}_${design_type}_${task_type}_${case_name}_$$"
mkdir -p "${result_dir}" "${score_dir}" "${temp_dir}"

if [[ "${task_type}" == "repair" ]]; then
    agent_output="${result_dir}/${case_name}_repaired.py"
else
    agent_output="${result_dir}/${case_name}_detection.json"
fi

# ---------------------------------------------------------------------------
# 5. Format prompt (build processed info.json with container paths)
# ---------------------------------------------------------------------------
echo "[Step 1] Formatting prompt..."

task_dir="${workspace}/task/${run_id}/${design_type}/${task_type}"
mkdir -p "${task_dir}"

case_info_json="${task_dir}/${case_name}_info.json"

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
    --task_type "${task_type}"

formatted_prompt_path="${task_dir}/${case_name}_${task_type}_prompt.md"

python3 "${src_dir}/prompt_format.py" \
    "${case_info_json}" \
    "${prompt_template}" \
    > "${formatted_prompt_path}"

echo "  Formatted prompt: ${formatted_prompt_path}"
echo ""

# ---------------------------------------------------------------------------
# 6. Run agent and downstream processing
# ---------------------------------------------------------------------------
original_script="${case_testcase_dir}/layout_script/${case_name}.py"

# Default values for agent meta (overwritten after agent call)
agent_status="fail"
agent_runtime_seconds="0"
tokens_json='{"input_tokens":0,"output_tokens":0,"cache_read_tokens":0,"cache_write_tokens":0}'

if [[ "${task_type}" == "repair" ]]; then

    # ===================================================================
    # REPAIR: single agent call, no iteration loop
    # ===================================================================
    echo "[Step 2] Calling LLM agent (single call, no timeout)..."

    agent_stderr_tmp="$(mktemp)"
    python3 "${AGENT_SCRIPT}" \
        "${formatted_prompt_path}" \
        "${agent_output}" \
        --model "${model_name}" \
        --task_type "repair" \
        --temp_dir "${temp_dir}" \
        --fallback "${original_script}" \
        --raw-json-out "${score_dir}/${case_name}_agent_raw.json" \
        ${claude_effort:+--effort "${claude_effort}"} \
        2>"${agent_stderr_tmp}" || true
    cat "${agent_stderr_tmp}" >&2

    agent_status="$(grep -oP 'STATUS=\K(success|fail)' "${agent_stderr_tmp}" | tail -1 || echo fail)"
    tokens_json="$(grep -oP 'TOKENS_JSON=\K.*' "${agent_stderr_tmp}" | tail -1 || echo '{"input_tokens":0,"output_tokens":0,"cache_read_tokens":0,"cache_write_tokens":0}')"
    agent_runtime_seconds="$(grep -oP 'RUNTIME_SECONDS=\K[0-9.]+' "${agent_stderr_tmp}" | tail -1 || echo 0)"
    rm -f "${agent_stderr_tmp}"

    echo "  Agent output  : ${agent_output}"
    echo "  Agent status  : ${agent_status}"
    echo "  Agent runtime : ${agent_runtime_seconds}s"
    echo ""

    # --- Render GDS ---
    echo "[Step 3] Rendering GDS..."
    render_script="${temp_dir}/${case_name}_render.py"
    gds_path="${temp_dir}/${case_name}.gds"
    lyrpt_path="${temp_dir}/${case_name}.lyrpt"
    drc_json_path="${temp_dir}/${case_name}.drc.json"

    python3 "${src_dir}/prepare_render_script.py" \
        "${agent_output}" "${render_script}" "${gds_path}"
    klayout -b -r "${render_script}" || echo "WARNING: KLayout render failed."

    # --- KLayout DRC ---
    if [[ "${SKIP_DRC:-0}" != "1" ]]; then
        echo "[Step 4] Running KLayout DRC..."
        python3 "${src_dir}/run_klayout_drc.py" "${gds_path}" "${design_rule}" "${lyrpt_path}" || true
        if [[ -f "${lyrpt_path}" ]]; then
            python3 "${src_dir}/process_klayout_reports.py" \
                --lyrpt "${lyrpt_path}" \
                --output "${drc_json_path}" \
                --case_name "${case_name}" \
                --design_type "${design_type}" \
                --layout-script "${agent_output}" || true
        fi
    fi

    # --- Sanity + Connectivity checks ---
    sanity_json_path="${temp_dir}/${case_name}_sanity.json"
    connectivity_json=""
    if [[ -f "${src_dir}/sanity_check.py" ]]; then
        echo "[Step 5] Running sanity check..."
        klayout -b -r "${src_dir}/sanity_check.py" \
            -rd "original_gds_path=${case_testcase_dir}/gds/${case_name}.gds" \
            -rd "modified_gds_path=${gds_path}" \
            -rd "original_script_path=${original_script}" \
            -rd "modified_script_path=${agent_output}" \
            -rd "design_type=${design_type}" \
            -rd "sanity_json_out=${sanity_json_path}" \
            || echo "WARNING: Sanity check failed."
    fi

    if [[ "${design_type}" == "cell" || "${design_type}" == "block" ]]; then
        echo "[Step 5] Checking connectivity (cell/block only)..."
        golden_conn_json="${original_script/\/layout_script\//\/connectivity\/}"
        golden_conn_json="${golden_conn_json%.py}.json"
        connectivity_json="${temp_dir}/${case_name}_connectivity.json"
        python3 "${src_dir}/check_connectivity.py" \
            "${golden_conn_json}" "${agent_output}" "${design_type}" \
            > "${connectivity_json}" || true
    fi

    # --- Score ---
    echo "[Step 6] Scoring..."
    score_json="${score_dir}/${case_name}_score.json"
    if [[ -f "${drc_json_path}" ]]; then
        repaired_arg="${drc_json_path}"
    elif [[ -f "${lyrpt_path}" ]]; then
        repaired_arg="${lyrpt_path}"
    else
        repaired_arg=""
    fi

    python3 "${src_dir}/score_repair.py" \
        "${golden_report}" \
        "${repaired_arg}" \
        --agent-status "${agent_status}" \
        --tokens-json "${tokens_json}" \
        --agent-runtime-seconds "${agent_runtime_seconds}" \
        > "${score_json}"

    # --- Merge check results into score ---
    if [[ -f "${sanity_json_path}" ]]; then
        echo "[Step 6.5] Merging sanity check into score..."
        python3 "${src_dir}/merge_score_sanity.py" \
            "${score_json}" "${sanity_json_path}" || true
    fi
    if [[ -n "${connectivity_json}" && -f "${connectivity_json}" ]]; then
        echo "[Step 6.5] Merging connectivity into score..."
        python3 "${src_dir}/merge_score_connectivity.py" \
            "${score_json}" "${connectivity_json}" || true
    fi

    # --- Write CSV ---
    score_csv="${score_dir}/${case_name}_score.csv"
    write_score_csv "${score_json}" "${score_csv}" "${case_name}"

else

    # ===================================================================
    # DETECTION: agent-only / score-only two-phase flow
    # ===================================================================
    meta_file="${result_dir}/.agent_meta.json"

    if [[ "${phase}" != "score" ]]; then
        # ----- Agent phase -----
        echo "[Step 2] Calling LLM agent (detection, single call, no timeout)..."

        agent_stderr_tmp="$(mktemp)"
        python3 "${AGENT_SCRIPT}" \
            "${formatted_prompt_path}" \
            "${agent_output}" \
            --model "${model_name}" \
            --task_type "detection" \
            --temp_dir "${temp_dir}" \
            --raw-json-out "${score_dir}/${case_name}_agent_raw.json" \
            ${claude_effort:+--effort "${claude_effort}"} \
            2>"${agent_stderr_tmp}" || true
        cat "${agent_stderr_tmp}" >&2

        agent_status="$(grep -oP 'STATUS=\K(success|fail)' "${agent_stderr_tmp}" | tail -1 || echo fail)"
        tokens_json="$(grep -oP 'TOKENS_JSON=\K.*' "${agent_stderr_tmp}" | tail -1 || echo '{"input_tokens":0,"output_tokens":0,"cache_read_tokens":0,"cache_write_tokens":0}')"
        agent_runtime_seconds="$(grep -oP 'RUNTIME_SECONDS=\K[0-9.]+' "${agent_stderr_tmp}" | tail -1 || echo 0)"
        rm -f "${agent_stderr_tmp}"

        echo "  Agent output  : ${agent_output}"
        echo "  Agent status  : ${agent_status}"
        echo "  Agent runtime : ${agent_runtime_seconds}s"
        echo ""

        # Persist agent meta for --score-only phase
        python3 -c 'import json,sys; d={"agent_status":sys.argv[1],"agent_runtime_seconds":float(sys.argv[2]),"tokens":json.loads(sys.argv[3])}; print(json.dumps(d))' \
            "${agent_status}" "${agent_runtime_seconds}" "${tokens_json}" > "${meta_file}"
    fi

    if [[ "${phase}" == "agent" ]]; then
        echo "  Agent-only phase complete."
        [[ -d "${temp_dir}" ]] && rm -rf "${temp_dir}"
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

    # Recover meta for score-only mode
    if [[ -f "${meta_file}" ]]; then
        agent_status="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["agent_status"])' "${meta_file}")"
        agent_runtime_seconds="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["agent_runtime_seconds"])' "${meta_file}")"
        tokens_json="$(python3 -c 'import json,sys; print(json.dumps(json.load(open(sys.argv[1]))["tokens"]))' "${meta_file}")"
    fi

    echo "[Step 3] Scoring detection results..."
    score_json="${score_dir}/${case_name}_score.json"

    python3 "${src_dir}/score_detection.py" \
        "${agent_output}" \
        "${golden_report}" \
        --agent-status "${agent_status}" \
        --tokens-json "${tokens_json}" \
        --agent-runtime-seconds "${agent_runtime_seconds}" \
        > "${score_json}"

    score_csv="${score_dir}/${case_name}_score.csv"
    write_score_csv "${score_json}" "${score_csv}" "${case_name}"

fi

# ---------------------------------------------------------------------------
# 7. Append to logs/runtime.csv
# ---------------------------------------------------------------------------
log_dir="${workspace}/logs"
mkdir -p "${log_dir}"
runtime_csv="${log_dir}/runtime.csv"
timestamp_now="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

python3 "${src_dir}/log_runtime.py" \
    "${runtime_csv}" \
    "${model_name}" "${claude_effort}" "${task_type}" "${design_type}" "${case_name}" \
    "${agent_status}" \
    "${agent_runtime_seconds}" \
    "${tokens_json}" \
    "${timestamp_now}"

echo "  Score: ${score_json}"
echo ""

# ---------------------------------------------------------------------------
# 8. Clean up temp directory
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
echo "  Scores : ${workspace}/score/${run_id}/${design_type}/${task_type}/"
echo "============================================="
