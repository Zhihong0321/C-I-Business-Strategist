---
id: REG-CONFLICTS
title: Conflict and verification register
covers: every point where the 9 research reports disagree with each other, or where a figure needs official confirmation
sources: [R1, R2, R3, R4, R5, R6, R7, R8, R9]
updated: 2026-10-23
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# Conflict and verification register

How to use: topic files tag disputed facts with `[C##]`. Look the ID up here before relying on the number. "Status" says what would settle it. None of these has been checked against an official source yet; all 9 reports are AI-generated.

Source IDs: R1 strategy hub · R2 MD mitigation portal · R3 BESS solutions dashboard · R4 market explorer · R5 BESS compliance navigator · R6 financing · R7 green tax portal · R8 market benchmark · R9 load profile analyzer. See `../00_INDEX.md`.

Note on independence: three of R9's seven case studies reuse figures from R1, R3 and R8 (see `internal_issues.md`). Where R9 repeats another report's number it is not a second source.

## Summary table

| ID | Topic | Severity | One-line summary | Status |
|---|---|---|---|---|
| C01 | GITA after 31 Dec 2026 | **Critical** | Reports disagree on whether standalone solar, standalone BESS and integrated solar+BESS keep GITA from 2027 | Open: read Budget 2027 Appendix 25 (tax-measures.pdf) and MGTC 2027 guideline |
| C02 | Size of the tax benefit | High | "Tax shield" quoted as 24%, 34%, 40% or 48% of capex depending on what is counted | Open: method issue; fix basis in our own models |
| C03 | CRESS System Access Charge | High | 14 / 20 / 25 sen firm; 40 / 45 sen non-firm; 4 sen consumer | Open: check PETRA/ST CRESS documents and the 18 Sep 2026 package |
| C04 | Legacy MD rate and % increase | Medium | Legacy baseline RM30.30, RM37.00 or RM45.10/kW; increase "+100% to +202%", "+115% to +201%" or "+162%" | Partly reconciled (different legacy tariffs) |
| C05 | MD share of a C&I bill | Medium | "30%–70%" vs "35%–45%" | Open: depends on load factor; measure per customer |
| C06 | ST licensing thresholds | Medium | Generation licence >72 kWac/kWp vs BESS licence ≥5 kW | Likely complementary (different assets); confirm |
| C07 | CAS / PSS fee above 1 MW | Low | RM15,000–20,000 for 1–5 MW vs RM15,000 for 1–2 MW and "high-tier" above 2 MW | Open: TNB fee schedule |
| C08 | SELCO sizing cap and mandatory BESS size | High | "No cap (85% MD limit abolished)" vs "up to 100% MD"; BESS ≥ 1 h × kWp stated by one report only | Open: GP/ST/No.51/2024 (Pin. 1/2026) text |
| C09 | SMP / ATAP export credit | Low | ~18.8–24.8 sen, 19.11 sen, 18.81 sen, 18–20 sen | Varies monthly; use published SMP |
| C10 | BESS turnkey cost | Medium | Assumptions range RM1,000–1,800/kWh | Open: use Eternalgy's own SAJ landed cost |
| C11 | Solar ATAP application process | Medium | eATAP application with RM7.50/kW fee + CAS vs post-commissioning filing (Forms G & H) | Open: SEDA ATAP guideline |
| C12 | Competitor portfolio figures | Low | Plus Xnergy >500 vs >400 MWp; Sunview >350 vs ~650–800 MWp | Open: Bursa filings |
| C13 | Peak window used in a warranty | Low | R6 Tier 2 warranty uses 08:00–22:00 (legacy window) vs RP4 14:00–22:00 | Error in R6 |
| C14 | Agency for GITA Asset | Low | MGTC (R1, R7) vs "MIDA GITA Asset" (R4) | R4 misattribution likely |
| C15 | MV account counts | Resolved | ~26,500 MV accounts vs ~12,200 MV industrial customers | Reconciled: 12,200 = E1 + E2 (industrial subset) |
| C16 | Voltage band definitions | Low | HV ">50 kV to ≤230 kV" vs "66 kV / 132 kV / 275 kV" | Open: tariff book |
| C17 | BESS payback claims | Medium | 1.6 yr to 6+ yr claimed; several calculators have errors | Method issue: payback depends on load shape |
| C18 | Zero-capex savings split | Low | Client keeps 15% vs 20–25% vs 15–30% | Different products; not a true conflict |
| C19 | Solar yield assumption | Low | 1,250 kWh/kWp/yr vs 115 kWh/kWp/month (~1,380/yr) | Use Eternalgy's SAJ fleet data |
| C20 | Standalone BESS GITA in 2027 (detail of C01) | **Critical** | 100% Tier 1 retained (R2, R3) vs "0% standalone, must integrate" (R7) | Open: same as C01 |
| C21 | Load shape of 24/7 process plants (gloves, fabs) | Medium | R4: Perak gloves among "peaky motor and furnace loads"; Penang 24-h plants suit SELCO + BESS and MD shaving. R9: gloves "extremely flat" (LF 88%, unviable); fabs flat (UPS + ATAP only) | Open: 30-min interval data from a glove plant and a fab |
| C22 | MD-shaving BESS sizing heuristic | Medium | Power 10%–20% of MD at 1–2 h (R3) vs top 20%–35% of peak with 1.3–1.5× energy buffer, 1–3 h by sector (R9) vs 3.5 h derated (R2) | Method issue: size from the customer's 30-min data |

---

## C01 — GITA treatment after 31 Dec 2026 (Critical)

| Report | Standalone solar (own use) | Standalone BESS (own use) | Integrated solar + BESS | Other |
|---|---|---|---|---|
| R1 (13:27, oldest) | 60% Tier 2, window closes 31 Dec 2026 | 100% Tier 1, window closes 31 Dec 2026 | not discussed | Calls 31 Dec 2026 a "tax cliff"; GITE 70% must apply to MIDA by 31 Dec 2026 |
| R2 | not stated | "BESS and integrated solar storage maintain Tier 1 status through 2030" | Tier 1, 100% ITA against 70% SI through 31 Dec 2030 | Standalone EE (VSDs, BMS, chillers) removed from GITA from 1 Jan 2027 |
| R3 | 2027–2030: Tier 2 60% (unchanged) | 2027–2030: Tier 1 100% (unchanged) | 2027–2030: elevated to Tier 1, 100% on entire system ("Major Catalyst") | — |
| R4 | — | — | — | Text: "31 December 2026 sunset of MIDA's GITA 100% tax allowance" |
| R6 | 2027–2030: 0% (removed) | not stated separately | 2027–2030: 100% Tier 1 | GITE deadline 31 Dec 2026 |
| R7 (dedicated tax research, cites MOF Appendix 25) | 0% from 1 Jan 2027 ("Omitted from Tier 2b RE list") | "0% Standalone (Must integrate)" | 100% Tier 1b (2027–2030), 70% SI cap | GITE solar leasing expires 31 Dec 2026; GITA Project Tier 3 (commercial solar) abolished; EE → ACA (Appendix 28) |
| R8 | — | — | — | "GITA / GTFS Sunset: 31 Dec 2026 — 60–100% Tax Allowance Deadline" |
| R9 | — | "Tier 1 Green Asset", 100% GITA (no date, no 2027 distinction) | — | Calls it "MIDA Tier 1" GITA; no Budget 2027 or 31 Dec 2026 mention |

Assessment:
- R7 is the only report built for this question, and the only one citing the Budget 2027 documents (speech 9 Oct 2026, Appendix 25 / Lampiran 25, MIDA release 12 Oct 2026). R6 agrees with R7 on solar and integrated systems.
- R1, R4 and R8 describe a full "sunset" on 31 Dec 2026; this reads like pre-Budget-2027 information.
- The sharpest disagreement is standalone BESS (see C20).
- R7 itself lists 5 unconfirmed items: gazette orders still in draft; no confirmed transition for late-2026 invoices commissioned in 2027; minimum BESS ratio for Tier 1b unknown; whether retrofitting BESS onto pre-2027 solar qualifies; MyHIJAU 100% treatment.

Status: **Open.** Settle by reading Budget 2027 Appendix 25 (tax-measures.pdf) and any MGTC 2027–2030 GITA Asset guideline. Matters for sales timing (a Q4 2026 rush for standalone solar) and for product design (solar must ship with BESS to keep GITA from 2027).

## C02 — Size of the tax benefit

| Report | Claimed benefit | Basis |
|---|---|---|
| R1 | Solar 38.4%, BESS 48.0% of capex | (GITA % + 100% CA) × 24% |
| R2 | 24% of BESS capex | GITA 100% × 24% |
| R3 | 24% of BESS capex; solar 14.4% | GITA × 24% |
| R4 calculator | 40% of BESS capex (net = 0.60 × gross) | "GITA + CA", not itemised |
| R5 calculator | 24% of BESS capex | GITA 100% × 24% on BESS only |
| R7 | "200% combined tax deduction… 48.0% of capex at 24%" (text); engine spreads CA (20% IA + 14% AA = 34% in year 1, then 14%/yr) and caps GITA at 70% of (SI − CA), unused GITA carried forward indefinitely | CA first is mandatory (P.U. (A) 243/2024 Para 6(1)) |
| R8 calculator | 34% of gross (100% GITA + CA), 24% (60% GITA) | Flat percentages |
| R9 | "Net ~48% CAPEX Subsidy"; payback "5–6 years down to 2.5–3.5 years"; its Solarvest case uses RM920k on RM2.4M (38.3%) | (100% GITA + 100% CA) × 24% |

Assessment: capital allowance is ordinary depreciation that any asset gets over time; GITA is the incentive. Payback headlines should show GITA alone (rate × capex × tax rate), state the 70% statutory-income cap, and show CA separately as timing. The customer must be profitable to use either.

## C03 — CRESS System Access Charge (SAC)

| Report | Firm supply | Non-firm | Other |
|---|---|---|---|
| R1 | 14 sen/kWh under the 18 Sep 2026 Acceleration Package (needs ≥50% / 4-hour BESS, ≥10-yr PPA, COD by 31 Dec 2028); 25 sen "legacy firm (pre-Sept 2026)" | 45 sen (solar without BESS) | 5 mandatory agreements |
| R3 | 14 sen/kWh (developers) | — | 4 sen/kWh (consumers) |
| R4 | 20 sen/kWh | 40 sen/kWh | "Expanded Mar 2025"; min 30 MW; >3,000 MW allocated; 18–24 months lead |
| R6 | 20 sen/kWh (with BESS) | 40 sen/kWh | ~26 sen generation + SAC; 10–21 yr tenure |

Possible reading: 20/40 sen = earlier framework, 14 sen = after the 18 Sep 2026 package. But R1's "legacy" figures (25/45) do not match R4/R6's 20/40. Status: open; check PETRA/ST CRESS guideline and the September 2026 announcement.

## C04 — Legacy (RP3) MD rate and % increase

| Report | Legacy MD (RM/kW/month) | Increase claimed |
|---|---|---|
| R1 chart | C1/E1 30.30; C2/E2 45.10; C3 29.20; C4/E3 43.60 | "+115% to +201%" (MV) |
| R2 | RM30.30–45.10 | "+100% to +202%"; "up to 202%" |
| R4 | — | "+115% to +201%" |
| R6 | "RP3 Baseline" 37.00 | "+162% vs RP3" |
| R8 | Text: from RM30.30; chart: legacy C1/C2 37.00; also an unexplained "RP4 High-Peak Industrial" 98.61 | "+162%" |
| R9 | "~RM37.00–RM45.10/kW" (E1/E2 ref); chart 41,000 per 1,000 kW; with 1.6% KWTBB ~RM37.59–45.82 | "+115% to +162%" |

Arithmetic: 89.27 / 30.30 = +194.6%; 97.06 / 45.10 = +115.2%; 97.06 / 37.00 = +162.3%. The ranges reflect which legacy tariff is the base. Use the per-tariff legacy rates (R1) when comparing. R9 gives RM98.61/kW = 97.06 × 1.016 (MV ToU incl. KWTBB), which explains R8's "unexplained" 98.61 bar.

## C05 — MD share of a C&I bill

R8: capacity + network "now represent 30% to 70% of C&I monthly power bills". R6: MD "accounting for 35% to 45% of an industrial electricity bill". R3's worked factory (500,000 kWh, 900 kW, MV General) gives 80,343 / 229,493 ≈ 35% (derived, not stated by R3). R9: 32.5% (rubber gloves, LF 88%) to 59.5% (metal stamping, LF 28%) — outputs of its own simulator at 1,000 kW with no solar, not measured bills; after solar without storage "from ~55% up to ~70%"; MPMA plastics plants "40%+". R9 supports the reading that the share depends on load factor. Share falls as load factor rises; measure per customer.

## C06 — ST licensing thresholds

R1: ST Section 9 generating licence mandatory above 72 kWac; ≤72 kWac exempt (Section 54 notification). R3: mandatory licensing for BESS ≥ 5 kW under the Electricity Supply Act 1990. R5: BESS ≥ 5 kW under GP/ST/No.62/2026 Clause 4.1(c), Section 9(1) Act 447 and ST licensing directive (1 July 2026); generation licence when SELCO PV > 72 kWp. Likely complementary (storage vs generation); confirm with the ST directive. R1 is also inconsistent with itself: its pathway table says SELCO ≤1 MWac needs only "ST Notification", while its CAS table requires a licence above 72 kWac.

## C07 — CAS / PSS fees above 1 MW

| Report | >1 MW tiers |
|---|---|
| R1 | >1,000–5,000 kWac: RM15,000–20,000, licence + mandatory BESS |
| R4 | "High Voltage (HV) Connection (Power System Study)": RM15,000 |
| R5 | >1,000–2,000 kW: RM15,000 (CAS/PSS, includes SELCO BESS study); >2,000–5,000 kW: "High-Tier PSS Fee" |

Tiers up to 1 MW agree across R1, R4, R5 (RM0 / 1,000 / 5,000 / 8,000).

## C08 — SELCO sizing cap and mandatory BESS size

- Cap: R1 "No Cap (85% MD limit abolished)" for SELCO >1 MWac; R4 "Up to 100% MD (No MW upper limit)".
- Mandatory BESS: all agree it applies to SELCO > 1 MWac from 1 Jan 2026. Only R5 gives a size rule: "E_BESS ≥ 1 × X kWh" (X = kWp; minimum 1-hour rating), citing "Clause 3.6 / GP 51". R6: threshold "raised from 72 kWp to >1 MWac".
- R7: minimum BESS ratio needed for GITA Tier 1b is unconfirmed (a separate rule from the SELCO one).

## C09 — SMP / ATAP export credit

R1: "Average SMP (~18.8–24.8 sen/kWh)", calculator default 0.1911, text "~19 sen". R2: RM0.1881/kWh. R4: "~18–20 sen/kWh". R5: ~RM0.188 (chart 0.1881). R6: ~RM0.1881. SMP is a monthly market figure; use the published value.

## C10 — BESS turnkey cost per kWh

| Report | Figure |
|---|---|
| R2 calculator | RM1,200/kWh |
| R3 | Banner RM1,150–1,600/kWh; calculator RM1,350/kWh; Northern Solar RM1,150–1,600/kWh turnkey |
| R4 calculator | RM1,800/kWh (outlier) |
| R5 calculator | RM1,100/kWh default |
| R6 | RM1,150–1,600/kWh (containerised) |
| R8 | 200–500 kWh cabinets RM1,150–1,450; 2–5 MWh containers RM1,000–1,350; chart 50–200 kWh racks 1,475 / cabinets 1,300 / containers 1,175; 2-hour LFP RM2,300–2,900/kW |

Use Eternalgy's own SAJ landed cost for modelling.

## C11 — Solar ATAP application process

R1: SEDA eATAP application, RM7.50/kW fee, plus TNB CAS. R4: "Post-commissioning filing (Forms G & H)", post-COD filing via atap.seda.gov.my. Could be two steps of one process; confirm with GP/ST/No.60/2025 and SEDA.

## C12 — Competitor portfolio figures

| Company | R3 | R8 |
|---|---|---|
| Plus Xnergy | 100 MWh BESS, >500 MWp solar | >400+ MWp solar, 100 MWh BESS |
| Sunview | >350 MWp completed across 150+ sites | ~650–800+ MWp portfolio; RM1.17B backlog |
| Ditrolic | >300 MW managed / >1 GW constructed | 1,000+ MW constructed / 300 MW O&M (consistent) |

## C13 — Peak window used in a warranty

R6 Tier 2 warranty: "≥97% system uptime specifically during peak hours (08:00–22:00)". RP4 peak window is 14:00–22:00 weekdays (all reports, including R6 elsewhere). 08:00–22:00 was the legacy window (R2). Treat as an R6 error.

## C14 — Agency for GITA Asset

R1 and R7: MGTC verifies GITA Asset (own consumption); MIDA handles GITA Project and GITE. R4: "MIDA GITA Asset 100% Investment Tax Allowance" and "MIDA's GITA 100% tax allowance". R9: "The MIDA Tier 1 Green Investment Tax Allowance (GITA) Shield", "100% MIDA GITA tax shield". Likely R4 and R9 misattribution.

## C15 — MV account counts (resolved)

R4: MV General ~19,120 (C1 ~11.2k, E1 ~7.8k, F1 ~120) + MV ToU ~7,380 (C2 ~2.9k, E2 ~4.4k, F2 ~80) = ~26,500 MV accounts. R4 geography: "~12,200 Medium Voltage industrial manufacturing customers" = E1 7.8k + E2 4.4k. Consistent.

## C16 — Voltage band definitions

R2: LV ≤1 kV (400 V); MV >1 kV to ≤50 kV; HV >50 kV to ≤230 kV. R4: LV 400 V / 230 V; MV 11 kV / 33 kV; HV 66 kV / 132 kV / 275 kV.

## C17 — BESS payback claims

Claims: R2 roadmap "2–3 years" with GITA; R3 "3–5 year payback"; R4 MV TAM "3.0–4.5 years (w/ GITA 100%)"; R8 zero-capex financier "~4-year payback", Solarvest "~3-year payback"; Plus Xnergy "RM1.25M/year savings per 10 MWh"; R9 "5–6 years down to 2.5–3.5 years" with a ~48% tax shield, "~2.5 yr payback" with GITA, case studies 2.1–4.2 years (three of them recycle R1, R3 and R8 figures). Calculator placeholders and their computed outputs disagree (see `internal_issues.md` and each source extract's "Extraction notes"). Payback depends on how many hours a day the load sits above the target MD; see `../topics/T08_bess_technical_and_sizing.md` §8.

## C18 — Zero-capex savings split

R6: IPMVP shared savings 75:25 or 80:20 (ESCO : host), 5–10 years (7 standard). R8: Plus Xnergy client keeps 15% (bills RM82.50/kW vs TNB RM97.06/kW); EV Connection 15%–30% client split. R6 also cites the Plus Xnergy 15% model; R9 repeats R8's Plus Xnergy example as a "case study" (15-year EaaS). Different products, not a true conflict.

## C19 — Solar yield assumption

R3: ~115 kWh per kWp per month (≈1,380 kWh/kWp/yr). R8: 1,250 kWh/kWp/yr at RM0.38 avoided cost. R9: ~105 kWh/kWp/month (≈1,260 kWh/kWp/yr). Use Eternalgy's SAJ fleet data by state.

## C20 — Standalone BESS GITA in 2027 (Critical, part of C01)

R2: "BESS and integrated solar storage maintain Tier 1 status through 2030." R3: standalone BESS "Tier 1: 100% GITA" in both 2024–2026 and 2027–2030. R7 matrix: standalone BESS (own use) 2027–2030 = "0% Standalone (Must integrate)"; R7 chart: standalone BESS 100 → 0. R6: does not separate. R9: BESS "Classified as a Tier 1 Green Asset, qualifying for 100%", with no date and no 2027 distinction (reads as pre-Budget-2027 information). If R7 is right, BESS-only MD-shaving retrofits lose GITA from 2027 unless paired with RE.

## C21 — Load shape of 24/7 process plants (gloves, semiconductor fabs)

| Report | Rubber gloves | Semiconductor / Penang fabs |
|---|---|---|
| R4 (state table) | Perak row lists "Cement & limestone, rubber gloves, ceramics, foundry & casting, shipbuilding/marine, automotive" with: Peaky motor and furnace loads; RM89.27/kW MD reduction via BESS "critical for margin preservation" | Penang: "24-hour MNC plants on MV/HV ToU; cleanroom chiller baseloads favour >1 MWac SELCO + BESS and precision MD shaving" |
| R9 (sector table) | LF 88%, "Extremely flat 24/7 load across all shifts. Stopping a line ruins in-process latex." — "Unviable for Standalone BESS" (score 15) | LF 85%, "<8% diurnal variation. Poor for standalone MD shaving" — "UPS / Solar ATAP Only" (score 25); Penang/Kedah automation vendors in BKIP/Perai are Tier 1 |

Possible reading: R4 describes a state's sector mix (cement and foundries are peaky; gloves may not be), and its Penang point is about the SELCO >1 MWac BESS mandate, not MD fit. R9 is about the load shape of each sector. Neither cites load data. Status: **open** — settle with 30-minute interval data from at least one glove plant and one fab before targeting either. Until then, treat flat 24/7 plants as solar (+ SELCO-mandated BESS) prospects, not MD-shaving BESS prospects.

## C22 — MD-shaving BESS sizing heuristic

| Report | Power | Energy / duration |
|---|---|---|
| R3 | 10%–20% of facility MD | 1–2 hours (0.5C–1C) |
| R9 | "top 20%–35% peak clipping" | "1.3×–1.5× energy buffer for 90% DoD and round-trip efficiency"; 1.0–3.0 h by sector (stamping 1.0–1.5 h; malls and hotels 2.0–3.0 h) |
| R2 calculator | ΔkW × 1.15 | ΔkW × 3.5 h / (0.85 × 0.90 × 0.90) |
| R3, R4, R8 calculators; R9 case studies | full kW shaved | ~2 kWh per kW (R9 cases 2.0–3.1 kWh/kW) |

Status: method issue, not a fact to verify. The right size depends on how many hours a day the load sits above the target MD; size from the customer's 12 months of 30-minute data (see `../context/eternalgy_profile_and_analysis.md` §3, analysis).
