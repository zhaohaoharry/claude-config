---
name: feedback_no_data_cleaning_steps_in_manuscript
description: "Don't report mechanical data-cleaning steps (de-duplication, overlap resolution, record collapsing) in manuscript prose or figure/table notes; only the final delivered data matters. Applies across all research projects."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

Mechanical data-cleaning steps do **not** belong in manuscript prose or figure/table notes. The user removed
the permit-overlap-resolution language I had added to the Figure A1/A2 notes and the appendix, saying: *"no need
to mention the resolve of overlapping in the figure notes. this is just data cleaning steps we dont need to report
at all."* So describe the **final** data unit plainly (e.g. "crop permit fields", "the acreage in the permit field
map") and never narrate how it was de-duplicated, de-overlapped, or collapsed to get there.

**Why:** to a referee, how the raw records were cleaned into the analysis unit is plumbing, not substance. Exposing
it reads as a research-note / lab-notebook detail and clutters the exhibit notes with steps the reader doesn't need.
The cleaning still lives in the code and in `DECISIONS.md` for provenance — just not in the paper.

**How to apply:** when a figure/table or its notes refer to a cleaned unit, name the unit and stop. Drop clauses
like "after overlapping permits are resolved to one field each", "after de-duplication", "the resolved footprint of
a cluster of …". If a cleaning step genuinely changes interpretation (not just mechanics), surface only its
*consequence*, not the procedure. Sibling rules: [[feedback_no_estimation_steps_in_tabnotes]],
[[feedback_no_research_note_language]], [[feedback_no_code_notation_in_papers]], [[feedback_no_file_paths_in_manuscripts]].
