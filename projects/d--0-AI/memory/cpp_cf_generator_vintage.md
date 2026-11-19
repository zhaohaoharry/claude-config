---
name: cpp-cf-generator-vintage
description: Carbon Pricing Policy counterfactual table generators need three env vars or they silently rebuild Section 7 from an old run
metadata:
  node_type: memory
  type: project
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-18T01:53:39.944Z
---

In Carbon Pricing Policy, `make_cf_v2.py`, `make_temp_cf2017.py` and `make_cf_v2_extra.py` pick their input files from
the environment. Run bare, they read the 2026-11-03 run and overwrite every Section 7 table and `v2_cf_numbers.tex`
with wrong numbers, with exit code 0. The manuscript vintage as of 2026-11-18 (2017 coverage adopted; the EU price
falls only on the EU ETS list) is:

`CPP_ACCESS_TAG=pc CPP_POT_SPEC=pc CPP_COST_SPEC=base CPP_KAPPA=0.0147 CPP_MAIN=m7 CPP_COVSHOCK=1 CPP_CF_COV=2017`
for `make_cf_v2.py`, `make_cf_v2_extra.py`, `make_theta_cp_numbers.py` and `jde_cf_income.py`. Without
`CPP_CF_COV=2017` they read the adoption-year-coverage runs, which put the EU price on members' national-tax products.

(Superseded 2026-11-12 vintage: `CPP_MAIN=m7 CPP_KAPPA=0.0132 CPP_ACCESS_TAG=hist`.)

`make_estimation_v2.py` needs one more, `CPP_NOCTL=1` (it selects `reduced_form_targets_cov.json`); without it the
script re-selects sigma 1.5 in place of the adopted 2.0 and overwrites `selected_m7_kappa0.0132_hist.json`:

`CPP_MAIN=m7 CPP_NOCTL=1 CPP_KAPPA=0.0132 CPP_ACCESS_TAG=hist python program/python/make_estimation_v2.py`

**Why:** on 2026-11-12 a bare run changed leakage from 62 to 64 percent and every other counterfactual number; it was
caught only because `v2_cf_numbers.tex` had been backed up and diffed.

**How to apply:** before running any of the three, back up `latex/tables/v2_cf_numbers.tex`, run with the env vars,
and diff. If the selected kappa or access tag changes (see `EvKappa` in `v2_est_numbers.tex` and
`data/clean/estimates/selected_m7_*.json`), update this note. Same caution for other generators with an `SFX` built
from `CPP_*` variables.
