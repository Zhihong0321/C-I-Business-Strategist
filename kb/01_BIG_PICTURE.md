---
id: BIG-PICTURE
title: Malaysia C&I solar + BESS market — big-picture synthesis across all research reports
sources: [R1, R2, R3, R4, R5, R6, R7, R8, R9]
updated: 2026-10-23
read_next: [topics/T01 … T10, registers/conflicts.md, context/eternalgy_profile_and_analysis.md]
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../RULES.md) yet, read it first.

# Big picture: Malaysia C&I solar + BESS (Peninsular / TNB area), as of Oct 2026

## 1. The market story in 10 points
1. **RP4 made Maximum Demand the main pain for MV customers.** From 1 Jul 2025, demand is billed as capacity + network: MV General RM89.27/kW (any time), MV ToU RM97.06/kW (14:00–22:00 weekdays), roughly +115% to +200% on legacy rates. A single 30-minute block sets the whole month's charge. MD is now ~30–45%+ of an MV industrial bill. [T01; C04, C05]
2. **LV customers have no kW demand charge.** LV capacity and network are per kWh (23.65 sen); all-in ~50.68 sen/kWh before AFA. Solar saves the full rate there; BESS has no MD to shave. [T01]
3. **Net metering ended; self-consumption rules took over.** NEM 3.0 closed 30 Jun 2025. From 1 Jan 2026: **Solar ATAP** (≤1 MWac, export credited only at SMP ~18–20 sen, no rollover) or **Enhanced SELCO** (zero export; above 1 MWac a **BESS is mandatory** plus **RM12/kWp/month standby**). [T02]
4. **Solar alone rarely cuts MD, and load shape decides whether BESS pays.** Solar peaks in the off-peak window and drops out with clouds and in the evening, so the month's peak survives (R9: the MD share of the bill rises after solar). BESS that charges at midday and discharges 14:00–22:00 is the lever on MV. R9 ranks spiky, 1–2 shift loads first — metal stamping, office towers, food processing, plastic injection (load factor 28%–55%) — and calls flat 24/7 loads (gloves, semiconductor fabs, textile spinning; LF 78%–88%) poor fits; unsourced. [T08 §8; C21]
5. **MV is the sweet spot.** ~26,500 MV accounts (1.6% of C&I accounts) use ~65,190 GWh (~59% of C&I energy). R4 puts MV TAM at 6,500–8,500 MWp solar and 3,500–5,500 MWh BESS. Selangor (33–35%) and Johor (21–23%) hold over half of MV industrial load; R9 puts the densest spiky-load clusters in Shah Alam, Klang, Bangi–Kajang, Tebrau and Senai. [T04]
6. **BESS is early.** Only ~145–180 MWh of C&I BESS exists (85–110 MWh commissioned by mid-2026), led by Plus Xnergy (100 MWh incl. a 20 MWh single site). C&I solar additions are ~600 MW (2025) → ~710 MW (2026F). [T04, T05]
7. **Tax incentives are pivoting — and the details are disputed.** The most-supported reading (R7, R6): Budget 2027 (9 Oct 2026) extends GITA to 2030 only for **integrated solar + BESS (100%)**; **standalone solar drops to 0%** and **GITE solar leasing ends** after 31 Dec 2026. Standalone BESS is contested. Pre-2027 rules need invoice + commissioning + MGTC receipt by 31 Dec 2026. [T03; C01, C20]
8. **Competition is consolidating around BESS + software.** Large listed EPCCs and funded zero-capex players (Solarvest, Plus Xnergy, Sunview, Samaiden, Ditrolic, Gentari, Cenergi, Northern Solar…) sell solar + BESS with proprietary EMS. Price wars: 50–300 kWp rooftops (~RM2.40/Wp quotes) and plain BESS hardware distribution. Protected: zero-capex MD shaving, data-centre electrical, HV grid. [T05]
9. **How customers pay:** SMEs mostly buy with bank debt (BNM LCTF ≤5%, HTG 3.5–5%); large firms mostly use PPAs (SARE 21 yrs ~25 sen; bilateral 10–30% below TNB). MD-shaving BESS is often zero-capex — the client keeps 15–30% of MD savings — because a single missed peak loses the month; guarantees add 2–8% to capex. [T07]
10. **BESS compliance is heavy:** ST licence for BESS ≥5 kW (GP/ST/No.62/2026), IEC 62619 / IEC 63056 / UL 9540A, BOMBA MS 2747:2024 2-hour fire rating and Fire Certificate (~8–14+ weeks), TNB CAS above 72 kW even at zero export, PEPC sign-off, Forms G/H. Insurers make it a condition of cover. [T09]

## 2. Key numbers cheat sheet
Grade: **A** consistent across reports and linked to an official document (not yet opened by us); **B** consistent across ≥2 reports, no official link; **C** single report; **D** reports conflict.
| Fact | Value | Grade | Where |
|---|---|---|---|
| RP4 period | 1 Jul 2025 – 31 Dec 2027 | B | T01 |
| MV General / MV ToU demand charge | RM89.27 / RM97.06 per kW-month | B | T01 |
| HV General / HV ToU demand charge | RM31.21 / RM44.82 per kW-month | B | T01 |
| ToU peak window | 14:00–22:00, Mon–Fri | B | T01 |
| LV capacity + network | 8.83 + 14.82 = 23.65 sen/kWh (no kW charge) | B | T01 |
| MD definition | 2 × max 30-min kWh in the billing month (assessed window) | B | T01 |
| Legacy → RP4 MD increase | +115% to +202% (base-dependent) | D | C04 |
| MD share of bill | 30%–70% (R8) / 35%–45% (R6) / 32.5%–59.5% by sector, modelled (R9) | D | C05 |
| BESS fit by load factor | LF < 0.60 good; LF > 0.75 "excessive storage" | C (R9) | T08 §8 |
| Tier 1 BESS sectors | Metal stamping, office towers, food processing, plastic injection | C (R9) | T08 §8 |
| Flat-load sectors (poor MD fit) | Rubber gloves (LF 88%), semiconductor (85%), textile spinning (78%) | D (R9 vs R4) | C21 |
| MD-shaving BESS size | 10%–20% of MD, 1–2 h (R3) vs top 20%–35% of peak, 1–3 h (R9) | D | C22 |
| MV ToU MD incl. 1.6% KWTBB | RM98.61/kW (MV General RM90.70) | C (R9) | T01 |
| Off-peak includes public holidays | Yes (R9 only) | C | T01 §3 |
| ATAP | ≤1 MWac; export at SMP (~18–20 sen); no rollover | B | T02 |
| SELCO >1 MWac | Mandatory BESS + RM12/kWp/month standby | B | T02 |
| SELCO BESS size | ≥1 h × PV kWp | C (R5) | C08 |
| CRESS firm SAC | 14 / 20 / 25 sen/kWh | D | C03 |
| C&I accounts / energy | ~1,648,000 / 110,140 GWh (76.5% of Peninsular) | C (R4) | T04 |
| MV accounts / energy | ~26,500 / ~65,190 GWh | C (R4) | T04 |
| C&I solar additions | ~600 MW (2025), ~710 MW (2026F) | C (R4) | T04 |
| Installed C&I BESS | ~145–180 MWh (85–110 commissioned) | C (R4) | T04 |
| MV TAM | 6,500–8,500 MWp solar; 3,500–5,500 MWh BESS | C (R4) | T04 |
| Solar EPCC price | RM1.85–3.80/Wp (scale-dependent) | C (R8) | T06 |
| BESS turnkey price | RM1,000–1,600/kWh | B (range overlap) | C10 |
| Direct C&I turnkey gross margin | 25%–35% | C (R8) | T06 |
| Zero-capex MD tariff (Plus Xnergy) | RM82.50/kW vs TNB RM97.06 (client keeps 15%) | B (R6, R8) | T07 |
| Integrated solar + BESS GITA 2027–2030 | 100% | B (R2, R3, R6, R7) | T03 |
| Standalone solar GITA from 2027 | 0% (R6, R7) vs 60% (R3) | D | C01 |
| Standalone BESS GITA from 2027 | 0% must integrate (R7) vs 100% (R2, R3) | D | C20 |
| GITE solar leasing (70%) | Ends 31 Dec 2026 | B (R1, R6, R7) | T03 |
| BESS ST licence threshold | ≥5 kW (GP/ST/No.62/2026) | A (R5 links ST PDF; R3 agrees) | T09 |
| CAS fees ≤1 MW | RM0 / 1,000 / 5,000 / 8,000 (≤72 / 180 / 425 / 1,000 kW) | B | T09 |
| BOMBA | MS 2747:2024, 2-hour FRR, ≥3.0 m or fire wall | B (R3, R5) | T09 |
| EECA 2024 | ≥21,600 GJ/yr → Regulated Energy Consumer, must appoint REM | C (R2) | T09 |
| GTFS 5.0 | RM1.0B to 31 Dec 2026, 0% rebate, 60–80% guarantee | C (R6) | T07 |
| Green Sustainability Fund 2.0 | RM2B, 1% p.a. subsidy for 5 yrs | C (R7) | T03 |

## 3. Solid vs shaky
- **Solid enough to plan on:** RP4 rate structure and MD mechanics; LV vs MV distinction; ATAP/SELCO basics; MV as the BESS market; BESS compliance stack; MD-miss risk shaping contracts.
- **Must verify before acting:** all Budget 2027 GITA rules [C01, C20]; CRESS SAC [C03]; SELCO BESS sizing rule [C08]; market sizes from R4 (modelled, several weak/stale sources); every competitor figure (no links); every calculator payback (see `registers/internal_issues.md`); R9's sector load factors and case studies (no sources; three cases recycle R1, R3 and R8 figures).
- **Evidence quality:** all 9 reports are AI-generated dashboards; only R4 (23 links) and R5 (3 links) cite anything. See `registers/citations.md`.

## 4. Top open questions
1. Exact Budget 2027 Appendix 25 wording: standalone solar, standalone BESS, integrated system, minimum BESS ratio for Tier 1b, transition for late-2026 invoices. (Drives Q4 2026 sales and 2027 product design.)
2. Real load shapes by industry: R9 gives a ranking (T08 §8) but no measured data or sources, and disagrees with R4 on gloves [C21]. 30-minute data from real MV customers is needed, and how to get it from TNB is still open (gap `tnb-30min-data-access`).
3. CRESS SAC after the 18 Sep 2026 package.
4. SELCO >1 MWac BESS sizing rule and "no cap" vs "100% MD".
5. RP5 tariffs from 1 Jan 2028 (RP4 ends 31 Dec 2027) — not covered by any report.

## 5. For Eternalgy
Company profile, the segment-fit table, the BESS payback rule of thumb and what this research changes for Eternalgy are in `context/eternalgy_profile_and_analysis.md` (marked as analysis, not report content).
