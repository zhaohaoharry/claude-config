---
name: sandbox/ is a subfolder of program/
description: Experimental/draft code goes in program/sandbox/, not a top-level sandbox/ folder
type: feedback
---

`sandbox/` must be a subfolder of `program/`, not a sibling at the project root.

**Why:** The `program/` folder contains all programs. `sandbox/` holds experimental code before it's promoted to production. Keeping it under `program/` reflects this hierarchy.

**How to apply:** When setting up a research project, create `program/sandbox/`. Place draft or untested do-files there. Production-ready code lives directly in `program/`.
