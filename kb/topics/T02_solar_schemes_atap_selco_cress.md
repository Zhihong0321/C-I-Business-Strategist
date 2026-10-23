---
id: T02
title: C&I solar schemes — NEM 3.0 (closed), Solar ATAP, Enhanced SELCO, CRESS, utility tenders
covers: scheme rules, sizing caps, export credit, mandatory BESS, standby charge, CRESS terms and agreements, scheme volumes
sources: [R1, R3, R4, R5, R6, R8]
conflicts: [C03, C08, C09, C11]
related: [T01, T03, T04, T09]
updated: 2026-10-23
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T02 — C&I solar schemes

## TL;DR
- **NEM 3.0 closed 30 June 2025** [R1, R4]. From **1 January 2026** two mutually exclusive behind-the-meter routes exist: **Solar ATAP** and **Enhanced SELCO** [R1, R4, R5].
- **Solar ATAP** (GP/ST/No. 60/2025): up to 100% of 12-month average MD, **hard cap 1 MWac**; export credited at **SMP (~18–20 sen/kWh)** against the energy charge only, **no rollover**; no standby charge; BESS optional [R1, R4, R6].
- **Enhanced SELCO** (GP/ST/No. 51/2024 Pin. 1/2026): **zero export**; above **1 MWac** a **BESS is mandatory** and a **standby charge of RM12/kWp/month** applies [R1, R4, R5, R6]. R5 states the BESS size rule as **E_BESS ≥ 1 × kWp (1-hour rating)** [C08].
- **CRESS** (off-site wheeling to MV/HV corporate buyers): minimum 30 MW; System Access Charge figures conflict (14 / 20 / 25 sen firm) [C03]. R1 reports an **18 Sep 2026 Acceleration Package**: 14 sen firm SAC, ≥50% / 4-hour BESS, ≥10-year PPA, COD by 31 Dec 2028.
- Only systems **≤72 kW** avoid a TNB Connection Assessment Study (CAS) — see T09.

## 1. Scheme comparison (merged)
| Feature | Solar ATAP | Enhanced SELCO ≤1 MWac | Enhanced SELCO >1 MWac | CRESS | NEM 3.0 (NEM NOVA) |
|---|---|---|---|---|---|
| Status | Live 1 Jan 2026 [R4] | Updated Jan 2026 [R4] | Updated Jan 2026 | "Expanded Mar 2025" [R4]; Acceleration Package 18 Sep 2026 [R1] | Closed 30 Jun 2025 [R1, R4] |
| Guideline | GP/ST/No. 60/2025 [R1, R4, R5] | GP/ST/No. 51/2024 (Pin. 1/2026) [R1, R5] | same | — | — |
| Target | LV & MV C&I [R4] | Large MV & HV industrial [R4] | same | HV malls, fabs, hyperscale data centres [R4]; HV and MV corporate off-takers [R1] | Legacy C&I rooftop [R4] |
| Size limit | 100% of 12-month average MD, hard cap 1,000 kW (1 MWac) [R1, R4, R6] | Sized to actual load, up to 1 MWac [R1] | No cap — "85% MD limit abolished" [R1]; "Up to 100% MD (No MW upper limit)" [R4] [C08] | Min 30 MW off-site farm [R4]; ≥30 MW solar + ≥50%/4-hr BESS under package [R1] | 1,700 MW national cap [R4] |
| National quota | None for C&I [R4, R6] | Uncapped [R4] | Uncapped | >3,000 MW allocated pipeline [R4] | 1,417.31 MW subscribed; 282.69 MW unsubscribed at closure [R4] |
| Mounting | Rooftop, carpark, covered walkways [R1] | Rooftop, ground, floating [R1] | Rooftop, ground, floating [R1] | Off-site farm | — |
| Export | Allowed; credited at Average SMP on base energy charge only [R1] | Prohibited (reverse power relay) [R1, R4] | Prohibited | Wheeled via TNB grid | SMP offset against net bill [R4] |
| Credit rollover | None — forfeited monthly [R1, R4, R6] | n/a | n/a | n/a | "3-mo rollover" [R4] |
| Standby charge | Exempt [R1] | Exempt [R1, R5] | **RM12/kWp/month** [R1, R4, R5, R6] | — | — |
| BESS | Optional [R1] | Optional [R1, R5] | **Mandatory from 1 Jan 2026** [R1, R3, R4, R5, R6]; E_BESS ≥ 1 × X kWh [R5] | ≥50% / 4-hour for 14 sen SAC [R1] | — |
| Application | SEDA eATAP, RM7.50/kW fee + TNB CAS [R1]; post-commissioning filing (Forms G & H) via atap.seda.gov.my [R4] [C11] | SEDA registration + TNB CAS + ST notification [R1] | SEDA registration + TNB CAS + ST licence [R1] | PSS Stage 1 & 2; 18–24 months lead [R4] | — |

## 2. Solar ATAP details
- Export value: R1 "Average SMP (~18.8–24.8 sen/kWh)", "~19 sen/kWh"; R4 "~18–20 sen/kWh"; R2/R5/R6 RM0.1881/kWh [C09]. R6: grid purchase "up to RM0.3132/kWh" vs export ~RM0.1881.
- R6: ATAP "Eliminated 1-to-1 retail tariff offsets for export."
- **Monthly Maximum Allowable Quantity (MAQ)** [R1]: **MAQ (kWh) = capacity (kWac) × 5 hours × days in month**. Export credit cannot exceed actual monthly grid import and is forfeited if unused. Example (R1 calculator default): 800 kWac × 5 × 30 = 120,000 kWh; × RM0.1911 = RM22,932 maximum gross export value.
- R4 (2026 forecast): ~185 MW of C&I Solar ATAP in 2026.
- R4 note: the 250 MW / RM150M **SuRIA Home** quota (RM600/kW rebate) is domestic only; C&I uses GITA instead.

## 3. Enhanced SELCO details
- Effective 1 Jan 2026 under GP/ST/No.51/2024 (Pin. 1/2026) and the notice "Notis Makluman Penyesuaian SELCO" [R5].
- Verbatim (as quoted by R5), Clause 3.6 / GP 51: "For a solar PV installation capacity of X kWp, the required BESS energy capacity (E_BESS) charged by the solar PV system must satisfy: E_BESS ≥ 1 × X kWh (a minimum 1-hour energy rating)."
- Verbatim (as quoted by R5), Clause 12.1 / Directive 27 March 2025: "IN ACCORDANCE WITH CLAUSE 12.1 OF THE SELCO GUIDELINES, THE MONTHLY STANDBY CHARGE AS APPROVED BY GOVERNMENT IS RM12/kWp."
- R6: the mandatory-BESS and RM12/kWp standby threshold was "raised from 72 kWp to >1 MWac"; large installations therefore lean to EaaS/PPA bundles. R4: standby "Reduced to RM12/kWp/month".
- Form of Information (Attachment 1) goes to TNB before installation and to ST within 30 days of commissioning (GP 51/2024) [R5].
- Example (R5 calculator default): 1,500 kWp at 1.2 MWac → mandatory BESS 1,500 kWh; standby RM18,000/month; "GITA 100%" offset RM396,000 (1,500 kWh × RM1,100 × 24%); CAS tier RM15,000 PSS.
- R3: BESS charges midday to "prevent zero-export clipping under SELCO guidelines".
- R4 volumes: SELCO additions ~45 MW (2022), ~65 (2023), ~95 (2024), ~160 (2025), ~210 forecast (2026); cumulative ~575 MW.

## 4. CRESS (Corporate Renewable Energy Supply Scheme) [C03]
- Renewable Energy Developers (REDs) sell green power directly to HV and MV corporate off-takers across Peninsular Malaysia via NEDA [R1].
- **18 September 2026 CRESS Acceleration Package** [R1]: firm-supply SAC cut from 25 to **14 sen/kWh**; plants must include **≥50% / 4-hour BESS**, sign **≥10-year PPAs**, reach COD by **31 December 2028**.
- SAC figures by report: R1 14 firm / 25 legacy firm / 45 non-firm; R3 14 sen developers / 4 sen consumers; R4 20 firm / 40 non-firm; R6 20 firm with BESS / 40 non-firm.
- Pricing: R6 "~26 sen generation + System Access Charge"; R1 calculator default PPA 38 sen/kWh vs HV ToU peak 44.52 sen.
- R1 CRESS calculator (defaults: PPA 38.0 sen, SAC 14 sen, 75 GWh/yr): net developer revenue 24.0 sen/kWh; RM18.0 million/yr; off-taker saving 14.6% vs 44.52 sen.
- Tenure 10–21 years; enforcement under BESC & CRESA security terms; developer keeps the remote farm/BESS [R6].
- **Five mandatory CRESS agreements** [R1]:
  1. Bilateral Energy Supply Contract (BESC) — RED ↔ Green Consumer PPA (min 10 years under the package).
  2. Corporate RE Supply Agreement (CRESA) — Green Consumer ↔ TNB top-up and backup supply.
  3. RE Supply Access Agreement (RE SAA) — RED ↔ TNB Grid Owner interconnection and transmission access.
  4. Back-feed Agreement — auxiliary station power imported by the solar plant and BESS from TNB.
  5. NEDA Agreement (Deed of Accession) — day-ahead dispatch scheduling with Single Buyer and SAC settlement.
- R1 HV/data-centre archetype: CRESS package with ≥30 MW solar + ≥50%/4-hr BESS; ≥10-year BESC via a ≥51% local RED SPV; "~38 sen/kWh delivered cost" with 24/7 RECs vs HV C4 peak 44.52 sen.
- Volumes: ~150 MW forecast 2026 [R4]; >3,000 MW allocated pipeline [R4]; >3,000 MWh off-site CRESS firming BESS [R4].
- Players: XPERTS.NRG consortium partner with TNB for 1,000 MWh CRESS BESS; Gentari "~1.5 GW Gamuda CRESS BESS"; Ditrolic EnerGreen SolarPack (CRESS) [R3, R8].

## 5. Utility-scale tenders (context for EPCC order books)
- "RM 13B–23B" EPCC order-book flow from LSS5, LSS6 and CRESS tenders [R8].
- MyBeST utility BESS auction: 400 MW / 1,600 MWh; Solarvest bidding [R8].
- Samaiden projected 125–188 MW LSS6 BESS awards [R8]; PETRA directed LSS6 BESS siting toward the south (Johor) [R4].
- Lake Kenyir 595 MWac floating solar + BESS, RM1.96B, Cypark (60%) / Sunview (40%) JV for TNB Genco (Apr 2026) [R8].

## 6. Scheme volumes (R4, C&I solar additions, MW)
| Scheme | 2022 | 2023 | 2024 | 2025 | 2026 forecast | Cumulative 2022–26 | Cap / pipeline | Source cited by R4 |
|---|---|---|---|---|---|---|---|---|
| NEM 3.0 (NEM NOVA C&I) | ~145 | ~240 | ~380 | ~440 | ~165 | ~1,370 | 1,417.31 MW subscribed (1,700 MW cap) | SEDA NEM portal & IET research (2025) |
| SELCO | ~45 | ~65 | ~95 | ~160 | ~210 | ~575 | Uncapped (100% MD sizing) | ST Strategic Plan 2026–2030 |
| Solar ATAP (C&I) | 0 | 0 | 0 | 0 | ~185 | ~185 | No national cap (max 1 MW/acct) | SEDA Solar ATAP portal (2026) |
| CRESS | 0 | 0 | 0 | 0 | ~150 | ~150 | >3,000 MW allocated | Farizal Partners RE review (2026) |
| Total | ~190 | ~305 | ~475 | ~600 | ~710 | ~2,280 | >4,417 MW subscribed/pipeline | ST Strategic Plan & SEDA |

## 7. Open questions
- Exact SELCO mandatory BESS rule (only R5 states 1 h × kWp) and whether "no cap" or "100% MD" applies above 1 MWac [C08].
- ATAP: pre-approval with fee vs post-COD filing [C11].
- CRESS SAC values after the 18 Sep 2026 package [C03].
