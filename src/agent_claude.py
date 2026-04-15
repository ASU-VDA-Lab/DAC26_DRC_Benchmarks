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
# Unified LLM Agent for DRC tasks. Calls models via the Claude Code CLI.
#
# The agent writes its output directly to the file path specified in the prompt
# (via the {output_path} placeholder). agent_claude.py does NOT capture or parse
# the agent's stdout -- it only manages invocation, timeouts, and runtime
# tracking.
#
# Fallback: for repair tasks, if --fallback is given (path to the original layout
#   script), it is copied to the output file *before* calling the agent.  If the
#   agent fails or times out, the original script remains so the pipeline can
#   still render and score it.
#
# Two-phase timeout (default: 10 min + 2 min):
#   1. Initial phase (--reminder_timeout, default 600s): agent works normally.
#   2. If the initial phase times out, a *reminder* prompt is sent asking the
#      agent to immediately write its best output to the output path within
#      --final_timeout (default 120s).  The reminder text includes the actual
#      timeout values and the output path.
#   3. If the reminder phase also times out, the agent is force-killed and the
#      pipeline continues with the fallback output (exit 0).

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time

AGENT_CMD = "claude"
LONG_PROMPT_THRESHOLD = 100000


def call_claude_agent(prompt_text, model_name, workspace=None, timeout=1200,
                      effort=None):
    # Invoke the Claude Code CLI.
    #
    # The agent writes output files directly (as instructed in the prompt).
    # This function only tracks the subprocess lifecycle.
    #
    # Raises subprocess.TimeoutExpired if the agent does not finish within
    # *timeout* seconds (the process is killed before re-raising).

    base_cmd = [
        AGENT_CMD,
        "--model", model_name,
        "--output-format", "text",
        "--allowedTools", "Bash(*)", "Read", "Write", "Edit",
            "Glob", "Grep", "Agent", "NotebookEdit",
        "-p",                           # print mode (non-interactive)
    ]
    if effort:
        base_cmd.extend(["--effort", effort])

    # Claude Code does not have a --workspace flag; use cwd instead.
    cwd = workspace if workspace else None

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
                    cwd=cwd,
                )
                try:
                    stdout, stderr = proc.communicate(timeout=timeout)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.communicate()  # drain pipes
                    raise
        else:
            cmd = base_cmd + [prompt_text]
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=cwd,
            )
            try:
                stdout, stderr = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.communicate()  # drain pipes
                raise
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


def continue_claude_agent(message, model_name, workspace=None, timeout=120,
                          effort=None):
    # Continue the most recent Claude Code conversation with a follow-up message.
    #
    # Uses `claude --continue -p "message"` to resume the session that was
    # killed during Phase 1, preserving all prior context.
    #
    # Raises subprocess.TimeoutExpired if the agent does not finish within
    # *timeout* seconds (the process is killed before re-raising).

    cmd = [
        AGENT_CMD,
        "--model", model_name,
        "--output-format", "text",
        "--allowedTools", "Bash(*)", "Read", "Write", "Edit",
        "Glob", "Grep", "Agent", "NotebookEdit",
        "--continue",
        "-p", message,
    ]
    if effort:
        cmd.extend(["--effort", effort])

    cwd = workspace if workspace else None

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
    )
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.communicate()
        raise

    stdout_text = stdout.decode("utf-8", errors="replace")
    stderr_text = stderr.decode("utf-8", errors="replace")

    if proc.returncode != 0:
        raise RuntimeError(
            "Agent CLI (continue) exited with code {}.\nstderr: {}\nstdout: {}".format(
                proc.returncode, stderr_text.strip(), stdout_text.strip())
        )


if __name__ == "__main__":
    if shutil.which(AGENT_CMD) is None:
        sys.stderr.write(
            "ERROR: '{}' command not found. Install the Claude Code CLI "
            "and ensure it is on PATH.\n".format(AGENT_CMD)
        )
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Unified LLM Agent for DRC tasks")
    parser.add_argument("prompt_file", help="Path to formatted prompt file")
    parser.add_argument("output_file",
                        help="Expected output file path (agent writes here "
                             "directly; used for fallback and verification)")
    parser.add_argument("--model", required=True,
                        help="Model name (e.g. claude-opus-4-6, claude-sonnet-4-6)")
    parser.add_argument("--task_type", default="repair",
                        choices=["repair", "detection"])
    parser.add_argument("--reminder_timeout", type=int, default=600,
                        help="Seconds before sending reminder (default: 600 = 10 min)")
    parser.add_argument("--final_timeout", type=int, default=120,
                        help="Seconds after reminder before force-kill (default: 120 = 2 min)")
    parser.add_argument("--fallback", default=None,
                        help="Path to original layout script; copied to output_file "
                             "as fallback before calling the agent (repair only)")
    parser.add_argument("--workspace", default=None,
                        help="Workspace directory for the agent (used as cwd)")
    parser.add_argument("--effort", default=None,
                        help="Claude reasoning effort level (e.g. high, medium, low)")
    parser.add_argument("--temp_dir", default=None,
                        help="Directory for intermediate/scratch files; "
                             "created before the agent runs")
    parser.add_argument("--reminder_prompt_file", default=None,
                        help="Path to pre-formatted reminder prompt file "
                             "(used for Phase 2 --continue call)")
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
    sys.stdout.write("Timeout: {}s initial + {}s after reminder\n".format(
        args.reminder_timeout, args.final_timeout))
    t_start = time.monotonic()

    # -- Phase 1: initial call with reminder_timeout --------------------------
    try:
        call_claude_agent(
            prompt_text, args.model,
            workspace=args.workspace, timeout=args.reminder_timeout,
            effort=args.effort,
        )
    except subprocess.TimeoutExpired:
        elapsed_so_far = time.monotonic() - t_start
        sys.stderr.write(
            "REMINDER: Agent timed out after {:.0f}s. "
            "Sending reminder with {}s deadline...\n".format(
                elapsed_so_far, args.final_timeout))

        # -- Phase 2: continue the killed session with a reminder ---------------
        if args.reminder_prompt_file and os.path.isfile(args.reminder_prompt_file):
            with open(args.reminder_prompt_file) as rf:
                reminder_message = rf.read()
        else:
            reminder_message = (
                "URGENT: Time is up. Write your best output to {} immediately."
            ).format(args.output_file)

        try:
            continue_claude_agent(
                reminder_message, args.model,
                workspace=args.workspace, timeout=args.final_timeout,
                effort=args.effort,
            )
            sys.stderr.write("  Reminder call completed.\n")
        except subprocess.TimeoutExpired:
            elapsed_so_far = time.monotonic() - t_start
            sys.stderr.write(
                "WARNING: Agent did not respond to reminder within {}s. "
                "Total elapsed: {:.0f}s. Keeping fallback output.\n".format(
                    args.final_timeout, elapsed_so_far))
        except Exception as exc:
            elapsed_so_far = time.monotonic() - t_start
            sys.stderr.write("ERROR during reminder call: {}\n".format(exc))
            sys.stderr.write("RUNTIME_SECONDS={:.3f}\n".format(elapsed_so_far))
            sys.stderr.write("  Keeping fallback output.\n")
            sys.exit(1)

    except Exception as exc:
        elapsed = time.monotonic() - t_start
        sys.stderr.write("ERROR: {}\n".format(exc))
        sys.stderr.write("RUNTIME_SECONDS={:.3f}\n".format(elapsed))
        sys.stderr.write("  Keeping fallback output.\n")
        sys.exit(1)

    elapsed = time.monotonic() - t_start
    sys.stderr.write("RUNTIME_SECONDS={:.3f}\n".format(elapsed))

    # Check if agent wrote the output file
    if os.path.isfile(args.output_file):
        sys.stdout.write("Output file exists: {}\n".format(args.output_file))
    else:
        sys.stdout.write("WARNING: Output file not found: {}\n".format(
            args.output_file))
