---
name: pipeline_doc_program_pipeline
description: Water and Crop curated pipeline doc is program/program_pipeline.tex (was PIPELINE_manual); PIPELINE.tex retired; new pipeline docs follow its format
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

SETTLED 2026-06-28 (Water and Crop). The curated, hand-verified pipeline document is
`program/program_pipeline.{tex,pdf}` — renamed from `PIPELINE_manual.{tex,pdf}`. It is THE pipeline
document going forward, and all new pipeline documentation must follow its format (the `\step` /
`\dstep` / `\estep` colored-badge layout with explicit per-program in/out file lists; Parts 1 Data /
2 Estimation / 3 Results, plus Part 4 In-text prose macros).

Retired: the redundant code-derived PDF rendering `PIPELINE.tex` and its sole generator
`build_pipeline_pdf.py` (it just re-rendered the same data as PIPELINE.md) →
`program/archive/retired_code_pipeline_20260628/`. Do not regenerate or reference PIPELINE.tex.

KEPT: `PIPELINE.md` + `build_pipeline.py` — the code-derived markdown manifest the provenance rule
mandates (run before sync; see [[feedback_code_derived_pipeline_manifest]]). `build_pipeline.py` reads
`latex/manuscript_v1.tex` + `program/**/*.py` and writes `PIPELINE.md`; it is independent of the .tex
docs and nothing reads `program_pipeline.tex`, so the rename needed no code change. `audit_provenance.py`
is the other provenance tool (0-orphan gate). Both had a now-removed vestigial `build_pipeline_pdf.py`
skip entry.
