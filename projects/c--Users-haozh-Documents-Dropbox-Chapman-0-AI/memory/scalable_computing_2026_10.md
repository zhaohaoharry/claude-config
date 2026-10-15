---
name: scalable-computing-2026-10
description: "ScalableComputing multi-PC compute framework (from Ohyun) installed 2026-10-15; file locations, host readiness, and what still blocks the laptop"
metadata:
  node_type: memory
  type: project
  originSessionId: 0a73e471-ad5d-46a8-9221-27dd2d33c900
  modified: 2026-10-15T03:57:05.821Z
---

Ohyun's `**ScalableComputing` framework was installed on 2026-10-15 so long computations (Monte Carlo, bootstraps, batch estimation) can be split across the user's PCs.

Locations: rule doc at `~/.claude/rules/scalable-computing.md`; trigger + worker clause added to `~/.claude/CLAUDE.md` (section "Scalable computing across PCs"); shared folder with `tools\`, `jobs\`, `machines\`, `WORKER_PROMPT.md` at `C:\Users\haozh\Dropbox\AI\ScalableComputing` (inside the live Dropbox account, so it actually syncs). The 8 tools are Ohyun's verbatim; only the docs were repathed. Runs compute in `C:\SC_local\<job_id>` and send sealed batches through Dropbox.

Host state as of 2026-10-15: desktop **LAOZHAO** (i7-12700H, 14 physical cores) passed the full local self-test — bench, detached launch via scheduled task, pause (frozen units verified at 0 CPU), resume, 24/24 units, `merge --verify`. Python 3.12.10 is present but **numpy/scipy/pandas are not installed for it**, so only numpy-free jobs run today. Laptop **LAPTOP-BIS2QGG1** (4 physical cores, Windows profile `Hao Zhao`, Dropbox root `D:\Dropbox (Chapman)`) got Python 3.12.10 with numpy 2.5.4, scipy 1.18.1 and pandas 3.0.6 on 2026-10-15 (winget, user-approved at that keyboard). Its one remaining blocker is Dropbox: the client is signed out and that tree is stale since June 2023, so job transport cannot reach it until someone signs in at its GUI.

Package versions will differ between the two PCs, so the per-job `validate` step matters: state a tolerance and compare before dispatching.

Cross-session messaging between the two PCs works (Remote Control, both in bypass mode) — tested with a `[ScalableComputing]` preflight that the laptop answered. Remote Control gives no read receipt, so a worker's reply is the only confirmation. See [[user_profile]] and [[research_data_repository]] (raw data stays in `D:\0. Research Data\`, never inside the ScalableComputing folder).
