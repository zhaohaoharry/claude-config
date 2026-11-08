---
name: feedback-etfp-symmetric-share-rule
description: "ETFP labor-share cleaning rules must be symmetric; asymmetric bounds (tl02l [.02,.95], tl01l [.01,.95]) are dropped, even as bootstrap targets"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-11-08T05:43:22.211Z
---

ETFP labor-share cleaning must use a symmetric rule: fixed bounds [a, 1-a] (e.g. [.05,.95], [.01,.99], [.005,.995]) or the bottom/top p% within 2-digit industry x year, like the other ratio cuts. User, 2026-11-08: "I dont like 0.02 0.95.. i want symmetry"; tl02l was "just a check, we dont need that any more because it is not symmetric".

**Why:** an asymmetric bound is hard to justify as a cleaning rule, even when it passes the screen with more data.

**How to apply:** never propose or bootstrap an asymmetric share-bound sample (tl02l, tl01l); the candidates are ts01l, ts005l and tp005l (330_build_sample.py --lo/--hi or --lspct) beside the tw95l baseline. Related: [[feedback_etfp_retest_scope]], [[feedback_etfp_corrected_pool]].
