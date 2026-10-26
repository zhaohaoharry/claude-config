---
name: feedback-manuscript-no-tracking
description: "Online Healthcare manuscript.tex is written from scratch, so edits are plain text without \\del/\\add marks for now"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2c90432b-2125-4d8b-8592-c76b411c6b5b
  modified: 2026-10-25T11:07:39.875Z
---

In the Online Healthcare project, `latex/manuscript.tex` (the submission draft, created 2026-10-25) is edited as plain text, without `\del`/`\add` track-change marks. The global manuscript-track-changes rule is suspended here for now. `latex/paper_skeleton.tex` stays in skeleton format (markers, results, decision log) and is separate from the manuscript.

**Why:** the user said "manuscript no need track for now, because it is written from scratch" (2026-10-25). Marking deletions against a draft that has no prior version adds noise.

**How to apply:** edit manuscript.tex directly. Ask before reinstating tracking. Once the user circulates a version to coauthors or a journal, ask whether tracking should resume against that version. Open tasks go in the skeleton as `\todo`/`\decision` markers, never in the manuscript. Related: [[feedback_report_only_what_serves_argument]].
