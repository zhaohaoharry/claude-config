---
name: decision_id_v2_vs_fine_impact
description: "Quantified impact of re-estimating the Water-and-Crop structural model on decision_id_v2 (appendix-consistent) vs decision_id_fine (current code) — beta_W halves, deterministic welfare headline reverses, IV stable, core thesis survives"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

**STATUS — SETTLED, DO NOT REVISIT: `decision_id_v2` is DROPPED and archived. Production stays on `decision_id_fine`. Fallow = drop zero-acre/no-permit pixel-years, NO inheritance. Never propose promoting v2, adding v2 to production, or re-asking how to handle fallow.** See [[fallow_handling_settled]].

2026-06-18. Resolved the decision-unit inconsistency by RE-ESTIMATING the full structural
chain on `decision_id_v2` (the construction the manuscript appendix `app:plot_reconstruction`
describes: entry/exit trim, plot-id forward-fill, per-dot inherited acreage) and diffing
against the canonical `decision_id_fine` (untrimmed; fallow/unmatched dots dropped at
`acres>0`). The paper's HEADLINE estimation runs on `fine`; the appendix describes `v2` — see
the prior finding that the two diverged.

**Isolated experiment**, suffix `_didv2`, canonical untouched. Chain: `B1d_step2_ccp_didv2`
→ step3 → step4 → `B4_counterfactuals_didv2`/`B4_two_task_counterfactuals_didv2`
(`B4_OUT_SUFFIX=_didv2`) → `T1p3_..._didv2`. All in `program/sandbox/decision_v2_variant/`
(+ the two B4 engine copies in `program/sandbox/`). Downstream code byte-identical (filename
substitution); step2 imports the canonical numerical core. Both use REV_TIMING=planting_zero
(canonical Jun-11 convention) and the same 22 districts — only the decision unit differs.
Full record: `program/sandbox/decision_v2_variant/RESULT_didv2_vs_fine.md`.

**First stage:** decisions 230,339→250,390; **Fallow 8.7%→15.3%** (v2 retains fallow-exit
decisions with inherited ~22ac, reproducing the appendix's ~15% construction); **β_W
0.001182 (t20.4) → 0.000641 (t11.8), ~46% lower**; β_R ≈0 both. Baseline cumulative GW
30.87→19.69 MAF (more fallow → less pumping).

**Welfare (ΔW @ σ=$1,000, M$ vs bilateral×open):** DET autarky-open **+475 → −455 (SIGN
FLIP)**, centralized-tax global max +3,529 → +1,623. IV autarky-open +1,843 → +1,118,
centralized-tax +5,886 → +3,636. **Crossovers:** autarky-vs-bilateral det 888→**1172**, IV
564→578; autarky-vs-centralized det 921→**1182**, IV 603→598; centralized-vs-bilateral det
1279→1236.

**Three conclusions.** (1) Core thesis SURVIVES qualitatively: centralized×tax still global
optimum, regulation restores ranking, centralization×regulation still complements — but all
magnitudes ~halve. (2) The DETERMINISTIC headline REVERSES at the benchmark: the paper's
"$888 crossover just below $1,000 → autarky raises welfare $0.48B" becomes a $1,172 crossover
ABOVE $1,000 → autarky REDUCES welfare $0.46B at σ=$1,000. (3) The IV ledger is ROBUST
(564→578, 603→598), inverting the paper's "deterministic conservative, IV only strengthens"
framing — under v2 the deterministic result is fragile and IV carries it.

**RESOLVED 2026-06-19: KEEP `decision_id_fine` in production; rewrite the appendix to match it.**
The user's reasoning (and it is correct): a permanent exit from the permit records is not idle
cropland (the parcel may move to housing or higher-value use), and a multi-year gap is not
continuous fallow (land may leave and re-enter ag, and we lack info for the gap). So `v2`'s
trim/inject/forward-fill/inherited-acreage OVERSTATES fallow; `fine` is the conservative,
defensible choice. My earlier "Option A (switch to v2) is principled" framing was WRONG — keeping
`fine` is the principled call. Implemented: appendix `\label{app:plot_reconstruction}` rewritten
(tracked) to describe `fine` (balanced grid, no-overlay=fallow, exclude no-permit/zero-acre
pixel-years, no inheritance), verified vs code, compiles 81pp. Recorded in project root
`DECISIONS.md`. v2 experiment archived + contained in `program/sandbox/decision_v2_variant/`
(`RESULT_didv2_vs_fine.md` + `outputs/`); never touches main results.
Validation: compare script reproduces every canonical number exactly; T1p3_didv2 independently
reproduces didv2 crossover (det 1172 / IV 578). See [[settled_cf_rules]], [[counterfactual_results]],
[[key_results]], [[feedback_verify_by_reexecution_not_rederivation]], [[feedback_workspace_program_sandbox_discipline]].
