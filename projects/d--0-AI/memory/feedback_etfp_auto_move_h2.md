---
name: feedback_etfp_auto_move_h2
description: Standing yes - move queued compute units to H2 whenever H2 is online and free and it speeds the run; never ask
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-11-05T11:23:58.369Z
---

When H2 is online and free and moving queued units there would speed up a run, move them without asking. The answer is always yes.

**Why:** Said directly on 2026-11-05 after I asked whether to move HMac's queued etfp_k1104g units to idle H2.

**How to apply:** Rebalance on my own initiative and report it afterwards. Keep H2 to at most 2 concurrent units for ETFP GMM jobs: 3 took free RAM down to 0.4 GB. Do not kill units already running elsewhere. This covers units of a run already authorized, not new runs. Related: [[feedback_etfp_runs_to_hmac]].
