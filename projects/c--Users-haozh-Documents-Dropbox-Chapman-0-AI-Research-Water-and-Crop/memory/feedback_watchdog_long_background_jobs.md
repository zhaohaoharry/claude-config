---
name: feedback-watchdog-long-background-jobs
description: Attach a heartbeat+death/stall watchdog to any long background compute; never wait blindly on silence
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

For any long-running background job (multi-hour reruns, bootstraps, parameter sweeps), attach a watchdog that emits a periodic heartbeat (~30 min) AND fires an immediate alert on completion, silent death, or stall. Silence must never be read as success.

**Why:** An overnight sensitivity rerun failed silently — a double-launch race oversubscribed the machine, one point hung for 6h, and my detached remediation processes got reaped by the environment — and we kept "waiting" with no idea it had died. The user explicitly does not want that again.

**How to apply:** Use a persistent Monitor that checks **forward progress** — the active job's log mtime advancing / cells completing — NOT merely "is a python process alive" (a hung process is still alive). Fire on three conditions: (1) completion marker present; (2) DEATH = no relevant process running while the job's done-marker is absent; (3) STALL = active log idle beyond a threshold (e.g. 30 min).

**Survival ladder (Windows), learned the hard way — each rung survives more:** (a) foreground tool call — dies at 10-min tool timeout; (b) detached `Popen`/`Start-Process` — reaped, unreliable (control-C / job-object kill); (c) `run_in_background` (Bash tool) — survives across TURNS but **dies on session teardown** with its children; (d) **Windows Scheduled Task (`schtasks /create ... /sc once /st <t> /f` then `schtasks /run`)** — process is parented to the Task Scheduler service, NOT Claude's job object, so it **survives session teardown**; this is the teardown-proof rung. Monitors themselves are only rung (c): they die with the session, so they are live-convenience only — never the sole guarantee. For a job that MUST finish regardless of the app being open, launch the compute via a scheduled task and have it write a completion marker + result to disk; then a later session just reads the files. Add a **freshness guard** (only run the downstream combine/merge if the recomputed point wrote a fresh output) so a crash can't bake a stale/partial result into the final artifact. See [[feedback-verify-canonical-data-before-use]].
