---
name: feedback-clean-keeps-green
description: "\"clean\"/\"clean up\" on tracked prose = drop red \\del/\\delx but KEEP green \\add wrappers; flatten green to black only on explicit \"final clean\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

When the user says "clean" or "clean up" on track-changed manuscript prose, drop the red `\del`/`\delx` content but **keep the green `\add{}` wrappers** so the additions stay green and visible. Do NOT flatten the green to plain black.

**Why:** The green stage lets the user review what was added before it is committed. Flattening prematurely removes the at-a-glance view of what changed. (Corrects an earlier reading in which plain "clean up" meant a full flatten to black.)

**How to apply:**
- "clean" / "clean up" → remove `\del`/`\delx`, keep `\add{}` (green stays).
- Flatten green → plain black ONLY when the user explicitly says "final clean" / "flatten the green" / similar.
- Applies to the track-change workflow in [[project-v1-tracked-working-draft]] and any project using the `\add`/`\del`/`\delx` marks.
