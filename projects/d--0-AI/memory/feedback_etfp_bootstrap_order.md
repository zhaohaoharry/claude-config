---
name: feedback_etfp_bootstrap_order
description: "ETFP bootstrap - resample firm-years everywhere; local first, report and save, then standard from the full-sample estimate only"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-11-06T00:49:00.925Z
---

For ETFP bootstraps: resample firm-years, not firms, in both the local and the standard bootstrap. Always run the local firm-year bootstrap first, report and save that quick result, then run the standard bootstrap to check that the result also makes sense there. The standard bootstrap starts from the full-sample estimate only, with no other starting values.

**Why:** Said on 2026-11-06. The user's reasons: estimation does not need firm id, and the local bootstrap is quick (about 2 minutes per draw) while the multi-start standard one took about 2.2 h per draw.

**How to apply:** In any bootstrap package, order local units before standard units, and summarize the local units as soon as they finish instead of waiting for the standard ones. Related: [[feedback_etfp_runs_to_hmac]].

A specification passes on the size of its bootstrap SD, not on a count of draws above sigma 3: jumps do not matter if the SD stays small (user, 2026-11-06).

User, 2026-11-07: settle the specification first; bootstrap only after all specification exploration is finished.
