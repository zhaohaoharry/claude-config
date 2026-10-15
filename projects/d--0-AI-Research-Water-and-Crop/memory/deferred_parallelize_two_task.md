---
name: Parallelize B4_two_task_counterfactuals before next re-run
description: User-flagged: implement multiprocessing.Pool over the 8 non-reference cells in B4_two_task_counterfactuals.py BEFORE the next time we re-run the simulator. Defers a ~25min sequential run to ~5min parallel. User said "do the edit before next time of rerun" on 2026-05-12.
type: feedback
originSessionId: b4754dda-83f6-4d1b-b643-a554a422873d
---
**Trigger:** Before any future re-run of `program/sandbox/B4_two_task_counterfactuals.py`, first implement parallelization.

**Why:** Each of the 8 non-reference cells (3 SW regimes × 3 GW regimes minus baseline_open) is independent after the reference cell runs. The bisections within tax/cap rows are sequential per cell but cells don't depend on each other. Wall time drops from ~25 min sequential to ~5 min parallel (limited by the slowest cell's bisection chain).

**How to apply:**

Refactor `main()` so:
1. Reference cell `baseline_open` runs serially first (sets up `inputs["baseline_SW_kt"]` and `base_pumping`).
2. The 8 remaining cells (3 open-access, 3 tax, 3 cap, minus baseline_open) get dispatched via `multiprocessing.Pool(processes=8).map`. Each pool worker takes a cell descriptor and returns the scen dict.
3. The pool worker function should be top-level (not nested in `main()`) so it's picklable.
4. After the pool returns, build the `scens` dict, run the summary loop, write outputs.

Sketch:
```python
from multiprocessing import Pool

def _run_cell_worker(args):
    label, allocator, kwargs = args
    return label, _run_one(label, allocator, **kwargs)

work_items = [
    ("autarky_open",    alloc_autarky,      {"gw_cap_k": gw_cap_open, "base_pumping": base_pumping, "inputs": inputs}),
    ("centralized_open", alloc_all_sw_pool, {"gw_cap_k": gw_cap_open, "base_pumping": base_pumping, "inputs": inputs}),
    # tax: each is a bisection; wrap calibrate_tax(...) into a single-call descriptor
    # cap: same
]
with Pool(processes=8) as pool:
    for label, scen in pool.imap_unordered(_run_cell_worker, work_items):
        scens[label] = scen
```

For the tax/cap bisections, the natural unit of work is the bisection itself (calls `_run_one` ~5-7 times sequentially internally). One worker = one row's calibration + one final run.

**Windows caveat.** On Windows, multiprocessing uses `spawn` (re-imports modules in each worker). The inputs dict will be re-loaded by each worker (~30s overhead). On Linux this would be `fork` with copy-on-write (no overhead). Net wall-time still much faster than sequential.

**Memory caveat.** Each worker holds its own copy of the CCP pickle (~few hundred MB depending on plot panel size). 8 workers × 300 MB = 2.4 GB peak RAM. Should fit on the dev machine (96GB-class) but worth flagging.

**Verification after the parallelized run.**
Numbers must be bit-identical to the sequential run on overlapping fields (no RNG, deterministic Bellman). Compare new vs backup JSON; max relative diff = 0.0 expected.

**Status:** Deferred. Implement at the start of the next session that needs to re-run B4_two_task_counterfactuals.py.
