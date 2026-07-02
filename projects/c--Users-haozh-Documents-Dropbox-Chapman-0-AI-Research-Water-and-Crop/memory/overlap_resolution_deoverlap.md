---
name: overlap-resolution-deoverlap
description: "Water and Crop: Kern crop permits overlap (one permit per crop on the same field, each carrying the full field acreage) — resolved by deoverlap_permits.py so each field counts once under one 8-category; dot_panel/plot_panel rebuilt 2026-06-23"
metadata: 
  node_type: memory
  type: project
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

**The problem (discovered 2026-06-23).** Kern crop-permit polygons overlap heavily: a grower files a separate permit
(PMT_SITE) for EACH crop on the same field, and **each permit carries the whole field acreage** (the acres are the field
size repeated, not crop-specific — verified: 79% of overlap clusters have identical member ACRES; a 14.5-ac organic field
had 42 crop permits all = 14.5 ac). So summing permit ACRES double-counts the ground by ~19% (2020: sum 1.06M vs union
859k), and a 300m sampling dot on shared ground falls in several polygons at once. This (not grid spacing — the grid
covers 98%) was the real source of the ~18% acreage discrepancy in the old reconstruction.

**The fix.** `program/1_data/deoverlap_permits.py` clusters polygons overlapping >50% and resolves each to ONE
8-category, cascade: fallow-loses -> pure -> majority(member count) -> larger member area -> **ranking**
(perennial{1,2,3} > annual{4,5,6,7} > fallow{8}, then high CalPoly water; **alfalfa(5) is annual**):
Tree fruit(2) > Nuts(1) > Grapes(3) > Alfalfa(5) > Cotton(4) > Veg(7) > Grain(6) > Fallow(8). Keeps the LARGEST member
polygon (= field footprint, union≈largest within 1% for 92% of clusters), relabeled to the resolved category.

**Where it lives.** Called inside `create_sampling_dots.py` STEP 4 (classify polygons -> `deoverlap` -> sjoin dots ->
`per_dot_acres` keyed on a unique `field_id`, NOT PMT_SITE). Gives a one-to-one dot<->plot mapping, acreage counted once.
Rebuilt `dot_panel`/`dot_coordinates`/`plot_panel` 2026-06-23 (235,904 plot-decisions). Old backed up
`data/temp/deoverlap_backup_20260623/`.

**Effect (1998-2022, k acres):** raw permit 26,425 -> de-overlapped 21,569 -> reconstructed (dot panel) 21,174.
Deflation concentrated in multi-cropped annuals (Veg -41%, Grain -39%, Cotton -23%); perennials hold (Nuts -3.5%).
Reconstructed vs de-overlapped gap is a clean ~2% per category (the true small-plot coverage loss).

**Exhibits refreshed (2026-06-23).** D2 now also writes `data/clean/deoverlapped_field_acreage.csv` (year x cat:
the de-overlapped FIELD acreage, every field once — the only non-circular truth source; raw `crop_plot_WD` is NOT
de-overlapped, dot panel has only covered fields). E5 `verify_plot_reconstruction.py` (Figure A2) REWRITTEN: truth =
that CSV vs reconstruction = dot-panel `per_dot_acres` (dedup on `(dot_id,year)` first — a pixel straddling KCWA
wholesale + a member district doubles `per_dot_acres` otherwise). Honest result: 98.2% coverage, 1.8% aggregate loss,
per-cat MAPD <4.5% (Tree fruit 4.43% max), reconstruction consistently BELOW truth. E3 Table 1 + E4 Figure A1 re-run;
manuscript Figure A1/A2 captions+notes + appendix "Overlapping permits" para updated (tracked), compiles 81pp 0 orphans.

**Still pending:** A10 (`mle_sample`)/A5/B1d/B4 structural steps must re-run on the new de-overlapped sample (annuals
deflate ~40%). Relates to [[crop_concordance_8cat]], [[deferred_repoint_8cat_revenue_cost]], [[feedback_verify_by_reexecution_not_rederivation]].
