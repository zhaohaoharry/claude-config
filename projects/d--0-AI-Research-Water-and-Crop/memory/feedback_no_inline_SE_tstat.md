---
name: No inline (SE, t-stat) in manuscript prose
description: Never present empirical results in main-text prose as "(SE 0.18, t=-3.95)". Only the point estimate belongs in prose; SE, t-stat, and other statistical machinery live in the tabnotes of the relevant figure or table, or in the relevant body section's regression-results paragraph. Applies across all research projects.
metadata:
  type: feedback
---
In manuscript prose — particularly in stylized facts, introduction discussions of empirical findings, and any main-text narrative — never report a result in the parenthetical form `(SE X, t=Y)`. Report only the point estimate. The standard error, t-statistic, R², N, and significance asterisks belong in the tabnotes of the relevant figure or table, never inline in narrative prose.

**Disallowed phrasings:**

- "A well one mile farther from the cluster loses 0.69 ft less head over the period (SE 0.18, $t=-3.95$)."
- "The treatment effect is $\beta = 0.34$ (SE 0.12, $t=2.83$, $p<0.01$)."
- "Drawdown decays at $-0.7$ ft/mile ($t=-3.95$, $N=313$)."

**Allowed phrasings:**

- "A well one mile farther from the cluster loses 0.69 ft less head over the period." (and tabnotes carry SE, t, R², N)
- "The treatment effect is 0.34 percentage points." (and the regression table carries SE)
- "Drawdown decays at roughly $-0.7$ ft per mile from the buyer cluster, statistically distinct from zero." (qualitative significance statement; full SE in tabnotes)

**Why:** Top-journal economics writing keeps narrative prose readable. Inline `(SE, t)` reports interrupt the sentence with statistical machinery the reader does not need at that moment, and they read as draft-style rather than finished prose. Reviewers and editors treat them as a draft-stage tic.

**Where SE/t-stat ARE appropriate:**

- In tabnotes of figures and tables.
- In the regression-results paragraph of Section 5 / Section 6, where the empirical specification is the subject of the paragraph and the reader expects the statistical detail.
- In appendix robustness paragraphs comparing alternative specifications.

**How to apply:** Before saving any manuscript edit that introduces a new empirical fact in prose, grep the diff for the patterns `(SE`, `t=`, `t = `, `t-stat`, `SE = `, and similar. If found inside running prose (not inside a tabnotes block or a regression-results subsection), strip the parenthetical and move the underlying statistics to the relevant figure's tabnotes.

**Why:** The user flagged the pattern explicitly on 2026-06-03 after I included "(SE 0.18, $t=-3.95$)" inline in the Fact 3 stylized-fact paragraph of the Water and Crop manuscript. The user wrote: "as I said, never present empirical results in this way: (SE 0.18, t=-3.95) here we dont need to mention these two stats. and further refine the language to be more natural econ writing." Apply across all research projects.
