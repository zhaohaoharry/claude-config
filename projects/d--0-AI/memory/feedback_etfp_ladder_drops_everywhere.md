---
name: feedback_etfp_ladder_drops_everywhere
description: ETFP cleaning ladder - dropped firm-years leave every analysis, not only the first-stage coefficients
metadata:
  type: feedback
---
ETFP sample ladder (user, 2026-11-06): firm-years dropped by F1-F3 are out of all analysis. The first stage runs on the cleaned sample (79,741 rows), the trim and GMM run inside it, and only GMM rows carry omega and tau into later analysis. e outside that sample is needed only for the t-1 lag of a kept row, either by the first-stage coefficients or by carrying e_t back.

**Why:** the code's F3b only moved the coefficient estimation; trim cutoffs and descriptive/aggregate exhibits still used wider rows (139,751 with e, 109,004 with omega and tau), which is how firm 14520's 2006 row reached Figure 7.

**How to apply:** check any sample change end to end: first stage, trim base, lags, GMM, every downstream exhibit. Related: [[feedback_etfp_bootstrap_order]].
