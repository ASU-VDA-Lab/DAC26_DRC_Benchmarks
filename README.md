# DAC 2026 DRC Benchmark

![Benchmarks](etc/benchmarks.png)

A benchmark framework for evaluating LLM models on chip physical design tasks -- specifically **DRC repair** and **DRC detection** -- using the ASAP7 7nm PDK and KLayout DRC.

This benchmark runs inside a self-contained Docker container. KLayout 0.30.1 and the Cursor/Claude Code CLIs are pre-installed in the image. No host KLayout installation or commercial EDA licenses are required.

Shortcut: [Table of Contents](#table-of-contents) | [Benchmark Tasks](#benchmark-tasks) | [Quick Start](#quick-start) | [Pipeline Architecture](#pipeline-architecture) | [Detection Isolation](#detection-isolation) | [Scoring Methodology](#scoring-methodology) | [Processed DRC Reports](#processed-drc-reports) | [Detection Output Format](#detection-output-format) | [Score Output](#score-output) | [Design Types](#design-types)

---

## Table of Contents

- *[Dockerfile.repair](./Dockerfile.repair)*: Repair-task image (AlmaLinux 8.10 + KLayout 0.30.1 + Cursor Agent CLI + Claude Code CLI).
- *[Dockerfile.detection](./Dockerfile.detection)*: Detection-task image -- no KLayout, runtime iptables blocklist on klayout/package-index domains to prevent the agent from invoking or installing DRC tools.
- *[CLAUDE.md](./CLAUDE.md)*: Agent behavior contract read by the LLM inside the container (unattended-Docker rules: never ask, never wait, never abort).
- *[docker/](./docker)*: Build-time helpers for the detection image (`entrypoint-blocklist.sh`).
- *[case_stat.md](./case_stat.md)*: Test case statistics -- polygon target rules, block design details, and cell DRC violations.
- *[example/](./example)*: Customizable files -- modify here and copy to *[src/](./src)* to use.
- *[src/](./src)*: Pipeline source code and agent scripts (incl. `skill.md`, the ASAP7 DRC reference fed to agents via `path_to_skill`).
- *[testcase/](./testcase)*: Test case assets and ASAP7 technology files.
- *[result/](./result)*: LLM outputs, stored at `result/<model_name>/<design_type>/<task_type>/<case_name>/` (auto-created on first run).
- *[score/](./score)*: Evaluation scores, stored at `score/<model_name>/<design_type>/<task_type>/` (auto-created on first run).
- *[task/](./task)*: Formatted prompts (auto-created on first run).
- *[temp/](./temp)*: Intermediate/scratch files written by LLM agents; cleaned up after each run (auto-created on first run).
- *[logs/](./logs)*: Full pipeline console logs (`<model>_<design>_<task>_<case>.log`) and `runtime.csv` (auto-created on first run).

---

## Benchmark Tasks

### Task 1: DRC Repair

The LLM agent receives a layout (GDS, layout script, screenshot) along with its KLayout DRC report and the ASAP7 design rule documentation. It must produce a **modified layout script** that resolves all reported violations without introducing new ones or corrupting the design.

**Inputs provided to the agent:**


| Input                       | Description                                                                |
| --------------------------- | -------------------------------------------------------------------------- |
| Layout script (`.py`)       | KLayout Python (`pya` API) script that generates the GDS                   |
| GDS file (`.gds`)           | Compiled GDS-II binary layout                                              |
| Layout screenshot (`.png`)  | Visual rendering of the layout                                             |
| DRC report (`.drc.json`)    | Processed DRC report in structured JSON with violation counts and geometry |
| Design rule file (`.lydrc`) | KLayout DRC rule file defining every design rule                           |
| Skill document (`skill.md`) | ASAP7 DRC knowledge reference for LLM agents                               |
| Connectivity JSON (`.json`) | Golden connectivity reference (cell/block only); the agent uses this with `check_connectivity.py` to verify electrical connections are preserved |


**Expected output:** The agent saves a modified KLayout Python layout script directly to `result/<model_name>/<design_type>/repair/<case_name>/<case_name>_repaired.py`.

**Evaluation flow:**

1. LLM's modified script is executed via KLayout to produce a new GDS
2. KLayout DRC is re-run on the new GDS
3. Repaired DRC results are converted to `.drc.json` for consistent comparison
4. Sanity check validates GDS integrity (top cell, layers, cell structure; for polygon designs, also verifies shape count per layer is unchanged)
5. Connectivity check verifies electrical connections are preserved (cell/block only)
6. Golden `.drc.json` and repaired `.drc.json` are compared to compute scoring metrics

### Task 2: DRC Detection

The LLM agent receives the same layout inputs **except** the DRC report. It must predict which rules are violated, estimate the violation count for each, and provide **DRV (Design Rule Violation) regions** for every violation instance.

**DRV region format:**

- **Spacing violations** (`.S.` rules): **edge pair** -- the two edges that are too close, each as `[x1, y1, x2, y2]` in dbu (integer database units; 1 dbu = 0.00025 um)
- **All other violations**: **bounding box** -- `[xmin, ymin, xmax, ymax]` in dbu (integer database units; 1 dbu = 0.00025 um)

**Expected output:** The agent saves a JSON array of predicted violations directly to `result/<model_name>/<design_type>/detection/<case_name>/<case_name>_detection.json`:

```json
[
  {
    "rule_name": "M1.S.4",
    "violation_count": 1,
    "violations": [
      {"type": "edge_pair", "edge1": [0, 200, 80, 200], "edge2": [0, 312, 80, 312]}
    ]
  },
  {
    "rule_name": "ACTIVE.A.1A",
    "violation_count": 1,
    "violations": [
      {"type": "bbox", "bbox": [0, 0, 270, 270]}
    ]
  }
]
```

**Evaluation flow:**

1. LLM's detection JSON is parsed (including DRV regions)
2. Golden `.drc.json` report is parsed (contains both violation counts and per-violation geometry)
3. Predicted violations are matched to golden violations using **geometry-based matching**:
  - **Polygon** golden bbox (non-zero area): overlap + area ratio within `[0.81, 1.21]` (linear ±10% squared)
  - **Edge** golden bbox (degenerate line, one dim = 0): both edge endpoints must lie inside the predicted bbox AND the predicted bbox's longest side must not exceed `edge_length × 1.1`
  - Both criteria must be met for a match
4. TP (matched), FP (unmatched predicted), FN (unmatched golden) are computed per rule
5. Aggregate and per-rule precision/recall/F1 metrics are calculated

---

## Quick Start

### Prerequisites

- **Docker** -- for building and running the benchmark container
- **Cursor CLI on the host** (for Cursor pipeline) -- install and log in:
  ```bash
  curl https://cursor.com/install -fsS | bash
  agent login
  ```
  The login credentials at `~/.config/cursor/auth.json` are bind-mounted (read-only) into the container at runtime.
- **Claude Code CLI on the host** (for Claude Code pipeline) -- install and log in:
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  claude login
  ```
  The login credentials at `~/.claude/` are bind-mounted (read-only) into the container at runtime.
- **KLayout 0.30.1** -- pre-installed in the Docker image (downloaded from klayout.org during build)
- **Python 3.6+** -- pre-installed in the Docker image (standard library only; no extra pip packages required)

### 1. Build the Docker Images

Two images are used:

- `drc-benchmark-repair` (full KLayout) -- for repair tasks, which legitimately need to run DRC.
- `drc-benchmark-detection` (no KLayout, with iptables blocklist on klayout/package-index domains) -- for detection tasks, to prevent the agent from leaking the golden DRC answer by invoking or installing KLayout.

```bash
cd DAC26_DRC_Benchmark/
docker build -f Dockerfile.repair    -t drc-benchmark-repair    .
docker build -f Dockerfile.detection -t drc-benchmark-detection .
```

Both images are AlmaLinux 8.10 with Cursor CLI + Claude Code CLI pre-installed. The repair image additionally has KLayout 0.30.1, Ruby, and Qt5. The detection image has Python 3.6 and `iptables` only; download tools (`wget`, `curl`, `pip`, `yum`, `rpm`, `gcc`, `git`, etc.) are stripped, and the entrypoint installs a runtime blocklist of klayout.org, pypi.org, github.com, etc. See [Detection Isolation](#detection-isolation) below.

### 2. Run a Single Test Case

**All commands must be run from the `DAC26_DRC_Benchmark/` directory.** To run a single case, prepare an `info.json` (see `example/info.json` for the required keys) and call the pipeline script inside the Docker container. Note: `output_path` and `temp_dir` are automatically overwritten by the pipeline with computed container paths -- you can leave them empty or set them to any placeholder value.

Use `drc-benchmark-repair` for repair tasks and `drc-benchmark-detection` for detection tasks. Detection additionally requires `--cap-add=NET_ADMIN` so the container entrypoint can program its iptables blocklist.

Both examples mirror what `evaluate_cursor.sh` / `evaluate_claude.sh` do per case: bind-mount only the single credential file (not the whole credential directory), bind-mount the four runtime I/O directories (`result`, `score`, `logs`, `temp`), and inject the golden DRC report via `docker cp` rather than a volume mount so detection runs never see it on the filesystem before the scoring phase.

**Cursor Agent CLI (repair example):**

```bash
CASE=Cell1
DESIGN=cell
CONTAINER=drc-bench-$CASE

docker create --name "$CONTAINER" \
    -v "$HOME/.config/cursor/auth.json:/root/.config/cursor/auth.json:ro" \
    -v "$(pwd)/result:/workspace/result" \
    -v "$(pwd)/score:/workspace/score" \
    -v "$(pwd)/logs:/workspace/logs" \
    -v "$(pwd)/temp:/workspace/temp" \
    drc-benchmark-repair \
    sleep infinity
docker start "$CONTAINER"

docker cp info.json "$CONTAINER:/workspace/task/info.json"
docker exec "$CONTAINER" mkdir -p "/workspace/testcase/asap7/$DESIGN/drc_report"
docker cp "testcase/asap7/$DESIGN/drc_report/$CASE.drc.json" \
    "$CONTAINER:/workspace/testcase/asap7/$DESIGN/drc_report/"

docker exec \
    -e AGENT_INITIAL_BUDGET=600 -e AGENT_REMINDER_BUDGET=300 \
    "$CONTAINER" bash src/run_pipeline_cursor.sh /workspace/task/info.json

docker rm -f "$CONTAINER"
```

**Claude Code CLI (detection example):**

Detection runs `--agent-only` first (no golden report visible), then `docker cp` injects the golden report, then `--score-only`. Detection additionally requires `--cap-add=NET_ADMIN` so the entrypoint can program its iptables blocklist.

```bash
CASE=Cell1
DESIGN=cell
CONTAINER=drc-bench-$CASE

docker create --name "$CONTAINER" --cap-add=NET_ADMIN \
    -v "$HOME/.claude/.credentials.json:/root/.claude/.credentials.json:ro" \
    -v "$(pwd)/result:/workspace/result" \
    -v "$(pwd)/score:/workspace/score" \
    -v "$(pwd)/logs:/workspace/logs" \
    -v "$(pwd)/temp:/workspace/temp" \
    drc-benchmark-detection \
    sleep infinity
docker start "$CONTAINER"

docker cp info.json "$CONTAINER:/workspace/task/info.json"

# Phase 1: agent-only (golden report NOT yet in container)
docker exec \
    -e AGENT_INITIAL_BUDGET=600 -e AGENT_REMINDER_BUDGET=300 \
    "$CONTAINER" bash src/run_pipeline_claude.sh --agent-only /workspace/task/info.json

# Phase 2: inject golden report, then score
docker exec "$CONTAINER" mkdir -p "/workspace/testcase/asap7/$DESIGN/drc_report"
docker cp "testcase/asap7/$DESIGN/drc_report/$CASE.drc.json" \
    "$CONTAINER:/workspace/testcase/asap7/$DESIGN/drc_report/"
docker exec \
    -e AGENT_INITIAL_BUDGET=1800 -e AGENT_REMINDER_BUDGET=120 \
    "$CONTAINER" bash src/run_pipeline_claude.sh --score-only /workspace/task/info.json

docker rm -f "$CONTAINER"
```

The `--agent-only` / `--score-only` phase flags exist exactly to gate when the golden DRC report becomes visible to the agent (see [Pipeline Architecture](#pipeline-architecture)).

### 3. Reproduce Paper Experiments

`evaluate_cursor.sh` (Cursor) and `evaluate_claude.sh` (Claude Code) are provided to reproduce the experiments in the paper. They automate info.json generation, Docker container lifecycle, and golden DRC report injection across all task/model/case combinations. Most users do not need these scripts.

```bash
# Edit the CASES array, then run:
bash src/evaluate_cursor.sh          # Cursor Agent CLI
bash src/evaluate_claude.sh   # Claude Code CLI
```

---

## Pipeline Architecture

The core pipeline runs inside a Docker container via `run_pipeline_cursor.sh` (Cursor) or `run_pipeline_claude.sh` (Claude Code). For paper experiments, `evaluate_cursor.sh` / `evaluate_claude.sh` wraps this with automated info.json generation and Docker container management:

```
evaluate_cursor.sh (paper experiments only)                             [HOST]
  |
  +-- For each task_type × model_name × case:
  |     +-- Generate info.json (build_case_info.py)
  |     +-- Create Docker container
  |     +-- Copy info.json into container
  |     +-- [Repair]: copy golden DRC report, run full pipeline
  |     +-- [Detection]: run agent-only, copy golden DRC report, run score-only
  |     +-- Clean up container
```

Inside the container, `run_pipeline_cursor.sh` executes:

```
run_pipeline_cursor.sh <info.json>                                      [CONTAINER]
  |
  +-- Step 1: Post-process info.json (rewrite paths to container perspective, including connectivity file path for cell/block)
  +-- Step 2: Format prompt (prompt_format.py + prompt_repair/detection.md; cell/block repair prompts include golden connectivity JSON path)
  |
  +-- Step 3: Call LLM model (agent_cursor.py or agent_claude.py --model <model_name>)
  |            Global budget: 10-min total across all repair iterations (timer paused during KLayout DRC and scoring)
  |            Reminder: when budget exhausted, agent gets 5 min to write final output
  |            Force-kill if reminder also times out
  |
  +-- [Repair only -- repeated up to MAX_ITERATIONS times (default: 5)]:
  |    +-- Step 3.5: Render GDS (KLayout batch mode)
  |    +-- Step 4: Run KLayout DRC (run_klayout_drc.py) -> .lyrpt
  |    +-- Step 4.5: Convert DRC report to JSON (process_klayout_reports.py) -> .drc.json
  |    +-- Step 5: Sanity check (sanity_check.py)
  |    +-- Step 5.5: Connectivity check (check_connectivity.py, cell/block only)
  |    +-- Break early if DRC-clean (polygon) or DRC-clean + connectivity
  |         preserved (cell/block); otherwise feed result back for next iteration
  |
  +-- Step 6: Score best iteration (score_repair.py or score_detection.py)
  +-- Write CSV (write_score_csv)
  +-- Append runtime to logs/runtime.csv
```

### Iterative Repair

For repair tasks, the pipeline retries up to `**MAX_ITERATIONS**` times (default: `5`, configurable via the `MAX_ITERATIONS` environment variable). Each iteration feeds the previous iteration's DRC result back to the agent as additional context. The agent operates under a **global time budget of 10 minutes (600s) shared across all iterations** -- the timer runs only while `agent_cursor.py` is executing and is paused during KLayout DRC, scoring, and other intermediate steps.

- **Early termination:** the loop breaks as soon as the output is DRC-clean. For cell/block designs, both DRC-clean **and** connectivity-preserved must hold.
- **Per-iteration score files:** each iteration writes its own score file (e.g., `<case_name>_score_iter1.json`). The agent output script is always written to `<case_name>_repaired.py` (overwritten each iteration); intermediate DRC files go to `result/<model_name>/<design_type>/repair/<case_name>/temp/`.
- **Best iteration selection:** among all iterations, the best is chosen by: connectivity preserved first, then fewest violations, then lowest iteration number (i.e., earliest clean repair wins ties).
- **Final score JSON:** contains `best_iteration`, `iteration_used`, and `iteration_history` keys summarising all iterations.

### Supported Models

Models are invoked via the Cursor Agent CLI (`src/agent_cursor.py`) or Claude Code CLI (`src/agent_claude.py`). The 6 default benchmark models (Cursor model names) are:


| Default Model              | Provider  | Description                |
| -------------------------- | --------- | -------------------------- |
| `gpt-5.4-high`             | OpenAI    | GPT-5.4 (high reasoning)   |
| `claude-4.6-opus-high`     | Anthropic | Claude 4.6 Opus (high)     |
| `claude-4.6-sonnet-medium` | Anthropic | Claude 4.6 Sonnet (medium) |
| `gemini-3.1-pro`           | Google    | Gemini 3.1 Pro             |
| `grok-4-20`                | xAI       | Grok 4.20                  |
| `kimi-k2.5`                | Moonshot  | Kimi K2.5                  |


See [Cursor Models and Pricing](https://cursor.com/docs/models-and-pricing) for the full list of available models. Any model supported by the Cursor Agent CLI can be passed as `model_name`.

### Agent Timeout Behavior

The agent uses a **two-phase timeout** to ensure the pipeline always completes. For repair tasks, the budget is **global across all iterations** (not per-iteration). **Detection tasks** are unchanged: single-shot with 10 min + 5 min reminder.


| Phase              | Duration            | Behavior                                                                        |
| ------------------ | ------------------- | ------------------------------------------------------------------------------- |
| **Initial budget** | 10 min (600s) total | Agent works across all iterations; timer paused during KLayout DRC and scoring  |
| **Reminder**       | 5 min (300s)        | When initial budget is exhausted, agent is given 5 min to write its best output |
| **Force-kill**     | --                  | If reminder also times out, agent is killed and iteration recorded as failed    |


Configurable via environment variables: `AGENT_INITIAL_BUDGET` (default `600`), `AGENT_REMINDER_BUDGET` (default `300`, as set by `evaluate_cursor.sh` / `evaluate_claude.sh`). These env vars are the canonical knobs. The underlying Python flags `agent_cursor.py --reminder_timeout` / `--final_timeout` / `--temp_dir` exist for direct invocation and carry their own Python-level defaults (`600` / `120`), which `evaluate_*.sh` overrides via the env vars above.

### Intermediate Files

LLM agents are instructed to place all intermediate/scratch files (test scripts, debug outputs, draft fixes) in the `temp/` directory at the project root. The `--temp_dir` flag passed to `agent_cursor.py` ensures this directory is created before the agent runs. The prompt templates embed the concrete `temp_dir` path via the `{temp_dir}` placeholder so the agent knows where to write. The `temp/` directory is automatically deleted at the end of each pipeline run.

### Detection Isolation

Detection agents should predict DRC violations from the layout script alone, without running a real DRC tool. To enforce this, `Dockerfile.detection`:

- Ships without `klayout`, `wget`, `curl`, `pip`, `yum`, `rpm`, `gcc`, `git`, `make`, `cpio`.
- Has `iptables` pre-installed. The entrypoint resolves known DRC-install domains (`klayout.org`, `pypi.org`, `files.pythonhosted.org`, `github.com`, `gitlab.com`, `conda.anaconda.org`, `sourceforge.net`, `dl.fedoraproject.org`, ...) to IPs and installs `OUTPUT REJECT` rules for each.
- Leaves the rest of the internet reachable so the agent can still call the Anthropic / Cursor API endpoints through Docker's default NAT.

Running the image requires `--cap-add=NET_ADMIN` (both `evaluate_*.sh` scripts add this automatically for detection tasks). Repair tasks are unaffected and continue to run in `drc-benchmark-repair` with full KLayout available.

### Runtime Tracking

Every pipeline run appends a row to `logs/runtime.csv` with columns:

```
model, task_type, design_type, case_name, agent_runtime_seconds, total_runtime_seconds, agent_initial_budget, timestamp
```

The `runtime_seconds` field is also embedded in each score JSON file.

### Pipeline Logs

All console output (stdout + stderr) from each pipeline run is captured to a log file at:

```
logs/<model_name>_<design_type>_<task_type>_<case_name>.log
```

The same output is still printed to the terminal in real time.

---

## Scoring Methodology

### Repair Metrics


| Metric                   | Formula                                    | Description                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `repair_rate`            | `removed_violations / original_violations` | Fraction of original violations eliminated                                                                                                                                                                                                                                                                             |
| `new_violation_rate`     | `new_violations / original_violations`     | New violations introduced relative to original count                                                                                                                                                                                                                                                                   |
| `connectivity_preserved` | boolean                                    | Whether all original electrical connections remain (cell/block only). Uses shape-aware DFS with per-path visited vias, directional search rule, redundant via pruning, and full polygon shape identity. Golden connectivity is stored as JSON in `testcase/asap7/{cell,block}/connectivity/`. |
| `iteration_used`         | integer                                    | Total number of repair iterations actually run                                                                                                                                                                                                                                                                         |


### Detection Metrics (Geometry-Based)

Predicted violations are matched to golden violations using **geometry-based matching**:

1. Each violation's DRV region is converted to a bounding box (edge pairs use the bbox enclosing both edges).
2. Match criteria depend on the golden bbox shape:
  - **Polygon / non-degenerate** (`w*h > 0`): bboxes overlap AND area ratio `0.81 <= predicted_area / golden_area <= 1.21` (linear ±10% squared into area tolerance).
  - **Edge / line** (`w*h = 0` and `w+h > 0`): both edge endpoints lie inside the predicted bbox AND the predicted bbox's longest side is at most `edge_length × 1.1`.
  - **Dot** (`w = h = 0`): cannot match. The ingest pipeline (`process_klayout_reports.py --fix-dots`) replaces dot violations with their containing polygon's bbox so this case does not occur in practice.
3. **Hopcroft-Karp maximum bipartite matching** is used per rule for optimal (order-independent) matching.
4. When geometry is unavailable on either side, no TP credit is awarded (`tp=0`). Affected rules are listed in the `geometry_unavailable_rules` output field.
5. Scoring policy: `geometry_required_edge_aware`. All TP credit requires both predicted and golden geometry.


| Metric          | Formula                               | Description              |
| --------------- | ------------------------------------- | ------------------------ |
| `Precision` | `sum(TP) / (sum(TP) + sum(FP))`       | Aggregate precision      |
| `Recall`    | `sum(TP) / (sum(TP) + sum(FN))`       | Aggregate recall         |
| `F1`        | Harmonic mean of precision and recall | Aggregate F1             |


---

## Detection Output Format

The detection agent saves its predictions as a JSON array at `result/<model_name>/<design_type>/detection/<case_name>/<case_name>_detection.json`. Each top-level object represents one violated rule.

All coordinates are in **dbu (database units)** -- integer coordinates from the layout script (`1 dbu = 0.00025 um`). These are the same units used by the golden `.drc.json` report.

**Per-violation geometry:**

- `"type": "edge_pair"` -- for spacing rules (`.S.`); contains `edge1` and `edge2`, each `[x1, y1, x2, y2]`.
- `"type": "bbox"` -- for every other rule (width, enclosure, area, ...); contains `bbox` as `[xmin, ymin, xmax, ymax]`.

**Example:**

```json
[
  {
    "rule_name": "M1.S.4",
    "violation_count": 1,
    "violations": [
      {
        "type": "edge_pair",
        "edge1": [0, 200, 80, 200],
        "edge2": [0, 312, 80, 312]
      }
    ]
  },
  {
    "rule_name": "ACTIVE.A.1A",
    "violation_count": 1,
    "violations": [
      {
        "type": "bbox",
        "bbox": [0, 0, 270, 270]
      }
    ]
  }
]
```

If no violations are detected, the agent writes an empty array `[]`.

---

## Processed DRC Reports

Golden DRC reports are pre-processed from KLayout's native `.lyrpt` XML format into structured JSON files stored at `testcase/asap7/{cell,polygon,block}/drc_report/<case_name>.drc.json`.

**JSON format:**

```json
{
  "case_name": "Cell1",
  "design_type": "cell",
  "total_violations": 20,
  "total_rules_violated": 2,
  "rules": {
    "M1.S.4": {
      "violation_count": 1,
      "description": "Minimum spacing of M1 on same track is 18 nm.",
      "violations": [
        {
          "type": "edge_pair",
          "edges": [[1768, 832, 1840, 832], [1768, 944, 1840, 944]],
          "bbox": [1768, 832, 1840, 944]
        }
      ]
    }
  }
}
```

The pipeline uses `.drc.json` for both golden and repaired reports. After KLayout DRC runs on a repaired GDS, the `.lyrpt` results are converted to JSON for consistent comparison.

---

## Score Output

Each pipeline run produces `.json` and `.csv` files at:

```
score/<model_name>/<design_type>/<task_type>/<case_name>_score.json
score/<model_name>/<design_type>/<task_type>/<case_name>_score.csv
```

The score JSON also contains `runtime_seconds` (agent wall-clock time) and `total_runtime_seconds` (full pipeline time).

**Repair tasks** additionally include:


| Key                 | Description                                     |
| ------------------- | ----------------------------------------------- |
| `best_iteration`    | 1-based index of the iteration selected as best |
| `iteration_used`    | Number of iterations actually run               |
| `iteration_history` | Array of per-iteration score summaries          |


**Detection tasks** additionally include:


| Key                          | Description                                                        |
| ---------------------------- | ------------------------------------------------------------------ |
| `matching_algorithm`         | `"hopcroft_karp"` -- algorithm used for violation matching         |
| `scoring_policy`             | `"geometry_required_edge_aware"` -- TP credit requires geometry on both sides; uses edge-encompass matching for line-shaped golden bboxes |
| `mercy_low` / `mercy_high`   | `0.81` / `1.21` -- area ratio bounds for polygon matches |
| `edge_side_tolerance`        | `1.1` -- multiplier on `edge_length` that caps the predicted bbox's longest side for edge matches |
| `geometry_unavailable_rules` | List of rule names where geometry was missing (tp forced to 0)     |


---

## Design Types


| Type      | Count | DRC Rule File      | Description                                                                                                                                                                 |
| --------- | ----- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cell`    | 255   | `asap7_cell.lydrc` | Standard-cell layouts (10-50 polygons, 5-15 violations)                                                                                                                     |
| `polygon` | 332   | `asap7.lydrc`      | Isolated polygon constructs testing specific DRC rules. Repair is restricted to resizing (width/length) or moving polygons; deletion and adding new polygons are forbidden. |
| `block`   | 7     | `asap7.lydrc`      | Larger block-level layouts with routing and vias (100+ polygons)                                                                                                            |


