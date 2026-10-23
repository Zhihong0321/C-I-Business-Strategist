---
id: T08
title: BESS for C&I — why it is needed, topologies, sizing rules, dispatch, EMS, demand-side alternatives, site suitability
covers: solar/tariff mismatch, load-curve examples, hardware topologies and models, sizing heuristics and formulas, dispatch patterns, EMS functions, MD mitigation hierarchy (tariff switch, DSM, EMS, BESS, thermal storage), which sites suit BESS, load profiles by industry (R9), BESS case studies (R9)
sources: [R1, R2, R3, R4, R5, R8, R6, R9]
conflicts: [C08, C10, C17, C21, C22]
related: [T01, T04, T05, T06, T09]
updated: 2026-10-23
note: R9 (research prompt #4, load profiles by industry) added 23 Oct 2026. Its load factors, sector ratings and case studies carry no source; three of its seven case studies reuse figures from R1, R3 and R8 (see §9).
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
- **Load shape by industry (R9, unsourced, grade C):** Tier 1 = metal stamping (load factor 28%), office towers (32%), food processing (42%), plastic injection (55%); Tier 2 = malls (52%), hotels (62%), hospitals (72%), cold storage (68%, "conditional"); poor fit = textile spinning (78%; dyeing plants are spiky), E&E / semiconductor (85%), rubber gloves (88%, "unviable for standalone BESS") [R9; C21]. Rule: LF < 0.60 good, LF > 0.75 "requires excessive storage" (§8).
- R9 sizes PCS for the **top 20%–35% of peak** with a 1.3×–1.5× energy buffer; R3 says 10%–20% of MD [C22].

## 1. Why BESS: the mismatch
- "Peak solar irradiance occurs from 10:00 AM to 3:00 PM (Off-Peak tariff). TNB's expensive Peak Tariff starts at 2:00 PM and extends to 10:00 PM. BESS bridges this gap…" [R3].
- "Standalone rooftop Solar PV fails to guarantee Maximum Demand reduction on MV/HV tariffs due to afternoon cloud transients (sudden solar drops) and the 18:00–22:00 dark peak. Pairing solar with BESS secures peak shaving and avoids cheap SMP export loss (RM0.1881/kWh)" [R2].
- R4: high rooftop solar in Selangor/Johor has depressed midday SMP (a "duck curve").
- R5: storing surplus solar instead of exporting at SMP (RM0.1881) to avoid peak import (RM0.3132) gives a spread of "RM 0.09 to RM 0.13 per kWh", plus the MD effect.
- R9 "Post-Solar Load Factor Distortion Effect": solar without storage cuts kWh but not MD, so "the MD share of the electricity bill surges from ~55% up to ~70%". R9's own simulator gives 59.5% → 66.4% for a 1,000 kW stamping plant with 500 kWp (T01 §6).

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

R9 "Dynamic Sizing" step: "Size PCS (kW) for top 20%–35% peak clipping with a 1.3×–1.5× energy buffer for 90% DoD and round-trip efficiency"; durations by sector run 1.0–3.0 hours (§8) [R9; C22].

## 4. Sizing formulas used in the reports
- **R2:** inverter kW = ΔkW × 1.15; battery kWh = ΔkW × 3.5 h / (0.85 DoD × 0.90 η × 0.90 SoH_EoL); capex RM1,200/kWh. Default (1,800 kW MD, 25% cut = 450 kW): 518 kW, 2,288 kWh, RM2,745,098, payback 4.0 yrs after 24% GITA (page placeholder shows 2.4 yrs). Note says "across the 8-hour weekday peak window" but code uses 3.5 h.
- **R3, R4, R8:** kWh = 2 × kW shaved (2-hour, 0.5C); full kW assumed shaved.
- **R5 (SELCO >1 MWac rule):** E_BESS ≥ 1 × PV kWp (kWh).
- **R8 zero-capex:** 2-hour LFP at RM2,300–2,900/kW.
- **R4 calculator:** RM1,800/kWh, 2-hour, net capex 60% after tax.
- **R9:** PCS kW = top 20%–35% of peak; energy = 1.3–1.5 × (kW × hours) buffer. R9's simulator takes "kW shaved" as an input and never sizes a battery. R9's case studies run ~2.0–3.1 kWh per kW of rating (§9).

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
| Automotive stamping (press spikes) | LVK 250 kW / 522 kWh case study [R3, R4]; Selangor stamping cluster [R4]; R9 Tier 1, score 95, LF 28%, 30–500 kW press inrush, 1.0–1.5 h [R9] |
| Plastic injection (heater bands, hydraulics) | R9 Tier 1, score 88, LF 55%, 30–45 min heater spikes + 18:00–22:00 solar drop-off spike [R9] |
| Food processing (batch ovens, retorts, blast freezers) | Plus Xnergy 20 MWh SELCO site (grain) [R4, R8]; R9 Tier 1, score 90, LF 42%, 45–90 min afternoon spikes [R9] |
| Office towers (chillers, 17:00–18:00 lift surge) | R9 Tier 1, score 92, LF 32%; load overlaps the window only 14:00–18:00; 2.0–2.5 h with PV [R9] |
| Malls, hotels, hospitals | R9 Tier 2 (scores 78 / 72 / 60); evening tails 17:30–21:30 (malls) and 15:30–21:30 (hotels); hospitals stack value with UPS/backup [R9] |
| Cold storage | R9 "Conditional (Tier 2/3)", LF 68%, 15%–25% afternoon hump; pre-cooling or solar + BESS [R9] |
| Shipbuilding / marine (cranes, welding) | HO Energy 4.3 MW / 8.36 MWh [R4]; Perak Lumut [R4] |
| Aerospace components | Elecod 1.5 MW / 2.60 MWh [R4] |
| Electronics (Penang) | ERS 200 kWh with 500 kWp solar, 35% MD cut [R8]; Penang 24/7 plants on ToU favour >1 MWac SELCO + BESS [R4]; R9: fabs/OSATs flat 24/7 (LF 85%, <8% diurnal variation) → "UPS / Solar ATAP Only", but precision automation vendors in BKIP/Perai are Tier 1 [R9] [C21] |
| Cement, foundry, gloves (Perak) | "High concentration of peaky motor and furnace loads" [R4]; R9: rubber gloves "extremely flat 24/7", LF 88%, "Unviable for Standalone BESS" [C21] |
| Textiles | R9: spinning/weaving flat 24/7 (poor); batch jet-dyeing houses spiky (Tier 1) [R9] |
| CNC, ovens, automated lines | Ride-through + MD shaving [R3]; overseas CNC case 250 kW / 515 kWh, 780 → 550 kW [R9] |
| Compressors, chillers | 10%–20% of MD shaving heuristic [R3]; TES for chillers [R2] |
| EV fast-charging hubs | PV + ESS + EV buffers [R3]; Gentari hub [R8] |
Full R9 sector table: §8. Case studies: §9. For a payback rule of thumb by "hours per day above target", see `../context/eternalgy_profile_and_analysis.md` (analysis, not from the reports).

## 8. Load profiles by industry (R9) [C21]
R9 is the only report built for this question (research prompt #4). Every figure below is unsourced, and the "MD share" column is an output of R9's own simulator (1,000 kW, no solar, MV ToU), not measured bills. Use it to choose which prospects to meter first, not to promise savings.
R9 rule: "High-power spiky loads with low load factors (LF < 0.60) offer maximum BESS returns, whereas flat 24/7 loads (LF > 0.75) require excessive storage capacity."
| Sector | R9 rating (score /100) | Load factor | MD share (modelled) | Shift pattern | Peak-window behaviour (14:00–22:00) | Spike drivers | Opt. BESS duration |
|---|---|---|---|---|---|---|---|
| Metal stamping | High, Tier 1 (95) | 28% | 59.5% | 1–2 shifts (07:00–23:00) | Jagged; sharp 30–60 min spikes 14:00–17:00 and 19:00–21:00 | Mechanical/servo press inrush (30–500 kW), spot welders, compressors | 1.0–1.5 h (0.5C–1C) |
| Office towers | High, Tier 1 (92) | 32% | 56.3% | Weekday day (08:00–18:00) | Trapezoidal block overlapping the window only 14:00–18:00; drops >75% after 18:00 | Chiller max loading (solar heat gain) + 17:00–18:00 lift surge | 2.0–2.5 h (with PV) |
| Food processing | High, Tier 1 (90) | 42% | 49.7% | Batch / 2-shift | Stepped batch plateaus; 45–90 min afternoon spikes 14:00–19:00 | Batch ovens, fryers, retort sterilisers, blast freezers, CIP | 1.5–2.0 h |
| Plastic injection | High, Tier 1 (88) | 55% | 43.1% | 2–3 shifts (24/5 or 24/7) | Elevated baseload, sharp 30–45 min heater spikes; evening solar drop-off spike 18:00–22:00 | Barrel heater bands at mould warm-up, hydraulic pumps, chillers | 1.5–2.0 h |
| Shopping malls | Moderate-High, Tier 2 (78) | 52% | 44.1% | Daily 10:00–22:00 | Broad 12-hr plateau; solar clips midday, steep evening cliff 17:30–21:30 | Central chiller plant, F&B cooking, tenant lighting, cinema | 2.0–3.0 h (evening tail) |
| Hotels & resorts | Moderate-High, Tier 2 (72) | 62% | 40.2% | 24/7 | Bimodal; late-afternoon/evening hump 15:30–21:30 | Check-in A/C surge, heat-pump hot water, laundry, banquet HVAC | 2.0–3.0 h |
| Hospitals | Moderate, Tier 2 (60) | 72% | 36.8% | 24/7 | High 24/7 baseload (60%) with daytime clinical plateau | OT chillers, CSSD autoclaves, MRI/CT | 1.5–2.0 h + microgrid (stack with UPS/backup) |
| Cold storage | Conditional, Tier 2/3 (55) | 68% | 38.2% | 24/7 | High baseload with 15%–25% afternoon thermal hump 14:00–18:00 | High condensing temperature, warm product at docks, defrost heaters | Pre-cooling or solar + BESS |
| Textiles & dyeing | Low (flat) / High (dyeing) (40) | 78% | 35.1% | 24/7 spinning/weaving | Flat for spinning; spiky afternoon for batch dyeing | Air-jet looms, ring frames; jet-dyeing autoclaves | Poor (weaving) / Tier 1 (dyeing) |
| E&E / semiconductor | Poor for standalone MD (25) | 85% | 33.2% | 24/7 cleanroom | Flat; <8% diurnal variation | Cleanroom MAUs/FFUs, ultra-pure water, chillers, IC test handlers | UPS / Solar ATAP only |
| Rubber gloves | Poor, flat 24/7 (15) | 88% | 32.5% | 24/7 continuous dipping | Extremely flat; stopping a line ruins in-process latex | Dipping-line conveyors, oven blowers, WWTP aerators | Unviable for standalone BESS |
Source: `../sources/R9_load_profile_analyzer.md` (E1). R9's tiers do not follow its LF rule exactly (plastic injection at 55% is Tier 1, malls at 52% Tier 2).
- Analysis note: on the rule of thumb in `../context/eternalgy_profile_and_analysis.md` §3 (no tax incentive: 1 h above target ≈ 1.6 yr payback, 2 h ≈ 3.2 yr, 4 h ≈ 6.4 yr), R9's Tier 1 durations of 1.0–2.5 h imply roughly 1.6–4 yr simple payback, and flat 24/7 loads land beyond 6 yr. This agrees with R9's ranking, but only a customer's 30-minute data shows the real hours above target.

## 9. BESS case studies (R9) [C17]
R9 calls these "published performance data"; none has a link or date. Three reuse figures from earlier AI reports and are **not independent evidence**.
| Case | Site | System | Demand cut | Savings claimed | Payback claimed | Evidence note |
|---|---|---|---|---|---|---|
| Livoltek evening peak suppression (Malaysia, MV ToU) | Factory with rooftop PV; shift to 22:00 after solar drops to 0 at 19:00 | 125 kW / 261 kWh LFP | 89.99 kW | RM9,000/month (>RM95,000/yr) | 2.8–3.5 yrs with GITA | 89.99 × 97.06 = RM8,734/month |
| Plus Xnergy zero-capex EaaS (Malaysia, MV ToU) | Large plant | 1.5 MW / 3.0 MWh | 1,478 kW (3,900 → 2,422 kW) | Client nets RM21,520/month (pays RM82.50/kW vs RM97.06; gross MD cut RM143,455/month), 15 years | 0 (EaaS) | **Same figures as R8's illustrative example** |
| Solarvest Solar ATAP + BESS reference site | MV C&I facility | 1,000 kWp + 500 kW / 1,000 kWh | >650 kW (>65%) | RM712,000/yr gross | <2.5 yrs (RM2.4M less RM920k GITA) | >650 kW from a 500 kW BESS needs ≥150 kW from PV; RM920k = 38.3% of capex |
| Avera Energy MV General → ToU | 500,000 kWh/month plant | Rooftop solar + 165 kW / 330 kWh | 315 kW (150 kW shift optimisation + 165 kW BESS) | RM58,945/month (25.7% bill cut) | 3.0–4.2 yrs | **Same RM and % as R3's simulator placeholder** for a 500,000 kWh/month factory |
| UniBess modular peak shaving | MV factory, 600 kW spikes | 500 kW / 1,044 kWh (4 × 125 kW cabinets) | "400 kW shaved (Capped at 200 kW target)" | RM38,824/month (RM465,888/yr) | 2.5–3.5 yrs | **Same as R1's hard-coded simulator result**; 400 vs 200 kW self-contradictory |
| Predictive HAPLT controller field trial | Industrial sub-load feeder | 50 kW / 155 kWh (139.5 kWh usable) | "89% Average MD Reduction Factor" | RM2,445/month | Academic trial | CNN/LSTM/XGBoost forecasting kept charge for the critical peaks |
| Precision CNC machining plant (overseas ToU market) | Machining + compressors | 250 kW / 515 kWh LFP | 230 kW (780 → 550 kW) | US$5,520/month (~RM295,000/yr) | 2.1 yrs | No location or tariff |
Lessons the cases illustrate (R9's details): evening shifts after solar drops out set the MD (Livoltek); EMS caps grid import at a preset threshold in the 14:00–22:00 window (UniBess, CNC); forecasting avoids draining the battery on early-afternoon humps (HAPLT); tariff switch and shift changes cut MD alongside BESS (Avera).
