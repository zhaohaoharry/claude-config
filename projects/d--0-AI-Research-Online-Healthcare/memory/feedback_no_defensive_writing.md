---
name: feedback-no-defensive-writing
description: "Do not write data quirks, untestable caveats or robustness asides that answer a critic who knows details the paper never reveals"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2c90432b-2125-4d8b-8592-c76b411c6b5b
  modified: 2026-10-29T04:12:25.593Z
---

Leave out of the manuscript anything written only in case a reader who knows everything asks: data quirks the reader would never learn otherwise (the platform relabelling diseases in May 2020, so all disease labels were kept), regulations that do not bind the data (the 2018 rules on online diagnosis), untestable departures, rounding bounds, alternative measures, and "the results are the same with X" asides. The user calls this defensive writing and says it is not standard writing.

**Why:** On 2026-10-29, the user flagged the COVID-label sentence in the Data section ("if we dont reveal, no one will know anyways") and asked for a sweep of the whole manuscript. 18 such passages were cut.

**How to apply:** Keep a caveat only when it changes how a main result is read (for example, why the online home premium is an upper bound). Keep sample rules but state the rule with at most one plain reason. Robustness goes in one sentence pointing to an appendix table, not as a list of specifications. Related: [[feedback-report-only-what-serves-argument]].
