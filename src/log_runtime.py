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
# Append a row to the runtime CSV log.
#
# Usage:
#     python3 src/log_runtime.py <csv_path> <model> <task_type> <design_type> \
#         <case_name> <agent_runtime> <total_runtime> <agent_initial_budget> <timestamp>

import csv
import os
import sys


FIELDNAMES = [
    "model", "task_type", "design_type", "case_name",
    "agent_runtime_seconds", "total_runtime_seconds",
    "agent_initial_budget", "timestamp",
]


def main():
    if len(sys.argv) != 10:
        print(
            "Usage: python3 log_runtime.py <csv_path> <model> <task_type> "
            "<design_type> <case_name> <agent_runtime> <total_runtime> "
            "<agent_initial_budget> <timestamp>",
            file=sys.stderr,
        )
        sys.exit(1)

    (csv_path, model, task_type, design_type, case_name,
     agent_rt, total_rt, agent_budget, ts) = sys.argv[1:]

    write_header = not os.path.exists(csv_path)

    with open(csv_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "model": model,
            "task_type": task_type,
            "design_type": design_type,
            "case_name": case_name,
            "agent_runtime_seconds": agent_rt,
            "total_runtime_seconds": total_rt,
            "agent_initial_budget": agent_budget,
            "timestamp": ts,
        })

    print(f"  Runtime logged: {csv_path}")


if __name__ == "__main__":
    main()
