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

"""Safe shell-friendly math operations without eval/exec."""

import argparse
import sys


def parse_float(s):
    """Convert a string to float, raising ValueError on failure."""
    try:
        return float(s)
    except ValueError:
        print(f"Error: not a valid number: {s}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Perform safe shell-friendly math operations."
    )
    parser.add_argument(
        "--op",
        required=True,
        choices=["max", "add", "gte", "div", "fmt", "sub"],
        help="Operation to perform",
    )
    parser.add_argument(
        "args",
        nargs="*",
        help="Numeric arguments",
    )
    parsed = parser.parse_args()

    op = parsed.op
    raw_args = parsed.args

    if op == "max":
        if len(raw_args) != 2:
            print("Error: 'max' requires exactly 2 arguments", file=sys.stderr)
            sys.exit(1)
        a = parse_float(raw_args[0])
        b = parse_float(raw_args[1])
        print(max(0, int(a - b)))

    elif op == "add":
        if len(raw_args) != 2:
            print("Error: 'add' requires exactly 2 arguments", file=sys.stderr)
            sys.exit(1)
        a = parse_float(raw_args[0])
        b = parse_float(raw_args[1])
        print(a + b)

    elif op == "sub":
        if len(raw_args) != 3:
            print("Error: 'sub' requires exactly 3 arguments", file=sys.stderr)
            sys.exit(1)
        a = parse_float(raw_args[0])
        b = parse_float(raw_args[1])
        c = parse_float(raw_args[2])
        print(max(0, int(a + b - c)))

    elif op == "gte":
        if len(raw_args) != 2:
            print("Error: 'gte' requires exactly 2 arguments", file=sys.stderr)
            sys.exit(1)
        a = parse_float(raw_args[0])
        b = parse_float(raw_args[1])
        print("yes" if a >= b else "no")

    elif op == "div":
        if len(raw_args) != 2:
            print("Error: 'div' requires exactly 2 arguments", file=sys.stderr)
            sys.exit(1)
        a = parse_float(raw_args[0])
        b = parse_float(raw_args[1])
        if b == 0:
            print("Error: division by zero", file=sys.stderr)
            sys.exit(1)
        print(f"{a / b:.3f}")

    elif op == "fmt":
        if len(raw_args) != 1:
            print("Error: 'fmt' requires exactly 1 argument", file=sys.stderr)
            sys.exit(1)
        a = parse_float(raw_args[0])
        print(f"{a:.1f}")


if __name__ == "__main__":
    main()
