---
name: avoid-em-dashes-colons-and-semicolons-in-academic-prose
description: "In final manuscript prose, default to ZERO em-dashes, colons, and semicolons. All three are AI-style and reviewer-noticeable. Use periods and conjunctions instead. Applies across all research projects."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---

In manuscript prose, default to **zero** em-dashes (`---`), colons (`:`), and semicolons (`;`). All three let the writer pack multiple thoughts into a single sentence rather than committing to short declarative sentences. Reviewers at top journals have a trained eye for the resulting rhythm and read it as AI-generated.

Before keeping any of the three marks in prose, ask: does the period-and-conjunction rewrite lose anything substantive? If no, rewrite.

**Why:** AI drafts overuse all three. Colons to introduce lists or elaborations; em-dashes for parenthetical insertions or emphatic appositions; semicolons to chain related clauses. The resulting prose has a recognizable AI-rhythm that reads as overstuffed and reviewer-noticeable. Human academic prose uses these marks sparingly, and top-econ writing (BPW R&R at REStud, Hagerty 2023, Rafey 2023) uses them almost not at all in the running body.

**Replacement playbook:**
- Em-dash (`X --- Y`) → comma, parenthesis, or two sentences.
- Colon (`X: Y`) → period + new sentence, or a subordinating conjunction (`because`, `since`, `namely`, `that is`).
- Semicolon (`X; Y`) → period + new sentence, or a coordinating conjunction (`and`, `but`, `because`).

**How to apply:**
- At draft-end, run `grep -c -- '---' manuscript.tex`, `grep -c ';' manuscript.tex`, and a colon count. Treat each hit as a rewrite candidate.
- Acceptable uses to keep (rare):
  - Colon introducing a formal definition, a labeled equation, or a quoted phrase.
  - Em-dash inside a constructed name (rare; usually not).
  - Semicolon separating items in a long list inside a parenthetical (usually means rewrite).
- Tables, figure captions, and notes are also subject to this rule.
- Applies across all research projects, all final-manuscript files (.tex prose, abstract, intro, results, conclusion).

**Does NOT apply to:** code comments, chat responses, scratch notes, decision/todo markers in skeletons, math (formula colons like `f: X \to Y` or ratios like `2:1`), or en-dashes for number ranges (`1998--2022`, `pp. 12--15`).

**History:** the user flagged colons and em-dashes initially (2026-05-19) and extended the rule to semicolons on 2026-05-31 with the explicit instruction: "they are AI-style and I want to avoid as possible as I can. this should be set up in the high-level writing guide." Pushed to `0.AI/Claude Master/AI_Writing_Guide_Academic.md` (§0 stop-sign list, §2.2 punctuation section, §11 after-writing checklist, §12 cheat sheet).
