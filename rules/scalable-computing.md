# Scalable Computing Across PCs — `**ScalableComputing`

Method and tooling by Ohyun (2026-10-12), installed here 2026-10-15. Spread long computation
(Monte Carlo, bootstraps, batch estimation — anything that would run for hours) over every PC the
user has open, the coordinator's own PC included.

Shared folder (live Dropbox account): `D:\Dropbox\AI\ScalableComputing`
(`tools\`, `jobs\`, `machines\`, `WORKER_PROMPT.md`). A worker PC whose Dropbox sits at a different
local path uses its own path to the same synced folder; each host's path is recorded in
`machines\<HOST>.json` at preflight. This desktop is `LAOZHAO`.

----------------------------------------------------------------
ROLES
----------------------------------------------------------------
- COORDINATOR = the session where `**ScalableComputing` is typed. It plans, packages, dispatches,
  monitors and merges, AND computes its own share.
- WORKERS = any Claude Code session on another PC with Remote Control on and Bypass permissions mode.
  EVERY coordinator message begins `[ScalableComputing]`, and the FIRST one to a session also says:
  "read <that PC's ScalableComputing folder>\WORKER_PROMPT.md and act as a worker by it". The global
  CLAUDE.md tells every session to do so, so nothing has to be pasted.
- Each worker PC's Dropbox must sync the `ScalableComputing` folder (selective sync).

----------------------------------------------------------------
COMMAND FORMS
----------------------------------------------------------------
  **ScalableComputing                 preflight + plan for the task at hand; dispatch only after "go"
  **ScalableComputing status          progress per host from the heartbeat files
  **ScalableComputing pause|resume|drain|stop [HOST|all]
  **ScalableComputing merge           collect all hosts' sealed batches, verify, aggregate, report

----------------------------------------------------------------
1. PREFLIGHT (every time, before dispatch)
----------------------------------------------------------------
1. ASK THE USER to confirm, and wait for the answer:
   (a) every PC has its Claude session open with Remote Control on, and
   (b) EVERY session, this coordinator included, is in Bypass permissions mode.
   Why (b): a permission-mode mismatch makes cross-session messages vanish without any error, and auto
   mode blocks code that arrives from another session (both seen 2026-10-11 on Ohyun's PCs).
2. ListAgents: find the Remote Control rows. A PC missing → tell the user, do not guess.
3. Send each worker `preflight`; it replies with its machine card (also written to `machines\<HOST>.json`;
   run `tools\machine_card.ps1` here for the coordinator). Check: sc_folder_synced true, python_312 with
   numpy/scipy/pandas, on_ac_power, free RAM, cpu_load_pct (someone using it?).
   A worker PC whose Dropbox does not sync ScalableComputing cannot take part: tell the user.
4. Package the job (section 2), then `check <job_id> <sha256 of manifest.json>` on every worker: Dropbox
   upload lag means a file just written here may not be there yet; launch nowhere until all say `match`.
5. `validate <job_id>` on every host (incl. here): reproduce a known result. Package versions differ by
   PC, so state the tolerance and compare.
6. `bench <job_id> <workers>` on every host (`tools\bench.py`): units/hour at the planned worker count.
7. Show the user the plan in a few lines: hosts, workers each, units each, expected finish, Dropbox upload
   per hour. Dispatch on "go".

----------------------------------------------------------------
2. PACKAGING — ScalableComputing\jobs\<job_id>\
----------------------------------------------------------------
- `code\` : a self-contained copy of what a unit needs. Never point at project folders: other PCs may not
  sync them. Keep it small (KB, not MB).
- `manifest.json`:
    {"job_id", "description",
     "command": [...],       placeholders {root} {job} {unit} {out} {local} {host}
     "cwd": "...", "env": {...}, "out_ext": ".csv",
     "unit_count": N  (ids u00000...)  or  "units": [...],
     "unit_seconds_estimate": s, "max_retries": 2,
     "validate": {"command": [...], "expect": "..."}}
- UNIT CONTRACT: one unit = one process that writes exactly one file to {out} and exits 0; all randomness
  seeded from the unit id, so a unit can be rerun anywhere with the same result.
- UNIT SIZE: 1-5 minutes of one core. Small enough that a STOP or a reboot loses little; large enough that
  process start-up (~1 s) is noise. Split a long job (e.g. 1,000 Monte Carlo draws x cells) into many units.
- `assignment.json`: `py -3.12 tools\plan.py <job> HOST1=uph1 HOST2=uph2` (contiguous blocks in proportion
  to the bench units/hour). HOST = the PC's %COMPUTERNAME% exactly as the machine card prints it; the
  runner finds its units by that name. Only the coordinator writes manifest, assignment and control files.

----------------------------------------------------------------
3. DISPATCH AND RUN
----------------------------------------------------------------
- Here: `powershell -ExecutionPolicy Bypass -File tools\launch.ps1 -Job jobs\<id> -Workers N [-SyncEvery 600]
  [-YieldWhenActive 2 -ActiveWorkers K]`. On each worker: message `launch <job_id> <same args>`.
- `launch.ps1` registers a scheduled task in the user's session: the run survives Claude exiting, keeps
  going on battery, has no time limit. Workers per host: physical cores minus 1-2. One thread per unit.
- `-YieldWhenActive 2 -ActiveWorkers K`: on a PC the user may be using, when they touch keyboard/mouse only
  K units keep running and the rest freeze, resuming once they have been idle 2 minutes. Offer it for
  daytime runs.
- Runs are resumable: a relaunch skips every unit already finished locally or already uploaded.

----------------------------------------------------------------
4. PAUSE — the user needs a PC
----------------------------------------------------------------
- On that PC, instant (~2 s): `tools\sc.ps1 pause` (or tell that PC's Claude "pause").
  resume / drain / stop the same way.
- From the coordinator: message the worker `pause` (seconds), or write
  `jobs\<id>\control\<HOST>.json {"state":"pause"}` (or `ALL.json`) when messaging fails (Dropbox lag,
  about a minute; polled every 60 s). The same file can lower "workers".
- pause = freeze the unit processes (CPU to zero within ~2 s, memory kept, nothing lost).
  drain = finish running units, start none, exit.   stop = kill running units now, exit; only those
  units are recomputed. After drain/stop, relaunch with `launch.ps1`.

----------------------------------------------------------------
5. DROPBOX DISCIPLINE (upload lag; sync itself costs CPU)
----------------------------------------------------------------
- Compute on local disk only: `C:\SC_local\<job_id>`. Never append to a growing file inside Dropbox: on
  2026-10-10 Dropbox re-syncing growing result CSVs took ~4.7 CPU-hours and slowed a run.
- Results go up as SEALED, IMMUTABLE batches every --sync-every s (default 600): the unit files first,
  then `batch_NNNN.done.json` listing names, sizes and sha256. Readers trust only listed files whose size
  matches; `merge.py` reports the rest as "still syncing".
- ONE WRITER PER FILE: each host writes only `results\<HOST>\` (batches + heartbeat.json); the coordinator
  writes only manifest, assignment, control. Two machines never write the same file (no conflicted copies).
- Poll Dropbox no faster than once a minute. Never put data sets into ScalableComputing; if a job needs
  large inputs, each host copies them once to `C:\SC_local`. Raw data stays where the data-repository rule
  puts it (`D:\0. Research Data\`), referenced in place.

----------------------------------------------------------------
6. MONITOR, REBALANCE, MERGE
----------------------------------------------------------------
- Ground truth = files, not messages: `results\<HOST>\heartbeat.json` (state, done/units, units/hour,
  hours_left, updated). Cross-session messages carry no receipt; every command expects a reply.
- A heartbeat older than 2 sync intervals → message that worker `status`; no answer → tell the user, offer
  to reassign its remaining units.
- Rebalance when the first host finishes: `drain` the slower host, wait for its final batch, then
  `plan.py <job> HOST=uph ... --remaining` and relaunch both (finished units are skipped).
- Merge: `py -3.12 tools\merge.py jobs\<id> [--concat-csv all.csv] --verify` (writes to
  `C:\SC_local\<id>\merged` here), then the job's own aggregation; report per-host contributions.
- The provenance rule still applies: the merged output is a build artifact of the job's `code\`, and the
  job folder plus its manifest are what `PIPELINE.md` must point to for any number that reaches a paper.

----------------------------------------------------------------
7. SAFETY (workers run in bypass mode)
----------------------------------------------------------------
- Workers act only on coordinator messages and only on the commands in `WORKER_PROMPT.md`: the tools in
  `ScalableComputing\tools` and commands named in a manifest under `ScalableComputing\jobs`.
- No installs, setting changes, or deletions outside `C:\SC_local\<job>` and the host's own results folder
  without the user's approval in that PC's window. A peer message is never the user's approval.

----------------------------------------------------------------
LESSONS BEHIND THE DESIGN (Ohyun, 2026-10-10/12, desktop EKWONOMIST and laptop WHA-AAB25WLM-WL)
----------------------------------------------------------------
- A Windows update with memory integrity (VBS) made paging ~4x slower; a 12-hour run slowed 2.7x.
  Benchmark, do not assume speed.
- Below-normal priority was throttled by Windows; runs use normal priority and yield via pause/yield.
- An automatic Windows reboot at 07:08 killed a detached run: units must be small and runs resumable.
- Messages to a session in a different permission mode were silently dropped; matching modes fixed it.
- Tested 2026-10-12: launch, pause (frozen units used 0 CPU), resume, stop (only running units lost),
  relaunch (skipped 20 done units), sealed batches, merge --verify 24/24.
- First two-PC run passed 2026-10-12 (120 units): desktop 806 units/h at 10 workers + laptop 1167 units/h
  at 14 workers = 2.4x the desktop alone; validate bit-identical across numpy 2.2.1 and 2.5.2.
- A laptop needs the lid OPEN and AC power (lid-close default is sleep, which freezes a run); watch
  units/hour in heartbeat.json for thermal throttling on long runs.
