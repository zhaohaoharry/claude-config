---
name: feedback-cpp-test-on-1000-first
description: "Carbon Pricing Policy — test any estimation change on the 1,000-product sample before running it on all products"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-13T05:13:47.938Z
---

Carbon Pricing Policy project: any change to the structural estimation (specification, design of the random
components, added controls, new moments) is first tested on the 1,000-product sample, and only the version that is
settled there is run on all 4,646 products. Stated by the user on 2026-11-13 ("always test with the 1000 product
sample before implement the all product run").

**Why:** an all-products run costs hours per stage (access costs about 25 minutes per sigma, the adoption stage about
45 minutes per grid point, plus standard errors and counterfactuals), against minutes on the sample. The final paper
reports all-products estimates only; the sample is a development tool and is not mentioned in the manuscript.

**How to apply:** `product_sample(1000)` in `program/python/estimate_access_costs.py` (seed 20260903) gives the sample;
the cells cache for it is in `%TEMP%\cpp_cells_cache`. Do tests in a sandbox folder, show the user the comparison,
then launch all products. See [[cpp-cf-generator-vintage]] for the environment the generators need.
