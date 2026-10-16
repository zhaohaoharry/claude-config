---
name: scalable-computing-2026-10
description: "ScalableComputing multi-PC compute framework (from Ohyun) installed 2026-10-15; file locations, host readiness, and the macOS port validated on HMac"
metadata:
  node_type: memory
  type: project
  originSessionId: 0a73e471-ad5d-46a8-9221-27dd2d33c900
  modified: 2026-10-16T06:14:24.861Z
---

Ohyun's `**ScalableComputing` framework was installed on 2026-10-15 so long computations (Monte Carlo, bootstraps, batch estimation, specification grids) can be split across the user's machines.

Locations: rule doc at `~/.claude/rules/scalable-computing.md`; trigger and worker clause in `~/.claude/CLAUDE.md`; shared folder at `D:\Dropbox\AI\ScalableComputing` (`tools\`, `jobs\`, `machines\`, `WORKER_PROMPT.md`), inside the live Dropbox account so it actually syncs. Computation runs on local disk (`C:\SC_local\<job_id>` on Windows, `~/SC_local/<job_id>` on macOS) and only sealed batches cross Dropbox.

**All three machines are now working compute hosts.** LaoZhao passed the full local self-test on 2026-10-15. H2 is preflighted (4 physical cores, numpy 2.5.4 / scipy 1.18.1 / pandas 3.0.6, VBS off) but has never run a job. **HMac passed on 2026-10-16**: 48/48 units of `jobs/selftest_mac`, zero failures, 1,912 units/h at 6 workers against an ideal 2,700, with pause freezing all six unit processes at 0% CPU and resume continuing them. That was the macOS port's first real run anywhere. HMac is python.org 3.13.2 (not Homebrew), numpy 2.4.5 / scipy 1.18.1 / pandas 3.0.3 / psutil 7.2.2, M3 with 8 cores and 16 GB.

**Three things learned bringing HMac up, all fixed in the tools:**
- **macOS hostnames are not stable.** `hostname -s` is DHCP-derived and changed between two consecutive days (`Haos-Laptop-266` → `-281`). Since `assignment.json` is keyed on host name, an unpinned run would silently find none of its own units and exit looking successful. `launch.sh` and `machine_card.sh` now read a pinned id from `~/.sc_host`, which `setup_mac.sh` writes as **HMAC** — use that name for HMac in every assignment.
- **A python.org interpreter has no CA bundle** until its `Install Certificates.command` is run, so pip fails with `CERTIFICATE_VERIFY_FAILED` and it is not TLS interception. `setup_mac.sh` probes TLS, runs that installer, and falls back to `--cert /etc/ssl/cert.pem`.
- **A heartbeat bug, found by HMac's session:** the runner wrote its forced heartbeat *before* `apply()`, so a state change published the previous freeze/thaw counts under the new state name (a resume advertised "run / running 0 / frozen 6" for an interval). Since `**ScalableComputing status` treats heartbeats as ground truth, that reads as a stall that is not happening. The beat now follows `apply()`; verified on Windows.

`tools/setup_mac.sh` is the one-shot macOS bring-up (stable host id, `python` on PATH for the hooks, packages, machine card, self-test assignment) and is safe to re-run. `jobs/selftest_mac/` is the cross-platform self-test: `{python}` placeholder and forward slashes, 48 units, no package dependencies, so it tests the framework rather than numpy. Windows accepts forward slashes, so one manifest runs on both platforms.

**Dispatch targets (user, 2026-10-16):** each worker PC has a dedicated Claude session named **SC_task** (one on HMac, one on H2). Send all future computing tasks (`[ScalableComputing]` commands) to those SC_task sessions, not to whatever other session happens to be open on that PC. The coordinating session on LaoZhao is for setting up jobs; the SC_task sessions run them. ListAgents does not show the host, so resolve each SC_task row's machine from its preflight reply.

**First real job, 2026-10-16 (ETFP `jobs/etfp_hettheta_g7`, 2 units, HMac):** one whole iterated-GMM estimation per unit worked despite breaking the 1–5 minute guideline (max_retries 0; a failure costs one estimation). HMac reproduced LaoZhao's single-theta estimates to the 5th digit (numpy 2.4.5 / pandas 3.0.3 / Python 3.13 vs LaoZhao's numpy 2.2.4). HMac now has jax 0.11.2 (CPU, user site). Like-for-like timing of one estimation: HMac 25 min (while running a second unit), LaoZhao alone 33 min; the 84 min seen in the grid came from several estimations contending for LaoZhao's cores (JAX/XLA takes ~7 cores per estimation regardless of intra_op threads). Lesson: trace every input file through the WHOLE unit, including post-estimation steps — the first launch failed after 23 min on a file read only at the end.

- **The yield feature had never worked at all.** `ioreg -c IOHIDSystem -d 1` limits the walk to depth 1 of the whole IORegistry rather than of the matched object, so the HIDIdleTime line was never reached and `idle_seconds()` returned None forever; `--yield-when-active` therefore ran at full workers and never yielded, silently. `-r` fixes it. A broken idle probe now logs a warning rather than failing open, and the heartbeat publishes `idle_s` and `yielding`.

**The macOS port is now fully validated** (HMac, 2026-10-16, `jobs/selftest_yield`, 180 units, 2,439 units/h): 6 workers untouched, down to 1 active with 5 frozen within 2 s of a keystroke, back to 6 within 2 s of the idle threshold. While a yield is in force the runner thaws a frozen unit as a live one finishes instead of launching a new one, so the in-flight count drains — intended. Budget about `active_workers/workers` of the unyielding rate while the user is working: roughly 400–450 units/h on HMac at `--active-workers 1`.

Still untested: any two-machine run. `selftest2` is packaged and preflighted but has never been launched, and H2 is 3 workers at 8.4 s per unit.

Cross-session messaging works between all three machines over Remote Control in bypass mode; there is no read receipt, so a worker's reply is the only confirmation. Worker sessions correctly refuse to install or change settings on a peer's word alone and ask their own user — that is the designed behaviour, not an obstacle. See [[machine_names]], [[h2_windows_updates]], [[stata_per_machine]] and [[research_data_repository]].
