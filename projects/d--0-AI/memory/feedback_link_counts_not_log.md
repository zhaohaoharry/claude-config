---
name: feedback-link-counts-not-log
description: "For product-link outcomes, regress the actual link count (linear or PPML), never log(1+link)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-09-12T09:57:37.750Z
---

For link (extensive-margin) outcomes in trade regressions, use the actual number of links as the dependent variable, estimated by OLS on the count or by PPML. Do not use log(1+link).

**Why:** At the finest product level the link is a 0/1 indicator, so log(1+link) is log 2 times the indicator and the coefficients are uninterpretable fractions; at aggregated levels (HS4 heading, EXIOBASE industry) the count of HS6 products traded within the group is the object of interest. Stated by the user on 2026-09-12 in the Carbon Pricing Policy project.

**How to apply:** In composition/DDD tables, the link column is "number of links" (count within pair-group-year), PPML or linear; keep log outcomes for values only. Product-level PPML with high-dimensional FE is too slow in ppmlhdfe, so run link-count PPML at the industry level or use R fixest. See [[feedback-regression-table-conventions]].
