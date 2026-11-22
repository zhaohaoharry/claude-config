---
name: project-travel-sync
description: "How the user sends edit requests on drafts: pasted sentences with comments in one prompt, or an annotated PDF they point to; the latest build goes to AI_share/Working Drafts"
metadata:
  type: project
---

Drafting workflow the user settled on after trying in-editor PDF annotation on 2026-11-22. They found the PDF Markup extension awkward, because typed text does not wrap, and asked to go back to Office Viewer as the VS Code PDF viewer.

1. **In-chat batches (the main route).** The user pastes several sentences from the draft, each followed by what to do with it, in one prompt. Locate each sentence in `latex/manuscript.tex` by its words, make all the edits in one pass, then compile once.
2. **Annotated PDF (when away from this computer).** The user annotates a PDF in any PDF program and either sends it or says where it is. Run `python program/python/read_pdf_notes.py "<path>"`. It lists each note with its page, section, marked text and context. Make all the edits in one pass.
- After every compile, run `python program/python/sync_travel.py`. It copies the build to `D:\Dropbox\AI\AI_share\Working Drafts\Online_Healthcare_manuscript.pdf`, one copy under a fixed name, replaced each time. The user wants no dated copies and no archives. The script will not replace a copy that carries annotations unless `--force` is given, which is used once the notes have been handled.
