---
name: model_spec_status
description: Canonical structural model is the June-12 nested-Frechet spec; the June-13 dark-mode draft regressed and has fixable errors; merge plan + key falsification test
metadata: 
  node_type: memory
  type: project
  originSessionId: 41f0bcf8-09c3-4e01-87a3-aa6bd66e9d7f
---

**Canonical structural model = `latex/answers/sqe_model_spec.tex` (June 12).** It already has: nested
Frechet (destination (i,s) x reporting-mode m in {R,U}, mode dispersion sigma DISTINCT from allocation
theta, sigma>theta); an outside option (home/high seas); surplus-production stock law in tonnes with
TOTAL removals (RAM + CMSY, K=4MSY/r); host welfare = resource rent + access/licence revenue + expected
fines − enforcement cost + terminal stock asset value Lambda(B); enforcement wedge tau as f(Hanson-Sigman
capacity S, conflict D). Identification discipline: "structure prices, data identify" — the one
conflict-exposed elasticity is GFW-anchored, NEVER the SAU R/U ratio (which SAU imputes from governance
indices -> set-identified, not point-identified).

**`latex/answers/dark_mode_sqe_model.tex` (June 13) REGRESSED — do not use as-is.** It collapsed the nest
to flat i.i.d. Frechet over (h,m) with a single theta and proposed the exact sigma-vs-kappa inversion the
June-12 spec forbids. An adversarial econ-referee panel (workflow wf_fb638d33-b34) flagged: theory+aggregation
NEEDS-WORK, identification BROKEN, all salvageable. Fixable math errors: (F1) the peak condition R t'=rho'Phi
is the turning point of the DIFFERENCE pi^D-pi^O, but the estimand is the SHARE (logit in the RATIO) — correct
peak t'/(1-t)=rho'Phi/pi^D; (F2) A1 (level ordering of charge t before interdiction rho) is insufficient —
need a single-crossing SLOPE condition for single-peakedness; (F3) "sigma~0 at low kappa" is FALSE under
Frechet (sigma(0)=(R-delta)^theta/(R^theta+(R-delta)^theta)~0.4), and the low-kappa arm slopes UP, so the
draft model predicts conflict LOWERS dark share — contradicting our going-dark null. (F4-F6) cannot recover
{theta,t,rho,delta,Phi} from one curve: Phi only enters as product rho*Phi, delta trades off with rho*Phi,
and A1 IS the inverted-U (circular).

**The June-13 IDEA is still valuable** (not a pure regression): replace the June-12 nest's CONTAMINATED SAU
reported/unreported mode with the CLEAN SAR-observable OPEN/DARK mode + the charge-capacity-vs-interdiction-
capacity split (admin capacity turns on early, physical/naval interdiction only at high capacity). PLAN =
MERGE: graft SAR open/dark mode + capacity split onto the June-12 nested machinery; re-derive the proposition
for the NESTED share with the slope-crossing condition; relocate the conflict-null to the nest/outside-option
(not a fictional flat). IDENTIFY t, rho*Phi, Phi off EXTERNAL moments (access-fee/licence revenue for t;
interdiction/confiscation/fine events for rho*Phi; statutory penalty schedules for Phi), treating A1 as a
TESTABLE restriction not an assumption.

**Key falsification to run FIRST (off-curve, breaks circularity):** staggered-onset ordering test of A1 —
regress host access-fee/licence revenue on the ADMINISTRATIVE capacity sub-index and interdiction/fine events
on the MILITARY/POLICE sub-index; A1 predicts charge turns on at LOW capacity, interdiction only above a
HIGHER threshold. Also place the 5 onset hosts (Somalia, Yemen, Guinea-Bissau, Libya, Myanmar) on the kappa
axis EX ANTE; if any sits mid-kappa the model REQUIRES a positive going-dark response there (testable in SAR).
NEW DATA NEEDED: host access-fee/licence revenue (e.g. EU SFPA agreements), interdiction/arrest events,
statutory penalty schedules.

**Deeper concern for the whole enforcement-wedge mechanism:** the robust +28% effort surge loads on INLAND
conflict (+0.479, p=.014) not COASTAL (+0.096, ns), with FLAT capacity heterogeneity — a "general state
distraction" signature, NOT an EEZ-specific coastal-enforcement-wedge signature. Confront this before
committing the model's Fact-1 mechanism. Empirical inverted-U is also FRAGILE (only 1 of 4 specs shows it:
SAR dark-share OLS cap2 p=.04; SAR Poisson, going-dark OLS+Poisson all monotone). Settle whether Fact 2 is
real (classified SAR dark-FISHING share + host FE + AIS-coverage control) before building the headline on it.
See [[disentangle_findings]].
