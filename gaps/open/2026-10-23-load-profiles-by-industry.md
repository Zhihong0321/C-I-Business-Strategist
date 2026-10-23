---
id: GAP-2026-10-23-load-profiles-by-industry
question: "Which Malaysian industries have short demand peaks inside 14:00-22:00 weekdays (good BESS fit) versus flat 24/7 loads?"
asked_via: "Knowledge base build (seed)"
date: 2026-10-23
status: open
priority: high
related: [T08, T04, C21, C22]
---

## Why the repo can't answer it
Partly answered since 23 Oct 2026 by R9 (`kb/sources/R9_load_profile_analyzer.md`, summarised in `kb/topics/T08_bess_technical_and_sizing.md` §8). R9 gives one load factor and a text load shape for 11 sectors, but no sources, no measured interval data, and its "MD share" figures come from its own simulator. Three of its seven case studies reuse figures from R1, R3 and R8. R4 and R9 disagree on rubber gloves [C21].

## What would answer it
12 months of 30-minute interval data from real MV customers in the R9 Tier 1 sectors (metal stamping, plastic injection, food processing, office towers) and in gloves / semiconductor; published case studies with a named site, date and link.

## Interim answer given (unverified)
R9 (grade C, unsourced): spiky, 1–2 shift loads suit BESS — metal stamping (LF 28%), office towers (32%), food processing (42%), plastic injection (55%); malls, hotels and hospitals are moderate; cold storage is conditional; flat 24/7 loads are poor — textile spinning (78%), E&E / semiconductor (85%), rubber gloves (88%). R4 calls Perak's cement, foundry and glove loads peaky. Meter before promising savings.
