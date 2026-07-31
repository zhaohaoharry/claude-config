---
name: feedback-two-pass-latex-after-label-edits
description: "Always run pdflatex twice after any edit that can move labels/numbering; a single pass leaves a stale .aux and every \\ref renders \"??\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-07-30T04:58:48.215Z
---

Single-pass `pdflatex` after an edit that adds/removes text is NOT enough. On 2026-07-30 a
run of single-pass compiles left the `.aux` stale, so every `\ref` in manuscript_v1.pdf
rendered as "??" and the page count read 83 instead of 84. The user caught it ("the cross
reference in the manuscript is missing"), not me.

**Why:** cross-references, page numbers, and the TOC resolve from the previous run's `.aux`.
Any edit that shifts a label, a float, or a page break invalidates it. The compile still
reports "Output written" and exit 0, so a clean-looking log proves nothing.

**How to apply:** compile twice (`pdflatex ...; pdflatex ...`) after every content edit, and
verify with `Select-String -Path <file>.log -Pattern "undefined" | Measure-Object` returning
0 before reporting a compile as clean. Three passes plus bibtex when the bibliography changed.
Related: [[feedback_evaluate_prose_before_showing]].
