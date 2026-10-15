---
name: stata-per-machine
description: Stata is only usable on LaoZhao for real work; H2 has Stata 13.1 with no HDFE packages and an institutional licence not in the user's name
metadata:
  type: project
---

Checked 2026-10-15.

- **LaoZhao**: StataMP 18, `C:\Program Files\Stata18\StataMP-64.exe`. All Stata analysis runs here.
- **H2**: Stata/MP 13.1 (2014), `D:\Stata\Stata13\StataMP-64.exe`, unpacked from a zip and not on PATH. Batch mode works (`-e do file.do`, log written to the working directory). `reghdfe`, `ppmlhdfe`, `ivreghdfe` and `ftools` are all absent (PLUS points at a non-existent `c:\ado\plus\`), and the licence is a **3-user 8-core network perpetual licence, institutional, not in the user's name**. Do not plan or distribute Stata work on H2 until the user confirms entitlement — and the question is open as of this writing.
- **HMac**: unchecked.

**Consequence:** the distributed compute layer is Python, which needs no licence seat and runs everywhere. Stata stays on LaoZhao for coauthor do-files and journal-facing work. See [[machine_names]] and [[scalable_computing_2026_10]].
