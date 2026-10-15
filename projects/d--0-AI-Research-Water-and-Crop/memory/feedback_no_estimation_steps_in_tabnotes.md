---
name: feedback-no-estimation-steps-in-tabnotes
description: "Don't expose internal estimation steps (recentering, intermediate normalizations, fitting procedures) in tabnotes or manuscript prose; only the final results matter"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---

In tabnotes and manuscript prose, do not describe internal estimation steps such as recentering, normalization switches that happen mid-fit, or transformation sequences. The reader only needs the final delivered results. If the final coefficients are correct under the reported normalization, the steps taken to get there are housekeeping that belongs in code, not in the paper.

**Why:** Estimation steps are scaffolding. The reader is buying a final number under a stated convention. Exposing the scaffolding ("we estimated under fallow normalization and then recentered to the continuation-state normalization for presentation") raises the question "did the recentering preserve identification?" without providing any new information — if the final alphas are right under the stated normalization, the path is irrelevant. The disclosure adds confusion, not clarity.

**How to apply:** If a coauthor or referee suggests a sentence like "estimated under X normalization, then recentered to Y for presentation, with fitted utilities invariant", DO NOT add it. Simply ensure the tabnote names the normalization the reported alphas are read under (e.g., "continuation normalization") and stop there. The recentering, whether it happens or not, is an implementation detail of the estimator and does not need to appear in the paper. Same logic applies to any other internal estimation step (iterative procedures, two-step recentering, GMM weighting passes, fitting pivots, etc.). Applies across all research projects.

User said it directly: "as long as we get the right alpha's we dont need to mention the recentering at all, they are just steps in estimation and we only deliver the final results."

Related: [[feedback_no_author_decision_meta]] (don't expose author's decision history); [[feedback_no_code_notation_in_papers]] (don't expose pipeline phrasing).
