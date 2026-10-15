---
name: scalable-computing-2026-10
description: "ScalableComputing multi-PC compute framework (from Ohyun) installed 2026-10-15; file locations, host readiness, and the macOS port"
metadata:
  node_type: memory
  type: project
  originSessionId: 0a73e471-ad5d-46a8-9221-27dd2d33c900
  modified: 2026-10-15T13:19:13.374Z
---

Ohyun's `**ScalableComputing` framework was installed on 2026-10-15 so long computations (Monte Carlo, bootstraps, batch estimation, specification grids) can be split across the user's machines.

Locations: rule doc at `~/.claude/rules/scalable-computing.md`; trigger and worker clause in `~/.claude/CLAUDE.md`; shared folder at `D:\Dropbox\AI\ScalableComputing` (`tools\`, `jobs\`, `machines\`, `WORKER_PROMPT.md`), inside the live Dropbox account so it actually syncs. Runs compute on local disk (`C:\SC_local\<job_id>` on Windows, `~/SC_local/<job_id>` on macOS) and send sealed batches through Dropbox.

**Host readiness as of 2026-10-15.** LaoZhao passed the full local self-test (bench, detached launch, pause with frozen units at 0 CPU, resume, 24/24 units, `merge --verify`) and now has numpy 2.5.4, scipy 1.18.1 and pandas 3.0.6 for Python 3.12. H2 is fully preflighted: Dropbox selective-syncs only `ScalableComputing`, all 8 tools arrived, same three package versions, VBS off, 4 physical cores. HMac is ported but untested — see below.

**The macOS port (2026-10-15, written here, not Ohyun's).** `sc_runner.py` was made cross-platform rather than forked: freeze uses SIGSTOP/SIGCONT on each unit's process group, idle detection reads `HIDIdleTime` from `ioreg`, local compute goes to `~/SC_local`. Added `sc.sh`, `launch.sh` and `machine_card.sh`; `launch.sh` detaches with nohup and wraps the runner in `caffeinate -s`. A `{python}` manifest placeholder lets one manifest run on both platforms. Ohyun's Windows originals are preserved in `tools\_original_windows\`. **Never run on macOS yet** — HMac needs its machine card and a self-test first.

**Job design constraint learned from the ETFP work:** a single 40–80 minute uncheckpointed GMM estimation does not fit the unit contract (units should be 1–5 minutes and resumable), so iterated GMM screens stay on LaoZhao. Specification grids and bootstraps are the right shape for distribution.

Cross-session messaging works between all three machines over Remote Control in bypass mode; there is no read receipt, so a worker's reply is the only confirmation. See [[machine_names]], [[stata_per_machine]] (compute layer is Python because Stata needs licence seats) and [[research_data_repository]].
