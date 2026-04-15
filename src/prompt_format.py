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
import json
import re
import sys


ALLOWED_KEYS = {
    "model_name",
    "case_name",
    "task_type",
    "path_to_skill",
    "path_to_layout_script",
    "path_to_layout_screenshot",
    "path_to_drc_report",
    "path_to_design_rule",
    "path_to_drm_jpg",
    "path_to_connectivity_file",
    "output_path",
    "temp_dir",
    "agent_initial_budget",
    "agent_reminder_budget",
}


def prompt_format(info_json_path: str, prompt_md_path: str) -> str:
    # Read info.json and prompt.md, validate placeholders, and return the formatted string.
    #
    # Args:
    #     info_json_path: Path to the info.json file containing key/value substitutions.
    #     prompt_md_path: Path to the prompt markdown template file.
    #
    # Returns:
    #     The formatted prompt string with all placeholders replaced by their values.
    #
    # Raises:
    #     ValueError: If any placeholder found in the template is not in ALLOWED_KEYS.
    with open(info_json_path, "r", encoding="utf-8") as f:
        info = json.load(f)

    with open(prompt_md_path, "r", encoding="utf-8") as f:
        template = f.read()

    found_keys = re.findall(r'\{(\w+)\}', template)

    invalid_keys = [key for key in found_keys if key not in ALLOWED_KEYS]
    if invalid_keys:
        raise ValueError(
            f"The following placeholder(s) in the prompt template are not allowed: "
            f"{invalid_keys}. Allowed keys are: {sorted(ALLOWED_KEYS)}"
        )

    result = template
    for key in found_keys:
        value = info.get(key, "")
        result = result.replace(f"{{{key}}}", str(value))

    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <info_json_path> <prompt_md_path>")
        sys.exit(1)

    info_json_path = sys.argv[1]
    prompt_md_path = sys.argv[2]

    formatted = prompt_format(info_json_path, prompt_md_path)
    print(formatted)
