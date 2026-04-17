## Your Role

You are an expert Electronic Design Automation (EDA) engineer with deep knowledge of
physical design and Design Rule Check (DRC) methodologies. You specialize in the ASAP7
process design kit (PDK) and are proficient with KLayout's Python scripting
API (pya). Your task is to **detect** which DRC rules are violated in the given layout
and estimate the number of violation instances for each violated rule - without running
any external DRC tool.

Your detections will be evaluated against the ground-truth KLayout DRC output. You must
also provide the **DRV (Design Rule Violation) region** for each violation instance:
- For **spacing violations** (rules containing `.S.`): provide an **edge pair** — the two
  edges that are too close to each other.
- For **all other violations** (width, enclosure, area, etc.): provide a **bounding box**
  of the violation region.

All coordinates in your output must be in **dbu (database units)**, the same integer
coordinate system used by the layout script (1 dbu = 0.00025 um). No unit conversion needed.

Aim for high precision and recall across all rule categories.

---

## Input Files

You have access to the following resources. Read each one carefully before proceeding.

### 1. Skill / DRC Knowledge
Path: {path_to_skill}
Purpose: Comprehensive DRC knowledge document with ASAP7 layer mappings, rule
         categories, design rule quick reference, and detection strategies.

### 2. KLayout Python Layout Script
Path: {path_to_layout_script}
Purpose: The Python source script (using the `pya` API) that generates the layout.
         Analyze the polygon coordinates and layer assignments in this script to
         measure geometric properties (widths, spacings, enclosures, pitches) and
         identify potential rule violations. Coordinates use the `dbu` convention
         defined at the top of the script (typically `layout.dbu = 0.00025` um).

### 3. Layout Screenshot
Path: {path_to_layout_screenshot}
Purpose: A visual PNG rendering of the layout with all layers visible. Use this to
         build spatial intuition about shape placement.

### 4. Design Rule Document
Path: {path_to_design_rule}
Purpose: The KLayout DRC rule file (.lydrc) that defines every design rule to be
         checked. This is the authoritative source for rule names, layer references,
         and numeric thresholds. Use the exact rule names from this file in your output.

### 5. Design Rule Manual (DRM) Images
Path: {path_to_drm_jpg}
Purpose: Directory of per-rule JPG images from the ASAP7 Design Rule Manual. Each
         file is named after its rule (e.g., M1.S.4.jpg). Use these alongside the
         design rule file to visually understand the geometric intent of each rule.

---

## What You Must Do

Follow these steps in order:

### Step 1 - Study the Design Rule File
**You must read the entire design rule file** at `{path_to_design_rule}` before
attempting any violation analysis. This is the authoritative source for every design
rule that could be violated. For each rule defined in the file, understand:
- The rule name (e.g., `M1.S.4`, `V0.EN.1`, `GATE.S.1`).
- Which layers are involved and how they are derived (boolean operations, layer
  interactions, connectivity definitions).
- The exact geometric check being performed (KLayout DRC operations such as `space`,
  `width`, `enclosed`, `area`) and the numeric threshold.
- Whether the rule applies to shapes on the same layer, across layers, or to
  derived (boolean) layers.

Also read `{path_to_skill}` for supplemental context on ASAP7 layer mappings, rule
categories, and common violation patterns. The design rule file is the primary
reference — do not guess rule names, thresholds, or layer associations.

### Step 2 - Inventory the Layers Present in the Layout
Read `{path_to_layout_script}` and identify which layers are used (M0, M1, V0, LIG,
LISD, GATE, WELL, FIN, ACTIVE, GCUT, SDT, etc.). Note the layer numbers and datatypes
used in each `layout.layer(pya.LayerInfo(...))` call. Cross-reference these layers with
the design rule file to determine which rules from Step 1 are applicable to this layout.

### Step 3 - Extract Geometric Properties for Each Layer
For each layer present in the design, extract the relevant geometric properties:
- **Width**: the smaller dimension of each rectangle or polygon bounding box.
- **Spacing**: the gap between each pair of non-touching shapes on the same layer.
- **Enclosure**: the extension of one layer's shape past the edge of an enclosed shape.
- **Pitch**: center-to-center distance between adjacent shapes (relevant for GATE, FIN).
- **Area**: total area of each shape polygon.

Compute these measurements using the coordinates from the script. All values in dbu.

### Step 4 - Compare Measurements Against Each Design Rule
For every applicable rule identified in Steps 1-2, determine whether any shape or
shape pair in the layout violates the rule. Use the exact thresholds from the design
rule file — not approximations. For each rule:
- Determine if at least one violation exists.
- If violated, count the number of individual violation instances.
- For each violation instance, identify the DRV region:
  - **Spacing violations** (`.S.` rules): record the two edges that are too close as
    an edge pair. Each edge is `[x1, y1, x2, y2]` in dbu.
  - **All other violations**: record the bounding box of the violating region as
    `[xmin, ymin, xmax, ymax]` in dbu.

### Step 5 - Format and Return the Detection
Return your detections as a JSON list.

---

## Hard Constraints

1. **Use exact ASAP7 rule names.** Rule names must match those defined in
   `{path_to_design_rule}` exactly (e.g., `WELL.W.1`, `FIN.S.1`, `M1.S.4`).

2. **Do not fabricate violations.** Only detect a violation if geometric analysis
   provides evidence.

3. **violation_count must be a positive integer.** Must be >= 1.

4. **Provide DRV regions.** Each violation must include geometry:
   - Spacing violations (`.S.` rules): `"type": "edge_pair"` with `edge1` and `edge2`.
   - Other violations: `"type": "bbox"` with `bbox`.

5. **Coordinates in dbu.** All coordinates must be in dbu (database units), the same
   integer coordinate system used by the layout script.

6. **Do not run any external tool.** This is a static analysis task.

---

## File Output Rules

**Intermediate / scratch files:** If you need to create any intermediate, temporary, or
scratch files during your analysis (e.g., coordinate calculations, measurement notes,
draft detections), you **must** place them in the following directory:

```
{temp_dir}
```

Do **not** write intermediate files anywhere else in the project directory tree.

**Final output:** The completed detection JSON must be saved to the result path below —
and **only** to this path.

---

## Expected Output

**Save the detection result as a JSON file to the following path:**

```
{output_path}
```

The JSON file must contain a single array of violation objects. Do not include any
prose or explanation in the file — only valid JSON.

Example format:

```json
[
  {
    "rule_name": "M1.S.4",
    "violation_count": 1,
    "violations": [
      {
        "type": "edge_pair",
        "edge1": [0.0, 0.050, 0.020, 0.050],
        "edge2": [0.0, 0.078, 0.020, 0.078]
      }
    ]
  },
  {
    "rule_name": "ACTIVE.A.1A",
    "violation_count": 1,
    "violations": [
      {
        "type": "bbox",
        "bbox": [0.0, 0.0, 0.0675, 0.0675]
      }
    ]
  },
  {
    "rule_name": "V0.M0.EN.5",
    "violation_count": 2,
    "violations": [
      {
        "type": "bbox",
        "bbox": [0.064, 0.035, 0.066, 0.053]
      },
      {
        "type": "bbox",
        "bbox": [0.064, 0.215, 0.066, 0.233]
      }
    ]
  }
]
```

If no violations are detected, write an empty JSON array:

```json
[]
```
