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
# evaluate_cursor.sh -- Batch experiment runner for reproducing the paper's results
#
# Iterates over task_type × model_name × (case_name, design_type) and runs
# the full Docker-based pipeline for each combination sequentially.
#
# This script is used to reproduce the experiment table in the paper.
# To run a single case, use run_pipeline_cursor.sh with your own info.json instead.
#
# IMPORTANT: Run this script from the DAC26_DRC_Benchmarks/ project root:
#   cd DAC26_DRC_Benchmarks/
#   bash src/evaluate_cursor.sh
#
# Prerequisites:
#   - Two Docker images must be built first:
#       docker build -f Dockerfile.repair    -t drc-benchmark-repair    .
#       docker build -f Dockerfile.detection -t drc-benchmark-detection .
#     (Detection uses a locked-down image with no KLayout and an iptables
#     blocklist to prevent the agent from installing / invoking KLayout.)
#   - Cursor CLI must be logged in on the host:
#       curl https://cursor.com/install -fsS | bash
#       cursor login

set -euo pipefail

# ===========================================================================
# Configuration -- edit these lists to control which runs to execute
# ===========================================================================

TASK_TYPES=(
    repair
    detection
)

MODEL_NAMES=(
    claude-4.6-opus-high
    claude-4.6-sonnet-medium
    gpt-5.4-high
    gemini-3.1-pro
    grok-4-20
    kimi-k2.5
)

CASES=(
    "Polygon69 polygon"
    "Polygon263 polygon"
    "Cell1 cell"
    "Cell228 cell"
    "Block5 block"
    "Block7 block"
)

# ===========================================================================
# Main loop
# ===========================================================================

# Docker images:
#   - drc-benchmark-detection : no klayout, runtime iptables blocklist (prevents
#                               the detection agent from invoking / installing
#                               klayout to leak the golden DRC answer).
#   - drc-benchmark-repair    : full klayout image (repair legitimately runs
#                               KLayout DRC to verify its own output).
DETECTION_IMAGE="${DETECTION_IMAGE:-drc-benchmark-detection}"
REPAIR_IMAGE="${REPAIR_IMAGE:-drc-benchmark-repair}"
host_dir="$(pwd)"
testcase_base="${host_dir}/testcase/asap7"
skill_file="${host_dir}/src/skill.md"

total=${#TASK_TYPES[@]}*${#MODEL_NAMES[@]}*${#CASES[@]}
run_idx=0

for task_type in "${TASK_TYPES[@]}"; do
    for model_name in "${MODEL_NAMES[@]}"; do
        for case_entry in "${CASES[@]}"; do

            # Extract case_name and design_type from the pair
            case_name="${case_entry%% *}"
            design_type="${case_entry##* }"

            run_idx=$((run_idx + 1))
            echo ""
            echo "=========================================================="
            echo "  Run ${run_idx}: ${task_type} | ${model_name} | ${case_name} (${design_type})"
            echo "=========================================================="

            # Validate design_type
            if [[ "${design_type}" != "cell" && "${design_type}" != "polygon" && "${design_type}" != "block" ]]; then
                echo "ERROR: Invalid design_type '${design_type}' for case '${case_name}'. Skipping." >&2
                continue
            fi

            # -----------------------------------------------------------------
            # Host paths
            # -----------------------------------------------------------------
            case_testcase_dir="${testcase_base}/${design_type}"

            if [[ "${design_type}" == "cell" ]]; then
                design_rule="${testcase_base}/asap7_cell.lydrc"
            else
                design_rule="${testcase_base}/asap7.lydrc"
            fi

            # Golden DRC report
            golden_json="${case_testcase_dir}/drc_report/${case_name}.drc.json"
            golden_lyrpt="${case_testcase_dir}/drc_report/${case_name}.lyrpt"
            if [[ -f "${golden_json}" ]]; then
                golden_report="${golden_json}"
            elif [[ -f "${golden_lyrpt}" ]]; then
                golden_report="${golden_lyrpt}"
            else
                echo "WARNING: Golden DRC report not found for ${case_name} at ${case_testcase_dir}/drc_report/" >&2
                golden_report=""
            fi

            # -----------------------------------------------------------------
            # Generate info.json on the host
            # -----------------------------------------------------------------
            info_dir="${host_dir}/temp/info"
            mkdir -p "${info_dir}"
            info_json="${info_dir}/${model_name}_${design_type}_${task_type}_${case_name}.json"

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
                --temp_dir "temp/${model_name}_${design_type}_${task_type}_${case_name}" \
                --json_output_path "${info_json}"

            echo "Generated info.json: ${info_json}"

            # -----------------------------------------------------------------
            # Docker container setup
            # -----------------------------------------------------------------
            container_name="drc-${model_name}-${design_type}-${task_type}-${case_name}-$$"
            container_name=$(echo "${container_name}" | tr -c 'a-zA-Z0-9_.-' '-')

            # Pick image + extra flags by task_type.  Detection container has
            # no klayout and an iptables blocklist; the entrypoint needs
            # NET_ADMIN to install the blocklist at start.
            if [[ "${task_type}" == "detection" ]]; then
                IMAGE_TO_USE="${DETECTION_IMAGE}"
                EXTRA_DOCKER_FLAGS=("--cap-add=NET_ADMIN")
            else
                IMAGE_TO_USE="${REPAIR_IMAGE}"
                EXTRA_DOCKER_FLAGS=()
            fi

            echo "Creating container: ${container_name} (image=${IMAGE_TO_USE})"

            docker create \
                --name "${container_name}" \
                "${EXTRA_DOCKER_FLAGS[@]}" \
                -v "${HOME}/.config/cursor/auth.json:/root/.config/cursor/auth.json:ro" \
                -v "${host_dir}/result:/workspace/result" \
                -v "${host_dir}/score:/workspace/score" \
                -v "${host_dir}/logs:/workspace/logs" \
                -v "${host_dir}/temp:/workspace/temp" \
                "${IMAGE_TO_USE}" \
                sleep infinity > /dev/null

            docker start "${container_name}" > /dev/null

            # -----------------------------------------------------------------
            # Copy info.json into container
            # -----------------------------------------------------------------
            docker cp "${info_json}" "${container_name}:/workspace/task/info.json"

            # -----------------------------------------------------------------
            # Run pipeline (flow depends on task type)
            # -----------------------------------------------------------------
            if [[ "${task_type}" == "repair" ]]; then
                echo "Injecting golden DRC report into container..."
                if [[ -n "${golden_report}" && -f "${golden_report}" ]]; then
                    docker exec "${container_name}" mkdir -p "/workspace/testcase/asap7/${design_type}/drc_report"
                    docker cp "${golden_report}" \
                        "${container_name}:/workspace/testcase/asap7/${design_type}/drc_report/"
                fi

                echo "Running full repair pipeline..."
                docker exec \
                    "${container_name}" \
                    bash src/run_pipeline_cursor.sh /workspace/task/info.json \
                || echo "WARNING: Repair pipeline failed for ${case_name}. Continuing." >&2

            else
                echo "Running agent (detection, no golden report visible)..."
                if docker exec \
                    "${container_name}" \
                    bash src/run_pipeline_cursor.sh --agent-only /workspace/task/info.json; then

                    echo "Injecting golden DRC report into container for scoring..."
                    if [[ -n "${golden_report}" && -f "${golden_report}" ]]; then
                        docker exec "${container_name}" mkdir -p "/workspace/testcase/asap7/${design_type}/drc_report"
                        docker cp "${golden_report}" \
                            "${container_name}:/workspace/testcase/asap7/${design_type}/drc_report/"
                    fi

                    echo "Running scoring phase..."
                    docker exec \
                        "${container_name}" \
                        bash src/run_pipeline_cursor.sh --score-only /workspace/task/info.json \
                    || echo "WARNING: Scoring failed for ${case_name}. Continuing." >&2
                else
                    echo "WARNING: Agent failed for ${case_name}, skipping scoring. Continuing." >&2
                fi
            fi

            echo "  Results : result/${model_name}/${design_type}/${task_type}/${case_name}/"
            echo "  Scores  : score/${model_name}/${design_type}/${task_type}/"

            # -----------------------------------------------------------------
            # Copy task directory (prompts, info.json) from container to host
            # -----------------------------------------------------------------
            mkdir -p "${host_dir}/task"
            docker cp "${container_name}:/workspace/task/" "${host_dir}/task/" 2>/dev/null || true

            # -----------------------------------------------------------------
            # Cleanup container for this iteration
            # -----------------------------------------------------------------
            echo "Cleaning up container: ${container_name}"
            docker stop "${container_name}" > /dev/null 2>&1 || true
            docker kill "${container_name}" > /dev/null 2>&1 || true
            docker rm "${container_name}" > /dev/null 2>&1 || true

        done
    done
done

echo ""
echo "=========================================================="
echo "  All runs complete."
echo "=========================================================="
