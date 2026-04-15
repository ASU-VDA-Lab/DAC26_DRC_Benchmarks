# example/ -- Customizable Files

This directory contains files that can be customized by the user. To use your customized versions, modify the files here and copy them to `src/`.

The pipeline always reads from `src/` at runtime -- files in `example/` are **not** used directly.

---

## Table of Contents

- [*info.json*](./info.json): Shows all required keys for info.json. For single-case runs, prepare your own info.json based on this template. For paper experiments, `src/build_case_info.py` generates it automatically.
- [*build_case_info.py*](./build_case_info.py): Reference copy of the info.json generator used by `evaluate_cursor.sh` for paper experiments. Uses argparse named arguments. Customize to change how info.json is built (e.g., different system prompts, custom paths).
- [*agent_cursor.py*](./agent_cursor.py): Reference copy of the Cursor Agent CLI wrapper. Customize to change how LLM models are invoked (e.g., different CLI tools, API calls, custom timeout behavior).
- [*agent_claude.py*](./agent_claude.py): Reference copy of the Claude Code CLI wrapper. Same interface as `agent_cursor.py` but uses Claude Code CLI.
- [*skill.md*](./skill.md): ASAP7 DRC knowledge document -- layer mapping, rule categories, repair/detection strategies, and connectivity verification instructions. Referenced by prompt templates via `{path_to_skill}`.
- [*prompt_repair_cell.md*](./prompt_repair_cell.md): Repair prompt template for cell designs. Constrains edits to M1 and V0 only; M0 polygons must not be modified. Includes `{path_to_connectivity_file}` and `check_connectivity.py` verification.
- [*prompt_repair_polygon.md*](./prompt_repair_polygon.md): Repair prompt template for polygon designs. Only resize or move polygons; deletion and adding new polygons are forbidden.
- [*prompt_repair_block.md*](./prompt_repair_block.md): Repair prompt template for block designs. Only metal and via layers may be modified. Includes `{path_to_connectivity_file}` and `check_connectivity.py` verification.
- [*prompt_detection.md*](./prompt_detection.md): Detection prompt template. Agent detects DRC violations with DRV regions.
- [*prompt_format.py*](./prompt_format.py): Reference copy of the prompt template engine. Reads an `info.json` and a prompt template, substitutes `{placeholder}` tokens, and prints the result.

---

## How to Customize

1. Edit the files in this directory to suit your needs (e.g., change prompt instructions, add domain knowledge to `skill.md`, adjust placeholder handling in `prompt_format.py`).
2. Copy the modified files to `src/`:
   ```bash
   cp example/skill.md src/skill.md
   cp example/prompt_repair_cell.md src/prompt_repair_cell.md
   cp example/prompt_format.py src/prompt_format.py
   # ... etc.
   ```
3. Run the pipeline as usual -- it reads everything from `src/`.

---

## Placeholder Variables

Prompt templates use `{key}` syntax. `prompt_format.py` replaces each `{key}` with the corresponding value from `info.json`. Only these keys are allowed -- any other `{word}` pattern raises `ValueError`.

`info.json` also contains `model_name`, `case_name`, `design_type`, and `task_type` fields. These are used by `run_pipeline_cursor.sh` to determine container paths and pipeline behavior, but are **not** used as template placeholders.

| Placeholder | Repair | Detection | Description |
|-------------|:------:|:----------:|-------------|
| `{path_to_skill}` | Yes | Yes | Path to DRC knowledge document (`skill.md`) |
| `{path_to_layout_script}` | Yes | Yes | Path to KLayout Python layout script |
| `{path_to_layout_screenshot}` | Yes | Yes | Path to PNG rendering of the layout |
| `{path_to_drc_report}` | Yes | No | Path to KLayout DRC report (`.drc.json`) |
| `{path_to_design_rule}` | Yes | Yes | Path to KLayout DRC rule file (`.lydrc`) |
| `{path_to_drm_jpg}` | Yes | Yes | Directory of per-rule DRM JPG images |
| `{path_to_connectivity_file}` | Cell/Block | No | Path to golden connectivity JSON (cell/block repair only; not used for polygon or detection) |
| `{output_path}` | Yes | Yes | Path where the agent must save its output (`.py` for repair, `.json` for detection) |
| `{temp_dir}` | Yes | Yes | Directory for intermediate/scratch files |

---

## Detection Output Format

The detection task requires the LLM to output **DRV (Design Rule Violation) regions** for each violation:

- **Spacing violations** (`.S.` rules): edge pair -- two edges as `[x1, y1, x2, y2]` in microns
- **All other violations**: bounding box -- `[xmin, ymin, xmax, ymax]` in microns

Evaluation uses geometry-based matching (**Hopcroft-Karp** maximum bipartite matching). Polygon golden bboxes use an area ratio tolerance of `[0.81, 1.21]`; edge-shaped golden bboxes use endpoint containment in the predicted bbox plus a longest-side cap of `edge_length × 1.1`.
