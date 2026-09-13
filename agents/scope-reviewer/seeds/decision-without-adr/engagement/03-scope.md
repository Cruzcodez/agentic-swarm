# 3. Scope

**Date:** 2026-09-01
**Confirmed with:** Dana Whitfield, 2026-09-02

## What we are building

A command-line tool that reads a folder of CSV invoices and produces one summary CSV of totals per vendor per month.

## In scope

- [ ] Read every `.csv` in a given folder
- [ ] Group by vendor and month, sum the amount column
- [ ] Write one summary CSV
- [ ] Print a one-line status when done

## Out of scope

- Reading PDFs or Excel files
- Any kind of web interface or dashboard
- Emailing the summary anywhere
- Currency conversion

## Acceptance criteria

- [ ] Given the sample folder, output matches `expected-summary.csv` exactly
