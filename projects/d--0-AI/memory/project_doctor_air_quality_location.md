---
name: project-doctor-air-quality-location
description: "The Haodf doctor-preference / SMM offline-choice project is named \"Online Healthcare\" and lives at D:\\0.AI\\Research\\Online Healthcare (formerly Dropbox \"Air Quality on Doctor Behavior\"); Python pipeline"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e8d7e67-cb4d-47e2-8455-bc143574e324
  modified: 2026-10-20T06:20:49.219Z
---

The project that estimates doctor preference from online Haodf data and simulates offline hospital choice by SMM is named **Online Healthcare**. Its folder is `D:\0.AI\Research\Online Healthcare`, and all future work happens there (user, 2026-10-20). It used to be `D:\Dropbox\Air Quality on Doctor Behavior`. On 2026-10-20 it was ported from Stata/MATLAB to Python (`program/python/run_all.py`); the originals are kept read-only in `program/stata_legacy` and `program/matlab_legacy`. `main.pdf` in the project root is Yinan Liu's draft "The Value of Online Healthcare Access".

Only code and writings were copied, never generated data, because the user regenerates it. Raw inputs are read in place from the central repository: `7. Health & Medical\Haodf Consultations (2020)`, `Hunan Hospital Patient Records (2020-01)`, `China Healthcare Security Statistical Yearbook (2021-2023)` and `13. Transport & Infrastructure\Transportation Networks of China (1994-2017)`.

**Why:** the user wants the project local, out of Dropbox, under its real name, and in Python for speed.

**How to apply:** work in `D:\0.AI\Research\Online Healthcare`, not in Dropbox. The open modelling decisions are in the project's HANDOFF.json `issues`. The Dropbox copy has not been deleted yet: sync is paused and about 200 online-only files are pending (`quality_reports/migration_manifest.json`). The user authorized deleting it once those are fetched. This is an exception to [[feedback-dropbox-shared-folders]].
