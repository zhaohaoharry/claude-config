---
name: machine-names
description: "The user's three computers are named LaoZhao (main), H2 and HMac (assistants) — hostnames differ from these names"
metadata:
  node_type: memory
  type: user
  originSessionId: 0a73e471-ad5d-46a8-9221-27dd2d33c900
  modified: 2026-10-15T09:05:40.052Z
---

The user named their three computers on 2026-10-15, and these names are what they use in conversation:

- **LaoZhao** — hostname `LAOZHAO`. The main machine: work happens here and it coordinates every compute job. i7-12700H, 14 physical cores, 32 GB.
- **H2** — hostname `LAPTOP-BIS2QGG1`, Windows profile `C:\Users\Hao Zhao`. An assistant that takes a share of compute jobs. 4 physical cores.
- **HMac** — MacBook Air M3, hostname `Haos-Laptop-266.local`, ComputerName "Hao's Laptop". An assistant for writing and reading only: the ScalableComputing tools are Windows-only, and it is fanless so it throttles under sustained load.

The Windows computer names were deliberately not renamed, so `%COMPUTERNAME%` and `machine_card.ps1` keep reporting the hostnames — map them to the friendly names when reporting to the user. The full register with hardware, Dropbox roots and Python versions is `D:\Dropbox\AI\MACHINES.md`.

See [[scalable_computing_2026_10]] for the compute framework and [[feedback_dropbox_shared_folders]] for what must not be touched in Dropbox.
