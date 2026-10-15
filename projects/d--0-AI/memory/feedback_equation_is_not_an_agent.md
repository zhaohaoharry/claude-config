---
name: feedback-equation-is-not-an-agent
description: Never write "equation (N) lowers/raises X"; the economic cause (a carbon price, a shock) is the subject and the equation is only where it is seen
metadata:
  type: feedback
---

In model prose the subject of a causal sentence is the economic cause, never
the equation. Write "A carbon price in the importing country raises the
domestic factor cost in equation (10) and so lowers the domestic sourcing
potential", not "equation (10) lowers the domestic sourcing potential".
Equations can be referenced as the place where the effect appears, not as
the thing that acts.

**Why:** The user (2026-09-02, Carbon Pricing Policy structural_model.tex):
"why equation lower? this is not accurate. we can say domestic tax lower".

**How to apply:** After drafting, grep for "equation ... (lowers|raises|
makes|reduces|increases|implies)" and "the same equation ..." and recast
each with the economic agent as subject. Related:
[[feedback-introduce-symbols-at-first-use]], [[feedback-no-process-narration]].
