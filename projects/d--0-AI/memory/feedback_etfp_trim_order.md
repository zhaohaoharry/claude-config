---
name: feedback_etfp_trim_order
description: "ETFP specification search runs the lightest second-stage trim first, moves to heavier trims only if it fails, and sends the lightest passing trim straight to the full downstream"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-10-30T03:44:16.987Z
---

In ETFP specification searches, run the lightest second-stage trim of ln S* first (none, U05, U10, U15, U20, U25, ...) and move to a heavier trim only when the lighter one fails the check (sigma, theta, eta plausible; gamma_ZZ > 0.8 gamma_Ztau). Once a trim passes, run the full downstream (run_tag_full.sh) on it directly. Do not run the heavier trims as well.

**Why:** the goal is to keep the largest sample (user, 2026-10-30). Heavier trims that also pass add nothing once a lighter one works, and running every trim wastes HMac/H2 time.

**How to apply:** when a new sample or rule is tested, queue the trims in ascending order, or check each result before queueing the next heavier trim. Report the lightest passing trim and go to its downstream. Related: [[feedback_etfp_runs_to_hmac]], [[feedback_no_rerun_existing_results]].
