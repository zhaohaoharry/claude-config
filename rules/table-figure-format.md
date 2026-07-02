# Table and Figure Caption Format — AER/RES Style

Universal rule for **all** research projects under `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Research\`.

## Tables

- **Title (caption): ABOVE the tabular** — placed immediately after `\begin{table}` and before the `\begin{tabular}` block.
- **Notes: BELOW the tabular** — placed after `\end{tabular}` and before `\end{table}`, on a separate line, in a smaller font.

Standard LaTeX skeleton:

```latex
\begin{table}[!htbp]
\centering
\caption{Short descriptive title.}
\label{tab:short_label}
\begin{tabular}{...}
... rows ...
\end{tabular}
\par\smallskip
\parbox{\linewidth}{\footnotesize\textit{Notes:} Full explanatory notes — what each column is, units, sample, standard-error conventions, significance stars, source. End with a period.}
\end{table}
```

The `\parbox{\linewidth}{...}` wrapper makes the Notes block **left-aligned and full-width**. A bare `{\footnotesize ...}` group inherits the table's `\centering` and renders the notes *centered* line-by-line, which is wrong; the parbox overrides it.

## Figures

- **Title (caption): BELOW the graphic** — placed after `\includegraphics{...}` and before `\end{figure}`.
- **Notes: BELOW the title, on a separate line** — placed after `\caption{...}` (or in a `\par\smallskip` block after the caption) in a smaller font.

Standard LaTeX skeleton:

```latex
\begin{figure}[!htbp]
\centering
\includegraphics[width=...]{figures/short_name.pdf}
\caption{Short descriptive title.}
\label{fig:short_label}
\par\smallskip
\parbox{\linewidth}{\footnotesize\textit{Notes:} Full explanatory notes — what each panel is, axis units, sample, source. End with a period.}
\end{figure}
```

## Rationale

This is the convention used by the American Economic Review (AER), the Review of Economic Studies (RES), and the Quarterly Journal of Economics. Reviewers expect this layout. Tables get the title up because tables are scanned column-by-column; figures get the title below because figures are scanned image-first.

## Migration for existing projects

When editing a manuscript that currently has captions in non-standard positions:
1. **For tables:** move `\caption{...}` and `\label{...}` to immediately after `\begin{table}\centering` and before `\begin{tabular}`. Any explanatory text that was *in the caption argument* moves to a `\par\smallskip {\footnotesize\textit{Notes:} ...}` block after `\end{tabular}`.
2. **For figures:** caption stays after the graphic; if it already contains explanatory text, split into a short title (in `\caption{}`) and a `\par\smallskip {\footnotesize\textit{Notes:} ...}` block after.
3. **Caption text discipline:** the `\caption{}` argument is a *short title only* — one sentence, ideally under 15 words. All explanatory material lives in the Notes block below.

## Implementation discipline

- Never use `\begin{table}` without a `\caption{}` and a `\label{tab:...}`.
- Never use `\begin{figure}` without a `\caption{}` and a `\label{fig:...}`.
- The Notes block is in `\footnotesize` (not `\small`, not full-size).
- Notes start with `\textit{Notes:}` (italicized "Notes:"), period after the colon contents.
- **Wrap the Notes block in `\parbox{\linewidth}{...}`** so it is left-aligned and full-width. Without the parbox, the notes inherit the table/figure `\centering` and come out centered, which looks wrong.
- Do not use `tablenotes` from threeparttable unless the project already loads that package; the plain `\par\smallskip` + `\parbox{\linewidth}{...}` pattern is portable across all journal templates.
