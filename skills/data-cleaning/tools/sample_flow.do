* sample_flow.do -- sample-flow ledger and coverage cards for Stata pipelines
* Implements rules 1-4 of ~/.claude/rules/data-integrity.md.
* Usage (after `do sample_flow.do` once per session):
*   sf_init using "log/sample_flow.csv", unit(firm_id)
*   sf_mark                                   // remember N before a step
*   drop if missing(sales)
*   sf_step "drop missing sales"              // writes a ledger line; error 9 if >5% dropped
*   sf_step "keep manufacturing", approved    // approved = the user accepted this drop
*   sf_merge "merge prices"                   // after merge ..., gen(_merge): logs unmatched master rows
*   sf_cover sales tfp, by(year) min(0.8)     // coverage card to log/coverage_<var>.csv

capture program drop sf_init sf_mark sf_step sf_merge sf_cover

program define sf_init
    syntax using/, [UNIT(name) MAXdrop(real 0.05)]
    global SF_FILE "`using'"
    global SF_UNIT "`unit'"
    global SF_MAX = `maxdrop'
    tempname fh
    file open `fh' using "`using'", write replace text
    file write `fh' "step,rows_in,rows_out,units_out,dropped,drop_share,reason" _n
    file close `fh'
    global SF_N = _N
    sf_write "load" `=_N' "initial load"
end

program define sf_mark
    global SF_N = _N
end

program define sf_units, rclass
    return scalar u = .
    if "$SF_UNIT" != "" {
        tempvar tag
        quietly egen `tag' = tag($SF_UNIT)
        quietly count if `tag'
        return scalar u = r(N)
    }
end

program define sf_write
    args step rows_in reason
    sf_units
    local u = r(u)
    local dropped = `rows_in' - _N
    local share = cond(`rows_in' > 0, `dropped' / `rows_in', 0)
    tempname fh
    file open `fh' using "$SF_FILE", write append text
    file write `fh' `""`step'","' (`rows_in') "," (_N) "," (`u') "," (`dropped') "," %6.4f (`share') `","`reason'""' _n
    file close `fh'
end

program define sf_step
    syntax anything(name=step), [APProved REAson(string)]
    local step `step'
    local rows_in = $SF_N
    local share = cond(`rows_in' > 0, (`rows_in' - _N) / `rows_in', 0)
    if "`reason'" == "" local reason "`step'"
    if `share' > $SF_MAX & "`approved'" == "" {
        sf_write "`step'" `rows_in' "STOPPED (applied; script halted): `reason'"
        global SF_N = _N
        di as err "[data-integrity] step `step' dropped " %4.1f (100*`share') "% of `rows_in' rows (threshold " %3.0f (100*$SF_MAX) "%). Report to the user before continuing."
        error 9
    }
    sf_write "`step'" `rows_in' "`reason'"
    global SF_N = _N
end

program define sf_merge
    syntax anything(name=step), [APProved]
    local step `step'
    capture confirm variable _merge
    if _rc {
        di as err "[data-integrity] sf_merge needs the _merge variable; run merge without nogen"
        error 9
    }
    quietly count if _merge == 1
    local m_only = r(N)
    quietly count if _merge == 2
    local u_only = r(N)
    quietly count if inlist(_merge, 1, 3)
    local n_master = r(N)
    local share = cond(`n_master' > 0, `m_only' / `n_master', 0)
    local reason "master unmatched=`m_only'; using unmatched=`u_only'"
    if `share' > $SF_MAX & "`approved'" == "" {
        sf_write "`step'" $SF_N "STOPPED (script halted): `reason'"
        global SF_N = _N
        di as err "[data-integrity] merge `step': " %4.1f (100*`share') "% of master rows unmatched. Report to the user before continuing."
        error 9
    }
    sf_write "`step'" $SF_N "`reason'"
    global SF_N = _N
end

program define sf_cover
    syntax varlist, [BY(varlist) MIN(real 0.8) DIR(string)]
    if "`dir'" == "" local dir "log"
    foreach v of local varlist {
        preserve
        quietly gen byte _nm = !missing(`v')
        quietly gen byte _one = 1
        if "`by'" == "" {
            quietly gen byte _all = 1
            local grp _all
        }
        else local grp `by'
        collapse (sum) n=_one nonmissing=_nm, by(`grp')
        quietly gen share = nonmissing / n
        quietly gen flag = cond(share < `min', "LOW_COVERAGE", "")
        quietly gen variable = "`v'"
        quietly export delimited using "`dir'/coverage_`v'.csv", replace
        quietly count if flag != ""
        if r(N) > 0 di as txt "[data-integrity] `v': " r(N) " group(s) below " %3.0f (100*`min') "% coverage -- see `dir'/coverage_`v'.csv"
        restore
    }
end
