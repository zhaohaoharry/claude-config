---
name: feedback_downstream_consistent_with_estimator
description: "Before running inherited downstream code (coauthor exhibits, counterfactuals), audit every step that re-estimates anything and make it match the current estimation procedure (FE, estimator, instruments, sample)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-10-14T09:47:27.993Z
---

Downstream analysis must use the same specification as the estimation it builds on. Inherited or coauthor code often re-estimates pieces of the model itself (VAR, first stage, demand) with the old specification, and the results then silently mix two estimators.

**Why:** ETFP, 2026-10-14. The downstream build (80_build_spec_format.do) and Table 1 (27_table1) re-estimated the technology VAR by 2SLS with industry x year effects and the old instruments (current capital, lagged S*), while our GMM concentrated out the VAR by least squares with year + 4-digit industry effects. The counterfactuals read that VAR, so the fee counterfactual flipped sign (induced share -8% vs +8.5% once consistent). The user: the program must be internally consistent; never make this mistake again.

**How to apply:**
- Before the first downstream run of a new specification, grep every downstream script for estimation commands (ivreghdfe, reghdfe, regress, gmm, nl, estimates save/use) and list what each re-estimates and what it reads.
- Any re-estimated model object (VAR, first stage, demand, smoothing of tau) must use the current FE, estimator, instruments and sample; otherwise pass the GMM estimates directly. Descriptive regressions (trends, validation, t-tests) are fine.
- Verify by comparing the downstream coefficients with the estimation-step values (e.g. GMM A_struct, gam_tau) before reporting any downstream number.
- Related: [[feedback_etfp_first_stage_no_sigma]], [[feedback_no_footprints_of_abandoned_designs]].
