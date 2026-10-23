---
id: T07
title: Financing and business models — bank debt, BNM facilities, GTFS 5.0, PPAs (SARE / bilateral / CRESS), zero-capex BESS, guarantees and liquidated damages, customer preferences
covers: how C&I customers pay for solar and BESS, who funds what, contract structures, BESS performance-risk allocation, preference by company size, decision logic
sources: [R6, R1, R7, R8, R3]
primary_source: R6 (answers research prompt #6; no hyperlinks or dates)
conflicts: [C03, C13, C18]
related: [T03, T05, T06, T10]
updated: 2026-10-23
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T07 — Financing and business models

## TL;DR
- **SMEs mostly buy with bank debt** (R6 preference: SMEs 80% outright debt / 15% lease / 5% PPA); **large firms mostly use PPAs** (10% / 20% / 70%); mid-market splits 55 / 25 / 20 [R6, unsourced].
- Concessional debt: **BNM LCTF (≤5.0% p.a., up to RM10M, 10 yrs)** and **BNM HTG (3.5%–5.0% p.a., up to RM10M)**; **GTFS 5.0** now gives only a 60%–80% guarantee with **0% interest rebate**, RM1.0B allocation until 31 Dec 2026 [R6]. Budget 2027 adds **Green Sustainability Fund 2.0** (RM2B, 1% p.a. subsidy for 5 years) [R7].
- **BESS for MD is binary risk:** one missed 30-minute peak wipes the month's saving, so contracts use a 3-tier guarantee ladder and liquidated damages = missed kW × RM97.06 [R6].
- **Zero-capex BESS norms:** client keeps 15%–30% of MD savings; ESCO keeps 70%–85%; 5–15 year terms [R6, R8].
- From 2027, **GITE (70% exemption for RPVIs) ends** and integrated solar + BESS gets 100% GITA only when the user owns it — R7 expects finance to shift to host-owned capex and hire purchase [R7] [C01].

## 1. Concessionary debt (R6)
| Facility | Target | Quantum | Tenure | Rate | Scope |
|---|---|---|---|---|---|
| BNM Low Carbon Transition Facility (LCTF) | Malaysian SMEs (sales ≤RM50M manufacturing or ≤RM20M services) | Up to RM2.5M (turnover ≤RM25M) or RM10.0M (turnover >RM25M) | Up to 10 yrs | Capped 5.0% p.a. | Rooftop solar, EE retrofits, low-carbon machinery |
| BNM High Tech and Green Facility (HTG) | Strategic manufacturing/services (E&E, chemicals, aerospace) or green tech providers (≥51% Malaysian-owned) | Up to RM10.0M | Up to 10 yrs | 3.5% p.a. (unsecured) or 5.0% p.a. (with CGC guarantee) | — |
| Green Sustainability Fund 2.0 (Budget 2027) | C&I low-carbon transition | RM2 billion fund | Up to 10 yrs | 1% p.a. subsidy for first 5 years | Via commercial banks [R7] |

## 2. GTFS 5.0 sovereign guarantee (R6)
"RM1.0B Allocation until 31 Dec 2026"; interest rebate 0% (government "eliminated the interest rate rebate entirely", now a "loss-given-default credit risk-sharing vehicle (60% to 80% guarantee coverage)"). "Technical criteria for 'User' category exclude standalone solar PV, prioritizing industrial EE and BESS."
| Applicant category | Max limit (group) | Max tenure | Guarantee | Rebate | Scope |
|---|---|---|---|---|---|
| Producer of green tech | RM100M | 15 yrs | 60% (80% waste) | 0% | Production of green products; excludes LSS and rooftop solar PV |
| User of green tech | RM50M | 10 yrs | 60% (80% waste) | 0% | Industrial EE retrofits, plant modernisation; excludes standalone solar |
| ESCO | RM25M | 10 yrs | 60% | 0% | Financing EE assets & EPC contracts; requires ST registration |
| Housing developer | RM100M | 5 yrs | 60% | 0% | Green residential (selling price RM350k–450k) |
| Mobility infrastructure | RM50M | 5 yrs | 60% | 0% | EV charging by Charge Point Operators |

## 3. Commercial bank offerings (R6)
| Bank | Offering |
|---|---|
| Maybank / Maybank Islamic | LCTF/-i (up to RM10M); SME property bundled financing (up to 20 yrs); 0% credit-card EPP up to 60 months with 6 solar partners |
| CIMB / CIMB Islamic | SME RE Financing-i (up to 100% margin); RM3B Sustainability-Linked Financing with up to 0.50% p.a. rebate tied to BEI / GHG targets |
| RHB / RHB Islamic | SME Green RE & CAPEX financing, 100% margin, from 4.50% p.a., via industrial hire purchase or commodity murabahah |
| UOB Malaysia | U-Solar 2.0 integrated with HTG/LCTF; bundles Huawei, Sungrow, Longi, Trina hardware; free civil studies; 1–3 yrs free O&M |
| Bank Islam | Business Financing-i (Tawarruq), Finance Lease-i; lead arranger for solar/BESS Sukuk Wakalah (e.g. Ditrolic RM150M) |
| OCBC & Alliance Bank | OCBC SME Sustainable Financing finances BESS under EE without prior green certification |

## 4. PPA architectures
| Dimension | Tripartite SARE (via TNBX) | Private bilateral PPA / lease | Off-site CRESS |
|---|---|---|---|
| Parties | Prosumer/host, RPVI investor, TNB [R1, R6] | RPVI and host directly [R1, R6] | RE developer, green consumer, TNB grid [R6] |
| Tenure | 21 years standard [R6] | 15–21 years [R6] | 10–21 years [R6]; ≥10 yrs under 2026 package [R1] |
| Pricing (2026) | Fixed/escalated ~25 sen/kWh+ [R6] | 10%–30% discount to TNB rate [R6] | ~26 sen generation + SAC [R6] [C03] |
| Billing | Consolidated into the TNB bill; TNB collects and remits; **TNB charges a fixed 2 sen/kWh (~6–8% of gross revenue)** [R1] | Direct invoicing; RPVI carries credit risk; RM0 to TNB [R1] | BESC + CRESA |
| Default enforcement | TNB can disconnect grid supply (ESA 1990 Sec 29) — "High bankability" [R1, R6] | Contractual remedies, arbitration, system shut-off [R6] | BESC & CRESA security terms [R6] |
| End of term | Automatic transfer to customer [R6] | Negotiated transfer or buyout [R6] | Developer keeps the remote farm/BESS [R6] |
| Best for | Pure rooftop solar on legacy Tariffs B, D, C1, E1 [R1] | Hybrid solar + BESS on C2, E2, E3; allows shared savings on MD [R1] | Large HV users without roof space [R6] |
R6 extraction note: CRESS at ~26 sen + 20/40 sen SAC (46–66 sen) is above the grid peak rate the same report quotes, yet R6 promises large users 10%–30% savings — unreconciled.

## 5. Zero-capex BESS models for MD shaving
| Model | Mechanics | Tenure | Source |
|---|---|---|---|
| Shared-savings IPMVP EPC | ESCO funds 100% of BESS + AI-EMS; verified monthly demand savings split **75:25 or 80:20 (ESCO : host)**; ESCO carries cash-flow and performance risk | 5–10 yrs (7 standard) | R6 |
| Discounted MD rate (Plus Xnergy) | Host pays **RM82.50/kW** on the shaved kW vs TNB RM97.06/kW → fixed 15% discount; no baseline disputes | 15 yrs | R6, R8 |
| Vendor hybrid / operating lease | Solarvest Powervest Powerflex Lite: 7-year payment for a 20% downpayment, customer claims GITA; UniBess EaaS/lease 7–10 yrs, monthly fee < monthly MD savings | 7–10 yrs | R6, R8 |
| EaaS fee below savings | Solarvest Powervest; Kawan Renergy BaaS/EaaS; Cenergi zero-capex SELCO BESS | 10–20 yrs | R8 |
| Bundled hybrid PPA | ERS Energy fixed rate 25%–40% below TNB incl. <20 ms backup | 15–25 yrs | R8 |

Plus Xnergy 15/85 worked example (R8): developer bills RM82.50/kW vs TNB RM97.06/kW; client keeps ~15% (~RM14.56/kW; ~RM21,520/month on 1,478 kW shaved); developer keeps ~85% to cover 2-hour LFP capex (RM2,300–2,900/kW), off-peak charging, 10–15 yr liquid-cooling O&M and mid-life augmentation; financier return 12%–18% p.a. (~4-year payback). R8: "CFOs heavily prefer Zero-Capex, Shared-Savings, and Energy-as-a-Service (EaaS) structures that transfer algorithmic risk to developers."

## 6. BESS performance risk (R6)
"BESS peak shaving is binary: because TNB bills Maximum Demand on the single highest 30-minute peak in a month, a single 30-minute battery failure during peak hours (14:00–22:00) destroys 100% of that month's demand charge savings."
| Tier | Guarantee | Cost adder | Remedy / limit |
|---|---|---|---|
| 1 | Hardware capacity retention (e.g. 80% SoH at yr 10) and round-trip efficiency (85% → 78%) | +2%–3% capex | Free cell replacement/augmentation; excludes missed TNB savings |
| 2 | Peak-window availability ≥97% (stated as 08:00–22:00 [C13]); 24/7 NOC; 6-hour on-site response | +3%–5% capex | Embedded in O&M / operating leases |
| 3 | Binding MD kW reduction or RM savings floor | +5%–8% capex | LDs = missed TNB charges or 100% monthly fee forfeiture; needed for project finance / shared savings |
- **LD formula:** Shortfall penalty (RM) = (guaranteed MD reduction − actual MD reduction) × RM97.06. Default example: 300 kW guaranteed, 100 kW achieved → 200 kW × 97.06 = **RM19,412.00/month**.
- **Customer Load Breach carve-out:** if BMS/EMS telemetry shows the miss came from EMS latency or a battery trip, the ESCO bears 100% of LDs; if site load exceeded the contracted kW/kWh envelope or staff bypassed load controls, it is an excused Customer Load Breach. IPMVP baseline normalisation applies. Example EMS: Tanand EasiEMS sends early Telegram alerts at 750 kW against an 800 kW ceiling.

## 7. Tax constraints that shape the model
- Pioneer Status / ITA (PIA 1986) / Reinvestment Allowance (Schedule 7A) firms cannot claim GITA (MIDA Sec 3.1(e)) → prefer zero-capex PPAs where the RPVI claims the tax shields (~25 sen/kWh) [R6].
- From 2027 the RPVI loses GITE and GITA Project Tier 3; the host gets no capital allowance under a PPA → R7 recommends host-owned integrated capex with 100% GITA Tier 1b + CA + GSF 2.0 [R7] [C01].
- Hire purchase: qualifying capex claimed progressively on principal paid (LHDN PR 4/2023) [R7].

## 8. Preference by company size (R6, unsourced, hard-coded)
| Segment | Outright bank debt (LCTF/HTG/GTFS) | Operating lease / vendor hybrid | Zero-capex PPA (SARE/bilateral) |
|---|---|---|---|
| SMEs (50–200 kWp) | 80% | 15% | 5% |
| Mid-market (200 kWp–1 MWp) | 55% | 25% | 20% |
| Large / MNCs (1–10 MWp+) | 10% | 20% | 70% |

## 9. R6 recommendation engine (summary of the decision logic; every branch with exact text is in `../sources/R6_financing_2026.md`)
- **Tax status = Pioneer / ITA / RA** → warning: GITA barred; opt for a zero-capex PPA (SARE or bilateral) at ~25 sen/kWh.
- **Standard taxpayer + solar or hybrid** → notice: standalone solar 0% GITA after 31 Dec 2026; pairing with BESS unlocks 100% GITA Tier 1 on combined capex (24% tax shield).
- **SME + tenant** → 5–10 year solar operating lease (Powervest or UniBess), because of relocation risk.
- **SME + owner-occupier** → financed outright purchase via BNM LCTF (≤5.0%) or HTG (3.5%) through CIMB, Maybank or RHB; Powerflex Lite to bridge a 20% downpayment. Benefit: owner-occupier SMEs capture 2x–3x the lifetime benefit (RM950k–1.6M over 25 yrs) vs a PPA.
- **Mid-market + BESS or hybrid** → split asset: outright loan for solar (GTFS 5.0 60% CGC guarantee or green loan, to claim GITA) + zero-capex shared savings for BESS (75:25) or Plus Xnergy RM82.50/kW, shifting peak-miss risk to the ESCO.
- **Mid-market + solar only** → GTFS 5.0-backed green loan, outright purchase; IRR 17%–30%, 4.0–6.0 yr payback.
- **Large** → 21-year SARE PPA, or CRESS wheeling at 20 sen firm SAC if roof space is constrained; 10%–30% opex savings, no balance-sheet liability, bundled Scope 2 RECs.
R6 extraction notes flag logic gaps (e.g. pioneer firms still told to buy outright to claim GITA; large-company branch ignores asset type).

## 10. R6 25-year cashflow illustration (hard-coded, 500 kWp)
Series: financed outright purchase with GITA (−RM1,200,000 in year 1; then +RM280,000 + RM196,000; then +RM190,000/yr); SARE PPA +RM60,000/yr; "15-yr" operating lease +RM102,000/yr plotted for 25 years. Illustrative only; see R6 extraction notes for the arithmetic issues.

## 11. Dual licence angle (R1)
Holding both SEDA RPVSP (service provider) and RPVI (investor) lets an operator "capture both upfront EPCC engineering margins and long-term PPA cashflows"; private bilateral hybrid PPAs avoid TNB's 2 sen/kWh SARE fee and allow MD shared-savings splits [R1].
