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
# Add iteration number, runtime, and connectivity status to a per-iteration score JSON.
#
# Usage:
#     python3 src/unify_iteration_score.py <score_json> <connectivity_json> \
#         <design_type> <iteration> <runtime_seconds>
#
# Note: connectivity_json can be empty string "" if not applicable.

import json
import os
import sys


def main():
    if len(sys.argv) != 6:
        print(
            "Usage: python3 unify_iteration_score.py <score_json> <connectivity_json> "
            "<design_type> <iteration> <runtime_seconds>",
            file=sys.stderr,
        )
        sys.exit(1)

    score_path = sys.argv[1]
    conn_path = sys.argv[2]
    design_type = sys.argv[3]
    iteration = int(sys.argv[4])
    runtime_sec = float(sys.argv[5])

    with open(score_path) as f:
        score = json.load(f)

    if design_type == "polygon":
        score["connectivity_preserved"] = True  # always True for polygon
    elif conn_path and conn_path != "" and os.path.isfile(conn_path):
        with open(conn_path) as f:
            conn = json.load(f)
        score["connectivity_preserved"] = conn.get("connectivity_preserved", False)
    else:
        score.setdefault("connectivity_preserved", False)

    score["iteration"] = iteration
    score["runtime_seconds"] = runtime_sec
    score["final_violations"] = score.get("final_violations", sum(
        v for v in score.get("final_violations_per_rule", {}).values()
    ) if "final_violations_per_rule" in score else score.get("final_violations", 0))

    with open(score_path, "w") as f:
        json.dump(score, f, indent=2)


if __name__ == "__main__":
    main()
