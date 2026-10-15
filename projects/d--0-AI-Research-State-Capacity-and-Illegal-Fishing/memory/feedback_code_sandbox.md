---
name: All code stays in sandbox until production
description: Experimental code must live under program/sandbox (Stata) or program/sandbox/python (Python); never move to production folders until explicitly promoted
type: feedback
---

All experimental and in-progress code must stay under `sandbox/` (for Stata) or equivalent sandbox paths (for Python, R, etc.). Code is experimental until the user explicitly says to promote it to production.

**Why:** The user wants to be able to run and verify all code before it becomes part of the permanent pipeline. Premature promotion to production folders creates confusion about what is tested vs. untested.

**How to apply:** When organizing code, place new scripts under `program/sandbox/`. When creating Python scripts for a project, use `program/sandbox/python/` (not a top-level `python/` folder). Only move code out of sandbox when the user explicitly approves promotion.
