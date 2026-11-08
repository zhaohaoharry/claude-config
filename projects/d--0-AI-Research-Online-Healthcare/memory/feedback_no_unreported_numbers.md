---
name: feedback-no-unreported-numbers
description: "Main text cites only numbers a reader can find in a table; robustness goes in its own paragraph after the result, pointing to the table"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2c90432b-2125-4d8b-8592-c76b411c6b5b
  modified: 2026-11-08T04:46:02.651Z
---

Never cite a result in the main text that no table reports. Either add it to a table (main or appendix) or drop it. A robustness claim without a table may go in a footnote phrased as "under X, the estimate is Y, consistent with the main findings; full results are available on request", but only when the user asks for that.

Structure for results subsections: the first paragraph reports the table's main finding only. A separate paragraph then names the key threat and gives the robustness checks, each tied to its table and panel ("as shown in Panel B of Appendix Table X").

**Why:** a number that a reader can't find in a results table looks suspicious (user, 2026-11-08, about the −1.27 procedure-department excess in Section 5.1).

**How to apply:** when drafting or auditing prose, check that every macro or number cited maps to a cell in a table referenced nearby. Related: [[feedback_report_only_what_serves_argument]], [[feedback_short_paragraphs]].
