---
id: R9
title: "Malaysia BESS Load Profile & Tariff Analysis | RP4 Framework (Malaysia BESS RP4 Analyzer)"
source_file: malaysia_bess_load_profile_analysis_commercial_calculator.html
source_modified: 2026-10-23 16:07
generated_by: AI research tool (interactive HTML dashboard, Tailwind + Chart.js + FontAwesome)
research_prompt: "#4 Load profiles and target industries (research/round2_research_prompts.md)"
stated_scope: "Medium Voltage Load Profiles & Commercial Feasibility. An 'interactive executive decision-support platform designed for energy managers, BESS developers, and corporate CFOs evaluating BESS under TNB's RP4 tariff framework'."
stated_sources: "Footer: 'Data Source: Tenaga Nasional Berhad (TNB) & Industry Case Studies'; 'Based on RP4 Medium Voltage Framework (Effective 1 July 2025 – 31 Dec 2027) & Energy Commission Guidelines.' No links."
as_of: "No report as-of date. Dates stated: RP4 effective 1 July 2025 (framework 2025–2027, to 31 Dec 2027); simulator AFA constant labelled 'Oct 2026 rate'; AFA chart Oct 2026 actual and Nov 2026 – Jan 2027 forecasts."
sections: ["Header & navigation (6 tabs)", "1. RP4 Architecture: Regulatory Period 4 (RP4) Tariff Restructuring & Peak Demand Economics", "2. Sector Load Profiles: Industry Load Profile & BESS Feasibility Evaluator", "3. Post-Solar Bill Simulator: Interactive Tariff & Post-Solar MD Distortion Simulator", "4. Case Studies & Payback: Empirical BESS Case Studies & ROI Benchmarks", "5. Industrial Parks & Hubs: Peninsular Malaysia Geographic Density & Target Industrial Parks", "6. GTM & Associations: Go-To-Market Ecosystem & Decision-Maker Engagement", "Footer"]
extraction: complete
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# R9 — Malaysia BESS Load Profile & Tariff Analysis (RP4 Analyzer)

> Faithful, complete markdown extract of `malaysia_bess_load_profile_analysis_commercial_calculator.html`. Body content comes only from the report. Extractor observations are confined to "Extraction notes" at the end.

## Key claims (index)

- BESS peak-shaving ROI "is dictated by load curve geometry": spiky loads with load factor LF < 0.60 "offer maximum BESS returns"; flat 24/7 loads with LF > 0.75 "require excessive storage capacity". (§2)
- 11 sectors rated (Embedded data E1). **Tier 1 (High):** Metal Stamping (LF 28%, score 95), Office Towers (LF 32%, 92), Food Processing (LF 42%, 90), Plastic Injection (LF 55%, 88). **Tier 2:** Shopping Malls (LF 52%, 78), Hotels & Resorts (LF 62%, 72), Hospitals (LF 72%, 60), Cold Storage (LF 68%, 55, "Conditional (Tier 2/3)"). **Flat / low fit:** Textiles & Dyeing (LF 78%, 40; dyeing plants spiky), E&E / Semiconductor (LF 85%, 25), Rubber Gloves (LF 88%, 15, "Unviable for Standalone BESS"). (§2, E1)
- "Post-RP4 MD Share" of the bill by sector runs from 59.5% (metal stamping) down to 32.5% (rubber gloves). (§2, E1; these equal the simulator's own outputs — see Extraction notes)
- Optimal BESS duration by sector: 1.0–1.5 h (stamping), 1.5–2.0 h (food, plastic injection), 2.0–2.5 h with PV (offices), 2.0–3.0 h (malls "Evening Tail", hotels); cold storage "Pre-cooling or Solar + BESS"; semiconductor "UPS / Solar ATAP Only". (E1)
- RP4 MV ToU demand charge RM97.06/kW (RM30.19 capacity + RM66.87 network); RM98.61/kW including 1.6% KWTBB; MV General RM89.27/kW (RM90.70 with KWTBB); legacy RP3 "~RM37.00–RM45.10/kW" → "+115% to +162%". (§1)
- Energy: MV ToU peak 31.32 / off-peak 27.23 sen/kWh (spread 4.09 sen, "Narrow"); MV General 29.83 sen flat; legacy RP3 peak 35.50–36.50 and off-peak 21.90–22.40 sen/kWh. Off-peak = 22:00–14:00 Mon–Fri plus "all weekends & public holidays". (§1)
- AFA (monthly, replaced 6-month ICPT): 3.61 sen/kWh Oct 2026; forecasts 4.27 (Nov 2026), 4.46 (Dec 2026), 7.59 (Jan 2027). (§1, Charts 2)
- "Post-Solar Load Factor Distortion Effect": rooftop solar without storage cuts kWh but not MD, so "the MD share of the electricity bill surges from ~55% up to ~70%". (§3)
- Simulator default (metal stamping, 1,000 kW, LF 28%, 45% peak-window kWh, 500 kWp solar, 250 kW shaved): savings RM24,265/month (RM291,180/year) = 250 kW × RM97.06. (§3, C1)
- 7 case studies (E2): Livoltek 125 kW / 261 kWh, 89.99 kW shaved, RM9,000/month, 2.8–3.5 yrs with GITA; Plus Xnergy 1.5 MW / 3.0 MWh zero-capex EaaS, 3,900 → 2,422 kW, client nets RM21,520/month at RM82.50/kW for 15 years; Solarvest 1,000 kWp + 500 kW / 1,000 kWh, >650 kW shaved, RM712,000/yr, <2.5 yrs; Avera Energy 165 kW / 330 kWh + shift optimisation, 315 kW cut, RM58,945/month (25.7%); UniBess 500 kW / 1,044 kWh, 400 kW, RM38,824/month; HAPLT predictive controller trial 50 kW / 155 kWh, RM2,445/month; overseas CNC plant 250 kW / 515 kWh, 230 kW, ~RM295,000/yr, 2.1 yrs. (§4, E2)
- Tax shield: "100% GITA" (called "MIDA Tier 1") + "100% Capital Allowance" at 24% → "Net ~48% CAPEX Subsidy", payback 5–6 yrs → "2.5–3.5 years". (§4)
- Geography: "over 500 industrial parks and 22 Free Industrial Zones (FIZs)"; Selangor 4,000+ factories and Johor 2,500+ hold the Tier 1 spiky-load plants; Penang fabs are flat 24/7. 9 clusters with factory-count ranges (E3). (§5)
- GTM: two personas (technical specifiers — REEM / CEM / facility managers; financial approvers — CFO / MD); associations FMM (3,500+ members), MPMA (800+ plants), MAREMA & MAESCO, IEM, MSIA, PPK / MAH / APHM with named events. (§6)
- Execution framework: target post-solar 1–2 shift MV factories (LF 0.28–0.55) in Shah Alam, Klang, Meru, Tebrau, Senai; get 12 months of 15/30-minute data "from myTNB portal"; size PCS for top 20%–35% peak clipping with 1.3×–1.5× energy buffer; offer capex + GITA (~2.5 yr payback) alongside zero-capex EaaS. (§6)

## Report purpose and design notes (from HTML comments)

Palette comment: "Chosen Palette: Warm Neutral Slate & Emerald Energy".

The "Application Structure Plan" comment says the application is "structured as an interactive executive decision-support platform designed for energy managers, BESS developers, and corporate CFOs evaluating BESS under TNB's RP4 tariff framework":

1. Executive Header & Navigation: Tabbed navigation with smooth section switching.
2. RP4 Tariff Architecture & Overview: Summary metrics cards and direct comparison between legacy RP3, RP4 MV General, and RP4 MV ToU structures.
3. Sector Load Profile & Suitability Evaluator: Interactive comparison matrix of 11 industries with sector filtering (Tier 1 Targets vs. Flat Loads), radar/bar visualization, and load profile specs.
4. Tariff & Post-Solar Load Factor Distortion Simulator: A real-time bill calculator allowing users to simulate their peak demand, load factor, and solar PV capacity to visualize how solar skyrockets the MD share of bills and how BESS mitigates it.
5. Empirical Case Studies Explorer: Searchable and filterable gallery of 9 published BESS case studies (Malaysia and global) featuring system specs, kW shaved, savings, tax shields, and payback.
6. Geographic Heatmap & Industrial Cluster Directory: Interactive regional mapping of 500+ industrial parks across Selangor, Johor, Penang, and Kedah with factory counts and target density.
7. Ecosystem Engagement & GTM Roadmap: Direct mapping of industry associations (FMM, MPMA, MSIA, MAREMA, IEM), regulatory triggers (EECA, ISO 50001, GITA tax shields), and execution roadmaps.

The "Visualization & Content Choices" comment lists:

- Key Indicators: Responsive CSS cards with accent highlights for core rates (RM97.06/kW, 14:00-22:00 window).
- Load Factor vs. BESS Suitability Chart: Chart.js Bar + Line combo chart showing Load Factor vs MD Share and Suitability Score (NO SVG).
- Dynamic Bill Simulator Chart: Chart.js Doughnut & Stacked Bar chart dynamically updated via JS logic based on user slider inputs.
- Geographic Cluster Visualizer: Chart.js Horizontal Bar Chart categorizing industrial park factory densities by region.
- Case Studies: Dynamic JS-filtered card list with modal/expand details.
- Icons: FontAwesome CSS web font classes (FontAwesome CDN) to prevent raw inline SVGs.
- Confirmed: NO SVG markup or Mermaid JS incorporated.

A further comment states: "CONFIRMATION: NO SVG graphics used. NO Mermaid JS used."

## Header and navigation

- Page title: "Malaysia BESS Load Profile & Tariff Analysis | RP4 Framework".
- Title block: "Malaysia BESS RP4 Analyzer" — "Medium Voltage Load Profiles & Commercial Feasibility".
- Badges: "RP4 Effective: 1 July 2025"; "Peak Window: 14:00–22:00".
- Tabs (only one section is visible at a time; `switchTab()`): "RP4 Architecture" (overview, default), "Sector Load Profiles", "Post-Solar Bill Simulator", "Case Studies & Payback", "Industrial Parks & Hubs", "GTM & Associations".

## 1. RP4 Architecture — Regulatory Period 4 (RP4) Tariff Restructuring & Peak Demand Economics

Text: On 1 July 2025, Tenaga Nasional Berhad (TNB) and Suruhanjaya Tenaga introduced the RP4 tariff framework (2025–2027), replacing legacy commercial/industrial tariffs (C1, C2, E1, E2, E3) with a standardized Medium Voltage (MV) schedule. This reform drastically shifted cost recovery from volumetric energy charges (sen/kWh) to fixed capacity and network demand charges (RM/kW), creating a high-stakes environment for facilities with spiky load profiles.

### 1.1 Metric cards

| Card | Value | Sub-label |
|---|---|---|
| Peak Demand Rate (MV ToU) | RM97.06 / kW / mo | RM98.61/kW incl. 1.6% KWTBB (+115% to +162% vs RP3) |
| Weekday Peak Window | 14:00 – 22:00 | Mon–Fri (8 hrs, extended 4 hrs past sunset) |
| Energy Arbitrage Spread | 4.09 sen / kWh | Peak 31.32 sen vs Off-Peak 27.23 sen (Narrow) |
| Automatic Fuel Adjustment (AFA) | +3.61 to +7.59 | sen/kWh monthly monthly variable surcharge |

### 1.2 Tariff structure table

| Tariff Element | Legacy RP3 (E1/E2 Ref) | RP4 MV General | RP4 MV Time-of-Use (MV ToU) | Billing & Operational Impact |
|---|---|---|---|---|
| Peak Energy Charge | 35.50–36.50 sen/kWh | 29.83 sen/kWh (Flat) | 31.32 sen/kWh | Billed per kWh drawn 14:00–22:00 Mon–Fri |
| Off-Peak Energy Charge | 21.90–22.40 sen/kWh | 29.83 sen/kWh (Flat) | 27.23 sen/kWh | Billed 22:00–14:00 Mon–Fri, all weekends & public holidays |
| Capacity Charge (Gen) | Bundled in MD | RM29.43/kW | RM30.19/kW | Highest 30-min average kW inside peak window |
| Network Charge (Grid) | Bundled in MD | RM59.84/kW | RM66.87/kW | Grid substation & cable availability charge |
| **Combined Base MD Charge** | ~RM37.00–RM45.10/kW | RM89.27/kW | **RM97.06/kW** | Surge of +115% to +162% in demand charges |
| Effective MD (+1.6% KWTBB) | ~RM37.59–RM45.82/kW | RM90.70/kW | RM98.61/kW | Includes Renewable Energy Fund surcharge |

### 1.3 Charts in this section

- "Maximum Demand Charge Surge (RP3 vs. RP4)" — "Comparing monthly cost per 1,000 kW Maximum Demand across tariff evolution" (Charts, Chart 1).
- "AFA Surcharge Forecast Trajectory (sen/kWh)" — "Monthly Automatic Fuel Adjustment volatility replacing static 6-month ICPT" (Charts, Chart 2).

## 2. Sector Load Profiles — Industry Load Profile & BESS Feasibility Evaluator

Text: BESS peak shaving ROI is dictated by load curve geometry. High-power spiky loads with low load factors (`$LF < 0.60$`) offer maximum BESS returns, whereas flat 24/7 loads (`$LF > 0.75$`) require excessive storage capacity.

Filter buttons (C2): "All (11 Sectors)" (default), "Tier 1 Target (High)", "Tier 2 (Moderate)", "Tier 3/4 (Flat / Low Fit)".

Chart: "Load Factor (`$LF$`) vs. BESS Peak Shaving Suitability Score" — "Notice the clear inverse relationship: lower load factor directly correlates with higher BESS financial fit and higher MD share of electricity bills." (Charts, Chart 3).

Sector cards are rendered from the JS array `sectorData` (all 11 rows in Embedded data tables, E1). Each card shows: name; suitability badge; "Load Factor (`$LF$`)" as a whole percentage; "Post-RP4 MD Share" %; "Shift Pattern:"; "Peak Window Behavior (14:00–22:00):"; "Primary Spike Drivers:"; "Opt. BESS Duration:".

Summary of the 11 cards:

| Sector | Suitability | LF | Post-RP4 MD share | Opt. BESS duration |
|---|---|---|---|---|
| Metal Stamping | High (Tier 1) | 28% | 59.5% | 1.0 – 1.5 Hours (0.5C – 1C) |
| Office Towers | High (Tier 1) | 32% | 56.3% | 2.0 – 2.5 Hours (with PV) |
| Food Processing | High (Tier 1) | 42% | 49.7% | 1.5 – 2.0 Hours |
| Plastic Injection | High (Tier 1) | 55% | 43.1% | 1.5 – 2.0 Hours |
| Shopping Malls | Moderate-High (Tier 2) | 52% | 44.1% | 2.0 – 3.0 Hours (Evening Tail) |
| Hotels & Resorts | Moderate-High (Tier 2) | 62% | 40.2% | 2.0 – 3.0 Hours |
| Cold Storage | Conditional (Tier 2/3) | 68% | 38.2% | Pre-cooling or Solar + BESS |
| Hospitals | Moderate (Tier 2) | 72% | 36.8% | 1.5 – 2.0 Hours + Microgrid |
| Textiles & Dyeing | Low (Flat) / High (Dyeing) | 78% | 35.1% | Poor (Weaving) / Tier 1 (Dyeing) |
| E&E / Semiconductor | Poor (Standalone MD) | 85% | 33.2% | UPS / Solar ATAP Only |
| Rubber Gloves | Poor (Flat 24/7) | 88% | 32.5% | Unviable for Standalone BESS |

## 3. Post-Solar Bill Simulator — Interactive Tariff & Post-Solar MD Distortion Simulator

Text: **The Post-Solar Load Factor Distortion Effect:** When a factory installs rooftop solar PV without storage, it reduces volumetric kWh consumption during sunny hours. However, because a single overcast 30-minute transient or late afternoon run (17:00–22:00) sets the full monthly Maximum Demand, **the MD share of the electricity bill surges from ~55% up to ~70%**. Use this tool to simulate your facility's bill and evaluate BESS peak clipping.

Control panel heading: "Facility Operational Parameters". Inputs (full detail in C1): "Preset Sector Profile"; "Peak Demand (`$P_{\text{max}}$`)"; "Monthly Load Factor (`$LF$`)"; "Peak Window kWh Ratio (`$\alpha$`)"; checkbox "Enable Rooftop Solar PV System" with "Solar PV Capacity"; checkbox "Deploy BESS Peak Shaving System" with "Target Demand Cut (kW Shaved)".

Output cards (HTML placeholders; replaced on load — see C1):

| Card | Placeholder value | Placeholder sub-line |
|---|---|---|
| Total Electricity Bill | RM 163,144 | Pre-Solar Baseline |
| MD Bill Share (%) | 59.5 % | Low Load Factor Exposure |
| Monthly BESS MD Savings | RM 24,265 | RM 291,180 / year |

Chart: "Monthly Bill Composition Breakdown (RM)" (Charts, Chart 5).

Insight banner, "Key Financial Takeaway:" (static text, never updated by the code): "Installing rooftop solar cuts volumetric energy charges but leaves the RM97.06/kW peak demand charge exposed. Notice how adding solar increases MD share from 59.5% to 69.4% of your total bill, making BESS peak shaving the single highest-return retrofit!"

## 4. Case Studies & Payback — Empirical BESS Case Studies & ROI Benchmarks

Text: Published performance data from C&I deployments across Peninsular Malaysia and benchmark ToU markets following the RP4 tariff restructuring.

Filter dropdown (C3): "All Deployment Types" (default), "Malaysia RP4 Projects", "Zero-Capex EaaS / Leases", "Comparable International ToU".

Case cards are rendered from the JS array `caseStudiesData` (7 rows, all fields in Embedded data tables, E2). Each card shows location badge, site type, title, details, "System Hardware:", "Demand Cut:", "Verified Savings:" and "Payback / Financials:".

| # | Case | Location | System | Demand cut | Savings | Payback |
|---|---|---|---|---|---|---|
| 1 | Livoltek C&I Evening Peak Suppression | Malaysia (RP4 MV ToU) | 125 kW / 261 kWh LFP (Liquid-cooled) | 89.99 kW shaved | RM 9,000 / month (>RM 95,000/yr) | 2.8 – 3.5 Years (with MIDA GITA) |
| 2 | Plus Xnergy Multi-MW Zero-Capex EaaS | Malaysia (RP4 MV ToU) | 1.5 MW / 3.0 MWh LFP Class | 1,478 kW shaved (3,900 kW → 2,422 kW) | Net client savings: RM 21,520 / month | Immediate (0-Yr Payback; EaaS Lease) |
| 3 | Solarvest Solar ATAP + BESS Reference Site | Malaysia (RP4 MV ToU) | 1,000 kWp PV + 500 kW / 1,000 kWh BESS | >650 kW shaved (>65% MD Cut) | RM 712,000 / year gross savings | <2.5 Years (Gross RM2.4M less RM920k GITA) |
| 4 | Avera Energy MV Factory Transition | Malaysia (MV General → ToU) | Rooftop Solar + 165 kW / 330 kWh BESS | 315 kW Total MD Cut (165 kW BESS) | RM 58,945 / month (25.7% total bill cut) | 3.0 – 4.2 Years integrated payback |
| 5 | UniBess C&I Modular Peak Shaving | Malaysia (RP4 MV ToU) | 500 kW / 1,044 kWh (4 x 125kW Cabinets) | 400 kW shaved (Capped at 200 kW target) | RM 38,824 / month (RM 465,888 / year) | 2.5 – 3.5 Years simple payback |
| 6 | Predictive HAPLT Controller Field Validation | Malaysia (Industrial Feeder) | 50 kW / 155 kWh Li-ion (139.5 kWh usable) | 89% Average MD Reduction Factor | RM 2,445 / month verified in field | Academic Field Validation Trial |
| 7 | Precision CNC Machining Plant | Comparable ToU Market | 250 kW / 515 kWh LFP BESS | 230 kW shaved (780 kW → 550 kW) | US$ 5,520 / mo (~RM 295,000 / year) | 2.1 Years simple payback |

### 4.1 The MIDA Tier 1 Green Investment Tax Allowance (GITA) Shield

| Box | Text |
|---|---|
| 100% GITA Tax Allowance | Classified as a Tier 1 Green Asset, qualifying for 100% Investment Tax Allowance offset against up to 70% of statutory income over 3–5 years. |
| 100% Capital Allowance | Enables 100% capital depreciation allowance against corporate income tax (24% standard corporate rate). |
| Net ~48% CAPEX Subsidy | Combined tax shields effectively subsidize up to 48% of gross project capital expenditure, reducing simple payback from 5–6 years down to **2.5–3.5 years**! |

## 5. Industrial Parks & Hubs — Peninsular Malaysia Geographic Density & Target Industrial Parks

Text: Peninsular Malaysia features over 500 industrial parks and 22 Free Industrial Zones (FIZs). Target industries are sharply segregated by state: Selangor (Klang Valley) and Johor (Iskandar) concentrate the densest clusters of Tier 1 spiky-load target plants, whereas Penang concentrates flat 24/7 semiconductor fabs.

Chart: "Estimated Industrial Factory Density by State/Region" — "Concentration of Medium Voltage commercial and industrial facilities" (Charts, Chart 4).

Region cards:

| Card | Text |
|---|---|
| Selangor / Klang Valley (Prime Target Hub) | Over 4,000+ factories across Shah Alam, Klang, Meru, Telok Gong, Bangi, and Kajang. Exceptional density of 1–2 shift metal stamping, plastic injection, food manufacturing, and cold chain logistics. |
| Johor Southern Corridor (Rapid Growth) | 2,500+ factories concentrated in Tebrau I-IV, Pasir Gudang, Senai, SILC, and Mount Austin. Heavy plastic injection, metal fabrication, oleochemicals, and packaging exporters. |
| Penang & Kedah Northern Corridor | Bayan Lepas, BKIP, Perai, and Kulim KHTP. Fabs/OSATs operate flat 24/7 loads (target for UPS + Solar ATAP); precision automation vendors in BKIP/Perai are Tier 1 peak shaving targets. |

Directory table (columns "Region / State", "Major Industrial Cluster / Park", "Est. Factory Count", "Dominant Sector Profiles", "BESS Opportunity Rating") is rendered from the JS array `geoParksData` — 9 rows, reproduced in Embedded data tables, E3. Ratings containing "Prime" are highlighted.

## 6. GTM & Associations — Go-To-Market Ecosystem & Decision-Maker Engagement

Text: BESS origination requires engaging two key personas: **Technical Specifiers** (Registered Electrical Energy Managers - REEM, Certified Energy Managers, Facility Managers) and **Financial Approvers** (CFO, Managing Director). Reaching these stakeholders is catalyzed by Malaysia's **Energy Efficiency and Conservation Act (EECA)** and ISO 50001 mandatory requirements.

### 6.1 Association & event matrix

| Association | Sub-label | Description | Key Touchpoints & Events |
|---|---|---|---|
| FMM (Federation of Malaysian Mfrs) | 3,500+ Member Factories | Malaysia's primary industrial body with active state committees in Selangor, Penang, and Johor. | FMM Energy Efficiency & Conservation Conference; FMM ISO 50001 EnMS Workshops; State Branch ESG Seminars. |
| MPMA (Plastics Mfrs Assoc) | 800+ Plastics & Injection Plants | Direct access to factory owners hit with 40%+ MD bill shares from heater bands and chillers. | MPMA Technical Seminars on RP4 Tariff Mitigation; Mould & Die Pavilion at MIMF (MITEC KL). |
| MAREMA & MAESCO | ST-Certified REEMs & ESCOs | The professional guild of registered energy managers auditing 15-min load profiles. | Energy Transition Conference (ETCON by TNB); MAREMA Technical Dialogues & CPD Hours Workshops. |
| IEM (Institution of Engineers) | Electrical & Building Engineers | Official training body for the 5-Day IEM Energy Manager Training Course (EMTC) for REEM certification. | CPD-Accredited Technical Talks at Wisma IEM (Petaling Jaya) and Regional Branches (Penang, JB, Ipoh). |
| MSIA (Semiconductor Assoc) | E&E, Precision & OSAT Vendors | Reaches VPs of Operations and Facility Directors at MNCs and local precision machining suppliers. | SEMICON Southeast Asia; MSIA Northern Corridor C-Suite & Facility Engineering Roundtables. |
| Commercial (PPK / MAH / APHM) | Malls, Hotels, Private Hospitals | Reaches Asset Managers, Chief Engineers, and REITs managing large MV C1/C2 commercial properties. | IGEM (International Greentech & Eco Products Expo at KLCC); BMAM / PPK Facility Summits. |

### 6.2 Strategic Commercial Execution Framework

| Step | Text |
|---|---|
| 1. Target Identification | Focus on post-solar 1–2 shift MV factories (`$LF = 0.28\text{--}0.55$`) in Shah Alam, Klang, Meru, Tebrau, and Senai. |
| 2. Interval Data Audit | Request 12 months of 15/30-minute load profile data from myTNB portal to map 14:00–22:00 peak pyramid curves. |
| 3. Dynamic Sizing | Size PCS (kW) for top 20%–35% peak clipping with a 1.3`$\times$`–1.5`$\times$` energy buffer for 90% DoD and round-trip efficiency. |
| 4. Bifurcated Offer | Present CAPEX purchase with 100% MIDA GITA tax shield (~2.5 yr payback) alongside Zero-Capex EaaS leasing. |

## Footer

- "Malaysia BESS Load Profile & Tariff Feasibility Platform"
- "Based on RP4 Medium Voltage Framework (Effective 1 July 2025 – 31 Dec 2027) & Energy Commission Guidelines."
- "Data Source: Tenaga Nasional Berhad (TNB) & Industry Case Studies"

## Charts

### Chart 1 — tariffCompareChart

- Location: §1, "Maximum Demand Charge Surge (RP3 vs. RP4)".
- Type: bar (Chart.js), single dataset, legend hidden; y axis begins at zero.
- Series: "MD Charge per 1,000 kW Peak (RM/month)".

| Label | RM/month per 1,000 kW |
|---|---|
| Legacy RP3 (E1/E2) | 41000 |
| RP4 MV General | 89270 |
| RP4 MV ToU (Base) | 97060 |
| RP4 MV ToU (+1.6% KWTBB) | 98610 |

### Chart 2 — afaTrendChart

- Location: §1, "AFA Surcharge Forecast Trajectory (sen/kWh)".
- Type: line, filled, legend hidden; y axis begins at zero.
- Series: "AFA Monthly Surcharge (sen/kWh)".

| Label | sen/kWh |
|---|---|
| Oct 2026 | 3.61 |
| Nov 2026 (Fcst) | 4.27 |
| Dec 2026 (Fcst) | 4.46 |
| Jan 2027 (Fcst) | 7.59 |

### Chart 3 — sectorSuitabilityChart

- Location: §2. Type: bar + line combo; legend at bottom; y axis 0 to max 100.
- Series: "Load Factor (%)" (bars, = loadFactor × 100) and "BESS Suitability Score (1-100)" (line).
- Labels and data come from `sectorData` (E1):

| Sector | Load Factor (%) | Suitability Score |
|---|---|---|
| Metal Stamping | 28 | 95 |
| Office Towers | 32 | 92 |
| Food Processing | 42 | 90 |
| Plastic Injection | 55 | 88 |
| Shopping Malls | 52 | 78 |
| Hotels & Resorts | 62 | 72 |
| Cold Storage | 68 | 55 |
| Hospitals | 72 | 60 |
| Textiles & Dyeing | 78 | 40 |
| E&E / Semiconductor | 85 | 25 |
| Rubber Gloves | 88 | 15 |

The comment promises "Load Factor vs MD Share and Suitability Score"; MD share is not plotted.

### Chart 4 — geoDistributionChart

- Location: §5. Type: horizontal bar; legend hidden; x axis begins at zero.
- Series: "Estimated Medium Voltage Factory Density".

| Label | Value |
|---|---|
| Selangor (Klang Valley) | 4200 |
| Johor (Southern) | 2600 |
| Penang & Kedah | 1400 |
| Central Spine (Melaka/NS/Perak) | 1500 |

### Chart 5 — simBillBreakdownChart

- Location: §3. Type: horizontal stacked bar, one category "Bill Component Breakdown"; legend at bottom. Rebuilt on every simulator update.
- Series: "Maximum Demand Charge (RM)", "Peak Energy Charge (RM)", "Off-Peak Energy Charge (RM)", "AFA Fuel Surcharge (RM)" (retail fee not plotted). Data = the C1 outputs.

At default inputs (computed, see C1): MD RM72,795; peak energy RM21,836.30; off-peak energy RM21,615.17; AFA RM5,382.51.

## Calculators and interactive logic

### C1 — Interactive Tariff & Post-Solar MD Distortion Simulator

Location: §3 (`applySimPreset()` / `updateSimulation()`); runs once on page load.

Inputs:

| Input | Type | Default | Range / options |
|---|---|---|---|
| Preset Sector Profile — `simPreset` | dropdown | metal (selected) | see preset table |
| Peak Demand (`$P_{\text{max}}$`) — `simPeakDemand` | range | 1000 (label "1,000 kW") | min 200, max 5000, step 100 |
| Monthly Load Factor (`$LF$`) — `simLoadFactor` | range | 0.28 (label "28 %") | min 0.15, max 0.90, step 0.01 |
| Peak Window kWh Ratio (`$\alpha$`) — `simPeakRatio` | range | 0.45 (label "45 %") | min 0.15, max 0.65, step 0.01 |
| Enable Rooftop Solar PV System — `simHasSolar` | checkbox | checked | shows/hides solar slider |
| Solar PV Capacity — `simSolarCapacity` | range | 500 (label "500 kWp") | min 100, max 3000, step 50 |
| Deploy BESS Peak Shaving System — `simHasBess` | checkbox | checked | shows/hides BESS slider |
| Target Demand Cut (kW Shaved) — `simBesskW` | range | 250 (label "250 kW (25%)") | min 50, max 1500, step 25 |

Preset dropdown options and what `applySimPreset()` sets:

| Value | Label | Peak Demand | LF | α |
|---|---|---|---|---|
| custom | Custom Configuration | (no change) | (no change) | (no change) |
| metal (default) | Metal Stamping (LF: 28%, Peak: 1,000 kW) | 1000 | 0.28 | 0.45 |
| office | Office Tower (LF: 32%, Peak: 1,000 kW) | 1000 | 0.32 | 0.42 |
| food | Food Processing (LF: 42%, Peak: 1,000 kW) | 1000 | 0.42 | 0.40 |
| plastic | Plastic Injection (LF: 55%, Peak: 1,000 kW) | 1000 | 0.55 | 0.35 |
| mall | Shopping Mall (LF: 52%, Peak: 1,000 kW) | (no branch — no change) | (no change) | (no change) |
| glove | Rubber Gloves (LF: 88%, Peak: 1,000 kW - Flat) | 1000 | 0.88 | 0.24 |

Constants ("Billing Parameters (RP4 MV ToU)"): mdRate 97.06 RM/kW; peakEnergyRate 0.3132 RM/kWh; offPeakEnergyRate 0.2723 RM/kWh; afaRate 0.0361 RM/kWh ("Oct 2026 rate"); retailFee 200 RM/month; 720 hours/month; solar yield 105 kWh/kWp/month ("~105 kWh/kWp/month yield"); solar split 0.4 to peak kWh and 0.6 to off-peak kWh.

Logic (faithful to the JS):

```
P   = peak demand (kW); LF = load factor; a = peak-window kWh ratio
S   = solar kWp if solar checked else 0
B   = kW shaved if BESS checked else 0

totalMonthlykWh = P * 720 * LF
peakkWh         = totalMonthlykWh * a
offPeakkWh      = totalMonthlykWh * (1 - a)

solarMonthlykWh = S * 105
netkWh          = max(0, totalMonthlykWh - solarMonthlykWh)
netPeakkWh      = max(0, peakkWh - solarMonthlykWh * 0.4)
netOffPeakkWh   = max(0, offPeakkWh - solarMonthlykWh * 0.6)
                  # comment: solar "replaces volumetric off-peak & partial peak kWh, but leaves peak kW set"

billedMD        = max(0, P - B)               # solar never reduces MD

mdCharge            = billedMD * 97.06
peakEnergyCharge    = netPeakkWh * 0.3132
offPeakEnergyCharge = netOffPeakkWh * 0.2723
afaCharge           = netkWh * 0.0361
totalBill           = mdCharge + peakEnergyCharge + offPeakEnergyCharge + afaCharge + 200

mdSharePct          = mdCharge / totalBill * 100
monthlyBessSavings  = B * 97.06               # annual = x 12

labels: "Total Electricity Bill" = "RM " + round(totalBill); "MD Bill Share (%)" = mdSharePct to 1 decimal;
        "Monthly BESS MD Savings" = "RM " + round(savings); "RM " + round(savings * 12) + " / year";
        BESS label = B + " kW (" + round(B / P * 100) + "%)"
sub-lines: solar and no BESS -> "With Rooftop Solar PV" / "Distortion Active (High MD Share)"
           BESS (with or without solar) -> "With Solar + BESS Peak Shaving" / "MD Clipped via BESS"
           neither -> "Pre-Solar Baseline" / "Unmitigated Grid Baseline"
```

Triggers: every slider "input", checkbox "change"; preset "change" calls `applySimPreset()` then `updateSimulation()`. Numbers use `toLocaleString()`.

Outputs at default inputs, as shown after load (computed by running the code logic: metal preset, 1,000 kW, LF 0.28, α 0.45, solar on 500 kWp, BESS on 250 kW):

| Quantity | Computed by code | Placeholder in HTML |
|---|---|---|
| totalMonthlykWh / peak / off-peak | 201,600 / 90,720 / 110,880 | – |
| solarMonthlykWh / netkWh | 52,500 / 149,100 | – |
| netPeakkWh / netOffPeakkWh | 69,720 / 79,380 | – |
| billedMD | 750 kW | – |
| mdCharge | RM 72,795 | – |
| peakEnergyCharge / offPeakEnergyCharge / afaCharge | RM 21,836.30 / RM 21,615.17 / RM 5,382.51 | – |
| Total Electricity Bill | RM 121,829 | RM 163,144 |
| Sub-line | With Solar + BESS Peak Shaving | Pre-Solar Baseline |
| MD Bill Share | 59.8 % | 59.5 % |
| MD sub-line | MD Clipped via BESS | Low Load Factor Exposure |
| Monthly BESS MD Savings | RM 24,265 | RM 24,265 |
| Annual | RM 291,180 / year | RM 291,180 / year |
| BESS label | 250 kW (25%) | 250 kW (25%) |

Scenarios at the default metal inputs (computed):

| Scenario | Bill | MD share | MD charge | BESS savings |
|---|---|---|---|---|
| No solar, no BESS (baseline) | RM 163,144 | 59.5 % | RM 97,060 | RM 0 |
| Solar 500 kWp only | RM 146,094 | 66.4 % | RM 97,060 | RM 0 |
| BESS 250 kW only | RM 138,879 | 52.4 % | RM 72,795 | RM 24,265 |
| Solar + BESS (default) | RM 121,829 | 59.8 % | RM 72,795 | RM 24,265 |

Each preset at 1,000 kW with the default 500 kWp solar and 250 kW BESS settings (computed):

| Preset | Baseline bill / MD share | Solar-only bill / MD share | Solar + BESS bill / MD share |
|---|---|---|---|
| metal (LF 0.28, α 0.45) | RM 163,144 / 59.5 % | RM 146,094 / 66.4 % | RM 121,829 / 59.8 % |
| office (0.32, 0.42) | RM 172,273 / 56.3 % | RM 155,223 / 62.5 % | RM 130,958 / 55.6 % |
| food (0.42, 0.40) | RM 195,467 / 49.7 % | RM 178,418 / 54.4 % | RM 154,153 / 47.2 % |
| plastic (0.55, 0.35) | RM 225,055 / 43.1 % | RM 208,005 / 46.7 % | RM 183,740 / 39.6 % |
| glove (0.88, 0.24) | RM 298,882 / 32.5 % | RM 281,832 / 34.4 % | RM 257,567 / 28.3 % |

Edge cases (computed): 200 kW peak with 1,500 kW shaved and 500 kWp solar → bill RM 200, MD share 0.0 %, "Monthly BESS MD Savings" RM 145,590 (RM 1,747,080 / year), label "1500 kW (750%)". 200 kW, LF 0.15, 3,000 kWp solar, no BESS → all energy charges 0 (solar 315,000 kWh vs 21,600 kWh load, no export credit), bill RM 19,612, MD share 99.0 %. Maximum sliders (5,000 kW, LF 0.90, α 0.65, 3,000 kWp, 1,500 kW) → bill RM 1,322,962, MD share 25.7 %, savings RM 145,590. Minimum sliders (200 kW, LF 0.15, α 0.15, 100 kWp, 50 kW) → net peak kWh clamps to 0, bill RM 18,444, MD share 78.9 %, savings RM 4,853.

### C2 — Sector filter

Location: §2 (`filterSectors(tier)` / `renderSectorGrid()`). Buttons: 'all' → all 11 rows of E1; 'tier1' → Metal Stamping, Office Towers, Food Processing, Plastic Injection; 'tier2' → Shopping Malls, Hotels & Resorts, Cold Storage, Hospitals; 'poor' ("Tier 3/4 (Flat / Low Fit)") → Textiles & Dyeing, E&E / Semiconductor, Rubber Gloves. The active button is highlighted. Card badge colour: emerald (tier1), amber (tier2), rose (poor). The chart (Chart 3) does not change with the filter.

### C3 — Case-study filter

Location: §4 (`filterCaseStudies()`). 'all' → all 7 rows of E2; 'malaysia' → Livoltek, Solarvest, Avera, UniBess, HAPLT; 'eaas' → Plus Xnergy; 'overseas' → Precision CNC Machining Plant. No search box and no expand/modal, although the design comments promise both.

## Embedded data tables

### E1 — `sectorData` (11 rows; §2)

| id | name | tier | suitability | suitabilityScore | loadFactor | shiftPattern | mdShare | peakDrivers | peakBehavior | optDuration |
|---|---|---|---|---|---|---|---|---|---|---|
| metal | Metal Stamping | tier1 | High (Tier 1) | 95 | 0.28 | 1–2 Shifts (07:00–23:00) | 59.5 | Mechanical/servo press inrush (30-500 kW), spot welders, compressors. | Jagged spiky curve with sharp 30-60 min spikes at 14:00–17:00 and 19:00–21:00. | 1.0 – 1.5 Hours (0.5C – 1C) |
| office | Office Towers | tier1 | High (Tier 1) | 92 | 0.32 | Weekday Day (08:00–18:00) | 56.3 | Chiller max loading (solar heat gain) + 17:00–18:00 elevator egress surge. | Trapezoidal block that overlaps peak window only from 14:00 to 18:00; drops >75% after 18:00. | 2.0 – 2.5 Hours (with PV) |
| food | Food Processing | tier1 | High (Tier 1) | 90 | 0.42 | Batch / 2-Shift Operations | 49.7 | Batch ovens, fryers, retort sterilizers, blast freezers, CIP sanitation. | Stepped batch plateaus; 45–90 min afternoon spikes between 14:00 and 19:00. | 1.5 – 2.0 Hours |
| plastic | Plastic Injection | tier1 | High (Tier 1) | 88 | 0.55 | 2–3 Shifts (24/5 or 24/7) | 43.1 | Barrel heater bands during mould warm-up, hydraulic pumps, chillers. | Elevated baseload with sharp 30-45 min heater spikes; evening solar drop-off spike (18:00-22:00). | 1.5 – 2.0 Hours |
| mall | Shopping Malls | tier2 | Moderate-High (Tier 2) | 78 | 0.52 | Daily (10:00–22:00) | 44.1 | Central chiller plant, F&B cooking, tenant lighting, cinema audio. | Broad 12-hr plateau; solar clips midday, leaving a steep evening cliff at 17:30–21:30. | 2.0 – 3.0 Hours (Evening Tail) |
| hotel | Hotels & Resorts | tier2 | Moderate-High (Tier 2) | 72 | 0.62 | 24/7 Hospitality | 40.2 | Guestroom A/C check-in surge, heat-pump hot water, laundry, banquet HVAC. | Bimodal profile; pronounced late-afternoon/evening hump from 15:30 to 21:30. | 2.0 – 3.0 Hours |
| cold | Cold Storage | tier2 | Conditional (Tier 2/3) | 55 | 0.68 | 24/7 Temperature Controlled | 38.2 | High ambient condensing temp, warm product loading docks, defrost heaters. | High continuous baseload with a 15%–25% afternoon thermal hump at 14:00–18:00. | Pre-cooling or Solar + BESS |
| hospital | Hospitals | tier2 | Moderate (Tier 2) | 60 | 0.72 | 24/7 Clinical Operations | 36.8 | Afternoon OT chillers, CSSD steam autoclaves, MRI/CT diagnostic spikes. | High 24/7 baseload (60%) with daytime clinical plateau; value stacked with UPS/backup. | 1.5 – 2.0 Hours + Microgrid |
| textile | Textiles & Dyeing | poor | Low (Flat) / High (Dyeing) | 40 | 0.78 | 24/7 Continuous (Spinning/Weaving) | 35.1 | Air-jet looms, ring frames (or batch jet-dyeing autoclaves in dyeing plants). | Flat 24/7 plateau for spinning; spiky afternoon profile for batch dyeing houses. | Poor (Weaving) / Tier 1 (Dyeing) |
| semicon | E&E / Semiconductor | poor | Poor (Standalone MD) | 25 | 0.85 | 24/7 Continuous Cleanroom | 33.2 | Cleanroom MAUs/FFUs, ultra-pure water, chillers, IC test handlers. | Flat, high-utilization 24/7 baseload; <8% diurnal variation. Poor for standalone MD shaving. | UPS / Solar ATAP Only |
| glove | Rubber Gloves | poor | Poor (Flat 24/7) | 15 | 0.88 | 24/7 Continuous Dipping | 32.5 | Dipping line conveyors, oven circulation blowers, WWTP aerators. | Extremely flat 24/7 load across all shifts. Stopping a line ruins in-process latex. | Unviable for Standalone BESS |

(Icons, display only: fa-cubes-stacked, fa-building-user, fa-utensils, fa-bottle-water, fa-store, fa-hotel, fa-snowflake, fa-hospital, fa-shirt, fa-microchip, fa-hand-dots. Colours: emerald ×4, amber ×4, rose ×3.)

### E2 — `caseStudiesData` (7 rows; §4)

| id | title | location | type | siteType | system | shaved | savings | payback | details |
|---|---|---|---|---|---|---|---|---|---|
| livoltek | Livoltek C&I Evening Peak Suppression | Malaysia (RP4 MV ToU) | malaysia | Industrial Factory with Existing Rooftop PV | 125 kW / 261 kWh LFP (Liquid-cooled) | 89.99 kW shaved | RM 9,000 / month (>RM 95,000/yr) | 2.8 – 3.5 Years (with MIDA GITA) | Rooftop solar dropped to 0 at 19:00, but factory ran shift until 22:00 causing severe net-grid spikes. BESS discharged 20:00-22:00 to eliminate evening peak. |
| plusxnergy | Plus Xnergy Multi-MW Zero-Capex EaaS | Malaysia (RP4 MV ToU) | eaas | Large Industrial Manufacturing Plant | 1.5 MW / 3.0 MWh LFP Class | 1,478 kW shaved (3,900 kW → 2,422 kW) | Net client savings: RM 21,520 / month | Immediate (0-Yr Payback; EaaS Lease) | Client pays RM82.50/kW shaved vs TNB RM97.06/kW rate. Gross MD bill cut by RM143,455/mo with zero capital outlay under a 15-year EaaS agreement. |
| solarvest | Solarvest Solar ATAP + BESS Reference Site | Malaysia (RP4 MV ToU) | malaysia | Medium Voltage C&I Facility | 1,000 kWp PV + 500 kW / 1,000 kWh BESS | >650 kW shaved (>65% MD Cut) | RM 712,000 / year gross savings | <2.5 Years (Gross RM2.4M less RM920k GITA) | Combines daytime PV self-consumption with peak shaving. Utilizes AI EPMS control to maintain reserve margin and maximize MIDA GITA tax allowances. |
| avera | Avera Energy MV Factory Transition | Malaysia (MV General → ToU) | malaysia | 500,000 kWh/mo Manufacturing Plant | Rooftop Solar + 165 kW / 330 kWh BESS | 315 kW Total MD Cut (165 kW BESS) | RM 58,945 / month (25.7% total bill cut) | 3.0 – 4.2 Years integrated payback | Switched from MV General to MV ToU, combining shift optimization (150 kW cut) with targeted 165 kW BESS peak clipping. |
| unibess | UniBess C&I Modular Peak Shaving | Malaysia (RP4 MV ToU) | malaysia | Medium Voltage Factory (600 kW spikes) | 500 kW / 1,044 kWh (4 x 125kW Cabinets) | 400 kW shaved (Capped at 200 kW target) | RM 38,824 / month (RM 465,888 / year) | 2.5 – 3.5 Years simple payback | Modular LFP liquid-cooled cabinets dynamically capped facility grid import below preset threshold during the 14:00-22:00 peak window. |
| haplt | Predictive HAPLT Controller Field Validation | Malaysia (Industrial Feeder) | malaysia | Industrial Sub-Load Feeder Trial | 50 kW / 155 kWh Li-ion (139.5 kWh usable) | 89% Average MD Reduction Factor | RM 2,445 / month verified in field | Academic Field Validation Trial | CNN/LSTM/XGBoost predictive controller prevented premature SOC depletion during early afternoon humps to preserve battery energy for critical peaks. |
| cnc | Precision CNC Machining Plant | Comparable ToU Market | overseas | Precision Machining & Compressor Plant | 250 kW / 515 kWh LFP BESS | 230 kW shaved (780 kW → 550 kW) | US$ 5,520 / mo (~RM 295,000 / year) | 2.1 Years simple payback | Automated EMS capped plant load at 550 kW during overlapping 45-90 min CNC cycle runs and compressor startup cycles. |

### E3 — `geoParksData` (9 rows; §5)

| region | park | count | sectors | rating |
|---|---|---|---|---|
| Selangor (Klang Valley) | Shah Alam Industrial Estates (Sec 15, 16, 22, 23, 26, HICOM) | ~1,200 – 1,500 | Automotive metal stamping, plastic injection, food processing, cold storage | Prime Tier 1 Hub |
| Selangor (Klang Valley) | Klang & Port Klang Corridor (Meru, Kapar, Bukit Raja, Telok Gong, PKFZ) | ~1,400 – 1,800 | Plastic moulding, rubber gloves, metal fab, edible oils, port cold storage | High-Volume Mixed |
| Selangor (Klang Valley) | Southern Corridor (Bangi, Kajang, Balakong, Seri Kembangan, Semenyih) | ~1,100 – 1,400 | Precision stamping, industrial automation, food mfr, pharma, plastics | Prime Tier 1 SMI Hub |
| Johor (Southern) | Tebrau Industrial Estates (I–IV), Mount Austin & Tampoi / Larkin | ~800 – 1,100 | Plastic injection moulding, metal stamping, wire harness, food processing | Prime Tier 1 Hub |
| Johor (Southern) | Pasir Gudang Industrial Estate & Tanjung Langsat (8,000+ acres) | ~500 – 700 | Oleochemicals, edible oil refining, tinplate, copper extrusion, cold storage | High-Capacity MV/HV |
| Johor (Southern) | Senai Industrial Estates (I–IV), i-Park, Kulai & SILC Nusajaya | ~600 – 850 | EMS/E&E assembly, precision plastics, aerospace, food & cold chain | High-Fit Modern Hub |
| Penang & Kedah | Bayan Lepas FIZ (Phases 1–4) & Technoplex (1,400 acres) | ~220 – 300+ | Semiconductor, OSAT (Intel, AMD, Infineon), EMS (Jabil, Plexus), medical | Selective (UPS / Solar) |
| Penang & Kedah | Batu Kawan (BKIP 1–3), Perai FIZ, Bukit Tengah & Bukit Minyak | ~850 – 1,000 | Automation (ViTrox, Greatech), sheet metal (UWC), automotive, food | Tier 1 Vendor Ecosystem |
| Central / Southern Spine | Nilai & Senawang (N.Sembilan), Ayer Keroh (Melaka), Ipoh (Perak) | ~1,200 – 1,600 | Halal food hubs, cold storage, rubber gloves, textiles, metal/plastics | High Regional Potential |

## Links and cited documents

| Label as shown | URL or document ID | Where used |
|---|---|---|
| (no hyperlinks in the page body) | — | — |
| Page libraries (scripts/styles, not content) | https://cdn.tailwindcss.com ; https://cdn.jsdelivr.net/npm/chart.js ; https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css | HTML head |
| "Tenaga Nasional Berhad (TNB) & Industry Case Studies" | — | Footer ("Data Source") |
| "Energy Commission Guidelines" | — (not named) | Footer |
| RP4 Medium Voltage Framework (1 July 2025 – 31 Dec 2027) | — | Header, §1, footer |
| Energy Efficiency and Conservation Act (EECA) | — | §6, design comment |
| ISO 50001 (EnMS) | — | §6, design comment |
| MIDA Tier 1 Green Investment Tax Allowance (GITA); Capital Allowance; 24% corporate tax rate | — | §4.1, §6.2, E2 |
| myTNB portal | — | §6.2 |
| Case-study sources (Livoltek, Plus Xnergy, Solarvest, Avera Energy, UniBess, "Predictive HAPLT Controller Field Validation", unnamed overseas CNC plant) | none cited | §4, E2 |
| Associations and events: FMM, MPMA, MAREMA, MAESCO, IEM (EMTC), MSIA, PPK, MAH, APHM, BMAM; MIMF (MITEC KL), ETCON (TNB), SEMICON Southeast Asia, IGEM (KLCC), Wisma IEM | none cited | §6.1 |

## Extraction notes

Recycled figures (not independent evidence):

- **Three of the seven "published" case studies reuse numbers from earlier AI reports in this repo.**
  - Plus Xnergy (1,478 kW shaved, client nets RM21,520/month at RM82.50/kW vs RM97.06/kW) is R8's illustrative "benchmark model" example, word for word in its figures. R9 adds "3,900 kW → 2,422 kW", "1.5 MW / 3.0 MWh" and "15-year", none of which is in R8's example.
  - UniBess (400 kW shaved, RM38,824/month, RM465,888/year) equals R1's hard-coded simulator result (400 kW × RM97.06).
  - Avera Energy (500,000 kWh/month plant, MV General → ToU, RM58,945/month, "25.7% total bill cut") equals R3's bill-simulator placeholder for a 500,000 kWh/month MV factory (RM229,693 → RM170,748 = RM58,945, −25.7%). R3's scenario used a 250 kW / 500 kWh BESS; R9 describes 165 kW / 330 kWh plus a 150 kW shift-optimisation cut.
- The 1,044 kWh UniBess system is "4 x 125kW Cabinets", i.e. 261 kWh per cabinet — the same 125 kW / 261 kWh unit as the Livoltek case.

Internal contradictions and numbers that don't reconcile:

- Design comment promises "9 published BESS case studies" and "Searchable and filterable gallery … with modal/expand details"; the page has 7, a filter dropdown, no search and no modal.
- **Sector "Post-RP4 MD Share" values are the simulator's own outputs, not measured data.** At 1,000 kW with no solar and no BESS, the simulator gives exactly 59.5% (metal preset), 56.3% (office), 49.7% (food), 43.1% (plastic) and 32.5% (glove). The other six values fit the same model with peak-window kWh ratios of about 0.48 (malls), 0.36 (hotels), 0.29 (cold storage), 0.31 (hospitals), 0.26 (textiles) and 0.25 (semiconductor) (back-solved by the extractor).
- Simulator insight text (static): "adding solar increases MD share from 59.5% to 69.4%". At the default 500 kWp the model gives 66.4% (solar only); 69.4% is not reproduced. The intro's "~55% up to ~70%" is a range claim with no stated basis.
- Simulator placeholders are the no-solar, no-BESS baseline (RM163,144; 59.5%; "Pre-Solar Baseline"; "Low Load Factor Exposure"), but both checkboxes are on by default, so on load the page shows RM121,829, 59.8%, "With Solar + BESS Peak Shaving", "MD Clipped via BESS".
- §2 header says spiky loads with LF < 0.60 give maximum returns and LF > 0.75 need excessive storage, but tiers do not follow LF strictly: Plastic Injection (LF 0.55) is Tier 1 while Shopping Malls (LF 0.52) are Tier 2; Hospitals (LF 0.72, score 60) score above Cold Storage (LF 0.68, score 55). The chart subtitle's "clear inverse relationship" holds only roughly.
- Cold Storage is labelled "Conditional (Tier 2/3)" but sits in the tier2 filter; Textiles & Dyeing combines a flat spinning plant and a spiky dyeing plant in one row with one LF (0.78).
- The "Tier 3/4 (Flat / Low Fit)" filter shows the three 'poor' rows; no row is labelled Tier 3 or Tier 4.
- Tariff table: the capacity-charge description "Highest 30-min average kW inside peak window" is given for both columns, but MV General demand is assessed in all blocks (T01, R2).
- Metric card: "+115% to +162% vs RP3" sits under the RM98.61 (incl. KWTBB) figure but is computed from base rates: 97.06 / 45.10 = +115.2%; 97.06 / 37.00 = +162.3%. KWTBB arithmetic checks out: 37.00 × 1.016 = 37.59; 45.10 × 1.016 = 45.82; 89.27 × 1.016 = 90.70; 97.06 × 1.016 = 98.61. Chart 1's RP3 bar (41,000 per 1,000 kW) is about the midpoint of RM37.00–45.10.
- AFA card: "+3.61 to +7.59 sen/kWh monthly monthly variable surcharge" (word repeated). The Nov 2026 – Jan 2027 forecasts (4.27, 4.46, 7.59) have no source or method.
- "Extended 4 hrs past sunset" is stated without a sunset time.
- Geography counts: Selangor "Over 4,000+" vs table rows summing to ~3,700–4,700 (chart 4,200); Johor "2,500+" vs rows ~1,900–2,650 (chart 2,600); Penang & Kedah rows ~1,070–1,300+ vs chart 1,400; Central Spine row ~1,200–1,600 vs chart 1,500. Kedah's Kulim KHTP is named in the region card but has no table row. The chart total is 9,700 and is labelled "Medium Voltage Factory Density", but nothing says the counts are MV accounts. The design comment says "500+ industrial parks across Selangor, Johor, Penang, and Kedah"; the text says 500+ parks and 22 FIZs across Peninsular Malaysia.
- GITA box: "offset against up to 70% of statutory income over 3–5 years". R7 says unused GITA carries forward indefinitely (T03). R9 attributes the allowance to MIDA (C14), applies "Tier 1" to BESS with no mention of Budget 2027 or the 31 Dec 2026 cutoff (C01, C20), and adds 100% CA × 24% to reach "~48%" (C02).

Case-study arithmetic (extractor checks):

- Livoltek: 89.99 kW × RM97.06 = RM8,734/month (× RM98.61 = RM8,874), shown as "RM 9,000 / month"; RM9,000 × 12 = RM108,000, shown as ">RM 95,000/yr". 89.99 kW is 72% of the 125 kW rating.
- Plus Xnergy: 3,900 − 2,422 = 1,478 kW; 1,478 × 97.06 = RM143,455 (matches); 1,478 × 82.50 = RM121,935; 143,455 − 121,935 = RM21,520 (matches). 1,478 kW from a 1.5 MW system is 98.5% of rated power.
- Solarvest: ">650 kW shaved" from a 500 kW BESS needs ≥150 kW from PV, which the report says elsewhere does not reliably cut MD. 650 kW × 97.06 × 12 = RM757,068/year from MD alone, more than the RM712,000 "gross savings". RM920k / RM2.4M = 38.3% tax benefit (neither the 24% GITA rate nor the "~48%" shown in §4.1). (2.4M − 0.92M) / 0.712M = 2.08 years, consistent with "<2.5 Years".
- Avera: 165 + 150 = 315 kW; 315 × 97.06 = RM30,574/month of the RM58,945; the rest (solar energy, tariff switch) is not itemised. RM58,945 / 25.7% implies a ~RM229,358 starting bill.
- UniBess: "400 kW shaved (Capped at 200 kW target)" is self-contradictory; the site has "600 kW spikes"; 400 × 97.06 = RM38,824 and × 12 = RM465,888 (match).
- HAPLT: 139.5 / 155 = 90% usable; RM2,445 / 97.06 ≈ 25.2 kW-equivalent; "89% Average MD Reduction Factor" is not defined.
- CNC: 780 − 550 = 230 kW (matches); US$5,520 × 12 = US$66,240 ≈ RM295,000 implies ~RM4.45/US$ (rate not stated). No location, tariff or date.

Calculator (C1) bugs and limitations:

- Solar never changes billed MD (by design, "leaves peak kW set"), and solar energy is split a fixed 40% peak / 60% off-peak regardless of shift pattern.
- No export credit: solar beyond consumption is clamped to zero energy charge (e.g. 3,000 kWp on a 200 kW site).
- "Monthly BESS MD Savings" = kW shaved × RM97.06 even when kW shaved exceeds peak demand (1,500 kW on a 200 kW site → RM145,590/month savings against a RM200 bill; label "750%").
- No BESS capex, payback, charging energy, round-trip losses or degradation; "kW shaved" is assumed achieved with no battery size.
- Monthly kWh = P × 720 × LF (30-day month); α (peak-window share of kWh) is independent of LF, so impossible combinations are allowed.
- KWTBB (1.6%) is shown in §1 but not applied; AFA is fixed at 3.61 sen; retail RM200 is in the bill total but not in the chart.
- Presets: "Shopping Mall (LF: 52%, Peak: 1,000 kW)" has no branch in `applySimPreset()`, so choosing it changes nothing; presets don't reset the solar or BESS controls; hotels, cold storage, hospitals, textiles and semiconductor have no preset. Moving a slider does not switch the dropdown to "Custom Configuration".
- The comment promises a "Doughnut & Stacked Bar chart"; only a stacked bar exists.

Rendering artefacts:

- LaTeX `$...$` is used with no math renderer loaded, so it shows as raw text: `$LF < 0.60$`, `$LF > 0.75$`, `$LF$`, `$P_{\text{max}}$`, `$\alpha$`, `$LF = 0.28\text{--}0.55$`, `1.3$\times$–1.5$\times$`.
- Libraries load from CDNs (Tailwind and Chart.js unversioned; FontAwesome 6.4.0), so the page needs internet access and may change over time.

Claims with no source in the report:

- The page has no hyperlinks. Every load factor, suitability score, shift pattern, peak behaviour, spike driver and BESS duration in E1 is unsourced, as are all 7 case studies (no publication, date or link), the factory counts in E3, the "500+ industrial parks and 22 FIZs", the association membership figures (FMM 3,500+, MPMA 800+), the AFA forecasts and the legacy RP3 energy rates (35.50–36.50 / 21.90–22.40 sen/kWh).
- "Off-peak … all weekends & public holidays" is stated without a source; no other report addresses public holidays.
- "myTNB portal" as the source of 12 months of 15/30-minute data is stated without a process or link.
- "EECA and ISO 50001 mandatory requirements": no clause is given for either; R2 is the only report with EECA thresholds (T09).
- "REEM" (Registered Electrical Energy Managers) is used where R2 uses "REM" (Registered Energy Manager); "MAREMA", "MAESCO", "PPK", "MAH", "APHM" and "BMAM" are not expanded.

Prompt coverage (prompt #4):

1. Which industries have short spikes in 14:00–22:00 vs flat 24/7 load, with typical load factor and daily shape — Answered for all 11 named sectors (E1), as text descriptions plus one LF figure each. No hourly load curves, no ranges and no sources.
2. Which industries have the highest MD share of the bill after RP4 — Answered (metal stamping 59.5% highest, rubber gloves 32.5% lowest), but the values are outputs of the report's own simulator, not measured bills.
3. Published BESS peak-shaving case studies — Partly. 7 cases (5 Malaysian commercial, 1 academic trial, 1 unnamed overseas). No links or dates; 3 reuse figures from R1, R3 and R8.
4. Industrial parks or clusters with approximate factory counts — Answered (E3, 9 clusters with ranges), unsourced; totals do not match the region cards or chart.
5. Industry associations and events — Answered for FMM, MPMA, MSIA, MAREMA/MAESCO, IEM and PPK/MAH/APHM with named events. "SMI Association" (named in the prompt) is not covered.
- Round-2 instruction "Ask for sourced text or tables with links and dates" — Not met: no links, and no dates beyond the tariff period and AFA months.
