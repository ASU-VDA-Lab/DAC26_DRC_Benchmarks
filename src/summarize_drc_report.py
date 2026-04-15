#!/usr/bin/env python3
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

"""Summarize a DRC JSON report, printing violation counts per rule."""

import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Print a human-readable summary of a .drc.json report."
    )
    parser.add_argument("drc_json", help="Path to .drc.json file")
    args = parser.parse_args()

    try:
        with open(args.drc_json, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: file not found: {args.drc_json}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in {args.drc_json}: {exc}", file=sys.stderr)
        sys.exit(1)

    total_violations = data.get("total_violations", 0)
    total_rules_violated = data.get("total_rules_violated", 0)
    rules = data.get("rules", {})

    print(f"Total violations: {total_violations}")
    print(f"Rules violated: {total_rules_violated}")

    for rule_name, info in rules.items():
        count = info.get("violation_count", 0)
        print(f"  {rule_name} : {count}")


if __name__ == "__main__":
    main()
