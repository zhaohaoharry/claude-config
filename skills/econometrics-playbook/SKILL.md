---
name: econometrics-playbook
description: Use when choosing a causal-inference design or writing the estimation code for it — difference-in-differences (including staggered: Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-D'Haultfoeuille), event studies, RDD (sharp/fuzzy), IV/2SLS with weak-IV-robust inference, synthetic control / SDID, panel fixed effects, DML / causal forests, or quantile / distributional methods. This is the method how-to lane: it names the modern estimator, the identifying assumptions, the must-run diagnostics, the common pitfalls, and the recommended Stata, R, and Python commands for each design.
argument-hint: "[design, e.g. 'staggered DiD' or 'fuzzy RDD']"
allowed-tools: ["Read", "Grep", "Glob", "Write"]
---

# Econometrics Playbook

## Overview

A single lookup for *how to estimate* a causal design once it has been chosen. For each common design it gives five things: the **modern recommended estimator**, the **key identifying assumptions**, the **must-run diagnostics**, the **common pitfalls**, and the **Stata / R / Python packages and commands**.

This is the **method how-to lane**. It is advisory — it helps pick a design and write the code; it does not run anything. Route to it from `aer-identification` (which decides *whether* the design is defensible for an AER-track paper) and pair its output with `aer-robustness` (the referee-anticipating check battery). For a critique of an already-estimated specification, hand off to the `econ-reviewer` agent.

## When to Use

- Picking the modern estimator for a design that is already chosen (which DiD? which RDD inference?)
- Writing the Stata / R / Python code for an IV, DiD, event study, RDD, SCM, panel FE, DML, or quantile analysis
- Checking that the must-run diagnostics for a method are all present
- Diagnosing why a referee flagged the estimator (e.g., TWFE on staggered data, first-stage F as the only IV evidence)

Skip when:
- The question is *whether* the identification strategy clears the AER bar → `aer-identification`
- The main results exist and need robustness / heterogeneity / placebo coverage → `aer-robustness`
- A finished specification needs a substantive critique → `econ-reviewer` agent
- The task is a formal identification proof → not this skill (use an identification-proof reference)

## Quick Reference

| Design | Modern estimator | Target | Stata | R | Python |
|--------|-----------------|--------|-------|---|--------|
| Panel FE | High-dim FE OLS | within effect | `reghdfe` | `fixest::feols` | `pyfixest.feols` / `linearmodels.PanelOLS` |
| 2×2 DiD | TWFE (if homogeneous) | ATT | `reghdfe` | `fixest::feols` | `pyfixest.feols` |
| Staggered DiD | C-SA / S-A / dCDH / BJS | ATT(g,t) | `csdid`, `did_multiplegt_dyn` | `did`, `fixest::sunab`, `didimputation` | `differences`, `pyfixest` (sunab) |
| Event study | C-SA / S-A / imputation | ATT(e) | `csdid`, `eventstudyinteract` | `fixest::sunab`, `did` | `pyfixest`, `differences` |
| RDD (sharp/fuzzy) | Local linear, MSE-bw, robust BC CI | LATE at cutoff | `rdrobust` | `rdrobust` | `rdrobust` |
| IV / 2SLS | 2SLS + weak-IV-robust inference | LATE | `ivreghdfe`, `weakivtest` | `fixest::feols`, `ivDiag` | `linearmodels.IV2SLS` |
| Synthetic control / SDID | augsynth / gsynth / SDID | ATT (treated) | `synth`, `sdid` | `augsynth`, `gsynth`, `synthdid` | `pysyncon`, `SparseSC` |
| DML / causal forest | DML, causal forest | ATE / CATE | — | `DoubleML`, `grf` | `doubleml`, `econml` |
| Quantile / distributional | RIF / IV-QR / changes-in-changes | QTE | `rifhdreg`, `ivqreg2`, `cic` | `qte`, `Counterfactual` | `statsmodels` QuantReg |

## Panel Fixed Effects

- **Estimator:** high-dimensional FE OLS. Default to `reghdfe` / `fixest::feols` / `pyfixest`, not `xtreg` or hand-built dummies.
- **Assumptions:** strict exogeneity conditional on the FE; no within-group feedback from outcome to regressor; correct FE structure.
- **Diagnostics:** report which FE absorb which variation; check the within-R²; confirm the regressor of interest is not collinear with the FE (singletons dropped).
- **Pitfalls:** Nickell bias if a lagged dependent variable is included with short T; absorbing the treatment variation itself; clustering finer than the level of treatment assignment.
- **Code:** Stata `reghdfe y x, absorb(id year) vce(cluster id)`; R `feols(y ~ x | id + year, cluster = ~id, data=df)`; Python `pyfixest.feols("y ~ x | id + year", df, vcov={"CRV1":"id"})`.

## Difference-in-Differences

### 2×2 (single date, two groups)

- **Estimator:** TWFE is fine **only if** timing is simultaneous, the control group is never treated, and effect heterogeneity is implausible. Otherwise move to a staggered estimator.
- **Code:** Stata `reghdfe y treat_post, absorb(id period) vce(cluster id)`; R `feols(y ~ treat_post | id + period, cluster=~id)`.

### Staggered adoption (most modern applications)

**Do not use TWFE.** Pick by setting:

```
Can treatment turn off (reversals / continuous dose)?
├── Yes → de Chaisemartin-D'Haultfoeuille (2020/2024)
└── No
    ├── Never-treated controls exist → Callaway-Sant'Anna with never-treated
    ├── Only not-yet-treated → Callaway-Sant'Anna (not-yet-treated) or Sun-Abraham
    └── Want imputation / efficiency → Borusyak-Jaravel-Spiess (2024)
```

- **Callaway-Sant'Anna (2021):** group-time ATT(g,t), doubly robust, flexible aggregation. Stata `csdid`; R `did::att_gt`; Python `differences`.
- **Sun-Abraham (2021):** interaction-weighted, integrates into the FE regression for event studies. Stata `eventstudyinteract`; R `fixest::sunab`; Python `pyfixest` `sunab()`.
- **de Chaisemartin-D'Haultfoeuille (2020):** handles reversals and continuous treatment. Stata `did_multiplegt_dyn`; R `DIDmultiplegtDYN`.
- **Borusyak-Jaravel-Spiess (2024):** imputation estimator. Stata `did_imputation`; R `didimputation`.

- **Assumptions:** parallel trends conditional on group and time; no anticipation; (for C-SA) correct outcome and/or propensity model.
- **Diagnostics:** Goodman-Bacon decomposition to show the weight on forbidden comparisons under TWFE (`bacondecomp`/`ddtiming`); event-study plot from the modern estimator; joint pre-trends test (not just the visual); cohort heterogeneity.
- **Pitfalls:** already-treated units used as controls (negative weights, possible sign flip); a single post indicator masking cohort heterogeneity; concluding parallel trends hold from insignificant pre-coefficients (low power — use Rambachan-Roth Honest DiD via `honestdid` / `HonestDiD`).

## Event Study

- **Estimator:** the staggered-DiD estimator's event-time aggregation (C-SA dynamic, Sun-Abraham, or imputation). Never raw TWFE leads/lags with staggered timing.
- **Assumptions:** as in staggered DiD, plus a clearly chosen and stated reference period (omit `-1`; never bin the endpoints silently).
- **Diagnostics:** flat, insignificant pre-period coefficients with 95% CIs; joint pre-trend test; Honest DiD sensitivity bounds on the post-period; uniform vs pointwise bands stated.
- **Pitfalls:** the "fully dynamic TWFE is contaminated" trap; under-binning the endpoints (multicollinearity with the FE); reading absence of a significant pre-trend as proof of parallel trends.
- **Code:** R `feols(y ~ sunab(cohort, period) | id + period); iplot(...)`; Stata `csdid ..., long2; estat event`; Python `pyfixest.feols("y ~ sunab(cohort, period) | id + period")`.

## Regression Discontinuity (sharp / fuzzy)

- **Estimator:** local linear regression with a triangular kernel; MSE-optimal bandwidth (Calonico-Cattaneo-Titiunik 2014); robust bias-corrected CI. Fuzzy RDD = IV at the cutoff (`fuzzy(D)` in `rdrobust`).
- **Assumptions:** continuity of potential outcomes at the cutoff; no manipulation of the running variable; (fuzzy) a first-stage jump in treatment probability and monotonicity.
- **Diagnostics:** McCrary / Cattaneo-Jansson-Ma density test (`rddensity`); covariate balance / placebo outcomes at the cutoff; bandwidth sensitivity across ≥3 bandwidths; placebo cutoffs; `rdplot` with the binning method stated; donut RDD if bunching at the cutoff.
- **Pitfalls:** polynomial order > 1 (Gelman-Imbens 2019 — discouraged); reporting only one bandwidth; high-order global polynomials masking misspecification; discrete running variable with few mass points (use Cattaneo-Idrobo-Titiunik discrete-RD methods, cluster on the running variable).
- **Code:** identical command across languages — `rdrobust(y, x, c=0)` and `rddensity(x, c=0)` in Stata, R, and Python; fuzzy via `fuzzy=D` (Py) / `fuzzy(D)` (Stata) / `fuzzy=D` (R).

## Instrumental Variables / 2SLS

- **Estimator:** 2SLS with cluster-robust SEs; LIML or Fuller as robustness under weak instruments; GMM if heteroskedasticity and over-identified.
- **Assumptions:** relevance (instrument shifts the endogenous regressor); exclusion (instrument affects Y only through D — argued, not tested); independence; monotonicity for the LATE interpretation.
- **Diagnostics:** the first-stage F > 10 rule is **obsolete** — report the **Olea-Pflueger effective F** and, for just-identified models, **Anderson-Rubin confidence sets** as primary inference (correct size at any instrument strength); reduced form; over-identification test if over-identified; compare OLS vs 2SLS direction; name the compliers.
- **Pitfalls:** reporting 2SLS CIs alone when F < 50 (use AR); forbidden regression (manual first-stage plugged into OLS, or nonlinear first stage with linear second stage — use a control function); Stock-Yogo critical values assume homoskedasticity and rarely apply under clustering; defending exclusion only with "we control for X".
- **Code:** Stata `ivreghdfe y (D = Z), absorb(fe) cluster(id)` then `weakivtest`; R `feols(y ~ 1 | fe | D ~ Z, cluster=~id)` plus `ivDiag::ivDiag(...)`; Python `linearmodels.IV2SLS.from_formula("y ~ 1 + [D ~ Z]", df).fit(cov_type="clustered", clusters=df.id)`.

### Shift-share / Bartik

Pick one identification source explicitly: **exogenous shares** (Goldsmith-Pinkham-Sorkin-Swift 2020 — report Rotemberg weights, inspect the top-5 industries) **or exogenous shocks** (Borusyak-Hull-Jaravel 2022; Adão-Kolesár-Morales 2019 — shock-level inference). Do not hand-wave between the two.

## Synthetic Control / SDID

- **Estimator:** for one (or few) treated units with a long pre-period and a large donor pool. Default to **augmented SC** (Ben-Michael-Feller-Rothstein 2021) for bias correction, **generalized SC / gsynth** (Xu 2017) for multiple treated units, or **synthetic DiD** (Arkhangelsky et al. 2021) to combine SCM and DiD weighting.
- **Assumptions:** pre-treatment fit implies the post-treatment counterfactual; donors are unaffected by the treatment (no spillovers); intervention is large and aggregate.
- **Diagnostics:** pre-treatment RMSPE (fit quality); in-space placebo across every donor with a permutation / Fisher exact p-value; in-time placebo at a fake earlier date; leave-one-out donor stability; report the weight vector and discuss donors with > 10% weight.
- **Pitfalls:** over-fitting the pre-period with too many predictors; a donor pool contaminated by the same shock; no placebo inference; interpolation bias when the treated unit is outside the donor convex hull.
- **Code:** Stata `synth`, `synth_runner`, `sdid`; R `augsynth`, `gsynth`, `synthdid`, `tidysynth`; Python `pysyncon`, `SparseSC`.

## Double / Debiased ML and Causal Forests

- **Estimator:** DML (Chernozhukov et al. 2018) for low-dimensional causal parameters with high-dimensional / nonlinear nuisance; causal forests (Wager-Athey 2018, `grf`) for heterogeneous effects (CATE).
- **Assumptions:** unconfoundedness / selection on observables (same as matching — ML does not fix endogeneity); overlap; Neyman-orthogonal moment + cross-fitting to remove regularization bias.
- **Diagnostics:** cross-fitting used (sample-split, not in-sample nuisance); overlap / propensity trimming; nuisance-model fit checked; for forests, calibration test (`test_calibration`) and best-linear-projection of the CATE; tune learners out of the causal parameter.
- **Pitfalls:** treating DML as an identification strategy when it is only an estimation strategy under unconfoundedness; no cross-fitting (bias from over-fit nuisance); extreme propensities; reading forest splits as causal mechanisms.
- **Code:** R `DoubleML::DoubleMLPLR`, `grf::causal_forest`; Python `doubleml.DoubleMLPLR`, `econml.dml.LinearDML`, `econml.grf.CausalForest`. (No mature Stata equivalent — use R or Python.)

## Quantile / Distributional

- **Estimator:** for distributional effects, not just the mean. Unconditional quantile / RIF regression (Firpo-Fortin-Lemieux 2009) for population QTEs; IV quantile regression (Chernozhukov-Hansen 2005) under endogeneity; changes-in-changes (Athey-Imbens 2006) for distributional DiD.
- **Assumptions:** conditional QR identifies *conditional* quantiles (not population QTEs — use RIF for the latter); IV-QR needs rank-similarity / rank-invariance; CiC needs a monotonicity / common-distribution assumption rather than parallel trends.
- **Diagnostics:** report QTEs across the distribution with bootstrap CIs; check no quantile crossing; compare the mean effect to the distributional pattern; test rank invariance plausibility for IV-QR.
- **Pitfalls:** interpreting conditional QR coefficients as effects on the unconditional distribution; analytic SEs (bootstrap instead); over-reading tail estimates where data are thin.
- **Code:** Stata `qreg`/`rifhdreg`, `ivqreg2`, `cic`; R `quantreg::rq`, `qte`, `Counterfactual`; Python `statsmodels.QuantReg` (RIF and IV-QR largely hand-built or via R).

## Inference Discipline (all designs)

- Cluster at the level of treatment assignment, at minimum.
- Few clusters (< 30–40): wild cluster bootstrap (Cameron-Gelbach-Miller 2008 — `boottest` / `fwildclusterboot`). Very few (< 10): randomization inference or aggregate to the cluster level.
- Report 95% CIs alongside p-values; many AER editors prefer effect-size reporting over stars.
- A "bad control" is an outcome of treatment — never condition on a post-treatment variable, mediator, or collider.

## Output Format

When invoked for a design, return this block, then the code:

```text
DESIGN: <panel FE | DiD 2x2 | staggered DiD | event study | RDD sharp/fuzzy | IV/2SLS | shift-share | SCM/SDID | DML/causal forest | quantile>
RECOMMENDED ESTIMATOR: <name + citation>
TARGET PARAMETER: <ATT | ATT(g,t) | LATE | CATE | QTE | within effect>
IDENTIFYING ASSUMPTIONS: <list>
MUST-RUN DIAGNOSTICS: <list>
INFERENCE: <cluster-robust | AR set | wild bootstrap | permutation>
LANGUAGE + PACKAGES: <Stata: ... | R: ... | Python: ...>
PITFALLS AVOIDED: <list or "none flagged">
HANDOFF: aer-identification (defensibility) | aer-robustness (check battery) | econ-reviewer (critique)
```

## Important

1. Name the estimator with its citation and the package command in all three languages the user runs — do not leave the choice implicit.
2. Always state the target parameter explicitly (LATE ≠ ATE; ATT from DiD ≠ ATE; conditional QR ≠ population QTE).
3. The first-stage F > 10 rule and the TWFE-on-staggered-data default are obsolete — flag them as red flags, never recommend them.
4. ML methods (DML, causal forests) are estimation strategies under unconfoundedness, not identification strategies — say so.
5. List the must-run diagnostics for the chosen design; an estimator without its diagnostics is incomplete.
6. This skill writes code and recommends designs — it does not execute, and it does not decide whether the design clears the journal bar. Defer defensibility to `aer-identification`, the referee-anticipating battery to `aer-robustness`, and substantive critique to the `econ-reviewer` agent.
