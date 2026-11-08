---
name: feedback-etfp-jde-after-fl05
description: ETFP ladder - run jde only after every fl05 trim path is finished, and only for cells where sigma passed
metadata:
  type: feedback
---

On the ETFP cleaning ladder, jde estimates come after fl05: wait until all fl05 results are in (not just the first trim), then run jde only for the cells whose sigma passed, under the same sample and trim rules.

**Why:** user, 2026-11-06: "in general jde has larger sigma than fl05", and "not after the u10 done. after all fl05 done."

**How to apply:** do not queue jde units when one fl05 trim finishes. Related: [[feedback_etfp_trim_order]], [[feedback_etfp_runs_to_hmac]].
