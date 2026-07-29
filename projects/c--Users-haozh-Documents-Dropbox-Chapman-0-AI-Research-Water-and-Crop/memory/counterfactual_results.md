---
name: counterfactual-results
description: "CANONICAL headline CF results (2026-07-28, option-B adoption) — leakage 1.85 MAF/43%, cen_open +1.04 & −0.12B@1k, crossovers 870/876/887, cen_tax +2.96B ≈ quarter of 11.8B FS, taxes 65/215/232"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-07-28T14:30:14.749Z
---

Canonical 3×3 grid (run_counterfactuals.py on the option-B engine, adopted
2026-07-28; supersedes the 3.25-MAF era, whose buyer decision price was a bug —
and the far older sandbox-B4 numbers this memory once held).
Baseline GW 22.69 MAF; SGMA target −19% → 18.38.

- Autarky vs bilateral (open): ΔGW = −1.85 MAF = 43% of over-extraction;
  ΔFS −1.61B; ΔW@$1k +0.24B.
- Centralized (open): ΔGW +1.04 MAF, ΔFS +0.93B, ΔW@$1k −0.12B
  (welfare-NEGATIVE at the benchmark).
- Crossovers cluster 870 / 876 / 887 $/AF (aut-bil / aut-cen / cen-bil), all
  below the $1,000 benchmark → above ~$890 autarky dominates both markets.
- Global max: centralized × tax, +$2.96B over bilateral ≈ a quarter of the
  $11.8B baseline FS. Taxes 65 (aut) / 215 (bil) / 232 (cen) $/AF — roughly
  double a marginal-cost benchmark because the blend dilutes the Pigouvian
  signal (rate-design finding, in results prose). Caps 8.6 / 18.1 / 16.0%.
- UNIFORM POOL CLOSURE adopted 2026-07-28 (evening): cen_cap now clears at one
  county-wide scarcity price; CfCenCapBn 2.79→2.76, cen cap 14.4→16.0%, IV
  crossovers CfIvXoverAutBil/AutCen 420→542/522. All other cells byte-identical
  (validated _unifp3). Pro-rata canonical archived archive_prorata_20260728.
- Rate-design CF (CF_PRICING_RULE=marginal, _pricefix files): bilateral trade
  collapses 0.94→0.04 MAF, autarky leakage 0.57, pool becomes the leakage
  channel (+2.93, −0.54B@1k). Reported in sensitivity via Mc* macros.

Baseline fit (tab:baseline_fit, untargeted): trade 0.94 vs 0.89 obs; buyer
demand −0.4%; fallow 9.5 vs 9.9%; blended cost $173 vs $171. STALE until the
long chain finishes: Sens* macros, Boot* CI brackets, sens_*.pdf figures.
Related: [[cf-decision-price-acpass]], [[settled-cf-rules]].
