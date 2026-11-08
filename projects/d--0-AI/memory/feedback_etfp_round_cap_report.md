---
name: feedback_etfp_round_cap_report
description: ETFP GMM - when a run hits the 30-round cap, report the adjustments of the final 5 rounds before calling it unconverged or converged
metadata:
  type: feedback
---
When an ETFP GMM run hits the 30-round cap, report the per-round adjustments of the final 5 rounds (user, 2026-11-07), to see if the estimates are really flat. Path is saved in row["path"]; 337_round_path.py prints it.

**Why:** the stop rule (max change below 1e-6) is strict, so a capped run may already be flat; "not converged" alone misleads.

**How to apply:** never label a capped cell non-converged without the last-5-round table; set any looser threshold only after seeing paths, the same for every cell.
