"""Sample-flow ledger, coverage cards and sentinel scan for pandas pipelines.

Implements rules 1-4 of ~/.claude/rules/data-integrity.md. Copy this file into a project's
program/ folder (or import it by path) and call it at every step that can lose rows.

    from sample_flow import Ledger, coverage_card, sentinel_scan
    led = Ledger("log/sample_flow.csv", unit="firm_id")
    df = led.start(df, "load raw")
    df = led.step(df, df.dropna(subset=["sales"]), "drop missing sales")
    df = led.merge(df, prices, on="year", how="left", validate="m:1", name="merge prices")
    coverage_card(df, ["sales", "tfp"], by=["year"]).to_csv("log/coverage.csv")

Each call appends a ledger line and raises StopThreshold when a step loses more than
`max_drop_share` of its input (default 5%) unless `approved=True` is passed with a reason the user
has accepted.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

SENTINELS = [9, 99, 999, 9999, 999996, 999997, 999998, 999999, -1, -8, -9, -99]


class StopThreshold(RuntimeError):
    """A step exceeded the data-integrity stop threshold."""


class Ledger:
    def __init__(self, path, unit=None, max_drop_share=0.05, max_unmatched_share=0.05):
        self.path = Path(path)
        self.unit = unit
        self.max_drop = max_drop_share
        self.max_unmatched = max_unmatched_share
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", newline="\n", encoding="utf-8") as f:
            csv.writer(f).writerow(
                ["step", "rows_in", "rows_out", "units_out", "dropped", "drop_share", "reason"])

    def _units(self, df):
        if self.unit and self.unit in df.columns:
            return int(df[self.unit].nunique())
        return ""

    def _write(self, name, rows_in, df_out, reason, stopped=False):
        rows_out = len(df_out)
        dropped = rows_in - rows_out
        share = dropped / rows_in if rows_in else 0.0
        if stopped:
            reason = "STOPPED (not applied): " + reason
        with self.path.open("a", newline="\n", encoding="utf-8") as f:
            csv.writer(f).writerow(
                [name, rows_in, rows_out, self._units(df_out), dropped, f"{share:.4f}", reason])
        return share

    def start(self, df, name="load"):
        self._write(name, len(df), df, "initial load")
        return df

    def step(self, df_in, df_out, name, reason="", approved=False):
        share = (len(df_in) - len(df_out)) / len(df_in) if len(df_in) else 0.0
        stop = share > self.max_drop and not approved
        self._write(name, len(df_in), df_out, reason or name, stopped=stop)
        if stop:
            raise StopThreshold(
                f"[data-integrity] step '{name}' dropped {share:.1%} of {len(df_in)} rows "
                f"(threshold {self.max_drop:.0%}). Report to the user before continuing.")
        return df_out

    def merge(self, left, right, name, how, validate, approved=False, **kw):
        """Merge with explicit `how` and `validate`; logs unmatched master rows."""
        # Merge outer once so unmatched rows on both sides can be counted, then keep per `how`.
        m = left.merge(right, how="outer", validate=validate, indicator=True, **kw)
        n_left = len(left)
        left_only = int((m["_merge"] == "left_only").sum())
        right_only = int((m["_merge"] == "right_only").sum())
        keep = {"left": ["both", "left_only"], "inner": ["both"],
                "right": ["both", "right_only"], "outer": ["both", "left_only", "right_only"]}[how]
        out = m[m["_merge"].isin(keep)].drop(columns="_merge")
        unmatched_share = left_only / n_left if n_left else 0.0
        too_many = unmatched_share > self.max_unmatched and not approved
        inner_loss = how == "inner" and left_only > 0 and not approved
        self._write(name, n_left, out,
                    f"how={how}; master unmatched={left_only}; using unmatched={right_only}",
                    stopped=too_many or inner_loss)
        if too_many:
            raise StopThreshold(
                f"[data-integrity] merge '{name}': {unmatched_share:.1%} of master rows unmatched "
                f"(threshold {self.max_unmatched:.0%}). Report to the user before continuing.")
        if inner_loss:
            raise StopThreshold(
                f"[data-integrity] merge '{name}' is inner and drops {left_only} master rows.")
        return out


def coverage_card(df, cols, by=None, min_share=0.80):
    """Non-missing count/share, distinct values and range for each column (optionally by group).

    Adds a `flag` column: 'LOW_COVERAGE' below `min_share`, 'CONSTANT' with one distinct value.
    """
    rows = []
    groups = [((), df)] if not by else df.groupby(by, dropna=False)
    for key, g in groups:
        key = key if isinstance(key, tuple) else (key,)
        for c in cols:
            s = g[c]
            nn = int(s.notna().sum())
            share = nn / len(g) if len(g) else 0.0
            nuniq = int(s.nunique(dropna=True))
            num = pd.api.types.is_numeric_dtype(s)
            flag = ";".join(f for f, on in (("LOW_COVERAGE", share < min_share),
                                             ("CONSTANT", nuniq <= 1)) if on)
            row = dict(zip(by or [], key))
            row.update(variable=c, n=len(g), nonmissing=nn, share=round(share, 4),
                       distinct=nuniq, min=s.min() if num and nn else None,
                       max=s.max() if num and nn else None, flag=flag)
            rows.append(row)
    return pd.DataFrame(rows)


def sentinel_scan(df, cols=None, sentinels=SENTINELS, top_heap_share=0.02):
    """Count candidate missing-value codes and heaping at the maximum in numeric columns."""
    cols = cols or [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    rows = []
    for c in cols:
        s = df[c].dropna()
        if s.empty:
            continue
        lo, hi = s.quantile(0.01), s.quantile(0.99)
        for v in sentinels:
            k = int((s == v).sum())
            # A code counts only where it sits at the edge of the distribution, not inside it.
            if k and (v == s.max() or v == s.min() or v > hi or v < lo):
                rows.append(dict(variable=c, value=v, count=k, kind="sentinel_candidate"))
        top = s.max()
        k = int((s == top).sum())
        if len(s) and k / len(s) >= top_heap_share and s.nunique() > 10:
            rows.append(dict(variable=c, value=top, count=k, kind="heaping_at_max"))
    return pd.DataFrame(rows, columns=["variable", "value", "count", "kind"])
