---
name: feedback_no_footprints_of_abandoned_designs
description: "When a design, result or mechanism is dropped from a paper, remove every trace of it from the prose; do not mention what the policy \"does not do\" or contrast with results the paper no longer presents or models"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-09-16T03:19:11.726Z
---

When a design, result or mechanism is abandoned, the manuscript must not carry footprints of it. Do not write clauses such as "rather than removing origins" or "while the set of suppliers barely changes" when the paper no longer presents the aggregate result or models that margin. The paper discusses the mechanism it examines and the results that mechanism predicts; it does not enumerate what else the policy does or does not do unless that is relevant to the mechanism under study.

**Why:** In the Carbon Pricing Policy introduction (2026-09-16) the claim sentence ended "adoption reallocates sourcing across products and origins rather than removing origins", a residue of the abandoned access-cost/link-removal design. The user: such residues are weird to a reader, since the paper presents no results on aggregate shrinkage and has no model for it, and a paper cannot discuss every possible result unrelated to its theory.

**How to apply:**
- After a design change, grep the draft for the abandoned objects (their names, their contrasts, "rather than", "does not", "barely") and delete or rewrite every sentence that only exists because of the old design.
- State results positively as what the mechanism predicts; keep negative statements only when they discriminate between mechanisms the paper actually compares.
- Related: [[feedback_write_for_human_readers]], [[feedback_no_process_narration]], [[feedback_no_loose_sentences]].
