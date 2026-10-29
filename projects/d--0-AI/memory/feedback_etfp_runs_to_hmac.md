---
name: feedback-etfp-runs-to-hmac
description: ETFP estimation runs go to HMac first whenever other projects are running on LaoZhao; check before launching
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-10-28T00:54:11.863Z
---

Before launching any ETFP computation (GMM estimations, specification or IV variants, diagnostics that take more than a few minutes), check whether other projects are already running on LaoZhao (python/Stata/Julia processes not belonging to ETFP). If any are, send the ETFP runs to HMac first, through its SC_task session and the ScalableComputing job mechanism, rather than starting them on LaoZhao. The user's default for ETFP runs is also HMac ("send the runs to hmac to save space in laozhao").

**Why:** user, 2026-10-27, after two policy-IV GMM runs (218_policy_iv_gmm.py, 1-2 hours each, ~7 cores per JAX estimation) were started locally on LaoZhao while other work shared the machine.

**How to apply:** list running processes first (PowerShell Get-CimInstance Win32_Process, check command lines). Package the run as a job under D:\Dropbox\AI\ScalableComputing\jobs (self-contained code + task extract, per [[scalable-computing-2026-10]]) and message HMac's SC_task session. Keep LaoZhao for setup, packaging and merging. HMac is opportunistic capacity (lid must stay open), so for a batch that must finish, say so and keep a fallback.

**Fallback order (user, 2026-10-28):** HMac first; if HMac's SC_task session is not connected (absent or offline in ListAgents), run on LaoZhao without asking; only if neither can run, do not run. H2 is not in this order.
