---
name: feedback-always-show-es-figures
description: "When reporting any event-study result, always build and show the ES figure (2x2 by outcome, overlaid against the main spec), not just a table of post means and lead counts"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-10-31T23:25:00.482Z
---

Whenever an event-study specification's results are reported (robustness, alternative samples, fixes, datings), build the event-study figure and show it — never report only post means and lead counts in chat.

**Why:** the user judges pre-trends and dynamics from the paths; a table of counts hides the shape (stated 2026-11-01, Carbon Pricing Policy, after asking for the accession-FE results: "Show me ES figures always").

**How to apply:** use a generator script that reads the run outputs, makes a 2x2 figure (import value, import links, export value, export links) overlaying the variant(s) on the main specification with 95% CIs, compiles a short PDF under `latex/answers/<topic>/`, opens it with `code -r` and syncs to AI_share when the user is reviewing there. Pattern: `program/sandbox/hs4_20261027/make_accession_review.py`. Related: [[feedback-open-pdf-in-preview]], [[reference-ai-share-folder]].
