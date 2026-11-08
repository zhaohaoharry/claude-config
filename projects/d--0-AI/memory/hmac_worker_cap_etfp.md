---
name: hmac-worker-cap-etfp
description: "HMac (16 GB M3) thrashes at 6 workers on ETFP GMM units (~5 GB each); use 3 workers, 2 if swap grows"
metadata:
  node_type: memory
  type: project
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-11-08T01:18:01.864Z
---

Measured 2026-11-08 on HMac during job etfp_l1106: six ETFP GMM units (T05, F0, mode sc) at 6 workers left 69 MB free, 6.6 of 8.2 GB swap used, ~68 GB swapped back in; the six units took ~7 hours against ~1 hour each on H2 at 2 workers. Footprint is about 5 GB per unit.

**Why:** memory thrashing plus the fanless thermal limit, not raw CPU, made HMac slower than H2 on these units — the older belief that H2 is ~4x slower than HMac on real units does not hold for these large units.

**How to apply:** launch ETFP GMM units on HMac with 3 workers (2 if swap keeps growing); weight assignments by measured units/hour, not by core count. Related: [[feedback_etfp_runs_to_hmac]], [[feedback_etfp_auto_move_h2]], [[scalable_computing_2026_10]].
