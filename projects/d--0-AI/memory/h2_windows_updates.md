---
name: h2-windows-updates
description: "H2's Windows Update and automatic reboot are deliberately disabled (2026-10-16) because it is a compute-only machine; how it was done and how to undo it"
metadata:
  node_type: memory
  type: project
---

**H2 (`LAPTOP-BIS2QGG1`) has Windows Update and automatic reboots switched off on purpose, since 2026-10-16.** The user's reason: "I dont need its windows to keep updated. it is just for computting. its an old computer I will not use it for other purposes." Do not re-enable any of it without asking.

Why it came up: H2 had been asleep from 2026-06-15 to 2026-10-15, so it was working through four months of updates and rebooted itself three times in two days, once at 01:35 — **inside** its own active hours, because updates flagged "Service Pack (Planned)" override them. Active hours are therefore not a setting a long run can be planned around.

H2 is **Windows 10 Home** (EditionID `Core`), so the `WindowsUpdate\AU` Group Policy keys are silently ignored. What actually worked: `wuauserv`, `UsoSvc` and `WaaSMedicSvc` all set to Start 4 (Disabled — `WaaSMedicSvc` exists to re-enable the others and must be set in the registry, and the change only takes effect at the next boot), `UxOption=1`, and every `\Microsoft\Windows\UpdateOrchestrator\` task disabled. Several of those tasks are SYSTEM-owned and refuse `Disable-ScheduledTask` even elevated; they were disabled through a one-off SYSTEM-context scheduled task that was deleted afterwards.

**Two things that are easy to get wrong here.** First, a lock-down applied over a staged update leaves a cumulative update half-applied indefinitely, so the sequence was: set `wuauserv` to Manual, reboot deliberately with nothing running, let the servicing stack finish, then set it to Disabled. Boot-time installation runs through TrustedInstaller rather than Windows Update, but with a four-month backlog that is not worth betting on. Second, `Reboot_AC` and `Reboot_Battery` were still armed for 10:55 that same morning after the services were disabled — freezing H2 without the reboot would have been bitten within the hour.

Defender is deliberately left on and still updates out of band (`MpCmdRun.exe -SignatureUpdate` works with `wuauserv` disabled), because an unpatched networked machine with stale antivirus definitions is a different risk from an unpatched one. Residual exposure the user has accepted: Windows 10 22H2 on ESU, no OS patches, and no protection against power loss or a manual restart.

**Undo:** `C:\Users\Hao Zhao\Documents\H2_update_lockdown\undo.ps1` (run elevated, then reboot), with the full before/after in `lockdown_log.txt` beside it.

H2 is good for long compute runs at **3 workers** (4 physical cores, 8.4 s per self-test unit). See [[scalable_computing_2026_10]] and [[machine_names]].
