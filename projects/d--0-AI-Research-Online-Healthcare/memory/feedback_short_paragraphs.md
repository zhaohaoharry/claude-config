---
name: feedback-short-paragraphs
description: Split a long paragraph into short ones whenever it divides cleanly by key meaning
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2c90432b-2125-4d8b-8592-c76b411c6b5b
  modified: 2026-10-30T02:14:57.127Z
---

Avoid very long paragraphs. When a paragraph can be cleanly divided into shorter paragraphs that each carry one key meaning, divide it. In a data section, give each short paragraph its own run-in `\paragraph{}` head.

**Why:** On 2026-10-30 the user flagged the Data section's "Travel and province characteristics" paragraph, which ran to about 400 words, as too long. It covered three things: travel between provinces, the money cost of an admission and province characteristics.

**How to apply:** Before saving prose, check any paragraph that covers more than one topic and split it at the topic boundary. This does not license choppy one-fact sentences within a paragraph; see [[feedback-plain-register]].

**Exception, 2026-11-11:** in the Estimation and identification section the user asked for no `\paragraph{}` heads. Each paragraph there opens with a core sentence that carries the logic and the transition from the previous paragraph ("The first part identifies…", "The second set…", "Turning to…"). The run-in heads stay in the Data section. My reading: argument sections get topic sentences, catalogue sections get heads.
