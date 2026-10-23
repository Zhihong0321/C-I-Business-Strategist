---
id: T08
title: BESS for C&I — why it is needed, topologies, sizing rules, dispatch, EMS, demand-side alternatives, site suitability
covers: solar/tariff mismatch, load-curve examples, hardware topologies and models, sizing heuristics and formulas, dispatch patterns, EMS functions, MD mitigation hierarchy (tariff switch, DSM, EMS, BESS, thermal storage), which sites suit BESS
sources: [R1, R2, R3, R4, R5, R8, R6]
conflicts: [C08, C10, C17]
related: [T01, T05, T06, T09]
updated: 2026-10-23
pending: R9 (research prompt #4, load profiles by industry) not yet received
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T08 — BESS technical and sizing

## TL;DR
- **Solar alone does not reliably cut MD**: peak solar (10:00–15:00) falls mostly in off-peak, and cloud dips plus the 18:00–22:00 "dark peak" set the month's MD anyway [R2, R3, R1].
- **BESS charges at midday (from solar surplus or off-peak grid) and discharges 14:00–22:00** to hold grid draw under a target [R3, R1].
- **Sizing heuristic for MD shaving: 10%–20% of facility MD, 1–2 hours (0.5C–1C)** [R3]. Several calculators assume 1 kW shaved per 2 kWh [R3, R4, R8]. R2 sizes for 3.5 hours with derating (DoD 0.85 × η 0.90 × SoH 0.90) and a 1.15 power safety factor.
- **SELCO >1 MWac: BESS ≥ 1 hour × PV kWp** (R5 only) [C08].
- **Mitigation ladder (R2):** tariff switch (zero capex) → operational DSM → EMS automatic load shedding → solar + BESS → thermal energy storage for chiller-heavy sites.
- Sites with short, sharp peaks in the window (stamping presses, cranes/welding, compressors, motors, furnaces) suit BESS; flat 24/7 loads need long durations [R3, R4, R2].

## 1. Why BESS: the mismatch
- "Peak solar irradiance occurs from 10:00 AM to 3:00 PM (Off-Peak tariff). TNB's expensive Peak Tariff starts at 2:00 PM and extends to 10:00 PM. BESS bridges this gap…" [R3].
- "Standalone rooftop Solar PV fails to guarantee Maximum Demand reduction on MV/HV tariffs due to afternoon cloud transients (sudden solar drops) and the 18:00–22:00 dark peak. Pairing solar with BESS secures peak shaving and avoids cheap SMP export loss (RM0.1881/kWh)" [R2].
- R4: high rooftop solar in Selangor/Johor has depressed midday SMP (a "duck curve").
- R5: storing surplus solar instead of exporting at SMP (RM0.1881) to avoid peak import (RM0.3132) gives a spread of "RM 0.09 to RM 0.13 per kWh", plus the MD effect.

### 1a. R2 example — cloud transient and dark peak (grid demand, kW)
| Time | Standalone solar | Solar + BESS |
|---|---|---|
| 08:00 | 400 | 400 |
| 10:00 | 300 | 300 |
| 12:00 | 250 | 250 |
| 14:00 (ToU peak starts) | 450 | 450 |
| 15:00 (cloud sag) | 1,100 | 750 |
| 17:00 | 800 | 750 |
| 19:00 (dark peak) | 1,200 | 750 |
| 21:00 | 1,000 | 750 |
| 22:00 | 600 | 600 |

### 1b. R1 example — 24-hour factory profile (kW)
Baseline load 00:00–23:00: 300, 300, 300, 300, 300, 400, 700, 950, 1100, 1150, 1200, 1180, 1100, 1150, 1200, 1200, 1180, 1150, 1100, 900, 700, 500, 350, 300.
Solar: 0 (00–05), 50 (06), 200, 450, 700, 850, 900 (11), 850, 700, 450, 200, 50 (16), 0 after.
BESS discharge: 400 kW at 14:00–19:00, 300 kW at 20:00 (~2,700 kWh/day; charging not modelled).
True peak-window MD (computed in R1 extract): baseline 1,200 kW; solar only 1,150 kW; solar + BESS 750 kW (R1 displays hard-coded 1,200 / 1,200 / 800 kW). Savings at RM97.06: 450 kW → RM43,677/month (R1 shows 400 kW → RM38,824).

### 1c. R3 example — dispatch visualiser (kW)
Baseline: 400, 380, 380, 390, 420, 500, 700, 850, 900, 920, 950, 940, 880, 900, 960, 980, 950, 910, 850, 750, 650, 550, 450, 420.
Solar: 0×6, 50, 200, 500, 850, 950, 980, 920, 750, 400, 150, 20, 0×7.
BESS (negative = charging): −200 at 10:00 and 11:00; +250 at 14:00–16:00, +200 at 17:00, +100 at 18:00.
Net peak in the window stays at 750 kW in every mode. Full series incl. the two hard-coded button modes: `../sources/R3_bess_solutions_dashboard.md`.
R3's three steps: 1. Midday charging (10am–1pm) from excess solar or off-peak grid ("to prevent zero-export clipping under SELCO"); 2. Peak discharge (2pm–10pm) by AI-driven EMS when equipment start-ups threaten the target; 3. Capped grid demand locks in lower capacity and network charges.

## 2. Hardware topologies (R3)
| Topology | Size range | Description | Models named |
|---|---|---|---|
| Modular outdoor cabinets | 100 kW – 2.5 MW, pre-assembled | Integrated LFP packs, BMS, liquid cooling, fire suppression and bidirectional PCS in < 2 m² footprint | Sungrow PowerStack 255CS; Huawei LUNA2000-215/241; LVK-GS-522 |
| Containerised systems | 5 MWh – 45+ MWh, heavy industry | 20-ft containers, AC-coupled liquid cooling, stepping up to 11 kV or 33 kV via MV skids | Sungrow PowerTitan 2.0; HyperStrong HyperBlock III AC Block |
| PV + ESS + EV microgrids | Fast-charging buffers | "5-in-1" buffers for 360–480 kW DC fast chargers so fleet charging does not trigger TNB demand penalties | Sigenergy SigenStor; Huawei One-Fits-All; Sungrow EVC platform |
Specs named elsewhere: Sungrow PowerStack 255CS 125 kW / 257 kWh; PowerTitan 2.0 2.5 MW / 5 MWh; Sungrow operates "up to 50°C without derating"; Huawei LUNA2000-213KTL smart PCS, 92% VDE-certified round-trip efficiency, hybrid cooling; LVK-GS-522ESSC-100 250 kW / 522 kWh, IP54 [R3]. Insurance-driven tropical specs: IEC 60529 IP54+, IK08 impact, active HVAC keeping internal temperature below 30°C [R5].

## 3. Sizing by objective (R3 matrix)
| Objective | Power rating | Duration | Driver |
|---|---|---|---|
| Demand-charge peak shaving | 10%–20% of facility MD | 1–2 hours (0.5C–1C) | Shave 30-minute spikes from compressors, chillers, stamping presses to cut RM89–97/kW |
| Solar arbitrage & clipping capture | Sized to PV clipping volume | 2–4 hours (0.25C–0.5C) | Store 10am–3pm SELCO/ATAP surplus to displace 31.32 sen evening peak energy |
| Short-interruption ride-through | 100% of critical process load | 15–30 minutes (2C) | Bridge voltage sags and brief trips for CNC, ovens, assembly lines |

## 4. Sizing formulas used in the reports
- **R2:** inverter kW = ΔkW × 1.15; battery kWh = ΔkW × 3.5 h / (0.85 DoD × 0.90 η × 0.90 SoH_EoL); capex RM1,200/kWh. Default (1,800 kW MD, 25% cut = 450 kW): 518 kW, 2,288 kWh, RM2,745,098, payback 4.0 yrs after 24% GITA (page placeholder shows 2.4 yrs). Note says "across the 8-hour weekday peak window" but code uses 3.5 h.
- **R3, R4, R8:** kWh = 2 × kW shaved (2-hour, 0.5C); full kW assumed shaved.
- **R5 (SELCO >1 MWac rule):** E_BESS ≥ 1 × PV kWp (kWh).
- **R8 zero-capex:** 2-hour LFP at RM2,300–2,900/kW.
- **R4 calculator:** RM1,800/kWh, 2-hour, net capex 60% after tax.

## 5. EMS functions named
- Predictive interval control: D_projected = 2 × [E(t_e) + P_inst × ((30 − t_e)/60)]; shed non-critical AHUs / unload chillers for 15 minutes when projected > target [R2].
- "Manual operational discipline fails over time" → 3-tier EMS synchronised to TNB's 30-minute windows [R2].
- Solarvest AIES (AI-driven Energy Simulator) predicts factory load curves to prevent premature battery depletion; EPMS monitoring [R3, R8].
- Ditrolic Net-Zero Energy OS, 15-minute interval dispatch; Plus Xnergy SOURCE; Tanand EasiEMS early alerts (750 kW vs 800 kW ceiling) [R8, R6].
- Pre-sizing studies: EVOLTS mandatory 30-day interval metering audit; EVC and XPERTS.NRG 12-month data logging / interval analysis [R3, R8].

## 6. MD mitigation ladder (R2)
1. **Tariff arbitrage (zero capex):** MV General vs MV ToU switch maths (T01 §8).
2. **Operational DSM:**
   - Morning shift pull-down (06:00–14:00): pre-14:00 demand carries zero MD on ToU, so run batch furnaces, autoclaves, extruders and thermal pull-downs 06:00–13:30, then drop to holding mode before 14:00.
   - PLC motor staggering with mutual-exclusion interlocks: stopping three 50 kW compressors starting in the same 30-min block saves 150 kW = **RM14,559/month** on MV ToU.
3. **Granular EMS & load shed** (§5).
4. **Solar PV + BESS** (§1).
5. **Thermal energy storage (TES):** chillers can be up to 60% of peak demand in commercial complexes, hospitals and cleanroom factories; make ice / chilled water off-peak (22:00–14:00) and discharge 14:00–22:00; qualifying sites can apply for TNB's **MV TES tariff schedule**.

## 7. Which sites suit BESS (from the reports)
| Load type / sector | Evidence |
|---|---|
| Automotive stamping (press spikes) | LVK 250 kW / 522 kWh case study [R3, R4]; Selangor stamping cluster [R4] |
| Shipbuilding / marine (cranes, welding) | HO Energy 4.3 MW / 8.36 MWh [R4]; Perak Lumut [R4] |
| Aerospace components | Elecod 1.5 MW / 2.60 MWh [R4] |
| Food / grain processing | Plus Xnergy 20 MWh SELCO site [R4, R8] |
| Electronics (Penang) | ERS 200 kWh with 500 kWp solar, 35% MD cut [R8]; Penang 24/7 plants on ToU favour >1 MWac SELCO + BESS [R4] |
| Cement, foundry, gloves (Perak) | "High concentration of peaky motor and furnace loads" [R4] |
| CNC, ovens, automated lines | Ride-through + MD shaving [R3] |
| Compressors, chillers | 10%–20% of MD shaving heuristic [R3]; TES for chillers [R2] |
| EV fast-charging hubs | PV + ESS + EV buffers [R3]; Gentari hub [R8] |
Load shapes by industry are the subject of research prompt #4 (R9, pending). For a payback rule of thumb by "hours per day above target", see `../context/eternalgy_profile_and_analysis.md` (analysis, not from the reports).
