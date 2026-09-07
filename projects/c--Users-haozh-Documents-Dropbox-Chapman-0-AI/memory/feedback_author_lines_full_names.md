---
name: feedback-author-lines-full-names
description: "Author lines on every note, memo, and draft must list all coauthors with full names; verify the author list against the main draft, not the project CLAUDE.md summary"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-09-07T07:25:06.503Z
---

Every `\author{}` line (coauthor notes, research memos, model notes, skeleton) lists all coauthors by full name, never surnames alone, and never a subset.

**Why:** On 2026-09-07 the Carbon Pricing Policy note and memo carried `Ding \and Dong \and Zhao` because the project CLAUDE.md listed three authors, while the model note had four (Haoning Sun was missing). The user: "why you keep removing one of the coauthor and you dont know the full name of coauthors?"

**How to apply:** Before creating any new document, take the author list from the most recent draft with full names (working paper / model note), not from a config summary. If a config file disagrees with a draft, fix the config. Carbon Pricing Policy authors: Haoyuan Ding (SUFE), Feng Dong (Tsinghua), Haoning Sun (affiliation to confirm), Hao Zhao (RUC). Related: [[feedback-follow-template-strictly]].
