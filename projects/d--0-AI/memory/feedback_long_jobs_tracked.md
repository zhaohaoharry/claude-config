---
name: feedback-long-jobs-tracked
description: "Launch long pipelines only as tracked background tasks, check processes via PowerShell command lines, serialize ETFP downstreams with run_locked.sh"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a92848a1-ac62-4dd2-9e7f-f902cdbb3c6e
  modified: 2026-11-04T06:59:32.552Z
---

Never start a long job with `&` inside a foreground Bash call, and never judge whether it is alive with Git Bash `ps aux | grep`: MSYS `ps` shows no command-line arguments, so the grep returns 0 for a job that is running. Use `run_in_background` (tracked, notified, stoppable), and check processes with PowerShell `Get-CimInstance Win32_Process` filtered on CommandLine. Never queue a job on a marker string in a log another copy can write; queue on process completion or a lock.

**Why:** 2026-11-04, ETFP: a `&` relaunch of run_tag_full.sh g7tw95f3bA was judged dead by `ps | grep` and relaunched; two copies overlapped, corrupted shared Stata logs, and their TAG_FULL_DONE line started the queued g7tw95f3bj5 downstream early. All three had to be killed and rerun (about 4 hours each).

**How to apply:** in ETFP run every downstream as `FIXLOG=229_trans_est.jsonl bash run_locked.sh run_tag_full.sh <tag> <job>` (program/sandbox/rebuild/run_locked.sh, a global lock, since the pipelines share logs in rebuild/). Never edit a shell script while bash is executing it (bash reads scripts incrementally). Related: [[scalable-computing-2026-10]].
