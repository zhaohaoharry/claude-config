---
name: feedback_cpp_priority_over_etfp
description: Carbon Pricing runs outrank ETFP on LaoZhao; pause ETFP there and never wait on memory or capacity because of it
metadata:
  node_type: memory
  type: feedback
  originSessionId: e0f69bb2-3049-48e5-8b02-442ca6dd3b02
  modified: 2026-11-07T02:54:52.195Z
---

Carbon Pricing Policy has priority over ETFP on LaoZhao. When both compete, ETFP waits (`sc.ps1 pause -Job <etfp job>` on LaoZhao, resume once the Carbon Pricing runs finish), and a Carbon Pricing queue must not sit idle waiting for memory or capacity that ETFP holds.

**Why:** user, 2026-11-07, after a memory gate threatened to hold the counterfactuals behind the ETFP job: "this project is of higher priority than etfp. please make sure laozhao wait for this one. and do not pause because of that reason again."

**How to apply:** do not write memory gates into Carbon Pricing queues. Pause, do not stop, so ETFP units are not lost. Say so when pausing, and resume ETFP when the Carbon Pricing jobs end. This narrows the earlier "do not touch ETFP processes" constraint for LaoZhao only; H2 and HMac ETFP runs are unaffected. See [[feedback_etfp_runs_to_hmac]] and [[feedback_long_jobs_tracked]].
