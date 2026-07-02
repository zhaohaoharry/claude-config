---
name: Dot grid is in-house, NOT Land IQ
description: The Water-and-Crop project's 300m sampling-dot grid is constructed in-house from Kern permit polygons; never call it "Land IQ".
type: feedback
---

The 300m sampling-dot grid used in the Water-and-Crop project is **constructed in-house** by `program/sandbox/create_sampling_dots.py`. Procedure: take the union of all Kern permit polygons across 1997-2022 (the "ever-farmed" footprint), generate a regular 300m grid of points within that footprint, assign each dot to a water district, then for each year spatially join the dots to that year's permit polygons to recover crop labels. Output: `data/clean/dot_panel.dta` (50,427 dots × 26 years ≈ 1.34M dot-years).

**Never call it "Land IQ" or "Land~IQ".** Land IQ is an unrelated public California Department of Water Resources land-use mapping product. The term appeared in a 2026-05-11 archived AI-generated answer file (`latex/archive/2026-05-11_pre-review/answers/answer_estimation_manual.tex`) and was hallucinated into manuscript drafts. The user does not recognize the term and it is factually wrong.

**Why:** A 2026-05-14 manuscript polish session inserted "Land~IQ dot panel" into Section 3.1 prose, the figure caption, and an appendix paragraph; the user caught it. The correct framing is descriptive, not branded: "constructed 300m sampling grid", "regular 300m sampling grid overlaid on the union of Kern permit polygons", or simply "the dot grid".

**How to apply:** Whenever describing the dot panel, use neutral descriptive language tied to the construction procedure (regular 300m grid, sampled within the ever-farmed Kern permit footprint). Do not attribute it to any external dataset unless the user explicitly says so. If unsure of any data provenance in this project, check `program/sandbox/create_sampling_dots.py` and the `program/README.md` rather than guessing.
