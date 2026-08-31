---
name: feedback_no_ai_acknowledgement_unless_required
description: "Do not include an AI-use acknowledgement in a manuscript or cover letter unless the target journal's own instructions ask for one; check the journal page first, keep a flag to restore"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: aece50ad-a4d5-4944-a434-58dd8a4fb288
  modified: 2026-08-30T12:16:29.094Z
---

On 2026-08-30 the user asked whether the AI-use acknowledgement in the RES package was
necessary and said "remove if the journal does not ask." RES's submission page and DCAP say
nothing about AI use, so the Acknowledgements paragraph came out of the manuscript and the
matching sentence out of the cover letter (kept behind `--ai-statement` in the flatten script).

**Why:** the user does not want a disclosure the journal has not requested; it draws attention
without being required.

**How to apply:** for any submission package, read the journal's own instructions (and note the
publisher's journal-level policy: some OUP journals, e.g. Biometrika, require a "Declaration of
the use of generative AI" but exempt grammar/spelling tools). Include an AI statement only when
the journal asks; otherwise omit it from both manuscript and cover letter, keep the text behind a
build flag, and tell the user what the publisher policy says. See [[res_submission_package]].
