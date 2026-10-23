---
id: T10
title: Strategy playbooks proposed by the reports (client archetypes, roadmaps, segment strategies)
covers: what each report recommends — R1 client archetypes and EPCC/RPVI playbook, R2 12-month C&I execution roadmap, R4 segment TAM strategy, R6 financing pathways, R7 post-2027 model, R8 moats and price-war segments
sources: [R1, R2, R3, R4, R6, R7, R8]
related: [T05, T07, T08]
updated: 2026-10-23
note: These are the reports' own recommendations, several written before the Budget 2027 tax changes (see C01). Our planning conclusions for Eternalgy are in ../context/eternalgy_profile_and_analysis.md.
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T10 — Strategy playbooks proposed by the reports

## 1. R1 — client archetype playbook (for a dual-licensed RPVSP + RPVI EPCC)
| Archetype | Optimal regulatory pathway | Recommended commercial model | Core engineering strategy | Sales pitch |
|---|---|---|---|---|
| 1. Q4 2026 tax cliff (outright capex buyers) | SELCO ≤1 MWac or Solar ATAP (fast-track commissioning) | Outright purchase with MGTC Tier 1/2 GITA Asset submission | Target COD before 31 Dec 2026 so the MGTC GITA/A application is filed before the deadline | "38.4% cash tax savings on Solar and 48% on BESS before the 31 Dec 2026 GITA window closes" (see C01, C02) |
| 2. Low Voltage C&I (Tariff B & D: retail, warehouses, light industrial) | SELCO ≤1 MWac (7-day load) or Solar ATAP (5-day load) | Outright capex or TNBX SARE tripartite PPA (TNB credit protection) | Size strictly to daytime base load to displace the full 50.68 sen/kWh + AFA | "Simple payback of 3.5–4.5 years by offsetting bundled LV energy + network rates" |
| 3. Medium Voltage C&I (C1, C2, E1, E2: manufacturing & process plants) — default selection | Enhanced SELCO (≤1 MWac voluntary BESS / >1 MWac mandatory BESS) | Private bilateral hybrid PPA (shared savings on MD reduction) | BESS shifts 10AM–2PM off-peak solar to shave RM89.27–97.06/kW MD in the 2PM–10PM peak | "Standalone solar fails on MV due to off-peak morning rates. Hybrid BESS unlocks massive MD savings." |
| 4. High Voltage & hyperscale data centres (C3, C4, E3) | CRESS Acceleration Package (≥30 MW solar + ≥50%/4-hr BESS) | ≥10-year BESC via ≥51% local RED SPV | Lock in 14 sen/kWh firm SAC; fast-track EPCC to hit the 31 Dec 2028 COD deadline | "Deliver green power with 24/7 RECs at ~38 sen/kWh delivered cost against HV Tariff C4 peak rate (44.52 sen)" |
R1 SARE vs private bilateral (detail in T07 §4): SARE for pure rooftop solar on B, D, C1, E1 (TNB collects, 2 sen/kWh fee, disconnection enforcement); private bilateral hybrid PPA for solar + BESS on C2, E2, E3 (no TNB fee, shared savings on MD).

## 2. R2 — phased 12-month C&I execution roadmap (for facility owners)
| Phase | Timing | Focus | Actions |
|---|---|---|---|
| 1 | Days 1–30 | Interval data audit & tariff arbitrage | Download 12 months of half-hourly smart-meter CSV data; compute demand factor and load factor; apply the ToU arbitrage equation |
| 2 | Days 30–90 | DSM sequencing & EMS | Reprogram morning-shift start-up cycles; install a 3-tier EMS with automatic 30-min MD predictive load shedding |
| 3 | Months 3–9 | BESS & solar storage | Deploy AI-sized BESS behind the meter; apply for Tier 1 GITA 100% ITA with MGTC "to compress payback to 2–3 years" |
| 4 | Months 6–12 | EECA institutionalisation & TES | Appoint certified REM Class 1/2; submit annual EECR report to ST; evaluate thermal storage for HVAC |
R2 mitigation hierarchy: zero-capex tariff arbitrage → operational scheduling → software load shedding → solar-plus-storage → thermal decoupling (T08 §6).

## 3. R4 — segment strategy (TAM synthesis)
- **LV:** Solar ATAP; ≤72 kW zero-CAS sweet spot plus 72–180 kW SMEs; top 8–10% of SME roofs (130k–160k premises); 2,500–3,200 MWp; BESS niche (50–100 MWh); payback 3.5–5.0 yrs.
- **MV ("sweet spot"):** SELCO + BESS (>1 MWac mandate) and Solar ATAP + BESS (≤1 MW); 6,500–8,500 MWp and 3,500–5,500 MWh; payback 3.0–4.5 yrs with GITA 100%.
- **HV:** CRESS wheeling + multi-MW SELCO + BESS; >3,000 MW CRESS + 800–1,200 MW onsite; 1,500–2,500 MWh BTM.
- Geography: Selangor first ("#1 market for 1–20 MWh SELCO + BESS"), Johor fastest-growing, Penang 24/7 MNC plants (T04 §6).

## 4. R6 — financing pathways by customer (detail in T07 §9)
SME owner → financed outright (LCTF/HTG); SME tenant → operating lease; mid-market → split asset (solar on a loan, BESS on zero-capex shared savings); large → SARE PPA or CRESS; Pioneer/ITA/RA firms → PPA. Standalone solar from 2027 → pair with BESS for 100% GITA.

## 5. R7 — post-2027 model
"Battery Storage (BESS) is Now Mandatory for Solar Tax Relief" from 1 Jan 2027; "Third-Party PPA / Leasing Models Lose Fiscal Parity" (GITE ends); recommended model is host-owned integrated solar + BESS capex claiming 100% GITA Tier 1b + CA, financed with Green Sustainability Fund 2.0 (1% subsidy) or bank hire purchase; EE retrofits move to ACA (Appendix 28). Urgent: pre-2027 standalone solar (60%) and GITE (70%) need full commissioning and MGTC/MIDA submission by 31 Dec 2026.

## 6. R8 — where margins survive
- Moats: bundling solar with mandatory SELCO BESS; HV switchgear / data-centre ELP integration; proprietary AI EMS dispatch.
- Avoid: 50–300 kWp rooftop price war (~RM2.40/Wp low-ball quotes), BoP subcontracting (6.5–10.8% GP), plain BESS hardware distribution without EMS.
- Protected: zero-capex / EaaS peak shaving (needs balance sheet, REM engineers, performance guarantees), data-centre ELP, HV grid.
- Direct C&I turnkey earns 25–35% GP vs 15–22% utility EPC.

## 7. R3 — positioning statements
- "The BESS + ToU Optimization Opportunity": under MV ToU, capacity and network are charged only on 2–10 PM weekday peaks; off-peak spikes are exempt; BESS discharges in the window.
- "The MV ToU Tariff Trap": migrating without demand control raises the MD rate +8.7% and peak energy to 31.32 sen.
