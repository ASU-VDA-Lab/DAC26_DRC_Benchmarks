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
# Select the best iteration from per-iteration score files, write final score JSON.
#
# Usage:
#     python3 src/select_best_iteration.py <score_dir> <case_name> <total_iterations> [--budget <B>]
#
# With --budget <B>, the per-iteration and final score files are named with an
# extra budget suffix:
#     <case>_score_<B>_iter<N>.json      (per-iteration)
#     <case>_score_<B>.json              (final best)

import argparse
import json
import os
import sys


def _iter_path(score_dir, case_name, n, budget):
    if budget is not None:
        return os.path.join(score_dir, f"{case_name}_score_{budget}_iter{n}.json")
    return os.path.join(score_dir, f"{case_name}_score_iter{n}.json")


def _final_path(score_dir, case_name, budget):
    if budget is not None:
        return os.path.join(score_dir, f"{case_name}_score_{budget}.json")
    return os.path.join(score_dir, f"{case_name}_score.json")


def main():
    parser = argparse.ArgumentParser(
        description="Select best iteration from per-iteration score files.")
    parser.add_argument("score_dir")
    parser.add_argument("case_name")
    parser.add_argument("total_iterations", type=int)
    parser.add_argument("--budget", default=None,
                        help="Agent initial budget suffix on iteration score filenames.")
    args = parser.parse_args()

    score_dir = args.score_dir
    case_name = args.case_name
    total_iters = args.total_iterations
    budget = args.budget

    results = []
    for n in range(1, total_iters + 1):
        path = _iter_path(score_dir, case_name, n, budget)
        if os.path.isfile(path):
            with open(path) as f:
                results.append(json.load(f))

    if not results:
        best = {"repair_rate": 0, "final_violations": 999999, "connectivity_preserved": False}
        best_idx = 0
    else:
        # Sort: connectivity_preserved=True first, then lowest final_violations, then lowest iteration
        results.sort(key=lambda r: (
            0 if r.get("connectivity_preserved") else 1,
            r.get("final_violations", 999999),
            r.get("iteration", 999)
        ))
        best = results[0]
        best_idx = best.get("iteration", 1)

    # Build final score with iteration history
    history = []
    for n in range(1, total_iters + 1):
        path = _iter_path(score_dir, case_name, n, budget)
        if os.path.isfile(path):
            with open(path) as f:
                d = json.load(f)
            history.append({
                "iteration": d.get("iteration", n),
                "final_violations": d.get("final_violations", 0),
                "repair_rate": d.get("repair_rate", 0),
                "new_violation_rate": d.get("new_violation_rate", 0),
                "connectivity_preserved": d.get("connectivity_preserved", False),
                "runtime_seconds": d.get("runtime_seconds", 0),
            })

    best["best_iteration"] = best_idx
    best["iteration_used"] = total_iters
    best["iteration_history"] = history
    # Sum all iteration runtimes
    best["total_runtime_seconds"] = sum(h.get("runtime_seconds", 0) for h in history)

    out_path = _final_path(score_dir, case_name, budget)
    with open(out_path, "w") as f:
        json.dump(best, f, indent=2)
    print(f"Best iteration: {best_idx}, total iterations: {total_iters}")


if __name__ == "__main__":
    main()
