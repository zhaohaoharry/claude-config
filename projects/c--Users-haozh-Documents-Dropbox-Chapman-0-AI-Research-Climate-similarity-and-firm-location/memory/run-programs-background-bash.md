---
name: run-programs-background-bash
description: "Launch long-running programs in the background via the Bash tool (run_in_background), NOT PowerShell — PowerShell pops up a console window the user dislikes"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 50884341-1a39-409e-91a0-02b4e86a8c41
---

The user wants long-running programs (Stata estimations, data downloads, Python builds) launched in the background via the **Bash tool** with `run_in_background: true` — **NOT PowerShell**.

**Why:** PowerShell `Start-Process` (even `-NoNewWindow`) pops up / flashes a console window in the user's view, which they dislike (2026-06-08). This **supersedes** the earlier "run in the background using PowerShell" preference — the user changed their mind specifically because the window popped up. Bash `curl`/`python` (and Stata batch) run without a visible window.

**How to apply:**
- Use the **Bash** tool with `run_in_background: true` for any run > ~30s (downloads, Python builds, Stata batch `-e`).
- Short checks/reads stay foreground (Bash or the dedicated tools).
- Still **ONE heavy job at a time** — heavy concurrent jobs contend for memory and crash Stata. See [[no-redundant-work]].

**Stata via Bash — two gotchas (learned 2026-06-08):**
1. Launch through a tiny **wrapper `.sh`** (`cd` to `program/sandbox`; `exec "/c/Program Files/Stata18/StataMP-64.exe" -e do x.do`), not a `cd ... && "quoted exe path"` one-liner — the compound form returns **exit 127** in background mode. Bash *can* exec Stata (a trivial foreground `-e do` works, RC 0).
2. Stata is a **GUI app**, so it DETACHES from the Bash launcher: the harness mis-reports the background command as **failed/127 and never sends a real completion notification**, even though Stata keeps running and writing its `.log`. Mitigation: after launching, confirm Stata is alive + the `.log` is growing, then start a separate Bash background **watcher loop** that polls the `.log` for the do-file's final `DONE` marker (and `^r([0-9]+);` errors), using `ps -W | grep StataMP-64` for liveness. Do NOT use `tasklist` in the watcher — it is **not on PATH** in the background Bash shell and gives false "exited" signals. Put an intermediate marker after the first/key spec so the watcher can break early on the headline before slow later specs.

**ppmlhdfe gotcha (learned 2026-06-12, this project):** `ppmlhdfe`'s IRLS reproducibly **STALLS before iteration 1 whenever a COUNTRY fixed effect is in `absorb()`** (e.g. `absorb(decision_id supplier_country)` or `absorb(decision_id country_pair)` froze 12+ min at the post-singleton point across 6 launches), while `decision_id`-only and `decision_id + city×ind×year` converge fine in minutes. It is **not** memory, row count, or collinearity — it is ppmlhdfe-specific to the country-FE configuration. **FIX: run that FE-robustness rung in `reghdfe` (LPM, no IRLS) — converges in ~7 iterations**; report the LPM sign/significance/relative-magnitude (LPM levels aren't logit-comparable). Also: a customer-country×supplier-country pair FE is near-collinear with `decision_id` (which already pins the customer country) → since `decision_id` absorbs the customer side, use the **supplier-country FE alone**. A full-sample logit spec absorbing `decision_id + city×ind×year` on the ~15M-row estimating sample takes ~30–50 min; budget for it. To beat 33.8M-row memory thrash, load only the regression columns (`use <varlist> using file`) and/or subsample DECISIONS (one `runiform()` draw per `decision_id` via tag + `egen max(),by()`; do NOT use `egen min(_u),by(decision_id)` over all rows — the min of ~90 draws is ~always below the threshold so it keeps ~everything).
