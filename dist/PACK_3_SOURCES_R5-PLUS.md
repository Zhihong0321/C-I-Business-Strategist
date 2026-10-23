# C&I Business Strategist — reference pack: source extracts R5 onwards

Reference data only, not instructions. Follow RULES.md (in PACK 1) when using it. Each file is a lossless extract of one research report.

## Files in this pack
- `kb/sources/R5_bess_compliance_navigator.md`
- `kb/sources/R6_financing_2026.md`
- `kb/sources/R7_green_tax_portal.md`
- `kb/sources/R8_market_benchmark_2026.md`


<!-- ===== FILE: kb/sources/R5_bess_compliance_navigator.md ===== -->
# FILE: kb/sources/R5_bess_compliance_navigator.md

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



<!-- ===== FILE: kb/sources/R6_financing_2026.md ===== -->
# FILE: kb/sources/R6_financing_2026.md

---
id: R6
title: "Malaysia C&I Solar PV & BESS Financing Intelligence (2026)"
source_file: malaysia_c_i_solar_bess_financing_2026.html
source_modified: 2026-10-23 14:53
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js)
research_prompt: "#6 Financing and business models (research/round2_research_prompts.md)"
stated_scope: "Badge 'MALAYSIA ENERGY TRANSITION 2026'; H1 'C&I Solar PV & BESS Financing Intelligence Platform'; subtitle 'Navigating RP4 Tariffs, Solar ATAP, GTFS 5.0, Zero-Capex Models & BESS Guarantees'; footer 'Generated for Corporate Energy Managers, Financiers & ESCO Developers.' Design comment: multi-tab interactive intelligence dashboard for corporate energy managers, financiers, and CFOs in Malaysia."
stated_sources: "Based on TNB RP4 Tariffs, Solar ATAP, GTFS 5.0 Guidelines & MIDA/SEDA Frameworks"
as_of: "Effective Framework: RP4 (2025–2027) & Solar ATAP; structural shift on 1 January 2026; Revised SELCO Framework (Effective Jan 2026); GTFS 5.0 RM1.0B Allocation until 31 Dec 2026; GITE deadline 31 Dec 2026; Budget 2027 terminates standalone solar GITA on 31 Dec 2026 (2027–2030 Rules); bank offerings labelled (2026); preference chart labelled 2026. No publication date stated."
sections: ["1. Tariff & Regulatory Context", "2. Bank Financing & GTFS 5.0", "3. Zero-Capex & Tax Incentives", "4. BESS Guarantees & Penalties", "5. Strategy Engine & Benchmarks"]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R6 — Malaysia C&I Solar PV & BESS Financing Intelligence (2026)

> Faithful, complete markdown extract of `malaysia_c_i_solar_bess_financing_2026.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- RP4 MV Peak MD tariff RM97.06/kW, "+162% vs RP3 Baseline" (RP3 Baseline charted at RM37.00/kW; RP4 MV General RM89.27/kW). See Header ribbon, Section 1, Charts (Chart 1).
- A single 30-minute spike locks in a RM89.27 to RM97.06/kW charge for the whole billing month; MD = 35% to 45% of an industrial electricity bill. See Section 1.
- Solar ATAP (replaced NEM 3.0): up to 100% of 12-month average MD (max 1,000 kWac); exports credited at SMP ~RM0.1881/kWh vs grid purchase up to RM0.3132/kWh; credits expire monthly. Revised SELCO (Jan 2026): mandatory BESS and RM12/kWp standby charge threshold raised from 72 kWp to >1 MWac. See Section 1.
- BNM concessionary debt 3.5% – 5.0% p.a.: LCTF capped 5.0% p.a. (RM2.5M / RM10.0M, up to 10 years); HTG 3.5% (unsecured) or 5.0% (with CGC guarantee), up to RM10.0 million. See Section 2.
- GTFS 5.0: RM1.0B allocation until 31 Dec 2026; interest rebate 0%; 60% guarantee (80% Waste); User category excludes standalone solar PV. See Section 2.
- Bank products: Maybank LCTF/-i up to RM10M; CIMB RM3B SLF with up to 0.50% p.a. rebate; RHB 100% margin from 4.50% p.a.; UOB U-Solar 2.0; Bank Islam (Ditrolic Energy RM150M Sukuk); OCBC finances BESS under EE. See Section 2.
- PPAs: Tripartite SARE (TNBX) 21 years standard, ~25 sen/kWh+; Private Bilateral PPA 15 to 21 years, 10%–30% discount to TNB rate; Off-Site CRESS ~26 sen generation + SAC 20 sen/kWh (Firm w/ BESS) / 40 sen (Non-firm). See Section 3.
- BESS zero-capex: Shared-Savings IPMVP EPC 75:25 or 80:20 (ESCO : Host), 5 to 10 years (7 standard); Plus Xnergy discounted MD rate RM82.50/kW (15% below RM97.06/kW); Solarvest Powervest / UniBess 7-to-10-year leases. See Section 3.
- Tax: 2026 — 60% GITA (Tier 2) standalone solar, 100% GITA (Tier 1) BESS; 2027–2030 — standalone solar 0%, integrated solar + BESS 100% Tier 1; Pioneer/ITA/RA holders barred from GITA (MIDA Sec 3.1e); GITE solar leasing 70% exemption for 5-10 yrs, ≥60% local equity, deadline 31 Dec 2026. See Section 3.
- 25-year cashflow (500 kWp, illustrative): Outright reaches RM3,836,000 at Yr 25, Lease RM2,550,000, SARE PPA RM1,500,000. See Charts (Chart 2).
- BESS 3-tier guarantees: Tier 1 hardware (+2%-3% CAPEX), Tier 2 ≥97% peak-window availability (+3%-5% CAPEX), Tier 3 binding MD reduction with LDs (+5%-8% CAPEX). See Section 4.
- LD formula: (Guaranteed − Actual MD reduction) × RM97.06/kW; default 300 kW vs 100 kW → RM 19,412.00/month. See Section 4, Calculators.
- Preferences 2026: SMEs 80% outright debt / 15% lease / 5% PPA; Mid-Market 55/25/20; Large/MNCs 10/20/70. See Section 5, Charts (Chart 4).
- Recommendation engine: SME owner → LCTF financed purchase; SME tenant → 5-to-10 Year lease; Mid-market → split asset (loan for PV + shared-savings BESS) or GTFS 5.0 purchase (IRR 17%–30%, 4.0–6.0 year payback); Large → SARE PPA or CRESS. See Section 5, Calculators.

## Header and key metrics ribbon (above the tabs)

- Badge: "MALAYSIA ENERGY TRANSITION 2026"
- Title (H1): "C&I Solar PV & BESS Financing Intelligence Platform"
- Subtitle: "Navigating RP4 Tariffs, Solar ATAP, GTFS 5.0, Zero-Capex Models & BESS Guarantees"
- "Effective Framework: RP4 (2025–2027) & Solar ATAP"

Key Metrics Highlight Ribbon:

| Metric | Value | Sub-note |
|---|---|---|
| MV Peak MD Tariff | RM97.06 / kW | +162% vs RP3 Baseline |
| Solar ATAP Export Credit | ~RM0.1881 / kWh | SMP Wholesale Rate (Monthly Forfeiture) |
| BNM Concessionary Debt | 3.5% – 5.0% p.a. | HTG & LCTF Facilities |
| LFP BESS Turnkey Cost | RM1,150 – RM1,600 / kWh | Commercial Containerized Storage |

### Report structure (from the HTML design comments)

- Application Structure Plan (HTML comment): designed as a multi-tab interactive intelligence dashboard for corporate energy managers, financiers, and CFOs in Malaysia. Planned structure: 1) Executive Summary & Regulatory Context with TNB Tariff Shift Visualizer; 2) Bank Debt & GTFS 5.0 Explorer with dynamic facility filtering; 3) Zero-Capex vs Outright Analysis with PPA/Lease Comparison and Dynamic Financial Model; 4) BESS Risk & Warranty Matrix with interactive MD Miss Liquidated Damages Calculator; 5) Decision Engine & Segment Benchmark tailored by company size and tax status. Stated purpose: "This non-linear structure allows decision-makers to evaluate financial, regulatory, and technical trade-offs dynamically."
- Visualization & Content Choices (HTML comment):
  - TNB Tariff Increase: Goal → Compare RP3 vs RP4 charges. Method → Chart.js Bar Chart.
  - Cumulative Financial Returns: Goal → Compare 25-yr financial yields. Method → Chart.js Multi-line Chart with interactive system size inputs.
  - BESS Warranty Tiers: Goal → Organize risk/cost trade-offs across 3 tiers. Method → Styled interactive HTML Cards + Chart.js Bar Chart.
  - Customer Preferences: Goal → Display preferences by size. Method → Chart.js Stacked Bar Chart.
  - MD Miss Liability: Goal → Interactive risk calculation. Method → HTML Sliders + Live Chart.js update.
  - Confirms no SVG graphics or Mermaid JS used; HTML/CSS styling, Unicode icons and Canvas render all visuals.
- A palette comment ("Warm Neutral & Sustainable Slate") lists styling colours only.

## 1. Tariff & Regulatory Context

### The 2026 Regulatory and Tariff Inflection Point

"Commercial and industrial energy procurement in Malaysia underwent a structural shift on 1 January 2026. Two simultaneous regulatory updates—Tenaga Nasional Berhad's (TNB) Regulatory Period 4 (RP4, 2025–2027) tariff structure and the replacement of NEM 3.0 with the Solar Accelerated Transition Action Programme (Solar ATAP)—fundamentally altered the underlying economics of rooftop solar PV and Battery Energy Storage Systems (BESS). Below, explore how punitive Maximum Demand (MD) charges make BESS-driven peak shaving the primary financial lever for C&I facilities."

### TNB Demand Charge Surge: RP3 vs RP4

Caption: "Comparison of combined Capacity and Network Charges for Medium Voltage (MV) C&I users." Bar chart (see Charts, Chart 1): RP3 Baseline RM37.00, RP4 MV General RM89.27, RP4 MV ToU Peak RM97.06 (RM / kW / Month).

Billing Spike Rule: "TNB records Maximum Demand based on the single highest 30-minute average kW draw in a billing month. A single 30-minute operational spike locks in a RM89.27 to RM97.06/kW charge across the entire billing cycle, accounting for 35% to 45% of an industrial electricity bill."

### Solar ATAP & SELCO Regulatory Rules

Solar ATAP (Rooftop Allocation):
- National quota ceilings removed; installation allowed up to 100% of 12-month average MD (max 1,000 kWac / 1 MWac).
- Eliminated 1-to-1 retail tariff offsets for export.
- Surplus exports credited at Average System Marginal Price (SMP) (~RM0.1881/kWh) vs grid purchase up to RM0.3132/kWh.
- Unused export credits expire at month-end without rollover. (highlighted as a warning)

Revised SELCO Framework (Effective Jan 2026):
- Mandatory BESS requirement and RM12/kWp standby charge threshold raised from 72 kWp to **>1 MWac**.
- Large installations (>1 MWac) must integrate BESS and pay standby fees, driving adoption of EaaS/PPA bundles.

### 30-Minute Peak Spike Calculator

Slider "Unmitigated Peak Spike (kW):" (default 500 kW) → "Locked TNB Monthly Charge (MV ToU):" "RM 48,530 / month" at default. Full logic in "Calculators and interactive logic" (Calculator A).

## 2. Bank Financing & GTFS 5.0

### Bank Debt Facilities, GTFS 5.0, and Central Bank Funds

"Malaysian commercial and Islamic banks distribute low-cost debt via Bank Negara Malaysia (BNM) facilities and sovereign credit guarantees under GTFS 5.0. Notably under GTFS 5.0, the government eliminated the interest rate rebate entirely, pivoting the program strictly into a loss-given-default credit risk-sharing vehicle (60% to 80% guarantee coverage)."

### BNM Low Carbon Transition Facility (LCTF) — badge "Cap: 5.0% p.a."

- Target: Malaysian SMEs (Sales ≤RM50M manufacturing or ≤RM20M services).
- Financing Quantum: Capped at RM2.5M (turnover ≤RM25M) or RM10.0M (turnover >RM25M).
- Tenure: Up to 10 years.
- Scope: Rooftop solar PV, energy efficiency retrofits, low-carbon machinery.

### BNM High Tech and Green Facility (HTG) — badge "Cap: 3.5% - 5.0% p.a."

- Target: Strategic manufacturing/services (E&E, chemicals, aerospace) or green tech providers (≥51% Malaysian ownership).
- Financing Quantum: Up to RM10.0 million.
- Tenure: Up to 10 years.
- Lowest Debt Cost: Capped at 3.5% p.a. (unsecured) or 5.0% p.a. (with CGC guarantee).

### GTFS 5.0 Sovereign Guarantee Matrix (RM1.0B Allocation until 31 Dec 2026)

Note (verbatim): "Note: Interest rebate is 0%. Technical criteria for 'User' category exclude standalone solar PV, prioritizing industrial EE and BESS."

| Applicant Category | Max Limit (Group Exposure) | Max Tenure | CGC Guarantee % | Interest Rebate | Key Technical Scope |
|---|---|---|---|---|---|
| Producer of Green Tech | RM 100 Million | 15 Years | 60% (80% Waste) | 0% (None) | Production of green products; excludes LSS and rooftop solar PV. |
| User of Green Tech | RM 50 Million | 10 Years | 60% (80% Waste) | 0% (None) | Industrial EE retrofits, plant modernization. Excludes standalone solar. |
| ESCO (Energy Service Co) | RM 25 Million | 10 Years | 60% | 0% (None) | Financing EE assets & EPC contracts. Requires ST registration. |
| Housing Developer | RM 100 Million | 5 Years | 60% | 0% (None) | Green residential builds (selling price RM350k-RM450k). |
| Mobility Infrastructure | RM 50 Million | 5 Years | 60% | 0% (None) | EV charging infrastructure deployment by Charge Point Operators. |

### Commercial & Islamic Bank C&I Offerings (2026)

| Bank | Offering (verbatim) |
|---|---|
| Maybank / Maybank Islamic | LCTF/-i (up to RM10M) & SME Property Bundled Financing (up to 20 yrs). 0% Credit Card EPP up to 60 months with 6 solar partners. |
| CIMB / CIMB Islamic | SME RE Financing-i (up to 100% margin). RM3B Sustainability-Linked Financing (SLF) offering up to **0.50% p.a. interest rebate** tied to BEI / GHG targets. |
| RHB / RHB Islamic | RHB SME Green RE & CAPEX Financing with **100% Margin of Financing** at rates as low as 4.50% p.a. structured via Industrial Hire Purchase or Commodity Murabahah. |
| UOB Malaysia | U-Solar 2.0 platform integrated with HTG/LCTF. Bundling Tier-1 hardware (Huawei, Sungrow, Longi, Trina) with free civil studies and 1-3 yrs free O&M. |
| Bank Islam | Business Financing-i (Tawarruq) & Finance Lease-i. Lead arranger for solar/BESS Sukuk Wakalah (e.g., Ditrolic Energy RM150M Sukuk). |
| OCBC & Alliance Bank | OCBC SME Sustainable Financing explicitly finances energy storage (BESS) under Energy Efficiency without requiring prior green certifications. |

## 3. Zero-Capex & Tax Incentives

### Zero-Capex PPA, Lease, Shared-Savings & Tax Framework

"Off-takers seeking off-balance-sheet structures choose between Tripartite SARE, Private Bilateral PPAs, CRESS, Operating Leases, and Shared-Savings EPCs. Concurrently, tax incentives undergo a major policy shift: Budget 2027 terminates standalone solar GITA on 31 Dec 2026, mandating integrated BESS for 100% GITA Tier 1 starting 2027."

### On-Site & Off-Site Zero-Capex PPA Architectures

| Dimension | Tripartite SARE (TNBX) | Private Bilateral PPA | Off-Site CRESS (2026 Reform) |
|---|---|---|---|
| Parties Involved | Tripartite: TNB, RPVI (Investor), Host | Bilateral: RPVI & Host directly | RE Developer, Green Consumer & TNB Grid |
| Typical Tenure | 21 Years Standard | 15 to 21 Years | 10 to 21 Years |
| 2026 Pricing Structure | Fixed/escalated ~25 sen/kWh+ | 10%–30% discount to TNB rate | ~26 sen generation + System Access Charge (SAC) |
| Grid Access Charge (SAC) | N/A (On-site behind meter) | N/A (On-site behind meter) | 20 sen/kWh (Firm w/ BESS) / 40 sen (Non-firm) |
| Default Enforcement | TNB can disconnect main grid electricity supply (ESA 1990 Sec 29) | Contractual remedies, arbitration, system shut-off | Governed by BESC & CRESA security terms |
| End-of-Term Asset Transfer | Automatic transfer to customer | Negotiated (Transfer or Buyout) | Developer retains remote solar farm/BESS |

### BESS Maximum Demand Shaving Zero-Capex Models

1. Shared-Savings IPMVP EPC — "ESCO finances 100% of BESS + AI-EMS. Verified monthly demand savings split on a **75:25 or 80:20 basis** (ESCO : Host). ESCO carries cash-flow and performance risk. Contract tenure 5 to 10 years (7 years standard)."
2. Discounted MD Rate Model (Plus Xnergy) — "Zero upfront cost. Provider charges an effective MD rate of **RM82.50/kW** on the shaved peak portion—offering a fixed **15% discount** below TNB's RM97.06/kW MV ToU peak charge. Eliminates monthly baseline disputes."
3. Vendor Hybrid & Operating Leases (Solarvest / UniBess) — "Solarvest Powervest (Powerflex Lite: 7-yr payment for 20% downpayment equity; customer claims GITA). UniBess EaaS / Lease: 7-to-10-year operating lease structured so monthly lease fee < monthly MD savings."

### Statutory Tax Guidelines & Budget 2027 Pivot

GITA Asset Allowance (Own Consumption):
- **2026 Rules:** 60% GITA (Tier 2) on Standalone Solar; 100% GITA (Tier 1) on BESS.
- **2027–2030 Rules:** Standalone Solar PV is **0% (Removed)**. Integrated Solar PV + BESS receives **100% GITA (Tier 1)**.

Tax Mutual Exclusivity Warning (MIDA Sec 3.1e): "Companies holding **Pioneer Status**, claiming **Investment Tax Allowance (ITA)** under PIA 1986, or claiming **Reinvestment Allowance (RA)** under Schedule 7A are legally barred from claiming GITA. These firms strongly prefer Zero-Capex PPAs."

GITE Solar Leasing (For Investors): "70% tax exemption on statutory income for 5-10 yrs for SEDA-registered RPVIs. Requires ≥60% local Malaysian equity. Deadline: 31 Dec 2026."

### 25-Year Cumulative Cashflow Simulator

Caption: "Compare Outright Financed Purchase (with GITA) vs Zero-Capex SARE PPA vs Operating Lease for a 500 kWp system." Multi-line chart (see Charts, Chart 2). Code comment: "Simplified illustrative model for 500 kWp system". There are no user inputs for this chart.

## 4. BESS Guarantees & Penalties

### BESS Contractual Risk Allocation & Performance Guarantees

"Unlike solar PV where revenue is linear with sunlight, BESS peak shaving is binary: because TNB bills Maximum Demand on the single highest 30-minute peak in a month, a single 30-minute battery failure during peak hours (14:00–22:00) destroys 100% of that month's demand charge savings. Contracts manage this through a 3-tiered guarantee hierarchy."

### 3-Tier Warranty Hierarchy

| Tier | Cost adder | Heading | Description (verbatim) | Remedy / Service / Penalty (verbatim) | Where standard |
|---|---|---|---|---|---|
| Tier 1 Warranty | +2%-3% CAPEX | Hardware Capacity Retention & RTE | OEM / EPCC warranty. Warrants LFP cell capacity retention (e.g. 80% SoH at Yr 10) & Round-Trip Efficiency (85% down to 78%). | Remedy Limitation: Supplier provides free cell replacement/augmentation but explicitly excludes liability for missed TNB demand savings. | Standard in Outright CAPEX Purchases |
| Tier 2 Warranty | +3%-5% CAPEX | Peak-Window Availability Guarantee | Embedded in O&M and Operating Leases. Guarantees **≥97% system uptime specifically during peak hours (08:00–22:00)**. | Service Level: Backed by 24/7 remote NOC monitoring and mandatory 6-hour on-site emergency engineering response in Peninsular Malaysia. | Standard in Storage Service Agreements |
| Tier 3 Guarantee | +5%-8% CAPEX | Binding MD Reduction & Savings Target | Full performance wrap. Contract specifies a binding numeric Maximum Demand kW reduction target or RM savings floor. | Penalties: Shortfall results in direct Liquidated Damages equal to missed TNB charges or 100% monthly fee forfeiture. | Required for Project Finance / Shared-Savings |

### Interactive BESS Missed Peak Shortfall Penalty Calculator

Formula (verbatim): "Formula: Shortfall Penalty (RM) = (Guaranteed MD Reduction - Actual MD Reduction) × TNB RP4 ToU Rate (RM97.06/kW)"

Sliders "Guaranteed MD Peak Shaving Target:" (default 300 kW) and "Actual Achieved MD Reduction (BESS Tripped/Depleted):" (default 100 kW); outputs "Missed Shaving Headroom:" 200 kW and "Monthly Liquidated Damages (LD) Liability:" RM 19,412.00 at defaults; bar chart (Chart 3). Full logic in Calculator B.

### IPMVP Baseline Normalization & "Customer Load Breach" Carve-Out

- "Because a BESS is sized to a specific baseline envelope, it cannot suppress unscheduled spikes if factory personnel turn on unmodeled machinery lines. Advanced EMS platforms (e.g., Tanand EasiEMS) issue early Telegram alerts when rolling demand reaches 750 kW against an 800 kW ceiling."
- "If immutable BMS/EMS telemetry proves a missed peak was caused by EMS algorithm latency or battery trip, the **ESCO bears 100% of LDs**. If telemetry proves site load exceeded the contracted kW/kWh baseline envelope or personnel manually bypassed load controls, it is classified as an **excused Customer Load Breach**, relieving the provider of liability."

## 5. Strategy Engine & Benchmarks

### 2026 Customer Strategy Engine & Benchmark by Size

"Customer choices in Malaysia stratify sharply across company size, tax residency, balance-sheet sensitivity, and whether the asset is solar PV or BESS. Use the benchmark chart below or run the interactive strategy decision engine to find the optimal financing pathway."

### 2026 Procurement Model Preference Distribution by Company Segment

Caption: "Percentage breakdown of preferred financing structures across Malaysian C&I off-takers."

| Segment | Outright Bank Debt (LCTF/HTG/GTFS) | Solar Operating Lease / Vendor Hybrid | Zero-Capex PPA (SARE / Bilateral) |
|---|---|---|---|
| SMEs (50-200 kWp) | 80% | 15% | 5% |
| Mid-Market (200 kWp - 1 MWp) | 55% | 25% | 20% |
| Large / MNCs (1-10 MWp+) | 10% | 20% | 70% |

### Interactive C&I Financing Recommendation Engine

Four dropdowns (Company Scale, Tax Status, Premises Status, Scope of Procurement) produce a "Recommended Pathway" card with "Debt & Commercial Route", "Expected Benefit" and an optional tax notice. Default output (Mid-Market, Standard Corporate Tax Payer (24%), Owner-Occupier, Integrated Solar PV + BESS):

- Recommended Pathway: Split Asset Model: Outright Loan for Solar PV + Zero-Capex Shared-Savings for BESS
- Debt & Commercial Route: Finance Solar PV using GTFS 5.0 (60% CGC guarantee) or bank green loan to claim GITA. Put BESS under an IPMVP Shared-Savings EPC (75:25 ESCO split) or Plus Xnergy Discounted MD Rate (RM82.50/kW) to shift peak-miss risk to the ESCO.
- Expected Benefit: Combines high PV return with total risk insulation against TNB Maximum Demand penalty spikes.
- Tax notice: GITA Strategy Notice: Under Budget 2027 rules, standalone solar receives 0% GITA after 31 Dec 2026. Coupling your solar with a BESS unlocks **100% GITA Tier 1 allowance** on the entire combined capital expenditure, worth a 24% tax savings shield.

All branches are listed in Calculator C.

## Footer

- "Malaysia C&I Solar PV & BESS Financing Intelligence (2026)"
- "Based on TNB RP4 Tariffs, Solar ATAP, GTFS 5.0 Guidelines & MIDA/SEDA Frameworks"
- "Generated for Corporate Energy Managers, Financiers & ESCO Developers."

## Charts

### Chart 1 — TNB Demand Charge Surge: RP3 vs RP4 (`tariffChart`)

- Location: Tab 1, "TNB Demand Charge Surge: RP3 vs RP4" card.
- Type: bar; legend hidden. Y axis title: "RM / kW / Month" (begins at zero). No x-axis title.
- Series: "TNB Monthly MD Charge (RM/kW)".
- Tooltip: " Charge: RM {value to 2 decimals} / kW / month".

| Label | TNB Monthly MD Charge (RM/kW) |
|---|---|
| RP3 Baseline | 37.00 |
| RP4 MV General | 89.27 |
| RP4 MV ToU Peak | 97.06 |

### Chart 2 — 25-Year Cumulative Cashflow Simulator (`cashflowChart`)

- Location: Tab 3, bottom card "25-Year Cumulative Cashflow Simulator" ("for a 500 kWp system").
- Type: line (outright series filled). Y axis title: "Cumulative Net Benefit (RM)". X labels: "Yr 1" … "Yr 25" (index i = 0 … 24).
- Tooltip: "{series label}: RM {value, en-US thousands separators}".
- Code comment: "Simplified illustrative model for 500 kWp system". No inputs; values are fixed by code.

Series formulas (faithful to the JS; i = 0 for Yr 1):
- "Financed Outright Purchase (w/ GITA)": i = 0 → −1,200,000 (comment "Capital outlay"); i = 1 → −1,200,000 + 280,000 + 196,000 (comment "Year 1 + GITA"); i ≥ 2 → −1,200,000 + 476,000 + i × 190,000.
- "Solar Lease (15-Yr Operating)" (dashed line): (i + 1) × 102,000.
- "SARE PPA (Zero-Capex)": (i + 1) × 60,000 (comment "Net monthly savings stacked").

| Year | Financed Outright Purchase (w/ GITA) (RM) | Solar Lease (15-Yr Operating) (RM) | SARE PPA (Zero-Capex) (RM) |
|---|---|---|---|
| Yr 1 | -1,200,000 | 102,000 | 60,000 |
| Yr 2 | -724,000 | 204,000 | 120,000 |
| Yr 3 | -344,000 | 306,000 | 180,000 |
| Yr 4 | -154,000 | 408,000 | 240,000 |
| Yr 5 | 36,000 | 510,000 | 300,000 |
| Yr 6 | 226,000 | 612,000 | 360,000 |
| Yr 7 | 416,000 | 714,000 | 420,000 |
| Yr 8 | 606,000 | 816,000 | 480,000 |
| Yr 9 | 796,000 | 918,000 | 540,000 |
| Yr 10 | 986,000 | 1,020,000 | 600,000 |
| Yr 11 | 1,176,000 | 1,122,000 | 660,000 |
| Yr 12 | 1,366,000 | 1,224,000 | 720,000 |
| Yr 13 | 1,556,000 | 1,326,000 | 780,000 |
| Yr 14 | 1,746,000 | 1,428,000 | 840,000 |
| Yr 15 | 1,936,000 | 1,530,000 | 900,000 |
| Yr 16 | 2,126,000 | 1,632,000 | 960,000 |
| Yr 17 | 2,316,000 | 1,734,000 | 1,020,000 |
| Yr 18 | 2,506,000 | 1,836,000 | 1,080,000 |
| Yr 19 | 2,696,000 | 1,938,000 | 1,140,000 |
| Yr 20 | 2,886,000 | 2,040,000 | 1,200,000 |
| Yr 21 | 3,076,000 | 2,142,000 | 1,260,000 |
| Yr 22 | 3,266,000 | 2,244,000 | 1,320,000 |
| Yr 23 | 3,456,000 | 2,346,000 | 1,380,000 |
| Yr 24 | 3,646,000 | 2,448,000 | 1,440,000 |
| Yr 25 | 3,836,000 | 2,550,000 | 1,500,000 |

### Chart 3 — Liquidated Damages chart (`ldChart`)

- Location: Tab 4, inside "Interactive BESS Missed Peak Shortfall Penalty Calculator".
- Type: bar; legend hidden. Y axis title: "Kilowatts (kW)" (begins at zero).
- Series: "Kilowatts (kW)". Initial data shown; updated live to [guaranteed, actual, missed] by Calculator B.

| Label | Kilowatts (kW) (initial) |
|---|---|
| Target kW | 300 |
| Actual kW | 100 |
| Missed kW | 200 |

### Chart 4 — 2026 Procurement Model Preference Distribution by Company Segment (`preferenceChart`)

- Location: Tab 5, "2026 Procurement Model Preference Distribution by Company Segment".
- Type: stacked bar (x and y stacked). Y axis title: "Share of Off-Takers (%)"; y max 100. Legend shown.

| Series | SMEs (50-200 kWp) | Mid-Market (200 kWp - 1 MWp) | Large / MNCs (1-10 MWp+) |
|---|---|---|---|
| Outright Bank Debt (LCTF/HTG/GTFS) | 80 | 55 | 10 |
| Solar Operating Lease / Vendor Hybrid | 15 | 25 | 20 |
| Zero-Capex PPA (SARE / Bilateral) | 5 | 20 | 70 |

## Calculators and interactive logic

### Calculator A — 30-Minute Peak Spike Calculator (`calculateSpikeCost`)

- Location: Tab 1, bottom of "Solar ATAP & SELCO Regulatory Rules" card.
- Input: `spikeKw`, range slider "Unmitigated Peak Spike (kW):", min 100, max 2000, step 50, default 500. Display "{kw} kW".
- Constant: 97.06 (code comment "MV ToU Peak Rate", RM/kW).
- Formula:
  ```
  kw   = spikeKw
  cost = kw * 97.06
  show "RM " + cost (en-US, max 0 decimals) + " / month"   // label "Locked TNB Monthly Charge (MV ToU):"
  ```
- Runs on slider input and once on page load.

Outputs at default inputs (computed by running the code logic):

| spikeKw | Output |
|---|---|
| 500 (default) | RM 48,530 / month |
| 100 (min) | RM 9,706 / month |
| 2000 (max) | RM 194,120 / month |

### Calculator B — BESS Missed Peak Shortfall Penalty / Liquidated Damages Calculator (`calculateLD`)

- Location: Tab 4.
- Inputs:
  - `guaranteedKw`, range slider "Guaranteed MD Peak Shaving Target:", min 100, max 1000, step 50, default 300.
  - `actualKw`, range slider "Actual Achieved MD Reduction (BESS Tripped/Depleted):", min 0, max 1000, step 50, default 100.
- Constant: 97.06 (RM/kW, "TNB RP4 ToU Rate").
- Formula:
  ```
  missed  = max(0, guaranteed - actual)            // "Missed Shaving Headroom: {missed} kW"
  penalty = missed * 97.06                         // "Monthly Liquidated Damages (LD) Liability: RM {penalty, 2 decimals}"
  ldChart.data = [guaranteed, actual, missed]
  ```
- Runs on slider input and once on page load.

Outputs at default inputs (computed by running the code logic): guaranteed 300 kW, actual 100 kW → Missed Shaving Headroom 200 kW → Monthly LD Liability RM 19,412.00; chart [300, 100, 200]. Extremes: guaranteed 1000, actual 0 → 1000 kW → RM 97,060.00; actual ≥ guaranteed → 0 kW → RM 0.00.

### Calculator C — Interactive C&I Financing Recommendation Engine (`runRecommender`)

- Location: Tab 5.
- Inputs (dropdowns; run on change and once on page load):

| Input | Option label | Value |
|---|---|---|
| Company Scale (`companySize`) | SME (50 kWp – 200 kWp) | sme |
| | Mid-Market (200 kWp – 1 MWp) (default) | mid |
| | Large Enterprise / MNC (1 MWp – 10 MWp+) | large |
| Tax Status (`taxStatus`) | Standard Corporate Tax Payer (24%) (default) | standard |
| | Pioneer Status / ITA / RA Exemption | pioneer |
| Premises Status (`premises`) | Owner-Occupier (default) | owner |
| | Tenant / Leaseholder | tenant |
| Scope of Procurement (`assetTarget`) | Rooftop Solar PV Only | solar |
| | Integrated Solar PV + BESS (default) | hybrid |
| | Standalone BESS (Peak Shaving) | bess |

- Logic (pseudo-code faithful to the JS):
  ```
  if tax == "pioneer":                     taxWarning = W-P
  elif asset == "hybrid" or asset == "solar": taxWarning = W-G
  else:                                     taxWarning = ""   (no box rendered)

  if size == "sme":
      if premises == "tenant": primaryRec = P1; debtRoute = D1
      else:                    primaryRec = P2; debtRoute = D2
      lifetimeBenefit = L1
  elif size == "mid":
      if asset == "bess" or asset == "hybrid": primaryRec = P3; debtRoute = D3
      else:                                    primaryRec = P4; debtRoute = D4
      lifetimeBenefit = L2
  else:  # large
      primaryRec = P5; debtRoute = D5; lifetimeBenefit = L3

  render: "Recommended Pathway" [primaryRec]
          "Debt & Commercial Route:" debtRoute
          "Expected Benefit:" lifetimeBenefit
          [taxWarning box, only if non-empty]
  ```

Exact output strings:

| Code | Field | Exact string |
|---|---|---|
| P1 | primaryRec | 5-to-10 Year Solar Operating Lease |
| D1 | debtRoute | Avoid outright capital expenditure due to tenancy relocation risk. Select a vendor operating lease (e.g. Powervest or UniBess). |
| P2 | primaryRec | Financed Outright Purchase via BNM Low Carbon Transition Facility (LCTF) |
| D2 | debtRoute | Borrow via CIMB, Maybank, or RHB under BNM LCTF (capped at 5.0% p.a.) or HTG (3.5% p.a.). Leverage Solarvest Powerflex Lite to bridge any 20% downpayment equity requirement. |
| L1 | lifetimeBenefit | Owner-occupier SMEs capture 2x to 3x higher lifetime financial benefit (RM950k–RM1.6M over 25 yrs) via outright ownership than under a PPA. |
| P3 | primaryRec | Split Asset Model: Outright Loan for Solar PV + Zero-Capex Shared-Savings for BESS |
| D3 | debtRoute | Finance Solar PV using GTFS 5.0 (60% CGC guarantee) or bank green loan to claim GITA. Put BESS under an IPMVP Shared-Savings EPC (75:25 ESCO split) or Plus Xnergy Discounted MD Rate (RM82.50/kW) to shift peak-miss risk to the ESCO. |
| P4 | primaryRec | GTFS 5.0 Green Debt Financed Outright Purchase |
| D4 | debtRoute | Secure commercial bank green loan backed by GTFS 5.0. IRR expected at 17%–30% with 4.0–6.0 year payback. |
| L2 | lifetimeBenefit | Combines high PV return with total risk insulation against TNB Maximum Demand penalty spikes. |
| P5 | primaryRec | Tripartite SARE PPA or Off-Site CRESS Bilateral Contract |
| D5 | debtRoute | Preserve corporate balance sheet and avoid HQ capex freezes. Execute a 21-year SARE PPA (or CRESS wheeling at 20 sen/kWh firm SAC if rooftop space is constrained). |
| L3 | lifetimeBenefit | Delivers immediate 10%–30% OPEX tariff savings with zero balance-sheet liability and bundled Scope 2 RECs. |
| W-P | taxWarning | Pioneer Status Exclusivity Alert: Because your company enjoys Pioneer Status, ITA, or Reinvestment Allowance, MIDA Sec 3.1(e) legally prohibits direct GITA claims. You should opt for a **Zero-Capex PPA (SARE or Bilateral)** where the RPVI investor claims tax shields and passes them down via lower tariffs (~25 sen/kWh). |
| W-G | taxWarning | GITA Strategy Notice: Under Budget 2027 rules, standalone solar receives 0% GITA after 31 Dec 2026. Coupling your solar with a BESS unlocks **100% GITA Tier 1 allowance** on the entire combined capital expenditure, worth a 24% tax savings shield. |
| (none) | taxWarning | empty string; no tax box is shown |

Every branch (3 sizes × 2 tax statuses × 2 premises × 3 asset scopes = 36):

| # | Size | Tax | Premises | Asset | primaryRec | debtRoute | lifetimeBenefit | taxWarning |
|---|---|---|---|---|---|---|---|---|
| 1 | sme | standard | owner | solar | P2 | D2 | L1 | W-G |
| 2 | sme | standard | owner | hybrid | P2 | D2 | L1 | W-G |
| 3 | sme | standard | owner | bess | P2 | D2 | L1 | (none) |
| 4 | sme | standard | tenant | solar | P1 | D1 | L1 | W-G |
| 5 | sme | standard | tenant | hybrid | P1 | D1 | L1 | W-G |
| 6 | sme | standard | tenant | bess | P1 | D1 | L1 | (none) |
| 7 | sme | pioneer | owner | solar | P2 | D2 | L1 | W-P |
| 8 | sme | pioneer | owner | hybrid | P2 | D2 | L1 | W-P |
| 9 | sme | pioneer | owner | bess | P2 | D2 | L1 | W-P |
| 10 | sme | pioneer | tenant | solar | P1 | D1 | L1 | W-P |
| 11 | sme | pioneer | tenant | hybrid | P1 | D1 | L1 | W-P |
| 12 | sme | pioneer | tenant | bess | P1 | D1 | L1 | W-P |
| 13 | mid | standard | owner | solar | P4 | D4 | L2 | W-G |
| 14 | mid | standard | owner | hybrid (default) | P3 | D3 | L2 | W-G |
| 15 | mid | standard | owner | bess | P3 | D3 | L2 | (none) |
| 16 | mid | standard | tenant | solar | P4 | D4 | L2 | W-G |
| 17 | mid | standard | tenant | hybrid | P3 | D3 | L2 | W-G |
| 18 | mid | standard | tenant | bess | P3 | D3 | L2 | (none) |
| 19 | mid | pioneer | owner | solar | P4 | D4 | L2 | W-P |
| 20 | mid | pioneer | owner | hybrid | P3 | D3 | L2 | W-P |
| 21 | mid | pioneer | owner | bess | P3 | D3 | L2 | W-P |
| 22 | mid | pioneer | tenant | solar | P4 | D4 | L2 | W-P |
| 23 | mid | pioneer | tenant | hybrid | P3 | D3 | L2 | W-P |
| 24 | mid | pioneer | tenant | bess | P3 | D3 | L2 | W-P |
| 25 | large | standard | owner | solar | P5 | D5 | L3 | W-G |
| 26 | large | standard | owner | hybrid | P5 | D5 | L3 | W-G |
| 27 | large | standard | owner | bess | P5 | D5 | L3 | (none) |
| 28 | large | standard | tenant | solar | P5 | D5 | L3 | W-G |
| 29 | large | standard | tenant | hybrid | P5 | D5 | L3 | W-G |
| 30 | large | standard | tenant | bess | P5 | D5 | L3 | (none) |
| 31 | large | pioneer | owner | solar | P5 | D5 | L3 | W-P |
| 32 | large | pioneer | owner | hybrid | P5 | D5 | L3 | W-P |
| 33 | large | pioneer | owner | bess | P5 | D5 | L3 | W-P |
| 34 | large | pioneer | tenant | solar | P5 | D5 | L3 | W-P |
| 35 | large | pioneer | tenant | hybrid | P5 | D5 | L3 | W-P |
| 36 | large | pioneer | tenant | bess | P5 | D5 | L3 | W-P |

Outputs at default inputs (computed by running the code logic): branch 14 → P3 / D3 / L2 / W-G (text reproduced in Section 5).

### Other interactive logic

- Tab switcher (`switchTab`): shows one of the five tab panels; Tab 1 is shown on load. No content logic.

## Embedded data tables

All JS data arrays in the page (the recommender strings are in Calculator C).

| Variable / chart | Array | Values |
|---|---|---|
| tariffChart labels | labels | 'RP3 Baseline', 'RP4 MV General', 'RP4 MV ToU Peak' |
| tariffChart dataset "TNB Monthly MD Charge (RM/kW)" | data | 37.00, 89.27, 97.06 |
| cashflowChart `years` | labels | 'Yr 1' … 'Yr 25' (Array.from length 25, 'Yr ' + (i + 1)) |
| `outrightCashflow` | data | generated; see Chart 2 table |
| `leaseCashflow` | data | generated; (i + 1) × 102000; see Chart 2 table |
| `ppaCashflow` | data | generated; (i + 1) × 60000; see Chart 2 table |
| ldChart labels | labels | 'Target kW', 'Actual kW', 'Missed kW' |
| ldChart dataset "Kilowatts (kW)" | data (initial) | 300, 100, 200 |
| preferenceChart labels | labels | 'SMEs (50-200 kWp)', 'Mid-Market (200 kWp - 1 MWp)', 'Large / MNCs (1-10 MWp+)' |
| preferenceChart "Outright Bank Debt (LCTF/HTG/GTFS)" | data | 80, 55, 10 |
| preferenceChart "Solar Operating Lease / Vendor Hybrid" | data | 15, 25, 20 |
| preferenceChart "Zero-Capex PPA (SARE / Bilateral)" | data | 5, 20, 70 |
| Constants in calculators | scalar | 97.06 (spike and LD rate); cashflow constants 1200000, 280000, 196000, 476000, 190000, 102000, 60000 |

## Links and cited documents

The report contains no hyperlinks to sources. The only URLs are page library scripts (not citations).

| Label as shown | URL or document ID | Where used |
|---|---|---|
| Tailwind CSS library script | https://cdn.tailwindcss.com | head (styling library, not a citation) |
| Chart.js library script | https://cdn.jsdelivr.net/npm/chart.js | head (chart library, not a citation) |
| TNB RP4 Tariffs / Regulatory Period 4 (RP4, 2025–2027) | none given | Header, Tab 1, Tab 4 formula, footer |
| RP3 (baseline) | none given | Ribbon, Chart 1 |
| Solar ATAP (Solar Accelerated Transition Action Programme) | none given | Header, ribbon, Tab 1, footer |
| NEM 3.0 (replaced) | none given | Tab 1 |
| SELCO, Revised SELCO Framework (Effective Jan 2026) | none given | Tab 1 |
| System Marginal Price (SMP) | none given | Ribbon, Tab 1 |
| Bank Negara Malaysia (BNM) | none given | Tab 2 |
| BNM Low Carbon Transition Facility (LCTF) | none given | Ribbon, Tab 2, Tab 5 (D2, chart series) |
| BNM High Tech and Green Facility (HTG) | none given | Ribbon, Tab 2, Tab 5 (D2, chart series) |
| GTFS 5.0 / GTFS 5.0 Guidelines (Sovereign Guarantee Matrix) | none given | Header, Tab 2, Tab 5 (D3, D4, chart series), footer |
| CGC (named only by acronym; "CGC guarantee", "CGC Guarantee %") | none given | Tab 2 (HTG, GTFS table header), Tab 5 (D3) |
| ST registration (for ESCO category) | none given | Tab 2 GTFS table |
| LSS (excluded from GTFS Producer category) | none given | Tab 2 GTFS table |
| Maybank / Maybank Islamic (LCTF/-i, SME Property Bundled Financing, 0% Credit Card EPP) | none given | Tab 2 |
| CIMB / CIMB Islamic (SME RE Financing-i, RM3B Sustainability-Linked Financing (SLF)) | none given | Tab 2, Tab 5 (D2) |
| RHB / RHB Islamic (RHB SME Green RE & CAPEX Financing; Industrial Hire Purchase, Commodity Murabahah) | none given | Tab 2, Tab 5 (D2) |
| UOB Malaysia (U-Solar 2.0) with Huawei, Sungrow, Longi, Trina | none given | Tab 2 |
| Bank Islam (Business Financing-i (Tawarruq), Finance Lease-i, Sukuk Wakalah; Ditrolic Energy RM150M Sukuk) | none given | Tab 2 |
| OCBC & Alliance Bank (OCBC SME Sustainable Financing) | none given | Tab 2 |
| BEI / GHG targets (CIMB SLF) | none given | Tab 2 |
| Tripartite SARE (TNBX) | none given | Tab 3, Tab 5 |
| RPVI (Investor); SEDA-registered RPVIs | none given | Tab 3, Tab 5 (W-P) |
| CRESS (2026 Reform), System Access Charge (SAC) | none given | Tab 3, Tab 5 (P5, D5) |
| BESC & CRESA security terms | none given | Tab 3 PPA table |
| ESA 1990 Sec 29 (TNB disconnection for SARE default) | none given | Tab 3 PPA table |
| IPMVP (Shared-Savings EPC; Baseline Normalization) | none given | Tab 3, Tab 4, Tab 5 (D3) |
| Plus Xnergy (Discounted MD Rate Model) | none given | Tab 3, Tab 5 (D3) |
| Solarvest Powervest / Powerflex Lite | none given | Tab 3, Tab 5 (D1, D2) |
| UniBess EaaS / Lease | none given | Tab 3, Tab 5 (D1) |
| GITA Asset Allowance (Own Consumption), Tier 1 / Tier 2 | none given | Tab 3, Tab 5 (W-G, D3) |
| Budget 2027 | none given | Tab 3, Tab 5 (W-G) |
| MIDA Sec 3.1e / MIDA Sec 3.1(e) | none given | Tab 3, Tab 5 (W-P) |
| Pioneer Status; Investment Tax Allowance (ITA) under PIA 1986 | none given | Tab 3, Tab 5 |
| Reinvestment Allowance (RA) under Schedule 7A | none given | Tab 3, Tab 5 |
| GITE Solar Leasing (For Investors) | none given | Tab 3 |
| MIDA/SEDA Frameworks | none given | Footer |
| Tanand EasiEMS (Telegram alerts) | none given | Tab 4 |
| Scope 2 RECs | none given | Tab 5 (L3) |

## Extraction notes

1. No sources. The report has no hyperlinks, citations or dates per claim; the only source statement is the footer line "Based on TNB RP4 Tariffs, Solar ATAP, GTFS 5.0 Guidelines & MIDA/SEDA Frameworks". `research/round2_research_prompts.md` round 2 asks for sourced text with links and dates, not a dashboard; this report does not meet that. Every figure below is unsourced.
2. RP3 baseline RM37.00/kW. Chart 1 and the ribbon compare RP4 MV ToU Peak RM97.06/kW with one unlabelled "RP3 Baseline" of RM37.00 (no RP3 tariff category named). The "+162%" is arithmetically consistent with 37.00 (97.06 / 37.00 = +162.3%). Other reports in the folder differ: `malaysia_tnb_maximum_demand_c_i_mitigation_portal.html` gives legacy MD charges of RM30.30–RM45.10/kW, and `malaysia_c_i_solar_bess_executive_intelligence.html` charts [30.30, 45.10, 29.20, 43.60]. `malaysia_c_i_solar_bess_market_2026.html` also uses 37.00.
3. Peak-window contradiction (confirmed). The Tab 4 intro gives peak hours as "(14:00–22:00)", but the Tier 2 warranty guarantees uptime "during peak hours (08:00–22:00)". `research/round2_research_prompts.md` prompt #4 states the MV ToU weekday peak is 14:00–22:00.
4. RP4 start date. Tab 1 says C&I procurement "underwent a structural shift on 1 January 2026" through "Two simultaneous regulatory updates" (RP4 and Solar ATAP). The header calls RP4 "(2025–2027)", and `research/round2_research_prompts.md` prompt #4 says "RP4, from July 2025". The report gives no RP4 effective date of its own.
5. The 25-year cashflow chart is a hard-coded illustration presented as a "Simulator" (confirmed):
   - It has no inputs. Both the design comment ("interactive system size inputs") and the "Simulator" title imply inputs that do not exist.
   - Outright: −1,200,000 in Yr 1, then −1,200,000 + 280,000 + 196,000 = −724,000 in Yr 2. From Yr 3 the formula is −724,000 + i × 190,000, so Yr 2 → Yr 3 jumps by 380,000 (two years of 190,000). Every value from Yr 3 on carries one extra 190,000. The Yr-2 savings of 280,000 versus 190,000/yr afterwards are not explained.
   - The series is labelled "Financed" but models no loan, interest or repayments; the full 1.2M is spent in Yr 1. There is also no degradation, tariff escalation or O&M.
   - The GITA credit of 196,000 does not match the report's own rates. At 24%, a 60% GITA (2026 standalone solar) on 1.2M is 172,800 and a 100% GITA is 288,000; 196,000 implies about 68.06% of capex. Under the report's 2027–2030 rules, standalone solar gets 0% GITA.
   - SARE PPA: a flat +60,000/yr. The code comment says "Net monthly savings stacked", but the values are annual steps.
   - Lease: a flat +102,000/yr labelled "15-Yr Operating" but plotted for all 25 years. It also beats the PPA every year, which is not explained. No 15-year lease appears anywhere else in the report: leases elsewhere are 7-yr (Powerflex Lite), 7-to-10-year (UniBess) and 5-to-10 Year (recommender P1).
   - Derived crossovers: outright turns positive in Yr 5 (36,000), passes the PPA in Yr 8 and the lease in Yr 11.
6. CRESS pricing does not add up. CRESS is "~26 sen generation" plus SAC of 20 sen/kWh (firm) or 40 sen (non-firm), i.e. about 46 or 66 sen/kWh. The report's grid purchase price is "up to RM0.3132/kWh". Yet the Large-enterprise output (P5/D5/L3) promises "immediate 10%–30% OPEX tariff savings" for SARE or CRESS. The SAC figures (20 sen firm / 40 sen non-firm), SARE ~25 sen/kWh with 21-year tenure, and GTFS 5.0 RM1.0B until 31 Dec 2026 with 0% interest rebate are all present as stated, all unsourced.
7. GTFS contradicts the recommender. The GTFS table excludes standalone solar from the "User" category and "LSS and rooftop solar PV" from the "Producer" category. Yet the recommender gives mid-market rooftop-solar-only customers "GTFS 5.0 Green Debt Financed Outright Purchase" (P4/D4), and D3 says "Finance Solar PV using GTFS 5.0 (60% CGC guarantee)". The guarantor is labelled "CGC" in the GTFS table and D3; no source is given, so this should be verified. The Tab 2 intro's "60% to 80% guarantee coverage" matches the table's "60% (80% Waste)".
8. Recommender logic issues (from the code):
   - (a) Pioneer/ITA/RA customers who are SME owners or mid-market are still told to buy outright via LCTF, or to take an "Outright Loan for Solar PV ... to claim GITA" (P2/D2, P3/D3, P4/D4). The W-P warning shown alongside says GITA is prohibited and recommends a zero-capex PPA.
   - (b) Standard taxpayer + Standalone BESS shows no tax notice, although the report says BESS gets 100% GITA (Tier 1) in 2026.
   - (c) The SME branch ignores asset scope: a standalone-BESS SME gets "5-to-10 Year Solar Operating Lease" or the LCTF route. SME tenants still see L1, "Owner-occupier SMEs capture ...".
   - (d) The mid-market branch ignores premises, so tenants get outright loans.
   - (e) The large branch ignores tax, premises and asset, so standalone BESS gets "Tripartite SARE PPA or Off-Site CRESS".
   - (f) W-G's "worth a 24% tax savings shield" assumes full allowance use; the report mentions no utilisation limits (`research/round2_research_prompts.md` prompt #1 asks about the 70% statutory income cap).
   - (g) The mid-market claims "IRR expected at 17%–30% with 4.0–6.0 year payback" and the SME claim "RM950k–RM1.6M over 25 yrs", "2x to 3x" versus a PPA, are unsourced. The 500 kWp chart's Yr-25 ratio (3,836,000 / 1,500,000 = 2.56x) falls in the 2x–3x range.
9. Spike calculator semantics. It multiplies the entire spike kW by 97.06, giving the full monthly MD charge for that kW, not the extra cost of the spike over the normal baseline. It always uses the ToU rate even though the Billing Spike Rule gives a RM89.27–RM97.06 range. The "35% to 45% of an industrial electricity bill" share is unsourced.
10. LD calculator: one month only, at the fixed 97.06 rate. It implements only the "missed TNB charges" form of Tier 3 LDs, not the "100% monthly fee forfeiture" alternative. If actual is at or above the guarantee, missed is clamped to 0. The arithmetic matches the stated formula, and the HTML placeholders match the default outputs.
11. Preference shares are hard-coded and unsourced. Chart 4 shows them as a 2026 distribution; each segment sums to 100.
12. Design comment versus implementation. The comment promises a "Chart.js Bar Chart" for BESS Warranty Tiers (none exists), "interactive system size inputs" for the cashflow chart (none exist), and "dynamic facility filtering" for Tab 2 (none exists; the facility cards and GTFS table are static).
13. Budget 2027 tax claims (present as stated, unsourced): standalone solar GITA "0% (Removed)" for 2027–2030 and "terminates ... on 31 Dec 2026"; integrated solar + BESS 100% GITA Tier 1 from 2027; 2026: 60% Tier 2 for standalone solar, 100% Tier 1 for BESS; GITE leasing 70% for 5-10 yrs, ≥60% local equity, "Deadline: 31 Dec 2026", with no mention of any Budget 2027 extension. These overlap with urgent prompt #1 and need official verification.
14. Other unsourced specifics worth verifying:
    - ESA 1990 Sec 29 (TNB disconnection power for SARE default)
    - MIDA Sec 3.1(e) exclusivity
    - Revised SELCO threshold "from 72 kWp to >1 MWac" and RM12/kWp standby charge
    - SMP ~RM0.1881/kWh (no month given)
    - LFP BESS turnkey RM1,150 – RM1,600 / kWh (ribbon only; not used in any calculation)
    - LCTF/HTG caps and quanta
    - Bank product details (e.g. CIMB RM3B SLF, 0.50% p.a. rebate; RHB 4.50% p.a.; Ditrolic Energy RM150M Sukuk)
    - Warranty cost adders (+2%-3%, +3%-5%, +5%-8% CAPEX)
    - Tier 2 "6-hour" response time
    - Tanand EasiEMS 750 kW / 800 kW example
15. Internally consistent checks: Plus Xnergy RM82.50/kW is 15% below RM97.06/kW (97.06 × 0.85 = 82.501). The shared-savings split 75:25 (ESCO : Host) matches D3. The ribbon's "3.5% – 5.0% p.a." matches the HTG/LCTF cards. CRESS "20 sen/kWh firm SAC" in D5 matches the PPA table.

Prompt coverage (research/round2_research_prompts.md prompt #6 "Financing and business models"):

1. Bank green financing (Maybank, CIMB, RHB, Bank Islam etc.), current GTFS terms, Bank Negara funds: **answered**, unsourced. Section 2 covers the LCTF and HTG cards, the GTFS 5.0 matrix (limits, tenure, guarantee %, 0% rebate, RM1.0B to 31 Dec 2026) and the bank offerings table (Maybank, CIMB, RHB, UOB, Bank Islam, OCBC & Alliance).
2. Zero-capex models (SARE vs private PPA, leases, shared-savings for MD reduction; tenure, pricing, who funds, requirements such as RPVI registration and GITE): **partly answered**, in Section 3 (PPA table, BESS zero-capex models, GITE box) and Calculator C. Tenure and pricing are given for SARE, Bilateral, CRESS and shared-savings, and funders are named (RPVI investor, ESCO finances 100%). Lease pricing is only qualitative ("monthly lease fee < monthly MD savings"). RPVI registration requirements are not described beyond "SEDA-registered RPVIs" and GITE's ≥60% local equity.
3. How BESS performance risk is handled (savings guarantees, MD target guarantees, penalties for a missed peak): **answered**, unsourced. Section 4 covers the 3-tier guarantees, the LD formula and calculator, and the Customer Load Breach carve-out; the Plus Xnergy model in Section 3 also applies.
4. What C&I customers prefer in 2026, outright or zero-capex, by company size: **answered, but with hard-coded unsourced percentages**. See Section 5 (Chart 4) and the recommendation engine.



<!-- ===== FILE: kb/sources/R7_green_tax_portal.md ===== -->
# FILE: kb/sources/R7_green_tax_portal.md

---
id: R7
title: "Malaysia Green Tax Incentives Framework (Post-Budget 2027)"
source_file: malaysia_green_tax_incentives_portal.html
source_modified: 2026-10-23 15:02
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js)
research_prompt: "#1 Green tax incentives after Budget 2027 (research/round2_research_prompts.md)"
stated_scope: "Malaysia Green Tax Incentives Portal — Post-Budget 2027 Regulatory & Financial Decision Framework (As of Oct 2026); badge 'Budget 2027 Enacted'; 'Coverage: 2024–2030 Rules'. Build comment: executive SPA with 7 tabs, tax calculator engine, rate comparison matrix, milestone cutoff tool and unconfirmed-items tracker, designed for C&I CFOs, energy developers and tax advisors."
stated_sources: "Footer: 'Primary Legal Sources: MOF Speech (9 Oct 2026), MOF Appendix 25 (tax-measures.pdf), MIDA Briefing Deck (12 Oct 2026), MGTC Guidelines, LHDN PR 4/2023, P.U. (A) 243/2024 & P.U. (A) 247/2024.' | Chart caption: 'Source: MOF Appendix 25 (tax-measures.pdf) & MIDA Belanjawan 2027 Release (12 Oct 2026).'"
as_of: "As of Oct 2026 (header); Budget 2027 tabled 9 October 2026; MIDA release / briefing deck 12 Oct 2026; current regime 2024–2026; Budget 2027 regime 2027–2030 (effective 1 Jan 2027); GITA extended to 31 December 2030; statutory cutoff 31 December 2026; SVA changes effective YA 2027; five items unconfirmed 'as of October 2026'"
sections: ["1. Overview & Policy Pivot", "2. Rate Matrix (2027–2030)", "3. 31 Dec 2026 Deadline", "4. GITE Leasing Phase-Out", "5. Tax & ROI Engine", "6. EE & Finance Options", "7. Unconfirmed Items & Audit"]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R7 — Malaysia Green Tax Incentives Framework (Post-Budget 2027)

> Faithful, complete markdown extract of `malaysia_green_tax_incentives_portal.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- Budget 2027 was tabled on 9 October 2026 (bs27.pdf) and extends GITA by four years until 31 December 2030; Appendix 25 ("Review of Green Technology Tax Incentive") restructures eligibility toward integrated renewable energy + battery storage (Solar + BESS/ESS). See section 1.
- Integrated Solar PV + BESS/ESS (own use): 100% GITA, Tier 1b, 2027–2030, 70% statutory income (SI) set-off. KPI says "Upgraded from 60% split"; the matrix gives the current regime as "Split 60% / 100%". See sections 1, 2.
- Standalone C&I solar PV (own use): 60% GITA (Tier 2) in 2024–2026, 0% GITA from 1 Jan 2027 ("Omitted from Tier 2b RE list. Must be integrated with BESS/ESS."). See sections 1, 2.
- Standalone BESS (own use): 100% GITA (Tier 1) in 2024–2026, "0% Standalone (Must integrate)" in 2027–2030. This appears in the matrix and the overview chart only. See section 2 and Charts.
- Energy efficiency assets (chillers/boilers/LED): 60% GITA (Tier 2), then 0% after 31 Dec 2026, shifted to the extended ACA under Appendix 28 (100% write-off over 2 years: 20% IA + 40% AA), effective 2027–2030. See sections 1, 2, 6.
- GITE Solar Leasing (70% income tax exemption for RPVIs, 5 to 10 years, P.U. (A) 247/2024) is not extended into 2027 and expires 31 Dec 2026. GITA Project Tier 3 (commercial solar projects, 100% GITA 5 yrs) is abolished. See sections 1, 2, 4.
- 31 Dec 2026 cutoff: the supplier invoice / QCE incurred date, full commissioning (COD) and MGTC receipt of the application must all fall on or before 31 Dec 2026 (MGTC Guideline REC-GTGT-007 Sec 3(d) and Section 7; LHDN PR 4/2023; ITA Schedule 3). See section 3.
- MGTC applications must be submitted within 24 months of the invoice date. See section 1.
- Mechanics: Schedule 3 CA is deducted first (P.U. (A) 243/2024 Para 6(1)). GITA then offsets SI up to 70% per YA, and unused GITA is carried forward indefinitely (Para 6(4)). Tier 1b = 100% CA + 100% GITA = "200% total tax deduction", stated as cash tax savings of "48.0% of capex" at 24%. See section 5.
- Engine at defaults (QCE RM 2,000,000; SI RM 1,500,000; Tier 1b; 24%): Year-1 CA RM 680,000, Year-1 GITA used RM 574,000, carry-forward RM 1,426,000, 5-year cumulative cash tax saving RM 912,000. See Calculators.
- RPVI pre-2027 GITE lock-in prerequisites: minimum 3MW aggregated COD with a SEDA verification letter; application received by MIDA before the first sales/energy invoice; at least 60% Malaysian equity; 5 full-time employees (2 competent green personnel); 1 entity per corporate group. See section 4.
- Other Budget 2027 instruments: SVA per-asset cap RM2,000 → RM3,000 and non-MSME annual cap RM20,000 → RM30,000 (Appendix 12, YA 2027); Green Sustainability Fund 2.0 (RM2 Billion, 1% p.a. subsidy for 5 years, tenure up to 10 years); TNB RM15 Billion grid investment; KWAP Dana Iklim RM1 Billion; Appendix 15 Sukuk PRISMA issuance-cost deduction. See section 6.
- Five items unconfirmed as of October 2026: gazettement of the 2024–2026 and 2027–2030 orders; transitional treatment; minimum BESS sizing ratio and retrofit rules; MyHIJAU 100% GITA; Appendix 15 body text. See section 7.
- Compliance rules: 5-year holding period with full clawback (P.U. (A) 243/2024 Para 7); MGTC Validation Letter required before filing; hire-purchase QCE claimed on capital principal paid (LHDN PR 4/2023). See section 7.

## 1. Overview & Policy Pivot

### Global page header, navigation and footer (shown on every tab)

- Header title: "Malaysia Green Tax Incentives Portal"
- Header subtitle: "Post-Budget 2027 Regulatory & Financial Decision Framework (As of Oct 2026)"
- Header badge: "Budget 2027 Enacted"
- Header note: "Coverage: 2024–2030 Rules"
- Navigation tabs: 1. Overview & Policy Pivot; 2. Rate Matrix (2027–2030); 3. 31 Dec 2026 Deadline; 4. GITE Leasing Phase-Out; 5. Tax & ROI Engine; 6. EE & Finance Options; 7. Unconfirmed Items & Audit
- Footer line 1: "Malaysia Green Tax Incentives Analytical Portal — Post-Budget 2027 Regulatory Assessment"
- Footer line 2: "Primary Legal Sources: MOF Speech (9 Oct 2026), MOF Appendix 25 (tax-measures.pdf), MIDA Briefing Deck (12 Oct 2026), MGTC Guidelines, LHDN PR 4/2023, P.U. (A) 243/2024 & P.U. (A) 247/2024."

### Build comments (HTML comments, not visible on the page)

- Chosen palette: "Warm Forest & Slate Neutral" (styling).
- Application Structure Plan: "Executive SPA layout with 7 functional tabs, dynamic tax calculator engine, interactive rate comparison matrix, milestone cutoff tool, and unconfirmed items tracker. Designed for C&I CFOs, energy developers, and tax advisors to explore Post-Budget 2027 green tax rules without non-linear friction."
- Visualization & Content Choices: "Source Report -> Interactive SPA Dashboard -> Canvas Charts (Chart.js), Interactive Data Filters, Multi-Year Tax Benefit Engine -> Pure HTML/CSS & Vanilla JS -> Justification: Ensures rapid, interactive synthesis of complex tax codes and decision rules without external dependencies or forbidden SVG/Mermaid JS."
- "CONFIRMATION: NO SVG graphics used. NO Mermaid JS used."

### Executive Summary: The Budget 2027 Green Tax Restructuring

Tabled on 9 October 2026 by Prime Minister and Finance Minister Datuk Seri Anwar Ibrahim via the official Ministry of Finance (MOF) portal (`bs27.pdf`), Budget 2027 extends Malaysia's Green Investment Tax Allowance (GITA) framework by four years until **31 December 2030**. However, the governing statutory annex—**Appendix 25: Review of Green Technology Tax Incentive**—fundamentally restructures asset and project eligibility. The corporate tax code now shifts fiscal support exclusively toward **integrated renewable energy and battery storage systems (Solar + BESS/ESS)** to tackle Peninsular Malaysia grid intermittency and peak demand, while withdrawing tax subsidies from standalone behind-the-meter solar, standalone energy efficiency equipment, and third-party solar leasing providers after 31 December 2026.

### KPI highlight cards

| Card | Headline value | Sub-line | Note |
|---|---|---|---|
| Integrated RE + BESS | 100% GITA | Tier 1b (2027–2030) \| Own Use | Upgraded from 60% split. Offsets up to 70% Statutory Income. |
| Standalone C&I Solar PV | 0% GITA | Effective 1 Jan 2027 | Omitted from Tier 2b RE list. Must be integrated with BESS/ESS. |
| GITE Solar Leasing | EXPIRED | Cutoff: 31 Dec 2026 | 70% Income Tax Exemption for RPVIs/PPAs not extended into 2027. |
| Mandatory MGTC Window | 24 Months | Post-Purchase Requirement | Applications must be submitted to MGTC within 24 months of invoice date. |

### The Policy Shift: Standalone vs Integrated Asset Treatment (chart panel)

"Comparison of qualifying tax allowance rates under the current regime (2024–2026) vs the enacted Budget 2027 regime (2027–2030)." The bar chart's data is in Charts, Chart 1.

Caption: "Source: MOF Appendix 25 (tax-measures.pdf) & MIDA Belanjawan 2027 Release (12 Oct 2026)."

### Core Strategic Takeaways for Commercial & Industrial Energy Users

1. **Battery Storage (BESS) is Now Mandatory for Solar Tax Relief.** C&I taxpayers installing solar PV arrays for own consumption on or after 1 January 2027 must co-deploy BESS/ESS to claim the 100% GITA Asset allowance under Tier 1b. Standalone solar capex receives 0% GITA.
2. **Third-Party PPA / Leasing Models Lose Fiscal Parity.** Solar leasing companies (RPVIs) lose the 70% GITE tax exemption after 31 December 2026. Project finance will pivot sharply toward host-owned balance-sheet capital expenditure or bank hire purchase.
3. **Standalone Energy Efficiency Shifted to Accelerated Capital Allowance.** Direct GITA for standalone energy efficiency assets (chillers, boilers, LED) expires on 31 Dec 2026. Users must pivot to the extended Accelerated Capital Allowance (ACA) under Appendix 28 (100% write-off over 2 years).

Callout, **Urgent Pre-2027 Action:** Projects seeking standalone 60% GITA solar or 70% GITE leasing must be fully commissioned and submitted to MGTC/MIDA on or before **31 December 2026**.

## 2. Rate Matrix (2027–2030)

### GITA Asset & Project Rates Comparison Matrix (2027–2030)

"Detailed regulatory comparison across statutory tiers defined in MOF Appendix 25 and Lampiran 25."

A "Filter Category" dropdown filters the table. Options: All Green Asset Categories; GITA Assets (Own Consumption - MGTC); GITA Projects (Business Purpose - MIDA); GITE Leasing (RPVI / PPA - SEDA/MIDA). The logic is in Calculators, item C.

The table is rendered from the JS array `matrixData` (11 rows; raw fields in Embedded data tables). As displayed:

| Filter group | Green Technology Category | Current Regime (2024–2026) | Enacted Budget 2027 Regime (2027–2030) | SI Set-Off Cap | Administering Agency & Citations |
|---|---|---|---|---|---|
| GITA Assets | Standalone Solar PV (Own Use) | 60% GITA (Tier 2) | 0% (Discontinued) | 70% SI | MGTC / LHDN (App 25, Lampiran 25) |
| GITA Assets | Standalone BESS (Own Use) | 100% GITA (Tier 1) | 0% Standalone (Must integrate) | 70% SI | MGTC / LHDN (App 25, Lampiran 25) |
| GITA Assets | Integrated Solar PV + BESS/ESS (Own Use) | Split 60% / 100% | 100% GITA (Tier 1b) | 70% SI | MGTC / LHDN (App 25, Lampiran 25) |
| GITA Assets | Energy Efficiency Assets (Chillers/Boilers) | 60% GITA (Tier 2) | 0% (Shifted to ACA App 28) | 70% SI | MGTC / LHDN (App 25, Lampiran 25) |
| GITA Assets | Locally Produced EV Chargers / Waste / Water | 100% / 60% GITA | 100% GITA (Tier 1a) | 70% SI | MGTC / LHDN (App 25, Lampiran 25) |
| GITA Assets | Imported EV Chargers / Waste / Water | 60% GITA | 60% GITA (Tier 2a) | 70% SI | MGTC / LHDN (App 25, Lampiran 25) |
| GITA Projects | Commercial Solar PV Project | 100% GITA 5 yrs (Tier 3) | 0% (Tier 3 Abolished) | 70% SI | MIDA (App 25, MIDA) |
| GITA Projects | Non-Solar RE Projects (Biomass/Hydro) | 100% GITA 5 yrs (Tier 3) | 60% GITA 5 yrs (Tier 2b) | 70% SI | MIDA (App 25, MIDA) |
| GITA Projects | Commercial EV Charging Stations | 100% GITA (100% SI) | 60% GITA (70% SI) | 70% SI | MIDA (App 25, MIDA) |
| GITA Projects | Green Hydrogen & OTEC Projects | 100% GITA (Green H2) | 100% GITA 5+5 yrs (Tier 1) | 100% / 70% SI | MIDA (App 25, MIDA) |
| GITE Leasing | GITE Solar Leasing (RPVI / PPA) | 70% Income Exemption | EXPIRED (0% Post-2026) | 70% SI | SEDA / MIDA (App 25, P.U.(A) 247) |

### GITA Assets (Own Consumption) Statutory Tiers

- **Tier 1b: 100% GITA (70% SI Set-Off).** Renewable Energy Integrated System (Biomass, Biogas, Mini Hydro, Solar, Geothermal, Wind) + Battery Energy Storage System (BESS) / Energy Storage System (ESS).
- **Tier 1a: 100% GITA (70% SI Set-Off) — Locally Produced.** EV infrastructure, waste composting/recycling systems, wastewater/rainwater systems manufactured locally ("keluaran tempatan").
- **Tier 2a/2b: 60% GITA (70% SI Set-Off).** Tier 2a: Non-local EV/waste/water systems. Tier 2b: Standalone RE (Biomass, Biogas, Mini Hydro, Geothermal, Wind). *Note: Standalone Solar & EE explicitly excluded.*

### GITA Projects & GITE Leasing Breakdown

- **GITA Project Tier 1: 100% GITA for 5+5 Years.** Green Hydrogen Production and Ocean Thermal Energy Conversion (OTEC). Set off against 100% or 70% Statutory Income.
- **GITA Project Tier 2: 60% GITA for 5 Years.** EV Charging Stations (business purpose) & Non-Solar RE projects. SI set-off ceiling reduced from 100% to 70% starting 1 Jan 2027.
- **Discontinued / Expired Tracks (0%).** GITA Project Tier 3 (Commercial Solar Projects) is abolished. GITE Solar Leasing (70% Tax Exemption for RPVIs) expires 31 Dec 2026.

## 3. 31 Dec 2026 Deadline

### The 31 December 2026 Regulatory Cliff: Exact Milestone Requirements

Despite the headline extension of GITA to 2030, **31 December 2026** remains a strict statutory cutoff for six major green incentive categories. Taxpayers attempting to claim pre-2027 rules (such as 60% standalone solar GITA or 70% GITE leasing) must satisfy three overlapping requirements across MGTC Guidelines, LHDN Public Rulings, and MOF Appendix 25.

### Milestone steps

| Step | Milestone | Requirement text | Deadline flag |
|---|---|---|---|
| Step 1: Supplier Invoicing & QCE | CAPEX Incurred Date | Supplier invoice date defines purchase timing. Per LHDN Public Ruling 4/2023 & ITA Schedule 3, plant/machinery capex is legally incurred when capable of business use. | Must be on/before 31 Dec 2026 |
| Step 2: Physical COD | Full Commissioning | Under MGTC Guideline REC-GTGT-007 Sec 3(d), GITA Asset applications can only be filed *after* the asset/project is fully commissioned and operational. | Must be completed by 31 Dec 2026 |
| Step 3: Verification Cutoff | MGTC Application Receipt | Section 7 of MGTC Guideline restricts eligibility to "applications received by MGTC from 1 Jan 2024 until 31 Dec 2026". Submissions after 31 Dec fall under 2027 rules. | Received by MGTC on/before 31 Dec 2026 |

### Interactive Cutoff Readiness Audit Checklist

"Check your project milestones below to verify whether your asset qualifies for the 2024–2026 regime or must transition to the 2027–2030 rules:"

1. **Purchase Invoice Issued & Deposit Paid:** Taxpayer received supplier invoice and incurred qualifying capex on or before 31 December 2026.
2. **Physical Installation & Commissioning (COD):** Solar PV or EE system is fully installed, grid-connected, and commissioned on or before 31 December 2026.
3. **Application Received by MGTC / MIDA:** Formal GITA GITA/A application received by MGTC or online submission logged at MIDA on or before 31 December 2026.
4. **BESS Integration Status:** System includes co-deployed Battery Energy Storage System (BESS) or Energy Storage System (ESS).

The result box starts as "Status: Pending selection above...". The branch logic and every output text are in Calculators, item B.

## 4. GITE Leasing Phase-Out

### GITE for Solar Leasing Phase-Out & C&I Project Finance Restructuring

Under the 2024–2026 framework, Registered Solar PV Investors (RPVIs) operating solar PPAs enjoyed a **70% Income Tax Exemption** for 5 to 10 years under `P.U. (A) 247/2024`. Budget 2027 explicitly **omits GITE Solar Leasing** from the 2027–2030 extension in Appendix 25. This creates a seismic shift in C&I solar project finance across Peninsular Malaysia.

### Pre-2027 Third-Party PPA Model (Expired)

- (cross icon) RPVI receives 0% GITE on leasing revenue starting 1 Jan 2027.
- (cross icon) GITA Project Tier 3 (100% GITA for solar projects) is abolished.
- (neutral bullet) Host company receives zero capital allowances (off-balance sheet asset).
- (neutral bullet) Requires RPVI to maintain 60% Malaysian equity & 5 full-time local staff.

### Post-2027 Host-Owned Integrated Capex Model (Recommended)

- (tick) Host company claims **100% GITA Asset (Tier 1b)** on Solar + BESS capex.
- (tick) Host company claims **100% Schedule 3 Capital Allowances** (200% combined tax shield).
- (tick) BESS shaves monthly Maximum Demand (MD) charges during TNB peak tariff hours.
- (tick) Eligible for **Green Sustainability Fund 2.0** (1% p.a. interest subsidy for 5 yrs).

### Strict Prerequisites for RPVIs Locking In Pre-2027 GITE before Cutoff

"RPVIs seeking to register before 31 December 2026 must adhere to MIDA 2024 Guidelines & P.U. (A) 247/2024 Para 5(3):"

| Prerequisite | Requirement |
|---|---|
| Min 3MW COD Threshold | Must achieve aggregated minimum 3MW installed capacity under NEM or SelCo with SEDA verification letter. |
| First Sales Invoice Rule | Application MUST be received by MIDA *before* issuing the first sales/energy invoice to off-taker. |
| Substance & Equity Criteria | Min 60% Malaysian equity, 5 full-time employees (2 competent green personnel), and 1 entity per corporate group. |

## 5. Tax & ROI Engine

### GITA Utilization Mechanics & Interactive ROI Tax Calculator Engine

GITA is granted **in addition to** standard Schedule 3 Capital Allowances (CA). A company acquiring a Tier 1b asset (100% GITA) receives 100% CA + 100% GITA = **200% total tax deduction on qualifying capex**. Per `P.U. (A) 243/2024` Para 6(1), deducting Schedule 3 CA first is legally mandatory. GITA then exempts Statutory Income up to a maximum cap of **70% per Year of Assessment (YA)**, with unutilised GITA carried forward **indefinitely** under Para 6(4).

### Financial & Tax Inputs (calculator form)

- Qualifying Capital Expenditure (QCE - RM): default 2000000, step 50000
- Annual Statutory Income (SI - RM): default 1500000, step 50000
- Asset Incentive Category: 2027 Integrated Solar + BESS (100% GITA Tier 1b) [default]; Pre-2027 Standalone Solar PV (60% GITA Tier 2); 2027 EE Equipment (100% ACA - 2-Year Write-Off)
- Corporate Income Tax Rate: 24% Standard Corporate Rate [default]; 15% MSME Preferential Rate

Note box, **Combined Shield Formula:** Total Tax Shield = Capex × (CA % + GITA %) × Tax Rate. Under Tier 1b (200%), cash tax savings equals **48.0% of capex** at the 24% tax rate.

### Live output cards

| Card | Default display before calculation | Sub-caption |
|---|---|---|
| Year 1 Schedule 3 CA | RM 0 | 20% IA + 14% AA (34%) |
| Year 1 GITA Utilized | RM 0 | Capped at 70% Statutory Inc |
| Carry-Forward GITA | RM 0 | Indefinite carry-forward |

Chart panel: "5-Year Cumulative Tax Benefit & Cash Flow Simulation" (Charts, Chart 2). The formula and computed outputs are in Calculators, item A.

## 6. EE & Finance Options

### Alternative Budget 2027 Instruments for Energy Efficiency & Green Finance

While Budget 2027 removed direct GITA from standalone energy efficiency equipment, MOF deployed four complementary fiscal, capital allowance, and concessional debt instruments to support C&I energy management and demand reduction.

### Instrument 1: Extended Accelerated Capital Allowance (ACA)

- Tag: Appendix 28. Effective: 2027–2030.
- Grants a 100% tax write-off over **2 years** (20% Initial Allowance + 40% Annual Allowance) for:
  - Procurement of plant and machinery from local manufacturers
  - ICT equipment, custom software, and AI Energy Management Systems (EMS/BMS)
- Footer: *Primary substitute tax shield for energy efficiency retrofits after GITA removal.*

### Instrument 2: Expanded Small Value Assets (SVA) Write-Off

- Tag: Appendix 12. Effective: YA 2027.
- Increases the 100% immediate Year-1 write-off thresholds for low-cost operational assets:
  - Per-asset cap raised from **RM2,000 to RM3,000**
  - Non-MSME annual cap raised from **RM20,000 to RM30,000** (Unlimited for MSMEs)
- Footer: *Covers IoT energy sensors, smart sub-meters, and VFD drives under RM3,000 per unit.*

### Instrument 3: Green Sustainability Fund 2.0

- Tag: Touchpoints Page 14. Fund Size: RM2 Billion.
- Concessional debt facility administered via commercial banking institutions to subsidize decarbonization capex:
  - **1% p.a. profit/interest rate subsidy** for the first 5 years
  - Financing tenure up to 10 years for C&I low-carbon transition projects
- Footer: *Directly lowers borrowing costs for corporate Solar + BESS capital expenditure.*

### Instrument 4: Utility Grid & Sukuk PRISMA Framework

- Tag: Budget Speech Para 112. Label: Macro Grid & Sukuk.
- Supporting infrastructure commitments and capital market tax deductions:
  - TNB RM15 Billion investment to upgrade national grid flexibility
  - Appendix 15: Income tax deduction on issuance costs for Sukuk PRISMA
  - KWAP Dana Iklim RM1 Billion allocation for green infrastructure
- Footer: *Strengthens grid capacity to absorb high penetration of industrial solar + BESS.*

## 7. Unconfirmed Items & Audit

### Unconfirmed Items & Operational Compliance Safeguards

In accordance with strict evidentiary standards, five regulatory items could not be independently confirmed as of October 2026 pending gazettement of official Exemption Orders by MOF, AGC, LHDN, or MGTC.

1. **Gazettement Status of 2024–2026 & 2027–2030 Exemption Orders.** While `P.U. (A) 243/2024` covers historical GITA Assets up to 31 Dec 2023, LHDN's Joint Memorandum response confirms that the draft Gazette Order for the 2024–2026 and 2027–2030 GITA Asset framework remains in drafting stage ("Draf GITA Asset sedang dimuktamadkan").
2. **Transitional Treatment for Late-2026 Invoices Commissioned in 2027.** It cannot be confirmed whether MOF will grant transitional grandfathering for standalone solar PV invoiced in late 2026 but commissioned/verified by MGTC in early 2027. Under published guidelines, MGTC verification date strictly governs eligibility.
3. **Minimum BESS Sizing Ratio & Retrofit Rules for Tier 1b.** Pending publication of MGTC's 2027–2030 Guidelines, the mandatory minimum battery storage capacity ratio (kWh BESS per kWp solar) and whether retrofitting BESS onto an existing pre-2027 solar array qualifies for Tier 1b remain unconfirmed.
4. **Budget 2026 Proposal for 100% GITA on General MyHIJAU Products.** Budget 2027 codifies the "locally produced" 100% Tier 1 distinction specifically for EV, waste, and water systems. Whether general MyHIJAU local mark products retain 100% GITA without statutory restriction remains unconfirmed.
5. **Body Text of Appendix 15 (Sukuk PRISMA).** While listed in the Table of Contents of `tax-measures.pdf` and speech text, the full body text of Appendix 15 was truncated in public extracts and cannot be verified.

### Mandatory Statutory Compliance Rules (LHDN Audit Risk)

| Rule | Text |
|---|---|
| 5-Year Asset Holding Period | Per `P.U. (A) 243/2024` Para 7, if a GITA asset is disposed of within 5 years of acquisition, all claimed GITA exemptions are clawed back in full. |
| Validation Letter Prerequisite | Taxpayers MUST NOT file tax returns claiming GITA before obtaining MGTC's formal Validation Letter (Subject to LHDN audit penalties). |
| Hire Purchase Instalment Basis | Per LHDN PR 4/2023, for hire purchase assets, QCE is claimed progressively based strictly on the capital principal portion paid during the basis period. |

## Charts

### Chart 1: Policy shift bar chart (`chartOverviewShift`)

- Location: Tab 1, panel "The Policy Shift: Standalone vs Integrated Asset Treatment".
- Type: grouped bar. Y-axis title: "GITA Rate (%)", begins at 0, max 100. X-axis: category labels. Tick labels longer than 16 characters are cut to 14 characters plus "...", so "Integrated Sol..." and "EV Chargers (L...".
- Legend at top. Tooltip format: "{series label}: {value}% Allowance", for example "Current (2024–2026): 60% Allowance".
- Caption: "Source: MOF Appendix 25 (tax-measures.pdf) & MIDA Belanjawan 2027 Release (12 Oct 2026)."

| Label | Current (2024–2026) | Budget 2027 (2027–2030) |
|---|---|---|
| Standalone Solar | 60 | 0 |
| Standalone BESS | 100 | 0 |
| Integrated Solar+BESS | 60 | 100 |
| EE Assets | 60 | 0 |
| EV Chargers (Local) | 100 | 100 |

### Chart 2: 5-year cumulative tax benefit line chart (`chartTaxBenefit`)

- Location: Tab 5, panel "5-Year Cumulative Tax Benefit & Cash Flow Simulation".
- Type: filled line. One series: "Cumulative Cash Tax Savings (RM)". X labels: Year 1, Year 2, Year 3, Year 4, Year 5. Y-axis title: "Tax Savings (RM)", begins at 0, ticks formatted as "RM " + (value/1000, 0 decimals) + "k".
- Data is computed live by `calculateTaxBenefits()` (Calculators, item A). Series at the default inputs (Tier 1b, 24%):

| Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|
| 300,960 | 573,120 | 777,600 | 844,800 | 912,000 |

The series for all six category × tax-rate combinations at default QCE/SI is in Calculators, item A.

## Calculators and interactive logic

### A. Tax benefit engine (`calculateTaxBenefits()`)

**Location:** Tab 5, "Tax & ROI Engine". It runs on page load (`DOMContentLoaded`), on any input change, and every time Tab 5 is opened.

**Inputs**

| Input | Type | Default | Options / step |
|---|---|---|---|
| `calcCapex`, Qualifying Capital Expenditure (QCE - RM) | number | 2000000 | step 50000; parsed with parseFloat, empty or invalid input becomes 0 |
| `calcStatIncome`, Annual Statutory Income (SI - RM) | number | 1500000 | step 50000; parsed with parseFloat, empty or invalid input becomes 0 |
| `calcCategory`, Asset Incentive Category | select | tier1b | `tier1b` = "2027 Integrated Solar + BESS (100% GITA Tier 1b)"; `standalone2026` = "Pre-2027 Standalone Solar PV (60% GITA Tier 2)"; `aca2027` = "2027 EE Equipment (100% ACA - 2-Year Write-Off)" |
| `calcTaxRate`, Corporate Income Tax Rate | select | 0.24 | `0.24` = "24% Standard Corporate Rate"; `0.15` = "15% MSME Preferential Rate"; parse failure falls back to 0.24 |

**Constants by category**

| Category | Year-1 CA rate | Year-2+ CA rate | GITA rate |
|---|---|---|---|
| tier1b | 0.34 | 0.14 | 1.0 |
| standalone2026 | 0.34 | 0.14 | 0.60 |
| aca2027 | 0.60 | 0.40 in Year 2 only, then 0 | 0.0 |

The GITA cap factor is 0.70 of SI after CA. The horizon is 5 years.

**Formula (faithful to the JS)**

```
caRateYr1 = 0.34; caRateYr2Plus = 0.14; gitaRate = 0
if cat == 'tier1b':         caRateYr1 = 0.34; gitaRate = 1.0
if cat == 'standalone2026': caRateYr1 = 0.34; gitaRate = 0.60
if cat == 'aca2027':        caRateYr1 = 0.60; caRateYr2Plus = 0.40; gitaRate = 0.0
# (caRateYr2Plus is assigned but never read below)

# Year-1 output cards
yr1CA          = QCE * caRateYr1
adjSIYr1       = max(0, SI - yr1CA)
totalGitaPool  = QCE * gitaRate
maxGitaCapYr1  = adjSIYr1 * 0.70
gitaUsedYr1    = min(totalGitaPool, maxGitaCapYr1)
carryForward   = max(0, totalGitaPool - gitaUsedYr1)
display "RM " + round(value) with thousands separators for yr1CA, gitaUsedYr1, carryForward

# 5-year cumulative cash saving series
pool = totalGitaPool; running = 0
for i in 0..4:
    if i == 0:                          caDeduction = yr1CA
    elif cat == 'aca2027' and i == 1:   caDeduction = QCE * 0.40
    elif i < 6 and cat != 'aca2027':    caDeduction = QCE * 0.14
    else:                               caDeduction = 0      # ACA years 3-5
    yearAdjSI   = max(0, SI - caDeduction)        # CA deducted first
    yearGitaCap = yearAdjSI * 0.70                # 70% statutory-income cap
    yearGitaUsed = min(pool, yearGitaCap)
    pool -= yearGitaUsed                          # remainder carried forward
    taxable  = yearAdjSI - yearGitaUsed
    taxPaid  = taxable * taxRate
    baseline = SI * taxRate                       # tax with no incentives
    saved    = max(0, baseline - taxPaid)
    running += saved
    series.append(round(running))
chart labels = ['Year 1'..'Year 5'], data = series
```

How the pieces interact: each year, CA (34% in Year 1, then 14% a year; ACA 60% then 40%) is deducted from SI first. GITA can then absorb at most 70% of what remains. Any GITA above that cap stays in the pool and carries into later years without limit. Annual cash saving is the tax with no incentives minus the tax after CA and GITA.

**Outputs:** the three Year-1 cards (Year 1 Schedule 3 CA, Year 1 GITA Utilized, Carry-Forward GITA) and the Chart 2 series. The cards' sub-captions are static: "20% IA + 14% AA (34%)", "Capped at 70% Statutory Inc", "Indefinite carry-forward".

**Outputs at default inputs (computed by running the code logic):** QCE RM 2,000,000 and SI RM 1,500,000.

| Category | Tax rate | Year-1 CA | Year-1 GITA used | Carry-forward GITA | Cumulative Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|---|---|---|---|
| tier1b | 24% | RM 680,000 | RM 574,000 | RM 1,426,000 | 300,960 | 573,120 | 777,600 | 844,800 | 912,000 |
| tier1b | 15% | RM 680,000 | RM 574,000 | RM 1,426,000 | 188,100 | 358,200 | 486,000 | 528,000 | 570,000 |
| standalone2026 | 24% | RM 680,000 | RM 574,000 | RM 626,000 | 300,960 | 518,400 | 585,600 | 652,800 | 720,000 |
| standalone2026 | 15% | RM 680,000 | RM 574,000 | RM 626,000 | 188,100 | 324,000 | 366,000 | 408,000 | 450,000 |
| aca2027 | 24% | RM 1,200,000 | RM 0 | RM 0 | 288,000 | 480,000 | 480,000 | 480,000 | 480,000 |
| aca2027 | 15% | RM 1,200,000 | RM 0 | RM 0 | 180,000 | 300,000 | 300,000 | 300,000 | 300,000 |

Year-by-year trace for tier1b at 24% (the default):

| Year | CA deduction | SI after CA | GITA cap (70%) | GITA used | GITA pool left | Taxable | Tax paid | Baseline tax | Cash saved | Cumulative |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 680,000 | 820,000 | 574,000 | 574,000 | 1,426,000 | 246,000 | 59,040 | 360,000 | 300,960 | 300,960 |
| 2 | 280,000 | 1,220,000 | 854,000 | 854,000 | 572,000 | 366,000 | 87,840 | 360,000 | 272,160 | 573,120 |
| 3 | 280,000 | 1,220,000 | 854,000 | 572,000 | 0 | 648,000 | 155,520 | 360,000 | 204,480 | 777,600 |
| 4 | 280,000 | 1,220,000 | 854,000 | 0 | 0 | 1,220,000 | 292,800 | 360,000 | 67,200 | 844,800 |
| 5 | 280,000 | 1,220,000 | 854,000 | 0 | 0 | 1,220,000 | 292,800 | 360,000 | 67,200 | 912,000 |

At 15%, tier1b uses GITA on the same schedule, and annual savings are 188,100; 170,100; 127,800; 42,000; 42,000. Standalone2026 at 24% uses GITA of 574,000 in Year 1 and 626,000 in Year 2 (pool exhausted), with annual savings of 300,960; 217,440; 67,200; 67,200; 67,200. At 15% the standalone2026 savings are 188,100; 135,900; 42,000; 42,000; 42,000. ACA at 24% deducts CA of 1,200,000 then 800,000, then 0, with annual savings of 288,000; 192,000; 0; 0; 0. At 15% the ACA savings are 180,000; 120,000; 0; 0; 0.

### B. Cutoff readiness audit checklist (`runAuditCheck()`)

**Location:** Tab 3, "Interactive Cutoff Readiness Audit Checklist". Four checkboxes, all unchecked by default; the check runs on each checkbox change.

- `chkInvoice`: 1. Purchase Invoice Issued & Deposit Paid
- `chkCommissioned`: 2. Physical Installation & Commissioning (COD)
- `chkSubmitted`: 3. Application Received by MGTC / MIDA
- `chkIntegrated`: 4. BESS Integration Status

Initial result box text, before any change: "Status: Pending selection above..."

**Branches, evaluated in order**

| # | Condition | Output text (exact) |
|---|---|---|
| 1 | chkInvoice AND chkCommissioned AND chkSubmitted (chkIntegrated ignored) | "STATUS: QUALIFIED FOR PRE-2027 REGIME" / "All three critical milestone events (Incurred QCE, Physical COD, Application Received) are satisfied on/before 31 Dec 2026. Eligible for 60% Standalone GITA / 70% GITE Leasing." |
| 2 | NOT chkSubmitted AND chkIntegrated (invoice and COD ignored) | "STATUS: QUALIFIED FOR 2027–2030 TIER 1b REGIME" / "Project will be verified on/after 1 Jan 2027. Because BESS is integrated, project qualifies for 100% GITA Asset allowance under Tier 1b." |
| 3 | NOT chkSubmitted AND NOT chkIntegrated (invoice and COD ignored) | "STATUS: DISQUALIFIED / 0% GITA RISK" / "Application will be received on/after 1 Jan 2027, but system lacks BESS integration. Standalone solar receives 0% GITA post-2026. Action Required: Integrate BESS or execute before 31 Dec 2026." |
| 4 | Otherwise (chkSubmitted checked but chkInvoice or chkCommissioned unchecked) | "Status: Evaluating milestones... Ensure all required boxes are checked for accurate audit diagnosis." |

### C. Matrix filter (`filterMatrixTable()` / `renderMatrixTable(filter)`)

- Location: Tab 2, "Filter Category" select (`matrixFilter`), default `all`.
- Options: `all` = "All Green Asset Categories" (11 rows); `asset` = "GITA Assets (Own Consumption - MGTC)" (6 rows); `project` = "GITA Projects (Business Purpose - MIDA)" (4 rows); `leasing` = "GITE Leasing (RPVI / PPA - SEDA/MIDA)" (1 row).
- Logic: if filter is `all`, show every row of `matrixData`; otherwise show rows where `cat == filter`. Each row shows title, current, budget2027 (as a coloured badge), cap, then agency with the ref in brackets underneath.
- The table is rendered with the `all` filter on page load.

### D. Tab switching (`switchTab(tabId)`)

This hides all sections and shows the selected one. Opening the overview tab resizes Chart 1. Opening the mechanics tab re-runs `calculateTaxBenefits()` and resizes Chart 2.

## Embedded data tables

### `matrixData` (JS array, 11 rows; `badge` styling field omitted)

| # | cat | title | current | budget2027 | cap | agency | ref |
|---|---|---|---|---|---|---|---|
| 1 | asset | Standalone Solar PV (Own Use) | 60% GITA (Tier 2) | 0% (Discontinued) | 70% SI | MGTC / LHDN | App 25, Lampiran 25 |
| 2 | asset | Standalone BESS (Own Use) | 100% GITA (Tier 1) | 0% Standalone (Must integrate) | 70% SI | MGTC / LHDN | App 25, Lampiran 25 |
| 3 | asset | Integrated Solar PV + BESS/ESS (Own Use) | Split 60% / 100% | 100% GITA (Tier 1b) | 70% SI | MGTC / LHDN | App 25, Lampiran 25 |
| 4 | asset | Energy Efficiency Assets (Chillers/Boilers) | 60% GITA (Tier 2) | 0% (Shifted to ACA App 28) | 70% SI | MGTC / LHDN | App 25, Lampiran 25 |
| 5 | asset | Locally Produced EV Chargers / Waste / Water | 100% / 60% GITA | 100% GITA (Tier 1a) | 70% SI | MGTC / LHDN | App 25, Lampiran 25 |
| 6 | asset | Imported EV Chargers / Waste / Water | 60% GITA | 60% GITA (Tier 2a) | 70% SI | MGTC / LHDN | App 25, Lampiran 25 |
| 7 | project | Commercial Solar PV Project | 100% GITA 5 yrs (Tier 3) | 0% (Tier 3 Abolished) | 70% SI | MIDA | App 25, MIDA |
| 8 | project | Non-Solar RE Projects (Biomass/Hydro) | 100% GITA 5 yrs (Tier 3) | 60% GITA 5 yrs (Tier 2b) | 70% SI | MIDA | App 25, MIDA |
| 9 | project | Commercial EV Charging Stations | 100% GITA (100% SI) | 60% GITA (70% SI) | 70% SI | MIDA | App 25, MIDA |
| 10 | project | Green Hydrogen & OTEC Projects | 100% GITA (Green H2) | 100% GITA 5+5 yrs (Tier 1) | 100% / 70% SI | MIDA | App 25, MIDA |
| 11 | leasing | GITE Solar Leasing (RPVI / PPA) | 70% Income Exemption | EXPIRED (0% Post-2026) | 70% SI | SEDA / MIDA | App 25, P.U.(A) 247 |

### Chart 1 dataset (JS)

- labels: ['Standalone Solar', 'Standalone BESS', 'Integrated Solar+BESS', 'EE Assets', 'EV Chargers (Local)']
- 'Current (2024–2026)': [60, 100, 60, 60, 100]
- 'Budget 2027 (2027–2030)': [0, 0, 100, 0, 100]

## Links and cited documents

The report contains no hyperlinks. Documents are cited by name or file name only. The only external URLs are the page's script libraries (cdn.tailwindcss.com, cdn.jsdelivr.net/npm/chart.js).

| Label as shown | URL or document ID | Where used |
|---|---|---|
| Budget 2027 speech, "official Ministry of Finance (MOF) portal" | bs27.pdf (no URL) | Tab 1 executive summary |
| MOF Speech (9 Oct 2026) | (no URL) | Footer |
| Appendix 25: Review of Green Technology Tax Incentive / MOF Appendix 25 / App 25 | tax-measures.pdf (no URL) | Tab 1 summary and chart caption; Tab 2 matrix (all rows' ref); Tab 3 intro; Tab 4 intro; footer |
| Lampiran 25 | (no URL) | Tab 2 subtitle; matrix ref for all asset rows |
| tax-measures.pdf, Table of Contents | tax-measures.pdf | Tab 7, unconfirmed item 5 |
| Appendix 28 (Extended ACA) | (within Budget 2027 tax measures; no URL) | Tab 1 takeaway 3; Tab 2 matrix row 4 ("ACA App 28"); Tab 6 ACA card |
| Appendix 12 (SVA write-off) | (no URL) | Tab 6 SVA card |
| Appendix 15 (Sukuk PRISMA issuance-cost deduction) | (no URL) | Tab 6 grid/Sukuk card; Tab 7 unconfirmed item 5 |
| Budget Speech Para 112 | (no URL) | Tab 6 grid/Sukuk card tag |
| Touchpoints Page 14 | (no URL; document not otherwise identified) | Tab 6 Green Sustainability Fund 2.0 card tag |
| MIDA Belanjawan 2027 Release (12 Oct 2026) | (no URL) | Tab 1 chart caption |
| MIDA Briefing Deck (12 Oct 2026) | (no URL) | Footer |
| MIDA 2024 Guidelines | (no URL) | Tab 4 RPVI prerequisites |
| MIDA (matrix ref) | (no URL) | Tab 2 matrix project rows |
| MGTC Guideline REC-GTGT-007, Sec 3(d) | (no URL) | Tab 3 Step 2 (applications only after full commissioning) |
| MGTC Guideline, Section 7 | (no URL) | Tab 3 Step 3 ("applications received by MGTC from 1 Jan 2024 until 31 Dec 2026") |
| MGTC Guidelines (general); MGTC's 2027–2030 Guidelines (pending) | (no URL) | Tab 3 intro; footer; Tab 7 item 3 |
| MGTC formal Validation Letter | (document type) | Tab 7 compliance rules |
| LHDN Public Ruling 4/2023 / LHDN PR 4/2023 | (no URL) | Tab 3 Step 1; Tab 7 hire-purchase rule; footer |
| LHDN Public Rulings (general) | (no URL) | Tab 3 intro |
| LHDN Joint Memorandum response ("Draf GITA Asset sedang dimuktamadkan") | (no URL, no date) | Tab 7 unconfirmed item 1 |
| ITA Schedule 3 / Schedule 3 Capital Allowances | (no URL) | Tab 3 Step 1; Tab 4 host-owned model; Tab 5 mechanics |
| P.U. (A) 243/2024 | (no URL) | Tab 5 mechanics; Tab 7 item 1 (covers GITA Assets up to 31 Dec 2023); footer |
| P.U. (A) 243/2024 Para 6(1) | (no URL) | Tab 5: CA deducted first, legally mandatory |
| P.U. (A) 243/2024 Para 6(4) | (no URL) | Tab 5: indefinite carry-forward of unutilised GITA |
| P.U. (A) 243/2024 Para 7 | (no URL) | Tab 7: 5-year holding period, full clawback |
| P.U. (A) 247/2024 | (no URL) | Tab 4 intro (GITE 70% for 5 to 10 years); matrix row 11 ref "P.U.(A) 247"; footer |
| P.U. (A) 247/2024 Para 5(3) | (no URL) | Tab 4 RPVI prerequisites |
| SEDA verification letter | (document type) | Tab 4 Min 3MW COD threshold |
| Draft Gazette Order for 2024–2026 and 2027–2030 GITA Asset framework / official Exemption Orders (MOF, AGC, LHDN, MGTC) | (not yet gazetted per report) | Tab 7 intro and item 1 |
| MyHIJAU (local mark products) | (no URL) | Tab 7 item 4 |
| Budget 2026 Proposal for 100% GITA on General MyHIJAU Products | (no URL) | Tab 7 item 4 |

## Extraction notes

1. **Integrated RE + BESS: current rate stated three different ways.** The KPI card says Tier 1b is "Upgraded from 60% split". The matrix row 3 gives the current regime as "Split 60% / 100%". Chart 1 plots the integrated system's Current value as 60. The report's own matrix row 2 and Chart 1 give standalone BESS a current rate of 100% (Tier 1). By the report's own figures, then, only the solar portion of an integrated system is upgraded (60% to 100%); the BESS portion was already at 100%. The chart's single "60" understates the current regime for an integrated system.

2. **Standalone BESS shown as 0% from 2027.** Matrix row 2 ("0% Standalone (Must integrate)") and Chart 1 (0) are the only places that say this. The four KPI cards do not mention standalone BESS. The executive summary lists the withdrawn categories as "standalone behind-the-meter solar, standalone energy efficiency equipment, and third-party solar leasing providers", which leaves out standalone BESS. No statutory wording is quoted for the BESS change. Other reports in the folder disagree:
   - `malaysia_c_i_bess_solutions_dashboard.html` shows Standalone BESS as "Tier 1: 100% GITA" in both its 2024–2026 and Budget 2027 (2027–2030) columns.
   - `malaysia_tnb_maximum_demand_c_i_mitigation_portal.html` says "BESS and integrated solar storage maintain Tier 1 status through 2030".
   - `malaysia_c_i_solar_bess_financing_2026.html` gives 2027–2030 rules only for standalone solar (0%) and integrated solar + BESS (100%).

   R7 is the only report that removes GITA from standalone BESS. This is a material conflict for a BESS-for-MD-reduction business and needs checking against the actual Appendix 25 / Lampiran 25 text.

3. **The 48.0% "Combined Shield Formula" does not match the engine's own 5-year output.**
   - The note says 200% × 24% = 48.0% of capex, which is RM 960,000 at the default QCE.
   - The engine's 5-year cumulative at defaults is RM 912,000, or 45.6% of QCE.
   - GITA is fully used by Year 3 (574,000 + 854,000 + 572,000 = 2,000,000), but CA reaches only 34% + 4 × 14% = 90% of QCE in 5 years. The missing 10% of CA (RM 200,000 × 24% = RM 48,000) accounts for the whole gap.
   - At 15%, the 5-year total is RM 570,000 (28.5%), against 30.0% on the formula.
   - Standalone 60% GITA gives RM 720,000 (36.0%) at 24%, against 160% × 24% = 38.4% on the formula, and RM 450,000 (22.5%) at 15%.
   - ACA gives RM 480,000 (24%) and RM 300,000 (15%).
   - The 48.0% figure is a lifetime, undiscounted total that assumes full absorption. The note box is static text and does not update with the inputs.

4. **Engine logic issues.**
   - The 70% cap is applied to SI after CA, not to SI. This is consistent with "CA first" (Para 6(1)), but the KPI wording ("Offsets up to 70% Statutory Income") and the card caption ("Capped at 70% Statutory Inc") do not say so.
   - Unabsorbed CA is not carried forward. If CA is greater than SI, the excess is simply lost (`max(0, SI − CA)`). Only GITA carries forward. This does not trigger at the defaults.
   - The horizon is 5 years, so the Schedule 3 CA residual (10%) is never shown.
   - The condition `i < 6` is always true, and `caRateYr2Plus` is assigned but never used; the rates are hard-coded instead.
   - The "Year 1 Schedule 3 CA" caption "20% IA + 14% AA (34%)" stays fixed even when ACA (60%) is selected.
   - The selected tax rate (including "15% MSME Preferential Rate") is applied flat to all SI. The report gives no income band for the MSME rate.
   - Savings are undiscounted. The engine models neither the 5-year holding-period clawback, nor the Validation Letter timing, nor hire-purchase progressive QCE.
   - Tier 1b and standalone2026 give identical Year-1 outputs at defaults, because the 70% cap binds in Year 1.
   - The ACA split (60% then 40%) matches the Appendix 28 card ("20% Initial Allowance + 40% Annual Allowance").

5. **The deadline tab and the GITE prerequisites do not line up.**
   - Tab 3 and the audit checklist treat pre-2027 GITE leasing as secured once the supplier invoice, COD and MGTC/MIDA receipt all fall by 31 Dec 2026. The checklist's pre-2027 result explicitly says "Eligible for 60% Standalone GITA / 70% GITE Leasing".
   - Tab 4 adds conditions for RPVIs that the checklist never checks: minimum 3MW aggregated COD with a SEDA verification letter; MIDA receipt *before* the first sales/energy invoice to the off-taker; at least 60% Malaysian equity; 5 full-time employees (2 competent green personnel); 1 entity per corporate group.
   - The two "invoice" rules are different invoices: the supplier purchase invoice (Step 1) and the first sales invoice to the off-taker (GITE).
   - The Tab 4 PPA-model bullet says "5 full-time local staff", while the prerequisites card says "5 full-time employees (2 competent green personnel)".

6. **The report does not settle what fixes the regime date.** Four different triggers appear:
   - "installing ... on or after 1 January 2027" (Tab 1 takeaway 1)
   - supplier invoice date, COD and "MGTC Application Receipt" (Tab 3)
   - "MGTC verification date strictly governs eligibility" (Tab 7 item 2)
   - "Project will be verified on/after 1 Jan 2027" (audit branch 2)

   Tab 3 Step 1 also mixes two tests: invoice date defines timing, yet capex is "legally incurred when capable of business use". The 24-month MGTC submission window (KPI card) has no citation, and the report does not explain how it interacts with the 31 Dec 2026 receipt cutoff. Tab 3 refers to "six major green incentive categories" with a 31 Dec 2026 cutoff but never lists the six.

7. **Audit checklist logic issues.**
   - Branch 1 ignores the BESS box, so an integrated system that meets all three milestones is labelled "60% Standalone GITA", although the matrix gives the current integrated regime as "Split 60% / 100%".
   - Branches 2 and 3 ignore the invoice and COD boxes.
   - Unticking every box after any interaction gives "DISQUALIFIED / 0% GITA RISK" rather than pending.
   - Ticking "submitted" without invoice or COD returns only the generic "Evaluating" text, even though Step 2 says applications can be filed only after commissioning.
   - The checklist is solar-centric (checkbox 2 says "Solar PV or EE system") and has no path for standalone BESS or EE under ACA.
   - Checkbox 3 contains a duplicated word ("Formal GITA GITA/A application").

8. **"Enacted" conflicts with the report's own gazettement caveat.** The header badge says "Budget 2027 Enacted" and the matrix column heading is "Enacted Budget 2027 Regime". Yet unconfirmed item 1 says the 2024–2026 and 2027–2030 GITA Asset gazette orders are still being drafted ("Draf GITA Asset sedang dimuktamadkan"). The item also says P.U. (A) 243/2024 covers GITA Assets only up to 31 Dec 2023. Even so, the mechanics in Tab 5 (Para 6(1), Para 6(4)) and the holding-period rule in Tab 7 (Para 7) are cited to P.U. (A) 243/2024 as if they govern 2024–2030 claims.

9. **Tier labels and matrix columns are inconsistent.**
   - Non-solar RE projects are "Tier 2b" in the matrix but "GITA Project Tier 2" in the breakdown card. "Tier 2b" is also used for the GITA Asset standalone-RE tier.
   - The current non-solar RE project rate is labelled "Tier 3", the same tier as commercial solar projects.
   - Standalone non-solar RE *assets* (Tier 2b, 60%) have no matrix row.
   - The "SI Set-Off Cap" column shows the 2027 cap (70% SI) even on rows whose current regime says "100% SI" (EV charging). It also gives "70% SI" for GITE, which the report elsewhere calls an income exemption, not a set-off.
   - Locally produced EV chargers are plotted at 100 for the current regime, while the matrix gives "100% / 60% GITA".
   - The current Green H2 row says "(Green H2)" only, while the 2027 row adds OTEC.

10. **The EE-to-ACA substitution is not reconciled.** The matrix and takeaway 3 say EE assets (chillers, boilers, LED) shift to ACA under Appendix 28. The ACA card, however, lists only "plant and machinery from local manufacturers" and "ICT equipment, custom software, and AI Energy Management Systems (EMS/BMS)". The report does not say whether imported EE equipment qualifies. The engine's "2027 EE Equipment (100% ACA)" option assumes it does.

11. **Sourcing is weak.**
    - There are no URLs anywhere. Documents are named only (bs27.pdf, tax-measures.pdf).
    - Only two statutory phrases are quoted verbatim: the MGTC Section 7 phrase and "Draf GITA Asset sedang dimuktamadkan". "keluaran tempatan" is a label, not a quoted clause.
    - The footer cites "MIDA Briefing Deck (12 Oct 2026)", while the chart cites "MIDA Belanjawan 2027 Release (12 Oct 2026)". These may be the same document.
    - "Touchpoints Page 14" is never identified as a document.
    - The "LHDN Joint Memorandum response" is undated.
    - These numbers carry only an appendix or paragraph tag, or no source at all: the 24-month MGTC window; GITE "5 to 10 years"; GSF 2.0 (RM2 Billion, 1% p.a. for 5 years, tenure up to 10 years); TNB RM15 Billion; KWAP Dana Iklim RM1 Billion; the SVA thresholds; the RPVI criteria.
    - The GITE KPI says "EXPIRED", but on the report's as-of date (Oct 2026) the cutoff (31 Dec 2026) had not yet passed.
    - Tab 6's fourth "instrument" (grid investment and Sukuk PRISMA) is not an EE or demand-reduction incentive for C&I users.

12. **Coverage check.** The coverage checker's only remaining "missing" values are Tailwind colour-shade numbers in class names (50, 400, 500, 600, 800). These are styling and were left out on purpose.

### Prompt coverage (research/round2_research_prompts.md prompt #1)

1. **GITA Asset rates (a) standalone solar, (b) standalone BESS, (c) integrated; extension; new conditions.** Answered (sections 1, 2; Chart 1; matrix).
   - (a) 60% (Tier 2) through 2026, 0% from 1 Jan 2027.
   - (b) 100% (Tier 1), then "0% Standalone (Must integrate)". This appears in the matrix and chart only and conflicts with other reports (Note 2).
   - (c) 100% Tier 1b for 2027–2030; the current rate is shown as 60% or "Split 60% / 100%" (Note 1).
   - The extension runs to 31 December 2030.
   - New conditions: BESS integration is mandatory for solar, 70% SI set-off, and a Tier 1a local-production distinction. The minimum BESS sizing ratio and the retrofit eligibility rule are unconfirmed (section 7 item 3).
   - No exact Appendix 25 wording, links or dates are given.
2. **31 Dec 2026 deadline and what must happen by then.** Answered (section 3; audit checklist). The supplier invoice / QCE incurred, full commissioning and MGTC receipt must all be on or before 31 Dec 2026, citing MGTC REC-GTGT-007 Sec 3(d) and Section 7 and LHDN PR 4/2023. There is also a 24-month post-invoice window. Transitional treatment is unconfirmed (section 7 item 2). The report is inconsistent on which date governs (Note 6).
3. **GITE for solar leasing.** Answered (sections 1, 2, 4). The 70% exemption for RPVIs (P.U. (A) 247/2024, 5 to 10 years) is not extended and expires 31 Dec 2026. Lock-in prerequisites are given (P.U. (A) 247/2024 Para 5(3), MIDA 2024 Guidelines).
4. **How GITA is used.** Answered (section 5; engine). CA is deducted first (P.U. (A) 243/2024 Para 6(1)), GITA is capped at 70% of SI per YA, unused GITA carries forward indefinitely (Para 6(4)), and the stated combined deduction is "200%". There is a 5-year holding clawback (Para 7) and a hire-purchase basis (PR 4/2023). Caveat: the report itself says P.U. (A) 243/2024 covers GITA Assets only up to 31 Dec 2023 (Note 8). The engine's lifetime figure differs from the formula (Note 3).
5. **New Budget 2027 incentives for BESS, EE or demand reduction.** Partly answered (section 6).
   - EE: extended ACA (Appendix 28) and the SVA increase (Appendix 12).
   - Finance: Green Sustainability Fund 2.0.
   - Grid and Sukuk: TNB RM15 Billion, Appendix 15 Sukuk PRISMA, KWAP Dana Iklim.
   - The only BESS-specific incentive is the Tier 1b integration rule, and there is no specific demand-reduction incentive beyond the statement that BESS shaves MD charges.
   - The Appendix 15 body text is unverified (section 7 item 5).
6. **Sourcing requirement (official or Big-4 sources, exact wording, link and date for every claim, mark anything unconfirmed).** Partly met. Official documents are named, but there are no links, few dates and few verbatim quotes. Five unconfirmed items are clearly marked (Note 11).



<!-- ===== FILE: kb/sources/R8_market_benchmark_2026.md ===== -->
# FILE: kb/sources/R8_market_benchmark_2026.md

---
id: R8
title: "Malaysia C&I Solar & BESS Market Benchmark (2026)"
source_file: malaysia_c_i_solar_bess_market_2026.html
source_modified: 2026-10-23 15:07
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js)
research_prompt: "#3 Competitors and pricing (research/round2_research_prompts.md)"
stated_scope: "Header: 'Malaysia C&I Solar & BESS Market' / '2026 Pricing Benchmarks, Competitors & Zero-Capex Economics'. Hero badge: 'Market Intelligence Report 2026'; hero title: 'Malaysia Commercial & Industrial Solar & BESS Benchmarks'. Footer: 'Designed for C&I Energy Buyers, Financiers & Developers.'"
stated_sources: "Synthesized from Bursa Malaysia filings, institutional equity research, SEDA & TNB RP4 guidelines."
as_of: "No explicit as-of date. Title says 2026. National capacity figure is 'End-2025'; cost pressure 'H1 2026'; latest dated items Aug 2026 (Solarvest order book 'Aug 2026'; Ditrolic SJREC approval 'Aug 2026'). RP4 tariff schedule '1 July 2025 – 31 Dec 2027'. GITA / GTFS sunset '31 Dec 2026'."
sections: ["Header & Navigation", "Executive Summary Dashboard (Overview)", "Section 1: Turnkey Pricing Benchmarks & Financial Feasibility Calculator", "Section 2: Top 15 C&I Solar & BESS Companies & Developers (2026 Matrix)", "Section 3: RP4 Tariff Catalyst & Zero-Capex Shared-Savings Mechanisms", "Section 4: EPCC Profit Margins, Payment Milestones & Competition Heatmap", "Footer", "Competitor Detail Modal"]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R8 — Malaysia C&I Solar & BESS Market Benchmark (2026)

> Faithful, complete markdown extract of `malaysia_c_i_solar_bess_market_2026.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- National solar capacity **5,777 MW** at end-2025, with **2.5 GW added in 2025** (Overview; Section 2).
- TNB RP4 (schedule **1 July 2025 – 31 Dec 2027**) raised commercial Maximum Demand charges by **162%**, "from RM 30.30/kW to RM 89.27–RM 97.06/kW/month" for Capacity + Network charges; card says "Up to RM 97.06/kW/mo" (Overview; Section 3; Chart 3).
- **31 Dec 2026** is presented as the "GITA / GTFS Sunset" and "60-100% Tax Allowance Deadline" (Overview; Section 1; calculator).
- EPCC order book flow of **RM 13B–23B** from LSS5, LSS6 & CRESS tenders (Overview).
- C&I rooftop solar turnkey EPCC spans **RM 1.85 to RM 3.80/Wp**: 100 kWp RM 2.40–3.80; 500 kWp RM 2.40–2.60; 1 MWp RM 2.00–2.50; 3 MWp RM 1.85–2.20/Wp (Section 1 table).
- C&I BESS: **RM 1,150–1,450/kWh** for 200–500 kWh cabinets and **RM 1,000–1,350/kWh** for 2–5 MWh containers (Section 1).
- O&M: rooftop solar 1.0–1.5%/yr (RM 25–45/kWp/yr); BESS preventive 1.5–2.5%/yr (RM 15–35/kWh/yr); BESS full wrap 3.5–4.5%/yr (RM 45–60/kWh/yr) (Section 1 table).
- H1 2026 cost pressure: China's 9% VAT rebate removal, silver +167%, copper +40% (Section 1).
- Top 15 matrix led by Solarvest (~3,700 MWp; record RM 2.37B unbilled order book, Aug 2026), Gentari (~9,100 MW global RE), Ditrolic (1,000+ MW constructed) (Section 2; Embedded data).
- Plus Xnergy 15/85 zero-capex benchmark: developer bills **RM 82.50/kW** vs TNB **RM 97.06/kW**; client keeps 15.0% (~RM 14.56/kW; ~RM 21,520/month on 1,478 kW shaved); financier return 12%–18% p.a. (~4-year payback) (Section 3).
- 8 zero-capex / shared-savings BESS providers with contract terms from 7 to 25 years (Section 3 cards).
- Margin hierarchy: direct C&I rooftop turnkey **25%–35% GP**; utility main contracting **15%–22%**; installation subcontracts **6.5%–10.8%**; HV grid engineering **~50%** (Section 4; Chart 4).
- Payment milestones: 10–20% LOA & survey; 40–50% equipment delivery; 20–25% installation; 5–10% COD; 5% retention for 12-month DLP (Section 4).
- Worst price competition: Tier-2 utility BoP subcontracting, small C&I rooftops 50–300 kWp (low-ball RM 2.40/Wp), standard BESS hardware distribution (Section 4).
- Calculator at defaults (500 kWp + 200 kWh, 100% GITA + CA) computes RM 1,520,000 gross, RM 516,800 tax shield, RM 344,624/yr savings, 2.9-year payback; the static placeholders show different numbers (Calculators section).

## 1. Header & Navigation

- Page `<title>`: "Malaysia C&I Solar & BESS Market Benchmark (2026)".
- Sticky header title: "Malaysia C&I Solar & BESS Market"; subtitle: "2026 Pricing Benchmarks, Competitors & Zero-Capex Economics".
- Navigation buttons (scroll to section): "Overview" (overview), "Pricing & ROI Calculator" (pricing), "Top 15 Competitors" (competitors), "Zero-Capex & RP4" (zerocapex), "Margins & Milestones" (margins).

### Design comments in the HTML source (not visible on the page)

- Palette comment: "Chosen Palette: Warm Cleantech Neutral" (styling only).
- "Application Structure Plan" comment — describes the intended page layout:
  1. Sticky Header & Navigation: quick-jump tabs for Executive Overview, Interactive ROI & Pricing Calculator, Top 15 Competitor Matrix, Zero-Capex & RP4 Tariff Analysis, and EPCC Margins & Risk Flow.
  2. Executive Summary Dashboard: 4 key metric cards highlighting 5,777 MW cumulative capacity, RP4 162% MD surge, 31 Dec 2026 GITA sunset, and RM 13B-23B tender replenishment.
  3. Interactive Section 1 - Pricing Benchmarks & ROI Simulator: dynamic project estimator to pick solar tier, BESS sizing and tax scenarios ("GITA 100% vs pre-tax") to simulate Gross CAPEX, Tax Shield, Annual Savings and Simple Payback; paired with Chart.js visualisation of solar EPCC rates and BESS turnkey costs.
  4. Interactive Section 2 - Top 15 Market Competitor Explorer: filterable/searchable matrix across listed and private developers, with modal detail popup on completed BESS projects, business models and EMS software moats.
  5. Interactive Section 3 - RP4 Tariff & Zero-Capex BESS Mechanisms: comparative breakdown of TNB RP4 capacity + network charges vs legacy demand charges; "Interactive comparison tool mapping terms, savings splits (15/85), and performance guarantees across 8 leading Zero-Capex providers."
  6. Interactive Section 4 - EPCC Margins & Payment Flow: Chart.js chart comparing Gross Margin vs Core Net Margin across market tiers (Turnkey C&I vs Utility EPC vs Subcontracting vs High-Voltage Grid); "Interactive milestone timeline illustrating working capital risk and 5% retention sum locks."
  - Why this structure: lets commercial end-users, developers and investors move between pricing benchmarks, competitive intelligence and financial feasibility modelling.
- "Visualization & Content Choices" comment — states the purpose of each visual:
  - Solar EPCC Pricing: compare across tiers; Chart.js bar chart (Pre-GITA vs Post-GITA Net CAPEX); interaction "Capacity tier toggle"; justification: illustrates economies of scale from 100 kWp to 3 MWp.
  - Turnkey BESS Rates: show range & tax impact; Chart.js grouped bar chart; hover tooltips; displays hardware vs net post-GITA effective cost (RM/kWh).
  - RP4 Tariff Demand Impact: demonstrate cost surge; bar chart comparing Legacy vs RP4 charges; "Quantifies the 162% surge in peak demand penalties."
  - Competitor Matrix: organise & filter; dynamic HTML table + search/filter JS; category filter & click for detail modal; compares 15 players across cumulative MW, BESS projects and EMS tools.
  - EPCC Margin Stratification: display profit hierarchy; Chart.js horizontal bar chart; "Visually separates direct C&I turnkey margins (25-35%) from thin BoP subcontracting (6.5-10.8%)."
  - "CONFIRMATION: NO SVG graphics used. NO Mermaid JS used." (also repeated as a separate comment).
- Other comments are placeholders only ("Populated by JavaScript", "Content inserted by JS").

## 2. Executive Summary Dashboard (Overview)

- Badge: "Market Intelligence Report 2026".
- Title: "Malaysia Commercial & Industrial Solar & BESS Benchmarks".
- Lead text (verbatim): "Driven by Tenaga Nasional Berhad’s (TNB) Regulatory Period 4 (RP4) unbundled tariffs, mandatory SELCO battery storage guidelines, and the imminent 31 December 2026 sunset of GITA tax allowances, Malaysia's C&I energy landscape has shifted permanently toward combined Solar + Storage deployment and Zero-Capex Peak Demand Shaving."

| Metric card | Value | Sub-text |
|---|---|---|
| National Solar Capacity | 5,777 MW | End-2025 (2.5 GW added in '25) |
| RP4 Peak Demand Charge | +162% | Up to RM 97.06/kW/mo |
| GITA / GTFS Sunset | 31 Dec 2026 | 60-100% Tax Allowance Deadline |
| EPCC Order Book Flow | RM 13B–23B | LSS5, LSS6 & CRESS Tenders |

## 3. Section 1 — Turnkey Pricing Benchmarks & Financial Feasibility Calculator

Lead text (verbatim): "While global module costs declined through 2025, H1 2026 experienced upward pressure due to China's 9% VAT rebate removal and raw material inflation (silver +167%, copper +40%). C&I rooftop solar turnkey EPCC spans RM 1.85 to RM 3.80/Wp depending on scale and structural enhancements, while C&I BESS ranges from RM 1,150 to RM 1,450/kWh for 200–500 kWh cabinets and RM 1,000 to RM 1,350/kWh for 2–5 MWh containerised units. Post-tax costs are substantially lowered by GITA capital allowances until 31 December 2026."

Chart panels (data in Charts section):
- "Solar EPCC CAPEX per Tier (Gross vs. Net Effective after GITA)" — caption: "Reflects 2026 turnkey installation benchmarks across 100 kWp to 3 MWp systems."
- "C&I BESS Turnkey Cost per kWh (Gross vs. GITA + CA Net Shield)" — caption: "Includes LFP active liquid-cooled cabinets/containers, PCS, EMS & NFPA 855 fire suppression."

Estimator panel: "Interactive C&I Solar + BESS Project ROI & Tax Shield Estimator" — "Select system capacities and tax parameters below to calculate estimated project CAPEX, GITA corporate tax savings, annual energy & MD savings, and simple payback horizon." (inputs, logic and outputs in Calculators section).

### C&I Solar EPCC Benchmark Table (2026)

| Capacity | Turnkey Unit Rate | Gross CAPEX Range | Payback (Post-GITA) |
|---|---|---|---|
| 100 kWp | RM 2.40 – RM 3.80/Wp | RM 240k – RM 380k | 4.0 – 4.5 Yrs |
| 500 kWp | RM 2.40 – RM 2.60/Wp | RM 1.20M – RM 1.30M | 4.4 Yrs |
| 1 MWp | RM 2.00 – RM 2.50/Wp | RM 2.00M – RM 2.50M | 3.5 – 4.5 Yrs |
| 3 MWp | RM 1.85 – RM 2.20/Wp (Solar) | RM 5.55M – RM 6.60M | 3.5 – 4.5 Yrs |

### Operations & Maintenance (O&M) Rates

| Asset Type | Annual O&M (% CAPEX) | Unit Rate | Scope & Notes |
|---|---|---|---|
| C&I Rooftop Solar | 1.0% – 1.5% / yr | RM 25 – RM 45 / kWp / yr | Cloud monitoring, panel washings, thermal scans |
| C&I BESS (Preventive) | 1.5% – 2.5% / yr | RM 15 – RM 35 / kWh / yr | EMS dashboard, chiller service, fire safety checks |
| C&I BESS (Full Wrap) | 3.5% – 4.5% / yr | RM 45 – RM 60 / kWh / yr | Includes mid-life cell augmentation & performance SLAs |

## 4. Section 2 — Top 15 C&I Solar & BESS Companies & Developers (2026 Matrix)

Lead text (verbatim): "Malaysia's cumulative solar capacity reached 5,777 MW at end-2025. Competition in 2026 is defined by three structural moats: bundling solar with mandatory SELCO BESS hardware, vertical integration into high-voltage switchgear and data-centre earthing (ELP), and deploying proprietary AI-driven EMS dispatch software."

Controls: search box (placeholder "Search company, client, or EMS..."); filter buttons "All (15)", "Listed", "Zero-Capex / EaaS", "Major BESS Track Record" (logic in Calculators section). Clicking a row opens the Competitor Detail Modal.

Table columns: Rank & Company | Listing & Scale | Cumulative Solar MW | Completed & Contracted BESS Projects | Business Models | EMS & Product Suite. The table is generated from the `competitors` array (full records in Embedded data tables). As rendered in the default "All" view:

| Rank & Company (line 1) | Ticker (line 2) | Listing & Scale badge | Cumulative Solar MW | Completed & Contracted BESS Projects (shows bessTrack, CSS-truncated) | Business Models (first 2 + overflow count) | EMS & Product Suite (emsProduct text before first "+") |
|---|---|---|---|---|---|---|
| 1. Solarvest Holdings Bhd | KLSE: SLVEST (0215) | Listed | ~3,700 MWp (3.7 GWp) | Multiple C&I BESS (20%-65% MD cuts); Utility BESS bidder under MyBeST auction | Outright CAPEX, Zero-CAPEX Powervest PPA +2 | AI machine-learning load simulator (truncated) |
| 2. Gentari Sdn Bhd | Private (Wholly PETRONAS) | Private | ~9,100 MW (9.1 GW) Global RE | Malaysia's 1st Solar+BESS EV Charging Hub (Oct 2023); ~1.5 GW Gamuda CRESS BESS | Zero-CAPEX PPA, CRESS Green Power Supply +2 | Integrated C&I energy management & CRESS BESS firming for hyperscale data centres |
| 3. Ditrolic Energy Holdings | Private (IFC & Sukuk Backed) | Private | 1,000+ MW Constructed / 300 MW O&M | C&I behind-the-meter EnerPack BESS; Johor RE Corridor utility BESS with IFC & PDT | Outright EPC (EnerGreen), Zero-CAPEX PPA (EnerLoop) +1 | EnerPack BTM BESS (truncated) |
| 4. Samaiden Group Bhd | KLSE: SAMAIDEN | Listed | 700+ MWp Cumulative | C&I BESS peak-shaving & backup installations (2025–2026); LSS6 BESS awards | Outright EPCC, Zero-CAPEX PPA Framework +2 | Automated BESS Peak-Shaving & MD Threshold Dispatch Controller |
| 5. Sunview Group Bhd | KLSE: SUNVIEW | Listed | ~650–800+ MWp Portfolio | 595 MWac Floating Solar + BESS at Lake Kenyir for TNB Genco; SunBESS projects | Outright EPCC, Solar + Storage CAPEX +1 | SunBESS automated C&I peak-shaving & SELCO (>72 kWp) storage system |
| 6. Plus Xnergy Services | KLSE: BMGREEN (Parent) | Listed | >400+ MWp Solar / 100 MWh BESS | 20 MWh SELCO BESS in Perak (HyperStrong, Jun 2026); 1.45 MWh NaS BESS in Kedah | Outright EPCC, 15-Yr Zero-CAPEX BESS Partnership +1 | AI-Driven BESS EMS & SOURCE smart energy platform (weekday 2–10 PM MD shaving) |
| 7. Cypark Resources Bhd | KLSE: CYPARK | Listed | >400 MWp Operational / Hybrid | 595 MWac Floating Solar + BESS at Lake Kenyir (60% JV lead with Sunview) | IPP Asset Ownership, Turnkey EPCC +1 | Utility & hybrid solar-storage dispatch and grid-firming SCADA |
| 8. Pekat Group Bhd | KLSE: PEKAT (0233) | Listed | ~300–400+ MWp Portfolio | Data centre & factory BESS integrated with EPE MV switchgear & ELP systems | Outright EPCC, Zero-CAPEX PPA / CGPP Asset +1 | Integrated Solar (truncated) |
| 9. GSPARX Sdn Bhd | Private (Wholly TNB) | Private | 224 MW Installed C&I | 76.8–170 kWh BESS at Elmina Ilham; C&I BESS partnership with EVE Energy | Zero-CAPEX SARE PPA (via TNB Bill), Outright EPCC | TNB Smart Grid-integrated BESS peak shaving & automated load management |
| 10. Progressture Solar | Private | Private | ~200–300+ MWp C&I | Turnkey C&I BESS for manufacturing factories, commercial property & data centres | Outright EPCC, Zero-Upfront Solar PPA +1 | End-to-end BESS peak shaving, load shifting & power expansion EMS |
| 11. Founder Group Ltd | NASDAQ: FGL (Reservoir Link) | Listed | ~200+ MWp EPCC | Iron-Flow Long-Duration Energy Storage (LDES) via JV RL ADS Power | Outright EPCC, BoP Subcontracting +1 | AI-powered O&M & Iron-Flow LDES industrial load-shifting platform |
| 12. Northern Solar Holdings | KLSE: NORTHERN (0340) | Listed | ~150+ MWp Cumulative | Contracted RM 20.5M ground-mounted SELCO BESS project (~15–18 MWh) | Outright EPCC (96.7% Rev), Zero-CAPEX PPA +1 | Interval-meter-calibrated BESS Peak Shaving suppressing 30-min TNB MD spikes |
| 13. ERS Energy Sdn Bhd | Private | Private | ~150+ MWp C&I | 500 kWp Solar + 200 kWh BESS at Penang Electronics Plant (35% MD cut) | Direct Purchase (CAPEX), Zero-Upfront PPA (15-25 Yrs) +1 | Solar (truncated) |
| 14. Cenergi SEA Bhd | Private (Khazanah / UEM) | Private | ~100+ MWp Clean Energy | Operational C&I BESS integrated with solar (>1 MWac SELCO) & biogas | Zero-CAPEX BESS, Zero-CAPEX Solar PPA (100% Funded) | Automated background BESS controller for SELCO compliance & MD network shaving |
| 15. XPERTS.NRG (Green Xperts) | Private / KLSE: KAB (Partner) | Private | 50 MW EPCC / 15 MW Owned | Consortium partner with TNB for 1,000 MWh BESS under CRESS | Zero-CAPEX Solar PPA, ESCO Shared Savings +1 | Dedicated MD Shaving BESS dispatch & industrial Energy Management Systems |

### Strategic insight cards (verbatim)

1. **Solar + Storage Convergence** — "Plus Xnergy leads direct industrial BESS with a 100 MWh portfolio (including a 20 MWh SELCO BESS in Perak and a 1.45 MWh NaS system in Kedah), while Northern Solar holds a RM 20.5M SELCO BESS award, and Sunview/Cypark lead the RM 1.96B Lake Kenyir 595 MWac floating solar + BESS JV."
2. **High-Voltage & Data Centre Integration** — "Pekat Group secured RM 47M in data-centre contracts across Port Dickson and Johor by combining solar EPCC with its 60% market share in Earthing & Lightning Protection (ELP) and EPE Switchgear, building an unbilled order book of RM 994M."
3. **Proprietary Algorithmic EMS** — "Top contractors rely on software moats to prevent 30-minute peak-shaving failures: Solarvest utilizes AI machine-learning EPMS, Ditrolic deployed its Net-Zero Energy OS with 15-min interval dispatch, and Plus Xnergy automates weekday peak shaving via SOURCE."

## 5. Section 3 — RP4 Tariff Catalyst & Zero-Capex Shared-Savings Mechanisms

Lead text (verbatim): "TNB’s RP4 tariff schedule (1 July 2025 – 31 Dec 2027) unbundled bills into five lines, unmasking peak demand penalties. Commercial Maximum Demand (MD) charges surged by 162% (from RM 30.30/kW to RM 89.27–RM 97.06/kW/month for Capacity + Network charges). Because a single 30-minute dispatch failure during weekday peak hours (2:00 PM – 10:00 PM) resets the entire month's MD charge, CFOs heavily prefer Zero-Capex, Shared-Savings, and Energy-as-a-Service (EaaS) structures that transfer algorithmic risk to developers."

Chart panel: "TNB Demand Tariff Surge: Legacy vs. RP4 Capacity + Network Charge" — caption: "Unbundled RP4 capacity & network charges now represent 30% to 70% of C&I monthly power bills." (data in Charts section, Chart 3).

### The 15% / 85% Savings Split Benchmark Explained

"Plus Xnergy’s benchmark model illustrates the financial mechanics of Zero-Capex MD shaving:"

- **Client Billing Rate:** The developer bills the host at RM 82.50/kW vs TNB's RM 97.06/kW rate.
- **Immediate Client Net Benefit:** The factory retains a risk-free 15.0% savings (~RM 14.56/kW shaved, yielding ~RM 21,520/month on 1,478 kW shaved).
- **Developer Retained Capital (85%):** The developer retains ~85% of gross utility savings to cover 2-hour LFP battery CAPEX (RM 2,300–RM 2,900/kW), off-peak charging power costs, 10-15 yr liquid-cooling O&M, and mid-life cell augmentation.
- **Financier Returns:** Generates a 12% to 18% p.a. return (~4-year payback) while transferring all 30-min peak shaving risk away from the industrial CFO.

### Comparison of 8 Key Zero-Capex & Shared-Savings BESS Providers

| # | Provider | Contract term (badge) | Model | Description (verbatim) |
|---|---|---|---|---|
| 1 | Plus Xnergy | 15 Years | Discounted MD Tariff (RM 82.50/kW) | Client retains 15% net MD savings. 100% funded CAPEX & O&M with AI-driven EMS discharging Mon–Fri (2–10 PM). |
| 2 | EV Connection (EVC) | 7 – 10 Years | Shared Savings Model | First Zero-Capex BESS programme. 15%–30% net client savings split. Curated via 12-month data logging by Registered Energy Managers. |
| 3 | Solarvest Holdings | 10 – 15 Years | Powervest EaaS Structure | Monthly EaaS fee structured lower than monthly MD savings. AI load simulator + EPMS achieving 20% to 65% MD cuts. |
| 4 | UniBess | 10 Years | Operating Lease + Performance SLAs | Written performance contracts with capped Liquidated Damages (LDs) for availability, Year-10 capacity, and round-trip efficiency. |
| 5 | ERS Energy | 15 – 25 Years | Bundled Hybrid PPA | Fixed PPA rate 25%–40% below TNB tariff. Includes <20ms backup switchover & mid-life inverter replacement at zero cost. |
| 6 | Cenergi SEA | 10 – 20 Years | Zero-Capex SELCO BESS | Khazanah/UEM-backed funding. Fully automated background controller for mandatory SELCO (≥1 MWac) storage compliance. |
| 7 | Kawan Renergy | 10 – 15 Years | BaaS & EaaS Models | Backed by internal project fund. Turnkey transformer, PCS, and BESS integration with automated peak-discharge control. |
| 8 | XPERTS.NRG | 10 – 15 Years | ESCO Shared Savings | ESCO shared-savings split on verified MD reductions after 12 months of interval meter analysis. Partnered on 1,000 MWh CRESS BESS. |

## 6. Section 4 — EPCC Profit Margins, Payment Milestones & Competition Heatmap

Lead text (verbatim): "Financial disclosures reveal a strict three-tier margin hierarchy in Malaysia's EPCC sector. Direct C&I rooftop turnkey solar yields 25% to 35% Gross Profit (GP) Margins, whereas utility-scale (LSS5/CGPP) main contracting compresses GP margins to 15%–22%, and pure installation subcontracts yield thin 6.5%–10.8% GP margins (often resulting in net operating losses). High-voltage grid engineering commands the highest profitability at ~50% GP margin."

Chart panel: "EPCC Gross Margin Hierarchy by Market Segment" — caption: "Exhibits the margin gap between direct C&I solar, utility EPC, and BoP subcontracting." (data in Charts section, Chart 4).

### Audited Financial Benchmarks of Listed EPCCs

| Company | Unbilled Order Book | Gross Margin | Net Margin |
|---|---|---|---|
| Northern Solar | RM 119.4M LSS5 + C&I | 27.4% – 37.8% | 10.1% – 13.5% |
| Solarvest | RM 2,370M (Aug 2026) | 28.3% – 28.5% | 10.7% – 12.5% |
| Pekat Group | RM 994M (Jul 2026) | 25.2% – 27.0% | 8.0% – 10.5% |
| Sunview Group | ~RM 1,169.5M | 12.0% – 16.0% | 2.1% – 2.8% |
| Founder Group | Active CGPP Subcontracts | 6.5% – 10.8% | -4.7% (Pre-tax Loss) |
| Cheeding (HV Grid) | RM 600M Target | ~50.0% | 28.2% |

### Standard C&I Turnkey Payment Milestones & Working Capital Flow

| Stage | Share | Milestone | Description (verbatim) |
|---|---|---|---|
| Stage 1 | 10% – 20% | LOA & Survey | Covers site engineering, SLD, TNB Connection Check & CAS filing. |
| Stage 2 | 40% – 50% | Equipment Delivery | Due upon arrival of Tier-1 modules, inverters & BESS cabinets on site. |
| Stage 3 | 20% – 25% | Installation | Roof mounting, DC/AC cabling, MV transformer & switchgear hookup. |
| Stage 4 | 5% – 10% | COD Commissioning | TNB meter swap, SCADA/EMS testing, grid handover sign-off. |
| Stage 5 | 5% Retention | 12-Month DLP | Held for 1-year Defects Liability Period. Locks ~half of contractor net margin. |

### Severe Price Competition Segments (Low Barrier)

- **Tier-2 Utility Balance-of-Plant Subcontracting:** Pure installation contractors compete fiercely on labour rates, eroding gross margins to 6.5%–10.8%.
- **Small C&I Rooftops (50–300 kWp):** Hundreds of RPVSPs pivoting from residential ATAP offer low-ball quotes (RM 2.40/Wp) by omitting roof reinforcement and structural warranties.
- **Standard BESS Hardware Distribution:** Direct Chinese OEM cabinet importers face heavy price degradation without software EMS integration.

### High-Moat & Margin-Insulated Segments

- **Zero-Capex / EaaS Peak Demand Shaving:** Protected by low-cost balance sheets, Sukuk facilities, REM engineers, and performance guarantee warranties.
- **Hyperscale Data Centre ELP & Switchgear:** Pekat commands ~30% GP margins in Earthing & Lightning Protection for Johor/PD data centres.
- **High-Voltage Grid Interconnections:** Cheeding holds 500 kV TNB transmission licenses, earning ~50% GP margins and 28% net margins.

## 7. Footer

- "Malaysia C&I Solar & BESS Market Report (2026)"
- "Synthesized from Bursa Malaysia filings, institutional equity research, SEDA & TNB RP4 guidelines."
- "Designed for C&I Energy Buyers, Financiers & Developers."

## 8. Competitor Detail Modal

Opened by clicking any competitor row; closed with the "×" button. Content for the clicked record (all fields listed in Embedded data tables):

- "Rank #{rank} Market Leader" (same wording for every rank), then the company name.
- "{ticker} | Portfolio Scale: {mw}".
- "Completed & Contracted BESS Projects:" → `bessProjects`.
- "Business Models Offered:" → every entry of `businessModels`.
- "EMS & Maximum Demand Product Suite:" → `emsProduct` (full text).
- "Strategic Moat & Positioning:" → `moat`.

## Charts

### Chart 1 — Solar EPCC rates (`chartSolarPricing`)

- Location: Section 1, left panel. Title: "Solar EPCC CAPEX per Tier (Gross vs. Net Effective after GITA)". Type: vertical bar, two series.
- Y axis: "Unit Cost (RM/Wp)" (begins at zero). X axis: tier labels (no title). Legend at bottom.
- Tooltip: "{series label}: RM {value to 2 dp}/Wp".

| Label | Gross CAPEX (RM/Wp) | Net Effective after GITA (RM/Wp) |
|---|---|---|
| 100 kWp | 2.80 | 2.12 |
| 500 kWp | 2.50 | 1.90 |
| 1 MWp | 2.25 | 1.71 |
| 3 MWp (Solar Only) | 2.00 | 1.52 |
| 3 MWp (Bundled BESS) | 3.25 | 2.21 |

### Chart 2 — BESS turnkey rates (`chartBessPricing`)

- Location: Section 1, right panel. Title: "C&I BESS Turnkey Cost per kWh (Gross vs. GITA + CA Net Shield)". Type: grouped vertical bar.
- Y axis: "Turnkey Rate (RM/kWh)" (begins at zero). Legend at bottom.
- Tooltip: "{series label}: RM {value}/kWh".

| Label | Gross Installed Cost (RM/kWh) | Net Effective Cost after GITA (RM/kWh) |
|---|---|---|
| 50-200 kWh Racks | 1475 | 973 |
| 200-500 kWh Cabinets | 1300 | 858 |
| 2-5 MWh Containers | 1175 | 775 |

### Chart 3 — RP4 demand tariff surge (`chartRp4Tariff`)

- Location: Section 3, left panel. Title: "TNB Demand Tariff Surge: Legacy vs. RP4 Capacity + Network Charge". Type: vertical bar, one series, legend hidden.
- Y axis: "RM / kW / Month" (begins at zero). Series label: "Monthly Demand Charge (RM/kW/month)".
- Tooltip: "Demand Penalty: RM {value to 2 dp}/kW/mo".

| Label | Monthly Demand Charge (RM/kW/month) |
|---|---|
| Legacy Commercial MD (C1/C2) | 37.00 |
| RP4 Commercial ToU (Capacity + Network) | 97.06 |
| RP4 NDMV General (Capacity + Network) | 89.27 |
| RP4 High-Peak Industrial | 98.61 |

### Chart 4 — EPCC margin hierarchy (`chartMargins`)

- Location: Section 4, left panel. Title: "EPCC Gross Margin Hierarchy by Market Segment". Type: horizontal bar (indexAxis y), two series.
- X axis: "Margin Percentage (%)" (begins at zero). Legend at bottom.
- Tooltip: "{series label}: {value to 1 dp}%".

| Label | Gross Profit Margin % | Core Net Profit Margin % |
|---|---|---|
| Direct C&I Turnkey | 30.0 | 12.5 |
| Utility Main EPC (LSS/CGPP) | 18.5 | 7.5 |
| Utility BoP Subcontracting | 8.6 | -2.5 |
| High-Voltage Grid Engineering | 50.0 | 28.2 |

## Calculators and interactive logic

### A. Interactive C&I Solar + BESS Project ROI & Tax Shield Estimator (`updateSimulator()`)

Runs on page load (DOMContentLoaded) and on every change of any of the three selects.

#### Inputs

1. "1. Rooftop Solar PV Scale" (`simSolarSize`)

| Option label | value | Default |
|---|---|---|
| 100 kWp (SME Factory - RM 2.80/Wp) | 100 | |
| 500 kWp (Medium Factory - RM 2.50/Wp) | 500 | selected |
| 1 MWp (Large Warehouse - RM 2.20/Wp) | 1000 | |
| 3 MWp (Industrial Campus - RM 2.00/Wp) | 3000 | |

2. "2. Battery Energy Storage (BESS)" (`simBessSize`)

| Option label | value | Default |
|---|---|---|
| None (Solar Only) | 0 | |
| 200 kWh Cabinet (Peak Shaving - RM 1,350/kWh) | 200 | selected |
| 500 kWh Cabinet Bank (RM 1,250/kWh) | 500 | |
| 2 MWh Container System (RM 1,150/kWh) | 2000 | |

3. "3. Fiscal Tax Allowance Scenario" (`simTaxMode`)

| Option label | value | Default |
|---|---|---|
| 100% GITA + CA Tax Allowance (Pre-Dec 2026) | gita100 | selected |
| 60% GITA Tier (Standard Solar Asset) | gita60 | |
| Pre-Tax / No GITA Allowance | none | |

#### Constants (from the code)

| Constant | Value | Code comment |
|---|---|---|
| solarRate (RM/Wp) | 2.80 default (100 kWp); 2.50 if 500; 2.20 if 1000; 2.00 if 3000 | "Unit rate dynamics" |
| bessRate (RM/kWh) | 1350 default (used for 0 and 200 kWh); 1250 if 500; 1150 if 2000 | |
| Tax shield factor, gita100 | 0.34 × gross CAPEX | "100% GITA ITA + standard Capital Allowance (~34% total tax shield)" |
| Tax shield factor, gita60 | 0.24 × gross CAPEX | "60% GITA ITA + standard CA (~24% net)" |
| Tax shield, none | 0 | |
| Corporate tax rate (comment only) | 24% | "Tax shield calculation (Corporate tax = 24%)" |
| Solar yield | 1250 kWh/kWp/yr | "Solar yield ~1,250 kWh / kWp / yr @ ~RM 0.38 blended avoided cost" |
| Solar avoided cost | RM 0.38/kWh | (same comment) |
| BESS kW shaved | kWh / 2 | "BESS MD Shaving: ~1 kW shaved per 2 kWh BESS @ RM 89.27/kW/month TNB NDMV rate" |
| MD rate | RM 89.27/kW/month, × 12 months | (same comment) |

#### Formula (pseudo-code faithful to the JS)

```
solarKw  = int(simSolarSize)          # 100 | 500 | 1000 | 3000
bessKwh  = int(simBessSize)           # 0 | 200 | 500 | 2000
taxMode  = simTaxMode                 # gita100 | gita60 | none

solarRate = 2.80; if solarKw==500: 2.50; if solarKw==1000: 2.20; if solarKw==3000: 2.00
bessRate  = 1350; if bessKwh==500: 1250; if bessKwh==2000: 1150

solarCapex = solarKw * 1000 * solarRate
bessCapex  = bessKwh * bessRate
grossCapex = solarCapex + bessCapex

taxSavings = grossCapex * 0.34  if taxMode=='gita100'
           = grossCapex * 0.24  if taxMode=='gita60'
           = 0                  otherwise
netCapex   = grossCapex - taxSavings

solarSavingsYr = solarKw * 1250 * 0.38
bessKwShaved   = bessKwh / 2
bessSavingsYr  = bessKwShaved * 89.27 * 12
totalSavingsYr = solarSavingsYr + bessSavingsYr
paybackYrs     = netCapex / totalSavingsYr
```

#### Outputs (four cards)

| Card label | Element | Main value format | Sub-line format |
|---|---|---|---|
| Total Gross CAPEX | outGrossCapex | "RM " + grossCapex (locale, thousands separators) | outCapexSub: "Solar: RM {solarCapex/1000, 0 dp}k \| BESS: RM {bessCapex/1000, 0 dp}k" |
| Tax Shield Savings | outTaxSavings | "RM " + round(taxSavings) | outTaxSub: "No tax shield applied" if none, else "GITA Allowance @ 24% tax rate" |
| Est. Year-1 Bill Savings | outYearlySavings | "RM " + round(totalSavingsYr) + " / yr" | outSavingsSub: "Solar: RM {round(solarSavingsYr/1000)}k \| MD Shaving: RM {round(bessSavingsYr/1000)}k" |
| Net Simple Payback | outPayback | paybackYrs (1 dp) + " Years" | outPaybackSub: "Net CAPEX RM {round(netCapex/1000)}k vs pre-tax {grossCapex/totalSavingsYr, 1 dp} yrs" |

#### Placeholder values in the static HTML (shown before the script runs) vs computed defaults

| Card | Static placeholder | Computed at defaults (500 kWp, 200 kWh, gita100) |
|---|---|---|
| Total Gross CAPEX | RM 1,520,000 | RM 1,520,000 |
| Gross CAPEX sub-line | Solar: RM 1.25M \| BESS: RM 270k | Solar: RM 1250k \| BESS: RM 270k |
| Tax Shield Savings | RM 391,800 | RM 516,800 |
| Tax sub-line | Combined GITA & Corporate CA | GITA Allowance @ 24% tax rate |
| Est. Year-1 Bill Savings | RM 253,200 / yr | RM 344,624 / yr |
| Savings sub-line | Solar energy + BESS MD cut | Solar: RM 238k \| MD Shaving: RM 107k |
| Net Simple Payback | 4.4 Years | 2.9 Years |
| Payback sub-line | vs. 6.0 yrs without GITA | Net CAPEX RM 1003k vs pre-tax 4.4 yrs |

#### Outputs at default inputs (computed by running the code logic)

500 kWp solar (RM 2.50/Wp), 200 kWh BESS (RM 1,350/kWh), "100% GITA + CA":
- solarCapex = 1,250,000; bessCapex = 270,000; grossCapex = RM 1,520,000.
- taxSavings = 1,520,000 × 0.34 = RM 516,800; netCapex = RM 1,003,200.
- solarSavingsYr = 500 × 1,250 × 0.38 = RM 237,500; bessKwShaved = 100 kW; bessSavingsYr = 100 × 89.27 × 12 = RM 107,124; totalSavingsYr = RM 344,624.
- paybackYrs = 1,003,200 / 344,624 = 2.911 → "2.9 Years"; pre-tax = 1,520,000 / 344,624 = 4.411 → "4.4 yrs".

#### Outputs for every input combination (4 × 4 × 3 = 48), computed with the code logic

Display rounding emulates the JS (`toLocaleString`, `Math.round`, `toFixed`). "k" columns are the values shown in the sub-lines.

| # | Solar (simSolarSize) | BESS (simBessSize) | Tax mode | outGrossCapex | Solar CAPEX (k) | BESS CAPEX (k) | outTaxSavings | outTaxSub | outYearlySavings | Solar savings (k) | MD shaving savings (k) | outPayback | Net CAPEX (k) | Pre-tax payback (yrs) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 100 | 0 | gita100 | RM 280,000 | 280k | 0k | RM 95,200 | GITA Allowance @ 24% tax rate | RM 47,500 / yr | 48k | 0k | 3.9 Years | 185k | 5.9 |
| 2 | 100 | 0 | gita60 | RM 280,000 | 280k | 0k | RM 67,200 | GITA Allowance @ 24% tax rate | RM 47,500 / yr | 48k | 0k | 4.5 Years | 213k | 5.9 |
| 3 | 100 | 0 | none | RM 280,000 | 280k | 0k | RM 0 | No tax shield applied | RM 47,500 / yr | 48k | 0k | 5.9 Years | 280k | 5.9 |
| 4 | 100 | 200 | gita100 | RM 550,000 | 280k | 270k | RM 187,000 | GITA Allowance @ 24% tax rate | RM 154,624 / yr | 48k | 107k | 2.3 Years | 363k | 3.6 |
| 5 | 100 | 200 | gita60 | RM 550,000 | 280k | 270k | RM 132,000 | GITA Allowance @ 24% tax rate | RM 154,624 / yr | 48k | 107k | 2.7 Years | 418k | 3.6 |
| 6 | 100 | 200 | none | RM 550,000 | 280k | 270k | RM 0 | No tax shield applied | RM 154,624 / yr | 48k | 107k | 3.6 Years | 550k | 3.6 |
| 7 | 100 | 500 | gita100 | RM 905,000 | 280k | 625k | RM 307,700 | GITA Allowance @ 24% tax rate | RM 315,310 / yr | 48k | 268k | 1.9 Years | 597k | 2.9 |
| 8 | 100 | 500 | gita60 | RM 905,000 | 280k | 625k | RM 217,200 | GITA Allowance @ 24% tax rate | RM 315,310 / yr | 48k | 268k | 2.2 Years | 688k | 2.9 |
| 9 | 100 | 500 | none | RM 905,000 | 280k | 625k | RM 0 | No tax shield applied | RM 315,310 / yr | 48k | 268k | 2.9 Years | 905k | 2.9 |
| 10 | 100 | 2000 | gita100 | RM 2,580,000 | 280k | 2300k | RM 877,200 | GITA Allowance @ 24% tax rate | RM 1,118,740 / yr | 48k | 1071k | 1.5 Years | 1703k | 2.3 |
| 11 | 100 | 2000 | gita60 | RM 2,580,000 | 280k | 2300k | RM 619,200 | GITA Allowance @ 24% tax rate | RM 1,118,740 / yr | 48k | 1071k | 1.8 Years | 1961k | 2.3 |
| 12 | 100 | 2000 | none | RM 2,580,000 | 280k | 2300k | RM 0 | No tax shield applied | RM 1,118,740 / yr | 48k | 1071k | 2.3 Years | 2580k | 2.3 |
| 13 | 500 | 0 | gita100 | RM 1,250,000 | 1250k | 0k | RM 425,000 | GITA Allowance @ 24% tax rate | RM 237,500 / yr | 238k | 0k | 3.5 Years | 825k | 5.3 |
| 14 | 500 | 0 | gita60 | RM 1,250,000 | 1250k | 0k | RM 300,000 | GITA Allowance @ 24% tax rate | RM 237,500 / yr | 238k | 0k | 4.0 Years | 950k | 5.3 |
| 15 | 500 | 0 | none | RM 1,250,000 | 1250k | 0k | RM 0 | No tax shield applied | RM 237,500 / yr | 238k | 0k | 5.3 Years | 1250k | 5.3 |
| 16 (default) | 500 | 200 | gita100 | RM 1,520,000 | 1250k | 270k | RM 516,800 | GITA Allowance @ 24% tax rate | RM 344,624 / yr | 238k | 107k | 2.9 Years | 1003k | 4.4 |
| 17 | 500 | 200 | gita60 | RM 1,520,000 | 1250k | 270k | RM 364,800 | GITA Allowance @ 24% tax rate | RM 344,624 / yr | 238k | 107k | 3.4 Years | 1155k | 4.4 |
| 18 | 500 | 200 | none | RM 1,520,000 | 1250k | 270k | RM 0 | No tax shield applied | RM 344,624 / yr | 238k | 107k | 4.4 Years | 1520k | 4.4 |
| 19 | 500 | 500 | gita100 | RM 1,875,000 | 1250k | 625k | RM 637,500 | GITA Allowance @ 24% tax rate | RM 505,310 / yr | 238k | 268k | 2.4 Years | 1238k | 3.7 |
| 20 | 500 | 500 | gita60 | RM 1,875,000 | 1250k | 625k | RM 450,000 | GITA Allowance @ 24% tax rate | RM 505,310 / yr | 238k | 268k | 2.8 Years | 1425k | 3.7 |
| 21 | 500 | 500 | none | RM 1,875,000 | 1250k | 625k | RM 0 | No tax shield applied | RM 505,310 / yr | 238k | 268k | 3.7 Years | 1875k | 3.7 |
| 22 | 500 | 2000 | gita100 | RM 3,550,000 | 1250k | 2300k | RM 1,207,000 | GITA Allowance @ 24% tax rate | RM 1,308,740 / yr | 238k | 1071k | 1.8 Years | 2343k | 2.7 |
| 23 | 500 | 2000 | gita60 | RM 3,550,000 | 1250k | 2300k | RM 852,000 | GITA Allowance @ 24% tax rate | RM 1,308,740 / yr | 238k | 1071k | 2.1 Years | 2698k | 2.7 |
| 24 | 500 | 2000 | none | RM 3,550,000 | 1250k | 2300k | RM 0 | No tax shield applied | RM 1,308,740 / yr | 238k | 1071k | 2.7 Years | 3550k | 2.7 |
| 25 | 1000 | 0 | gita100 | RM 2,200,000 | 2200k | 0k | RM 748,000 | GITA Allowance @ 24% tax rate | RM 475,000 / yr | 475k | 0k | 3.1 Years | 1452k | 4.6 |
| 26 | 1000 | 0 | gita60 | RM 2,200,000 | 2200k | 0k | RM 528,000 | GITA Allowance @ 24% tax rate | RM 475,000 / yr | 475k | 0k | 3.5 Years | 1672k | 4.6 |
| 27 | 1000 | 0 | none | RM 2,200,000 | 2200k | 0k | RM 0 | No tax shield applied | RM 475,000 / yr | 475k | 0k | 4.6 Years | 2200k | 4.6 |
| 28 | 1000 | 200 | gita100 | RM 2,470,000 | 2200k | 270k | RM 839,800 | GITA Allowance @ 24% tax rate | RM 582,124 / yr | 475k | 107k | 2.8 Years | 1630k | 4.2 |
| 29 | 1000 | 200 | gita60 | RM 2,470,000 | 2200k | 270k | RM 592,800 | GITA Allowance @ 24% tax rate | RM 582,124 / yr | 475k | 107k | 3.2 Years | 1877k | 4.2 |
| 30 | 1000 | 200 | none | RM 2,470,000 | 2200k | 270k | RM 0 | No tax shield applied | RM 582,124 / yr | 475k | 107k | 4.2 Years | 2470k | 4.2 |
| 31 | 1000 | 500 | gita100 | RM 2,825,000 | 2200k | 625k | RM 960,500 | GITA Allowance @ 24% tax rate | RM 742,810 / yr | 475k | 268k | 2.5 Years | 1865k | 3.8 |
| 32 | 1000 | 500 | gita60 | RM 2,825,000 | 2200k | 625k | RM 678,000 | GITA Allowance @ 24% tax rate | RM 742,810 / yr | 475k | 268k | 2.9 Years | 2147k | 3.8 |
| 33 | 1000 | 500 | none | RM 2,825,000 | 2200k | 625k | RM 0 | No tax shield applied | RM 742,810 / yr | 475k | 268k | 3.8 Years | 2825k | 3.8 |
| 34 | 1000 | 2000 | gita100 | RM 4,500,000 | 2200k | 2300k | RM 1,530,000 | GITA Allowance @ 24% tax rate | RM 1,546,240 / yr | 475k | 1071k | 1.9 Years | 2970k | 2.9 |
| 35 | 1000 | 2000 | gita60 | RM 4,500,000 | 2200k | 2300k | RM 1,080,000 | GITA Allowance @ 24% tax rate | RM 1,546,240 / yr | 475k | 1071k | 2.2 Years | 3420k | 2.9 |
| 36 | 1000 | 2000 | none | RM 4,500,000 | 2200k | 2300k | RM 0 | No tax shield applied | RM 1,546,240 / yr | 475k | 1071k | 2.9 Years | 4500k | 2.9 |
| 37 | 3000 | 0 | gita100 | RM 6,000,000 | 6000k | 0k | RM 2,040,000 | GITA Allowance @ 24% tax rate | RM 1,425,000 / yr | 1425k | 0k | 2.8 Years | 3960k | 4.2 |
| 38 | 3000 | 0 | gita60 | RM 6,000,000 | 6000k | 0k | RM 1,440,000 | GITA Allowance @ 24% tax rate | RM 1,425,000 / yr | 1425k | 0k | 3.2 Years | 4560k | 4.2 |
| 39 | 3000 | 0 | none | RM 6,000,000 | 6000k | 0k | RM 0 | No tax shield applied | RM 1,425,000 / yr | 1425k | 0k | 4.2 Years | 6000k | 4.2 |
| 40 | 3000 | 200 | gita100 | RM 6,270,000 | 6000k | 270k | RM 2,131,800 | GITA Allowance @ 24% tax rate | RM 1,532,124 / yr | 1425k | 107k | 2.7 Years | 4138k | 4.1 |
| 41 | 3000 | 200 | gita60 | RM 6,270,000 | 6000k | 270k | RM 1,504,800 | GITA Allowance @ 24% tax rate | RM 1,532,124 / yr | 1425k | 107k | 3.1 Years | 4765k | 4.1 |
| 42 | 3000 | 200 | none | RM 6,270,000 | 6000k | 270k | RM 0 | No tax shield applied | RM 1,532,124 / yr | 1425k | 107k | 4.1 Years | 6270k | 4.1 |
| 43 | 3000 | 500 | gita100 | RM 6,625,000 | 6000k | 625k | RM 2,252,500 | GITA Allowance @ 24% tax rate | RM 1,692,810 / yr | 1425k | 268k | 2.6 Years | 4373k | 3.9 |
| 44 | 3000 | 500 | gita60 | RM 6,625,000 | 6000k | 625k | RM 1,590,000 | GITA Allowance @ 24% tax rate | RM 1,692,810 / yr | 1425k | 268k | 3.0 Years | 5035k | 3.9 |
| 45 | 3000 | 500 | none | RM 6,625,000 | 6000k | 625k | RM 0 | No tax shield applied | RM 1,692,810 / yr | 1425k | 268k | 3.9 Years | 6625k | 3.9 |
| 46 | 3000 | 2000 | gita100 | RM 8,300,000 | 6000k | 2300k | RM 2,822,000 | GITA Allowance @ 24% tax rate | RM 2,496,240 / yr | 1425k | 1071k | 2.2 Years | 5478k | 3.3 |
| 47 | 3000 | 2000 | gita60 | RM 8,300,000 | 6000k | 2300k | RM 1,992,000 | GITA Allowance @ 24% tax rate | RM 2,496,240 / yr | 1425k | 1071k | 2.5 Years | 6308k | 3.3 |
| 48 | 3000 | 2000 | none | RM 8,300,000 | 6000k | 2300k | RM 0 | No tax shield applied | RM 2,496,240 / yr | 1425k | 1071k | 3.3 Years | 8300k | 3.3 |

### B. Competitor table search and filter (`filterCompetitors()`, `setFilter()`)

- Search box `compSearch` fires on every key-up. Query is lower-cased; a record matches if `name`, `bessTrack` or `emsProduct` (lower-cased) contains the query. Other fields (ticker, mw, bessProjects, businessModels, moat) are not searched.
- Filter buttons set `activeFilter` (default 'all') and re-run the search:
  - "All (15)" → 'all': search match only.
  - "Listed" → 'listed': search match AND `listed` = true (8 records: ranks 1, 4, 5, 6, 7, 8, 11, 12).
  - "Zero-Capex / EaaS" → 'zerocapex': search match AND `hasZeroCapex` = true (13 records; excludes Cypark Resources Bhd and Founder Group Ltd).
  - "Major BESS Track Record" → 'bess': search match AND `hasMajorBess` = true (14 records; excludes Progressture Solar).
  - The active button is highlighted; others reset.
- `renderCompetitors(data)` rebuilds the table body: per record, "{rank}. {name}" with ticker beneath; badge "Listed" or "Private" from `listed`; `mw`; `bessTrack` (single-line, truncated by CSS); first two `businessModels` plus "+N" if more; `emsProduct` text before the first "+" character. Each row opens the modal (section 8).
- `scrollToSection(id)` smooth-scrolls to the section for the nav buttons.

## Embedded data tables

### `competitors` array (15 records)

#### Summary of flags and scale (all 15 records)

| rank | name | ticker | listed | mw | hasZeroCapex | hasMajorBess | businessModels (count) |
|---|---|---|---|---|---|---|---|
| 1 | Solarvest Holdings Bhd | KLSE: SLVEST (0215) | true | ~3,700 MWp (3.7 GWp) | true | true | 4 |
| 2 | Gentari Sdn Bhd | Private (Wholly PETRONAS) | false | ~9,100 MW (9.1 GW) Global RE | true | true | 4 |
| 3 | Ditrolic Energy Holdings | Private (IFC & Sukuk Backed) | false | 1,000+ MW Constructed / 300 MW O&M | true | true | 3 |
| 4 | Samaiden Group Bhd | KLSE: SAMAIDEN | true | 700+ MWp Cumulative | true | true | 4 |
| 5 | Sunview Group Bhd | KLSE: SUNVIEW | true | ~650–800+ MWp Portfolio | true | true | 3 |
| 6 | Plus Xnergy Services | KLSE: BMGREEN (Parent) | true | >400+ MWp Solar / 100 MWh BESS | true | true | 3 |
| 7 | Cypark Resources Bhd | KLSE: CYPARK | true | >400 MWp Operational / Hybrid | false | true | 3 |
| 8 | Pekat Group Bhd | KLSE: PEKAT (0233) | true | ~300–400+ MWp Portfolio | true | true | 3 |
| 9 | GSPARX Sdn Bhd | Private (Wholly TNB) | false | 224 MW Installed C&I | true | true | 2 |
| 10 | Progressture Solar | Private | false | ~200–300+ MWp C&I | true | false | 3 |
| 11 | Founder Group Ltd | NASDAQ: FGL (Reservoir Link) | true | ~200+ MWp EPCC | false | true | 3 |
| 12 | Northern Solar Holdings | KLSE: NORTHERN (0340) | true | ~150+ MWp Cumulative | true | true | 3 |
| 13 | ERS Energy Sdn Bhd | Private | false | ~150+ MWp C&I | true | true | 3 |
| 14 | Cenergi SEA Bhd | Private (Khazanah / UEM) | false | ~100+ MWp Clean Energy | true | true | 2 |
| 15 | XPERTS.NRG (Green Xperts) | Private / KLSE: KAB (Partner) | false | 50 MW EPCC / 15 MW Owned | true | true | 3 |

#### Full records (every field, verbatim)

##### 1. Solarvest Holdings Bhd

- rank: 1
- name: "Solarvest Holdings Bhd"
- ticker: "KLSE: SLVEST (0215)"
- listed: true
- mw: "~3,700 MWp (3.7 GWp)"
- bessTrack: "Multiple C&I BESS (20%-65% MD cuts); Utility BESS bidder under MyBeST auction"
- bessProjects: "2024–2026 deployments across manufacturing plants, data centres & EV hubs. Bidding for 400 MW / 1,600 MWh MyBeST."
- businessModels: "Outright CAPEX", "Zero-CAPEX Powervest PPA", "Fintech Financing", "Zero-CAPEX BESS EaaS"
- emsProduct: "AI machine-learning load simulator + EPMS (Energy Performance Monitoring System)"
- moat: "Record RM 2.37B unbilled order book (Aug 2026) anchored by RM 1.06B LSS5+ EPCC in Perak."
- hasZeroCapex: true
- hasMajorBess: true

##### 2. Gentari Sdn Bhd

- rank: 2
- name: "Gentari Sdn Bhd"
- ticker: "Private (Wholly PETRONAS)"
- listed: false
- mw: "~9,100 MW (9.1 GW) Global RE"
- bessTrack: "Malaysia's 1st Solar+BESS EV Charging Hub (Oct 2023); ~1.5 GW Gamuda CRESS BESS"
- bessProjects: "Hyperscale data centre CRESS BESS firming + EV supercharging hub buffering."
- businessModels: "Zero-CAPEX PPA", "CRESS Green Power Supply", "Outright EPCC", "Integrated EaaS"
- emsProduct: "Integrated C&I energy management & CRESS BESS firming for hyperscale data centres"
- moat: "Backed by PETRONAS balance sheet; targeting 1.5 GW hyperscale data centre green power."
- hasZeroCapex: true
- hasMajorBess: true

##### 3. Ditrolic Energy Holdings

- rank: 3
- name: "Ditrolic Energy Holdings"
- ticker: "Private (IFC & Sukuk Backed)"
- listed: false
- mw: "1,000+ MW Constructed / 300 MW O&M"
- bessTrack: "C&I behind-the-meter EnerPack BESS; Johor RE Corridor utility BESS with IFC & PDT"
- bessProjects: "Industrial & data centre EnerPack deployments; 600 MW SJREC cross-border export approval (Aug 2026)."
- businessModels: "Outright EPC (EnerGreen)", "Zero-CAPEX PPA (EnerLoop)", "O&M Asset Mgmt"
- emsProduct: "EnerPack BTM BESS + Integrated Net-Zero Energy OS & 15-min Smart Integrated System"
- moat: "RM 150M Sukuk Wakalah tranche; IFC partnership for regional utility BESS."
- hasZeroCapex: true
- hasMajorBess: true

##### 4. Samaiden Group Bhd

- rank: 4
- name: "Samaiden Group Bhd"
- ticker: "KLSE: SAMAIDEN"
- listed: true
- mw: "700+ MWp Cumulative"
- bessTrack: "C&I BESS peak-shaving & backup installations (2025–2026); LSS6 BESS awards"
- bessProjects: "Industrial factory BESS; projected 125–188 MW LSS6 BESS awards."
- businessModels: "Outright EPCC", "Zero-CAPEX PPA Framework", "O&M Services", "REC Trading"
- emsProduct: "Automated BESS Peak-Shaving & MD Threshold Dispatch Controller"
- moat: "RM 600M YTD contract wins (Jul 2026); strong C&I client base including Nippon Electric Glass."
- hasZeroCapex: true
- hasMajorBess: true

##### 5. Sunview Group Bhd

- rank: 5
- name: "Sunview Group Bhd"
- ticker: "KLSE: SUNVIEW"
- listed: true
- mw: "~650–800+ MWp Portfolio"
- bessTrack: "595 MWac Floating Solar + BESS at Lake Kenyir for TNB Genco; SunBESS projects"
- bessProjects: "40% lead share in RM 1.96B CRE-Sunview JV at Lake Kenyir (Apr 2026); Uzbekistan BESS."
- businessModels: "Outright EPCC", "Solar + Storage CAPEX", "Asset Ownership / PPA"
- emsProduct: "SunBESS automated C&I peak-shaving & SELCO (>72 kWp) storage system"
- moat: "RM 1.17B backlog; massive utility floating solar + storage pipeline."
- hasZeroCapex: true
- hasMajorBess: true

##### 6. Plus Xnergy Services

- rank: 6
- name: "Plus Xnergy Services"
- ticker: "KLSE: BMGREEN (Parent)"
- listed: true
- mw: ">400+ MWp Solar / 100 MWh BESS"
- bessTrack: "20 MWh SELCO BESS in Perak (HyperStrong, Jun 2026); 1.45 MWh NaS BESS in Kedah"
- bessProjects: "Flagship 20 MWh single industrial deployment at Perak food factory; Leader Energy NaS BESS."
- businessModels: "Outright EPCC", "15-Yr Zero-CAPEX BESS Partnership", "Zero-CAPEX PPA"
- emsProduct: "AI-Driven BESS EMS & SOURCE smart energy platform (weekday 2–10 PM MD shaving)"
- moat: "Market leader in direct C&I BESS with 100 MWh deployed; offers benchmark RM 82.50/kW MD tariff."
- hasZeroCapex: true
- hasMajorBess: true

##### 7. Cypark Resources Bhd

- rank: 7
- name: "Cypark Resources Bhd"
- ticker: "KLSE: CYPARK"
- listed: true
- mw: ">400 MWp Operational / Hybrid"
- bessTrack: "595 MWac Floating Solar + BESS at Lake Kenyir (60% JV lead with Sunview)"
- bessProjects: "Co-lead in RM 1.96B Lake Kenyir floating PV + BESS project for TNB Genco (Apr 2026)."
- businessModels: "IPP Asset Ownership", "Turnkey EPCC", "Public-Private Partnerships"
- emsProduct: "Utility & hybrid solar-storage dispatch and grid-firming SCADA"
- moat: "Pioneer in utility-scale floating solar and large-scale hybrid storage infrastructure."
- hasZeroCapex: false
- hasMajorBess: true

##### 8. Pekat Group Bhd

- rank: 8
- name: "Pekat Group Bhd"
- ticker: "KLSE: PEKAT (0233)"
- listed: true
- mw: "~300–400+ MWp Portfolio"
- bessTrack: "Data centre & factory BESS integrated with EPE MV switchgear & ELP systems"
- bessProjects: "Port Dickson (RM 20M) and Johor (RM 27M) data centre electrical & BESS wins in Jul 2026."
- businessModels: "Outright EPCC", "Zero-CAPEX PPA / CGPP Asset", "BESS + O&M"
- emsProduct: "Integrated Solar + BESS peak-shaving & EPE medium-voltage distribution EMS"
- moat: "60% Peninsular market share in Earthing & Lightning Protection (ELP); RM 994M unbilled backlog."
- hasZeroCapex: true
- hasMajorBess: true

##### 9. GSPARX Sdn Bhd

- rank: 9
- name: "GSPARX Sdn Bhd"
- ticker: "Private (Wholly TNB)"
- listed: false
- mw: "224 MW Installed C&I"
- bessTrack: "76.8–170 kWh BESS at Elmina Ilham; C&I BESS partnership with EVE Energy"
- bessProjects: "Residential & factory BESS; EVE Energy built 36 MWh / 18 MW BESS at KLIA (Feb 2026)."
- businessModels: "Zero-CAPEX SARE PPA (via TNB Bill)", "Outright EPCC"
- emsProduct: "TNB Smart Grid-integrated BESS peak shaving & automated load management"
- moat: "Direct billing integration via TNB electricity invoice via SARE mechanism."
- hasZeroCapex: true
- hasMajorBess: true

##### 10. Progressture Solar

- rank: 10
- name: "Progressture Solar"
- ticker: "Private"
- listed: false
- mw: "~200–300+ MWp C&I"
- bessTrack: "Turnkey C&I BESS for manufacturing factories, commercial property & data centres"
- bessProjects: "600+ Shell stations, ~100 Petron stations, data centres, 12 MWp Brunei utility plant in 2026."
- businessModels: "Outright EPCC", "Zero-Upfront Solar PPA", "Custom Solar/BESS Financing"
- emsProduct: "End-to-end BESS peak shaving, load shifting & power expansion EMS"
- moat: "Dominant retail fuel station solarization track record across Peninsular Malaysia."
- hasZeroCapex: true
- hasMajorBess: false

##### 11. Founder Group Ltd

- rank: 11
- name: "Founder Group Ltd"
- ticker: "NASDAQ: FGL (Reservoir Link)"
- listed: true
- mw: "~200+ MWp EPCC"
- bessTrack: "Iron-Flow Long-Duration Energy Storage (LDES) via JV RL ADS Power"
- bessProjects: "Commercializing long-duration iron-flow batteries across MY, SG, and ID (2025–2026)."
- businessModels: "Outright EPCC", "BoP Subcontracting", "C&I Rooftop Investor"
- emsProduct: "AI-powered O&M & Iron-Flow LDES industrial load-shifting platform"
- moat: "Specialised in Iron-Flow LDES chemistry for long-duration industrial storage."
- hasZeroCapex: false
- hasMajorBess: true

##### 12. Northern Solar Holdings

- rank: 12
- name: "Northern Solar Holdings"
- ticker: "KLSE: NORTHERN (0340)"
- listed: true
- mw: "~150+ MWp Cumulative"
- bessTrack: "Contracted RM 20.5M ground-mounted SELCO BESS project (~15–18 MWh)"
- bessProjects: "Disclosed RM 20.5M SELCO BESS award; C&I Sungrow/Huawei/EVE cabinets."
- businessModels: "Outright EPCC (96.7% Rev)", "Zero-CAPEX PPA", "GTFS 5.0 Financing"
- emsProduct: "Interval-meter-calibrated BESS Peak Shaving suppressing 30-min TNB MD spikes"
- moat: "Direct high-margin C&I specialist (~34.4% FY26 GP margin) with RM 119.4M LSS5 award."
- hasZeroCapex: true
- hasMajorBess: true

##### 13. ERS Energy Sdn Bhd

- rank: 13
- name: "ERS Energy Sdn Bhd"
- ticker: "Private"
- listed: false
- mw: "~150+ MWp C&I"
- bessTrack: "500 kWp Solar + 200 kWh BESS at Penang Electronics Plant (35% MD cut)"
- bessProjects: "Penang electronics plant cutting peak demand by 35% with zero upfront CAPEX."
- businessModels: "Direct Purchase (CAPEX)", "Zero-Upfront PPA (15-25 Yrs)", "Green Lease"
- emsProduct: "Solar + BESS Hybrid EMS (<20 ms UPS switchover & 35% MD cut)"
- moat: "Pioneer in seamless <20ms UPS switchover for high-tech semiconductor & electronics plants."
- hasZeroCapex: true
- hasMajorBess: true

##### 14. Cenergi SEA Bhd

- rank: 14
- name: "Cenergi SEA Bhd"
- ticker: "Private (Khazanah / UEM)"
- listed: false
- mw: "~100+ MWp Clean Energy"
- bessTrack: "Operational C&I BESS integrated with solar (>1 MWac SELCO) & biogas"
- bessProjects: "Mandatory SELCO BESS projects paired with rooftop solar across West Malaysia."
- businessModels: "Zero-CAPEX BESS", "Zero-CAPEX Solar PPA (100% Funded)"
- emsProduct: "Automated background BESS controller for SELCO compliance & MD network shaving"
- moat: "Backed by Khazanah's green vehicle UEM Group; strong public sector & corporate access."
- hasZeroCapex: true
- hasMajorBess: true

##### 15. XPERTS.NRG (Green Xperts)

- rank: 15
- name: "XPERTS.NRG (Green Xperts)"
- ticker: "Private / KLSE: KAB (Partner)"
- listed: false
- mw: "50 MW EPCC / 15 MW Owned"
- bessTrack: "Consortium partner with TNB for 1,000 MWh BESS under CRESS"
- bessProjects: "1,000 MWh CRESS utility storage partnership with TNB; C&I ESCO MD shaving."
- businessModels: "Zero-CAPEX Solar PPA", "ESCO Shared Savings", "Outright EPCC"
- emsProduct: "Dedicated MD Shaving BESS dispatch & industrial Energy Management Systems"
- moat: "Consortium partner for TNB's 1,000 MWh CRESS mega-storage deployment."
- hasZeroCapex: true
- hasMajorBess: true

## Links and cited documents

The report contains no hyperlinks (`<a href>`) and no per-figure citations. External URLs appear only as script sources.

| Label as shown | URL or document ID | Where used |
|---|---|---|
| Tailwind CSS CDN (script) | https://cdn.tailwindcss.com | Page styling library |
| Chart.js CDN (script, unversioned) | https://cdn.jsdelivr.net/npm/chart.js | Renders Charts 1–4 |
| Bursa Malaysia filings | (no ID/link) | Footer source line |
| institutional equity research | (no ID/link) | Footer source line |
| SEDA | (no ID/link) | Footer source line |
| TNB RP4 guidelines / "TNB’s RP4 tariff schedule (1 July 2025 – 31 Dec 2027)" | (no ID/link) | Footer; Overview; Section 3; Chart 3 |
| Legacy tariff C1/C2; RP4 Commercial ToU; RP4 NDMV General; RP4 High-Peak Industrial | tariff categories | Chart 3; calculator comment ("TNB NDMV rate") |
| SELCO (mandatory SELCO battery storage guidelines; "SELCO (>72 kWp)"; "SELCO (≥1 MWac)"; ">1 MWac SELCO") | (no ID/link) | Overview; Section 2; Section 3 card 6; Sunview, Cenergi, Plus Xnergy, Northern Solar records |
| GITA (Green Investment Tax Allowance) — "60-100%", "100% GITA + CA", "60% GITA Tier", "GITA ITA" | (no ID/link) | Overview card; Section 1; calculator; Charts 1–2 |
| GTFS; "GTFS 5.0 Financing" | (no ID/link) | Overview card; Northern Solar record |
| CA (Capital Allowance) | — | Calculator |
| LSS5; "LSS5+" | tender | Overview card; Section 4; Solarvest, Northern Solar records |
| LSS6 | tender | Overview card; Samaiden record |
| CRESS | programme/tender | Overview card; Gentari, XPERTS.NRG records; Section 3 card 8 |
| CGPP | programme | Section 4 text and table; Chart 4 label; Pekat record |
| MyBeST auction ("400 MW / 1,600 MWh MyBeST") | tender | Solarvest record |
| NFPA 855 | standard | Chart 2 caption |
| SARE mechanism ("Zero-CAPEX SARE PPA (via TNB Bill)") | — | GSPARX record |
| Sukuk Wakalah ("RM 150M Sukuk Wakalah tranche") | — | Ditrolic record |
| SJREC cross-border export approval (600 MW, Aug 2026); Johor RE Corridor | — | Ditrolic record |
| TNB Connection Check; CAS filing; SLD | — | Payment Stage 1 |
| Defects Liability Period (DLP) | — | Payment Stage 5 |
| ATAP (residential); RPVSPs | — | Section 4 competition box |
| China's 9% VAT rebate removal | — | Section 1 lead text |
| Registered Energy Managers (REM) | — | Section 3 card 2; Section 4 moat box |
| Lake Kenyir 595 MWac floating solar + BESS (RM 1.96B; TNB Genco; CRE-Sunview JV, Apr 2026) | project | Section 2 card 1; Sunview, Cypark records |
| Exchange listings: KLSE: SLVEST (0215); KLSE: SAMAIDEN; KLSE: SUNVIEW; KLSE: BMGREEN (Parent); KLSE: CYPARK; KLSE: PEKAT (0233); KLSE: NORTHERN (0340); NASDAQ: FGL (Reservoir Link); KLSE: KAB (Partner) | tickers | Competitor records |

## Extraction notes

Extractor observations (not report content).

1. **No sources.** The report has no hyperlinks and no per-figure citations; the only source statement is the generic footer line. No figure in it can be traced (prompt #3 asked "Link every figure").
2. **GITA deadline may be stale.** The report treats 31 Dec 2026 as the GITA/GTFS sunset ("imminent 31 December 2026 sunset", "60-100% Tax Allowance Deadline", "until 31 December 2026", calculator option "(Pre-Dec 2026)") and never mentions Budget 2027, although the file is dated 2026-10-23. Other reports in the same folder say otherwise: `malaysia_green_tax_incentives_portal.html` says Budget 2027 (tabled 9 October 2026) "extends Malaysia's Green Investment Tax Allowance (GITA) framework by four years until 31 December 2030", with support shifted to integrated Solar + BESS; `malaysia_c_i_solar_bess_financing_2026.html` says standalone solar GITA ends 31 Dec 2026 and integrated BESS is needed for 100% GITA Tier 1 from 2027. Not reconciled here.
3. **"+162%" does not match the stated base.** Text says from RM 30.30/kW to RM 89.27–97.06/kW/month, which works out to +194.6% to +220.3%. +162% matches the chart's legacy bar of RM 37.00 → RM 97.06 (+162.3%). So the legacy base is RM 30.30 in the text but RM 37.00 in the chart.
4. **Unexplained 98.61.** Chart 3's "RP4 High-Peak Industrial" bar (RM 98.61/kW/month) is not mentioned anywhere else, and it is higher than the metric card's "Up to RM 97.06/kW/mo".
5. **Calculator placeholders do not match the code.** At defaults the code gives a tax shield of RM 516,800 (34% of RM 1,520,000), savings of RM 344,624/yr and a 2.9-year payback. The placeholders show RM 391,800, RM 253,200/yr and 4.4 years. RM 391,800 equals exactly 1,250,000 × 0.24 + 270,000 × 0.34 (24% on solar, 34% on BESS), which matches the charts' implied net factors (note 9) but not the code. RM 253,200 cannot be rebuilt from the code's constants. The placeholder 4.4 years does not even follow from the placeholders themselves: (1,520,000 − 391,800) / 253,200 = 4.46, which displays as "4.5". The "6.0 yrs without GITA" does follow (1,520,000 / 253,200 = 6.00). By coincidence, the code's pre-tax payback at defaults is 4.4 yrs. The placeholder sub-lines also use different formats ("RM 1.25M" vs "RM 1250k").
6. **Tax-shield factors are hard-coded and not derived.** The code comment states 24% corporate tax. 100% × 24% = 24% and 60% × 24% = 14.4% for the allowance alone, but the code uses 34% and 24% without showing how capital allowance adds the rest. The same factor applies to solar and BESS CAPEX alike (even though the gita60 option is labelled "Standard Solar Asset"), and the shield is taken off CAPEX at year 0, with no timing or utilisation limit.
7. **Savings are gross.** MD savings assume each 2 kWh of storage shaves 1 kW every month at the full RM 89.27 (NDMV General) × 12. There is no charging cost, no O&M (Section 1 itself lists 1.5%–4.5%/yr for BESS and 1.0%–1.5% for solar), no degradation and no dispatch-failure risk, even though Section 3 says one 30-minute failure resets the month's MD charge. Example: 2 MWh gives RM 1,071k/yr against RM 2,300k of BESS CAPEX. Solar uses a flat 1,250 kWh/kWp × RM 0.38. You cannot model BESS-only, because there is no "no solar" option.
8. **Calculator vs tables.**
   - 1 MWp rate is RM 2.20/Wp in the calculator but 2.25 in Chart 1.
   - The Section 1 table's "Payback (Post-GITA)" values (100 kWp 4.0–4.5; 500 kWp 4.4; 1 MWp 3.5–4.5; 3 MWp 3.5–4.5 yrs) differ from the calculator's solar-only gita100 results (3.9 / 3.5 / 3.1 / 2.8 yrs) and gita60 results (4.5 / 4.0 / 3.5 / 3.2 yrs).
   - The table's 500 kWp "4.4 Yrs" equals the placeholder.
9. **Chart "net" values: basis not stated.**
   - Chart 1 solar net values are 76% of gross (2.12/2.80, 1.90/2.50, 1.71/2.25, 1.52/2.00), a 24% reduction. That matches the calculator's gita60 factor, not the default gita100 (34%). 2.80 × 0.76 = 2.128 is shown as 2.12.
   - "3 MWp (Bundled BESS)" is 68% (2.21/3.25), and its BESS size is not stated.
   - Chart 2 BESS net values are 66% of gross (973/1475, 858/1300, 775/1175), i.e. a 34% reduction.
   - Chart 2 gross values 1300 and 1175 are the midpoints of the text ranges 1,150–1,450 and 1,000–1,350. The "50-200 kWh Racks" tier (RM 1,475) appears only in the chart.
10. **Solar table.** Gross CAPEX ranges equal capacity × unit rate in all four rows. The tier ranges overlap: 100 kWp and 500 kWp both start at RM 2.40/Wp. The "low-ball quotes (RM 2.40/Wp)" in Section 4 equal that benchmark floor.
11. **Plus Xnergy 15/85 example.**
    - The arithmetic checks out: 97.06 − 82.50 = 14.56/kW (15.0%); 14.56 × 1,478 = RM 21,519.68 ≈ "~RM 21,520/month"; 82.50/97.06 = 85.0%.
    - "2-hour LFP" at RM 2,300–2,900/kW = RM 1,150–1,450/kWh, which matches the cabinet range.
    - The return claim does not reconcile. Developer revenue of RM 82.50 × 12 = RM 990/kW/yr gives a 2.3–2.9-yr gross payback before costs. Over a 15-year term a ~4-year payback implies about 24% IRR, while 12%–18% p.a. implies roughly a 5–7-year payback. The example also uses the RM 97.06 Commercial ToU rate, while the calculator uses RM 89.27.
12. **MW figures vs national total.** The national cumulative total is 5,777 MW (end-2025). The 15 companies' MW figures add up to at least 8,224 MW even without Gentari's 9,100 MW, which is labelled "Global RE". Solarvest alone (~3,700 MWp) is 64% of 5,777. The MW basis (Malaysia vs global, constructed vs portfolio vs owned, utility vs C&I) varies by company and is not stated. Prompt #3 asked for C&I MW.
13. **Ranking basis not stated.** Gentari (~9,100 MW) is ranked #2 behind Solarvest (~3,700 MWp). Below that the list roughly descends by MW.
14. **SELCO BESS threshold inconsistent.** Sunview's record says "SELCO (>72 kWp)"; Cenergi says "SELCO (≥1 MWac)" / ">1 MWac SELCO". Neither is sourced.
15. **Filter flags barely discriminate.**
    - hasMajorBess is true for 14 of 15 (only Progressture is false). That includes GSPARX, whose own BESS is "76.8–170 kWh" (the 36 MWh KLIA system is credited to EVE Energy), and Founder, whose iron-flow LDES is "Commercializing" with no completed project given.
    - hasZeroCapex is true for 13 of 15, including Sunview, whose businessModels list no explicit zero-capex model.
    - Listing labels are mixed: Founder is "listed" on NASDAQ, and Plus Xnergy via its parent (KLSE: BMGREEN). Cenergi "SEA Bhd" is marked "Private (Khazanah / UEM)", and XPERTS.NRG is not listed but shows "KLSE: KAB (Partner)".
16. **Table and search quirks.**
    - The search placeholder promises "client" search, but only name/bessTrack/emsProduct are searched. Client names in bessProjects/moat (e.g. Nippon Electric Glass, Shell, Petron) cannot be found.
    - The table column "Completed & Contracted BESS Projects" shows `bessTrack`, while the modal heading of the same name shows `bessProjects`.
    - The EMS column cuts at the first "+", so ERS shows only "Solar".
    - The modal labels every company "Market Leader".
17. **BESS project detail incomplete for prompt Q2.** Size / client type / year are given only sometimes. Examples with no size: Solarvest "Multiple C&I BESS", Progressture, Cenergi, Pekat.
18. **Lake Kenyir JV.** Sunview has "40% lead share", Cypark "60% JV lead"; both are called lead. Value (RM 1.96B), size (595 MWac) and date (Apr 2026) are consistent across records.
19. **Margins.**
    - Chart 4 gross values are midpoints of the text ranges (30.0 of 25–35; 18.5 of 15–22; 8.6 ≈ 6.5–10.8). The net values 12.5 and 7.5 appear nowhere in the text. BoP net −2.5 differs from Founder's −4.7% (pre-tax loss) in the table.
    - Sunview's 12.0%–16.0% GM is below the stated utility main-contracting tier (15%–22%).
    - Pekat's "~30% GP margins in ELP" is a segment figure, vs 25.2%–27.0% company-level.
    - The "Audited Financial Benchmarks" table gives no financial year or period. Cheeding is not in the Top 15.
20. **Payment milestones.** The ranges sum to 80%–110%, so only some combinations total 100%.
21. **Unsourced headline numbers.** RM 13B–23B order-book flow (no breakdown); "2.5 GW added in '25"; "30% to 70% of C&I monthly power bills"; silver +167% / copper +40%; EVC "First Zero-Capex BESS programme" (no date).
22. **Design comments overstate interactivity.** The comments promise a "Capacity tier toggle" on the solar chart, an "Interactive comparison tool" for the 8 providers and an "Interactive milestone timeline". All three are static in the code. The comment also describes the tax choice as "GITA 100% vs pre-tax", but there is a 60% option too. Chart.js is loaded unversioned.

### Prompt coverage (research/round2_research_prompts.md #3 "Competitors and pricing")

1. **Price ranges** (solar EPCC at 100 kWp / 500 kWp / 1 MWp / 3 MWp; BESS 200–500 kWh cabinets and 2–5 MWh containers; O&M): **answered, but unsourced.** Section 1 lead text, Solar EPCC table, O&M table, Charts 1–2. No links or dates per figure, and the chart and calculator point values differ from the table (notes 8–9).
2. **Top 15 companies by MW** (listed/private, MW, BESS projects with size/client/year, business models, MD/EMS product): **mostly answered.** Section 2 and the Embedded data tables cover all 15 with every field. Weak spots: MW basis is mixed and ranking basis unstated (notes 12–13), BESS project size/client/year is incomplete (note 17), no links.
3. **Zero-capex / shared-savings BESS providers and terms** (contract length, savings split, guarantees): **partly answered.** Section 3 has 8 provider cards and the 15/85 box. All 8 give contract length. Savings split is given for Plus Xnergy (15%), EVC (15%–30%) and ERS (25%–40% below TNB); Solarvest says only "fee lower than MD savings"; UniBess, Cenergi, Kawan and XPERTS.NRG give none. Guarantees are given only for UniBess (capped LDs on availability, Year-10 capacity, RTE) and ERS (zero-cost mid-life inverter replacement); Plus Xnergy says "100% funded CAPEX & O&M". Nothing is sourced.
4. **EPCC margins, payment terms, worst price competition:** **answered, but unsourced.** Section 4 lead text, Chart 4, listed-EPCC table, payment milestones, and the competition / high-moat boxes.
5. **Overall instruction to link every figure:** **not met.** There are no links (note 1).
