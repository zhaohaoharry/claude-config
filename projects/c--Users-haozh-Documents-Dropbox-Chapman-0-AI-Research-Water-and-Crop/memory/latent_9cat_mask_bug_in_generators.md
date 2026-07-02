---
name: latent_9cat_mask_bug_in_generators
description: "Water-and-Crop: leftover hardcoded 9-cat crop_cat masks (perennial=[1,2,3,4], active/non-fallow includes cat 8) are a recurring latent bug in exhibit generators not yet repointed to the 8-cat construct. Check every generator that hardcodes a crop_cat list."
metadata:
  node_type: memory
  type: project
---

When repointing an exhibit generator to the **de-overlapped 8-category** data, watch for **hardcoded `crop_cat`
masks written for the retired 9-category scheme**. Under 9-cat, perennials were `crop_cat 1-4` and fallow was `9`;
under 8-cat, perennials are `[1,2,3]` (nuts, tree fruit, grapes & berries), annuals `[4,5,6,7]`, and **fallow is `8`**.
A leftover `crop_cat.isin([1,2,3,4])` silently counts **Cotton & field (cat 4) as perennial**, and a leftover
"active/non-fallow" mask `[1..8]` wrongly **includes fallow** (now cat 8).

Two instances found and fixed 2026-06-23:
- **Figure 2** (`draw_fig_sf1_v2.py`): `PERM = {1,2,3,4}` → `{1,2,3}`. Inflated perennial growth ×1.14 → corrected ×1.89.
- **Figure 3** (`build_sf3_spatial_leakage.py`): perennial-share control `per=[1,2,3,4]`, `active=[1..8]` →
  `per=[1,2,3]`, `active=[1..7]`. Perennial-share mean 0.71 → 0.57; controlled slope −1.27 → −1.77.

**To-do when touching any remaining un-repointed generator** (e.g. `tab:sf4_trades` / `build_*` exhibit scripts,
and the structural A5/A10/B1d when the user runs the rerun): grep for `isin([` / `crop_cat ==` / `1, 2, 3, 4` and
confirm the mask is on the 8-cat convention. The canonical perennial set is `[1,2,3]`, fallow is `8`. See
[[overlap_resolution_deoverlap]], [[crop_concordance_8cat]], [[fig2_perennial_water_2017_artifact]].
