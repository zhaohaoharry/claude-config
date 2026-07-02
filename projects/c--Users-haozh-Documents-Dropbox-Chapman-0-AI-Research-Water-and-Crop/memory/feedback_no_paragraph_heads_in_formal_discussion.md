---
name: feedback-no-paragraph-heads-in-formal-discussion
description: "Do not use \\paragraph{} subheadings inside results, discussion, or sensitivity sections of an econ paper; use flowing prose with topic sentences and paragraph breaks instead"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---

In formal economics-paper sections (Results, Sensitivity Analysis, Discussion, Robustness, etc.), **do not use `\paragraph{}` subheadings** to organize the prose. Top-5 econ journals expect these sections to flow as continuous argument, with topic shifts signaled by topic sentences and paragraph breaks. Subheadings inside a subsection read as research-note or thesis-chapter formatting.

**Where `\paragraph{}` is OK:** the model section (e.g., `\paragraph{Setup}`, `\paragraph{Equilibrium}`), the data section (e.g., `\paragraph{Plot panel construction}`), or as an italic run-in lead for a worked example or a definition. Headings of this sort describe a *building block* of the model or data, not a *result*.

**Where it is NOT OK:** Results, Sensitivity Analysis, Robustness, Discussion, Conclusion subsections. The prose there should narrate findings, not partition them with subheadings.

**Example.** A Sensitivity Analysis subsection with headings like `\paragraph{Externality value $\sigma$}` then `\paragraph{Discount factor $\beta$}` reads as a checklist. The same subsection without those headings — with topic sentences like *"I conduct sensitivity analysis on the auxiliary parameter values..."* / *"The other auxiliary parameters leave the ranking unchanged..."* — reads as econ-paper prose.

**How to apply:** when adding a new results / sensitivity / robustness section, write as flowing paragraphs. If a structural break is needed, use a paragraph break and a sharp topic sentence. Reserve `\paragraph{}` for the model/data/estimation building-block sections.

Applies across all research projects.
