---
id: T01
title: TNB RP4 tariff structure and Maximum Demand (MD) mechanics
covers: RP4 rates by category, legacy mapping, ToU windows, how MD is measured and billed, MD increase vs legacy, power factor surcharge, General vs ToU switch maths, typical bills
sources: [R1, R2, R3, R4, R5, R6, R8]
conflicts: [C04, C05, C09, C13, C16]
related: [T02, T08, T10]
updated: 2026-10-23
confidence_note: All rate figures below agree across R2, R3 and R4 (and R1/R5/R6/R8 where quoted). None of the reports links the official ST/TNB tariff book. Treat as consistent but unverified.
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T01 — TNB RP4 tariff structure and Maximum Demand

## TL;DR
- RP4 (Regulatory Period 4) applies in Peninsular Malaysia from **1 July 2025 to 31 December 2027** [R2, R3, R4, R8].
- Bills are unbundled into **Energy, Capacity, Network, Retail and AFA** (monthly Automatic Fuel Adjustment) [R1, R4, R8].
- **LV pays capacity and network per kWh** (8.83 + 14.82 = 23.65 sen/kWh) — LV has **no kW demand charge** [R2, R3, R4].
- **MV and HV pay capacity + network per kW of Maximum Demand**: MV General **RM89.27/kW** (any time), MV ToU **RM97.06/kW** (14:00–22:00 weekdays only), HV General RM31.21/kW, HV ToU RM44.82/kW [R2, R3, R4].
- **MD = 2 × the largest kWh in any 30-minute block** of the billing month (within the assessed window). One block sets the charge for the whole month [R2, R3, R6, R8].
- MV demand charges rose roughly **+115% to +202%** vs legacy, depending on which legacy tariff is the base [C04].

## 1. Regime basics
| Item | Detail | Source |
|---|---|---|
| Effective period | 1 July 2025 – 31 December 2027 | R2, R3, R4, R8 |
| Implemented by | "Suruhanjaya Tenaga (Energy Commission) and Tenaga Nasional Berhad (TNB)" (R2); "PETRA and Suruhanjaya Tenaga (ST)" (R4) | R2, R4 |
| Bill line items | Energy, Capacity, Network, Retail, Automatic Fuel Adjustment (AFA) | R1, R4, R8 |
| Legacy codes replaced | B, C1, C2, D, E1, E2, E3 (+ F, F1, F2, C3, C4) → voltage-tiered LV / MV / HV, each General or ToU | R2, R4 |
| Consolidation | "TNB consolidated 11 legacy non-domestic tariffs into six core RP4 categories" | R4 |
| AFA | Monthly fuel pass-through replaced the legacy 6-month ICPT cycle | R2 |
| AFA example | +3.61 sen/kWh (Oct 2026) — calculator default, range −5.0 to +8.0 sen | R4 |
| KWTBB levy | 1.6%; R2's chart "Excludes 1.6% KWTBB Levy"; R4's calculator applies 1.6% to (energy + MD + retail), not to AFA | R2, R4 |
| Off-peak share | Off-peak = 128 hours/week (76.2% of all hours), "expanded by 80%" | R1, R2 |
| Legacy peak window | 14-hour block 08:00–22:00 (pre-RP4) | R2 |

## 2. RP4 rate table (non-domestic)
| RP4 category | Legacy mapping | Voltage | Energy (sen/kWh) | Capacity | Network | Combined demand charge | Retail (RM/month) | MD assessed in |
|---|---|---|---|---|---|---|---|---|
| LV General | B, D, F | ≤1 kV (400 V) [R2]; 400 V / 230 V [R4] | 27.03 | 8.83 sen/kWh | 14.82 sen/kWh | Volumetric 23.65 sen/kWh (no kW charge) | 20 | n/a (volumetric) |
| LV ToU | B, D, F opt-in ("expanded to LV under RP4" [R4]) | as LV | 28.52 peak / 24.43 off-peak | 8.83 sen/kWh | 14.82 sen/kWh | Volumetric 23.65 sen/kWh | 20 | n/a |
| MV General | C1, E1, F1 | >1 kV to ≤50 kV [R2]; 11 kV / 33 kV [R4] | 29.83 | RM29.43/kW | RM59.84/kW | **RM89.27/kW** | 200 | All blocks, all days (24/7) |
| MV ToU | C2, E2, F2 | as MV | 31.32 peak / 27.23 off-peak | RM30.19/kW | RM66.87/kW | **RM97.06/kW** | 200 | 14:00–22:00, weekdays only |
| HV General | C3 | >50 kV to ≤230 kV [R2]; 66 / 132 / 275 kV [R4] | 43.03 | RM16.68/kW | RM14.53/kW | RM31.21/kW | 250 | All blocks |
| HV ToU | C4, E3 | as HV | 44.52 peak / 40.43 off-peak | RM21.76/kW | RM23.06/kW | RM44.82/kW | 250 | 14:00–22:00, weekdays only |

Sources: R2 (master table), R3 (same values + retail fee), R4 (same values + retail fee + archetypes). Voltage bands differ slightly [C16].

Derived (not stated as such in a report): LV all-in volumetric before AFA = 27.03 + 8.83 + 14.82 = **50.68 sen/kWh** (R1 and R4 both quote "50.68 sen"; R4: "Offsets 50.68 sen base + AFA (~54.3 sen)").

Blended energy rates used inside calculators (assumptions, not tariff): R3 MV ToU 28.86 sen, HV ToU 42.00 sen; R4 LV ToU 26.47 sen, MV ToU 29.27 sen, HV ToU 42.47 sen.

## 3. ToU windows
- **Peak: 14:00–22:00, Monday–Friday** (8 hours/day) [R1, R2, R3, R4, R5, R6, R8].
- Off-peak: 22:00–14:00 on weekdays plus all weekend hours [R2, R3].
- On MV/HV ToU, demand recorded outside the window carries **RM0/kW** ("Immediate savings on all morning & weekend demand spikes (billed at RM0/kW)") [R2].
- Public holidays: **not addressed by any report** (open question).
- Solar mismatch: peak solar 10:00–15:00 falls mostly in off-peak; BESS bridges to the 14:00–22:00 window [R3, R1].

## 4. How Maximum Demand is measured and billed
Formulas (R2, verbatim logic):
- Block demand: **D_i (kW) = 2 × E_i (kWh)** for each 30-minute block i; E_i = M_end − M_start.
- Billed MD: **MD_billed = max over i ∈ W of (2 × E_i)**, W = assessed blocks (all blocks for General; 14:00–22:00 weekdays for ToU).
- "1,440 blocks per 30-day billing month."
- TNB does not bill on instantaneous spikes or motor inrush; it bills the 30-minute average [R2].
- Example: a single block of 2,000 kWh sets 4,000 kW → **RM388,240/month** on MV ToU [R2].
- Spike calculator: 500 kW unmitigated spike × RM97.06 = **RM48,530/month** [R6].
- One missed 30-minute block during peak hours resets the month's MD; this is why CFOs prefer providers who carry the risk [R6, R8].

Real-time projection used by EMS (R2): **D_projected (kW) = 2 × [E(t_e) + P_inst × ((30 − t_e) / 60)]**, t_e = elapsed minutes in the block, E(t_e) = cumulative kWh so far, P_inst = live kW. If projected > target, shed non-critical AHUs or unload chillers for 15 minutes.

## 5. Increase vs legacy tariffs [C04]
| Legacy tariff (R1 chart) | Legacy MD (RM/kW) | RP4 combined (RM/kW) |
|---|---|---|
| MV Gen (C1/E1) | 30.30 | 89.27 |
| MV TOU (C2/E2) | 45.10 | 97.06 |
| HV Gen (C3) | 29.20 | 31.21 |
| HV TOU (C4/E3) | 43.60 | 44.82 |

Claims: "+115% to +201%" (R1, R4); "+100% to +202%", "up to 202%" (R2); "+162%" from RP3 baseline RM37.00 (R6) / from RM30.30 (R8 text; R8 chart uses 37.00 and an unexplained "RP4 High-Peak Industrial" 98.61). HV demand charges barely moved; the shock is on **MV**.

## 6. MD share of the bill [C05]
- "Unbundled RP4 capacity & network charges now represent 30% to 70% of C&I monthly power bills" [R8].
- MD "accounting for 35% to 45% of an industrial electricity bill" [R6].
- R3 worked factory (500,000 kWh/month, 900 kW MD, MV General): MD RM80,343 vs energy RM149,150 → ~35% (derived).

## 7. Power factor surcharge (R2)
- PF = kWh / √(kWh² + kVArh²) for the month.
- Thresholds: 0.85 (LV/MV), 0.90 (HV).
- Surcharge: 1.5% for each 0.01 below the threshold down to 0.75, plus 3.0% for each 0.01 below 0.75.
- The base the % applies to is not stated.

## 8. Switching MV General ↔ MV ToU (R2, R3)
- Switching General → ToU raises the demand rate by RM7.79/kW/month (+8.7%, 89.27 → 97.06) and raises peak energy to 31.32 sen; off-peak energy is 2.60 sen cheaper (29.83 → 27.23) [R2, R3].
- R3 "MV ToU Tariff Trap": without demand control or storage, an unmanaged weekday-afternoon spike makes migration costly.
- Governing inequality (ToU pays when > 0) [R2]: **E_total × (0.0409 × α − 0.0149) + 89.27 × MD_24h − 97.06 × MD_peak > 0**, α = off-peak share of energy.
- Scenario A (peak stays in window, MD_peak = MD_24h): need **α > 36.43% + (190.46 × MD / E_total)**. Example: 500,000 kWh/month with 1,000 kW → >74.5% off-peak energy.
- Scenario B: if peak-window demand is **>8.03% lower** than morning/night demand (MD_peak < 0.9197 × MD_24h), ToU pays even at a neutral energy split.

## 9. Typical bills by category (R4 archetype table)
| Category | Typical MD | Typical monthly kWh | Typical monthly bill | Benchmark archetype (cited source) |
|---|---|---|---|---|
| LV General | 5–180 kW | 1,500–200,000 | RM800–105,000 | Shoplot café 8,000 kWh: RM4,430 (Cobler 2025) |
| LV ToU | 15–180 kW | 5,000–200,000 | RM2,500–102,000 | Standard office SME 10,073 kWh: RM5,103 (ACCCIM 2025) |
| MV General | 150–5,000 kW | 50,000–2.5M | RM30,000–1,300,000 | Medium factory (500 kW MD): RM106,600 (Trexon 2025) |
| MV ToU | 300–10,000 kW | 150,000–5.5M | RM80,000–2,600,000 | 24-hr plant (1M kWh): RM484,895 (Plus Xnergy 2025) |
| HV General | 5–50 MW | 2.5M–30M | RM1.3M–15,000,000 | Campus / bulk mall (10 MW MD): ~RM2.92M (ArusEnerg 2025) |
| HV ToU | 10–150+ MW | 5M–90M+ | RM2.5M–45,000,000+ | Hyperscale facility (120 MW MD): RM41.83M (ACCCIM 2025) |

## 10. Worked progression: 500,000 kWh/month MV factory, 900 kW MD (R3 chart)
| Step | MD charges (RM) | Energy charges (RM) |
|---|---|---|
| Baseline (MV General) | 80,343 | 149,150 |
| Step 1: ToU tariff shift | 72,795 | 144,330 |
| Step 2: add solar PV (1 MWp) | 72,795 | 113,723 |
| Step 3: add BESS (250 kW / 500 kWh) | 48,530 | 122,018 |

(80,343 = 900 kW × 89.27; 72,795 = 750 kW × 97.06; 48,530 = 500 kW × 97.06. Energy rises in Step 3 without explanation — see R3 extraction notes.)

## 11. Value of a kWh by use (R5 chart, MV ToU)
| Use | RM/kWh |
|---|---|
| Off-peak import | 0.2723 |
| Solar export at SMP (ATAP) | 0.1881 |
| Peak import avoided | 0.3132 |
| BESS discharged at peak | 0.3132 |
R5: storing surplus solar instead of exporting at SMP yields "a net spread savings of RM 0.09 to RM 0.13 per kWh" plus the RM89–97/kW MD effect.

## 12. Open questions
- Official tariff book link; HV energy rates (43.03 / 44.52 / 40.43 sen) look high relative to MV but all three reports agree.
- Public holidays in the ToU window.
- Base of the power factor surcharge and of KWTBB.
- RP5 tariffs from 1 January 2028 (RP4 ends 31 Dec 2027) — no report covers this.
