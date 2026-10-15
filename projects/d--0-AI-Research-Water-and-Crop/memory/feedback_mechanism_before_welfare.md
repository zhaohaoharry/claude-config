---
name: feedback-mechanism-before-welfare
description: "In counterfactual results sections, present the mechanism (what physically changes) before the welfare aggregation, not after — the reader should understand *why* welfare moves before seeing the number"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---

In a counterfactual results subsection, the right ordering is **mechanism first, welfare second**.

> **Section opening (topic sentence):** "Using the structural estimates, I conduct the counterfactual analysis."
>
> **Then immediately:** the figure that shows the *physical* change (crop mix, acreage, prices — the thing the model is producing).
>
> **Then the mechanism paragraph:** what economic force is at work. E.g., "groundwater regulation closes the over-pumping that sustained orchards → perennial acreage falls and reallocates to annual + fallow → escapes demand hardening. Surface-water integration acts on the same margin in the opposite direction."
>
> **Then welfare table** with $\Delta\mathcal{W}$ headline numbers, CIs in brackets, sandwiched between the mechanism (now understood) and the policy ranking discussion.

**Why:** The welfare numbers are the *consequence* of the mechanism, not the substance. Leading with a $3\times 3$ welfare table forces the reader to memorize nine numbers before they know what economic force produced them. Leading with the crop-mix figure lets the reader build the mechanism in their head, so the welfare numbers land as "yes, of course — that's the size of the effect."

**How to apply:** When restructuring a counterfactual subsection, ask: does the reader already know *what physically changes* by the time they see the welfare number? If not, move the physical-change figure (acreage, prices, quantities — whatever the model produces beyond welfare) ahead of the welfare table. Remove duplicate display: if the same data appears in both the figure and the welfare table (e.g., the welfare table also lists acreage rows), strip it from the table.

Composes with [[feedback-topic-sentence-first]] (topic sentence carries purpose+method) and [[feedback-econ-paper-flow]] (table-first within a paragraph, but mechanism-first across paragraphs).

Applies across all research projects.
