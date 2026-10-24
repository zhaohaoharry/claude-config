# Data Integrity in Analysis Code — no silent sample loss, no hollow variables

Universal rule for every script that reads, cleans, merges or estimates on data (Stata, R, Python,
Julia), in every project. Added 2026-10-24.

## Why this rule exists

Coding agents take the simplest path through messy data and do not report it. In a June 2026 test
of Claude Code and Codex on an ISSP reproduction, each agent resolved undocumented choices (a
`999,996` no-answer sentinel in income, wave-specific education codes) silently and differently
across runs, moving the analytical N by up to about 1,000 respondents (Alizadeh, Gilardi, Mosleh
and Kasneci, arXiv 2606.11456). In BAITBENCH, agents that found a shortcut presented it as a valid
strategy in 42.7% of runs (arXiv 2608.30724). The two failures that matter here are (a) rows lost
without a count and a reason, and (b) a variable reported as available when it is mostly missing.
An instruction alone does not stop either, so this rule pairs with the `data-guard` hook and with
the checks in `data-cleaning`, `econometrics-playbook` and `verify-code`.

## The rules

1. **Every row lost has a count and a reason.** A script that drops, filters, merges, reshapes or
   estimates writes one line per step to a sample-flow ledger, `log/sample_flow.csv`, with columns
   `step, rows_in, rows_out, units_out, dropped, reason`. The ledger is written by the script, never
   by hand, so it is a build artifact like `tables/*.tex`. Helpers: `skills/data-cleaning/tools/`
   (`sample_flow.py` for Python, `sample_flow.do` for Stata).
2. **Every variable used or described has a coverage card.** Before code relies on a variable, or
   before any message says a variable "exists", "is available" or "is in the data", report its
   non-missing count and share overall and by the panel's time and unit dimensions, its number of
   distinct values, and its min/max. A variable that is constant, or non-missing for under 80% of
   the intended sample, is reported as such in the same sentence. Never write "the data contain X"
   on the strength of a column name.
3. **Scan for sentinel codes before treating values as real.** Check every numeric variable for
   values such as 9, 99, 999, 9999, 999996-999999, -1, -8, -9, -99, and for heaping at a top code.
   Decode them to missing with a cited source (the codebook or questionnaire page), or report them
   as an open question. Do not guess their meaning.
4. **Stop thresholds.** Stop and report to the user, instead of continuing, when any single step
   drops more than **5%** of its input rows without a reason the user has already approved, when a
   merge leaves more than **5%** of the master unmatched, or when a key variable covers under
   **80%** of the intended sample. A project may set other thresholds in its `CLAUDE.md`; the
   project values then apply.
5. **Merges are diagnosed, never assumed.**
   - Stata: `merge` with the cardinality stated (`1:1`, `m:1`), `tab _merge` before any `keep`, and
     `keep(match)` only after the unmatched counts are written to the ledger.
   - Python: `pd.merge(..., validate="m:1", indicator=True)` (or the right cardinality), report
     `_merge` counts, and name `how=` explicitly. The pandas default `how="inner"` silently drops
     unmatched rows.
   - R: `dplyr::*_join(..., relationship = "many-to-one")`, then `anti_join` to count unmatched.
6. **No bare missing-value drops.** No `dropna()` without `subset=` and a ledger line; no
   `drop if missing(...)` / `keep if !missing(...)` without the count; no `na.omit()` on a whole
   frame. `groupby` in pandas drops missing keys by default: pass `dropna=False` or count them.
7. **The estimation sample is reconciled.** After each regression, compare the estimation N
   (`e(N)`, `nobs`, `len(model.model.endog)`) with the intended sample in the ledger. Report the
   gap and which variables caused it (listwise deletion over controls, `reghdfe` singleton and
   separation drops, `ppmlhdfe` separated observations). Every N in a table must match a ledger row
   or a stated reconciliation.
8. **Low-coverage results are labelled where they are reported.** If an estimate rests on a
   subsample created by missing data, say so next to the number, with the share of the intended
   sample it covers.

## What this rule does not do

It does not forbid dropping data. Dropping by an explicit, recorded, justified rule is ordinary
cleaning. It forbids dropping, imputing or recoding **without a count and a reason**, and describing
data more completely than the counts support.
