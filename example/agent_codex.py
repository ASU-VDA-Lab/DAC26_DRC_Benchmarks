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
# Unified LLM Agent for DRC tasks. Calls models via the Codex CLI.
#
# The agent runs to completion under `codex exec` with no artificial timeout.
# It writes its output directly to the file path passed via the prompt. This
# wrapper parses the CLI's stdout JSONL to recover token usage when available,
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
import time

AGENT_CMD = "codex"


def _as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _first_int(data, keys):
    for key in keys:
        if isinstance(data, dict) and key in data:
            value = _as_int(data.get(key))
            if value is not None:
                return value
    return None


def _update_tokens_from_dict(tokens, data):
    # Codex JSONL event schemas can evolve. Accept the common snake_case,
    # camelCase, and OpenAI API-style usage names.
    input_tokens = _first_int(data, [
        "input_tokens", "inputTokens", "prompt_tokens", "promptTokens",
        "total_input_tokens", "totalInputTokens",
    ])
    output_tokens = _first_int(data, [
        "output_tokens", "outputTokens", "completion_tokens",
        "completionTokens", "total_output_tokens", "totalOutputTokens",
    ])
    cache_read_tokens = _first_int(data, [
        "cache_read_tokens", "cacheReadTokens", "cache_read_input_tokens",
        "cacheReadInputTokens", "cached_input_tokens", "cachedInputTokens",
    ])
    cache_write_tokens = _first_int(data, [
        "cache_write_tokens", "cacheWriteTokens",
        "cache_creation_input_tokens", "cacheCreationInputTokens",
    ])

    if input_tokens is not None:
        tokens["input_tokens"] = max(tokens["input_tokens"], input_tokens)
    if output_tokens is not None:
        tokens["output_tokens"] = max(tokens["output_tokens"], output_tokens)
    if cache_read_tokens is not None:
        tokens["cache_read_tokens"] = max(
            tokens["cache_read_tokens"], cache_read_tokens)
    if cache_write_tokens is not None:
        tokens["cache_write_tokens"] = max(
            tokens["cache_write_tokens"], cache_write_tokens)


def _walk_json(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            for nested in _walk_json(child):
                yield nested
    elif isinstance(value, list):
        for child in value:
            for nested in _walk_json(child):
                yield nested


def parse_codex_jsonl(stdout_text):
    events = []
    tokens = {
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_read_tokens": 0,
        "cache_write_tokens": 0,
    }

    for line in stdout_text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except ValueError:
            event = {"raw": line}
        events.append(event)
        for obj in _walk_json(event):
            _update_tokens_from_dict(tokens, obj)

    return tokens, {"events": events}


def call_codex_agent(prompt_text, model_name, workspace=None, effort=None):
    # Invoke Codex non-interactively. Prompt text is always provided on stdin so
    # large benchmark prompts do not hit argv length limits.
    #
    # Returns a tuple (tokens, raw_data):
    #   tokens:   dict with normalized snake_case token keys:
    #             input_tokens, output_tokens, cache_read_tokens, cache_write_tokens
    #   raw_data: parsed JSONL events from Codex stdout.
    #
    # Raises:
    #   RuntimeError if the CLI exits non-zero.

    base_cmd = [
        AGENT_CMD,
        "exec",
        "--model", model_name,
        "--json",
        "--ephemeral",
        "--skip-git-repo-check",
        # Docker already provides the benchmark isolation boundary. Codex's
        # workspace-write sandbox may require user namespaces that are often
        # disabled inside containers.
        "--sandbox", os.environ.get("CODEX_SANDBOX", "danger-full-access"),
        "-c", 'approval_policy="{}"'.format(
            os.environ.get("CODEX_APPROVAL_POLICY", "never")),
        "-c", 'web_search="disabled"',
        "-c", 'sandbox_workspace_write.network_access=false',
        "--color", "never",
    ]

    if workspace:
        base_cmd.extend(["--cd", workspace])
    if effort:
        base_cmd.extend(["-c", 'model_reasoning_effort="{}"'.format(effort)])

    cmd = base_cmd + ["-"]
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate(prompt_text.encode("utf-8"))

    stdout_text = stdout.decode("utf-8", errors="replace")
    stderr_text = stderr.decode("utf-8", errors="replace")

    if proc.returncode != 0:
        raise RuntimeError(
            "Agent CLI exited with code {}.\nstderr: {}\nstdout: {}".format(
                proc.returncode, stderr_text.strip(), stdout_text.strip())
        )

    tokens, raw_data = parse_codex_jsonl(stdout_text)
    return tokens, raw_data


if __name__ == "__main__":
    if shutil.which(AGENT_CMD) is None:
        sys.stderr.write(
            "ERROR: '{}' command not found. Install the Codex CLI "
            "and ensure it is on PATH.\n".format(AGENT_CMD)
        )
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Unified LLM Agent for DRC tasks")
    parser.add_argument("prompt_file", help="Path to formatted prompt file")
    parser.add_argument("output_file",
                        help="Expected output file path (agent writes here "
                             "directly; used for fallback and verification)")
    parser.add_argument("--model", required=True,
                        help="Model name (e.g. gpt-5.4)")
    parser.add_argument("--task_type", default="repair",
                        choices=["repair", "detection"])
    parser.add_argument("--fallback", default=None,
                        help="Path to original layout script; copied to output_file "
                             "as fallback before calling the agent (repair only)")
    parser.add_argument("--workspace", default=None,
                        help="Workspace directory for the agent")
    parser.add_argument("--effort", default=None,
                        help="Codex reasoning effort level (e.g. high, medium, low)")
    parser.add_argument("--temp_dir", default=None,
                        help="Directory for intermediate/scratch files; "
                             "created before the agent runs")
    parser.add_argument("--raw-json-out", dest="raw_json_out", default=None,
                        help="Path to dump parsed Codex JSONL events for "
                             "out-of-band token/metric inspection")
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
    if args.effort:
        sys.stdout.write("Reasoning effort: {}\n".format(args.effort))

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
        tokens, raw_data = call_codex_agent(
            prompt_text, args.model,
            workspace=args.workspace, effort=args.effort,
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

    # Dump the raw CLI JSONL events (or a failure stub) for out-of-band inspection.
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

    # Always exit 0 -- pipeline keys off the STATUS= marker, not the exit code.
    sys.exit(0)
