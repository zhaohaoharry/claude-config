---
name: feedback-etfp-first-stage-no-sigma
description: ETFP first-stage share coefficient is a nuisance; never judge it by an implied sigma or the sigma<0 bound
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-10-10T12:32:54.199Z
---

In ETFP, the coefficient on ln S in the JDE-style first stage is a nuisance parameter (as alpha_SM in Zhang 2019). Never map it to sigma or evaluate it by "implied sigma", "sigma < 0", or "the model rules out c > -1".

**Why:** the user and I established (2026-10-10) that the first stage carries no information about sigma; sigma comes only from the second-stage GMM.

**How to apply:** judge a first-stage coefficient only by how well it recovers e: the size of the divisor 1+c (how much e = u/(1+c) is scaled), precision, stability across specifications, and whether the recovered e looks like iid measurement error (size, persistence, correlation with the deflator). Related: [[feedback-no-footprints-of-abandoned-designs]].
