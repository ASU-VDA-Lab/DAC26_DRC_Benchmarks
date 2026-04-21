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
#################################################################################
# Unified LLM Agent for DRC tasks. Calls models via the Cursor Agent CLI.
#
# The agent runs to completion under the Cursor Agent CLI with no artificial
# timeout. It writes its output directly to the file path passed via the
# prompt. This wrapper parses the CLI's stdout JSON to recover token usage,
# then emits STATUS=/TOKENS_JSON=/RUNTIME_SECONDS= markers on stderr for the
# pipeline shell script to consume.
#
# Fallback: for repair tasks, the original script is copied to the output
# path before the agent runs. For detection tasks, an empty JSON array is
# written. If the agent fails, those fallback files remain.

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

AGENT_CMD = "agent"
LONG_PROMPT_THRESHOLD = 100000


def call_cursor_agent(prompt_text, model_name, workspace=None):
    # Invoke the Cursor Agent CLI with --output-format json and no timeout.
    #
    # Returns a tuple (tokens, raw_data):
    #   tokens:   dict with normalized snake_case token keys:
    #             input_tokens, output_tokens, cache_read_tokens, cache_write_tokens
    #   raw_data: the full parsed CLI JSON with the "result" key popped.
    #
    # Raises:
    #   RuntimeError if the CLI exits non-zero.
    #   json.JSONDecodeError / KeyError / TypeError if stdout cannot be parsed
    #   into the expected {"usage": {...}} shape.

    base_cmd = [
        AGENT_CMD,
        "--model", model_name,
        "--output-format", "json",
        "--trust",              # trust workspace without prompting
        "-p",                   # print mode (non-interactive)
    ]
    if workspace:
        base_cmd.extend(["--workspace", workspace])

    tmp_path = None
    try:
        if len(prompt_text) > LONG_PROMPT_THRESHOLD:
            fd, tmp_path = tempfile.mkstemp(suffix=".txt", prefix="agent_prompt_")
            with os.fdopen(fd, "w") as tmp:
                tmp.write(prompt_text)
            with open(tmp_path) as stdin_fh:
                proc = subprocess.Popen(
                    base_cmd,
                    stdin=stdin_fh,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                stdout, stderr = proc.communicate()
        else:
            cmd = base_cmd + [prompt_text]
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdout, stderr = proc.communicate()
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)

    stdout_text = stdout.decode("utf-8", errors="replace")
    stderr_text = stderr.decode("utf-8", errors="replace")

    if proc.returncode != 0:
        raise RuntimeError(
            "Agent CLI exited with code {}.\nstderr: {}\nstdout: {}".format(
                proc.returncode, stderr_text.strip(), stdout_text.strip())
        )

    # Parse stdout JSON and extract token usage.
    data = json.loads(stdout_text)
    usage = data["usage"]

    tokens = {
        "input_tokens":       int(usage["inputTokens"]),
        "output_tokens":      int(usage["outputTokens"]),
        "cache_read_tokens":  int(usage.get("cacheReadTokens", 0)),
        "cache_write_tokens": int(usage.get("cacheWriteTokens", 0)),
    }

    # Strip the "result" key (LLM final text) before returning raw data.
    raw_data = dict(data)
    raw_data.pop("result", None)

    return tokens, raw_data


if __name__ == "__main__":
    if shutil.which(AGENT_CMD) is None:
        sys.stderr.write(
            "ERROR: '{}' command not found. Install the Cursor Agent CLI "
            "and ensure it is on PATH.\n".format(AGENT_CMD)
        )
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Unified LLM Agent for DRC tasks")
    parser.add_argument("prompt_file", help="Path to formatted prompt file")
    parser.add_argument("output_file",
                        help="Expected output file path (agent writes here "
                             "directly; used for fallback and verification)")
    parser.add_argument("--model", required=True,
                        help="Model name (e.g. claude-4.6-opus-high, gpt-5.4-high)")
    parser.add_argument("--task_type", default="repair",
                        choices=["repair", "detection"])
    parser.add_argument("--fallback", default=None,
                        help="Path to original layout script; copied to output_file "
                             "as fallback before calling the agent (repair only)")
    parser.add_argument("--workspace", default=None,
                        help="Workspace directory for the agent")
    parser.add_argument("--temp_dir", default=None,
                        help="Directory for intermediate/scratch files; "
                             "created before the agent runs")
    parser.add_argument("--raw-json-out", dest="raw_json_out", default=None,
                        help="Path to dump full CLI JSON (minus 'result' key) "
                             "for out-of-band token/metric inspection")
    args = parser.parse_args()

    # -- Ensure temp directory exists -------------------------------------------
    if args.temp_dir:
        os.makedirs(args.temp_dir, exist_ok=True)
        sys.stdout.write("Temp dir: {}\n".format(args.temp_dir))

    # -- Pre-populate output with fallback --------------------------------------
    if args.task_type == "repair" and args.fallback:
        if os.path.isfile(args.fallback):
            shutil.copy2(args.fallback, args.output_file)
            sys.stdout.write("Fallback: copied original script to {}\n".format(
                args.output_file))
        else:
            sys.stderr.write("WARNING: fallback file not found: {}\n".format(
                args.fallback))
    elif args.task_type == "detection":
        with open(args.output_file, "w") as f:
            f.write("[]")
        sys.stdout.write("Fallback: wrote empty detection JSON to {}\n".format(
            args.output_file))

    with open(args.prompt_file) as f:
        prompt_text = f.read()

    sys.stdout.write("Calling model: {}\n".format(args.model))

    zero_tokens = {
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_read_tokens": 0,
        "cache_write_tokens": 0,
    }

    t_start = time.monotonic()
    raw_data = None
    agent_error = None
    try:
        tokens, raw_data = call_cursor_agent(
            prompt_text, args.model,
            workspace=args.workspace,
        )
        status = "success"
    except Exception as exc:
        sys.stderr.write("ERROR: {}\n".format(exc))
        tokens = zero_tokens
        status = "fail"
        agent_error = str(exc)

    elapsed = time.monotonic() - t_start
    sys.stderr.write("STATUS={}\n".format(status))
    sys.stderr.write("TOKENS_JSON={}\n".format(json.dumps(tokens)))
    sys.stderr.write("RUNTIME_SECONDS={:.3f}\n".format(elapsed))

    # Dump the raw CLI JSON (or a failure stub) for out-of-band inspection.
    if args.raw_json_out:
        if status == "success" and raw_data is not None:
            payload = raw_data
        else:
            payload = {"status": "fail", "error": agent_error or "unknown"}
        try:
            os.makedirs(os.path.dirname(os.path.abspath(args.raw_json_out)),
                        exist_ok=True)
            with open(args.raw_json_out, "w") as f:
                json.dump(payload, f, indent=2)
        except Exception as exc:
            sys.stderr.write("WARNING: failed to dump raw JSON to {}: {}\n".format(
                args.raw_json_out, exc))

    # Check if agent wrote the output file
    if os.path.isfile(args.output_file):
        sys.stdout.write("Output file exists: {}\n".format(args.output_file))
    else:
        sys.stdout.write("WARNING: Output file not found: {}\n".format(
            args.output_file))

    # Always exit 0 — pipeline keys off the STATUS= marker, not the exit code.
    sys.exit(0)
