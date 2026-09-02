---
name: feedback-no-process-narration
description: "Never write researcher-process narration (\"We spell out...\", \"it is worth stating...\") in manuscript prose"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 366d52e4-00c4-455f-b6b6-aa97d4559cd9
  modified: 2026-09-01T10:19:55.724Z
---

Manuscript prose must not narrate the researcher's decision or writing
process. Banned patterns: "We spell out X in full", "it is worth stating
precisely", "we now turn to writing", "let us now introduce" — any sentence
whose subject is the act of writing/deciding rather than the economics.

**Why:** The user (2026-09-01, Carbon Pricing Policy structural_model.tex)
flagged "We spell out the Copeland--Taylor structure in full" as "language
reflecting researcher decision process [that] should not be included in any
writing."

Also banned: sentences that justify a specification choice against an
alternative the paper never presents ("This specification is well defined
without carbon pricing") — the property is implicitly revealed by the
equations; defending the choice narrates the decision process.

Also banned (added 2026-09-01, same session): forward-pointing
self-defense of the math — sentences that walk the reader through where a
variable appears and pre-announce that a later assumption will neutralize
it ("The own price appears only in the allocation term; it also sits
inside the price index, a dependence that Assumption 1 below makes
negligible"). This is the author reassuring the referee mid-derivation.
If the dependence matters, the assumption itself and its discussion (at
the point where the assumption is stated) carry it; the derivation just
derives.

**How to apply:** State the economics directly: "Emissions and abatement
follow Copeland and Taylor (2004)" instead of "We spell out the
Copeland--Taylor structure". Replace "it is worth stating what X changes"
with the statement itself. Standard roadmaps ("Section 2 derives...") and
result-announcing ("Three implications follow") remain acceptable.
Related: [[feedback-cumulative-sentences-and-verbs]].
