---
name: feedback-cpp-guarded-build
description: "Carbon Pricing Policy — always rebuild the manuscript with program/python/build_manuscript_v3.sh, which stops on broken sentences or shifted numbers in the tracked copy"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-13T07:32:17.697Z
---

Carbon Pricing Policy: rebuild the manuscript and its review copies only with
`bash program/python/build_manuscript_v3.sh` (from the project root), never with the separate commands.

**Why:** on 2026-11-13 the user found sentences broken in the tracked copy (paragraph breaks left by deleted text,
a deleted display shown green, an empty footnote mark, subsections numbered 5.0) and said "make sure that problem never
appear again". The script runs `check_tracked_text.py`, which requires the tracked copy with every change accepted to
read paragraph by paragraph like manuscript_v3.tex, and `--numbers`, which requires every section, equation, table and
figure number to match. The build stops on any difference.

**How to apply:** if the build stops, fix the cause in `build_review_v3.py` or `round_marks.py` (the marking), not in
the manuscript text, and rerun until it passes before copying to AI_share. See [[feedback-cpp-test-on-1000-first]].
