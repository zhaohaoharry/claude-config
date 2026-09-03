---
name: feedback-introduce-symbols-at-first-use
description: "In model prose, introduce every parameter/symbol only in the sentence or paragraph where its first equation uses it; never stockpile definitions ahead of use"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 366d52e4-00c4-455f-b6b6-aa97d4559cd9
  modified: 2026-09-02T03:04:55.827Z
---

A symbol or parameter is introduced only where it is first used: in the
sentence leading into, or immediately after, the equation in which it
first appears. Never define a symbol in a paragraph that contains no use
of it, never define it one or more paragraphs ahead "for later", and
never write a lone "Let X denote..." sentence detached from an equation.
The same discipline covers productivity of an agent whose production
function is not yet written (write the production function first), and
regularity conditions on parameters not yet introduced.

**Why:** The user (2026-09-02, Carbon Pricing Policy structural_model.tex)
flagged "Shipping a task from j to i requires d_ijk ≥ 1 ... The pre-carbon
price ... is w_jkt > 0" sitting in the Fréchet paragraph where neither
appears: "it is weird to introduce these two parameters in the paragraph
where they are not shown in an equation or used. please introduce
parameters only when they are used. avoid any of this issue throughout
this model." Earlier the same day: "why introduce the productivity of the
wholesaler as we don't show its production function?" and "do we
introduce theta yet?" for a regularity condition stated before θ existed.

**How to apply:** After drafting any model section, audit every symbol:
definition line vs. first-use line; move the definition to the first-use
paragraph. Also check for symbols used before any definition, and for
one letter carrying two live meanings (the same audit surfaced D/B reused
for flow counts, ζ for three objects, r for four). Related:
[[feedback-no-process-narration]], [[feedback-no-gloss-of-implicit-notation]].
