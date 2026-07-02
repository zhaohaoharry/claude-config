---
name: swp-delivery-entitlement-weighted
description: "Water and Crop: SWP delivery+cost+simple delivery price cleaned by build_swp_delivery_cost.py (D5) from Bulletin 132 App B; market-price calibration deferred (compare_swp_price_options.py, undocumented); district SWP alloc = entitlement share of Kern-Ag delivery (Stage-1.5 LP)"
metadata:
  type: project
---

Since 2026-06-22 the surface-water pipeline (PIPELINE_manual.tex) runs:
**D4 SWP entitlement** (`SWP_entitlement.do`), **D5 SWP delivery+cost** (`build_swp_delivery_cost.py`),
**D6 CVP** (`CVP_trade.do`), **D7 Kern River** (`build_kern_river_allocation.py`), **D8 roster**
(`build_district_roster.py`), **D9 supply** (`build_district_sw_supply.py`). Auto-numbered via `\dstep`/`\dref`.

**D8 roster** (`build_district_roster.py`, NEW) replaces the legacy `WD_month.do` (archived): a slim pure-roster
builder that inner-joins the DWR GIS district layer to the curated Kern concordance, sorts by agencyname,
`agency_id = _n`. Writes `Kern_WD.dta` + `agency_id.dta`, reproducing the legacy essentials exactly (agency_id kept
float to match the merge key). WD_month.do's other outputs had no production consumers.

**D9 supply** (`build_district_sw_supply.py`, rewritten) = the district x year panel the estimation reads:
**SW_SWP = ACTUAL supply** = `(E_k/sum_l E_l) * Kern_Ag_delivery` over the **13 ag SWP districts** (KCWA ID4 excluded,
urban), reading SWP_entitlement (D4) + SWP_Kern_B132_Ag_MI (D5) -- moved here from B1d, reproduces it exactly
(verified, district allocations sum to Bulletin-132 delivered total). **SW_CVP = actual delivery; SW_KR = rights.**
**Clean panel (2026-06-22 "clean it"):** the vestigial `SWP_rights`/`allocation_final` columns were DROPPED from the
D9 output, so `district_sw_supply.dta` is now a pure actual-supply panel
`[agency_id, agencyname, year, GW, has_SWP, SW_SWP, has_CVP, SW_CVP, has_KR, SW_KR, SW_total, connected_{SWP,CVP,KR}]`.
A5 (the only live consumer of those two cols) now reads the statewide rate `a_t` (`allocation_final`) from its own
source `SWP_allocation_year.dta` (merge on year) -- **proven AC_kt-invariant** (all 343 SW_SWP>0 district-years had
old-panel rate == source rate; differences only on SW_SWP=0 rows, ×0). A5's read path is therefore already clean.
The remaining DEFERRED item is only the *propagation*: re-running A5 recomputes `district_water_cost.dta` on the
actual SW_SWP (left for the user's structural rerun; B1d still builds its own identical SW_SWP copy).
Plan: quality_reports/plans/2026-06-22_d9-district-year-supply-restructure.md.

**D5 = single Bulletin-132 extraction point** (`build_swp_delivery_cost.py`, renamed from `build_swp_delivery.py`):
delivery (Table B-5B) + the Kern SWP bill (total transport B-19 + Delta charge B-21 + revenue-bond surcharge B-22,
summed over the 3 Kern cols) + the **simple delivery price** `delivery_price = (Total bill x Ag share) / Kern_Ag
delivery` (= total cost / total delivered, NO calibration). Outputs `SWP_Kern_B132_Ag_MI.csv` (delivery) +
`SWP_Kern_B132_cost.csv` (bill + delivery_price). Charge tables located by caption + "San Joaquin Valley" header
(NOT hardcoded pages). `delivery_price` == `compare`'s `P1_uniform`.

**Transfer-price DATA collection is now a real step (2026-06-22), D10 `build_swp_transfer_prices.py`** -- collects
SWP/water transfer (market) price observations from multiple sources into one labeled panel
`data/clean/swp_transfer_prices.csv` (66 obs, 26 in_fit). Reads a NEW raw file
`data/raw/Water supply/SWP/swp_transfer_price_records.csv` (54 cited bilateral transfers Belridge/Berrenda/Lost Hills
2014-15 + Westside5 2010 + 3 news quotes; seeded from `transfer_transactions_consolidated.csv`, numbers identical) +
raw FRED `NQH2O_FRED_weekly.csv` (computes Apr-Oct irrigation-season means) + `SWP_allocation_year.dta`. Schema:
source_type (bilateral_transfer/nqh2o_index/news_quote)/source_label/price_usd_af/volume_af/classification/role/in_fit/
alloc_t/units/citation/notes. Also regenerates `NQH2O_irrigation_season_stats.csv` (was an orphan). Verified: bilateral
prices == canonical (max|Δ|=0), NQH2O stats bit-identical. `\dstep{swptransfer}` after D9.

**Market-price CALIBRATION FIT remains deferred (user: "haven't worked on it yet")** -- D10 is DATA-ONLY (no fit).
The trade price `P3_market` (and the full `SWP_KernAg_three_prices.csv` that B1d reads for
P1_uniform/P3_market/Deliv_Ag) is still produced by `compare_swp_price_options.py`, left untouched, as future work.
TRANSITIONAL: `calibrate_swp_price_v3.py` (fit) + `build_price_source_figure.py` (figure) still hardcode their own
copies of the records; repoint them to read `swp_transfer_prices.csv` (filter in_fit) later (user drives).

**Known bug for the future calibration (in the deferred `compare`, NOT fixed):** `compare`'s B-18 read is PDF p157 =
North Bay sheet, not San Joaquin Valley (p158); its "variable cost" is tiny/negative. Affects only `compare`'s
figure-only two-tier price P2, never P1_uniform/P3_market/Deliv_Ag. D5 is unaffected (drops B-18; the bill uses B-19,
which already includes the variable component).

**District SWP allocation = delivery weighted by entitlement.** Each district's *actual* SWP allocation is its
entitlement share of the realized Kern-Ag delivery, `Ealloc_k = (E_k / sum_k E_k) * Kern_Ag`, so district
allocations sum to the Bulletin 132 delivered total — NOT to the nominal Table-A x allocation-rate aggregate.
This pro-rata is applied in the **Stage-1.5 LP** `program/2_structural/B1d_step1p5_water_allocation.py` (it reads
`SWP_KernAg_three_prices.csv` -> `Deliv_Ag` = `Q_deliv_SWP`). The entitlement weights `E_k` come from D4.

**D5 generator** `program/1_data/build_swp_delivery.py` extracts annual Kern Ag + M&I SWP delivery from
`data/raw/Water supply/SWP/DWR_Bulletin_132-23_AppB.pdf`, **Table B-5B** ("San Joaquin Valley Area / Kern" sheet,
PDF page 79) -> `data/clean/SWP_Kern_B132_Ag_MI.csv` (year, Kern_Ag, Kern_MI, 1996-2022). It **closed an orphan**:
that CSV had no generator but production already depended on it. Parser is **positional chunk-by-9** (a naive
year-led parse breaks: area values like Empire's 1,978 AF look like a year and truncate the row, silently dropping
1968/1979/1990/2008/2009); validated by per-row checksum (7 area cols sum to printed Total) + documented anchors.
8 columns: Dudley[11] Empire[12] Kern_MI[13] Kern_Ag[14] Kings[16] OakFlat[17] Tulare[18] Total[19] (no [15]).

(Reconciled 2026-06-22: D9's `SW_SWP` IS the delivery-weighted actual supply `(E_k/ΣE)×Kern_Ag` — the old
"entitlement × rate" notion is gone from the panel, and the entitlement/rate columns are no longer carried. The
delivery-weighted allocation that once lived only in the Stage-1.5 LP now also lives in D9, reproducing it exactly.)
Relates to [[settled_cf_rules]] and [[counterfactual_results]].
