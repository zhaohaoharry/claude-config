---
name: feedback-focused-scope-not-cascade
description: "When asked to change/restructure a specific step or part, make only that focused change; do NOT cascade the edit through downstream consumers unless asked — the user drives the rest themselves"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
---

When the user asks to restructure or change a specific piece of the pipeline (e.g. "update D11 and D12", "fix this step", "after D11 generate the plot data"), implement ONLY that focused change and leave downstream consumers untouched unless they explicitly ask. The user frequently says "I will change the rest later" and prefers to control the sequence of changes himself.

**Why:** he keeps a tight mental model of the pipeline and wants to drive the cascade in his own order. Over-scoping (auto-repointing A5/A10/the estimator/exhibits, deleting now-redundant files that still have live consumers) creates churn he didn't ask for and risks touching validated code. He interrupted a full-restructure attempt with exactly this correction.

**How to apply:** do the requested part; for anything downstream that would need to change, NAME it and leave it for him (mark redundant-but-still-consumed files "transitional" rather than deleting them). Confirm the design when he asks "what do you think?" before implementing. Links [[feedback_workspace_program_sandbox_discipline]], [[ownership_analysis_dropped]].
