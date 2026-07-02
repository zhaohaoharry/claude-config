---
name: data-cleaning
description: Build a reproducible, scripted data-preparation pipeline in Stata or R — import, merge, reshape, construct variables, handle missing data, deduplicate, encode/label, winsorize, and save tidy analysis-ready files with CSV snapshots. Use when turning raw data into an analysis dataset, NOT for estimation (use econometrics-playbook for that).
argument-hint: "[raw file or task, e.g. 'survey.csv' or 'merge waves into a panel']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Bash"]
---

# Data Cleaning

Build a reproducible data-PREP pipeline that turns raw inputs into a tidy, analysis-ready dataset. This skill does **data preparation only** — no estimation, regressions, or tables of results (that is `econometrics-playbook`).

**Input:** `$ARGUMENTS` — a raw data file, a folder of raw files, or a prep task (e.g. "merge the three waves into a panel").

## Reproducible-build mindset

- Everything is scripted in a do-file (Stata) or `.R` script. **Never edit the data by hand**, never overwrite raw inputs.
- The script runs top-to-bottom from raw inputs to the saved analysis file with no manual steps in between.
- Re-running the script on the same raw data reproduces the same analysis file, byte-equivalent where possible.
- Default to writing and running the script in `program\sandbox\` unless the user explicitly requests a production run.

## Steps

1. **Understand the data and target.** From `$ARGUMENTS`, identify: the raw source(s) and format; the unit of observation; the desired unit of the final dataset (cross-section, panel, etc.); key variables needed downstream. Ask the user only if these are not inferable.

2. **Pick the language.** Stata if the project already uses Stata or the raw is `.dta`; R if the project uses R or the raw is mixed/large CSV. State which and why.

3. **Scaffold the script** with a header (project, author, date, input, output), environment setup, and clearly numbered sections (import → inspect → clean → construct → missing → dedup → label → validate → save). Define path globals/objects at the top; use relative or global-defined paths, never hard-coded absolute paths scattered in the body.

4. **Import and inspect.** Load raw data read-only. Inspect structure and ranges (`describe`, `codebook, compact`, `summarize` in Stata; `str`, `summary`, `skimr::skim` in R). Export a CSV snapshot of the as-loaded data to `log\`.

5. **Merge / append / reshape** as needed. Always diagnose merges (`tab _merge` BEFORE asserting in Stata; check join key cardinality and unmatched rows in R). Confirm the post-reshape unit of observation. Snapshot to `log\` after each structural step.

6. **Construct variables.** Derive analysis variables with documented logic; comment WHY, not just what. Guard against Stata's missing-sorts-high trap (`& !missing(x)` on every `>`/`>=` condition).

7. **Handle missing data.** Decode missing-value codes (`mvdecode` / explicit `NA`), create missing-indicator variables where informative, and document the missingness (counts and patterns). Do not silently drop — record what is dropped and why.

8. **Deduplicate.** Report duplicates before acting (`duplicates report`/`list`), resolve by an explicit rule, then verify the key is unique (`isid`/`unique` in Stata; `stopifnot(!any(duplicated(...)))` in R).

9. **Encode and label.** Encode strings to numeric where appropriate; attach variable labels and value labels to every kept variable. Standardize string categories (case/trim) before encoding.

10. **Outliers / winsorize.** When called for, winsorize or trim at stated cuts (e.g. 1/99) into NEW variables, never destroying the raw values. Document the cut and the affected count.

11. **Validate.** Assert expected ranges, types, and key uniqueness. Use the house-rule failure idiom (see Important), not `assert ..., msg()`.

12. **Save and snapshot.** `compress` (Stata), order variables logically, save the tidy analysis file to the clean-data location, and export a final CSV snapshot to `log\`. Write a short codebook of the final file.

## Output Format

Deliver a single runnable script. Structure it as:

```stata
/*=============================================================================
  Project: [name]      Author: [name]      Date: [YYYY-MM-DD]
  Purpose: Prepare raw [...] into analysis-ready dataset
  Input:   data/raw/[...]      Output: data/clean/[...].dta
=============================================================================*/
clear all
set more off
cap log close
log using "data_prep.log", replace          // log created in CWD (run from sandbox\)

global raw   "data/raw"
global clean "data/clean"
global snap  "log"                            // CSV snapshots for debugging

* 1. IMPORT & INSPECT
import delimited "${raw}/survey.csv", clear varnames(1)
codebook, compact
export delimited "${snap}/snap_01_loaded.csv", replace

* 2. MERGE / RESHAPE  -> tab _merge BEFORE assert
* 3. CONSTRUCT        -> guard missing: gen hi = (x>50000) if !missing(x)
* 4. MISSING / DEDUP  -> duplicates report id ; isid id
* 5. LABEL / WINSORIZE
* 6. VALIDATE
qui count if missing(id)
if r(N) > 0 { di as err "id has missing values"; error 9 }
isid id

compress
order id year
save "${clean}/analysis.dta", replace
export delimited "${snap}/snap_final.csv", replace
log close
```

After producing the script, report: language chosen, where it was written/run, the snapshot files created in `log\`, and any rows dropped or values winsorized (with counts).

## Important

- **Stata house rules (mandatory):**
  - Batch mode uses the `-e` flag, never `/e` (e.g. `stata-mp -e do data_prep.do`).
  - The log file is created in the **current working directory**, not the do-file directory — run from `program\sandbox\`.
  - Keep do-files in **CRLF** line endings (run `unix2dos` if they were written with LF).
  - Run in `program\sandbox\` unless the user explicitly requests a production run.
  - Export **CSV snapshots to `log\`** at every key data step so failures are debuggable.
  - Validate with `if <fail> { di as err "..."; error 9 }` — **never** `assert ..., msg()`.
  - Always `tab _merge` before asserting on a merge; guard every `>`/`>=` with `& !missing(x)`.
- **No estimation.** Stop at the saved analysis file. Regressions, fixed effects, and results tables belong to `econometrics-playbook`.
- **Never overwrite or hand-edit raw data.** Raw inputs are read-only; all changes happen in the script.
- **Document drops.** Every dropped row and every winsorized value is logged with a count and a reason.
- **Determinism.** Set a seed for any random step; sort before order-dependent operations; avoid machine-specific absolute paths.
