---
id: R1
title: "Malaysia C&I Solar PV & BESS Strategic Intelligence Hub (2026–2030)"
source_file: malaysia_c_i_solar_bess_executive_intelligence.html
source_modified: 2026-10-23 13:27
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js)
research_prompt: none (first-round report the user ran before our research prompts)
stated_scope: "C&I Solar & BESS Intelligence Hub — RPVSP + RPVI EPCC Strategic Command Platform (2026–2030); Designed for SEDA RPVSP + RPVI Dual-Licensed Contractors. HTML comment: executive decision-making and analytical intelligence dashboard tailored for Malaysian SEDA RPVSP + RPVI dual-licensed EPCC operators, organised into 7 thematic operational domains."
stated_sources: "Malaysia C&I Solar & BESS Strategic Intelligence Hub • Designed for SEDA RPVSP + RPVI Dual-Licensed Contractors / Fully compliant with Energy Commission (ST), SEDA, TNB RP4, PETRA CRESS, and LHDN GITA Guidelines (2026)"
as_of: "No explicit as-of date. Dates stated: NEM 3.0 closed 30 June 2025; RP4 implemented 1 July 2025; ATAP / Enhanced SELCO pathways effective 1 January 2026 (Mandatory BESS for SELCO > 1 MWac from 1 Jan 2026); CRESS Acceleration Package 18 September 2026; fiscal incentive deadline 31 December 2026; CRESS COD deadline 31 December 2028; horizon 2026–2030."
sections: [Executive Pulse, ATAP vs SELCO, RP4 & BESS Simulator, CRESS Open Access, Tax Shields & Cliff, CAS & BOMBA Rules, EPCC Playbook]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R1 — Malaysia C&I Solar PV & BESS Strategic Intelligence Hub (2026–2030)

> Faithful, complete markdown extract of `malaysia_c_i_solar_bess_executive_intelligence.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- TNB RP4 Peak window is **2:00 PM – 10:00 PM**, 8 hours/day Mon–Fri; Off-Peak "expanded by 80% to 128 hrs/wk" (Section 1).
- MV Peak Maximum Demand charge under RP4 is **RM 89.27 – 97.06 /kW**, "+115% to +201% increase over legacy tariffs" (Sections 1, 3; chart: legacy 30.30 / 45.10 vs RP4 89.27 / 97.06 for MV Gen / MV TOU).
- NEM 3.0 closed 30 June 2025; from 1 January 2026 two mutually exclusive behind-the-meter pathways: **Solar ATAP** (GP/ST/No. 60/2025; export credited at Average SMP ~18.8–24.8 sen/kWh, capped at 1 MWac) and **Enhanced SELCO** (GP/ST/No. 51/2024 Pin. 1/2026; zero export, no capacity cap, RM 12/kWp/month Standby Charge and Mandatory BESS above 1 MWac) (Section 2).
- ATAP MAQ (kWh) = Capacity (kWac) × 5 Hours × Days in Month; default 800 kWac × 30 days = 120,000 kWh, worth RM 22,932 at RM 0.1911/kWh SMP (Section 2).
- Solar alone does not cut billed peak MD on an MV factory; a 400 kW BESS shaving the 2 PM – 10 PM peak saves RM 97.06/kW × 400 kW = RM 38,824/month (RM 465,888/year) in the simulator (hard-coded result; Section 3).
- **18 September 2026 CRESS Acceleration Package**: firm-supply System Access Charge cut from 25 sen/kWh to **14 sen/kWh**; plants must have ≥50% / 4-hour BESS, minimum 10-year PPAs, COD by **31 December 2028**; non-firm (solar without BESS) SAC 45 sen/kWh (Section 4).
- CRESS needs 5 mandatory agreements: BESC, CRESA, RE SAA, Back-feed Agreement, NEDA Agreement (Deed of Accession) (Section 4).
- CRESS calculator default: 38.0 sen/kWh PPA − 14 sen SAC = 24.0 sen/kWh net; 75 GWh/yr → RM 18.00 Mil/yr; 14.6% off-taker saving vs HV Tariff C4 Peak Rate 44.52 sen/kWh (Section 4).
- Fiscal "cliff" on **31 December 2026**: 100% GITA (Tier 1) for BESS, 60% GITA (Tier 2) for solar PV, 70% GITE income tax exemption for Solar Leasing; stacking GITA with Capital Allowance recovers **38.4% of Solar PV capex** and **48.0% of BESS capex** at 24% tax (Section 5).
- Tax calculator default: RM 2,000,000 solar + RM 1,000,000 BESS → RM 1,248,000 total cash tax savings, RM 1,752,000 net effective capex (Section 5).
- TNB CAS fee by tier: RM 0 (≤72 kWac), RM 1,000 (>72–180), RM 5,000 (>180–425), RM 8,000 (>425–1,000), RM 15,000 – RM 20,000 (>1,000–5,000 kWac); ST Section 9 license mandatory above 72 kWac; BESS mandatory above 1,000 kWac (Section 6).
- SARE (tripartite via TNBX) carries a fixed 2 sen/kWh TNB fee (~6–8% of gross revenue); Private Bilateral Hybrid PPA pays RM 0 to TNB and allows shared-savings on MD peak shaving (Section 7).
- Four client archetypes: Q4 Tax Cliff buyers; LV C&I (Tariff B & D, payback 3.5–4.5 years against 50.68 sen/kWh + AFA); MV factories (Tariff C1/C2/E1/E2, hybrid BESS PPA); HV / data centres (CRESS, ≥30 MW solar + ≥50%/4-hr BESS, ~38 sen/kWh vs 44.52 sen C4 peak) (Section 7).

## 0. Page frame (header, navigation, HTML planning comments)

### Header
- Brand mark: "MY-SOLAR"
- Page heading: "C&I Solar & BESS Intelligence Hub"
- Subtitle: "RPVSP + RPVI EPCC Strategic Command Platform (2026–2030)"
- Status badges: "RP4 Active Paradigm"; "31 Dec 2026 Tax Cliff"

### Navigation tabs (report order; Executive Pulse is shown on load)
1. Executive Pulse
2. ATAP vs SELCO
3. RP4 & BESS Simulator
4. CRESS Open Access
5. Tax Shields & Cliff
6. CAS & BOMBA Rules
7. EPCC Playbook

### HTML comment: "Application Structure Plan" (author's design brief, not displayed)
Audience/purpose: "Designed as an executive decision-making and analytical intelligence dashboard tailored for Malaysian SEDA RPVSP + RPVI dual-licensed EPCC operators. Organised into 7 thematic operational domains:"
1. Executive Pulse & Agency Governance Matrix: Core policy direction, statutory roles (PETRA, ST, SEDA, TNB, MIDA, MGTC).
2. Behind-the-Meter Pathways (ATAP vs. Enhanced SELCO): Interactive rule matrix, MAQ formula calculator, 1MWac threshold, RM12/kWp standby & BESS rules.
3. TNB Tariff Overhaul (RP4) & BESS Peak Shaving Simulator: Interactive 24-hour load curve model, Peak window (2PM-10PM), MD charge surge (RM89.27-97.06/kW), dynamic peak shaving savings.
4. Front-of-Meter CRESS Open Access Framework: CRESS 5-contract structure, Sept 18, 2026 Acceleration Package (14 sen SAC, 10-yr PPA, Dec 31 2028 COD deadline), developer revenue calculator.
5. Fiscal Incentives & Dec 31, 2026 Tax Cliff Engine: Tiered GITA (100% BESS, 60% Solar), GITE 70% exemption, Capital Allowance stacking (38.4% Solar recovery, 48% BESS recovery), interactive tax shield calculator.
6. Technical Interconnection & BOMBA Guidelines: CAS study fee matrix, ST Section 9 licenses, PEPC endorsement rules, BOMBA fire safety & thermal runaway compliance.
7. Commercial Playbook & Client Pitch Generator: SARE vs Private Bilateral PPA comparison, 4-Archetype strategy matrix, client proposal blueprint generator.

### HTML comment: "Visualization & Content Choices" (not displayed)
- RP4 24-Hour Load Curve: Interactive Chart.js Line Chart with peak window highlights to visualize MD shaving and solar shifting economics (Canvas-based).
- Tariff Rate Structure: Chart.js Bar Chart comparing Legacy vs RP4 Energy and MD charges across LV, MV, and HV tariffs (Canvas-based).
- Tax Recovery Stack: Chart.js Stacked Bar Chart illustrating GITA + Capital Allowance cash tax shield recovery (38.4% for Solar, 48% for BESS) (Canvas-based).
- CRESS SAC Comparison: Chart.js Bar Chart highlighting the 44% tariff reduction in wheeling charges under the Sept 2026 Acceleration Package (Canvas-based).
- Interactive Calculators: Pure Vanilla JS reactive state components for MAQ caps, Tariff Savings, GITA Tax Shield, CRESS Net Returns, and CAS Fee lookup.
- Icons & Elements: Styled HTML/Tailwind containers and Unicode symbols (NO SVG, NO Mermaid JS).

Other comments: "Chosen Palette: Warm Neutral Slate (Slate Blue, Warm Neutral Gray, Emerald Green, Amber Gold)"; "CONFIRMATION: NO SVG graphics used. NO Mermaid JS used."

## 1. Executive Pulse — "Executive Summary: The Post-NEM Regulatory & Economic Paradigm"

Malaysia's Commercial & Industrial (C&I) solar landscape in 2026 has transitioned away from volumetric Net Energy Metering (NEM 3.0) subsidies toward unbundled, grid-stabilized self-consumption (**Solar ATAP** and **Enhanced SELCO**) and open-access wheeling (**CRESS**). Under Tenaga Nasional Berhad's **Regulatory Period 4 (RP4)** tariff overhaul and the strict **31 December 2026 fiscal incentive cliff**, dual-licensed **RPVSP** (Service Provider) and **RPVI** (Investor) contractors must integrate **Battery Energy Storage Systems (BESS)** to capture Maximum Demand peak-shaving revenue and protect project bankability.

### KPI cards

| Card | Headline value | Sub-text |
|---|---|---|
| TNB RP4 Peak Window | 2:00 PM – 10:00 PM | 8 Hours/Day Mon–Fri (Off-Peak expanded by 80% to 128 hrs/wk) |
| MV Maximum Demand Surge | RM 89.27 – 97.06 /kW | +115% to +201% increase over legacy tariffs under RP4 |
| CRESS Firm SAC Wheeling Fee | 14 sen /kWh | Sept 18, 2026 Acceleration Package (Reduced from 25 sen) |
| Combined Tax Shield (BESS) | 48.0% of Capex | 100% GITA Tier 1 + 100% Capital Allowance (Closes 31 Dec 2026) |

### Malaysian C&I Regulatory & Statutory Governance Architecture

| Agency | Role tag | Description (verbatim) |
|---|---|---|
| PETRA | Policy Ministry | Ministry of Energy Transition & Water Transformation. Sets national capacity quotas (Solar ATAP, GREENS MADANI), CRESS acceleration packages, and long-term targets (70% RE by 2050). |
| Suruhanjaya Tenaga (ST) | Technical Regulator | Issues binding guidelines (Solar ATAP, SELCO, CRESS), grants Section 9 Generating Licenses (>72 kWac), regulates Class A Contractors and Competent Persons under Electricity Supply Act 1990. |
| SEDA Malaysia | Quota & Registry | Administers the eATAP portal, manages RPVSP and RPVI directories, certifies GCPV/OGPV Qualified Persons, and verifies first invoices for GITE Solar Leasing tax exemptions. |
| TNB / Single Buyer / GSO | Grid & Utility | Conducts Connection Assessment Studies (CAS), manages bi-directional metering, enforces RP4 tariff schedules, operates NEDA, and administers SARE contracts via TNBX. |
| MGTC (MyHIJAU) | Tax Verifier | Evaluates and approves GITA Asset (Own Consumption) applications for solar (60% Tier 2) and BESS (100% Tier 1). Manages MyHIJAU green product directory listings. |
| MIDA & LHDN | Investment & Tax | MIDA evaluates GITA Project and GITE Solar Leasing applications. LHDN enforces statutory income set-offs (70% limit per year) and Capital Allowance claims. |

## 2. ATAP vs SELCO — "Behind-the-Meter Regulatory Framework: Solar ATAP vs. Enhanced SELCO"

Following the closure of NEM 3.0 on 30 June 2025, Suruhanjaya Tenaga established two mutually exclusive behind-the-meter pathways effective 1 January 2026. **Solar ATAP** (GP/ST/No. 60/2025) allows export credits at Average SMP (~18.8–24.8 sen/kWh) but caps system capacity at 1 MWac. **Enhanced SELCO** (GP/ST/No. 51/2024 Pin. 1/2026) permits unlimited system capacity for zero-export sites, but enforces a **RM 12/kWp/month Standby Charge** and **Mandatory BESS** for installations exceeding 1 MWac.

### Regulatory Framework Feature Comparison (Effective 1 January 2026)

| Parameter | Solar ATAP (GP/ST/No. 60/2025) | Enhanced SELCO ≤ 1 MWac | Enhanced SELCO > 1 MWac |
|---|---|---|---|
| System Capacity Limit | 100% 12-mo Avg MD, **Hard Cap 1,000 kW (1 MWac)** | Sized to actual load (Up to **1 MWac**) | No Cap (85% MD limit abolished) |
| Allowed Mounting | Rooftop, Carpark, Covered Walkways | Rooftop, Ground, Floating (Water Bodies) | Rooftop, Ground, Floating (Water Bodies) |
| Grid Export & Settlement | Export allowed; credited at **Average SMP** (~19 sen/kWh) on Base Energy Charge ONLY | Strictly Prohibited (Reverse Power Relay) | Strictly Prohibited (Reverse Power Relay) |
| Credit Rollover | NONE (Forfeited monthly; use-it-or-lose-it) | N/A (Zero export) | N/A (Zero export) |
| TNB Standby Charge | EXEMPT (RM 0) | EXEMPT (RM 0) | RM 12 / kWp / month |
| Mandatory BESS Rule | Optional (For peak shaving / ROI) | Optional (For peak shaving / ROI) | MANDATORY BESS (From 1 Jan 2026) |
| Application Portal & Fee | SEDA `eATAP` (**RM 7.50 / kW** fee) + TNB CAS | SEDA registration + TNB CAS + ST Notification | SEDA registration + TNB CAS + ST License |

### Solar ATAP Monthly Maximum Allowable Quantity (MAQ) Calculator
"Calculate the upper ceiling of export energy eligible for bill offset under ATAP rules: `MAQ (kWh) = Capacity (kWac) × 5 Hours × Days in Month`"

- Inputs: "Installed Capacity (kWac) [Max 1000]:" (default 800); "Billing Period Days:" (default 30); "Assumed Avg SMP (RM/kWh):" (default 0.1911).
- Outputs: "Monthly MAQ Cap" (shown 120,000 kWh); "Max Gross Export Value" (shown RM 22,932); "ATAP Rule Constraint": "Cannot exceed actual monthly grid energy import (kWh). Forfeited if unused."
- Full logic: see "Calculators and interactive logic" → Calculator 1.

## 3. RP4 & BESS Simulator — "TNB RP4 Tariff Overhaul & C&I BESS Peak Shaving Economics"

Under TNB's Regulatory Period 4 (RP4) schedule implemented on 1 July 2025, consumption charges were itemised into Energy, Capacity, Network, Retail, and Automatic Fuel Adjustment (AFA) components. While Medium Voltage (MV) volumetric energy rates dropped, **Peak Demand hours were shifted to 2:00 PM – 10:00 PM**, and Peak Maximum Demand charges surged to **RM 89.27–97.06/kW**. Because morning solar PV generation falls in TNB's Off-Peak window (10 PM – 2 PM), **BESS integration is essential** to store excess solar and shave peak demand during the 2 PM – 10 PM window.

### 24-Hour Factory Profile & BESS Peak Shaving Simulator
"Simulate solar PV self-consumption and battery discharge during the 2:00 PM – 10:00 PM TNB Peak window."

- Mode buttons: "1. Baseline Grid Load"; "2. With Solar PV Only"; "3. Solar + BESS Peak Shaving" (the third is styled as the highlighted button).
- Line chart of grid power draw (see Charts → Chart 1).
- Output cards (text shown before any button is clicked):

| Card | Value shown | Sub-text shown |
|---|---|---|
| Billed Peak Demand (2PM-10PM) | 1,200 kW | Unmitigated baseline peak |
| Monthly MD Charge Rate (Tariff E2) | RM 97.06 / kW (static) | TNB RP4 Peak MD Rate |
| Monthly Demand Shaving Savings | RM 0 / month | Select Hybrid Mode to activate |
| Annualized Peak Demand Offset | RM 0 / year | Direct bottom-line RP4 savings |

- Full logic and per-mode outputs: see Calculator 2.

### RP4 Peak Maximum Demand Charges Across C&I Tariff Categories
"Comparison of monthly peak demand charges per kW under RP4 for Medium and High Voltage commercial and industrial consumers." Bar chart: see Charts → Chart 2.

## 4. CRESS Open Access — "Front-of-Meter Open Access: CRESS & The September 18, 2026 Acceleration Package"

The **Corporate Renewable Energy Supply Scheme (CRESS)** allows Renewable Energy Developers (REDs) to sell green power directly to High Voltage (HV) and Medium Voltage (MV) corporate off-takers across Peninsular Malaysia's grid via NEDA. The landmark **18 September 2026 CRESS Acceleration Package** slashed the System Access Charge (SAC) for firm supply from 25 sen/kWh down to **14 sen/kWh**, establishing strict rules: plants must incorporate **≥50% / 4-hour BESS**, sign **minimum 10-year PPAs**, and hit COD by **31 December 2028**.

### The 5 Mandatory CRESS Agreements

| # | Agreement | Description (verbatim) |
|---|---|---|
| 1 | Bilateral Energy Supply Contract (BESC) | Direct PPA between RED and Green Consumer (Min 10-year tenure under Acceleration Package). |
| 2 | Corporate RE Supply Agreement (CRESA) | Top-up and backup retail supply agreement between Green Consumer and TNB. |
| 3 | RE Supply Access Agreement (RE SAA) | Grid interconnection and transmission access contract between RED and TNB Grid Owner. |
| 4 | Back-feed Agreement | Governs auxiliary station power imported by the solar plant and BESS facility from TNB. |
| 5 | NEDA Agreement (Deed of Accession) | Governs day-ahead dispatch scheduling with Single Buyer and SAC settlement. |

### CRESS Developer Net Generation Revenue Calculator (header tag: "14 sen/kWh SAC Active")
- Inputs: "Contracted PPA Price to Off-taker (sen/kWh):" (default 38.0; helper text "Competes against HV Tariff C4 Peak Rate (44.52 sen/kWh)"); "System Access Charge (SAC) Category:" (three options, default 14 sen firm); "Annual Green Energy Generation (GWh):" (default 75); "Mandatory BESS Requirement:" fixed text "50% GEP MW / 4-Hours Duration".
- Outputs (placeholder text in HTML): "Net Developer Revenue" 24.0 sen /kWh; "Annual Gross Cashflow" RM 18.0 Mil; "Off-taker Savings vs Tariff" 14.6% Offset.
- SAC comparison bar chart below the outputs: see Charts → Chart 3.
- Full logic: see Calculator 3.

## 5. Tax Shields & Cliff — "Corporate Tax Architecture: Navigating the 31 December 2026 Fiscal Cliff"

Malaysia's green tax incentive architecture—jointly administered by **MGTC**, **MIDA**, and **LHDN**—provides a massive capital subsidy for C&I Solar and BESS. However, the current framework faces a hard statutory deadline on **31 December 2026**. By stacking **Green Investment Tax Allowance (GITA)** with standard **Capital Allowance (CA)**, corporate buyers recover **38.4% of Solar PV Capex** and **48.0% of BESS Capex** through corporate income tax offsets.

### Tax category cards

| Tag | Heading | Text (verbatim) |
|---|---|---|
| MGTC GITA Asset (Tier 1) | 100% GITA for BESS | 100% tax allowance on qualifying battery storage Capex. Sets off up to 70% of statutory income per year. Must be commissioned and submitted to MGTC before **31 Dec 2026**. |
| MGTC GITA Asset (Tier 2) | 60% GITA for Solar PV | 60% tax allowance on qualifying solar rooftop Capex for own consumption. Combine with Capital Allowance for 38.4% tax shield. MGTC window closes **31 Dec 2026**. |
| MIDA GITE Solar Leasing | 70% Income Tax Exemption | Exempts 70% of statutory income for SEDA-registered RPVIs offering Solar PPAs (>3 MW capacity) for 5 to 10 years. Must apply to MIDA before **31 Dec 2026**. |

### Effective Tax Shield Recovery Stack (% of Capex)
Stacked bar chart: see Charts → Chart 4.

### Client Tax Recovery & Net Capex Calculator
- Inputs: "Solar PV Investment (RM):" (default 2000000); "BESS Investment (RM):" (default 1000000).
- Breakdown lines (placeholder = computed at defaults):

| Line label | Value at defaults |
|---|---|
| Solar GITA (60% × 24% Tax Rate): | RM 288,000 |
| Solar Capital Allowance (100% × 24%): | RM 480,000 |
| BESS GITA Tier 1 (100% × 24% Tax Rate): | RM 240,000 |
| BESS Capital Allowance (100% × 24%): | RM 240,000 |
| Total Cash Tax Savings | RM 1,248,000 |
| Net Effective Capex | RM 1,752,000 |

- Full logic: see Calculator 4.

## 6. CAS & BOMBA Rules — "Technical Grid Interconnection, Licensing & BOMBA Safety Regulations"

Connecting C&I solar and BESS systems in Peninsular Malaysia requires compliance with **Electricity Regulations 1994**, **MS IEC 60364**, and Suruhanjaya Tenaga licensing thresholds. Furthermore, installing rooftop solar and lithium-ion BESS on designated industrial premises modifies the building's fire hazard profile, mandating formal **Jabatan Bomba dan Penyelamat Malaysia (JBPM / BOMBA)** consultations and thermal runaway safety integration.

### TNB Interconnection Study (CAS) & ST Generating License Matrix

| Capacity Tier (kWac) | Required Interconnection Study | Regulated CAS Fee | ST Section 9 License | TNB Metering Fee |
|---|---|---|---|---|
| 1 kW – 72 kWac | Exempt (CCC for domestic >15kW) | RM 0 | Exempt (Sec 54 Notification) | RM 0 (OPC) / RM 1,530 (LPC) |
| >72 kW – 180 kWac | Connection Assessment Study (CAS) | RM 1,000 | Mandatory ST License | RM 1,530 (LV) / RM 2,330 (MV) |
| >180 kW – 425 kWac | Connection Assessment Study (CAS) | RM 5,000 | Mandatory ST License | RM 1,530 (LV) / RM 2,330 (MV) |
| >425 kW – 1,000 kWac | Connection Assessment Study (CAS) | RM 8,000 | Mandatory ST License | RM 2,330 (MV) |
| >1,000 kW – 5,000 kWac | Connection Assessment Study (CAS) | RM 15,000 – RM 20,000 | License + Mandatory BESS | RM 2,330 (MV) |

### JBPM (BOMBA) Fire Safety & BESS Compliance
- **Designated Premises Fire Certificate:** Factories, warehouses, and shopping complexes must consult BOMBA prior to solar/BESS install to update their annual Fire Certificate (Form I).
- **Rooftop Firefighting Access:** PV arrays must maintain clear perimeter setbacks and access walkways deducted from usable roof space.
- **BESS Thermal Runaway Mitigation:** Enclosures must integrate SIRIM/IEC-certified fire suppression systems and gas detection.
- **Direct Station Alarm Linkage:** Automatic fire alarm switchboards must link directly to the nearest BOMBA Fire Station.

### Electrical & Structural Mandates
- **PEPC Endorsement:** Mounting structure C&S drawings and electrical single-lines must be endorsed by a BEM-registered Professional Engineer (PEPC).
- **Anti-Islanding Protection:** Inverters certified to MS IEC 62109 must trip within 2 seconds upon loss of TNB grid supply.
- **Reverse Power Relay:** Mandatory on all SELCO systems to prevent accidental export to TNB distribution lines.
- **In-House Competent Personnel:** RPVSP must deploy certified GCPV Qualified Persons, Class A Chargemen, and CIDB G7 registered personnel.

## 7. EPCC Playbook — "Dual-Licensed EPCC + RPVI Strategic Commercial Playbook"

Holding both **SEDA RPVSP** (Service Provider) and **SEDA RPVI** (Investor) credentials allows an operator to capture both upfront EPCC engineering margins and long-term PPA cashflows. This section compares **SARE** vs **Private Bilateral PPAs** and provides a dynamic Client Archetype Decision Matrix to structure high-conversion customer proposals.

### SARE vs Private Bilateral PPA

| Item | SARE (Tripartite via TNBX) — tag "TNB Billing" | Private Bilateral Hybrid PPA / Lease — tag "Direct Contracting" |
|---|---|---|
| Parties | Prosumer, RPVI Investor, and TNB. | Direct contract between C&I Customer and RPVI. |
| Billing & Collection | Consolidated into monthly TNB bill; TNB collects and remits payment to RPVI. | Direct invoicing by RPVI; RPVI manages credit risk. |
| Service Fee | TNB charges a fixed **2 sen/kWh** fee (~6–8% of gross revenue). | **RM 0 fee to TNB** (Saves full 2 sen/kWh margin for RPVI). |
| Default Enforcement / Contractual Flexibility | Default Enforcement: High bankability; non-payment triggers TNB power disconnection. | Contractual Flexibility: High; allows **shared-savings split on Maximum Demand (RM/kW) peak shaving**. |
| Best Used For | Pure rooftop solar PV projects on Tariff B, D, C1, E1. | Hybrid Solar + BESS installations on Tariff C2, E2, E3. |

### Strategic Origination Playbook by Client Archetype
"Select a target client archetype to view the optimal regulatory pathway, engineering architecture, and sales pitch narrative."

Archetype buttons: "1. Q4 Tax Cliff" (Outright Ready Buyers); "2. Low Voltage C&I" (Tariff B & D (Retail/SMEs)); "3. MV Medium Factory" (Tariff C1/C2/E1/E2); "4. High Voltage / DC" (CRESS Off-takers). The card shown on load is archetype 3 (MV Medium Factory). Full card text for all four: see "Embedded data tables" → Table E.

## 8. Footer
- "Malaysia C&I Solar & BESS Strategic Intelligence Hub • Designed for SEDA RPVSP + RPVI Dual-Licensed Contractors"
- "Fully compliant with Energy Commission (ST), SEDA, TNB RP4, PETRA CRESS, and LHDN GITA Guidelines (2026)"

## Charts

### Chart 1 — 24-hour load curve (canvas `loadCurveChart`)
- Location: Section 3, "24-Hour Factory Profile & BESS Peak Shaving Simulator".
- Type: line (filled), one dataset whose data is replaced by the mode buttons.
- Dataset label: "Grid Power Draw (kW)". Legend at top. Tooltip text: " Grid Load: {value} kW".
- Y axis title: "Power Demand (kW)" (begins at zero). X axis title: "Hour of Day (00:00 - 23:00)".
- X labels: "0:00", "1:00", … "23:00" (24 hourly labels).
- Values (kW) per mode. Baseline is the array in the code; Solar-only and Hybrid are computed by the code as max(50, baseline − solar) and max(50, baseline − solar − BESS). Input arrays are in Embedded data table A.

| Hour | Baseline (shown on load) | With Solar PV Only | Solar + BESS Peak Shaving |
|---|---|---|---|
| 0:00 | 300 | 300 | 300 |
| 1:00 | 300 | 300 | 300 |
| 2:00 | 300 | 300 | 300 |
| 3:00 | 300 | 300 | 300 |
| 4:00 | 300 | 300 | 300 |
| 5:00 | 400 | 400 | 400 |
| 6:00 | 700 | 650 | 650 |
| 7:00 | 950 | 750 | 750 |
| 8:00 | 1100 | 650 | 650 |
| 9:00 | 1150 | 450 | 450 |
| 10:00 | 1200 | 350 | 350 |
| 11:00 | 1180 | 280 | 280 |
| 12:00 | 1100 | 250 | 250 |
| 13:00 | 1150 | 450 | 450 |
| 14:00 | 1200 | 750 | 350 |
| 15:00 | 1200 | 1000 | 600 |
| 16:00 | 1180 | 1130 | 730 |
| 17:00 | 1150 | 1150 | 750 |
| 18:00 | 1100 | 1100 | 700 |
| 19:00 | 900 | 900 | 500 |
| 20:00 | 700 | 700 | 400 |
| 21:00 | 500 | 500 | 500 |
| 22:00 | 350 | 350 | 350 |
| 23:00 | 300 | 300 | 300 |

### Chart 2 — RP4 MD charges by tariff category (canvas `tariffChart`)
- Location: Section 3, "RP4 Peak Maximum Demand Charges Across C&I Tariff Categories".
- Type: grouped bar. Legend at top. Y axis title: "Demand Charge Rate (RM / kW / Month)" (begins at zero). No x-axis title.

| Category label | Legacy MD Charge (RM/kW) | RP4 Combined MD Charge (RM/kW) |
|---|---|---|
| MV Gen (C1/E1) | 30.30 | 89.27 |
| MV TOU (C2/E2) | 45.10 | 97.06 |
| HV Gen (C3) | 29.20 | 31.21 |
| HV TOU (C4/E3) | 43.60 | 44.82 |

### Chart 3 — CRESS SAC comparison (canvas `cressChart`)
- Location: Section 4, below the CRESS calculator outputs. Static (does not react to the calculator).
- Type: bar, single dataset "System Access Charge (SAC sen/kWh)"; legend hidden. Tooltip text: " SAC Rate: {value} sen/kWh". Y axis title: "SAC Fee (sen/kWh)" (begins at zero).

| Label | SAC (sen/kWh) |
|---|---|
| Non-Firm (Solar Only) | 45 |
| Pre-Sept 2026 Firm | 25 |
| Sept 18, 2026 Accelerated Firm | 14 |

### Chart 4 — Effective Tax Shield Recovery Stack (canvas `taxStackChart`)
- Location: Section 5, "Effective Tax Shield Recovery Stack (% of Capex)".
- Type: stacked bar (x and y stacked). Legend at top. Y axis title: "Tax Recovery (% of System Capex)", 0 to max 60. Tooltip footer: " Total Tax Recovery: {sum of tooltip items, 1 dp}%".
- Code comments: "60% * 24% = 14.4%; 100% * 24% = 24.0%" (GITA series); "100% * 24% = 24%" (CA series).

| Label | GITA Tax Shield (% of Capex) | Capital Allowance Shield (% of Capex) | Stack total |
|---|---|---|---|
| Solar PV (Tier 2 GITA) | 14.4 | 24.0 | 38.4 |
| BESS Storage (Tier 1 GITA) | 24.0 | 24.0 | 48.0 |

## Calculators and interactive logic

### Calculator 1 — Solar ATAP Monthly MAQ Calculator (`calculateMAQ`)
- Location: Section 2 (ATAP vs SELCO). Runs on page load and on every input change.
- Inputs:

| Element | Label | Type | Default | Min | Max | Step | JS fallback if blank/0/NaN |
|---|---|---|---|---|---|---|---|
| maq-capacity | Installed Capacity (kWac) [Max 1000]: | number | 800 | 1 | 1000 | (none) | 0 |
| maq-days | Billing Period Days: | number | 30 | 28 | 31 | (none) | 30 |
| maq-smp | Assumed Avg SMP (RM/kWh): | number | 0.1911 | (none) | (none) | 0.005 | 0.1911 |

- Constant: 5 hours per day.
- Formula:
  ```
  maqKwh   = cap * 5 * days
  grossVal = maqKwh * smp
  res-maq-kwh   = maqKwh.toLocaleString() + " kWh"
  res-maq-value = "RM " + grossVal (0 decimals, thousands separators)
  ```
- Static output text: "ATAP Rule Constraint — Cannot exceed actual monthly grid energy import (kWh). Forfeited if unused."
- Outputs at default inputs (computed by running the code logic): Monthly MAQ Cap = 120,000 kWh; Max Gross Export Value = RM 22,932 (exact 22,932.00). Same as the HTML placeholders.
- Additional computed points: 1,000 kWac × 31 days → 155,000 kWh, RM 29,621 (29,620.5); 800 kWac × 28 days → 112,000 kWh, RM 21,403.

### Calculator 2 — 24-Hour Load Curve & BESS Peak Shaving Simulator (`initLoadCurveChart`, `updateLoadProfile(mode)`)
- Location: Section 3. Input: three mode buttons (no numeric inputs). Data arrays: Embedded data table A.
- Page load: `initLoadCurveChart()` draws the baseline array; `updateLoadProfile` is NOT called, so outputs keep the HTML placeholders ("1,200 kW", "Unmitigated baseline peak", "RM 0 / month", "Select Hybrid Mode to activate", "RM 0 / year", "Direct bottom-line RP4 savings"), while button 3 is styled as highlighted.
- Constant: MD rate RM 97.06/kW (code comment "Tariff E2 MD Rate"); floor of 50 kW on every hourly value.
- Branches (exact code behaviour and text):

| Mode (button) | Curve plotted | billedMD (hard-coded) | monthlySavings | sim-md-desc text | sim-md-savings-sub text | Code comment |
|---|---|---|---|---|---|---|
| 'baseline' (1. Baseline Grid Load) | baseLoad | 1200 | 0 | Unmitigated baseline peak | Select Hybrid Mode to activate | — |
| 'solar' (2. With Solar PV Only) | max(50, baseLoad[i] − solarGen[i]) | 1200 | 0 | Solar drops off during late peak | Solar alone fails to reduce Peak MD | "Morning solar offsets load, but 2PM-10PM peak remains unmitigated at 5:00 PM"; "Peak occurs at 16:00 - 17:00 when solar drops off" |
| 'hybrid' (3. Solar + BESS Peak Shaving) | max(50, baseLoad[i] − solarGen[i] − bessDischarge[i]) | 800 | 400 × 97.06 | BESS Shaved 400 kW during Peak | RM 97.06/kW × 400 kW Shaved | "Solar + 400 kW BESS Discharge during 2:00 PM - 10:00 PM window"; "Shaved 400 kW of Peak Demand"; "Tariff E2 MD Rate" |

- Output formatting after a button click:
  ```
  sim-billed-md      = billedMD.toLocaleString() + " kW"
  sim-md-savings     = "RM " + monthlySavings (0 dp) + " / mo"
  sim-annual-savings = "RM " + (monthlySavings * 12) (0 dp) + " / yr"
  sim-annual-sub     unchanged ("Direct bottom-line RP4 savings")
  ```
- Outputs per mode (computed by running the code logic):

| Mode | Billed Peak Demand shown | Monthly savings shown | Annual savings shown | Actual max of plotted curve within 14:00–21:00 (peak window 2 PM–10 PM) | Actual max over 24 h |
|---|---|---|---|---|---|
| Baseline | 1,200 kW | RM 0 / mo | RM 0 / yr | 1,200 kW (at 14:00 and 15:00) | 1,200 kW |
| Solar only | 1,200 kW | RM 0 / mo | RM 0 / yr | 1,150 kW (at 17:00) | 1,150 kW |
| Solar + BESS | 800 kW | RM 38,824 / mo | RM 465,888 / yr | 750 kW (at 17:00) | 750 kW (at 07:00 and 17:00) |

- Energy totals from the arrays (computed): baseline 19,010 kWh/day; solar 5,400 kWh/day; BESS discharge 2,700 kWh/day. No BESS charging is modelled.

### Calculator 3 — CRESS Developer Net Generation Revenue Calculator (`calculateCRESS`)
- Location: Section 4. Runs on page load and on input/select change.
- Inputs:

| Element | Label | Type | Default | Step / options | JS fallback if blank/0/NaN |
|---|---|---|---|---|---|
| cress-ppa | Contracted PPA Price to Off-taker (sen/kWh): | number | 38.0 | step 0.5 | 38.0 |
| cress-sac | System Access Charge (SAC) Category: | select | 14 (first option) | see options below | 14.0 |
| cress-gen | Annual Green Energy Generation (GWh): | number | 75 | step 5 | 75 |

  SAC options (value: label):
  - 14: "Firm Supply (Solar + ≥50%/4-hr BESS) - 14 sen/kWh"
  - 25: "Legacy Firm Supply (Pre-Sept 2026) - 25 sen/kWh"
  - 45: "Non-Firm Supply (Solar without BESS) - 45 sen/kWh"
- Constant: hvTariffPeak = 44.52 (sen/kWh; helper text "Competes against HV Tariff C4 Peak Rate (44.52 sen/kWh)"). Fixed display: "Mandatory BESS Requirement: 50% GEP MW / 4-Hours Duration".
- Formula:
  ```
  netRate        = ppa - sac                                  // sen/kWh
  annualRevMil   = (gen * 1,000,000 * (netRate / 100)) / 1,000,000   // RM million
  savingsPercent = ((44.52 - ppa) / 44.52) * 100
  res-cress-net-rate = netRate.toFixed(1) + " sen /kWh"     (label "Net Developer Revenue")
  res-cress-annual   = "RM " + annualRevMil.toFixed(2) + " Mil"  (label "Annual Gross Cashflow")
  res-cress-savings  = savingsPercent.toFixed(1) + "% Offset"    (label "Off-taker Savings vs Tariff")
  ```
- Outputs at default inputs (computed by running the code logic): 24.0 sen /kWh; RM 18.00 Mil; 14.6% Offset (14.645…%). HTML placeholders were "24.0 sen /kWh", "RM 18.0 Mil", "14.6% Offset".
- Other SAC options at default PPA 38.0 and 75 GWh (computed): SAC 25 → 13.0 sen /kWh, RM 9.75 Mil, 14.6% Offset; SAC 45 → -7.0 sen /kWh, RM -5.25 Mil, 14.6% Offset.

### Calculator 4 — Client Tax Recovery & Net Capex Calculator (`calculateTax`)
- Location: Section 5. Runs on page load and on input change.
- Inputs:

| Element | Label | Type | Default | Step | JS fallback |
|---|---|---|---|---|---|
| tax-solar-capex | Solar PV Investment (RM): | number | 2000000 | 100000 | 0 |
| tax-bess-capex | BESS Investment (RM): | number | 1000000 | 100000 | 0 |

- Constants: solar GITA rate 0.60; BESS GITA rate 1.00; Capital Allowance rate 1.00 (both assets); tax rate 0.24.
- Formula:
  ```
  solarGita    = solarCapex * 0.60 * 0.24
  solarCa      = solarCapex * 1.00 * 0.24
  bessGita     = bessCapex  * 1.00 * 0.24
  bessCa       = bessCapex  * 1.00 * 0.24
  totalSavings = solarGita + solarCa + bessGita + bessCa
  netCapex     = (solarCapex + bessCapex) - totalSavings
  all outputs  = "RM " + value (0 dp, thousands separators)
  ```
- Outputs at default inputs (computed by running the code logic): Solar GITA RM 288,000; Solar CA RM 480,000; BESS GITA RM 240,000; BESS CA RM 240,000; Total Cash Tax Savings RM 1,248,000; Net Effective Capex RM 1,752,000. Same as the HTML placeholders.
- Implied recovery rates: solar 0.60×0.24 + 1.00×0.24 = 38.4% of capex; BESS 1.00×0.24 + 1.00×0.24 = 48.0% of capex.

### Selector 5 — Client Archetype Blueprint (`selectArchetype(key)`)
- Location: Section 7. Four buttons; `selectArchetype('mvmfg')` runs on page load. Buttons do not change visual state.
- Output card template: title; badge "Strategic Blueprint"; four labelled fields "Optimal Regulatory Pathway:" (reg), "Recommended Commercial Model:" (comm), "Core Engineering Strategy:" (tech), "Key Sales Pitch Narrative:" (pitch).
- Branches: one per key (taxcliff, lvsme, mvmfg, hvdc); full text in Embedded data table E.

### Tab switcher (`switchTab(tabId)`)
- Sections: dashboard, pathways, tariff, cress, tax, tech, playbook. Hides all, shows the selected one. Default: dashboard.

## Embedded data tables

### Table A — Load-curve arrays (`updateLoadProfile`; baseline also in `initLoadCurveChart`)

| Hour index | baseLoad (kW) | solarGen (kW) | bessDischarge (kW) |
|---|---|---|---|
| 0 | 300 | 0 | 0 |
| 1 | 300 | 0 | 0 |
| 2 | 300 | 0 | 0 |
| 3 | 300 | 0 | 0 |
| 4 | 300 | 0 | 0 |
| 5 | 400 | 0 | 0 |
| 6 | 700 | 50 | 0 |
| 7 | 950 | 200 | 0 |
| 8 | 1100 | 450 | 0 |
| 9 | 1150 | 700 | 0 |
| 10 | 1200 | 850 | 0 |
| 11 | 1180 | 900 | 0 |
| 12 | 1100 | 850 | 0 |
| 13 | 1150 | 700 | 0 |
| 14 | 1200 | 450 | 400 |
| 15 | 1200 | 200 | 400 |
| 16 | 1180 | 50 | 400 |
| 17 | 1150 | 0 | 400 |
| 18 | 1100 | 0 | 400 |
| 19 | 900 | 0 | 400 |
| 20 | 700 | 0 | 300 |
| 21 | 500 | 0 | 0 |
| 22 | 350 | 0 | 0 |
| 23 | 300 | 0 | 0 |

### Table B — Tariff chart data (`initTariffChart`)
Labels ['MV Gen (C1/E1)', 'MV TOU (C2/E2)', 'HV Gen (C3)', 'HV TOU (C4/E3)']; "Legacy MD Charge (RM/kW)" [30.30, 45.10, 29.20, 43.60]; "RP4 Combined MD Charge (RM/kW)" [89.27, 97.06, 31.21, 44.82]. (Tabulated in Chart 2.)

### Table C — CRESS SAC chart data (`initCressChart`)
Labels ['Non-Firm (Solar Only)', 'Pre-Sept 2026 Firm', 'Sept 18, 2026 Accelerated Firm']; "System Access Charge (SAC sen/kWh)" [45, 25, 14]. (Tabulated in Chart 3.)

### Table D — Tax stack chart data (`initTaxStackChart`)
Labels ['Solar PV (Tier 2 GITA)', 'BESS Storage (Tier 1 GITA)']; "GITA Tax Shield (% of Capex)" [14.4, 24.0]; "Capital Allowance Shield (% of Capex)" [24.0, 24.0]. (Tabulated in Chart 4.)

### Table E — Client archetype data object (`selectArchetype`)

| Key (button) | title | reg (Optimal Regulatory Pathway) | comm (Recommended Commercial Model) | tech (Core Engineering Strategy) | pitch (Key Sales Pitch Narrative) |
|---|---|---|---|---|---|
| taxcliff ("1. Q4 Tax Cliff" — Outright Ready Buyers) | Q4 2026 Tax Cliff Pipeline (Outright Capex Buyers) | SELCO ≤1 MWac or Solar ATAP (Fast-track commissioning) | Outright Purchase with MGTC Tier 1/2 GITA Asset Submission | Target COD before 31 Dec 2026 to ensure MGTC GITA/A application filing prior to statutory deadline. | Pitch 38.4% cash tax savings on Solar and 48% on BESS before the 31 Dec 2026 GITA window closes. |
| lvsme ("2. Low Voltage C&I" — Tariff B & D (Retail/SMEs)) | Low Voltage C&I (Tariff B & D: Retail, Warehouses, Light Industrial) | SELCO ≤1 MWac (7-day load) or Solar ATAP (5-day load) | Outright Capex or TNBX SARE Tripartite PPA (TNB Credit Protection) | Size strictly to daytime base load to displace full 50.68 sen/kWh + AFA volumetric tariff. | Simple payback of 3.5–4.5 years by offsetting bundled LV energy + network rates. |
| mvmfg ("3. MV Medium Factory" — Tariff C1/C2/E1/E2) — default on load | Medium Voltage C&I (Tariff C1, C2, E1, E2: Manufacturing & Process Plants) | Enhanced SELCO (≤1 MWac Voluntary BESS / >1 MWac Mandatory BESS) | Private Bilateral Hybrid PPA (Shared savings on Maximum Demand reduction) | Integrate BESS to shift 10AM-2PM off-peak solar to shave RM 89.27–97.06/kW MD charges during 2PM-10PM peak. | Standalone solar fails on MV due to off-peak morning rates. Hybrid BESS unlocks massive MD savings. |
| hvdc ("4. High Voltage / DC" — CRESS Off-takers) | High Voltage & Hyperscale Data Centres (Tariff C3, C4, E3) | CRESS Acceleration Package (≥30 MW Solar + ≥50%/4-hr BESS) | ≥10-Year Bilateral Energy Supply Contract (BESC) via ≥51% Local RED SPV | Lock in 14 sen/kWh Firm SAC. Fast-track EPCC engineering to hit mandatory 31 Dec 2028 COD deadline. | Deliver green power with 24/7 RECs at ~38 sen/kWh delivered cost against HV Tariff C4 peak rate (44.52 sen). |

## Links and cited documents

| Label as shown | URL or document ID | Where used |
|---|---|---|
| Tailwind CSS CDN (script, not a visible link) | https://cdn.tailwindcss.com | page head |
| Chart.js CDN (script, unversioned; not a visible link) | https://cdn.jsdelivr.net/npm/chart.js | page head |
| Solar ATAP guideline | GP/ST/No. 60/2025 | Section 2 intro and table header |
| Enhanced SELCO guideline | GP/ST/No. 51/2024 Pin. 1/2026 | Section 2 intro |
| Electricity Supply Act 1990 | Electricity Supply Act 1990 | Section 1 (ST card) |
| ST Section 9 Generating License | Section 9 (Electricity Supply Act 1990) | Section 1 (ST card), Section 6 table |
| Sec 54 Notification | Sec 54 | Section 6 table (≤72 kWac) |
| Electricity Regulations 1994 | Electricity Regulations 1994 | Section 6 intro |
| MS IEC 60364 | MS IEC 60364 | Section 6 intro |
| MS IEC 62109 (inverter certification, anti-islanding) | MS IEC 62109 | Section 6, Electrical & Structural Mandates |
| BOMBA annual Fire Certificate | Form I | Section 6, BOMBA list |
| CRESS Acceleration Package | 18 September 2026 package (no document ID given) | Sections 1, 4, 7 |
| RP4 tariff schedule (TNB Regulatory Period 4) | implemented 1 July 2025 (no document ID given) | Sections 1, 3 |
| eATAP portal (SEDA) | no URL given | Sections 1, 2 |
| MyHIJAU green product directory (MGTC) | no URL given | Section 1 |
| CIDB G7 registration; BEM-registered Professional Engineer (PEPC); SIRIM/IEC certification | no document IDs given | Section 6 |

No hyperlinks (href) to sources appear anywhere in the report.

## Extraction notes

- **31 Dec 2026 "tax cliff" framing.** The header badge, Section 1 summary/KPI, all three Section 5 cards (MGTC GITA Tier 1 BESS, MGTC GITA Tier 2 solar, MIDA GITE Solar Leasing) and the "Q4 Tax Cliff" archetype treat 31 Dec 2026 as a hard statutory deadline. The report contains no mention of Budget 2027 or any extension. The task brief says other reports in the set state Budget 2027 changed this; not verified by this extractor. Cross-check before relying on the deadline.
- **Tax shield stacking is simplistic.** The 38.4% (solar) and 48.0% (BESS) figures are GITA rate × 24% plus a 100% Capital Allowance × 24%, presented as immediate "Total Cash Tax Savings" and a "Net Effective Capex". The calculator ignores the 70%-of-statutory-income annual set-off cap that the report itself states (MIDA & LHDN card; Tier 1 card). It also ignores CA timing (no schedule is given; "100%" is applied up front), assumes enough taxable profit, and applies no discounting. The 24% tax rate is assumed, with no source. The footer cites "LHDN GITA Guidelines", while the body says MGTC/MIDA evaluate GITA.
- **Load-curve billed MD is hard-coded and does not match the plotted curves.** Within the 2 PM–10 PM window (14:00–21:00), the actual maxima are: baseline 1,200 kW (matches); solar-only 1,150 kW at 17:00 (shown: 1,200 kW); hybrid 750 kW at 17:00 (shown: 800 kW).
  - So, in the report's own data, solar alone cuts the in-window peak by 50 kW (about RM 4,853/month at RM 97.06). This contradicts "Solar alone fails to reduce Peak MD".
  - Hybrid against baseline is a 450 kW reduction (RM 43,677/month; RM 524,124/year at RM 97.06), not the hard-coded 400 kW (RM 38,824/month; RM 465,888/year). The actual 1,150 → 750 kW drop against the solar-only curve does equal 400 kW.
  - The comment "Peak occurs at 16:00 - 17:00" matches the computed solar-only peak at 17:00.
- **BESS charging is not modelled, and there is no "excess solar".** Solar never exceeds load in the profile (smallest net load is 250 kW at 12:00). The narrative "store excess solar" therefore has no surplus to draw on, and the 2,700 kWh/day of discharge (400 kW × 6 h + 300 kW × 1 h) has no modelled charging source. BESS discharge starts at 14:00, when net load is only 750 kW, and stops at 21:00, when load is 500 kW. The 50 kW floor (Math.max(50, …)) never binds.
- **Initial-state mismatches.**
  - On load, button 3 ("Solar + BESS Peak Shaving") is styled as selected, but the chart and outputs show the baseline. `updateLoadProfile` is not called at start-up.
  - The placeholders say "RM 0 / month" and "RM 0 / year", while the JS writes "/ mo" and "/ yr". "Direct bottom-line RP4 savings" is never updated.
  - The CRESS placeholder is "RM 18.0 Mil", while the code writes "RM 18.00 Mil" (toFixed(2)). All other placeholders match the computed defaults.
- **Legacy tariff names.** The report uses pre-RP4 tariff codes B, D, C1, C2, C3, C4, E1, E2 and E3 alongside RP4 terms. The chart maps them to "MV Gen", "MV TOU", "HV Gen" and "HV TOU". Examples: "Monthly MD Charge Rate (Tariff E2)" is labelled "TNB RP4 Peak MD Rate"; "HV Tariff C4 Peak Rate (44.52 sen/kWh)"; the LV "50.68 sen/kWh + AFA". None of these rates is sourced.
- **"+115% to +201%" does not reconcile with the chart data.** MV Gen goes from 30.30 to 89.27 (+194.6%) and MV TOU from 45.10 to 97.06 (+115.2%). The HV categories rise only +6.9% (29.20 → 31.21) and +2.8% (43.60 → 44.82). The "RM 89.27–97.06/kW surge" in the Section 3 intro applies only to MV, although the sentence does not say so.
- **"Off-Peak expanded by 80% to 128 hrs/wk".** 128 h/wk is consistent with the stated 8 h × 5 weekdays of peak (168 − 40). An 80% increase would imply a legacy off-peak of about 71 h/wk. The report does not state the legacy peak or off-peak hours, so the figure cannot be checked from the report.
- **SMP figures differ.** The Section 2 intro gives "~18.8–24.8 sen/kWh", the table gives "~19 sen/kWh", and the calculator default is 0.1911 RM/kWh. No source or period is given. The MAQ formula (kWac × 5 h × days) is stated without a source. The calculator's min/max attributes are not enforced by the JS, and 0 days or 0 SMP silently fall back to 30 days and 0.1911.
- **CRESS SAC figures.** The report gives 14 sen/kWh firm (18 Sept 2026 Acceleration Package), 25 sen/kWh legacy (pre-Sept 2026) firm and 45 sen/kWh non-firm (solar without BESS). The 44% cut cited in an HTML comment matches (25 → 14). No source is cited.
  - The "14 sen/kWh SAC Active" header tag and the SAC chart are static, regardless of the option selected.
  - Choosing Non-Firm at the default 38 sen PPA gives negative values (−7.0 sen/kWh, RM −5.25 Mil) with no warning.
  - "Annual Gross Cashflow" is actually revenue net of SAC.
  - The off-taker saving compares the PPA price only with the 44.52 sen C4 peak energy rate (no off-peak or blended rate, no CRESA top-up or other charges). It does not change with SAC, which implies the developer bears the SAC.
  - The hvdc archetype adds a "≥30 MW Solar" minimum and a "≥51% Local RED SPV" requirement that Section 4 does not mention.
- **Markdown syntax inside HTML.** `**bold**` markers (Sections 1, 2, 3, 4, 5 and 7) and backticks around `eATAP` (Section 2 table) display as literal asterisks and backticks in the browser. This extract renders them as markdown bold or code.
- **ST licensing inconsistency.** The Section 2 table lists "ST Notification" for Enhanced SELCO ≤ 1 MWac. The Section 6 matrix and the ST card require a "Mandatory ST License" (Section 9) above 72 kWac, which covers most of the ≤ 1 MWac range.
- **HTML comments describe features that do not exist.** The "Visualization & Content Choices" comment promises a "CAS Fee lookup" and a "Tariff Savings" calculator; CAS is a static table and there is no tariff-savings calculator beyond the simulator. It also promises a tariff chart comparing "Energy and MD charges across LV, MV, and HV". The actual chart shows MD charges only, for MV and HV only. The "client proposal blueprint generator" is a fixed four-option text switcher.
- **No sources at all.** The report has no citations or source links. The footer's "Fully compliant with Energy Commission (ST), SEDA, TNB RP4, PETRA CRESS, and LHDN GITA Guidelines (2026)" is an unsupported claim. All fees (CAS RM 1,000/5,000/8,000/15,000–20,000; metering RM 1,530/2,330; eATAP RM 7.50/kW; standby RM 12/kWp/month; SARE 2 sen/kWh) are unsourced.
- **Possible typo and undefined terms.** "GITA/A application" (taxcliff archetype) looks like a typo for GITA Asset. These terms are never defined: GEP ("50% GEP MW"), OPC/LPC, CCC, TNBX, NEDA, GSO, "7-day load" / "5-day load" (lvsme archetype), and SARE (never expanded).
- **Tax stack chart tooltip.** The footer sums only the items in the tooltip. Under Chart.js default interaction settings (no mode is set in this code), hovering one segment probably shows only that segment's value as the "Total Tax Recovery". Not verified in a browser.
- **Script loading.** Chart.js is loaded from an unversioned CDN URL (https://cdn.jsdelivr.net/npm/chart.js), so how the page renders depends on whichever Chart.js version is current.
