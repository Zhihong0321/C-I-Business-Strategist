---
id: T06
title: Pricing benchmarks, O&M rates, EPCC margins, payment milestones, paybacks
covers: solar EPCC RM/Wp by size, BESS RM/kWh by size, cost drivers, O&M %, warranty cost adders, gross/net margins by segment, payment stages and retention, payback and IRR claims, savings assumptions used by the calculators
sources: [R8, R3, R6, R2, R4, R5, R1, R9]
primary_source: R8 (answers research prompt #3; unsourced)
conflicts: [C10, C17, C19]
related: [T05, T07, T08]
updated: 2026-10-23
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T06 — Pricing, margins and payment terms

## TL;DR
- **C&I rooftop solar turnkey: RM1.85–3.80/Wp** (100 kWp RM2.40–3.80; 500 kWp RM2.40–2.60; 1 MWp RM2.00–2.50; 3 MWp RM1.85–2.20) [R8].
- **C&I BESS turnkey: RM1,150–1,450/kWh** for 200–500 kWh cabinets; **RM1,000–1,350/kWh** for 2–5 MWh containers [R8]; other reports RM1,150–1,600/kWh [R3, R6] [C10].
- H1 2026 cost pressure: China's 9% VAT rebate removal; silver +167%; copper +40% [R8].
- **Direct C&I turnkey GP 25%–35%** vs utility main EPC 15%–22% vs balance-of-plant subcontracting 6.5%–10.8% vs HV grid ~50% [R8].
- Typical payments: 10–20% at LOA, 40–50% on equipment delivery, 20–25% installation, 5–10% COD, **5% retention for a 12-month defects period** ("locks ~half of contractor net margin") [R8].

## 1. Solar EPCC pricing (R8, 2026)
| Capacity | Turnkey unit rate | Gross capex range | Payback (post-GITA) |
|---|---|---|---|
| 100 kWp | RM2.40–3.80/Wp | RM240k–380k | 4.0–4.5 yrs |
| 500 kWp | RM2.40–2.60/Wp | RM1.20M–1.30M | 4.4 yrs |
| 1 MWp | RM2.00–2.50/Wp | RM2.00M–2.50M | 3.5–4.5 yrs |
| 3 MWp | RM1.85–2.20/Wp (solar) | RM5.55M–6.60M | 3.5–4.5 yrs |

R8 chart "Solar EPCC CAPEX per Tier (Gross vs Net Effective after GITA)" (basis of "net" not stated):
| Tier | Gross RM/Wp | Net after GITA RM/Wp |
|---|---|---|
| 100 kWp | 2.80 | 2.12 |
| 500 kWp | 2.50 | 1.90 |
| 1 MWp | 2.25 | 1.71 |
| 3 MWp (solar only) | 2.00 | 1.52 |
| 3 MWp (bundled BESS) | 3.25 | 2.21 |
R8 simulator unit rates: 100 kWp RM2.80; 500 kWp RM2.50; 1 MWp RM2.20; 3 MWp RM2.00.
Low-ball market quotes for 50–300 kWp: ~RM2.40/Wp, achieved "by omitting roof reinforcement and structural warranties" [R8].

## 2. BESS pricing [C10]
| Source | Figure | Notes |
|---|---|---|
| R8 text | 200–500 kWh cabinets RM1,150–1,450/kWh; 2–5 MWh containers RM1,000–1,350/kWh | "Includes LFP active liquid-cooled cabinets/containers, PCS, EMS & NFPA 855 fire suppression" |
| R8 chart (gross → net after GITA) | 50–200 kWh racks 1,475 → 973; 200–500 kWh cabinets 1,300 → 858; 2–5 MWh containers 1,175 → 775 | Net ≈ 66% of gross |
| R8 simulator | 200 kWh RM1,350; 500 kWh RM1,250; 2 MWh RM1,150 | — |
| R8 zero-capex example | 2-hour LFP battery RM2,300–2,900/kW (≈RM1,150–1,450/kWh) | Plus Xnergy model |
| R3 | RM1,150–1,600/kWh turnkey benchmark; calculator RM1,350/kWh "avg"; Northern Solar RM1,150–1,600/kWh | "3–5 Year Payback for C&I Facilities" |
| R6 | RM1,150–1,600/kWh "Commercial Containerized Storage" | — |
| R2 calculator | RM1,200/kWh | — |
| R4 calculator | RM1,800/kWh | outlier |
| R5 calculator | RM1,100/kWh default | — |

## 3. O&M rates (R8)
| Asset | Annual O&M (% capex) | Unit rate | Scope |
|---|---|---|---|
| C&I rooftop solar | 1.0%–1.5% | RM25–45/kWp/yr | Cloud monitoring, panel washing, thermal scans |
| C&I BESS (preventive) | 1.5%–2.5% | RM15–35/kWh/yr | EMS dashboard, chiller service, fire safety checks |
| C&I BESS (full wrap) | 3.5%–4.5% | RM45–60/kWh/yr | Includes mid-life cell augmentation & performance SLAs |

## 4. BESS warranty / guarantee cost adders (R6)
| Tier | What is guaranteed | Cost adder | Typical in |
|---|---|---|---|
| Tier 1 | Hardware: LFP capacity retention (e.g. 80% SoH at year 10) and round-trip efficiency (85% down to 78%); remedy = free cell replacement/augmentation; excludes missed TNB savings | +2%–3% capex | Outright capex purchases |
| Tier 2 | Peak-window availability ≥97% (R6 states 08:00–22:00 [C13]); 24/7 remote NOC; 6-hour on-site response in Peninsular Malaysia | +3%–5% capex | Storage service agreements, O&M, operating leases |
| Tier 3 | Binding MD kW reduction or RM savings floor; LDs = missed TNB charges or 100% monthly fee forfeiture | +5%–8% capex | Project finance / shared savings |

## 5. EPCC margins (R8)
| Segment | Gross margin (text) | Chart GP % | Chart core net % |
|---|---|---|---|
| Direct C&I rooftop turnkey | 25%–35% | 30.0 | 12.5 |
| Utility main EPC (LSS5 / CGPP) | 15%–22% | 18.5 | 7.5 |
| Utility BoP / installation subcontracting | 6.5%–10.8% ("often net operating losses") | 8.6 | −2.5 |
| High-voltage grid engineering | ~50% | 50.0 | 28.2 |
Listed company margins: see T05 §2 (Northern Solar 27.4–37.8% GM, FY26 ~34.4%; Solarvest 28.3–28.5%; Pekat 25.2–27.0%; Sunview 12–16%; Founder 6.5–10.8%; Cheeding ~50%).

## 6. Payment milestones and working capital (R8)
| Stage | Share | Trigger | Covers |
|---|---|---|---|
| 1 | 10%–20% | LOA & survey | Site engineering, SLD, TNB connection check & CAS filing |
| 2 | 40%–50% | Equipment delivery | Tier-1 modules, inverters & BESS cabinets on site |
| 3 | 20%–25% | Installation | Roof mounting, DC/AC cabling, MV transformer & switchgear hookup |
| 4 | 5%–10% | COD commissioning | TNB meter swap, SCADA/EMS testing, grid handover sign-off |
| 5 | 5% retention | 12-month Defects Liability Period | "Locks ~half of contractor net margin" |

## 7. Payback, IRR and return claims [C17]
| Claim | Source |
|---|---|
| LV solar payback 3.5–4.5 yrs (offsetting LV energy + network) | R1 |
| LV solar 3.5–5.0 yrs; MV solar + BESS 3.0–4.5 yrs (w/ GITA 100%); HV 3.5–5.5 yrs | R4 |
| BESS "3–5 Year Payback for C&I Facilities"; Northern Solar "3–5 year industrial payback with GITA Tier 1"; Solarvest "~3-year payback" | R3 |
| Roadmap: Tier 1 GITA "to compress payback to 2–3 years" | R2 |
| Mid-market solar financed via GTFS 5.0: IRR 17%–30%, payback 4.0–6.0 yrs | R6 |
| Owner-occupier SMEs: RM950k–1.6M lifetime benefit over 25 yrs, 2x–3x a PPA | R6 |
| Zero-capex BESS financier return 12%–18% p.a. (~4-year payback) | R8 |
| Plus Xnergy: RM1.25M/yr savings per 10 MWh | R3, R4 |
| "100% GITA" + "100% Capital Allowance" at 24% = "Net ~48% CAPEX Subsidy", cutting simple payback "from 5–6 years down to 2.5–3.5 years"; capex purchase with GITA "~2.5 yr payback" (see C02) | R9 |
| Case studies: 2.1 yrs (overseas CNC), <2.5 yrs (Solarvest), 2.5–3.5 yrs (UniBess), 2.8–3.5 yrs (Livoltek, with GITA), 3.0–4.2 yrs (Avera); three reuse figures from R1, R3, R8 (T08 §9) | R9 |
Calculator outputs at default inputs, as computed by running each report's code (placeholders shown on the pages are often different):
| Report | Calculator | Computed at defaults | Placeholder shown |
|---|---|---|---|
| R2 | BESS ROI (MV ToU, 1,800 kW, 25% cut) | 2,288 kWh, RM2,745,098 capex, 4.0 yrs | 1,825 kWh, RM1,642,500, 2.4 yrs |
| R3 | Bill & BESS (MV ToU, 500,000 kWh, 900 kW, 1,000 kWp, 250 kW BESS) | Bills RM231,854 → 174,400 (−24.8%), RM689,448/yr, 1.8 yrs | RM229,693 → 170,748, RM707,340, 3.1 yrs |
| R4 | Bill & BESS (MV General, 800 kW, 250,000 kWh, 250 kW shaved) | RM157,280 → 134,605, RM272,095/yr, ~2.0 yrs | RM135,420 → 113,102, RM267,810, ~3.2 yrs |
| R8 | Project ROI (500 kWp, 200 kWh, 100% GITA + CA) | RM1,520,000 gross, RM516,800 tax shield (34%), RM344,624/yr gross savings, 2.9 yrs | RM1,520,000 gross, RM391,800 tax, RM253,200/yr, 4.4 yrs |
| R1 | Load-curve simulator (hybrid mode) | True peak-window MD 750 kW (450 kW shaved, RM43,677/month) | Hard-coded 800 kW (400 kW shaved, RM38,824/month) |
| R7 | Tax engine (Tier 1b, RM2M capex, RM1.5M SI, 24%) | Year-1 CA RM680,000; Year-1 GITA used RM574,000; 5-yr cumulative cash saving RM912,000 (45.6%) | Text claims 48.0% of capex |
| R9 | Post-solar bill simulator (MV ToU, 1,000 kW stamping plant, LF 0.28, 500 kWp, 250 kW shaved) | Bill RM121,829, MD share 59.8%, BESS savings RM24,265/month (RM291,180/yr); no capex or payback computed | Bill RM163,144, 59.5% (the no-solar, no-BESS baseline) |
Each source extract's "Calculators" section has the formulas and full outputs.

## 8. Savings assumptions used inside calculators [C19]
| Assumption | Value | Source |
|---|---|---|
| Solar yield | 1,250 kWh/kWp/yr at RM0.38 blended avoided cost | R8 |
| Solar yield | ~115 kWh/kWp/month; solar energy capped at 40% of consumption | R3 |
| Solar yield | ~105 kWh/kWp/month (~1,260 kWh/kWp/yr), split 40% peak / 60% off-peak; solar never reduces MD; no export credit | R9 |
| BESS savings | kW shaved × RM97.06/month, no battery size or charging cost | R9 |
| BESS shaving ratio | 1 kW shaved per 2 kWh (2-hour, 0.5C) | R3, R4, R8 |
| BESS sizing | kW shaved × 3.5 h / (0.85 DoD × 0.90 η × 0.90 SoH); inverter × 1.15 | R2 |
| Tax benefit | 24% / 34% / 40% / 48% of capex depending on report | C02 |
