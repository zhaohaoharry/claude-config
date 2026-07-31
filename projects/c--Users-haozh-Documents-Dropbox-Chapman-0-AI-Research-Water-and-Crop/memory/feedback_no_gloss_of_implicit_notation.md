---
name: feedback-no-gloss-of-implicit-notation
description: Do not add prose explaining what the equation or notation already implies; explain only critical points. Keep the writing neat.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-07-30T04:58:41.176Z
---

Never write a sentence that spells out what the math already says. Repeatedly cut in
2026-07-30: "This expected cost is one point on a per-district state-contingent schedule
$\overline{AC}^*_k(\omega,h)$..." (the notation shows the function), ", fallow included, so
that leaving a fallow plot fallow is its own continuation" (implicit in $c\in\mathcal{A}$),
"Fallowing an already fallow plot therefore carries no intercept, and every other intercept
is read against that baseline" (implicit in the normalization), and three sentences of
establishment-period bookkeeping after the perennial zero-revenue rule.

**Why:** the user wants neat writing at top-5 density. A gloss of the obvious signals the
author does not trust the reader, and it buries the one or two points that DO deserve
explanation. "Only add explanation in critical messages."

**How to apply:** after drafting any explanatory clause, ask whether a reader who read the
preceding equation would already know it. If yes, delete. Explain a step only when it is
non-obvious, contested, or a convention the reader could not guess (e.g. WHY $\beta_W$
rather than $\beta_R$ sets the money metric -- that one earned a footnote).
Related: [[feedback_no_decision_sentences]], [[feedback_evaluate_prose_before_showing]],
[[feedback_no_research_note_language]].
