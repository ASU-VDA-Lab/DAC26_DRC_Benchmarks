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
# evaluate_claude_parallel.sh -- Parallel Claude Code benchmark runner.
#
# Same semantics as evaluate_claude.sh except:
#   - Adds an AGENT_INITIAL_BUDGET list dimension.
#   - Expands TASK_TYPES x MODEL_NAMES x CASES x AGENT_INITIAL_BUDGET into a
#     job list and executes up to PARALLEL_JOBS jobs concurrently via xargs.
#   - Each job runs its own Docker container; container names and all output
#     filenames include the budget so runs never overwrite each other.
#   - Per-job exit status, runtime, and resulting score file path are
#     collected and summarised at the end.
#
# Prerequisites:
#   - Two Docker images built:
#       docker build -f Dockerfile.repair    -t drc-benchmark-repair    .
#       docker build -f Dockerfile.detection -t drc-benchmark-detection .
#   - Host-side Claude Code CLI logged in (~/.claude populated).
#
# Usage:
#   bash src/evaluate_claude_parallel.sh

set -u  # no -e: individual job failures are tolerated.

# ===========================================================================
# Configuration -- edit these lists to control which runs to execute.
# ===========================================================================

TASK_TYPES=(
    repair
)

MODEL_NAMES=(
    "claude-sonnet-4-6 medium"
    "claude-opus-4-6 high"
)

CASES=(
    "Block1 block"
    "Block2 block"
    "Block3 block"
    "Block4 block"
)

AGENT_INITIAL_BUDGET=(
    # 600   # already run; keep commented so we don't re-overwrite those results.
    1800
)

# Maximum number of docker containers to run simultaneously.
PARALLEL_JOBS="${PARALLEL_JOBS:-2}"

# ===========================================================================
# Docker image selection (matches evaluate_claude.sh).
# ===========================================================================

DETECTION_IMAGE="${DETECTION_IMAGE:-drc-benchmark-detection}"
REPAIR_IMAGE="${REPAIR_IMAGE:-drc-benchmark-repair}"

host_dir="$(pwd)"
testcase_base="${host_dir}/testcase/asap7"
skill_file="${host_dir}/src/skill.md"

# Unique base tag for this orchestrator invocation (used for container names).
orch_pid="$$"

summary_dir=$(mktemp -d)
# Trap EXIT once the job_list also exists (see below after the expansion block).

# ===========================================================================
# Per-job worker -- runs inside an xargs-spawned subshell.
#
# Reads a single tab-separated job spec on stdin:
#   task_type\tmodel_name\tclaude_effort\tcase_name\tdesign_type\tbudget\tcounter
# ===========================================================================

run_one_job() {
    local task_type="$1"
    local model_name="$2"
    local claude_effort="$3"
    local case_name="$4"
    local design_type="$5"
    local budget="$6"
    local counter="$7"

    local t_start=$(date +%s)
    local tag="${task_type}|${model_name}|${case_name}|${design_type}|budget=${budget}"
    local case_testcase_dir="${testcase_base}/${design_type}"

    # --- Basic validation -----------------------------------------------
    if [[ "${design_type}" != "cell" && "${design_type}" != "polygon" && "${design_type}" != "block" ]]; then
        echo "[${tag}] ERROR: Invalid design_type '${design_type}'. Skipping." >&2
        echo "${tag}|SKIPPED|0|-" > "${summary_dir}/${counter}.summary"
        return 0
    fi

    # --- DRC rule file --------------------------------------------------
    local design_rule
    if [[ "${design_type}" == "cell" ]]; then
        design_rule="${testcase_base}/asap7_cell.lydrc"
    else
        design_rule="${testcase_base}/asap7.lydrc"
    fi

    # --- Golden DRC report ---------------------------------------------
    local golden_report=""
    local golden_json="${case_testcase_dir}/drc_report/${case_name}.drc.json"
    local golden_lyrpt="${case_testcase_dir}/drc_report/${case_name}.lyrpt"
    if [[ -f "${golden_json}" ]]; then
        golden_report="${golden_json}"
    elif [[ -f "${golden_lyrpt}" ]]; then
        golden_report="${golden_lyrpt}"
    fi

    # --- Generate per-job info.json on the host ------------------------
    local info_dir="${host_dir}/temp/info"
    mkdir -p "${info_dir}"
    local info_json="${info_dir}/${model_name}_${design_type}_${task_type}_${case_name}_${budget}.json"

    python3 "${host_dir}/src/build_case_info.py" \
        --model_name "${model_name}" \
        --case_name "${case_name}" \
        --design_type "${design_type}" \
        --task_type "${task_type}" \
        --output_path "placeholder" \
        --path_to_layout_script "${case_testcase_dir}/layout_script/${case_name}.py" \
        --path_to_layout_screenshot "${case_testcase_dir}/layout_screenshot/${case_name}/${case_name}.png" \
        --path_to_drc_report "${golden_report}" \
        --path_to_design_rule "${design_rule}" \
        --path_to_drm_jpg "${testcase_base}/drm_jpg" \
        --path_to_skill "${skill_file}" \
        --temp_dir "temp/${model_name}_${design_type}_${task_type}_${case_name}_${budget}" \
        --json_output_path "${info_json}" \
        > /dev/null

    # --- Container selection + flags -----------------------------------
    local image_to_use extra_flags
    if [[ "${task_type}" == "detection" ]]; then
        image_to_use="${DETECTION_IMAGE}"
        extra_flags=("--cap-add=NET_ADMIN")
    else
        image_to_use="${REPAIR_IMAGE}"
        extra_flags=()
    fi

    # --- Unique container name -----------------------------------------
    local container_name="drc-${model_name}-${design_type}-${task_type}-${case_name}-${budget}-${orch_pid}-${counter}"
    container_name=$(echo "${container_name}" | tr -c 'a-zA-Z0-9_.-' '-')

    echo "[${tag}] Starting container ${container_name} (image=${image_to_use})"

    docker create \
        --name "${container_name}" \
        "${extra_flags[@]}" \
        -v "${HOME}/.claude:/root/.claude:ro" \
        -v "${host_dir}/result:/workspace/result" \
        -v "${host_dir}/score:/workspace/score" \
        -v "${host_dir}/logs:/workspace/logs" \
        -v "${host_dir}/task:/workspace/task" \
        "${image_to_use}" \
        sleep infinity > /dev/null \
        || { echo "[${tag}] ERROR: docker create failed"; echo "${tag}|DOCKER_CREATE_FAILED|0|-" > "${summary_dir}/${counter}.summary"; return 0; }

    docker start "${container_name}" > /dev/null 2>&1

    docker cp "${info_json}" "${container_name}:/workspace/task/info.json"

    local exit_code=0
    if [[ "${task_type}" == "repair" ]]; then
        if [[ -n "${golden_report}" && -f "${golden_report}" ]]; then
            docker exec "${container_name}" mkdir -p "/workspace/testcase/asap7/${design_type}/drc_report"
            docker cp "${golden_report}" "${container_name}:/workspace/testcase/asap7/${design_type}/drc_report/"
        fi

        docker exec \
            -e "CLAUDE_EFFORT=${claude_effort}" \
            -e "AGENT_INITIAL_BUDGET=${budget}" \
            "${container_name}" \
            bash src/run_pipeline_claude.sh /workspace/task/info.json \
            || { echo "[${tag}] WARNING: Repair pipeline failed"; exit_code=1; }
    else
        # Detection: agent-only (no golden) -> inject golden -> score-only
        if docker exec \
            -e "CLAUDE_EFFORT=${claude_effort}" \
            -e "AGENT_INITIAL_BUDGET=${budget}" \
            "${container_name}" \
            bash src/run_pipeline_claude.sh --agent-only /workspace/task/info.json; then

            if [[ -n "${golden_report}" && -f "${golden_report}" ]]; then
                docker exec "${container_name}" mkdir -p "/workspace/testcase/asap7/${design_type}/drc_report"
                docker cp "${golden_report}" "${container_name}:/workspace/testcase/asap7/${design_type}/drc_report/"
            fi

            docker exec \
                -e "CLAUDE_EFFORT=${claude_effort}" \
                -e "AGENT_INITIAL_BUDGET=${budget}" \
                "${container_name}" \
                bash src/run_pipeline_claude.sh --score-only /workspace/task/info.json \
                || { echo "[${tag}] WARNING: Scoring failed"; exit_code=1; }
        else
            echo "[${tag}] WARNING: Agent phase failed; skipping scoring."
            exit_code=1
        fi
    fi

    # --- Cleanup container --------------------------------------------
    docker stop "${container_name}" > /dev/null 2>&1 || true
    docker rm   "${container_name}" > /dev/null 2>&1 || true

    # --- Record summary ----------------------------------------------
    local t_end=$(date +%s)
    local elapsed=$((t_end - t_start))
    local score_path="score/${model_name}/${design_type}/${task_type}/${case_name}_score_${budget}.json"
    echo "${tag}|exit=${exit_code}|elapsed=${elapsed}s|score=${score_path}" \
        > "${summary_dir}/${counter}.summary"
    echo "[${tag}] Done (exit=${exit_code}, elapsed=${elapsed}s)"
    return 0
}

export -f run_one_job
export host_dir testcase_base skill_file DETECTION_IMAGE REPAIR_IMAGE
export orch_pid summary_dir

# ===========================================================================
# Expand TASK x MODEL x CASE x BUDGET into a job list.
# ===========================================================================

job_list=$(mktemp)
trap 'rm -f "$job_list"; rm -rf "$summary_dir"' EXIT

counter=0
for task_type in "${TASK_TYPES[@]}"; do
    for model_entry in "${MODEL_NAMES[@]}"; do
        model_name="${model_entry%% *}"
        claude_effort="${model_entry##* }"
        for case_entry in "${CASES[@]}"; do
            case_name="${case_entry%% *}"
            design_type="${case_entry##* }"
            for budget in "${AGENT_INITIAL_BUDGET[@]}"; do
                counter=$((counter + 1))
                # Tab-separated fields: task\tmodel\teffort\tcase\tdesign\tbudget\tcounter
                printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
                    "${task_type}" "${model_name}" "${claude_effort}" \
                    "${case_name}" "${design_type}" "${budget}" "${counter}" \
                    >> "${job_list}"
            done
        done
    done
done

total_jobs="${counter}"

echo "=========================================================="
echo "  Parallel evaluation runner"
echo "  Total jobs     : ${total_jobs}"
echo "  Parallel limit : ${PARALLEL_JOBS}"
echo "  Budgets        : ${AGENT_INITIAL_BUDGET[*]}"
echo "=========================================================="

# xargs -P runs run_one_job in parallel; each line is a tab-separated job spec.
# We split the line on tabs (-d '\t' via IFS) and pass fields as positional args.
< "${job_list}" xargs -d '\n' -I {} -P "${PARALLEL_JOBS}" \
    bash -c '
        IFS=$'\''\t'\'' read -r task_type model_name effort case_name design_type budget counter <<< "$1"
        run_one_job "$task_type" "$model_name" "$effort" "$case_name" "$design_type" "$budget" "$counter"
    ' _ {}

# ===========================================================================
# Summary
# ===========================================================================

echo ""
echo "=========================================================="
echo "  All jobs complete. Per-job summary:"
echo "=========================================================="
if compgen -G "${summary_dir}/*.summary" > /dev/null; then
    cat "${summary_dir}"/*.summary | sort
else
    echo "  (no summary files written)"
fi
echo "=========================================================="
