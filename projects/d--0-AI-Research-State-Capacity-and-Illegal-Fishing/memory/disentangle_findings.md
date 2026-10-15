---
name: disentangle_findings
description: Under-reporting cannot be point-identified; both cheap defenses came back limiting; contribution hinges on pulling SAR dark-vessel data
metadata: 
  node_type: memory
  type: project
  originSessionId: 41f0bcf8-09c3-4e01-87a3-aa6bd66e9d7f
---

The "conflict → illegal/undocumented foreign fishing rises" causal claim cannot be cleanly
point-identified with current data. An adversarial econ-referee panel (2026-06-13, 5 strategies)
was unanimous: state capacity is a COMMON CAUSE of both weak enforcement and bad biology
(thin/overfished stocks, low-catchability flag-of-convenience fleets), so productivity leaks back
into any capacity/exposure contrast in the inflating direction. The honest ceiling is a signed
LOWER BOUND on conflict-driven under-reporting + a depletion falsification — NOT clean separation
or a level.

Two cheap "defend the measure" tests both came back LIMITING:
1. **SAU circularity gate = AMBER (corrected, was overstated as RED).** The raw unreported/reported
   ratio at host×fisher×year is NOT a fixed multiple — median within-pair CV = 1.27, only 1.8% of
   pairs near-constant — so SAU unreported is NOT pure imputation and carries real time variation.
   BUT it applies flat sector/EEZ expansion factors in pockets (GEO+KNA+VCT all exactly 0.35 in MRT;
   PRT 0.05 for 20 yrs in CAN, CV=0), correlates with host_capacity (−0.17), and is 66% between-host
   variance (mostly cross-sectional). NB: the earlier "138/143 fleets single value" was
   `peace_unreported_share`, a PROJECT-CONSTRUCTED peacetime moderator (one value per fleet BY
   CONSTRUCTION) — NOT raw evidence of SAU imputation; that framing was too strong. Net: contaminated
   enough to be UNSAFE as the headline causal dark outcome for a capacity/conflict treatment, but not
   a pure mechanical artifact. Decisive open check: does SAU bump unreported AT onset years for our
   hosts (needs country-reconstruction-doc audit).
2. **RAM biomass falsification = INCONCLUSIVE where it matters.** RAM Legacy (survey/age-structured
   stocks only, dropping catch-MSY/surplus-production) covers only 3 of 21 PITF-onset hosts
   (MEX, RUS, VEN — none of the weak conflict states Somalia/Yemen/Guinea-Bissau/Libya/Myanmar).
   On those 3 non-representative countries biomass does not fall (att +0.33, n=3, marginal
   pre-trend) → depletion cannot be directly falsified for the relevant population.

SAR ACCESS CONFIRMED (2026-06-13): GFW dataset `public-global-sar-presence:v4.0` is reachable with
our token via POST /v3/4wings/report, body key `geojson`, group-by FLAG or VESSEL_ID, 2017–2021.
Unmatched detections (empty flag/vesselId/mmsi) = dark vessels invisible to AIS = the keystone
extraction signal. One open design issue: isolating fishing vs non-fishing among UNMATCHED detections
(Paolo's NN labels may need a separate dataset/filter).

NET: the robust core is GFW observed effort +28% (clean event study). The under-reporting/illegal
contribution now hinges on pulling **SAR radar dark-vessel detections (Paolo et al. 2024, 2017–2021)**
— an extraction signal orthogonal to BOTH the SAU reconstruction lineage AND AIS-visible effort —
plus the economic-plausibility argument (weak-state grounds are under-exploited, so marginal product
of the +28% effort is not ≈0). Reduced-form workhorse = S1 within-ground triple-diff but with a SAR
placebo, not the SAU reported share. Structural model (S5) quantifies the bound, not a point level;
drop the pre-2012 back-cast. See [[project_framing]]. Full reasoning in
quality_reports/session_logs/2026-06-13_disentangle-underreporting.md and
latex/answers/disentangle_underreporting.pdf.
