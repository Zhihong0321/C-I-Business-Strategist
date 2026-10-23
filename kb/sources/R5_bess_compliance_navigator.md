---
id: R5
title: "Malaysia C&I BTM BESS Compliance & Safety Navigator 2026"
source_file: malaysia_bess_compliance_navigator.html
source_modified: 2026-10-23 14:51
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js)
research_prompt: "#5 BESS regulation and fire safety (research/round2_research_prompts.md)"
stated_scope: "Malaysia C&I Behind-the-Meter Regulatory Framework (2026). Multi-agency statutory clearances (Suruhanjaya Tenaga, JBPM / BOMBA, TNB, industrial insurance underwriters) for behind-the-meter BESS in Peninsular Malaysia; 'an operational, data-backed execution framework aligned with the latest 2026 regulatory updates' for EPCC contractors, electrical service engineers and facility owners."
stated_sources: "Direct statutory citations: Suruhanjaya Tenaga (GP/ST/No.62/2026, GP/ST/No.51/2024 Pin 1/2026), Jabatan Bomba dan Penyelamat Malaysia (MS 2747:2024), Tenaga Nasional Berhad."
as_of: "No report as-of date. Dates stated: GP/ST/No.62/2026 issued 22 May 2026; ST licensing directive Keperluan Pelesenan BESS 1 July 2026; GP/ST/No.51/2024 (Pin. 1/2026) effective 1 January 2026; standby charge directive 27 March 2025; Act A1775 amendment 2025; MS 2747:2024."
sections: ["Header & navigation", "Hero: Malaysia Commercial & Industrial BTM BESS Executive Compliance Hub (key metric cards)", "1. Suruhanjaya Tenaga Regulatory Framework (GP/ST/No.62/2026)", "2. Enhanced SELCO Above 1 MWac: Mandatory Storage & Standby Calculator", "3. BOMBA Fire Safety Compliance (MS 2747:2024)", "4. Tenaga Nasional Berhad (TNB): Connection Assessment Study (CAS)", "5. Factory Insurance Requirements & EPCC Execution Roadmap", "Footer"]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R5 — Malaysia C&I BTM BESS Compliance & Safety Navigator 2026

> Faithful, complete markdown extract of `malaysia_bess_compliance_navigator.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- GP/ST/No.62/2026, "Guidelines on Battery Energy Storage System (BESS) Safety", was issued 22 May 2026 under Section 50C of the Electricity Supply Act 1990 [Act 447] (as amended by Act A1775 in 2025) and is the mandatory statutory code for stationary lithium-ion systems; a C&I behind-the-meter asset is an "End User BESS" (Page 16). (§1)
- Any stationary BESS rated 5 kW and above is under ST licensing jurisdiction (Clause 4.1(c) of GP/ST/No.62/2026, Section 9(1) of Act 447, Keperluan Pelesenan BESS 1 July 2026); a generation licence is needed when solar PV exceeds 72 kWp; systems below 5 MW go through ST Regional Offices with post-commissioning registration within 30 days of energization. (§1.2)
- 4-tier competent person regime (Clauses 4.1(a) and 4.2): ST-registered electrical contractor; PEPC or Competent Engineer (Regulation 65); Form G and Form H before energization; technician course STECE-0005/01: BESS. (§1.3)
- 7 certification standards (Appendix A): IEC 62619, IEC 63056, UL 9540A, IEC 62933-5-1, IEC 60529 (min IP54), IEC 62116:2014, UN 38.3 & IK08. (§1.4, Embedded data tables E1)
- Enhanced SELCO (GP/ST/No.51/2024 (Pin. 1/2026), effective 1 January 2026): BESS mandatory for C&I solar PV exceeding 1 MWac, sized E_BESS ≥ 1 × X kWh for X kWp (1-hour rating, quoted as Clause 3.6 / GP 51); monthly standby charge RM12/kWp (quoted as Clause 12.1 / Directive 27 March 2025). Systems at or below 1 MWac can use Solar ATAP (GP/ST/No.60/2025) or SELCO without mandatory BESS or standby charge. (§2)
- Default calculator case: 1,500 kWp at 1.2 MWac and RM 1,100/kWh gives 1,500 kWh BESS, RM 18,000/month standby, RM 396,000 GITA tax offset (24%), CAS tier RM 15,000 (PSS). (Calculators C1)
- Tariff chart: off-peak import RM 0.2723/kWh, solar export (SMP) RM 0.1881/kWh, peak import (avoided) and BESS-discharged peak RM 0.3132/kWh; storing surplus instead of exporting is claimed to deliver net spread savings of RM 0.09 to RM 0.13 per kWh (MV peak 2 PM–10 PM, plus RM 89–97/kW MD charge). (§2.4, Charts)
- BOMBA enforces MS 2747:2024 (with Clause 4.3(a) of GP/ST/No.62/2026 and Fire Services Act 1988 [Act 341]); BESS needs an updated Fire Certificate (FC) and a 2-hour fire-resistance rating (FRR); not verifying the Malaysian 2-hour FRR on imported containers is "the primary cause of project delays". (§3)
- Siting rule in simulator: ≥ 3.0 m from factory walls/openings is compliant; < 3.0 m is compliant only with an unpierced 2-hour fire wall (with UL 9540A radiant heat validation); otherwise rejected by BOMBA. (§3.2, C2)
- 4 fire-protection layers: off-gas detection + EPO; total-flooding clean agent (FK-5-1-12) or potassium aerosol; deflagration venting / ATEX fans; water boundary cooling with hydrant within 30-45 meters. (§3.3)
- BOMBA 4-stage approval: 8–14 weeks plan to FC endorsement (stages 2-3, 4-8, 4-8, 3-6 weeks). (§3.4)
- Zero-export BESS still needs a TNB CAS above 72 kW (fault level, power quality/load flow, anti-islanding per IEC 62116:2014); CAS/PSS fees RM 0 (1–72 kW, CCC only), RM 1,000, RM 5,000, RM 8,000, RM 15,000, and "High-Tier PSS Fee" for >2–5 MW. (§4, E2)
- Insurers (PAR/IAR) treat ST and BOMBA MS 2747:2024 compliance as conditions precedent; requirements listed across 5 policy phases (Marine Cargo, CAR/EAR, PAR/IAR, Machinery Breakdown, claims/O&M). (§5.1)
- 12-item EPCC readiness checklist with percentage score. (§5.2, C4, E3)

## Report purpose and design notes (from HTML comments)

The "Application Structure Plan" comment states the page is organised as a header plus hero and five regulatory sections, and justifies this: "It reorganizes complex multi-agency regulations into a task-oriented engineering workflow while allowing instant scenario calculation and statutory verification." Its planned items:

1. Header & Navigation Bar: Sticky header with rapid navigation across 6 core regulatory modules.
2. Executive Hero & Metrics Bar: Quick stats summary (5kW licensing, 1MWac SELCO BESS threshold, RM12/kWp standby charge, 2-Hr FRR, 8-14 wk BOMBA cycle).
3. Section 1: Suruhanjaya Tenaga Framework (GP/ST/No.62/2026, 4-tier human capital, certification finder table, 7 mandatory forms).
4. Section 2: Enhanced SELCO >1MWac Rules & Dynamic Calculator (Interactive sizing calculator for kWp/kWh, RM12/kWp standby charge, GITA tax allowance, ToU tariff arbitrage chart).
5. Section 3: BOMBA Fire Safety Engineering (MS 2747:2024, interactive separation distance simulator, 4-tier suppression layers, approval timeline).
6. Section 4: TNB CAS & Technical Interconnection Matrix (Interactive capacity tier selector `$1kW to >2MW$`, study fees, zero-export technical rationale).
7. Section 5: Factory Insurance & EPCC Implementation Audit (16-week execution roadmap, operational readiness checklist with dynamic score).

The "Visualization & Content Choices" comment lists:

1. Core Metrics Counters: HTML/Tailwind high-impact stats for statutory thresholds.
2. SELCO Storage & Financial Calculator: JS interactive inputs -> calculates BESS kWh, standby charge, GITA offset, CAS fee -> dynamic Chart.js ToU comparison.
3. Standards & Certification Matrix: Interactive search/filter table for IEC 62619, IEC 63056, UL 9540A, UN 38.3, etc.
4. Siting & Separation Distance Simulator: HTML5 Canvas / JS visual feedback showing BESS container, separation wall, clearance distance compliance with MS 2747.
5. TNB Study Tier Selector: Interactive tab/card display showing study requirements based on system capacity.
6. Dynamic Audit Checklist: JS interactive checkboxes tracking project compliance % readiness.
- Libraries/Methods: Chart.js for tariff charts, HTML5 Canvas for Siting Simulator, Vanilla JS for calculations and interactivity. NO SVG, NO Mermaid JS.

A further comment states: "CONFIRMATION: NO SVG graphics used. NO Mermaid JS used."

## Header and navigation

- Title block: "BESS COMPLIANCE NAVIGATOR" — "Malaysia C&I Behind-the-Meter Regulatory Framework (2026)".
- Navigation links: "1. ST Framework" (#st-framework), "2. SELCO Sizing" (#selco-calculator), "3. BOMBA Siting" (#bomba-safety), "4. TNB Grid CAS" (#tnb-cas), "5. Insurance & Roadmap" (#insurance-roadmap).
- Button: "Readiness Audit" (#compliance-checklist).

## Hero: Malaysia Commercial & Industrial BTM BESS Executive Compliance Hub

Badge: "2026 Statutory Codification • GP/ST/No.62/2026 & MS 2747:2024".

Text: Deploying behind-the-meter (BTM) Battery Energy Storage Systems (BESS) in Peninsular Malaysia requires synchronized multi-agency statutory clearances across Suruhanjaya Tenaga (ST), Jabatan Bomba dan Penyelamat Malaysia (JBPM / BOMBA), Tenaga Nasional Berhad (TNB), and industrial insurance underwriters. This interactive application provides EPCC contractors, electrical service engineers, and facility owners with an operational, data-backed execution framework aligned with the latest 2026 regulatory updates.

Key metric cards:

| Card | Value | Sub-label |
|---|---|---|
| ST Licensing Limit | ≥ 5 kW | Under Act 447 / GP 62 |
| Mandatory SELCO BESS | > 1 MWac | 1-Hour Rating Minimum |
| SELCO Standby Charge | RM 12/kWp | Monthly (>1 MWac systems) |
| BOMBA Fire Rating | 2-Hour FRR | MS 2747:2024 Enclosure |
| BOMBA FC Timeline | 8 – 14 Wks | Plan to FC Endorsement |

## 1. Suruhanjaya Tenaga Regulatory Framework (GP/ST/No.62/2026)

Section intro: This section details the primary statutory safety guidelines governing stationary battery energy storage systems, statutory definitions, mandatory human capital competencies, equipment certification requirements, and required submission forms.

### 1.1 Context

Issued on 22 May 2026 under Section 50C of the Electricity Supply Act 1990 [Act 447] (as amended by Act A1775 in 2025), GP/ST/No.62/2026 (Guidelines on Battery Energy Storage System (BESS) Safety) constitutes the mandatory statutory code for stationary lithium-ion systems in Malaysia. For commercial and industrial facilities operating behind-the-meter, the guidelines officially designate the asset as an "End User BESS" (Page 16), defined as a "BESS owned and operated by the consumer in parallel with the grid and producing energy for self-consumption or for grid export."

Links shown:
- "ST BESS Portal Node 5353" — https://www.st.gov.my/resources/guidelines-battery-energy-storage-system-bess-safety
- "Direct PDF: GP/ST/No.62/2026" — https://www.st.gov.my/sites/default/files/2026-05/Guidelines-on-Battery-Energy-Storage-System-%28BESS%29-Safety_0.pdf
- "Licensing Directive (1 July 2026)" — https://www.st.gov.my/resources/keperluan-pelesenan-battery-energy-storage-system-bess

### 1.2 Licensing Thresholds & Statutory Trigger

Under Clause 4.1(c) of GP/ST/No.62/2026 and Section 9(1) of Act 447, alongside ST's licensing directive (Keperluan Pelesenan BESS, 1 July 2026):

- BESS Capacity Threshold: Any stationary BESS rated at 5 kW and above is subject to ST licensing jurisdiction. Virtually all C&I installations exceed this threshold.
- Solar PV Licensing Threshold: When combined with a behind-the-meter SELCO PV system, a public or private generation licence is required when solar PV capacity exceeds 72 kWp.
- Licence Processing: Systems below 5 MW are processed via ST Regional Offices with post-commissioning registration submitted within 30 days of energization.

Callout — Mandatory BESS Trigger (SELCO 2026): BESS is mandatory for behind-the-meter SELCO solar systems exceeding 1 MWac at a minimum 1-hour energy storage rating (`$1 \times X \text{ kWh}$`).

### 1.3 4-Tier Competent Person Requirements

Clauses 4.1(a) and 4.2 enforce strict regulatory oversight across all BESS project lifecycle stages:

1. Registered Electrical Contractor: Installation must be executed by an ST-registered contractor under Electricity Regulations 1994.
2. PEPC / Competent Electrical Person: Plans, single-lines, and relay sheets must be prepared/endorsed by a Professional Engineer with Practising Certificate (PEPC) or Competent Engineer (Regulation 65).
3. Commissioning Sign-off: The Competent Person must execute statutory completion certificates (Form G and Form H) prior to energization.
4. ST-ECE Competency Upskilling: Technicians must undergo ST Energy Competency Excellence training (Course STECE-0005/01: BESS).

### 1.4 Mandatory Technical Certifications & Standards Matrix (Appendix A)

Subtitle: "Filter standard requirements for Purchase Order type-test verification." Search box placeholder: "Search standard (e.g., UL 9540A, IEC)...".

Displayed columns: Standard Code | Official Title / Scope in GP/ST/No.62/2026 | Component & Verification Deliverable (the third column shows the scope text, then "Deliverable: ..."). The table is rendered from the JS array `standardsData` — all 7 rows are reproduced in Embedded data tables, E1 (IEC 62619, IEC 63056, UL 9540A, IEC 62933-5-1, IEC 60529, IEC 62116:2014, UN 38.3 & IK08). Search logic: Calculators and interactive logic, C5.

### 1.5 7 Mandatory Statutory Forms & Lifecycle Certificates

(Heading says 7; six cards are listed.)

| # | Form / certificate | Description as given |
|---|---|---|
| 1 | FAT Certificate | Pre-shipment deliverable from BESS OEM/Lab verifying cell, pack, and BMS safety compliance. |
| 2 | Permit to Work (PTW) | Regulation 113, Electricity Regulations 1994. Written safety instruction for live/dead work. |
| 3 | SAT Certificate | Post-installation certificate detailing BMS interlock, insulation, earthing, and function tests. |
| 4 | Form G (Completion) | Supervision and Completion Certificate under First Schedule, Electricity Regulations 1994. |
| 5 | Form H (Test Cert) | Statutory Electrical Test Certificate executed by Competent Person prior to energization. |
| 6 | Form of Info (Attachment 1) | Submitted to TNB pre-installation and ST within 30 days post-commissioning (GP 51/2024). |

## 2. Enhanced SELCO Above 1 MWac: Mandatory Storage & Standby Calculator

Section intro: This section analyzes the regulatory evolution of self-consumption rules (GP/ST/No.51/2024 (Pin. 1/2026)), provides the verbatim statutory clauses, and includes an interactive calculator for sizing BESS, standby charges, tax credits, and ToU tariff savings.

### 2.1 Context

Effective 1 January 2026 under updated guidelines GP/ST/No.51/2024 (Pin. 1/2026) and notice Notis Makluman Penyesuaian SELCO, mandatory BESS installation applies to all C&I solar PV installations exceeding 1 MWac. Systems at or below 1 MWac can opt for Solar ATAP (GP/ST/No.60/2025) or SELCO without mandatory battery storage or standby charges.

### 2.2 Verbatim clauses (as presented by the report)

Verbatim Guideline Sizing Rule (Clause 3.6 / GP 51):

> "For a solar PV installation capacity of X kWp, the required BESS energy capacity (E_BESS) charged by the solar PV system must satisfy: E_BESS ≥ 1 × X kWh (a minimum 1-hour energy rating)."

Verbatim Standby Charge Clause (Clause 12.1 / Directive 27 March 2025):

> "IN ACCORDANCE WITH CLAUSE 12.1 OF THE SELCO GUIDELINES, THE MONTHLY STANDBY CHARGE AS APPROVED BY GOVERNMENT IS RM12/kWp."

### 2.3 Dynamic C&I BESS Sizing & Financial Modeling Studio

Subtitle: "Input factory solar capacity to calculate mandatory battery size, standby fee, GITA tax offset, and ToU arbitrage impact."

Badge: "Revised ToU Peak Window: 2:00 PM – 10:00 PM".

Inputs: Planned Solar PV Capacity (kWp slider, 200–10,000, default 1,500); Solar Inverter Output Capacity (MWac dropdown 0.8 / 1.2 / 2.5 / 5.0, default 1.2); Assumed BESS Capital Expenditure (RM / kWh, default 1100). Outputs: Mandatory BESS Energy, Monthly Standby Charge, GITA 100% Tax Offset Est. (24% tax), TNB Interconnection CAS Tier. Full logic, option labels and computed outputs: Calculators and interactive logic, C1.

### 2.4 Chart and Financial Strategy Insight

Chart: "Value Comparative: BESS Peak Self-Consumption vs Solar Export (SMP)" — values in Charts.

Financial Strategy Insight: Exporting surplus solar under Solar ATAP yields only SMP (~RM 0.188/kWh). Storing surplus generation in BESS to avoid Medium Voltage peak import (2 PM–10 PM @ RM 0.313/kWh + RM 89–97/kW MD charge) delivers a net spread savings of RM 0.09 to RM 0.13 per kWh, accelerating payback despite the RM 12/kWp standby charge.

## 3. BOMBA Fire Safety Compliance (MS 2747:2024)

Section intro: Jabatan Bomba dan Penyelamat Malaysia (JBPM) enforces stationary energy storage system fire safety under MS 2747:2024. This section covers structural fire ratings, spatial separation rules, suppression layers, and the approval workflow.

### 3.1 Context

Under Clause 4.3(a) of GP/ST/No.62/2026 and the Fire Services Act 1988 [Act 341], stationary BESS units are classified as high-risk industrial installations requiring an updated Fire Certificate (FC). Importing generic overseas BESS containers without verifying Malaysian 2-hour structural fire-resistance rating (FRR) is the primary cause of project delays.

### 3.2 Interactive Siting & Separation Distance Compliance Visualizer

Subtitle: "Simulate separation distance from factory walls to determine required 2-hour blast walls and UL 9540A conditions under MS 2747:2024."

Inputs: Outdoor Distance to Factory Main Building (0.5–8.0 m, default 3.5 Meters); Factory Wall Construction Type ("Standard Wall with Windows/Openings" or "Solid 2-Hour Fire-Rated Barrier Wall (Unpierced)"). Rule: compliant at ≥ 3.0 m; below 3.0 m compliant only with the 2-hour fire wall; otherwise "NON-COMPLIANT (REJECTED BY BOMBA)". Canvas caption: "Interactive canvas representation of BESS unit, separation zone, and factory perimeter." Full rules and messages: Calculators and interactive logic, C2.

### 3.3 4 Sequential Layers of Fire Protection (MS 2747:2024)

1. Early Detection & EPO: Multi-criteria off-gas sensors (`$H_2, CO, VOCs$`) interlocked with BMS to trigger Emergency Power Off before thermal runaway ignition.
2. Total Flooding Suppression: SIRIM/BOMBA approved clean agent (FK-5-1-12) or potassium aerosol system at module/rack level.
3. Deflagration Venting: Pressure relief vents or ATEX-rated extraction fans to keep off-gas below explosive lower flammability limits.
4. Water Boundary Cooling: External dry-riser breeching inlet with internal spray header plus pressurized hydrant within 30-45 meters.

### 3.4 BOMBA 4-Stage Approval Workflow (8-14 Weeks)

| Stage | Description | Duration |
|---|---|---|
| Stage 1: Pre-Procurement Gap Audit | Audit OEM specs for 2-hr FRR, UL 9540A & BOMBA agents. | 2-3 Wks |
| Stage 2: Technical Dossier & Plan Submission | PEPC submits architectural & M&E fire drawings to JBPM State HQ. | 4-8 Wks |
| Stage 3: Installation, FAT & SAT Execution | Construct civil pad/firewalls and complete FAT/SAT testing. | 4-8 Wks |
| Stage 4: JBPM Site Inspection & FC Endorsement | Live witness testing of BMS trips, suppression & FC issuance. | 3-6 Wks |

## 4. Tenaga Nasional Berhad (TNB): Connection Assessment Study (CAS)

Section intro: Detailed breakdown of TNB technical study requirements for behind-the-meter BESS. Explains why zero-export systems still require formal grid interconnection clearance.

### 4.1 Technical Rationale: Why Zero-Export BESS Requires Mandatory TNB CAS (>72 kW)

Even when reverse power protection prevents active energy (`$\text{kW}$`) export across the meter, a BTM BESS operates in parallel with the grid ("Indirect Connection"). This creates three critical grid impacts verified during a CAS:

1. Fault Level Contribution — PCS inverters inject short-circuit fault current into the Point of Interconnection (POI). TNB must verify switchgear withstand capacity.
2. Power Quality & Load Flow — High-power off-peak charging and peak discharging alter feeder voltage profiles, power factor, THD, and flicker.
3. Anti-Islanding Safety — Mandatory compliance with IEC 62116:2014 prevents BESS from energizing dead TNB distribution lines during grid outages.

### 4.2 TNB Technical Study Tiers & Cost Structure Matrix

Filter buttons: "Show All Tiers"; "Low Voltage / Small Systems (≤180 kW)"; "Medium Voltage / High Capacity (>180 kW)" (logic: C3).

Displayed columns: Capacity Tier | Study Required | Study Fee (RM) | Scope of Deliverables & EPCC Documents. Rendered from JS array `casTiersData`; all 6 rows in Embedded data tables, E2. Summary of fees: 1 kW - 72 kW RM 0 (No CAS Required (CCC Only)); > 72 kW - 180 kW RM 1,000; > 180 kW - 425 kW RM 5,000; > 425 kW - 1,000 kW (1 MW) RM 8,000; > 1,000 kW - 2,000 kW (2 MW) RM 15,000; > 2,000 kW - 5,000 kW (5 MW) "High-Tier PSS Fee".

## 5. Factory Insurance Requirements & EPCC Execution Roadmap

Section intro: Malaysian industrial property insurers (PAR/IAR) require full compliance with ST guidelines and BOMBA MS 2747:2024 as binding conditions precedent to policy validity.

### 5.1 Underwriting Compliance Matrix Across Policy Phases

| # | Phase | Policy / stage | Requirements |
|---|---|---|---|
| 1 | Marine Transit | Marine Cargo Policy | UN 38.3 test summary matching exact delivered battery model + OEM FAT certificate. |
| 2 | Erection Phase | CAR / EAR Policy | ST registered electrical contractor, Competent Person, PTW logs, Form G & Form H. |
| 3 | Factory PAR / IAR | Operational Phase | Valid BOMBA Fire Certificate (FC), MS 2747 audit, 2-hr FRR enclosure & UL 9540A report. |
| 4 | Machinery Breakdown | Tropical Warranty | IEC 60529 IP54+, IK08 impact, and active HVAC keeping internal temp below 30°C. |
| 5 | Claims Defensibility | O&M Lifecycle | Clause 6.7.5: Maintenance logs, Appendix D checklists, and BMS firmware logs. |

### 5.2 EPCC Statutory Audit & Operational Readiness Checklist

Subtitle: "Tick completed compliance milestones to calculate your project's overall readiness score." Score panel "Readiness Score", initial "0%", with a progress bar. 12 checkbox items rendered from JS array `checklistItems` — full list in Embedded data tables, E3; scoring logic in C4.

## Footer

- "Malaysia Commercial & Industrial BTM BESS Compliance Navigator (2026 Framework)"
- "Direct statutory citations: Suruhanjaya Tenaga (GP/ST/No.62/2026, GP/ST/No.51/2024 Pin 1/2026), Jabatan Bomba dan Penyelamat Malaysia (MS 2747:2024), Tenaga Nasional Berhad."

## Charts

### Chart 1 — touTariffChart

- Location: §2 Enhanced SELCO, calculator panel, chart column (canvas id `touTariffChart`).
- Title (heading above chart): "Value Comparative: BESS Peak Self-Consumption vs Solar Export (SMP)".
- Type: bar (Chart.js), single dataset, legend hidden.
- Axis titles: none set. Y axis begins at zero, ticks formatted "RM " + value to 2 decimals. X axis: category labels.
- Tooltip: "RM {value to 4 decimals} / kWh".
- Series: "Effective Tariff Value (RM / kWh)".
- Data is hard-coded and does not change with calculator inputs (see C1 and Extraction notes).

| Label | Effective Tariff Value (RM / kWh) |
|---|---|
| Off-Peak Import | 0.2723 |
| Solar Export (SMP) | 0.1881 |
| Peak Import (Avoided) | 0.3132 |
| BESS Discharged Peak | 0.3132 |

## Calculators and interactive logic

### C1 — Dynamic C&I BESS Sizing & Financial Modeling Studio

Location: §2.3 (`initCalculator()` / `updateCalc()`).

Inputs:

| Input | Type | Default | Range / options |
|---|---|---|---|
| Planned Solar PV Capacity (`$X\text{ kWp}$`) — `pv-capacity-input` | range slider | 1500 (display "1,500 kWp") | min 200, max 10000, step 100. Tick labels: "200 kWp (SELCO ≤1MW)", "1,000 kWp (Threshold)", "10,000 kWp (Large C&I)" |
| Solar Inverter Output Capacity (`$MW_{ac}$`) — `inverter-ac-select` | dropdown | 1.2 (selected) | see option table below |
| Assumed BESS Capital Expenditure (RM / kWh) — `bess-cost-per-kwh` | number | 1100 | step 50; no min/max |

Dropdown options:

| Value | Label |
|---|---|
| 0.8 | 0.8 MWac (≤ 1 MWac Threshold: Optional BESS / No Standby) |
| 1.2 (default) | 1.2 MWac (> 1 MWac Threshold: Mandatory BESS & Standby Charge) |
| 2.5 | 2.5 MWac (> 1 MWac Threshold: High-Tier PSS Required) |
| 5.0 | 5.0 MWac (> 1 MWac Threshold: ST Regional Office Limit) |

Constants: sizing factor 1.0 (hours, "E_BESS = 1 * X kWh"); standby RM 12 per kWp per month; tax rate 0.24 ("assumes 24% corporate tax rate"); cost fallback 1100; CAS thresholds 180, 425, 1000, 2000 kWp.

Logic (faithful to the JS):

```
pvkWp      = slider value
acMw       = dropdown value
costPerKwh = parseFloat(cost input) || 1100        # empty or 0 -> 1100
display pvkWp + " kWp"

bessKwh = pvkWp * 1.0                              # "Mandatory sizing E_BESS = 1 * X kWh"
output "Mandatory BESS Energy" = bessKwh + " kWh"  # always computed, regardless of acMw

if acMw > 1.0:
    monthlyStandby = pvkWp * 12
    output "Monthly Standby Charge" = "RM " + monthlyStandby + " / mo"
else:
    output "Monthly Standby Charge" = "Exempt (≤ 1 MWac)"

capex       = bessKwh * costPerKwh
gitaSavings = capex * 0.24                         # "GITA 100% Tax allowance (assumes 24% corporate tax rate)"
output "GITA 100% Tax Offset Est. (24% tax)" = "RM " + round(gitaSavings)

casFee = "RM 1,000 (CAS)"
if   180 < pvkWp <= 425:   casFee = "RM 5,000 (CAS)"
elif 425 < pvkWp <= 1000:  casFee = "RM 8,000 (CAS/PSS)"
elif 1000 < pvkWp <= 2000: casFee = "RM 15,000 (PSS)"
elif pvkWp > 2000:         casFee = "High-Tier PSS"
output "TNB Interconnection CAS Tier" = casFee     # keyed on PV kWp, not acMw

updateChartData(pvkWp, bessKwh)                    # only calls chart.update(); data unchanged
```

Triggers: slider "input", dropdown "change", cost "input"; runs once on load. Numbers are formatted with the browser's `toLocaleString()`.

Outputs at default inputs (computed by running the code logic: 1500 kWp, 1.2 MWac, RM 1100/kWh):

| Output | HTML placeholder | Computed | Match |
|---|---|---|---|
| PV display | 1,500 kWp | 1,500 kWp | yes |
| Mandatory BESS Energy | 1,500 kWh | 1,500 kWh | yes |
| Monthly Standby Charge | RM 18,000 / mo | RM 18,000 / mo | yes |
| GITA 100% Tax Offset Est. (24% tax) | RM 396,000 | RM 396,000 (capex RM 1,650,000 × 0.24) | yes |
| TNB Interconnection CAS Tier | Tier 5 (RM 15,000 PSS) | RM 15,000 (PSS) | no — text differs (placeholder is overwritten on load) |

Additional cases (computed by running the code logic, cost RM 1100/kWh):

| kWp | MWac | BESS kWh | Standby | GITA offset | CAS tier |
|---|---|---|---|---|---|
| 200 | 0.8 | 200 | Exempt (≤ 1 MWac) | RM 52,800 | RM 5,000 (CAS) |
| 200 | 1.2 | 200 | RM 2,400 / mo | RM 52,800 | RM 5,000 (CAS) |
| 400 | 1.2 | 400 | RM 4,800 / mo | RM 105,600 | RM 5,000 (CAS) |
| 500 | 0.8 | 500 | Exempt (≤ 1 MWac) | RM 132,000 | RM 8,000 (CAS/PSS) |
| 1,000 | 1.2 | 1,000 | RM 12,000 / mo | RM 264,000 | RM 8,000 (CAS/PSS) |
| 1,100 | 1.2 | 1,100 | RM 13,200 / mo | RM 290,400 | RM 15,000 (PSS) |
| 2,000 | 2.5 | 2,000 | RM 24,000 / mo | RM 528,000 | RM 15,000 (PSS) |
| 2,100 | 2.5 | 2,100 | RM 25,200 / mo | RM 554,400 | High-Tier PSS |
| 5,000 | 5.0 | 5,000 | RM 60,000 / mo | RM 1,320,000 | High-Tier PSS |
| 10,000 | 0.8 | 10,000 | Exempt (≤ 1 MWac) | RM 2,640,000 | High-Tier PSS |
| 10,000 | 5.0 | 10,000 | RM 120,000 / mo | RM 2,640,000 | High-Tier PSS |

Cost-input edge cases (computed): empty or "0" → falls back to 1100 (RM 396,000 at defaults); "-100" → RM -36,000.

### C2 — Interactive Siting & Separation Distance Compliance Visualizer

Location: §3.2 (`initSitingSimulator()` / `updateSiting()` / `drawSitingDiagram()`).

Inputs:

| Input | Type | Default | Range / options |
|---|---|---|---|
| Outdoor Distance to Factory Main Building — `dist-input` | range slider | 3.5 (display "3.5 Meters") | min 0.5, max 8.0, step 0.5 (display = value to 1 decimal + " Meters") |
| Factory Wall Construction Type — `wall-type-select` | dropdown | standard (first option) | "standard" = "Standard Wall with Windows/Openings"; "firewall" = "Solid 2-Hour Fire-Rated Barrier Wall (Unpierced)" |

Rules and exact messages:

```
if dist >= 3.0:
    compliant; green box
    "COMPLIANT (MS 2747:2024 Standard Clearance): Distance ≥ 3.0m satisfies standard spatial separation from factory openings."
elif dist < 3.0 and wallType == 'firewall':
    compliant; green box
    "COMPLIANT WITH FIRE BARRIER: Reduced clearance (<3.0m) accepted because facing wall is an unpierced 2-Hour Fire Wall with UL 9540A radiant heat validation."
else:
    non-compliant; red box
    "NON-COMPLIANT (REJECTED BY BOMBA): Distance < 3.0m without a 2-Hour Fire Wall violates MS 2747 separation rules. High risk of FC rejection."
```

Triggers: slider "input", dropdown "change"; first run after a 100 ms timeout (status box is empty until then).

Canvas content: a factory wall on the right labelled "2-HR FIRE WALL" (firewall) or "FACTORY WALL" (standard); a box labelled "BESS" / "CONTAINER", green if compliant, red if not; a separation line and badge showing the distance as "{d}m". Scale in code: 28 px per metre (code comment says "scale: 1m = ~25px").

Output at default inputs (computed): 3.5 Meters, standard wall → "COMPLIANT (MS 2747:2024 Standard Clearance)" message; badge "3.5m". Other computed cases: 0.5 m or 2.5 m with standard wall → NON-COMPLIANT; 0.5 m or 2.5 m with firewall → COMPLIANT WITH FIRE BARRIER; 3.0 m and above with either wall → COMPLIANT (standard clearance).

### C3 — TNB CAS tier filter

Location: §4.2 (`filterCasTier(cat)` / `renderCasTable()`).

| Button | Argument | Rows shown (from E2) |
|---|---|---|
| Show All Tiers (default view on load) | 'all' | all 6 |
| Low Voltage / Small Systems (≤180 kW) | 'lv' | 1 kW - 72 kW; > 72 kW - 180 kW |
| Medium Voltage / High Capacity (>180 kW) | 'mv' | > 180 kW - 425 kW; > 425 kW - 1,000 kW (1 MW); > 1,000 kW - 2,000 kW (2 MW); > 2,000 kW - 5,000 kW (5 MW) |

The button highlight is not changed when a filter is clicked.

### C4 — EPCC Statutory Audit & Operational Readiness Checklist

Location: §5.2 (`renderChecklist()` / `updateChecklistScore()`).

- Inputs: 12 checkboxes (items E3), all unchecked by default; rendered as "{n}. {item}".
- Logic: `pct = round(checked / 12 * 100)`; score text = pct + "%"; progress bar width = pct%; bar colour red if pct < 50, amber if pct < 85, otherwise emerald.
- Default output: "0%" (static initial text; bar width 0).

Computed score for each number of ticked items:

| Ticked | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Score | 0% | 8% | 17% | 25% | 33% | 42% | 50% | 58% | 67% | 75% | 83% | 92% | 100% |
| Bar colour | red | red | red | red | red | red | amber | amber | amber | amber | amber | emerald | emerald |

### C5 — Standards matrix search

Location: §1.4 (`renderStandardsTable(filterText)`). Text input (placeholder "Search standard (e.g., UL 9540A, IEC)..."), default empty (all 7 rows). On each "input" event, rows are kept where the lower-cased `code`, `title` or `scope` contains the lower-cased search text (the `deliverable` field is not searched).

## Embedded data tables

### E1 — `standardsData` (7 rows; §1.4)

| code | title | scope | deliverable |
|---|---|---|---|
| IEC 62619 | Industrial Secondary Lithium Cells & Batteries Safety | Battery Packs & BMS: Safety evaluation for cells, modules, overcharge & thermal protection. | Type-test report from accredited lab. |
| IEC 63056 | Secondary Lithium Batteries for Electrical Energy Storage | Electrical Storage Architectures: Safety rules for stationary storage up to max DC voltage. | System level safety certificate. |
| UL 9540A | Thermal Runaway Fire Propagation Test Method | Fire Containment: Evaluates cell, module, and unit level thermal runaway propagation. | Full UL 9540A test report. |
| IEC 62933-5-1 | Grid-Integrated EES Systems - Safety Specification | Worker & Maintenance Safety (Clause 6.4): Effective worker isolation during maintenance. | Compliance declaration. |
| IEC 60529 | Enclosure Ingress Protection (IP Code) | Outdoor Enclosures (Clause 6.4.5): Minimum IP54 rating against moisture and pollution. | IEC 60529 test report. |
| IEC 62116:2014 | Photovoltaic Inverters Anti-Islanding Protection | Grid Disconnection: Inverters must cease operation within utility specified trip time. | Anti-islanding test certificate. |
| UN 38.3 & IK08 | Transport Testing & Mechanical Impact Protection | Logistics & Enclosure: UN 38.3 summary for shipment; IK08 impact rating for enclosures. | UN 38.3 Summary & IK08 certificate. |

### E2 — `casTiersData` (6 rows; §4.2)

| capacity | study | fee | cat | scope |
|---|---|---|---|---|
| 1 kW - 72 kW | No CAS Required (CCC Only) | RM 0 | lv | Zero-export verified via inverter. Submit Form of Information to TNB prior to work. |
| > 72 kW - 180 kW | Connection Assessment Study (CAS) | RM 1,000 | lv | Load flow, peak/off-peak voltage profile, power factor, and short-circuit fault level at POI. |
| > 180 kW - 425 kW | Connection Assessment Study (CAS) | RM 5,000 | mv | Full distribution feeder & transformer thermal/fault withstand analysis, zero-export protection scheme. |
| > 425 kW - 1,000 kW (1 MW) | CAS / Power System Study (PSS) | RM 8,000 | mv | MV/LV network study, harmonic/flicker power quality report, PE-stamped relay setting sheet. |
| > 1,000 kW - 2,000 kW (2 MW) | CAS / Power System Study (PSS) | RM 15,000 | mv | Mandatory SELCO BESS integration study (>1 MWac), verifying 1-hr BESS smoothing & standby charge metering. |
| > 2,000 kW - 5,000 kW (5 MW) | Power System Study (PSS) | High-Tier PSS Fee | mv | Substation stability study, ST generation & BESS licensing, TNB SELCO Welcome Letter sign-off. |

### E3 — `checklistItems` (12 items; §5.2)

1. Verify BESS OEM has UN 38.3, IEC 62619, IEC 63056, and UL 9540A type-test reports
2. Ensure container/enclosure structural fire-resistance rating is 2-Hour FRR (MS 2747:2024)
3. Confirm internal fire suppression uses BOMBA/SIRIM approved local agent (FK-5-1-12 / aerosol)
4. Appoint ST-registered Electrical Contractor and PEPC for drawing endorsements (Regulation 65)
5. Submit Connection Assessment Study (CAS/PSS) and Form of Information to TNB (>72 kW)
6. For SELCO >1 MWac: Confirm BESS capacity is at least 1-hour rating (1 x X kWp in kWh)
7. Apply for ST BESS Licence (≥5 kW) and Generation Licence (>72 kWp) via ST Regional Office
8. Maintain separation distance ≥3.0m from factory walls or install solid 2-hr fire barrier wall
9. Execute Factory Acceptance Testing (FAT) and site Site Acceptance Testing (SAT)
10. Issue Permit to Work (PTW) logs under Regulation 113 for all commissioning activities
11. Complete statutory Supervision Certificate (Form G) and Electrical Test Certificate (Form H)
12. Pass JBPM BOMBA site inspection to secure Fire Certificate (FC) endorsement for factory PAR insurance

## Links and cited documents

| Label as shown | URL or document ID | Where used |
|---|---|---|
| ST BESS Portal Node 5353 | https://www.st.gov.my/resources/guidelines-battery-energy-storage-system-bess-safety | §1.1 |
| Direct PDF: GP/ST/No.62/2026 | https://www.st.gov.my/sites/default/files/2026-05/Guidelines-on-Battery-Energy-Storage-System-%28BESS%29-Safety_0.pdf | §1.1 |
| Licensing Directive (1 July 2026) | https://www.st.gov.my/resources/keperluan-pelesenan-battery-energy-storage-system-bess | §1.1 |
| Navigation anchors | #st-framework, #selco-calculator, #bomba-safety, #tnb-cas, #insurance-roadmap, #compliance-checklist | Header |
| Page libraries (scripts, not content) | https://cdn.tailwindcss.com ; https://cdn.jsdelivr.net/npm/chart.js | HTML head |
| GP/ST/No.62/2026 — Guidelines on Battery Energy Storage System (BESS) Safety (issued 22 May 2026) | Page 16 ("End User BESS"); Clause 4.1(a); Clause 4.1(c); Clause 4.2; Clause 4.3(a); Appendix A | Hero, §1, §3.1, footer |
| Electricity Supply Act 1990 [Act 447] | Section 50C; Section 9(1) | §1.1, §1.2, hero card |
| Act A1775 (2025 amendment to Act 447) | — | §1.1 |
| Keperluan Pelesenan BESS (ST licensing directive) | 1 July 2026 | §1.2 |
| Electricity Regulations 1994 | Regulation 65 (PEPC / Competent Engineer); Regulation 113 (Permit to Work); First Schedule (Form G) | §1.3, §1.5, E3 |
| Form G (Supervision and Completion Certificate) | Electricity Regulations 1994, First Schedule | §1.3, §1.5, §5.1, E3 |
| Form H (Electrical Test Certificate) | — | §1.3, §1.5, §5.1, E3 |
| Form of Info / Form of Information (Attachment 1) | GP 51/2024 | §1.5, E2, E3 |
| FAT Certificate; SAT Certificate; Permit to Work (PTW) | — | §1.5, §3.4, §5.1, E3 |
| ST Energy Competency Excellence training | Course STECE-0005/01: BESS | §1.3 |
| GP/ST/No.51/2024 (Pin. 1/2026) — SELCO guidelines | Clause 3.6 (sizing); Clause 12.1 (standby charge); effective 1 January 2026 | §2, footer |
| Notis Makluman Penyesuaian SELCO | — | §2.1 |
| Standby charge directive | 27 March 2025 | §2.2 |
| GP/ST/No.60/2025 (Solar ATAP) | — | §2.1 |
| GITA (Green Investment Tax Allowance), "100%", 24% tax rate | — | C1 |
| Fire Services Act 1988 [Act 341] | — | §3.1 |
| MS 2747:2024 | — | Hero, §3, §5, E3, C2, footer |
| Fire Certificate (FC) | — | §3, §5.1, E3 |
| IEC 62619 | — | E1, E3 |
| IEC 63056 | — | E1, E3 |
| UL 9540A | — | E1, §3, §5.1, E3, C2 |
| IEC 62933-5-1 | Clause 6.4 | E1 |
| IEC 60529 (IP Code) | Clause 6.4.5; IP54 | E1, §5.1 |
| IEC 62116:2014 | — | E1, §4.1 |
| UN 38.3 | — | E1, §5.1, E3 |
| IK08 | — | E1, §5.1 |
| FK-5-1-12 clean agent; potassium aerosol | — | §3.3, E3 |
| ATEX-rated extraction fans | — | §3.3 |
| TNB Connection Assessment Study (CAS); Power System Study (PSS); CCC | — | §4, C1 |
| TNB SELCO Welcome Letter | — | E2 |
| Insurance policies: Marine Cargo Policy; CAR / EAR; PAR / IAR; Machinery Breakdown | — | §5.1 |
| Clause 6.7.5; Appendix D checklists (document not named) | — | §5.1 |

## Extraction notes

Internal contradictions and numbers that don't reconcile:

- "7 Mandatory Statutory Forms & Lifecycle Certificates" (heading, and "7 mandatory forms" in the Structure Plan comment), but only 6 cards are listed (FAT, PTW, SAT, Form G, Form H, Form of Info).
- Net spread claim "RM 0.09 to RM 0.13 per kWh" does not reconcile with the chart values: peak 0.3132 − SMP 0.1881 = 0.1251 (matches the upper end, rounded); peak 0.3132 − off-peak 0.2723 = 0.0409; off-peak 0.2723 − SMP 0.1881 = 0.0842. Nothing in the report gives the 0.09 lower bound. The RM 89–97/kW MD charge is not converted to a per-kWh value or used in any calculation.
- "BESS Discharged Peak" and "Peak Import (Avoided)" have the same value (0.3132), so the chart shows no difference between them.
- BOMBA timeline "8-14 Weeks" / "8 – 14 Wks Plan to FC Endorsement" vs stage durations: all four stages sum to 13–25 weeks; Stages 2–4 sum to 11–22; only Stage 2 + Stage 4 (7–14) come near 8–14.
- The Structure Plan promises a "16-week execution roadmap" in Section 5, and the section heading says "EPCC Execution Roadmap", but no roadmap or timeline is in the page (only the insurance matrix and the checklist).
- The Structure Plan says navigation covers "6 core regulatory modules"; the header has 5 section links plus a "Readiness Audit" button.
- The Structure Plan describes the CAS selector as "`$1kW to >2MW$`", but the table goes up to 5 MW.
- Label "ST BESS Portal Node 5353": the URL is a slug and contains no node ID 5353.
- Siting simulator subtitle says "2-hour blast walls"; the rule and options refer to a 2-hour fire wall / fire-rated barrier wall.

Calculator (C1) bugs and limitations:

- The kWp slider and the MWac dropdown are independent. Any kWp can be paired with any MWac (e.g. 200 kWp with 1.2 MWac gives a RM 2,400/month standby charge; 10,000 kWp with 0.8 MWac is "Exempt (≤ 1 MWac)").
- "Mandatory BESS Energy" is always kWp × 1.0 kWh, even when 0.8 MWac is selected, where the report says BESS is optional. The GITA offset is then computed on that BESS too.
- Standby charge = kWp × RM 12 per month only when MWac > 1.0, applied to the full PV kWp.
- "GITA 100% Tax Offset Est. (24% tax)" = BESS capex (kWh × RM/kWh) × 0.24 only. PV capex is not included, and no limit, timing or utilisation constraint is modelled.
- The ToU chart is static. `updateChartData()` only calls `chartInstance.update()` without changing data, so the "dynamic Chart.js ToU comparison" in the Visualization comment does not happen. On the first run the chart does not exist yet (initCalculator runs before initChart).
- The CAS tier is keyed on PV kWp, not on the MWac selection or the BESS kW. The dropdown labels "High-Tier PSS Required" (2.5 MWac) and "ST Regional Office Limit" (5.0 MWac) drive no logic.
- The default branch "RM 1,000 (CAS)" (pvkWp ≤ 180) cannot be reached because the slider minimum is 200. The table's RM 0 tier (1 kW - 72 kW) has no branch. Everything above 2,000 kWp, including 5,000–10,000 kWp (beyond the table's 5 MW top tier), shows "High-Tier PSS".
- Placeholder vs computed mismatch: the CAS output placeholder "Tier 5 (RM 15,000 PSS)" is replaced on load by "RM 15,000 (PSS)". The other default placeholders match the computed values (1,500 kWp; 1,500 kWh; RM 18,000 / mo; RM 396,000).
- The cost input has no min. Empty or 0 falls back to 1100 (`|| 1100`); negative values give a negative GITA offset (e.g. -100 → RM -36,000).
- Slider tick labels equate "1,000 kWp (Threshold)" and "200 kWp (SELCO ≤1MW)" (DC kWp) with the 1 MWac (AC) threshold. The sizing rule and standby charge are stated per kWp while the trigger is stated in MWac.
- Number formatting uses `toLocaleString()` with no locale, so separators depend on the browser.

Other interactive issues:

- Siting (C2): at ≥ 3.0 m the wall type is ignored. With the fire wall, any distance down to the 0.5 m minimum is accepted. The "UL 9540A radiant heat validation" in the message is not an input. The canvas code comment says "1m = ~25px", but the code uses 28 px/m.
- CAS filter (C3): the active-button highlight never changes.
- Checklist (C4): before any click the progress bar has the emerald class at 0%. Because of the < 85 threshold, 10/12 (83%) is amber and 11/12 (92%) is emerald.
- Standards search (C5) does not search the `deliverable` field.

Rendering artefacts:

- LaTeX `$...$` is used with no math renderer loaded (no MathJax/KaTeX), so it shows as raw text: `$1 \times X \text{ kWh}$` (§1.2 callout), `$X\text{ kWp}$` and `$MW_{ac}$` (C1 labels), `$E_{\text{BESS}}$` (C1 output label), `$H_2, CO, VOCs$` (§3.3), `$\text{kW}$` (§4.1), and `$1kW to >2MW$` (Structure Plan comment).
- Markdown backticks inside HTML render as literal backtick characters: `` `GP/ST/No.51/2024 (Pin. 1/2026)` `` (§2 intro) and `` `GP/ST/No.60/2025` `` (§2.1).
- Checklist item 9 has the typo "site Site Acceptance Testing", kept verbatim.
- Libraries load from unversioned CDNs (cdn.tailwindcss.com, cdn.jsdelivr.net/npm/chart.js), so the page needs internet access and may change over time.
- The palette comment was dropped as styling. Its content: "Chosen Palette: Industrial Warm Slate & Energetic Gold (Background: Warm Slate/Light Slate #f8fafc, Nav: Slate-900, Accents: Emerald/Green #15803d and Gold/Amber #b45309)".

Claims with no source in the report:

- Only three links exist, all st.gov.my (the GP/ST/No.62/2026 page and PDF, and the licensing directive). The "verbatim" SELCO sizing rule (Clause 3.6 / GP 51), the standby clause (Clause 12.1 / Directive 27 March 2025), the notice Notis Makluman Penyesuaian SELCO and GP/ST/No.51/2024 (Pin. 1/2026) itself have no link. The standby directive is dated 27 March 2025, before the stated 1 January 2026 effective date of Pin. 1/2026; the report does not explain how they relate.
- No bomba.gov.my, SIRIM/Department of Standards Malaysia, or TNB link or document ID is given. MS 2747:2024 is never quoted or cited by clause. The ≥ 3.0 m separation rule, the 2-hour FRR, the 4 protection layers, the 30-45 m hydrant distance and the 8–14 week / stage durations are all unsourced.
- The TNB CAS thresholds (72 / 180 / 425 / 1,000 / 2,000 / 5,000 kW), the fees (RM 0 to RM 15,000, plus "High-Tier PSS Fee" with no amount) and the term "CCC" (not defined) are unsourced.
- Tariff values (0.2723, 0.1881, 0.3132), the RM 89–97/kW MD charge, the 2:00 PM – 10:00 PM peak window, the RM 1,100/kWh default capex and the 24% tax rate are unsourced.
- Insurance requirements (§5.1) name no insurer, insurer association or policy wording. The "Clause 6.7.5" and "Appendix D" do not say which document they belong to (possibly GP/ST/No.62/2026). The IP54+/IK08/below 30°C HVAC conditions are unsourced.
- Standards-table clause references "Clause 6.4" and "Clause 6.4.5" do not say whether they are clauses of GP/ST/No.62/2026 or of the IEC standard.
- STECE-0005/01 and the 30-day post-commissioning registration have no link.
- The only text presented as a verbatim guideline definition is the "End User BESS" definition (GP/ST/No.62/2026, Page 16).

Prompt coverage (prompt #5):

1. ST guideline, licensing thresholds, certifications, forms, competent persons — Answered (§1). GP/ST/No.62/2026 confirmed, with issue date, legal basis and two st.gov.my links. Licensing thresholds are given in kW only (≥ 5 kW BESS, > 72 kWp PV generation licence, < 5 MW via Regional Office); there is no kWh threshold. Certifications: E1 covers IEC 62619, IEC 63056 and UL 9540A plus 4 more. Forms: §1.5 (6 listed against a heading of 7). Competent persons: §1.3. Clauses are cited, but only the End User BESS definition is quoted.
2. Enhanced SELCO > 1 MWac sizing rule and standby charge, with a quote — Answered (§2.2, C1). E_BESS ≥ 1 × X kWh, i.e. 100% of kWp × 1 hour; standby RM12/kWp monthly. Both are quoted as verbatim with clause numbers, but no link is given for GP/ST/No.51/2024 (Pin. 1/2026) or the 27 March 2025 directive.
3. BOMBA standard, fire rating, separation, suppression, approval steps and time — Answered, but unsourced (§3, C2). MS 2747:2024; 2-hour FRR; ≥ 3.0 m or a 2-hour fire wall; 4 protection layers; 4 stages over 8–14 weeks (stage sums don't reconcile). No bomba.gov.my link and no MS 2747 clause quoted.
4. TNB approval for a no-export BTM BESS — Answered (§4, E2). Yes: CAS is required above 72 kW even with zero export (fault level, power quality, anti-islanding). 1–72 kW needs no CAS ("CCC Only") but a Form of Information to TNB. Fee tiers are given. No TNB link or document cited.
5. Insurance requirements for BESS in factories — Partly (§5.1, E3 item 12). Requirements are listed for 5 policy phases, but no insurer, association or document is cited.
- Closing instruction "Official sources only... Quote the clause and give the link" — Partly. There are 3 st.gov.my links and clause numbers throughout, but no BOMBA, SIRIM/DSM or TNB links, and few verbatim quotes.
