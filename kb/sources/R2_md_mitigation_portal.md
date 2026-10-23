---
id: R2
title: "Malaysia TNB Maximum Demand & C&I Mitigation Intelligence Portal"
source_file: malaysia_tnb_maximum_demand_c_i_mitigation_portal.html
source_modified: 2026-10-23 14:15
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js)
research_prompt: none (first-round report the user ran before our research prompts)
stated_scope: "Comprehensive technical analysis of Peninsular Malaysia's RP4 unbundled tariff architecture, 30-minute integration mathematics, and behind-the-meter mitigation engineered for Commercial and Industrial (C&I) facilities. Header badges: RP4 Regulatory Period (1 July 2025 – 31 Dec 2027); Malaysia Electricity Reform. HTML comment: interactive executive intelligence portal for C&I C-Suite, Energy Managers, and Plant Engineers."
stated_sources: "Based on official Energy Commission (*Suruhanjaya Tenaga*) RP4 Tariff Schedules (1 July 2025 – 31 Dec 2027), EECA 2024 (Act 861), and Budget 2027 GITA Framework. Built for engineering and executive analysis. | Malaysia TNB Maximum Demand & C&I Mitigation Intelligence Portal © 2026"
as_of: "No report date stated. Footer © 2026. RP4 period 1 July 2025 – 31 Dec 2027; EECA 2024 enforced 1 Jan 2025; Budget 2027 GITA: BESS & Solar+BESS Tier 1 through 31 Dec 2030, standalone EE assets removed effective 1 Jan 2027 (CapEx incurred and submitted to MGTC on/before 31 Dec 2026)."
sections: ["Header & RP4 MD Tariff Hike stat box", "Sticky navigation", "Section 1: The Regulatory Period 4 (RP4) Paradigm Shift", "Section 2: Physics & Mathematical Formulation of TNB MD", "Section 3: C&I Maximum Demand Reduction & BESS ROI Estimator", "Section 4: Comprehensive C&I MD Mitigation Solutions", "Section 5: EECA 2024 & Budget 2027 Green Tax Catalysts", "Section 6: Phased C&I Execution Roadmap", "Footer"]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R2 — Malaysia TNB Maximum Demand & C&I Mitigation Intelligence Portal

> Faithful, complete markdown extract of `malaysia_tnb_maximum_demand_c_i_mitigation_portal.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- RP4 (Regulatory Period 4) took effect 1 July 2025 and governs Peninsular Malaysia tariffs through 31 December 2027; it abolished legacy activity-based tariff codes in favour of voltage-categorised Non-Domestic accounts (LV, MV, HV). (Section 1)
- Maximum Demand (MD) charges are unbundled into a Capacity Charge plus a Network Charge: MV General RM29.43 + RM59.84 = RM89.27/kW; MV ToU RM30.19 + RM66.87 = RM97.06/kW; HV General RM16.68 + RM14.53 = RM31.21/kW; HV ToU RM21.76 + RM23.06 = RM44.82/kW; LV is volumetric (8.83 + 14.82 sen/kWh, "Bundled in kWh"). (Section 1 table)
- Header stat: "RP4 MD Tariff Hike +100% to +202%"; legacy bundled MD charges were RM30.30–RM45.10/kW; Section 1 says MD charges rose "by up to 202%". (Header, Section 1)
- ToU peak window compressed from the legacy 14-hour block (08:00–22:00) to 8 hours, 14:00–22:00 weekdays only; off-peak = 128 hours/week (76.2%). Monthly Automatic Fuel Adjustment (AFA) replaced the 6-month ICPT cycle. (Section 1)
- TNB MD = twice the largest kWh imported in any 30-minute block of the month (1,440 blocks per 30-day month); one 2,000 kWh block sets 4,000 kW = RM388,240/month on MV ToU. (Section 2)
- Power factor surcharge applies below 0.85 (LV/MV) or 0.90 (HV): 1.5% per 0.01 drop down to 0.75, plus 3.0% per 0.01 below 0.75. (Section 2)
- Switching MV General to MV ToU costs RM7.79/kW/month more in demand; break-even inequality E_total × (0.0409 × α − 0.0149) + 89.27 × MD_24h − 97.06 × MD_peak > 0; with unchanged peak, α > 36.43% + (190.46 × MD / E_total) (example: 500k kWh/mo, 1,000 kW needs > 74.5% off-peak); or a peak-window reduction > 8.03% (MD_peak < 0.9197 × MD_24h) makes ToU profitable. (Section 4, tab 1)
- PLC staggering of three 50 kW compressors saves 150 kW = RM 14,559/month on MV ToU. (Section 4, tab 2)
- Standalone solar PV "fails to guarantee" MD reduction (cloud transients; 18:00–22:00 dark peak); solar + BESS caps grid demand (chart: 1,200 kW standalone-solar peak vs 750 kW cap with BESS); SMP export value RM0.1881/kWh. (Section 4, tab 4)
- Central chillers are up to 60% of peak demand in commercial complexes, hospitals and cleanroom factories; TNB offers an MV TES tariff schedule. (Section 4, tab 5)
- EECA 2024 (Act 861), enforced 1 Jan 2025: ≥ 21,600 GJ over 12 months (~500,000 kWh/month, ~RM200k/month bill) = Regulated Energy Consumer; 21,600–50,000 GJ/yr → REM Class 1; ≥ 50,000 GJ/yr → REM Class 2; fines up to RM100,000. (Section 5)
- Budget 2027 GITA: BESS and Solar+BESS keep Tier 1 (100% ITA against 70% Statutory Income) through 31 Dec 2030, "~24% CapEx cash tax reduction"; standalone EE assets (VSDs, BMS, Chillers) removed effective 1 Jan 2027, CapEx to be incurred and submitted to MGTC on/before 31 Dec 2026. (Section 5)
- ROI estimator at defaults (MV ToU, 1,800 kW, 25% reduction): RM 43,677/month, RM 524,124/year, 518 kW AC inverter; the page's static placeholder shows 2.4 years payback / 1,825 kWh / RM 1,642,500, but the code computes 4.0 years / 2,288 kWh / RM 2,745,098. (Section 3)
- 12-month, 4-phase roadmap; Phase 3 claims Tier 1 GITA can "compress payback to 2–3 years". (Section 6)

## Report header, navigation and authoring comments

### Header banner

- Badge: "RP4 Regulatory Period (1 July 2025 – 31 Dec 2027)"
- Badge: "Malaysia Electricity Reform" (with Malaysian flag emoji)
- Title (H1): "TNB Maximum Demand Charges & C&I Mitigation Intelligence"
- Subtitle: "Comprehensive technical analysis of Peninsular Malaysia's RP4 unbundled tariff architecture, 30-minute integration mathematics, and behind-the-meter mitigation engineered for Commercial and Industrial (C&I) facilities."
- Stat box:
  - Label: "RP4 MD Tariff Hike"
  - Value: "+100% to +202%"
  - Caption: "Unbundled Capacity & Network Charges up to RM97.06/kW"

### Sticky navigation (in order)

1. "1. RP4 Tariff Architecture" → #rp4-paradigm
2. "2. MD Mathematics & Surcharges" → #physics-math
3. "Dynamic Savings Calculator" (gear icon, no number) → #roi-calculator
4. "4. C&I Mitigation Solutions" → #mitigation-solutions
5. "5. EECA 2024 & GITA Incentives" → #eeca-gita
6. "6. Execution Roadmap" → #roadmap

### Authoring comments in the HTML (not visible on the page)

- Palette comment: "Chosen Palette: Warm Neutral / Executive Slate & Tech Amber" (colour codes only; styling).
- "Application Structure Plan" — intended audience and purpose: "Designed as an interactive executive intelligence portal for C&I C-Suite, Energy Managers, and Plant Engineers". Planned structure (verbatim list):
  1. Executive Header & Dynamic Stat Ticker (RP4 Highlights, Tariff Rebalance Metrics).
  2. Sticky Section Navigation bar.
  3. Section 1: RP4 Tariff Paradigm Shift (Interactive Rate Comparison Table & Demand Unbundling Breakdown).
  4. Section 2: Mathematical Formulation & Physics of MD (Interactive 30-Min Integrator Simulator & Power Factor Surcharge Calculator).
  5. Section 3: C&I Interactive MD Savings & BESS ROI Calculator (Live dynamic scenario modeling with GITA tax shields).
  6. Section 4: Comprehensive Mitigation Solutions Matrix (Interactive deep dive tabs covering 6 C&I engineering solutions).
  7. Section 5: Regulatory Navigator (EECA 2024 Threshold Assessment & Budget 2027 GITA Transition Timeline).
  8. Section 6: Phased Actionable Implementation Roadmap.
  - Closing line: "This structure translates complex engineering formulas and regulatory shifts into visual, actionable decision tools."
- "Visualization & Content Choices" (verbatim bullets):
  - RP4 Demand Rate Comparison: Interactive Data Table & Dynamic Bar Chart (Chart.js) comparing LV, MV, HV General vs ToU rates.
  - 30-Min Integration Mechanics: Chart.js Line Chart displaying a simulated 24-hour 30-minute block interval curve with peak window highlight (14:00-22:00).
  - Solar PV vs Solar+BESS Curve: Dual-line Chart.js chart showing cloud transient voltage sag and evening peak shaving.
  - Interactive BESS & Tariff ROI Calculator: JS engine calculating monthly demand savings, BESS inverter (kW) & capacity (kWh) sizing, and GITA 100% ITA payback.
  - Confirmation: NO SVG elements used. NO Mermaid JS used. All visual indicators use CSS badges, Unicode, and Chart.js HTML5 Canvas.
- Separate comment: "CONFIRMATION: NO SVG graphics used. NO Mermaid JS used."

## 1. The Regulatory Period 4 (RP4) Paradigm Shift

Section label: "Section 1". Context paragraph (verbatim; the asterisks are literal in the HTML):

> Context & Overview: On 1 July 2025, \*Suruhanjaya Tenaga\* (Energy Commission) and Tenaga Nasional Berhad (TNB) implemented Regulatory Period 4 (RP4), governing Peninsular Malaysia's electricity tariffs through 31 December 2027. RP4 abolished legacy activity-based tariff codes (Tariffs B, C1, C2, D, E1, E2, E3) in favor of voltage-categorized Non-Domestic accounts (Low Voltage, Medium Voltage, High Voltage). This section explores how RP4 rebalanced utility cost recovery by slashing per-kWh energy rates while dramatically elevating Maximum Demand (kW) charges by up to 202%.

### Key Pillars of the RP4 Tariff Rebalancing

- **Unbundled Capacity & Network Charges:** Legacy bundled MD charges (RM30.30–RM45.10/kW) were replaced by two separate grid infrastructure components: a *Capacity Charge* (generation reserve reservation) and a *Network Charge* (transmission/distribution line capacity), pushing Medium Voltage peak demand rates to **RM89.27/kW** (General) and **RM97.06/kW** (Time-of-Use).
- **Compressed Weekday Peak Window (14:00 – 22:00):** RP4 compressed the ToU Peak Period from the legacy 14-hour block (08:00–22:00) down to an 8-hour window on weekdays only. Off-peak hours now encompass 128 hours per week (76.2% of all hours), including the entire 08:00–14:00 morning shift and all weekend hours.
- **Monthly Automatic Fuel Adjustment (AFA):** Replaced the legacy 6-month ICPT cycle with a dynamic monthly fuel pass-through, transferring global coal/gas price fluctuations directly onto monthly C&I energy bills.

### Chart 1 (see Charts): "RP4 Unbundled Demand Charge Comparison (RM/kW/month)" — subtitle "Excludes 1.6% KWTBB Levy"

### RP4 Tariff Master Reference Table

| RP4 Tariff Category | Legacy Equivalent | Supply Voltage | Energy Rate (sen/kWh) | Capacity Charge | Network Charge | Total MD Rate (RM/kW) | MD Assessment Window |
|---|---|---|---|---|---|---|---|
| LV General Non-Domestic | Tariff B, D, F | ≤ 1 kV (400V) | 27.03 | 8.83 sen/kWh | 14.82 sen/kWh | Bundled in kWh | N/A (Volumetric) |
| LV Time-of-Use (ToU) | Tariff B, D (ToU) | ≤ 1 kV (400V) | 28.52 Peak / 24.43 Off-Peak | 8.83 sen/kWh | 14.82 sen/kWh | Bundled in kWh | N/A (Volumetric) |
| MV General Non-Domestic | Tariff C1, E1, F1 | >1 kV to ≤50 kV | 29.83 | RM29.43 / kW | RM59.84 / kW | RM89.27 / kW | 24 Hours / All Days |
| MV Time-of-Use (ToU) | Tariff C2, E2, F2 | >1 kV to ≤50 kV | 31.32 Peak / 27.23 Off-Peak | RM30.19 / kW | RM66.87 / kW | RM97.06 / kW | 14:00–22:00 Weekdays Only |
| HV General Non-Domestic | Tariff C3 | >50 kV to ≤230 kV | 43.03 | RM16.68 / kW | RM14.53 / kW | RM31.21 / kW | 24 Hours / All Days |
| HV Time-of-Use (ToU) | Tariff C4, E3 | >50 kV to ≤230 kV | 44.52 Peak / 40.43 Off-Peak | RM21.76 / kW | RM23.06 / kW | RM44.82 / kW | 14:00–22:00 Weekdays Only |

(The MV rows and the "Total MD Rate (RM/kW)" column are visually highlighted in the report.)

## 2. Physics & Mathematical Formulation of TNB MD

Section label: "Section 2". Context paragraph (verbatim):

> Context & Mathematical Mechanics: TNB does not bill Maximum Demand on instantaneous microsecond current spikes or motor starting inrush currents. Instead, TNB defines Maximum Demand as *twice the largest active energy (kWh) imported during any consecutive 30-minute block* in the billing month. This section presents the exact mathematical formulas governing interval demand, power factor penalties, and peak window integration.

### Governing formulas (three cards)

**Card 1 — "1. 30-Min Interval Integration"**

- Formula (HTML subscripts shown as `_`): `D_i (kW) = 2 × E_i (kWh)`
- Text, raw as written in the HTML (LaTeX not rendered): "In any 30-minute block $i$ ($t = 0.5\text{ h}$), active energy $E_i = M_{\text{end}} - M_{\text{start}}$ is integrated. Multiplying by 2 converts 0.5-hour energy into average active power demand in kW."
- Plain-text version: In any 30-minute block i (t = 0.5 h), active energy E_i = M_end − M_start is integrated. Multiplying by 2 converts 0.5-hour energy into average active power demand in kW.
- Footer line: "1,440 blocks per 30-day billing month"

**Card 2 — "2. Monthly Billed MD Lock-In"**

- Formula: `MD_billed = max_{i ∈ W} (2 × E_i)`
- Text, raw: "TNB scans all assessment blocks $W$. A single 30-minute interval where consumption reaches $2,000\text{ kWh}$ sets a $4,000\text{ kW}$ demand charge ($\text{RM}388,240/\text{month}$ on MV ToU) for the entire billing cycle."
- Plain-text version: TNB scans all assessment blocks W. A single 30-minute interval where consumption reaches 2,000 kWh sets a 4,000 kW demand charge (RM388,240/month on MV ToU) for the entire billing cycle.
- Footer line: "W = 14:00–22:00 weekdays for ToU"

**Card 3 — "3. Power Factor Surcharge Formula"**

- Formula (HTML uses √ and superscript ²): `PF = kWh / √(kWh² + kVArh²)`; plain: PF = kWh / sqrt(kWh^2 + kVArh^2)
- Text, raw: "If monthly average PF drops below $0.85$ (LV/MV) or $0.90$ (HV), TNB levies a penalty: $1.5\%$ surcharge per $0.01$ drop down to $0.75$, plus $3.0\%$ per $0.01$ below $0.75$."
- Plain-text version: If monthly average PF drops below 0.85 (LV/MV) or 0.90 (HV), TNB levies a penalty: 1.5% surcharge per 0.01 drop down to 0.75, plus 3.0% per 0.01 below 0.75.
- Footer line: "Threshold: 0.85 (LV/MV), 0.90 (HV)"

### Interactive 30-Minute Interval Load & Demand Simulator

- Subtitle: "Adjust energy consumption in a 30-minute block to observe how instant active power dictates monthly MD billing."
- Input: "30-Min Energy Import (E_i):" [number] kWh — default 500 (full logic in Calculators section A).
- Output cards (static placeholder text in the HTML): "30-Min Energy (E_i)" = 500 kWh; "Recorded MD (2 × E_i)" = 1,000 kW; "MV General MD Cost" = RM 89,270.00; "MV ToU MD Cost (Peak)" = RM 97,060.00.
- Chart 2 (see Charts): "Simulated 24-Hour Load Profile & RP4 Weekday ToU Peak Window (14:00 – 22:00)".

## 3. C&I Maximum Demand Reduction & BESS ROI Estimator

Section label: "Section 3"; tag: "Fully Dynamic Simulation Engine". Intro (verbatim):

> Executive Planning Tool: Configure your facility's energy parameters below to simulate monthly demand charge reductions, optimal behind-the-meter Battery Energy Storage System (BESS) sizing (kW / kWh), Green Investment Tax Allowance (GITA) tax shields, and estimated capital payback period.

### Inputs panel — "1. Facility Operational Parameters"

- "Select RP4 Tariff Category:" dropdown — Medium Voltage General (RM89.27 / kW); Medium Voltage ToU (RM97.06 / kW) [selected]; High Voltage ToU (RM44.82 / kW).
- "Monthly Energy Consumption (kWh):" number, default 600000.
- "Current Unmitigated Peak Demand (kW):" slider, default 1,800 kW.
- "Target Peak MD Reduction Goal (%):" slider, default "25% (450 kW)".
- "GITA Asset Tax Allowance Status:" dropdown — "Tier 1: 100% Investment Tax Allowance (BESS & Solar+BESS)"; "No Tax Incentives Applied".

### Outputs panel

Summary cards (static placeholder text in the HTML, before the script runs):

| Card | Placeholder main value | Placeholder sub-line |
|---|---|---|
| Monthly MD Savings | RM 43,677 | RM 524,124 / year |
| Estimated BESS Payback (Net CapEx) | 2.4 Years | Includes 24% GITA Corporate Tax Shield |

"Recommended BESS System Sizing Specifications" (placeholder text):

| Field | Placeholder |
|---|---|
| Required Inverter Power | 518 kW AC |
| Nominal Battery Capacity | 1,825 kWh |
| Gross Turn-Key CapEx | RM 1,642,500 |

Sizing footnote, raw as written (LaTeX not rendered):

> *BESS sizing factors in an engineering safety factor ($k_s = 1.15$), $85\%$ Depth of Discharge ($\text{DoD}$), $90\%$ round-trip efficiency ($\eta_{\text{dis}}$), and $90\%$ State of Health ($\text{SoH}_{\text{EoL}}$) across the 8-hour weekday peak window.

Plain-text version: BESS sizing factors in an engineering safety factor (k_s = 1.15), 85% Depth of Discharge (DoD), 90% round-trip efficiency (η_dis), and 90% State of Health (SoH_EoL) across the 8-hour weekday peak window.

Chart 4 (see Charts): "10-Year Cumulative Cash Flow Projection (CapEx vs Cumulative Savings)".

The values the code actually displays at load are in Calculators section B.

## 4. Comprehensive C&I MD Mitigation Solutions

Section label: "Section 4". Intro (verbatim):

> Engineering & Operational Hierarchy: Reducing TNB Maximum Demand charges requires a structured progression ranging from zero-CapEx tariff arbitrage and operational scheduling to software-driven automated load shed, solar-plus-storage integration, and thermal decoupling. Select a solution tab below to explore technical mechanics, mathematical break-evens, and optimal facility profiles.

Tabs (tab 1 is shown by default; tabs 2–5 are hidden until clicked): "1. Tariff Arbitrage Math", "2. Operational DSM", "3. Granular EMS & Load Shed", "4. Solar PV vs Solar + BESS", "5. Thermal Storage (TES)".

### Tab 1 — Tariff Arbitrage Math: "Zero-CapEx Tariff Switch: MV General vs MV ToU Decision Boundary"

Text, raw: "Switching from Medium Voltage General (RM89.27/kW) to Medium Voltage ToU (RM97.06/kW) introduces a demand penalty of RM7.79/kW/month. To justify the switch, the off-peak energy savings ($2.60\text{ sen/kWh}$ discount) or demand reduction outside 14:00–22:00 must outweigh this differential."

Plain: ... the off-peak energy savings (2.60 sen/kWh discount) or demand reduction outside 14:00–22:00 must outweigh this differential.

**Governing C&I Arbitrage Inequality** (HTML subscripts shown as `_`):

`E_total × (0.0409 × α - 0.0149) + 89.27 × MD_24h - 97.06 × MD_peak > 0`

**Scenario A: Unchanged Peak Location (α constraint)**

- Text, raw: "If peak demand cannot be shifted out of the 14:00–22:00 window ($\text{MD}_{\text{peak}} = \text{MD}_{24\text{h}}$), the facility must consume at least **α > 36.43% + (190.46 × MD / E_total)** of its energy during off-peak hours to break even."
- Plain condition: MD_peak = MD_24h; break-even α > 36.43% + (190.46 × MD / E_total).
- Example box: "Example: 500k kWh/mo with 1,000 kW peak requires > 74.5% off-peak energy share."

**Scenario B: Peak Demand Shifted Outside Peak Window**

- Text, raw: "If process rescheduling reduces peak demand during 14:00–22:00 by just **> 8.03%** relative to morning/night demand ($\text{MD}_{\text{peak}} < 0.9197 \times \text{MD}_{24\text{h}}$), ToU becomes immediately profitable even at neutral energy splits."
- Plain condition: MD_peak < 0.9197 × MD_24h (peak-window reduction > 8.03%).
- Box: "Immediate savings on all morning & weekend demand spikes (billed at RM0/kW)."

### Tab 2 — Operational DSM: "Operational Demand-Side Management & Process Sequencing"

- Intro: "Operational DSM eliminates simultaneous concurrency of high-draw machinery during the 14:00–22:00 weekday peak window without requiring capital-intensive energy storage assets."
- **1. Morning Shift Pull-Down (06:00 – 14:00):** "Because electricity demand recorded prior to 14:00 carries zero MD charge on RP4 ToU, batch furnaces, autoclaves, extruders, and thermal pull-downs should be scheduled between 06:00 and 13:30, transitioning to low-draw holding modes before 14:00."
- **2. Hard-Wired PLC Motor Staggering:** raw: "Configure Programmable Logic Controllers (PLCs) with mutual-exclusion interlocks. Preventing three $50\text{ kW}$ air compressors from starting together in the same 30-min block saves $150\text{ kW}$, yielding **RM 14,559/month** in MD savings on MV ToU." Plain: three 50 kW air compressors; saves 150 kW; RM 14,559/month on MV ToU.

### Tab 3 — Granular EMS & Load Shed: "3-Tier EMS Architecture & Real-Time Trajectory Prediction"

- Intro: "Manual operational discipline fails over time. Deploying real-time Energy Management Systems (EMS) synchronized with TNB's 30-minute integration windows prevents accidental peak lock-ins through predictive algorithms."
- **Real-Time Interval Peak Projection Formula** (verbatim): `D_projected (kW) = 2 × [ E(t_e) + P_inst × ((30 - t_e) / 60) ]`
- Explanation, raw: "Where $t_e$ is elapsed interval minutes, $E(t_e)$ is cumulative kWh, and $P_{\text{inst}}$ is live kW draw. If projected demand exceeds target MD, the EMS automatically sheds non-critical AHUs or unloads chillers for 15 minutes."
- Plain: t_e = elapsed interval minutes; E(t_e) = cumulative kWh; P_inst = live kW draw. If projected demand exceeds target MD, the EMS sheds non-critical AHUs or unloads chillers for 15 minutes.

### Tab 4 — Solar PV vs Solar + BESS: "Solar PV vs. Solar + BESS: Overcoming the Cloud Transient & Evening Peak Trap"

- Text (verbatim): "Standalone rooftop Solar PV fails to guarantee Maximum Demand reduction on MV/HV tariffs due to afternoon cloud transients (sudden solar drops) and the 18:00–22:00 dark peak. Pairing solar with BESS secures peak shaving and avoids cheap SMP export loss (RM0.1881/kWh)."
- Chart 3 (see Charts): "Cloud Transient & Evening Dark Peak Comparison: Standalone Solar vs. Solar + BESS".

### Tab 5 — Thermal Storage (TES): "Thermal Energy Storage (TES) & Dedicated TES Tariff Optimization"

- Text (verbatim): "For commercial complexes, hospitals, and cleanroom factories, central chillers represent up to 60% of peak electrical demand. TES systems freeze ice or chill water during off-peak overnight hours (22:00–14:00) and discharge cooling during the 14:00–22:00 weekday window, enabling chiller compressors to shut down during high-tariff periods."
- **TNB Dedicated MV TES Tariff Incentive:** "Qualifying facilities utilizing thermal storage can apply for TNB's Medium Voltage TES tariff schedule, permanently shielding chiller compressor kilowatts from weekday peak demand surcharges."

## 5. EECA 2024 & Budget 2027 Green Tax Catalysts

Section label: "Section 5". Intro (verbatim):

> Regulatory & Fiscal Alignment: C&I demand mitigation investments intersect directly with Malaysia's mandatory energy efficiency legislation and federal tax allowances. This section breaks down compliance requirements under the Energy Efficiency and Conservation Act 2024 (EECA 2024) and the strategic GITA transition window.

### Box 1 — "1. EECA 2024 (Act 861) Mandatory Compliance" — badge "Enforced 1 Jan 2025"

- "Any commercial or industrial facility consuming **≥ 21,600 Gigajoules (GJ)** of combined energy over 12 consecutive months (~500,000 kWh/month or ~RM200k/month electricity bill) is legally classified as a Regulated Energy Consumer."

| Annual energy (GJ/yr) | Equivalent (kWh/year) | Requirement |
|---|---|---|
| 21,600 GJ to 50,000 GJ/yr | 6.0M to 13.9M kWh/year | Appoint REM Class 1 |
| ≥ 50,000 GJ/yr | > 13.9M kWh/year | Appoint REM Class 2 |

- Footnote: "*Non-compliance carries statutory fines up to RM100,000 under Energy Commission enforcement."

### Box 2 — "2. GITA Asset Tax Shield Transition" — badge "Budget 2027 Shift"

- "Budget 2027 restructured the Green Investment Tax Allowance (GITA). BESS and integrated solar storage maintain Tier 1 status through 2030, while standalone energy efficiency equipment loses eligibility after 31 Dec 2026."

| Asset class | Status (verbatim) |
|---|---|
| Battery Storage (BESS) & Solar+BESS | Maintained Tier 1: 100% ITA against 70% Statutory Income through 31 Dec 2030. Yields ~24% CapEx cash tax reduction. |
| Standalone EE Assets (VSDs, BMS, Chillers) | REMOVED from GITA effective 1 Jan 2027. CapEx must be incurred and submitted to MGTC on/before 31 Dec 2026. |

## 6. Phased C&I Execution Roadmap

Section label: "Section 6". Intro (verbatim):

> Implementation Playbook: Recommended 12-month engineering and financial action plan for C&I facility management teams to capture maximum RP4 bill savings and lock in federal green tax allowances.

| Phase | Timing | Title | Actions (verbatim) |
|---|---|---|---|
| Phase 1 | Days 1–30 | Interval Data Audit & Tariff Arbitrage | Download 12 months of half-hourly smart meter CSV data. Calculate Demand Factor, Load Factor, and apply the C&I ToU Arbitrage equation. |
| Phase 2 | Days 30–90 | DSM Sequencing & EMS Deployment | Reprogram morning shift startup cycles. Install a 3-tier EMS with automated 30-min MD predictive load shedding. |
| Phase 3 | Months 3–9 | BESS & Solar Storage Integration | Deploy AI-sized BESS behind the meter. Apply for Tier 1 GITA 100% ITA tax allowance with MGTC to compress payback to 2–3 years. |
| Phase 4 | Months 6–12 | EECA Institutionalization & TES | Appoint certified REM Class 1/2. Submit annual EECR report to Suruhanjaya Tenaga and evaluate Thermal Storage for HVAC loads. |

## Footer

- "Malaysia TNB Maximum Demand & C&I Mitigation Intelligence Portal © 2026"
- "Based on official Energy Commission (\*Suruhanjaya Tenaga\*) RP4 Tariff Schedules (1 July 2025 – 31 Dec 2027), EECA 2024 (Act 861), and Budget 2027 GITA Framework. Built for engineering and executive analysis."

## Charts

### Chart 1 — RP4 Unbundled Demand Charge Comparison

- Location: Section 1 (canvas `rp4RatesChart`).
- Title: "RP4 Unbundled Demand Charge Comparison (RM/kW/month)"; subtitle "Excludes 1.6% KWTBB Levy".
- Type: stacked bar (x and y stacked); legend at bottom.
- X axis: categories (no axis title). Y axis title: "Rate (RM / kW / month)", begins at zero.
- Tooltip: index mode; each line = `<series label>: RM <value to 2 decimals>`.

| Label | Capacity Rate (RM/kW) | Network Rate (RM/kW) | Stack total |
|---|---|---|---|
| LV General | 0 | 0 | 0 |
| MV General | 29.43 | 59.84 | 89.27 |
| MV ToU (Peak) | 30.19 | 66.87 | 97.06 |
| HV General | 16.68 | 14.53 | 31.21 |
| HV ToU (Peak) | 21.76 | 23.06 | 44.82 |

(Stack totals are the sum of the two series and equal the "Total MD Rate" column of the Section 1 table.)

### Chart 2 — Simulated 24-Hour Load Profile & RP4 Weekday ToU Peak Window

- Location: Section 2, inside the Interactive 30-Minute Interval Load & Demand Simulator (canvas `intervalProfileChart`).
- Title: "Simulated 24-Hour Load Profile & RP4 Weekday ToU Peak Window (14:00 – 22:00)".
- Type: line, filled; one series "30-Min Interval Active Power (kW)"; legend hidden.
- X axis: 48 half-hour labels 00:00, 00:30 … 23:30 (no axis title; auto-skipped ticks). Y axis title: "Power Demand (kW)", begins at zero.
- Tooltip: "Demand: {kW} kW ({kW/2, 0 decimals} kWh)".
- Code comment: "Background color array for RP4 Peak Window (Intervals 28 to 43 = 14:00 to 22:00)". The colour array is computed but never attached to the chart (see Extraction notes).
- Array comments in the code group the values as "00:00 - 08:00" (16 values), "08:00 - 12:00" (8), "12:00 - 20:00" (16), "20:00 - 24:00" (8).
- Interactivity: the simulator overwrites index 27 (13:30) with the user's 2 × E_i (see Calculators A).

| Index | Label | Demand (kW) | Tooltip kWh (kW/2) | In code's peak-window range (28–43) |
|---|---|---|---|---|
| 0 | 00:00 | 250 | 125 | No |
| 1 | 00:30 | 240 | 120 | No |
| 2 | 01:00 | 230 | 115 | No |
| 3 | 01:30 | 220 | 110 | No |
| 4 | 02:00 | 220 | 110 | No |
| 5 | 02:30 | 230 | 115 | No |
| 6 | 03:00 | 350 | 175 | No |
| 7 | 03:30 | 450 | 225 | No |
| 8 | 04:00 | 600 | 300 | No |
| 9 | 04:30 | 650 | 325 | No |
| 10 | 05:00 | 700 | 350 | No |
| 11 | 05:30 | 750 | 375 | No |
| 12 | 06:00 | 780 | 390 | No |
| 13 | 06:30 | 800 | 400 | No |
| 14 | 07:00 | 780 | 390 | No |
| 15 | 07:30 | 750 | 375 | No |
| 16 | 08:00 | 800 | 400 | No |
| 17 | 08:30 | 850 | 425 | No |
| 18 | 09:00 | 880 | 440 | No |
| 19 | 09:30 | 900 | 450 | No |
| 20 | 10:00 | 870 | 435 | No |
| 21 | 10:30 | 850 | 425 | No |
| 22 | 11:00 | 820 | 410 | No |
| 23 | 11:30 | 800 | 400 | No |
| 24 | 12:00 | 820 | 410 | No |
| 25 | 12:30 | 850 | 425 | No |
| 26 | 13:00 | 880 | 440 | No |
| 27 | 13:30 | 1000 | 500 | No |
| 28 | 14:00 | 950 | 475 | Yes |
| 29 | 14:30 | 900 | 450 | Yes |
| 30 | 15:00 | 880 | 440 | Yes |
| 31 | 15:30 | 850 | 425 | Yes |
| 32 | 16:00 | 820 | 410 | Yes |
| 33 | 16:30 | 800 | 400 | Yes |
| 34 | 17:00 | 780 | 390 | Yes |
| 35 | 17:30 | 750 | 375 | Yes |
| 36 | 18:00 | 700 | 350 | Yes |
| 37 | 18:30 | 680 | 340 | Yes |
| 38 | 19:00 | 650 | 325 | Yes |
| 39 | 19:30 | 600 | 300 | Yes |
| 40 | 20:00 | 500 | 250 | Yes |
| 41 | 20:30 | 450 | 225 | Yes |
| 42 | 21:00 | 400 | 200 | Yes |
| 43 | 21:30 | 350 | 175 | Yes |
| 44 | 22:00 | 300 | 150 | No |
| 45 | 22:30 | 280 | 140 | No |
| 46 | 23:00 | 260 | 130 | No |
| 47 | 23:30 | 250 | 125 | No |

### Chart 3 — Cloud Transient & Evening Dark Peak Comparison

- Location: Section 4, Tab 4 (canvas `solarBessChart`).
- Title: "Cloud Transient & Evening Dark Peak Comparison: Standalone Solar vs. Solar + BESS".
- Type: line, two series; legend at bottom. Standalone-solar series is dashed (dash 5, 5); BESS series filled.
- X axis: 9 category labels (no axis title). Y axis title: "Grid Demand (kW)", begins at zero.

| Label | Grid Demand with Standalone Solar PV (kW) | Grid Demand with Solar PV + BESS Peak Shaving (kW) |
|---|---|---|
| 08:00 | 400 | 400 |
| 10:00 | 300 | 300 |
| 12:00 | 250 | 250 |
| 14:00 (ToU Peak Starts) | 450 | 450 |
| 15:00 (Cloud Sag) | 1100 | 750 |
| 17:00 | 800 | 750 |
| 19:00 (Dark Peak) | 1200 | 750 |
| 21:00 | 1000 | 750 |
| 22:00 | 600 | 600 |

Tooltip extra text (shown after the values):

- On a label containing "Cloud Sag": "Cloud Transient: Standalone Solar output drops, causing full 1100 kW grid draw."
- On a label containing "Dark Peak": "Dark Evening Peak: Solar output = 0 kW. BESS discharges to cap grid demand at 750 kW."
- Other labels: no extra text.

### Chart 4 — 10-Year Cumulative Cash Flow Projection

- Location: Section 3 (canvas `cashflowChart`).
- Title: "10-Year Cumulative Cash Flow Projection (CapEx vs Cumulative Savings)".
- Type: line, filled; one series "Net Cumulative Cash Flow (RM)"; legend hidden. No axis titles.
- Labels: Year 0, Year 1, Year 2, Year 3, Year 4, Year 5, Year 6, Year 7, Year 8, Year 9, Year 10.
- Initial data in code: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; replaced on load by calculateROI() (formula in Calculators B).
- Tooltip: "Cumulative Net Cash: RM {value with thousands separators}".
- Values at default inputs (computed by running the code logic):

| Label | Net Cumulative Cash Flow (RM) |
|---|---|
| Year 0 | -2,086,274.51 (not rounded in code) |
| Year 1 | -1,562,151 |
| Year 2 | -1,038,027 |
| Year 3 | -513,903 |
| Year 4 | 10,221 |
| Year 5 | 534,345 |
| Year 6 | 1,058,469 |
| Year 7 | 1,582,593 |
| Year 8 | 2,106,717 |
| Year 9 | 2,630,841 |
| Year 10 | 3,154,965 |

## Calculators and interactive logic

### A. Interactive 30-Minute Interval Load & Demand Simulator (`updateIntervalSim`)

- Location: Section 2.
- Input: `simEnergyInput` — "30-Min Energy Import (E_i)", type number, default 500, min 50, max 5000, step 50, unit kWh. Fires on every input change.
- Constants: 89.27 (MV General RM/kW), 97.06 (MV ToU RM/kW).
- Formula (faithful to JS):

```
energy      = parseFloat(input) or 0
demand      = energy * 2                      # kW
costGeneral = demand * 89.27                  # RM
costToU     = demand * 97.06                  # RM
show "30-Min Energy (E_i)"      = energy (thousands separators) + " kWh"
show "Recorded MD (2 × E_i)"    = demand (thousands separators) + " kW"
show "MV General MD Cost"       = "RM " + costGeneral (en-US, 2 decimals)
show "MV ToU MD Cost (Peak)"    = "RM " + costToU (en-US, 2 decimals)
# code comment: "Update interval 27 (13:30) and 28 (14:00) in chart"
chart series data[27] = demand ; redraw      # only index 27 is written
```

- Not called on page load (only on input), so the static placeholders show first.
- Outputs at default inputs (computed by running the code logic): 500 kWh; 1,000 kW; RM 89,270.00; RM 97,060.00 — identical to the HTML placeholders. Chart index 27 would be set to 1000 (same as its base value).
- At max input 5000 (computed): 10,000 kW; RM 892,700.00; RM 970,600.00.

### B. C&I Maximum Demand Reduction & BESS ROI Estimator (`calculateROI`)

- Location: Section 3. Runs on page load and on every input change.
- Inputs:

| Input (id) | Label | Type | Default | Min / Max / Step or options |
|---|---|---|---|---|
| calcTariff | Select RP4 Tariff Category | select | MV_ToU (selected) | MV_General = "Medium Voltage General (RM89.27 / kW)"; MV_ToU = "Medium Voltage ToU (RM97.06 / kW)"; HV_ToU = "High Voltage ToU (RM44.82 / kW)" |
| calcKwh | Monthly Energy Consumption (kWh) | number | 600000 | min 50000, step 50000, no max |
| calcPeakKw | Current Unmitigated Peak Demand (kW) | range | 1800 | min 300, max 5000, step 50 |
| calcRedPct | Target Peak MD Reduction Goal (%) | range | 25 | min 5, max 50, step 1 |
| calcGita | GITA Asset Tax Allowance Status | select | Tier1_100 (first option) | Tier1_100 = "Tier 1: 100% Investment Tax Allowance (BESS & Solar+BESS)"; None = "No Tax Incentives Applied" |

- Constants: MD rates 97.06 (default / MV_ToU), 89.27 (MV_General), 44.82 (HV_ToU); inverter safety factor 1.15; discharge duration 3.5 h; DoD 0.85; efficiency 0.90; SoH 0.90; turn-key BESS cost RM1,200 per kWh ("~RM1,200 per kWh"); GITA tax shield 24% of gross CapEx.
- Formula (faithful to JS, including code comments):

```
tariff, kwh, peakKw, redPct, gitaOption = inputs   # kwh is read but never used
label calcPeakKwVal = peakKw (thousands separators) + " kW"
deltaKw = peakKw * (redPct / 100)
label calcRedPctVal = redPct + "% (" + round0(deltaKw) + " kW)"

mdRate = 97.06                         # "Default MV ToU"
if tariff == "MV_General": mdRate = 89.27
if tariff == "HV_ToU":     mdRate = 44.82

monthlySavings = deltaKw * mdRate
annualSavings  = monthlySavings * 12

bessKw  = deltaKw * 1.15               # "Inverter Power rating (kW AC) with 1.15 safety margin"
bessKwh = (deltaKw * 3.5) / (0.85 * 0.90 * 0.90)
          # "Storage Capacity (kWh): Delta kW * 3.5 hours peak discharge duration / (DoD 0.85 * Eff 0.90 * SoH 0.90)"
grossCapex = bessKwh * 1200            # "Turn-key BESS Cost (~RM1,200 per kWh)"

gitaTaxShield = 0
if gitaOption == "Tier1_100": gitaTaxShield = grossCapex * 0.24
          # "GITA Tier 1 = 100% ITA against 70% Statutory Income at 24% tax rate"; "24% effective tax reduction"
netCapex    = grossCapex - gitaTaxShield
paybackYears = annualSavings > 0 ? netCapex / annualSavings : 0

cash[0] = -netCapex                    # not rounded
for y in 1..10: cash[y] = round(-netCapex + annualSavings * y)
```

- Output formatting and branches:
  - resMonthlySavings = "RM " + round(monthlySavings) with thousands separators.
  - resAnnualSavings = "RM " + round(annualSavings) + " / year".
  - resPayback = paybackYears to 1 decimal + " Years" if paybackYears > 0, else "N/A".
  - resGitaShield = if Tier1_100: "Includes RM {round(gitaTaxShield)} GITA Tax Shield"; else "No Tax Shield Applied".
  - resBessKw = round(bessKw) + " kW AC"; resBessKwh = round(bessKwh) + " kWh"; resGrossCapex = "RM " + round(grossCapex).
  - Cash-flow chart series = cash[0..10].

Outputs at default inputs (computed by running the code logic: MV_ToU, 600000 kWh, 1800 kW, 25%, Tier1_100):

| Output | Computed by code | Static HTML placeholder |
|---|---|---|
| Peak slider label | 1,800 kW | 1,800 kW |
| Reduction slider label | 25% (450 kW) | 25% (450 kW) |
| deltaKw | 450 | — |
| Monthly MD Savings | RM 43,677 | RM 43,677 |
| Annual savings | RM 524,124 / year | RM 524,124 / year |
| Required Inverter Power | 518 kW AC (517.5 unrounded) | 518 kW AC |
| Nominal Battery Capacity | 2,288 kWh (2,287.58 unrounded) | 1,825 kWh |
| Gross Turn-Key CapEx | RM 2,745,098 | RM 1,642,500 |
| GITA shield line | Includes RM 658,824 GITA Tax Shield | Includes 24% GITA Corporate Tax Shield |
| Net CapEx | RM 2,086,274.51 | — |
| Estimated BESS Payback (Net CapEx) | 4.0 Years (3.98 unrounded) | 2.4 Years |

Outputs for every dropdown combination at the other defaults (1,800 kW, 25%) (computed):

| Tariff | GITA | Monthly savings | Annual savings | Payback | Shield line | Inverter | Capacity | Gross CapEx | Year 10 cumulative |
|---|---|---|---|---|---|---|---|---|---|
| MV_General | Tier1_100 | RM 40,172 | RM 482,058 / year | 4.3 Years | Includes RM 658,824 GITA Tax Shield | 518 kW AC | 2,288 kWh | RM 2,745,098 | 2,734,305 |
| MV_General | None | RM 40,172 | RM 482,058 / year | 5.7 Years | No Tax Shield Applied | 518 kW AC | 2,288 kWh | RM 2,745,098 | 2,075,482 |
| MV_ToU | Tier1_100 | RM 43,677 | RM 524,124 / year | 4.0 Years | Includes RM 658,824 GITA Tax Shield | 518 kW AC | 2,288 kWh | RM 2,745,098 | 3,154,965 |
| MV_ToU | None | RM 43,677 | RM 524,124 / year | 5.2 Years | No Tax Shield Applied | 518 kW AC | 2,288 kWh | RM 2,745,098 | 2,496,142 |
| HV_ToU | Tier1_100 | RM 20,169 | RM 242,028 / year | 8.6 Years | Includes RM 658,824 GITA Tax Shield | 518 kW AC | 2,288 kWh | RM 2,745,098 | 334,005 |
| HV_ToU | None | RM 20,169 | RM 242,028 / year | 11.3 Years | No Tax Shield Applied | 518 kW AC | 2,288 kWh | RM 2,745,098 | -324,818 |

### C. Solution tab switcher (`showSolution`)

- Location: Section 4. Clicking a tab hides all five tab panels, resets all tab buttons to the inactive style, then shows the chosen panel (sol-1 … sol-5) and highlights its button. Tab 1 is active on load. No data logic.

### D. Page initialisation

- On DOMContentLoaded: build Chart 1, Chart 2, Chart 3, Chart 4, then run calculateROI(). updateIntervalSim() is not run on load.

## Embedded data tables

All JS data arrays and objects in the page, verbatim:

```
// Chart 1 (rp4RatesChart)
labels: ['LV General', 'MV General', 'MV ToU (Peak)', 'HV General', 'HV ToU (Peak)']
'Capacity Rate (RM/kW)': [0, 29.43, 30.19, 16.68, 21.76]
'Network Rate (RM/kW)':  [0, 59.84, 66.87, 14.53, 23.06]

// Chart 2 (intervalProfileChart) baseDemand, 48 values (labels generated 00:00, 00:30 ... 23:30)
[250, 240, 230, 220, 220, 230, 350, 450, 600, 650, 700, 750, 780, 800, 780, 750,   // 00:00 - 08:00
 800, 850, 880, 900, 870, 850, 820, 800,                                             // 08:00 - 12:00
 820, 850, 880, 1000, 950, 900, 880, 850, 820, 800, 780, 750, 700, 680, 650, 600,    // 12:00 - 20:00
 500, 450, 400, 350, 300, 280, 260, 250]                                             // 20:00 - 24:00
bgColors: index 28..43 -> peak colour, else neutral   (computed, never used)

// Chart 3 (solarBessChart)
hours: ['08:00','10:00','12:00','14:00 (ToU Peak Starts)','15:00 (Cloud Sag)','17:00','19:00 (Dark Peak)','21:00','22:00']
'Grid Demand with Standalone Solar PV (kW)':          [400, 300, 250, 450, 1100, 800, 1200, 1000, 600]
'Grid Demand with Solar PV + BESS Peak Shaving (kW)': [400, 300, 250, 450, 750, 750, 750, 750, 600]

// Chart 4 (cashflowChart)
labels: ['Year 0', 'Year 1', ..., 'Year 10']
'Net Cumulative Cash Flow (RM)' initial data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

// calculateROI tariff map
default 97.06 (MV_ToU); 'MV_General' -> 89.27; 'HV_ToU' -> 44.82
// BESS constants
1.15 (inverter safety factor); 3.5 h; 0.85 DoD; 0.90 efficiency; 0.90 SoH; 1200 RM/kWh; 0.24 GITA shield
// updateIntervalSim constants
2 (kWh -> kW); 89.27; 97.06; writes chart index 27
```

Chart 2 data with labels is tabulated in full in the Charts section.

## Links and cited documents

| Label as shown | URL or document ID | Where used |
|---|---|---|
| 1. RP4 Tariff Architecture | #rp4-paradigm (in-page anchor) | Sticky navigation |
| 2. MD Mathematics & Surcharges | #physics-math (in-page anchor) | Sticky navigation |
| Dynamic Savings Calculator | #roi-calculator (in-page anchor) | Sticky navigation |
| 4. C&I Mitigation Solutions | #mitigation-solutions (in-page anchor) | Sticky navigation |
| 5. EECA 2024 & GITA Incentives | #eeca-gita (in-page anchor) | Sticky navigation |
| 6. Execution Roadmap | #roadmap (in-page anchor) | Sticky navigation |
| Tailwind CSS CDN (script, not a link) | https://cdn.tailwindcss.com | Page styling library |
| Chart.js CDN (script, not a link) | https://cdn.jsdelivr.net/npm/chart.js | Chart library |
| Energy Commission (Suruhanjaya Tenaga) RP4 Tariff Schedules (1 July 2025 – 31 Dec 2027) | named, no URL | Footer source line; Section 1 |
| EECA 2024 / Energy Efficiency and Conservation Act 2024 (Act 861) | Act 861, named, no URL | Section 5; footer; Section 6 |
| Budget 2027 GITA Framework | named, no URL | Footer; Section 5 |
| Green Investment Tax Allowance (GITA) Tier 1 (100% ITA against 70% Statutory Income) | named, no URL | Sections 3, 5, 6 |
| MGTC (submission body for GITA) | named, no URL; acronym not expanded | Sections 5, 6 |
| REM Class 1 / REM Class 2 appointment | named; acronym not expanded | Sections 5, 6 |
| Annual EECR report to Suruhanjaya Tenaga | named; acronym not expanded | Section 6 |
| TNB Medium Voltage TES tariff schedule | named, no URL | Section 4, tab 5 |
| KWTBB Levy (1.6%) | named; acronym not expanded | Chart 1 subtitle |
| Automatic Fuel Adjustment (AFA); legacy ICPT (6-month cycle) | named | Section 1 |
| SMP export rate (RM0.1881/kWh) | named; acronym not expanded | Section 4, tab 4 |
| Legacy tariff codes: Tariffs B, C1, C2, D, E1, E2, E3 (abolished list); table also lists F, F1, F2, C3, C4 | named | Section 1 |

No external hyperlinks (href to http/https) appear in the page.

## Extraction notes

- Unrendered LaTeX: the page loads only Tailwind and Chart.js (no MathJax/KaTeX), so all `$...$` math shows raw on screen: Section 2 cards 1–3 (e.g. `$E_i = M_{\text{end}} - M_{\text{start}}$`, `$\text{RM}388,240/\text{month}$`, `$1.5\%$`), the Section 3 BESS sizing footnote (`$k_s = 1.15$`, `$\eta_{\text{dis}}$`, `$\text{SoH}_{\text{EoL}}$`), Section 4 tab 1 (`$2.60\text{ sen/kWh}$`, Scenario A/B MD conditions), tab 2 (`$50\text{ kW}$`, `$150\text{ kW}$`) and tab 3 (`$t_e$`, `$E(t_e)$`, `$P_{\text{inst}}$`). Plain-text versions are given in the body.
- Literal markdown asterisks: "\*Suruhanjaya Tenaga\*" appears with visible asterisks in the Section 1 context paragraph and the footer.
- BESS ROI placeholder vs computed mismatch (calculator runs on load, so the computed values are what users see): placeholder 1,825 kWh / RM 1,642,500 / 2.4 Years / "Includes 24% GITA Corporate Tax Shield" vs computed 2,288 kWh / RM 2,745,098 / 4.0 Years / "Includes RM 658,824 GITA Tax Shield". Placeholder figures are internally consistent with RM900/kWh (1,825 × 900 = 1,642,500; 1,642,500 × 0.76 / 524,124 = 2.38 years), not with the code's RM1,200/kWh and 3.5-hour sizing. Placeholders for monthly/annual savings and 518 kW AC match the code.
- BESS sizing duration conflict: the code sizes energy for 3.5 hours of discharge ("Delta kW * 3.5 hours peak discharge duration"), but the visible footnote says sizing is "across the 8-hour weekday peak window". Using 8 h in the same formula would give 5,229 kWh at defaults (arithmetic only).
- Safety factor k_s = 1.15 is applied only to inverter kW, not to kWh capacity, though the footnote lists it among the battery sizing factors. The footnote calls 90% "round-trip efficiency" but labels it η_dis (discharge efficiency).
- The "Monthly Energy Consumption (kWh)" input (default 600000) is read into `kwh` but never used in any formula; changing it has no effect.
- GITA tax shield is a flat 24% of gross CapEx in year 0; the code comment and Section 5 mention "100% ITA against 70% Statutory Income", but no 70% cap, utilisation timing or tax-rate input is modelled. Cash flow has no O&M, degradation, tariff escalation or discounting. Year 0 cash value is unrounded while years 1–10 are rounded.
- Payback claims do not reconcile: Phase 3 says Tier 1 GITA can "compress payback to 2–3 years" and the placeholder shows 2.4 years, but the calculator at its own defaults computes 4.0 years (5.2 years without GITA).
- 30-minute simulator writes the user's demand only to chart index 27 (13:30), which is outside the 14:00–22:00 window the chart title highlights; the code comment says "Update interval 27 (13:30) and 28 (14:00)" but index 28 is never written. The peak-window background colour array (`bgColors`, indexes 28–43) is computed but never applied, so no peak-window highlight is drawn.
- The simulator's "MV ToU MD Cost (Peak)" bills the 13:30 block at RM97.06/kW, although the report itself says demand before 14:00 carries zero MD charge on ToU (Tab 2; Scenario B "billed at RM0/kW"). The simulator also does not apply its own max-over-month rule: "Recorded MD" is just 2 × the entered block, regardless of the other 47 blocks in the profile.
- In the base profile the daily maximum (1,000 kW) sits at 13:30, just outside the peak window; the maximum inside 14:00–21:30 is 950 kW (observation from the array).
- Simulator subtitle says "instant active power dictates monthly MD billing", contradicting the Section 2 statement that TNB does not bill on instantaneous spikes but on 30-minute average demand.
- Tariff arbitrage figures recorded exactly as shown: inequality `E_total × (0.0409 × α - 0.0149) + 89.27 × MD_24h - 97.06 × MD_peak > 0`; α > 36.43% + (190.46 × MD / E_total); example 74.5%; > 8.03%; 0.9197. They reconcile arithmetically with the report's own table: 31.32 − 27.23 = 4.09 sen; 31.32 − 29.83 = 1.49 sen; 0.0149 / 0.0409 = 0.3643; 7.79 / 0.0409 = 190.46; 0.3643 + 190.46 × 1,000 / 500,000 = 0.745; 89.27 / 97.06 = 0.9197; 1 − 0.9197 = 8.03%. "Neutral energy splits" in Scenario B implicitly means the energy term equals zero (α = 36.43%). The 2.60 sen/kWh "discount" = MV General 29.83 − MV ToU off-peak 27.23.
- Other arithmetic checks that reconcile: RM7.79 = 97.06 − 89.27; RM388,240 = 4,000 × 97.06; RM 14,559 = 150 × 97.06; 1,440 = 30 × 48; 128 / 168 = 76.2%; 21,600 GJ = 6.0M kWh/yr = 500,000 kWh/month; 50,000 GJ ≈ 13.9M kWh; component sums equal each Total MD Rate.
- "+100% to +202%" MD hike (header) and "up to 202%" (Section 1) cannot be reproduced from the report's own figures: against the stated legacy range RM30.30–RM45.10/kW, the RP4 MV rates give +97.9% (89.27 vs 45.10) to +220.3% (97.06 vs 30.30), with 89.27 vs 30.30 = +194.6%. The report does not say which legacy rate maps to which RP4 rate.
- Legacy-code inconsistency: the context paragraph lists abolished codes "Tariffs B, C1, C2, D, E1, E2, E3", but the table's legacy column also uses F, F1, F2, C3 and C4.
- Tariff table oddities to verify against the ST schedule (no source given): HV energy rates (43.03; 44.52/40.43 sen/kWh) are higher than MV (29.83) and LV (27.03); every ToU row has the same peak/off-peak spread (4.09 sen) and the same peak premium over General (1.49 sen). For LV, it is not stated whether the 8.83 + 14.82 sen/kWh capacity/network charges are included in or added to the 27.03 sen energy rate. Chart 1 plots LV General as 0 RM/kW (volumetric) and omits LV ToU, though the design comment says the chart compares LV, MV and HV General vs ToU.
- PF surcharge: the base the 1.5% / 3.0% surcharge applies to is not stated. The design comment promises a "Power Factor Surcharge Calculator" in Section 2, but none exists in the page.
- Design-comment vs page mismatches: "Dynamic Stat Ticker" is a static stat box; the rate table and EECA threshold assessment are static, not interactive; Section 4 is planned to cover "6 C&I engineering solutions" but has 5 tabs; the planned peak-window highlight is not rendered. The nav label for Section 3 has no "3." number; the calculator's input panel is headed "1. Facility Operational Parameters" with no "2." heading.
- Claims with no source citation in the page (only the footer's generic source line): Budget 2027 GITA restructuring (BESS/Solar+BESS Tier 1 through 31 Dec 2030; standalone EE removed from 1 Jan 2027; MGTC submission by 31 Dec 2026); EECA thresholds, REM classes and RM100,000 fine; SMP export RM0.1881/kWh; 1.6% KWTBB levy; chillers "up to 60%" of peak demand; TNB MV TES tariff "permanently shielding" chiller kW; turn-key BESS cost ~RM1,200/kWh (code comment only); "AI-sized BESS" (Phase 3).
- Undefined acronyms in the report: REM, MGTC, EECR, KWTBB, SMP, ICPT, AHU, VSD, BMS, ITA (ITA is expanded only in the calculator option text).
- Terminology: "cloud transient voltage sag" (design comment) describes a solar output drop, not a voltage event; Tab 5 describes off-peak as "overnight hours (22:00–14:00)", which spans the 08:00–14:00 daytime as well.
- Chart 3 x-axis labels are unevenly spaced in time (08, 10, 12, 14, 15, 17, 19, 21, 22) but plotted as equal categories.
- Chart.js is loaded from an unversioned CDN URL (`npm/chart.js`), so rendering depends on whatever version is current.
- `toLocaleString()` is called without a locale for most outputs, so separators follow the viewer's browser locale; the computed values above use en-US formatting.
