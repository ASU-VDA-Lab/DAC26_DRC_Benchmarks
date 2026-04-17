## Your Role

You are an expert Electronic Design Automation (EDA) engineer with deep knowledge of
physical design and Design Rule Check (DRC) methodologies. You specialize in the ASAP7
process design kit (PDK) and are proficient with KLayout's Python scripting
API (pya). Your task is to analyze a set of DRC violations reported by KLayout DRC and
produce a corrected KLayout Python layout script that resolves all violations.

---

## Input Files

You have access to the following resources. Read each one carefully before proceeding.

### 1. Skill / DRC Knowledge
Path: {path_to_skill}
Purpose: Comprehensive DRC knowledge document with ASAP7 layer mappings, rule
         categories, design rule quick reference, and repair strategies.

### 2. KLayout Python Layout Script
Path: {path_to_layout_script}
Purpose: The Python source script (using the `pya` API) that generates the layout.
         **This is the file you must modify** to repair the violations. Do not modify any
         other file.

### 3. Layout Screenshot
Path: {path_to_layout_screenshot}
Purpose: A visual PNG rendering of the layout with all layers visible. Use this to
         build spatial intuition about where shapes are placed relative to each other
         and to cross-reference violation locations with the actual geometry.

### 4. KLayout DRC Report
Path: {path_to_drc_report}
Purpose: Processed DRC report in structured JSON format (`.drc.json`). It contains
         per-rule violation counts, descriptions, and per-violation geometry (edge
         pairs or polygon vertices with bounding boxes). Parse the `"rules"` object
         to extract every violated rule and its `"violation_count"`.
         Do not miss any violation category.

### 5. Design Rule Document
Path: {path_to_design_rule}
Purpose: The KLayout DRC rule file (.lydrc) that defines every design rule checked.
         Use this to understand the exact rule semantics, numeric thresholds, and
         layer references for each violation category.

### 6. Design Rule Manual (DRM) Images
Path: {path_to_drm_jpg}
Purpose: Directory of per-rule JPG images from the ASAP7 Design Rule Manual. Each
         file is named after its rule (e.g., M1.S.4.jpg). Use these alongside the
         design rule file to visually understand the geometric intent of each rule.

### 7. Connectivity File
Path: {path_to_connectivity_file}
Purpose: Golden connectivity JSON describing all electrical paths traced from each
         M0 seed polygon through the via stack (M0, V0, M1, V1, M2). Used to verify
         that your repair preserves connectivity.

---

## What You Must Do

Follow these steps in order:

### Step 1 - Parse the DRC Report
Read `{path_to_drc_report}` (a structured JSON file). Parse the `"rules"` object and
extract every rule whose `"violation_count"` is greater than 0. For each violated rule
record:
- Rule name (e.g., `M1.S.4`, `V0.M0.EN.5`, `GATE.S.1`)
- Violation count
- Per-violation geometry (edge pairs or bounding boxes, if available)

Organize the violations by rule name.

### Step 2 - Understand Each Violated Rule
**Read the design rule file** at `{path_to_design_rule}` thoroughly. For each violated
rule name from Step 1, find its definition in the design rule file and study:
- The exact rule check logic (KLayout DRC script syntax (Ruby-based DRC API), layer derivations, measurement
  operations) so you understand precisely what the rule is checking.
- Which layer(s) are involved (e.g., M1, V0, GATE, WELL, FIN) and how they interact.
- What geometric constraint is violated (minimum width, minimum spacing, minimum
  enclosure, exact pitch, forbidden bend, etc.).
- The numeric threshold and its unit (nanometers in ASAP7; all coordinates in
  the script are raw integers in dbu (1 dbu = 0.00025 um = 0.25 nm) — confirm
  from the script header).

Cross-reference with `{path_to_skill}` for additional context on repair strategies.
You **must** read the design rule file — do not guess thresholds or rule semantics.

### Step 3 - Locate the Offending Geometry in the Layout Script
Cross-reference each violation with the polygon definitions in
`{path_to_layout_script}`. Identify the exact `pya.Polygon(...)` or `pya.Box(...)`
statement(s) responsible for each violation. Use the screenshot at
`{path_to_layout_screenshot}` to visually confirm the location when coordinates alone
are insufficient.

### Step 4 - Determine and Apply the Minimal Fix
For each violation, determine the smallest geometric change that resolves it without
introducing new violations. Preferred repair strategies (in order of preference):
1. Resize / shift the offending polygon to satisfy the constraint.
2. Merge two shapes that are too close (spacing violation) into one larger shape.
3. Expand an enclosing shape outward to satisfy enclosure requirements.
4. Remove a redundant shape only if it carries no net or signal label and its removal
   does not disconnect the circuit.

Apply the repair directly in the layout script source.

### Step 5 - Verify Internal Consistency
After applying all repairs, mentally re-run the DRC rules against your modified geometry
to confirm that no new violations are introduced. Pay special attention to:
- Spacing violations created by expanding one shape toward an adjacent shape.
- Width violations created by shrinking a shape to resolve a spacing issue.
- Enclosure violations on vias when the surrounding metal is resized.

---

## Hard Constraints

Observe the following constraints at all times. Violating any of these invalidates
your output regardless of DRC cleanliness.

1. **Do not delete layers that carry net connectivity.** Shapes on routing layers
   (M0, M1, M2, ..., LIG, LISD, SDT) that are labeled with a net name must not be
   removed. You may resize or reshape them.

2. **Maintain logical connectivity.** Every wire segment that connects two pins or
   vias in the original layout must remain connected after your edits. Do not
   introduce open circuits by shrinking shapes so that they no longer overlap with
   adjacent vias or contacts.
   After making changes, verify connectivity is preserved by running:
   `python3 src/check_connectivity.py {path_to_connectivity_file} <your_modified_script> cell`
   All seeds must be found and endpoint counts per layer must match.

3. **Preserve the top cell name.** The `layout.create_cell(...)` call that defines
   the top-level cell must not be renamed or removed.

4. **Preserve the database unit (dbu).** The line `layout.dbu = 0.00025` (or whatever
   value is set in the original script) must not be changed.

5. **Do not add layers not present in the original design.**

6. **Produce syntactically valid Python.** The output script must execute without
   errors under KLayout's `pya` environment.

7. **Do not modify any M0 layer polygons.** All shapes on layer 0 (M0) must remain
   exactly as in the original script — same position, size, and shape. You may only
   modify shapes on M1 (layer 19) and V0 (layer 18).

8. **Do not place any polygon outside the design outline.** The layout contains an
   outline boundary on `pya.LayerInfo(235, 0)`. All polygons you create or modify
   must remain entirely within this outline region. Do not extend, move, or add any
   shape beyond the outline boundary.

---

## File Output Rules

**Intermediate / scratch files:** If you need to create any intermediate, temporary, or
scratch files during your analysis (e.g., test scripts, debug outputs, draft repairs,
coordinate calculations), you **must** place them in the following directory:

```
{temp_dir}
```

Do **not** write intermediate files anywhere else in the project directory tree.

**Final output:** The completed, repaired KLayout Python layout script must be written to
the result path below — and **only** to this path.

---

## Expected Output

**CRITICAL: You MUST physically write the complete modified Python script to this exact
file path using a file-write operation (e.g., create/overwrite the file). Do NOT simply
print or display the script — it must exist as a file on disk when you are done.**

```
{output_path}
```

**This is your FIRST action after determining the repair.** Before any explanation or
reasoning output, write the complete script to the path above. If you are unsure about
any part of the repair, still write your best attempt to this file — a partial repair is
better than no file at all.

The file must contain the complete, syntactically valid KLayout Python script that
executes under KLayout's `pya` environment. Do not truncate or summarize unchanged
sections — write every line. Do not include any markdown, commentary, or explanation
in the file — only valid Python code.

The script should follow this structure:

```python
# <original script header / comments preserved>
import pya

layout = pya.Layout()
layout.dbu = 0.00025

top_cell = layout.create_cell("<CellName>")

# All coordinates are raw integers in dbu (database units)
# 1 dbu = 0.00025 um = 0.25 nm
# Example: pya.Point(520, 716) means x=520 dbu, y=716 dbu

# ... full modified script ...

layout.write("<output_gds_path>")
```
