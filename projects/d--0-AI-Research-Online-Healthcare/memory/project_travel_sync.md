---
name: project-travel-sync
description: Online Healthcare draft PDF is copied to AI_share for reading on the phone; rerun sync_travel.py after every compile
metadata:
  type: project
---

On 2026-11-11 the user asked to "keep the working draft sync so i can work remotely" and then clarified: "For sharing i mean aishare where i used on my phone not share to other computers". So sharing means the compiled PDF in AI_share, not a Dropbox travel copy for another computer (one was built by mistake and removed).

`program/python/sync_travel.py` copies `latex/manuscript.pdf` to `D:\AI_share\Online_Healthcare_manuscript.pdf` and `D:\Dropbox\AI\AI_share\Online_Healthcare_manuscript.pdf` under a fixed name. Both folders exist; other sessions used `D:\AI_share` on 2026-11-11 and earlier Online Healthcare PDFs (dated names, to 2026-10-30) are in the Dropbox one. Which one the phone reads was not confirmed (my uncertainty).

**How to apply:** run the script after each compile of the manuscript. PDF only; no sources or data go there.
