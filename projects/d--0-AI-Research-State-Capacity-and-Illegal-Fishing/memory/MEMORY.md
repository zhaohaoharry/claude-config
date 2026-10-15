# Memory Index

- [Paper framing decision](project_framing.md) — International order framing chosen for top-5 push; IUU fishing as test of rules-based order
- [User research context](user_context.md) — Economist, not state capacity specialist, prefers autonomous Claude work
- [Code stays in sandbox](feedback_code_sandbox.md) — All experimental code under sandbox/; never promote to production without explicit approval
- [Use existing LaTeX styles](feedback_tex_style.md) — Always use paper.sty and bibliography.bst; add packages to sty, never replace
- [Real data only](feedback_real_data_only.md) — All empirical output from runnable code on real data; no fake numbers (applies to ALL projects)
- [Disentangling findings](disentangle_findings.md) — Under-reporting not point-identifiable; SAU share circular, RAM biomass no coverage of conflict states; contribution hinges on SAR dark-vessel pull
- [Model spec status](model_spec_status.md) — Canonical model = June-12 nested-Frechet sqe_model_spec.tex; June-13 dark-mode draft regressed; merge plan + A1 staggered-onset falsification + inland-not-coastal concern
- [Data pulls complete](data_pulls_complete.md) — All 5 GFW/SAR/NOAA API pulls done (effort, gaps, SAR flag+class, chlorophyll) in data/clean/; SAR null-tile gotcha fixed; resume-safe
- [Final empirical picture](onset_did_robust.md) — first-collapse state failure raises foreign fishing PRESSURE (effort +0.206** at 1982, first-ever-onset only) but the DARK/ILLEGAL margin is robustly NULL across Watson/SAU + GFW going-dark + SAR dark-fishing; lead paper with "pressure not illegality"
- [war variable corrupted](war_variable_corrupted.md) — panel `war` col = conflict-PARTICIPATION (USA/UK/FRA in Vietnam/Gulf/ISIS; Rwanda missing), NOT PITF state failure; use data/clean/pitf_sf_onset_hostyear.csv (genuine, from pitf_all_iso.dta); every "PITF war" result used the wrong treatment
