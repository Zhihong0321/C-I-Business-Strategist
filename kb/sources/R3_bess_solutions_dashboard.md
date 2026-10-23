---
id: R3
title: "Malaysia C&I BESS Solutions & RP4 Maximum Demand Optimization"
source_file: malaysia_c_i_bess_solutions_dashboard.html
source_modified: 2026-10-23 14:15
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js)
research_prompt: none (first-round report the user ran before our research prompts)
stated_scope: "Malaysia C&I BESS Navigator — RP4 Maximum Demand Optimization & Provider Ecosystem; footer: Malaysia Commercial & Industrial BESS Executive Decision Support System"
stated_sources: "Based on RP4 Peninsular Malaysia Tariff Schedules, Energy Commission Guidelines, BOMBA MS 2747:2024, and Budget 2027 GITA Framework."
as_of: "No report date stated. RP4 described as governing Peninsular Malaysia through 31 December 2027; GITA compared as Current Framework (2024 – 2026) vs Revised Budget 2027 (2027 – 2030); ST guideline cited as GP/ST/No.62/2026; BOMBA standard MS 2747:2024."
sections: [Header & Key Metrics Banner, Tariff Overview, ROI & Bill Simulator, Dispatch Visualizer, Provider Directory, Architectures, Regulatory & GITA, Footer]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R3 — Malaysia C&I BESS Solutions & RP4 Maximum Demand Optimization

> Faithful, complete markdown extract of `malaysia_c_i_bess_solutions_dashboard.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- RP4 (governing Peninsular Malaysia through 31 December 2027) unbundles tariffs into LV, MV and HV tiers; MD charges split into a Capacity Charge (generation reserve) and a Network Charge (grid stress); a single 30-minute peak draw sets the MD charge for the whole month. (Section 2)
- Combined MD charges: MV General RM89.27/kW (anytime), MV ToU RM97.06/kW (peak window), HV General RM31.21/kW (anytime), HV ToU RM44.82/kW (peak window); LV is volumetric 23.65 sen/kWh. (Section 2 table)
- Moving from MV General to MV ToU raises MD rates by +8.7% (RM89.27 to RM97.06/kW) and peak energy to 31.32 sen/kWh ("The MV ToU Tariff Trap"). (Section 2)
- Under MV ToU, capacity and network charges are levied only on demand recorded 2:00 PM – 10:00 PM on weekdays; off-peak (10:00 PM – 2:00 PM and weekends) demand is exempt. (Banner, Section 2)
- BESS turnkey CapEx benchmark RM1,150 – 1,600 / kWh with 3–5 year payback for C&I facilities; simulator uses RM1,350/kWh average. (Banner, Sections 3 and 5)
- Budget 2027 GITA: 100% tax allowance, Tier 1 for integrated Solar + BESS (whole system), versus standalone BESS Tier 1 100% and standalone solar Tier 2 60% (14.4% effective CapEx reduction at 24% corporate tax). (Banner, Section 7)
- Case study: 500,000 kWh/month MV factory, 900 kW baseline MD, monthly MD + energy charges go from RM80,343 + RM149,150 (MV General) to RM48,530 + RM122,018 after ToU shift + 1 MWp solar + 250 kW/500 kWh BESS. (Charts)
- Simulator shows placeholder results RM 229,693 baseline, RM 170,748 optimized (-25.7%), RM 707,340 annual savings, RM 675,000 BESS CapEx, RM 162,000 GITA saving, 3.1-year payback; the code computes different figures at its defaults (see Calculators). (Section 3)
- ST licensing mandatory for BESS ≥ 5 kW under Electricity Supply Act 1990; Guidelines GP/ST/No.62/2026 mandate IEC 62619, IEC 63056, UL 9540A. (Section 7)
- BOMBA MS 2747:2024 requires a 2-hour fire-rated enclosure or separating wall for stationary BESS; Fire Certificate needed to keep industrial insurance valid. (Section 7)
- TNB/GSO: CAS study required for SELCO > 72 kWp; BESS mandatory for all new SELCO systems > 1 MWac; CRESS grid access charges 14 sen/kWh (developers) / 4 sen/kWh (consumers). (Section 7)
- Provider directory of 12 players: 6 EPCC/developers (Solarvest, Plus Xnergy, Ditrolic, Sunview, Gentari, Northern Solar), 2 integrators (EVOLTS, VertexSol3), 4 OEMs (Sungrow, Huawei, HyperStrong, LVK Power). (Section 5, Embedded data)
- Sizing heuristics: peak shaving at 10% – 20% of facility MD, 1 – 2 hours; solar clipping capture 2 – 4 hours; ride-through at 100% of critical load for 15 – 30 minutes. (Section 6)

## 1. Header, navigation and key metrics banner

### Design notes from HTML comments (intended purpose / structure)

The HTML comments are the generator's build plan for an executive decision-support single-page app. Content of the comments:

- Chosen Palette: "Warm Slate & Emerald Energy".
- Application Structure Plan:
  1. Executive Header & Dynamic Stat Ticker: Highlights key RP4 changes, GITA tax changes, and BESS market drivers.
  2. Navigation Bar: Smooth tab-based single-page navigation across 6 core functional views.
  3. Section 1: RP4 Tariff Catalyst & Baseline Data: Displays unbundled tariff structures (MV/HV/LV) and comparative MD penalties.
  4. Section 2: Interactive RP4 Bill & BESS ROI Simulator: Allows users to input load parameters (kWh, kW MD) and calculate bill savings with Solar + BESS + GITA Tax Shields.
  5. Section 3: 24-Hour BESS Peak Shaving Visualizer: Interactive Chart.js visualization showing solar peak vs TNB Peak Window (2pm-10pm) and BESS dynamic discharge.
  6. Section 4: Solution Ecosystem & Provider Directory: Multi-tab filterable database of Turnkey EPCCs, Integrators, and OEMs with expandable details.
  7. Section 5: Technical Architectures & Sizing Heuristics: Structural comparison of Cabinets, Containers, Microgrids, and Tropical Cooling/Grid-Forming tech.
  8. Section 6: Regulatory, BOMBA Safety & Procurement Roadmap: Step-by-step checklist for ST Licensing, MS 2747:2024 compliance, and Budget 2027 GITA rules.
- Visualization & Content Choices:
  - RP4 Tariff Rates: Responsive HTML Table with dynamic ToU vs General highlight.
  - Interactive Bill Simulator: Custom Vanilla JS dynamic calculator + Chart.js Waterfall/Bar Chart.
  - 24-Hour Load & Dispatch Curve: Interactive Chart.js Line Chart with live toggle controls for Solar and BESS output.
  - Provider Ecosystem: Dynamic Search + Filter Chips + Dynamic Modal/Drawer details.
  - Confirmation: NO SVG graphics used (uses HTML/CSS shapes & Unicode icons). NO Mermaid JS used.

### Header

- Badge "BESS"; heading "Malaysia C&I BESS Navigator"; subtitle "RP4 Maximum Demand Optimization & Provider Ecosystem".
- Navigation tabs (desktop and mobile menu, same six): Tariff Overview; ROI & Bill Simulator; Dispatch Visualizer; Provider Directory; Architectures; Regulatory & GITA. The Tariff Overview section is shown on load; other sections are hidden until their tab is clicked.

### Key metrics banner

| Metric label | Value | Sub-text |
|---|---|---|
| RP4 Combined MV ToU Peak MD | RM97.06 / kW | Capacity + Network Fee (30-min peak) |
| TNB ToU Peak Billing Window | 2:00 PM – 10:00 PM | Mon–Fri (Off-peak exempt from MD) |
| Budget 2027 GITA Incentive | 100% Tax Allowance | Tier 1 for Integrated Solar + BESS |
| BESS Turnkey CapEx Benchmark | RM1,150 – 1,600 / kWh | 3–5 Year Payback for C&I Facilities |

## 2. Tariff Overview — RP4 Tariff Architecture & Maximum Demand Catalyst

Intro text: Under Regulatory Period 4 (RP4, governing Peninsular Malaysia through 31 December 2027), Tenaga Nasional Berhad (TNB) and the Energy Commission (ST) unbundled legacy tariffs into Low Voltage (LV), Medium Voltage (MV), and High Voltage (HV) tiers. Maximum Demand (MD) charges are split into an explicit **Capacity Charge** (generation reserve) and **Network Charge** (grid stress). A single 30-minute peak draw recorded by smart meters during the billing cycle sets the baseline charge for the entire month.

### RP4 schedule table

| RP4 Tariff Tier | Legacy Mapping | Energy Charge (sen/kWh) | Capacity Charge | Network Charge | Combined MD Charge | Monthly Retail Fee |
|---|---|---|---|---|---|---|
| LV General | Tariffs B, D, F | 27.03 | 8.83 sen/kWh | 14.82 sen/kWh | Volumetric: 23.65 sen/kWh | RM20 |
| LV ToU | Tariffs B, D, F (Opt-in) | Peak: 28.52 / Off-Peak: 24.43 | 8.83 sen/kWh | 14.82 sen/kWh | Volumetric: 23.65 sen/kWh | RM20 |
| MV General (row highlighted) | Tariffs C1, E1, F1 | 29.83 | RM29.43 / kW | RM59.84 / kW | RM89.27 / kW (Anytime) | RM200 |
| MV ToU (row highlighted) | Tariffs C2, E2, F2 | Peak: 31.32 / Off-Peak: 27.23 | RM30.19 / kW | RM66.87 / kW | RM97.06 / kW (Peak Window) | RM200 |
| HV General | Tariff C3 | 43.03 | RM16.68 / kW | RM14.53 / kW | RM31.21 / kW (Anytime) | RM250 |
| HV ToU | Tariffs C4, E3 | Peak: 44.52 / Off-Peak: 40.43 | RM21.76 / kW | RM23.06 / kW | RM44.82 / kW (Peak Window) | RM250 |

### Strategic ToU explanation (two callout cards)

- **The MV ToU Tariff Trap (Unmanaged Migration):** Migrating from MV General to MV ToU raises maximum demand rates by **+8.7%** (from RM89.27 to RM97.06/kW) and increases peak volumetric energy rates to 31.32 sen/kWh. Without active demand control or energy storage, an uncoordinated peak spike during weekday afternoons results in severe financial penalties.
- **The BESS + ToU Optimization Opportunity:** Under MV ToU, TNB calculates Capacity and Network charges **exclusively on peak demand recorded between 2:00 PM and 10:00 PM on weekdays**. Maximum demand spikes occurring off-peak (10:00 PM – 2:00 PM and weekends) are completely exempt. BESS discharges dynamically during peak hours to cap grid draw.

### Industrial Bill Reduction Progression Case Study

Subtitle: "Worked scenario for a 500,000 kWh/month Medium-Voltage factory (900 kW baseline MD) transitioning across optimization tiers." Rendered as a stacked bar chart; full data under Charts (Chart 1).

| Step | Maximum Demand Charges (RM) | Energy Consumption Charges (RM) |
|---|---|---|
| Baseline (MV General) | 80343 | 149150 |
| Step 1: ToU Tariff Shift | 72795 | 144330 |
| Step 2: Add Solar PV (1 MWp) | 72795 | 113723 |
| Step 3: Add BESS (250kW/500kWh) | 48530 | 122018 |

## 3. ROI & Bill Simulator — Interactive RP4 Bill & BESS ROI Calculator

Intro text: Estimate monthly core electricity expenditure, Maximum Demand savings, and projected GITA tax shields by modeling your facility's operational parameters.

### Facility Operational Inputs (controls)

- Tariff Classification (dropdown): Medium Voltage ToU (Tariff C2/E2/F2) - RM97.06/kW [selected]; Medium Voltage General (Tariff C1/E1/F1) - RM89.27/kW; High Voltage ToU (Tariff C4/E3) - RM44.82/kW; High Voltage General (Tariff C3) - RM31.21/kW.
- Monthly Energy Consumption (kWh): slider, shown 500,000.
- Baseline Peak Maximum Demand (kW): slider, shown 900.
- Solar PV Capacity (kWp): slider, shown 1,000.
- Target BESS Shaving Capacity (kW / kWh): slider, shown "250 kW / 500 kWh". Note under slider: "Assumes 2-hour discharge duration at 0.5C rate for peak shaving."
- Checkbox (checked): "Apply Budget 2027 GITA 100% Tax Shield (24% Corporate Tax)".

### Output tiles (as shown in the HTML before JavaScript runs)

| Tile | Placeholder value | Sub-text |
|---|---|---|
| Baseline Core Monthly Bill | RM 229,693 | Before optimization |
| Optimized Monthly Core Bill | RM 170,748 | -25.7% Total Reduction |
| Annualized Savings | RM 707,340 | Per year utility offset |

### Financial ROI highlights (placeholder values)

| Line | Placeholder value |
|---|---|
| Estimated BESS Installed CapEx (RM1,350/kWh avg): | RM 675,000 |
| Direct Tax Savings via GITA Tier 1 (24%): | RM 162,000 |
| Estimated Net Simple Payback Horizon: | 3.1 Years |

Chart below the outputs: "Monthly Expenditure Breakdown Comparison" (Chart 2). Inputs, formulas and the values the code actually displays at defaults are under "Calculators and interactive logic".

## 4. Dispatch Visualizer — 24-Hour Load & BESS Dispatch Simulation

Intro text: Simulate dynamic demand peak shaving between TNB's 2:00 PM and 10:00 PM Peak Tariff window.

- Dispatch Controls: buttons "Standard Peak Shave" (styled as active on load) and "Late Afternoon Spike".
- **Solar & Tariff Mismatch Notice:** Peak solar irradiance occurs from 10:00 AM to 3:00 PM (Off-Peak tariff). TNB's expensive Peak Tariff starts at 2:00 PM and extends to 10:00 PM. BESS bridges this gap by charging midday and discharging from 2:00 PM to 10:00 PM to keep net grid draw below the dynamic MD target.
- Line chart of 24-hour profile (Chart 3).
- Three explanation cards:
  1. **Midday Charging (10am–1pm):** BESS absorbs excess solar PV generation or off-peak grid energy to prevent zero-export clipping under SELCO guidelines.
  2. **Peak Discharge (2pm–10pm):** AI-driven EMS releases stored energy when factory equipment startups risk breaching the pre-defined target threshold.
  3. **Capped Grid Demand:** TNB smart meter records the reduced net grid peak, locking in low Capacity and Network charges for the billing cycle.

## 5. Provider Directory — Malaysia C&I BESS Provider Ecosystem Directory

Intro text: Filter across turnkey EPCCs, specialized integrators, and tier-one hardware OEMs.

- Search box (placeholder "Search providers, tech, or models...").
- Category tabs: All Providers (ALL, default); Turnkey EPCC & Developers (EPCC); Specialized Integrators (INTEGRATOR); Global Hardware OEMs (OEM).
- Each provider card shows: category badge, type, name, portfolio, description (clamped to two lines), tags, and a button "View Solution Architecture & Specs" that opens a details modal.
- Modal headings: name, category, "type • portfolio"; "Core Solution Architecture & Technology" (tech); "Target Customer Segments" (target); "Commercial & Financing Models" (commercial); "Verified ROI Metrics & Impact" (roi); "Detailed Description" (description).
- Empty-result text: "No solution providers matched your query."

Providers by category (every field of every provider is under "Embedded data tables"):

- EPCC: Solarvest Holdings Berhad; Plus Xnergy (BM GreenTech); Ditrolic Energy Holdings; Sunview Group Berhad; Gentari (PETRONAS); Northern Solar Holdings.
- INTEGRATOR: EVOLTS Integrators; VertexSol3 Compliance.
- OEM: Sungrow Power Supply; Huawei Digital Power; HyperStrong; LVK Power.

## 6. Architectures — C&I BESS Topologies & Technical Engineering

Intro text: Hardware topologies deployed in Malaysia are engineered for tropical heat dissipation, dynamic load response, and microgrid grid-forming stability.

### Topologies

| Topology | Range / class | Description | Models |
|---|---|---|---|
| Modular Outdoor Cabinets | 100 kW to 2.5 MW / Pre-assembled | Integrated LFP battery packs, BMS, liquid cooling, fire suppression, and bidirectional PCS inside a compact footprint (< 2 m²). | Sungrow PowerStack 255CS, Huawei LUNA2000-215/241, LVK-GS-522. |
| Containerized Systems | 5 MWh to 45+ MWh / Heavy Industry | 20-foot industrial containers featuring AC-coupled liquid cooling blocks, directly stepping up to 11kV or 33kV distribution rings via MV skid units. | Sungrow PowerTitan 2.0, HyperStrong HyperBlock III AC Block. |
| PV + ESS + EV Microgrids | Integrated Fast-Charging Buffers | 5-in-1 architectures acting as power buffers for 360 kW–480 kW DC fast chargers, preventing fleet charging from triggering TNB demand penalties. | Sigenergy SigenStor, Huawei One-Fits-All, Sungrow EVC Platform. |

### Operational Objective Sizing Matrix

| Operational Objective | Typical Power Rating (kW) | Discharge Duration (kWh) | Primary Driver & Application |
|---|---|---|---|
| Demand-Charge Peak Shaving | 10% – 20% of Facility MD | 1 – 2 Hours (0.5C – 1C) | Shaving 30-min rolling demand spikes from compressors, chillers, and stamping presses to eliminate RM89–97/kW fees. |
| Solar Arbitrage & Clipping Capture | Sized to PV Clipping Volume | 2 – 4 Hours (0.25C – 0.5C) | Capturing 10am–3pm SELCO/ATAP surplus solar to displace 31.32 sen/kWh evening peak energy draw. |
| Short-Interruption Ride-Through | 100% of Critical Process Load | 15 – 30 Minutes (2C) | Bridging voltage sags and brief grid trips for CNC machines, ovens, and automated assembly lines to prevent batch loss. |

## 7. Regulatory & GITA — Regulatory, BOMBA Safety & GITA Tax Framework

Intro text: Navigating mandatory Malaysian grid licensing, BOMBA MS 2747:2024 fire safety certification, and Budget 2027 tax allowance rules.

### Compliance cards

**Suruhanjaya Tenaga (ST) — Licensing & Safety Mandate**
- **Threshold:** Mandatory licensing for BESS ≥ 5 kW under Electricity Supply Act 1990.
- **Guidelines GP/ST/No.62/2026:** Mandatory IEC 62619, IEC 63056, UL 9540A certification.
- **Certification:** Form G (Completion) & Form H (Testing) signed by ST Competent Person.

**BOMBA Fire Safety — MS 2747:2024 Standards**
- **Fire Rating:** 2-hour fire-rated enclosure or separating wall required for stationary BESS.
- **Safety Clearance:** Mandatory thermal runaway suppression and isolation clearances.
- **Insurance Impact:** Fire Certificate (FC) is required to maintain valid industrial insurance.

**Grid Interconnection — TNB & GSO Regulations**
- **CAS Study:** Connection Assessment Study required for SELCO installations > 72 kWp.
- **Mandatory BESS:** Required for all new SELCO systems exceeding 1 MWac capacity.
- **CRESS Package:** Grid access charges set at 14 sen/kWh (developers) / 4 sen/kWh (consumers).

### Green Investment Tax Allowance (GITA) Comparison

| Parameter | Current Framework (2024 – 2026) | Revised Budget 2027 (2027 – 2030) | Strategic Financial Implication |
|---|---|---|---|
| Standalone BESS | Tier 1: 100% GITA | Tier 1: 100% GITA | Yields direct 24% tax shield on battery CapEx against 70% statutory income. |
| Standalone Solar PV | Tier 2: 60% GITA | Tier 2: 60% GITA | Lower tax shield (14.4% effective CapEx reduction at 24% corporate tax). |
| Integrated Solar + BESS (row highlighted) | Assessed separately (100% BESS / 60% Solar) | Elevated to Tier 1: 100% GITA on entire integrated system | Major Catalyst: Pairing solar with BESS elevates solar CapEx allowance to 100%. |

## 8. Footer

- "Malaysia Commercial & Industrial BESS Executive Decision Support System"
- "Based on RP4 Peninsular Malaysia Tariff Schedules, Energy Commission Guidelines, BOMBA MS 2747:2024, and Budget 2027 GITA Framework."

## Charts

### Chart 1 — Industrial Bill Reduction Progression Case Study (`tariffProgressionChart`)

- Location: Section 2 (Tariff Overview).
- Type: stacked bar (x and y stacked). Legend at bottom; tooltip mode index.
- X axis: no title (step labels). Y axis title: "Monthly Core Expenditure (RM)".

| Label | Maximum Demand Charges (RM) | Energy Consumption Charges (RM) |
|---|---|---|
| Baseline (MV General) | 80343 | 149150 |
| Step 1: ToU Tariff Shift | 72795 | 144330 |
| Step 2: Add Solar PV (1 MWp) | 72795 | 113723 |
| Step 3: Add BESS (250kW/500kWh) | 48530 | 122018 |

### Chart 2 — Monthly Expenditure Breakdown Comparison (`simWaterfallChart`)

- Location: Section 3 (ROI & Bill Simulator).
- Type: bar (single series, three bars; legend hidden). Y axis title "RM / Month", begins at zero. No x-axis title.
- Series "Monthly Expenditure (RM)". Bar 2 = baseline bill minus the MD-charge saving; bar 3 = optimized bill (see Calculators).

| Label | Hard-coded initial data | Value after calculateSim() runs on page load (default inputs) |
|---|---|---|
| Baseline Bill | 229693 | 231854 |
| After MD Peak Shaving | 205428 | 207589 |
| Final Optimized Core Bill | 170748 | 174400 |

### Chart 3 — 24-Hour Load & BESS Dispatch Simulation (`dispatchProfileChart`)

- Location: Section 4 (Dispatch Visualizer).
- Type: line. Legend at bottom; tooltip mode index. Y axis title "Power Demand (kW)"; x axis title "Hour of Day (24-Hr Clock)". X labels "0:00" to "23:00".
- Series plotted: "Baseline Factory Load (kW)" (dashed), "Solar PV Output (kW)" (filled area), "Net Grid Draw with BESS Peak Capping (kW)".
- Non-plotted array `bessDischargeStd` (kW; positive = discharge, negative = charge) is used only to compute the initial net series: net = max(100, baselineLoad − solarGen − bessDischargeStd).
- Net series has three states: initial (computed on load), "Standard Peak Shave" button (hard-coded `stdNet`), "Late Afternoon Spike" button (hard-coded `heavyNet`, code comment: "Late afternoon rainstorm solar drop simulation"). Baseline and solar series do not change between modes.

| Hour | Baseline Factory Load (kW) | Solar PV Output (kW) | bessDischargeStd (kW, not plotted) | Net grid draw: initial computed (kW) | Net grid draw: Standard Peak Shave button (kW) | Net grid draw: Late Afternoon Spike button (kW) |
|---|---|---|---|---|---|---|
| 0:00 | 400 | 0 | 0 | 400 | 400 | 400 |
| 1:00 | 380 | 0 | 0 | 380 | 380 | 380 |
| 2:00 | 380 | 0 | 0 | 380 | 380 | 380 |
| 3:00 | 390 | 0 | 0 | 390 | 390 | 390 |
| 4:00 | 420 | 0 | 0 | 420 | 420 | 420 |
| 5:00 | 500 | 0 | 0 | 500 | 500 | 500 |
| 6:00 | 700 | 50 | 0 | 650 | 650 | 650 |
| 7:00 | 850 | 200 | 0 | 650 | 650 | 650 |
| 8:00 | 900 | 500 | 0 | 400 | 400 | 400 |
| 9:00 | 920 | 850 | 0 | 100 | 70 | 70 |
| 10:00 | 950 | 950 | -200 | 200 | 200 | 200 |
| 11:00 | 940 | 980 | -200 | 160 | 160 | 160 |
| 12:00 | 880 | 920 | 0 | 100 | 0 | 0 |
| 13:00 | 900 | 750 | 0 | 150 | 150 | 150 |
| 14:00 | 960 | 400 | 250 | 310 | 310 | 510 |
| 15:00 | 980 | 150 | 250 | 580 | 580 | 730 |
| 16:00 | 950 | 20 | 250 | 680 | 680 | 720 |
| 17:00 | 910 | 0 | 200 | 710 | 710 | 710 |
| 18:00 | 850 | 0 | 100 | 750 | 750 | 750 |
| 19:00 | 750 | 0 | 0 | 750 | 750 | 750 |
| 20:00 | 650 | 0 | 0 | 650 | 650 | 650 |
| 21:00 | 550 | 0 | 0 | 550 | 550 | 550 |
| 22:00 | 450 | 0 | 0 | 450 | 450 | 450 |
| 23:00 | 420 | 0 | 0 | 420 | 420 | 420 |

(Initial computed column produced by running the code's formula; the raw value before the 100 kW floor is 70 at 9:00 and -40 at 12:00.)

## Calculators and interactive logic

### Calculator 1 — Interactive RP4 Bill & BESS ROI Calculator (`calculateSim()`)

- Location: Section 3 (ROI & Bill Simulator). Runs on page load (after charts are built) and on every input change.

Inputs:

| Input (id) | Label | Type | Default | Min | Max | Step | Options / notes |
|---|---|---|---|---|---|---|---|
| sim-tariff | Tariff Classification | select | MV_TOU | – | – | – | MV_TOU = "Medium Voltage ToU (Tariff C2/E2/F2) - RM97.06/kW"; MV_GEN = "Medium Voltage General (Tariff C1/E1/F1) - RM89.27/kW"; HV_TOU = "High Voltage ToU (Tariff C4/E3) - RM44.82/kW"; HV_GEN = "High Voltage General (Tariff C3) - RM31.21/kW" |
| sim-kwh | Monthly Energy Consumption (kWh) | range | 500000 | 50000 | 2000000 | 25000 | label shows value with thousands separators |
| sim-md | Baseline Peak Maximum Demand (kW) | range | 900 | 100 | 5000 | 50 | |
| sim-solar | Solar PV Capacity (kWp) | range | 1000 | 0 | 3000 | 50 | |
| sim-bess | Target BESS Shaving Capacity (kW / kWh) | range | 250 | 0 | 1000 | 25 | label shows "{bessKw} kW / {bessKw × 2} kWh" |
| sim-gita | Apply Budget 2027 GITA 100% Tax Shield (24% Corporate Tax) | checkbox | checked | – | – | – | |

Constants (rates by tariff; code comments in quotes):

| Tariff value | energyRate (RM/kWh) | mdRate (RM/kW) |
|---|---|---|
| MV_GEN (code default branch) | 0.2983 ("RM/kWh avg") | 89.27 |
| MV_TOU | 0.2886 ("blended peak/off-peak") | 97.06 |
| HV_TOU | 0.4200 | 44.82 |
| HV_GEN | 0.4303 | 31.21 |

Other constants: monthly fixed fee 200 (RM, added to both bills for every tariff); solar yield 115 kWh per kWp per month ("~115 kWh per kWp per month"); solar capped at 0.4 × monthly kWh; MD after BESS floored at 0.5 × baseline MD; BESS duration 2 hours (kWh = kW × 2); BESS CapEx 1350 RM/kWh ("RM 1,350 per kWh"); GITA tax rate 0.24.

Formula (faithful to the JS):

```
baselineMDCharge     = md * mdRate
baselineEnergyCharge = kwh * energyRate
baselineBill         = baselineMDCharge + baselineEnergyCharge + 200

solarGenKwh   = min(kwh * 0.4, solarKw * 115)
postSolarKwh  = kwh - solarGenKwh

postBessMD            = max(md * 0.5, md - bessKw)
optimizedMDCharge     = postBessMD * mdRate
optimizedEnergyCharge = postSolarKwh * energyRate
optimizedBill         = optimizedMDCharge + optimizedEnergyCharge + 200

monthlySavings = baselineBill - optimizedBill
annualSavings  = monthlySavings * 12
reductionPct   = round1((monthlySavings / baselineBill) * 100)

bessKwh      = bessKw * 2
bessCapEx    = bessKwh * 1350
gitaTaxShield = applyGita ? bessCapEx * 0.24 : 0
netCapEx     = bessCapEx - gitaTaxShield

paybackYears = annualSavings > 0
               ? round1(netCapEx / (bessKw > 0 ? bessKw * mdRate * 12 : 1))
               : 'N/A'

waterfall = [ round(baselineBill),
              round(baselineBill - (baselineMDCharge - postBessMD * mdRate)),
              round(optimizedBill) ]
```

Outputs displayed: "RM {round(baselineBill)}" (Baseline Core Monthly Bill); "RM {round(optimizedBill)}" (Optimized Monthly Core Bill); "-{reductionPct}% Total Reduction"; "RM {round(annualSavings)}" (Annualized Savings); "RM {round(bessCapEx)}" (Estimated BESS Installed CapEx); "RM {round(gitaTaxShield)}" (Direct Tax Savings via GITA Tier 1); "{paybackYears} Years" (Estimated Net Simple Payback Horizon); Chart 2 data.

Outputs at default inputs (computed by running the code logic with node; MV_TOU, 500000 kWh, 900 kW, 1000 kWp, 250 kW, GITA on):

| Quantity | Computed by code | Placeholder in HTML |
|---|---|---|
| baselineMDCharge | 87354 | – |
| baselineEnergyCharge | 144300 | – |
| Baseline Core Monthly Bill | RM 231,854 | RM 229,693 |
| solarGenKwh / postSolarKwh | 115000 / 385000 | – |
| postBessMD (kW) | 650 | – |
| optimizedMDCharge | 63089 | – |
| optimizedEnergyCharge | 111111 | – |
| Optimized Monthly Core Bill | RM 174,400 | RM 170,748 |
| Total Reduction | -24.8% | -25.7% |
| monthlySavings | 57454 | – |
| Annualized Savings | RM 689,448 | RM 707,340 |
| BESS size (label) | 250 kW / 500 kWh | 250 kW / 500 kWh |
| Estimated BESS Installed CapEx | RM 675,000 | RM 675,000 |
| Direct Tax Savings via GITA | RM 162,000 | RM 162,000 |
| netCapEx | 513000 | – |
| Payback denominator (bessKw × mdRate × 12) | 291180 | – |
| Estimated Net Simple Payback Horizon | 1.8 Years | 3.1 Years |
| Chart 2 data | 231854, 207589, 174400 | 229693, 205428, 170748 |

Outputs for each tariff option at the other default inputs (computed):

| Tariff | GITA | Baseline bill | Optimized bill | Reduction | Annual savings | CapEx | GITA saving | Payback | Chart 2 data |
|---|---|---|---|---|---|---|---|---|---|
| MV_TOU | on | RM 231,854 | RM 174,400 | -24.8% | RM 689,448 | RM 675,000 | RM 162,000 | 1.8 Years | 231854 / 207589 / 174400 |
| MV_TOU | off | RM 231,854 | RM 174,400 | -24.8% | RM 689,448 | RM 675,000 | RM 0 | 2.3 Years | 231854 / 207589 / 174400 |
| MV_GEN | on | RM 229,693 | RM 173,071 | -24.7% | RM 679,464 | RM 675,000 | RM 162,000 | 1.9 Years | 229693 / 207376 / 173071 |
| MV_GEN | off | RM 229,693 | RM 173,071 | -24.7% | RM 679,464 | RM 675,000 | RM 0 | 2.5 Years | 229693 / 207376 / 173071 |
| HV_TOU | on | RM 250,538 | RM 191,033 | -23.8% | RM 714,060 | RM 675,000 | RM 162,000 | 3.8 Years | 250538 / 239333 / 191033 |
| HV_TOU | off | RM 250,538 | RM 191,033 | -23.8% | RM 714,060 | RM 675,000 | RM 0 | 5.0 Years | 250538 / 239333 / 191033 |
| HV_GEN | on | RM 243,439 | RM 186,152 | -23.5% | RM 687,444 | RM 675,000 | RM 162,000 | 5.5 Years | 243439 / 235637 / 186152 |
| HV_GEN | off | RM 243,439 | RM 186,152 | -23.5% | RM 687,444 | RM 675,000 | RM 0 | 7.2 Years | 243439 / 235637 / 186152 |

Branch behaviour (computed examples, MV_TOU, GITA on):

- bessKw = 0, solar 1000 kWp: optimized RM 198,665, -14.3%, annual RM 398,268, CapEx RM 0, payback "0.0 Years" (denominator falls back to 1).
- bessKw = 0, solar 0: annual RM 0, payback "N/A Years".
- bessKw = 1000 with MD 900: postBessMD floors at 450 kW; optimized RM 154,988, -33.2%, annual RM 922,392, CapEx RM 2,700,000, GITA RM 648,000, payback 1.8 Years (denominator still uses 1000 kW).

### Interactive 2 — Dispatch mode toggle (`toggleDispatchMode(mode)`)

- Location: Section 4.
- On load: net series = computed initial series (Chart 3 table); "Standard Peak Shave" button is styled active.
- mode 'standard': highlights "Standard Peak Shave"; replaces net series with `stdNet`.
- any other mode ('heavy'): highlights "Late Afternoon Spike"; replaces net series with `heavyNet`.
- Only dataset index 2 (net grid draw) changes; all values are in the Chart 3 table.

### Interactive 3 — Provider directory filter (`renderProviders()`, `setProviderCategory()`, `openModal()`)

- Location: Section 5.
- Category filter: ALL shows all; otherwise `provider.category === currentCategory`.
- Search: lower-cased query matched as substring against name, tech, or any tag (not type, portfolio, target, commercial, roi or description).
- No match: "No solution providers matched your query."
- Card click opens a modal with the fields listed in Section 5.

### Interactive 4 — Navigation (`switchTab()`, `toggleMobileMenu()`)

- Shows one section at a time; highlights the active nav button; resizes the chart in the shown section. No nav button is highlighted on initial load.

## Embedded data tables

### providerData (12 entries, every field)

#### solarvest

| Field | Value |
|---|---|
| name | Solarvest Holdings Berhad |
| category | EPCC |
| type | Bursa-Listed Clean Energy Market Leader |
| portfolio | ~3.7 GWp portfolio / RM2.37B order book |
| tech | LFP Hardware + AIES (AI-driven Energy Simulator) + EPMS real-time monitoring |
| target | Large Manufacturing, MNCs, Data Centers |
| commercial | Outright Purchase (CapEx), GITA Financing, Corporate Asset Ownership |
| roi | 20% to 65% Maximum Demand reduction, ~3-year payback |
| tags | Turnkey EPCC; AI EMS; Zero-CapEx; GITA Advisory |
| description | Solarvest provides turnkey C&I solar and storage integration with proprietary AI-driven Energy Simulators (AIES) that predict factory load curves and prevent premature battery depletion. |

#### plusxnergy

| Field | Value |
|---|---|
| name | Plus Xnergy (BM GreenTech) |
| category | EPCC |
| type | Bursa-Listed Subsidiary (BM GreenTech) |
| portfolio | 100 MWh BESS portfolio & >500 MWp solar |
| tech | HyperStrong HyperBlock III AC-coupled systems & NaS storage |
| target | Heavy Industry, Food Manufacturing Hubs, Airports |
| commercial | 15-Year Performance Sharing Agreement (PSA / Zero-CapEx) |
| roi | RM1.25M/year savings per 10 MWh deployed |
| tags | 100 MWh Portfolio; HyperStrong Partner; 15-Yr PSA; Heavy Industry |
| description | Plus Xnergy commissioned one of Malaysia's largest single-site C&I BESS assets (20 MWh SELCO) at a food processing hub in Perak, executed in 2.5 months. |

#### ditrolic

| Field | Value |
|---|---|
| name | Ditrolic Energy Holdings |
| category | EPCC |
| type | Regional Clean Energy Developer |
| portfolio | >300 MW managed assets / >1 GW constructed |
| tech | EnerPack (Behind-the-meter BESS) & EnerGreen SolarPack (CRESS) |
| target | Facilities on MV/HV ToU Tariffs, Corporate 24/7 Green Buyers |
| commercial | Energy-as-a-Service (EaaS / Zero-CapEx), CRESS Tariffs |
| roi | ToU arbitrage + MV/HV Capacity charge mitigation |
| tags | EnerPack EaaS; CRESS Integration; MV/HV ToU; Zero-CapEx |
| description | Ditrolic Energy specializes in utility and C&I behind-the-meter energy storage paired with CRESS off-site solar access for large energy users. |

#### sunview

| Field | Value |
|---|---|
| name | Sunview Group Berhad |
| category | EPCC |
| type | Bursa-Listed Solar & Storage EPCC |
| portfolio | >350 MWp completed across 150+ sites |
| tech | SunBESS (AIoT LFP Storage tailored for RP4 & SELCO >1MWac) |
| target | C&I Factories, Warehouses, Retail Malls |
| commercial | SunVertax (Outright CapEx) & SunValue (Zero-CapEx Ownership) |
| roi | Full MGTC/MIDA GITA tax advisory & O&M |
| tags | SunBESS AIoT; SELCO >1MWac; SunValue Lease; GITA Advisory |
| description | Sunview provides end-to-end engineering and regulatory advisory, helping clients comply with ST BESS licensing and GITA Tier 1 tax submissions. |

#### gentari

| Field | Value |
|---|---|
| name | Gentari (PETRONAS) |
| category | EPCC |
| type | PETRONAS Clean Energy Entity |
| portfolio | Regional utility & C&I portfolio |
| tech | Integrated Solar+BESS + Ultra-fast EV Charging Hubs (BYD Partner) |
| target | Corporates, Industrial Parks, Highway Fast-Charging Nodes |
| commercial | Corporate PPAs, Zero-CapEx Leasing, Co-Investment |
| roi | High reliability grid firming & peak demand buffering |
| tags | PETRONAS Entity; EV Fast Charging; Corporate PPA; High-Power |
| description | Gentari builds integrated commercial solar, storage, and EV ultra-fast charging microgrids using battery buffers to protect against grid surge charges. |

#### northernsolar

| Field | Value |
|---|---|
| name | Northern Solar Holdings |
| category | EPCC |
| type | Bursa-Listed C&I EPCC |
| portfolio | Nationwide C&I factory installations |
| tech | Turnkey LFP BESS (Sungrow, Huawei, EVE Energy hardware) |
| target | SMEs to Large Factories on MV General/ToU |
| commercial | Outright Purchase (RM1,150–RM1,600/kWh turnkey pricing) |
| roi | 3–5 year industrial payback with GITA Tier 1 |
| tags | Competitive CapEx; ST Chargemen; Modular Cabinets |
| description | Northern Solar provides cost-competitive turnkey C&I storage systems with certified ST chargemen and local grid interconnection capabilities. |

#### evolts

| Field | Value |
|---|---|
| name | EVOLTS Integrators |
| category | INTEGRATOR |
| type | Specialized Engineering Integrator |
| portfolio | Engineering-led C&I projects |
| tech | Dual-function MD Shaving + Sub-cycle Ride-Through (15-30 min) |
| target | Automated Assembly, Precision CNC, Industrial Ovens |
| commercial | 30-day interval metering audit & turnkey delivery |
| roi | Eliminates momentary voltage sags + 15-20% MD reduction |
| tags | Precision Audit; Process Ride-Through; CNC Protection |
| description | EVOLTS mandates 30-day interval metering studies before sizing, designing systems that perform peak shaving while buffering critical process lines from voltage trips. |

#### vertexsol3

| Field | Value |
|---|---|
| name | VertexSol3 Compliance |
| category | INTEGRATOR |
| type | Technical Compliance Consultancy |
| portfolio | BOMBA & ST Regulatory Rescues |
| tech | BOMBA MS 2747:2024 Audit + GTFS 5.0 Bankability Dossiers |
| target | Overseas BESS Importers, C&I Project Owners |
| commercial | Consultancy & Pre-Procurement Audits |
| roi | Guarantees Fire Certificate (FC) issuance & insurance validity |
| tags | BOMBA MS 2747; ST Licensing; GTFS Validation; Safety Audit |
| description | VertexSol3 conducts gap audits on imported overseas BESS units to meet BOMBA MS 2747:2024 2-hour fire enclosure rules and secure ST licensing. |

#### sungrow

| Field | Value |
|---|---|
| name | Sungrow Power Supply |
| category | OEM |
| type | Global #1 Tier-1 Storage OEM |
| portfolio | >43 GWh shipped globally |
| tech | PowerStack 255CS (125kW/257kWh), PowerTitan 2.0 (2.5MW/5MWh) |
| target | Modular Cabinets to Utility C&I Containers |
| commercial | Supplied via Inverpower, ERS Energy, Northern Solar |
| roi | Liquid-cooled, ArcDefender™ safety, Stem-Cell Grid-Forming |
| tags | Global #1; PowerStack 255CS; PowerTitan 2.0; Grid-Forming |
| description | Sungrow leads the C&I market with pre-assembled liquid-cooled cabinets and containers operating at up to 50°C without derating. |

#### huawei

| Field | Value |
|---|---|
| name | Huawei Digital Power |
| category | OEM |
| type | Global Smart Energy Tech Giant |
| portfolio | Global Smart PV & ESS Leader |
| tech | LUNA2000-215/241 Series, LUNA2000-213KTL Smart PCS |
| target | C&I Factories, Microgrids, EV Highway Hubs |
| commercial | Distributed via KVC Industrial Supplies, Northern Solar, Trexon |
| roi | 92% VDE-certified round-trip efficiency, Cell-to-Consumption safety |
| tags | Hybrid Cooling; 92% Efficiency; Smart PCS; LUNA2000 |
| description | Huawei deploys industry-first C&I Hybrid Cooling systems with pack-level energy optimization and cell-level safety isolation. |

#### hyperstrong

| Field | Value |
|---|---|
| name | HyperStrong |
| category | OEM |
| type | Global High-Density BESS Manufacturer |
| portfolio | Multi-GWh international deployments |
| tech | HyperBlock III AC-Coupled LFP BESS |
| target | Multi-megawatt Heavy Industrial Plants |
| commercial | Exclusively deployed via Plus Xnergy partnership in Malaysia |
| roi | Rapid 2.5-month site execution for multi-MWh deployments |
| tags | HyperBlock III; AC-Coupled; Multi-MWh Scale |
| description | HyperStrong provides high-density AC-coupled battery blocks engineered for fast installation in heavy manufacturing facilities. |

#### lvkpower

| Field | Value |
|---|---|
| name | LVK Power |
| category | OEM |
| type | Industrial Cabinet Manufacturer |
| portfolio | Automotive & Stamping Workshop Deployments |
| tech | LVK-GS-522ESSC-100 (250 kW / 522 kWh Outdoor Cabinet) |
| target | Medium Factories, Automotive Stamping Workshops |
| commercial | Direct Supply & Local Integrators (e.g. Maju Antara) |
| roi | IP54 liquid-cooled, integrated BMS/PCS for stamping surges |
| tags | 250kW/522kWh Cabinet; IP54 Outdoor; Stamping Peak Shave |
| description | LVK Power's 250 kW / 522 kWh outdoor cabinets are field-proven at Malaysian automotive stamping plants to shave heavy motor startup spikes. |

### Dispatch arrays (kW, index 0 = 0:00)

- baselineLoad: 400, 380, 380, 390, 420, 500, 700, 850, 900, 920, 950, 940, 880, 900, 960, 980, 950, 910, 850, 750, 650, 550, 450, 420
- solarGen: 0, 0, 0, 0, 0, 0, 50, 200, 500, 850, 950, 980, 920, 750, 400, 150, 20, 0, 0, 0, 0, 0, 0, 0
- bessDischargeStd: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -200, -200, 0, 0, 250, 250, 250, 200, 100, 0, 0, 0, 0, 0
- stdNet: 400, 380, 380, 390, 420, 500, 650, 650, 400, 70, 200, 160, 0, 150, 310, 580, 680, 710, 750, 750, 650, 550, 450, 420
- heavyNet: 400, 380, 380, 390, 420, 500, 650, 650, 400, 70, 200, 160, 0, 150, 510, 730, 720, 710, 750, 750, 650, 550, 450, 420

### Chart data arrays

- tariffProgressionChart "Maximum Demand Charges (RM)": 80343, 72795, 72795, 48530
- tariffProgressionChart "Energy Consumption Charges (RM)": 149150, 144330, 113723, 122018
- simWaterfallChart "Monthly Expenditure (RM)" (initial): 229693, 205428, 170748

## Links and cited documents

| Label as shown | URL or document ID | Where used |
|---|---|---|
| (script) Tailwind CSS CDN | https://cdn.tailwindcss.com | page styling library |
| (script) Chart.js CDN | https://cdn.jsdelivr.net/npm/chart.js | chart library (unversioned) |
| RP4 / Regulatory Period 4 tariff schedules (Peninsular Malaysia) | no URL | Banner, Section 2, footer |
| Tariffs B, D, F; C1, E1, F1; C2, E2, F2; C3; C4, E3 (legacy tariff codes) | no URL | Section 2 table, simulator options |
| Electricity Supply Act 1990 | no URL | Section 7 (ST card) |
| Guidelines GP/ST/No.62/2026 | no URL | Section 7 (ST card) |
| IEC 62619 | standard | Section 7 (ST card) |
| IEC 63056 | standard | Section 7 (ST card) |
| UL 9540A | standard | Section 7 (ST card) |
| Form G (Completion), Form H (Testing) | ST forms | Section 7 (ST card) |
| MS 2747:2024 (BOMBA fire safety) | standard | Section 7, VertexSol3 entry, footer |
| Fire Certificate (FC) | BOMBA certificate | Section 7, VertexSol3 entry |
| Connection Assessment Study (CAS) | TNB study | Section 7 (Grid card) |
| SELCO | programme | Sections 4, 6, 7; Plus Xnergy and Sunview entries |
| ATAP | programme | Section 6 sizing matrix |
| CRESS Package | programme | Section 7; Ditrolic entry |
| Green Investment Tax Allowance (GITA), Budget 2027 | no URL | Banner, Sections 3 and 7, footer |
| MGTC/MIDA (GITA advisory) | agencies | Sunview entry |
| GTFS 5.0 Bankability Dossiers | document type | VertexSol3 entry |
| VDE certification (92% round-trip efficiency) | certification | Huawei entry |
| IP54 | enclosure rating | LVK Power entry |

No hyperlinks to sources appear anywhere in the report.

## Extraction notes

- **Simulator placeholders differ from computed values.** HTML placeholders (RM 229,693 / RM 170,748 / -25.7% / RM 707,340 / 3.1 Years; Chart 2 bars 229693 / 205428 / 170748) are replaced on page load by calculateSim(), which at defaults (MV_TOU selected) gives RM 231,854 / RM 174,400 / -24.8% / RM 689,448 / 1.8 Years; bars 231854 / 207589 / 174400. CapEx RM 675,000 and GITA RM 162,000 match. The placeholders reproduce the Chart 1 case study plus the RM200 fee (80,343 + 149,150 + 200 = 229,693; 48,530 + 122,018 + 200 = 170,748; 58,945 × 12 = 707,340; 229,693 − 250 × 97.06 = 205,428), i.e. an MV General baseline, not the MV ToU default. "3.1 Years" cannot be reproduced from any tariff/GITA combination at default inputs (computed range 1.8 – 7.2 years); it appears hard-coded.
- **Payback formula counts only MD savings from the BESS nameplate.** Payback = net BESS CapEx / (bessKw × mdRate × 12). It ignores solar savings and solar CapEx, assumes the 2-hour battery (kWh = 2 × kW) shaves its full kW rating every month, and ignores the 50% MD floor used in the bill calculation (bessKw 1000 vs MD 900: bill shaves 450 kW, payback divides by 1000 kW). With bessKw = 0 and solar > 0 it shows "0.0 Years"; with no savings it shows "N/A Years". No degradation, O&M, efficiency losses, financing or tariff escalation.
- **GITA in the simulator** is 24% × full BESS CapEx deducted up front. It ignores the "70% statutory income" limit stated in the GITA table and is not applied to solar CapEx, although the same report says integrated solar + BESS gets 100% GITA on the entire system.
- **Fixed fee hard-coded at RM200 for every tariff**, but the tariff table gives RM250/month for HV General and HV ToU.
- **Single blended energy rates**: MV_TOU 0.2886 and HV_TOU 0.4200 RM/kWh with no stated peak/off-peak weighting. Solar offsets kWh at the blended rate and never reduces MD. BESS energy arbitrage is not modelled.
- **CapEx average RM1,350/kWh** is labelled "avg", but the midpoint of the stated RM1,150 – 1,600/kWh benchmark is 1,375.
- **Case-study chart does not reconcile with its own subtitle or the simulator.** The subtitle says 900 kW baseline MD, but Step 1 MD charges 72,795 = 750 kW × 97.06 (900 kW would give 87,354). Step 3's 48,530 = 500 kW × 97.06, i.e. 750 − 250. The 750 kW peak-window MD is never stated. Step 2 energy 113,723 cannot be reproduced from 1 MWp × 115 kWh/kWp at 0.2886 (that gives 111,111). **Energy charges rise from Step 2 (113,723) to Step 3 (122,018) when the BESS is added**, with no explanation. Stack totals (extractor arithmetic, excluding the fee): 229,493 / 217,125 / 186,518 / 170,548.
- **Dispatch visualizer, three different net-grid series.** The initial series is computed with a 100 kW floor (100 at 9:00 and 12:00). The "Standard Peak Shave" button, which is styled active on load, swaps in hard-coded stdNet (70 and 0 at those hours), so clicking the already-active button changes the chart. "Late Afternoon Spike" (heavyNet) differs from stdNet only at 14:00 (510 vs 310), 15:00 (730 vs 580) and 16:00 (720 vs 680). The code comment calls it a "rainstorm solar drop" but the solar series is unchanged. The comment's promised "live toggle controls for Solar and BESS output" do not exist.
- **Dispatch energy does not balance.** bessDischargeStd discharges 1,050 kWh (14:00–18:00) but charges only 400 kWh (10:00–11:00). Charging covers 2 hours, against the card's "Midday Charging (10am–1pm)". No battery size is stated for the visualizer. In every mode the net peak inside 14:00–22:00 is 750 kW (18:00–19:00), against a baseline peak of 980 kW at 15:00. The "dynamic MD target" is never drawn or given a value.
- **Solar mismatch notice is internally inconsistent.** It calls 10:00 AM – 3:00 PM "Off-Peak tariff", but 2:00–3:00 PM is inside the stated 2:00 PM – 10:00 PM peak window.
- **Tariff table internal checks.** Capacity + network = combined MD in every row, and +8.7% reconciles (97.06 / 89.27 = 1.0873). HV energy charges (43.03; 44.52 / 40.43 sen/kWh) are higher than MV (29.83; 31.32 / 27.23) and LV (27.03; 28.52 / 24.43). That is unusual for a voltage-tier structure and worth checking against the primary RP4 schedule. LV capacity and network charges are given in sen/kWh, not RM/kW.
- **GITA table claims have no source.** It says Budget 2027 (2027 – 2030) keeps standalone BESS at Tier 1 100% and standalone solar at Tier 2 60%, and raises integrated solar + BESS to Tier 1 100% for the whole system (also the banner headline). The KB coordinator flagged this as conflicting with other reports in the set; this extract does not check that.
- **Regulatory cards cite nothing.** No citation or link is given for any of them: ST licensing for BESS ≥ 5 kW under Electricity Supply Act 1990; GP/ST/No.62/2026 (IEC 62619, IEC 63056, UL 9540A); Form G / Form H; BOMBA MS 2747:2024 2-hour fire-rated enclosure; CAS for SELCO > 72 kWp; mandatory BESS for new SELCO > 1 MWac; CRESS 14 sen/kWh developers / 4 sen/kWh consumers. All should be verified against primary documents.
- **Provider directory has no sources.** No citation or link supports any provider claim: portfolios, order books, the 20 MWh Perak project, "Global #1", the HyperStrong exclusivity via Plus Xnergy, distributor lists, the 92% efficiency. The modal heading says "Verified ROI Metrics & Impact", yet nothing is verified, and several "roi" fields are not ROI metrics (Sunview: advisory and O&M; Sungrow: product features; HyperStrong: execution time). EVOLTS "Sub-cycle Ride-Through (15-30 min)" is self-contradictory wording.
- **Smaller inconsistencies.** The sizing matrix pairs "15 – 30 Minutes" with "(2C)", but 2C is 30 minutes and 15 minutes would be 4C. The cabinet range "100 kW to 2.5 MW" overlaps the containerized PowerTitan 2.0 (2.5MW/5MWh). The banner's "3–5 Year Payback" contrasts with the simulator's computed 1.8 years at defaults.
- **HTML comment plan vs implementation.** The "Dynamic Stat Ticker" is a static banner. The "dynamic ToU vs General highlight" is static row shading. The "Waterfall" chart is a plain bar chart. "Filter Chips" are only category tabs plus search. There is no separate "Tropical Cooling/Grid-Forming" comparison. The "Step-by-step checklist / Procurement Roadmap" is three cards. No nav tab is highlighted on initial load.
