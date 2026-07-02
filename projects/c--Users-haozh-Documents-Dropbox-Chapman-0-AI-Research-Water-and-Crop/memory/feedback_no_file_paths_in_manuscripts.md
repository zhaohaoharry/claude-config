---
name: No file paths or implementation details in manuscripts
description: Never reference internal code file paths (program/sandbox/foo.py, data/clean/bar.csv) or implementation tooling in academic manuscript text. Applies across all research projects.
type: feedback
originSessionId: 78ced47c-e9ad-4b4d-84b1-a497ab260cb9
---
In any academic manuscript (research paper, working paper, revision, slide deck), never write sentences that point readers to internal code files, scripts, or pipeline artifacts. Examples to avoid:

- "The construction is documented in `program/sandbox/build_crop_cost_panel.py`."
- "See `data/clean/transfer_transactions_consolidated.csv` for the underlying transactions."
- "The replication script `B1d_step1p5_water_allocation.py` implements the algorithm."

These belong in the replication archive's README, not the manuscript. Acceptable alternatives:

- Cite a specific data source by name (USDA NASS, FRED series ID, Bulletin 132 Table B-18).
- Reference an appendix section or table label inside the manuscript ("Appendix B states the full algorithm").
- For replication, write "Replication code and data are available at [archive URL / DOI]" once at the end of the paper, not inline in the prose.

**Why:** Academic readers should be able to read the manuscript without ever seeing internal pipeline structure. File-path references look like notes to self that escaped into the final draft and signal that the methodology has not been distilled into prose. Reviewers and editors take this as a quality flag.

**How to apply:** Before any LaTeX edit that involves describing how a variable is constructed, ask whether the sentence would still make sense if the file system did not exist. If it would not, rewrite it as a description of the methodology and move file references to the replication archive. Applies across all research projects under `0.AI/Research/`.
