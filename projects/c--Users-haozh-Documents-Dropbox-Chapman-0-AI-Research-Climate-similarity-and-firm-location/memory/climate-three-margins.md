---
name: climate-three-margins
description: "Climate enters supplier choice through 3 margins (own-suitability, distance, similarity); the current design identifies only similarity+distance and absorbs suitability — which is the channel a warming counterfactual needs"
metadata:
  type: project
  originSessionId: 50884341-1a39-409e-91a0-02b4e86a8c41
---

Climate can affect the supplier-location choice through THREE distinct margins, and conflating them led me to wrongly dismiss the warming counterfactual:

1. **Own-suitability** f(C_j): a candidate location's OWN climate as a place to operate — likely non-monotonic (an optimal climate; too hot/cold/wet/hazard-prone is bad). A LEVEL effect on a location's attractiveness.
2. **Geographic distance** d_ij.
3. **Climate similarity** |C_i − C_j|: bilateral operational compatibility between customer and supplier climates.

**What the current sorting design identifies:** the location×industry×year FE (delta_jkt) ABSORBS margin 1 (candidate own-climate), and the customer×year FE absorbs the customer's own climate. So we identify ONLY the bilateral terms — margins 2 and 3. The "prefer-similar" headline is margin 3 (modest, measure-sensitive). We have NOT estimated margin 1.

**Why this matters (the user's 2026-06-08 correction):** global warming is largely a COMMON LEVEL shift, so it CANCELS in margin 3 (the difference |C_i−C_j| is unchanged) — that is why the similarity-only warming counterfactual is a near-null (matrix moved −1.4% over 2003–2021, <0.1% of links re-sort). BUT DIFFERENTIAL warming reshapes margin 1: some places become newly suitable (Russia, Canada), others worse (tropics). That does NOT cancel and is the TRUE engine of a climate counterfactual. So a credible warming counterfactual must go through OWN-SUITABILITY, which the current design absorbs and must be separately identified.

**The hard part — RESOLVED 2026-06-08 by the `climate-margins-redesign` workflow (empirical gate):** f(C_j) is economically LARGE (PPML own-temp p5–p95 swing +0.21, rivals distance −0.20/log-km — so the counterfactual is NOT a near-null), BUT the FactSet cross-section CANNOT identify its SHAPE. Raw (k#year FE) the curve is wrong-signed (hotter=better — a development/survivorship confound); confound-controlled (country#k#year FE) the signal vanishes to statistical zero. **The confound WAS the signal**, and there is no within-data rescue (in-sample warming is small + near-uniform across latitudes). **The only credible route is an EXTERNAL exogenous suitability measure: FAO-GAEZ agronomic potential yield (Costinot-Donaldson-Smith 2016) at each centroid for climate-sensitive sectors.** With GAEZ, f(C_j) was to be a triangulated BOUND for a partial-equilibrium link-migration counterfactual under CMIP6/SSP.

**OUTCOME (2026-06-08 empirical gate, `suit_respec.do`, 30% sample): THE GAEZ RESCUE FAILED → the warming counterfactual is DEAD.** GAEZ DOES survive country#k#year FE (gsi −0.019, p=0.034) BUT with the WRONG SIGN (negative: higher agronomic suitability → FEWER suppliers), and the services-flat placebo FAILS (effect not concentrated in climate-sensitive sectors; interaction p=0.385; subsamples null). Reason: GAEZ measures AGRICULTURAL suitability = farmland, which the sample's mostly-manufacturing suppliers (NAICS 31–33 = 70%) are negatively selected against — a land-use confound, not a climate-operability amenity. The conceptually-right industrial-climate suitability has no exogenous analogue to GAEZ → only cross-sectionally identified → confounded (the original problem). **Own-suitability f(C_j) is NOT credibly identifiable here. The paper ships on margins (2) distance + (3) similarity** (prefer-similar formation + the diversification null), a clean JIE/MS field paper. The pre-committed gates worked as designed. Full numbers: `quality_reports/2026-06-08_suitability_margin_verdict.md` (EMPIRICAL GATE OUTCOME section).

Related: [[climate-similarity-supplier-choice-project]].
