---
name: feedback-keep-source-data-unless-clear-fix
description: "Keep a data source's records as reported unless there is a strong documented reason they are wrong AND a clear way to fix them; do not correct on upper bounds or illustrative splits"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-17T07:42:30.259Z
---

Records from a data source stay as the source reports them, as long as they are used consistently with the project's stated data rules. Change one only when there is both a very good, documented reason that it is wrong and a clear way to fix it. Known but unfixable inaccuracies (sizes given only as upper bounds, or resting on shares the data do not report) are left alone, and no bounding or sensitivity run is added for them unless asked.

**Why:** said by the user on 2026-11-17 in the Carbon Pricing Policy project, about national carbon prices of 2017 in the World Carbon Pricing Database that an internal audit flagged for France, Ireland, Sweden, Denmark, Norway, Slovenia, Portugal and Iceland. His reasoning: the counterfactual checks the leakage mechanism given a set of price data, and the EU exercise uses the actual 2026 certificate price, so imprecision in the 2017 national prices is not a big matter. My interpretation: this extends the earlier rule that only documented source-data corrections are made (see [[feedback-no-own-coding-fixes-in-manuscript]]).

**How to apply:** when an audit finds source records that look wrong, report them, but recommend correcting only those with a document that contradicts the record and a rule that can be coded exactly. Do not propose bounding runs for the rest by default.
