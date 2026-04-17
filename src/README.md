# src/ -- Pipeline Source Code

All scripts for the KLayout DRC benchmark evaluation pipeline.

---

## Table of Contents

- [*run_pipeline_cursor.sh*](./run_pipeline_cursor.sh): **In-container** pipeline orchestrator (Cursor) -- accepts info.json, post-processes paths, runs prompt formatting, LLM model, DRC, scoring.
- [*run_pipeline_claude.sh*](./run_pipeline_claude.sh): **In-container** pipeline orchestrator (Claude Code) -- same as `run_pipeline_cursor.sh` but uses `agent_claude.py`.
- [*evaluate_cursor.sh*](./evaluate_cursor.sh): **Paper experiment runner** (Cursor) -- batch orchestrator that iterates over task_type × model_name × case, generates info.json via `build_case_info.py`, manages Docker containers, and injects golden DRC reports.
- [*evaluate_claude.sh*](./evaluate_claude.sh): **Paper experiment runner** (Claude Code) -- same as `evaluate_cursor.sh` but uses `run_pipeline_claude.sh`.
- [*agent_cursor.py*](./agent_cursor.py): Cursor Agent CLI wrapper -- invokes any LLM model via Cursor Agent CLI.
- [*agent_claude.py*](./agent_claude.py): Claude Code CLI wrapper -- invokes any LLM model via Claude Code CLI.
- [*prompt_format.py*](./prompt_format.py): Template engine -- fills `{placeholder}` tokens in prompt templates with values from info.json. Allowed keys include `path_to_connectivity_file` (golden connectivity JSON for cell/block repair).
- [*build_case_info.py*](./build_case_info.py): Builds per-case info.json with paths and prompt configuration (used by `evaluate_cursor.sh` for paper experiments). For cell/block cases, also generates the `path_to_connectivity_file` key pointing to the golden connectivity JSON.
- [*run_klayout_drc.py*](./run_klayout_drc.py): KLayout DRC runner -- invokes KLayout in batch mode with `.lydrc` rule files, produces `.lyrpt` reports.
- [*process_klayout_reports.py*](./process_klayout_reports.py): KLayout DRC report converter -- converts `.lyrpt` XML to structured `.drc.json` (batch or single-file).
- [*score_repair.py*](./score_repair.py): Repair scorer -- compares original vs repaired DRC reports (`repair_rate`, `new_violation_rate`).
- [*score_detection.py*](./score_detection.py): Detection scorer -- geometry-based matching (Hopcroft-Karp) of detected DRV regions against golden violations; `geometry_required_edge_aware` policy (polygon area mercy 0.81-1.21; edges matched by endpoint containment + longest-side ≤ `edge_length × 1.1`).
- [*sanity_check.py*](./sanity_check.py): GDS integrity validator -- checks top cell, non-empty, critical layers, cell structure; for polygon designs also verifies shape count per layer is unchanged (requires `pya`).
- [*check_connectivity.py*](./check_connectivity.py): Connectivity verifier -- checks electrical connections are preserved after LLM edits using shape-aware DFS with per-path visited vias, directional search rule, redundant via pruning, and full polygon shape identity. Reads golden connectivity from JSON files in `testcase/asap7/{cell,block}/connectivity/`.
- [*prepare_render_script.py*](./prepare_render_script.py): Rewrites `layout.write()` path in LLM output script for GDS rendering.
- [*merge_score_connectivity.py*](./merge_score_connectivity.py): Merges connectivity check fields into a score JSON file.
- [*write_score_csv.py*](./write_score_csv.py): Converts a score JSON to a single-row CSV file.
- [*log_runtime.py*](./log_runtime.py): Appends a row to the runtime CSV log.
- [*parse_info_json.py*](./parse_info_json.py): Parses info.json and outputs shell variable assignments (`task_type`, `model_name`, `case_name`, `design_type`) with `shlex.quote`.
- [*postprocess_info_json.py*](./postprocess_info_json.py): Rewrites info.json paths for the container perspective (layout script, screenshot, DRC report, DRM images, output path, temp dir, and connectivity file).
- [*read_score_field.py*](./read_score_field.py): Reads a single field from a score JSON file; supports `--default` for missing fields.
- [*skill.md*](./skill.md): ASAP7 DRC knowledge document -- layer mapping, rule categories, repair/detection strategies, and connectivity verification instructions. Referenced by prompt templates via `{path_to_skill}`.
- [*prompt_repair_cell.md*](./prompt_repair_cell.md): Repair prompt for cell designs. Includes `{path_to_connectivity_file}` placeholder for the golden connectivity JSON and instructs the agent to verify connectivity using `check_connectivity.py`.
- [*prompt_repair_block.md*](./prompt_repair_block.md): Repair prompt for block designs. Includes `{path_to_connectivity_file}` placeholder for the golden connectivity JSON and instructs the agent to verify connectivity using `check_connectivity.py`.
- [*prompt_repair_polygon.md*](./prompt_repair_polygon.md): Repair prompt for polygon designs (only resize or move allowed; no deletion, no adding new polygons).
- [*prompt_detection.md*](./prompt_detection.md): DRC detection task prompt template (requires DRV regions).

## Configuration

The example `info.json` template (showing all required keys) is located in `example/info.json`. The JSON includes both pipeline control fields (`model_name`, `case_name`, `design_type`, `task_type`) and prompt placeholder keys.

For paper experiments, `evaluate_cursor.sh` calls `build_case_info.py` (argparse named args) on the host to generate a per-case info.json. For single-case runs, prepare your own info.json manually (see `example/info.json` for required keys). Inside the container, `run_pipeline_cursor.sh` post-processes the JSON to rewrite all paths to the container perspective.

**Note:** `output_path` and `temp_dir` in info.json are **automatically overwritten** by `run_pipeline_cursor.sh` / `run_pipeline_claude.sh` with computed container paths. You can leave them empty or set them to any placeholder value -- the pipeline will replace them before use.

---

## Pipeline Flow

### `run_pipeline_cursor.sh` (in-container, primary entry point)

To run a single case, prepare an `info.json` and call `run_pipeline_cursor.sh` directly inside the container:

```bash
bash src/run_pipeline_cursor.sh /workspace/task/info.json
```

### `evaluate_cursor.sh` (host-side, paper experiments only)

```bash
# Edit the CASES array in evaluate_cursor.sh, then run:
bash src/evaluate_cursor.sh
```

Batch orchestrator that iterates over task_type × model_name × case. Generates `info.json` via `build_case_info.py`, manages Docker container lifecycle, and injects golden DRC reports at the right time via `docker cp`. For detection, the golden report is injected **after** the agent finishes (so the agent cannot see the answers). For repair, it is injected **before** the agent runs. Used to reproduce the paper's experiment table.

### `run_pipeline_cursor.sh` details

```bash
bash src/run_pipeline_cursor.sh [--agent-only|--score-only] <info.json>
```

The `info.json` must contain `task_type`, `model_name`, `case_name`, `design_type`, and all prompt placeholder keys (see `example/info.json`).

**Phase flags** (detection only):
- `--agent-only`: run only prompt formatting and agent call (no scoring)
- `--score-only`: run only scoring, CSV, and logging (agent must have run first)

Each invocation processes exactly one model. Results are stored under `result/<model_name>/` and `score/<model_name>/`.

**Pipeline steps:**

| Step | Script | Description |
|------|--------|-------------|
| 1 | `prompt_format.py` | Post-process info.json (rewrite paths to container perspective), then format prompt from template + info.json; DRC report points to `.drc.json` |
| 2 | `agent_cursor.py` or `agent_claude.py` | Call LLM model once via Cursor CLI or Claude Code CLI with `--model <model_name>` and `--output-format json`; the wrapper parses token usage from stdout and emits `STATUS=` / `TOKENS_JSON=` / `RUNTIME_SECONDS=` markers on stderr |
| 2.5 (repair) | KLayout batch | Render GDS from LLM's modified layout script |
| 3 (repair) | `run_klayout_drc.py` | Run KLayout DRC on the LLM-produced GDS, producing `.lyrpt` report |
| 3.5 (repair) | `process_klayout_reports.py` | Convert `.lyrpt` DRC report to structured `.drc.json` for consistent comparison |
| 4 (repair) | `sanity_check.py` + `check_connectivity.py` | Validate GDS integrity (all repair designs); verify connectivity preservation (cell/block only). Each writes a JSON file in `temp_dir/` |
| 5 | `score_repair.py` or `score_detection.py` | Score: also writes `agent_status`, `runtime_seconds`, and the 4 token fields directly into the score JSON |
| 5.5 (repair) | `merge_score_sanity.py`, `merge_score_connectivity.py` | Merge sanity (and connectivity, cell/block only) fields into the score JSON |
| 6 | `write_score_csv.py`, `log_runtime.py` | Write per-case CSV and append a row to `logs/runtime.csv` |

All console output (stdout + stderr) is also captured to `logs/<run_id>_<design_type>_<task_type>_<case_name>.log` via `tee`, where `run_id` is `<model_name>-<effort>` for claude pipeline runs (e.g. `claude-sonnet-4-6-medium`) and `<model_name>` for cursor runs.

**Environment variables:**

| Variable | Default | Description |
|----------|---------|-------------|
| `WORKSPACE` | `/workspace` | Root workspace directory (set by Docker image ENV) |
| `SKIP_DRC` | `0` | Set to `1` to skip KLayout DRC step (repair only) |
| `CLAUDE_EFFORT` | unset | Claude Code reasoning effort level (e.g. `high`, `medium`, `low`); passed as `--effort` to the CLI |

---

## Agent (`agent_cursor.py` / `agent_claude.py`)

CLI wrappers that invoke LLM models. `agent_cursor.py` uses the Cursor Agent CLI; `agent_claude.py` uses the Claude Code CLI. The agent writes its output directly to the file path specified in the prompt (via the `{output_path}` placeholder). Each wrapper parses the CLI's JSON stdout for token usage and emits stderr markers for the pipeline shell script to consume.

```bash
# Cursor Agent CLI
python3 src/agent_cursor.py <prompt_file> <output_file> --model <model_name> --task_type <repair|detection> \
    [--workspace <dir>] [--fallback <path>] [--temp_dir <path>]

# Claude Code CLI
python3 src/agent_claude.py <prompt_file> <output_file> --model <model_name> --task_type <repair|detection> \
    [--workspace <dir>] [--fallback <path>] [--temp_dir <path>] [--effort <level>]
```

- `output_file`: the expected output path (agent writes here directly as instructed by the prompt)
- `--temp_dir`: directory for intermediate/scratch files; created (via `os.makedirs`) before the agent runs
- `--fallback`: path to the original layout script (repair only); copied to `output_file` before the agent runs so the pipeline can still render/score if the agent fails

**Single-call execution**

The agent runs once to completion with no timeout or reminder. After the CLI
returns:

- `STATUS=success` or `STATUS=fail` is written to stderr.
- `TOKENS_JSON={...}` carries the 4 normalized token counters.
- `RUNTIME_SECONDS=<float>` carries the wall-clock runtime.

The process always exits 0; failure mode is conveyed via the `STATUS=` marker.
On failure, all four token counters are reported as 0 while `RUNTIME_SECONDS`
remains the real elapsed time.

---

## Scoring Scripts

### `score_repair.py`

```bash
python3 src/score_repair.py <original_report> <repaired_report>
```

Auto-detects report format by extension: `.drc.json` (processed JSON) or `.lyrpt` (KLayout XML). The pipeline uses `.drc.json` for both golden and repaired reports. Outputs JSON to stdout.

**Metrics:**

| Metric | Formula |
|--------|---------|
| `repair_rate` | `sum(max(0, orig[r] - repaired[r])) / sum(orig)` |
| `new_violation_rate` | `sum(max(0, repaired[r] - orig[r])) / sum(orig)` |

### `score_detection.py`

```bash
# With processed .drc.json (preferred -- single file contains counts + geometry):
python3 src/score_detection.py <detection.json> <golden.drc.json>

# Legacy (KLayout XML report):
python3 src/score_detection.py <detection.json> <golden.lyrpt>
```

Uses **geometry-based matching** when the detection includes DRV regions and the golden report provides per-violation geometry (from `.drc.json` or `.lyrpt`):

1. Each violation is converted to a bounding box:
   - Edge pairs (spacing): bbox enclosing both edges
   - Bounding boxes (other): used directly
   - Golden violations: bbox read directly from `.drc.json` (or converted from `.lyrpt` coordinates)
2. Matching depends on the golden bbox shape:
   - **Polygon / non-degenerate** (`w*h > 0`): overlap + area ratio `0.81 <= pred_area / golden_area <= 1.21`.
   - **Edge / line** (`w*h = 0`, `w+h > 0`): both golden edge endpoints inside pred bbox + `max(pred_w, pred_h) <= edge_length * 1.1`.
   - **Dot** (`w = h = 0`): cannot match. Normally eliminated upstream by `process_klayout_reports.py --fix-dots`.
3. **Hopcroft-Karp maximum bipartite matching** per rule for optimal (order-independent) assignment.
4. **`geometry_required_edge_aware` policy**: when geometry is unavailable on either side, `tp=0` for that rule. Affected rules are reported in `geometry_unavailable_rules` in the output JSON.

**Detection JSON format:**

```json
[
  {
    "rule_name": "M1.S.4",
    "violation_count": 1,
    "violations": [
      {"type": "edge_pair", "edge1": [x1,y1,x2,y2], "edge2": [x1,y1,x2,y2]}
    ]
  },
  {
    "rule_name": "ACTIVE.A.1A",
    "violation_count": 1,
    "violations": [
      {"type": "bbox", "bbox": [xmin,ymin,xmax,ymax]}
    ]
  }
]
```

Coordinates in microns (um). Spacing violations (`.S.` rules) use `edge_pair`; all others use `bbox`.

---

## Data Flow

```
info.json (includes model_name, temp_dir) + prompt_*.md
        |
        v
  prompt_format.py --> task/<model_name>/<case>_<task>_prompt.md
        |                (DRC report = .drc.json from drc_report/)
        |                ({temp_dir} = workspace/temp/ for intermediate files)
        v
  agent_cursor.py / agent_claude.py --model <model_name> --temp_dir <path>
        |
  +-----+----------------------------+
  | REPAIR                           | DETECTION
  v                                  v
  LLM modified .py          LLM detection .json
  |  (result_dir/)           (result_dir/, with DRV regions)
  v                                  |
  KLayout renders .gds               |
  |  (result_dir/temp/)              |
  v                                  |
  run_klayout_drc.py                 |
  |  -> .lyrpt (temp/)               |
  v                                  |
  process_klayout_reports.py         |
  |  -> .drc.json (temp/)            |
  v                                  |
  +----+----+----+                   |
  |    |         |                   |
  v    v         v                   v
sanity conn.  score_repair.py   score_detection.py
check  check  (golden .drc.json (golden .drc.json
  \    /       vs repaired       vs detection
   \  /        .drc.json)        .json + geometry
 merge into                       edge-aware matching)
 score JSON                            |
        |                              |
        v                              v
  score/<run_id>/...            score/<run_id>/...
  (+ agent_status, runtime_seconds, (+ agent_status, runtime_seconds,
   input/output/cache_*_tokens)   input/output/cache_*_tokens)
        |                            |
        +--------------+-------------+
                       v
                 logs/runtime.csv
```
