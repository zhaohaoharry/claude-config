---
name: term-consistency-with-baseline
description: "Before introducing any term in new manuscript text, grep the unchanged baseline for existing renderings of the same concept and unify"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3c98c8fa-3aa0-4de9-946d-d576929d04b8
  modified: 2026-09-04T04:43:14.496Z
---

When writing new (green) text into a tracked manuscript, grep the whole file for every existing rendering of the concept before choosing a word. Example (2026-09-04, Governor and Border Emissions): a new sentence introduced "deputy-national rank" while the untouched baseline already said "vice-national" and "sub-national" for the same 副国级 rank. The author caught it: "please compare new writing with existing unchanged ones to avoid such term inconsistency."

**Why:** the author reads the compiled PDF as one document. A term coined in a green sentence that disagrees with black baseline text reads as two concepts, and the baseline is easy to forget because it is not on screen while composing.

**How to apply:** before saving any new prose containing a technical or institutional term (rank names, treatment labels, variable names, place names), run a grep over the manuscript for synonyms and translations of that term. If the baseline already uses one, either adopt it or convert every baseline occurrence with tracked marks in the same edit. Never leave two renderings live. Related: [[cumulative-sentences-and-verbs]], [[minimal-track-changes]].
