---
name: No code-style notation in formal academic writing
description: In paper drafts, never write function calls, code variable names with underscores, or pipeline-style notation like `plot_id = factorize(pmt_site, year, crop, crop_lag)`. Applies to all research projects.
type: feedback
originSessionId: 78ced47c-e9ad-4b4d-84b1-a497ab260cb9
---
Rule: In any formal academic draft (paper, slides for an academic audience, referee response), do not include code-style notation. This includes:
- Function calls like `factorize(...)`, `groupby(...)`, `merge(...)`.
- Variable names lifted from code with underscores or camelCase like `pmt_site`, `crop_lag`, `plot_id`, `decision_id_v2`.
- Data-pipeline phrasing like "we then groupby plot_id and sum per_dot_acres."
- Column names from data files quoted verbatim with `\texttt{}`.

**Why:** It reads as a data-processing log, not research writing. It distracts the reader from the substantive economic argument and signals that the description was copied from the implementation rather than thought through as prose. The user (Chapman economist) flagged this explicitly and asked for the rule to apply across all research projects.

**How to apply:** When a section needs to describe how a dataset was constructed:
1. State the raw data — what it is and what it records.
2. State the issue — what's wrong with the raw data for the question at hand.
3. State the solution — the conceptual procedure that fixes the issue, in plain prose.
4. Translate any code-level details to mathematical notation (e.g., $\bar A_p$ for plot acreage) or to natural-language paraphrase ("a plot is the set of dots that share a permit identifier and the same current and lagged crop").
5. Reserve the literal column names, function calls, and step-by-step pipeline details for the replication archive or a code-comment-style technical appendix that is clearly separate from the main narrative.

**Counter-example to avoid:** "I aggregate dot-years to plot-years via `plot_id = factorize(pmt_site, year, crop, crop_lag)` and compute `per_dot_acres = original_plot_acreage / number_of_dots_on_permit`."

**Preferred form:** "A plot is defined as the set of dots that share a permit identifier and the same current and lagged crop in a given year. Per-dot acreage is the permit-reported plot acreage divided by the number of dots inside that permit."

**Also avoid: implementation-flavored adjectives.** Words that signal the writer is thinking about the code rather than the substance — e.g., "panel-attested entitlement" (where "panel-attested" describes a data pre-processing choice and adds nothing for the reader), "baseline-simulator pumping" (when "baseline pumping" is what the reader needs), "R1-scaled endowment". If an adjective only makes sense to someone who has read the simulator, drop it; the substantive object stands on its own.
