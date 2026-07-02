---
name: feedback_every_number_has_provenance
description: Every number in a paper must trace to a saved generator+raw data or a verified citation; no hand-built results; run the provenance audit before sharing
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

Research-integrity rule the user made non-negotiable (2026-06-18, Water and Crop, after finding tab_sumstats_district.tex and tab_cf_iv.tex were hand-built and stale/wrong). **Applies across all research projects.**

Every number that appears in a manuscript is exactly one of two kinds:
1. **Computed** — it traces to a *saved generator script* in `program/` that reads *credible canonical raw data* and writes the artifact. The `tables/*.tex` and `figures/*` files are build artifacts, NEVER hand-edited. Re-running the generator must reproduce the committed file.
2. **Cited** — it traces to a specific external source (bibkey + page/table/figure or official-doc locator), verified against the actual document.

There is no third category. **Never type a computed result directly into the manuscript or into a `tables/*.tex` file.** That is how `tab_sumstats_district.tex` (Fallow 11,086 vs the true 8.7%) and `tab_cf_iv.tex` (numbers that reproduce from no result file) went stale/wrong with no way to detect it.

**Why:** a hand-entered number has no link to the data, so when the data or params update it silently goes stale, and it cannot be audited. This is a research-integrity failure, not a cosmetic one.

**How to apply:**
- Before writing any number into prose/table/figure, make sure a script produces it. If reporting an estimation sample, summarize the *exact* data that enters estimation (e.g. `results/B1d_ccp_firststage.pkl`), not a convenient nearby file. Never use experimental/robustness vintages (e.g. 2017-fill, `_v2`) for main results — see [[data_v2_suffix_is_experimental_not_canonical]] and [[feedback_verify_canonical_data_before_use]].
- In-text numbers ideally come from `\newcommand` macros that a generator writes into a `latex/*_auto.tex` the manuscript `\input`s, so prose numbers update on re-run too.
- Run `python program/audit_provenance.py` (built 2026-06-18) before every `/sync-to-github` and before any submission. It flags any `\input{tables/...}` or `\includegraphics{figures/...}` with no generator script (an ORPHAN = hand-built risk). Exit 1 on any orphan.
- A generator existing is necessary but not sufficient: also confirm its output still *matches* the committed file (staleness) and that the source data is canonical.

See [[project_table2_provenance_rebuild]] for the Water-and-Crop specifics (Table 2 fixed via `build_tab_sumstats.py`; `tab_cf_iv.tex` still an open orphan).
