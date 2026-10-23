---
id: T05
title: Competitors, zero-capex BESS providers, integrators and hardware OEMs
covers: master list of every company named across the reports, with scale, BESS track record, business models, EMS products, financials, competitive moats and price-competition segments
sources: [R3, R8, R6, R4, R1]
primary_source: R8 (answers research prompt #3; no hyperlinks), R3 provider directory (no sources)
conflicts: [C12, C18]
related: [T06, T07, T08]
updated: 2026-10-23
confidence_note: No company figure in R3 or R8 carries a link. Treat portfolio sizes, order books and project claims as leads to verify against Bursa filings and company releases.
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T05 — Competitors and providers

## TL;DR
- **Three structural moats** in 2026 (R8): (1) bundling solar with the mandatory SELCO BESS hardware; (2) vertical integration into HV switchgear and data-centre earthing (ELP); (3) **proprietary AI-driven EMS dispatch software**.
- **Direct C&I BESS leader:** Plus Xnergy (100 MWh portfolio incl. 20 MWh single-site SELCO BESS in Perak; zero-capex MD tariff at RM82.50/kW) [R3, R4, R8].
- **Largest listed EPCC:** Solarvest (~3.7 GWp, RM2.37B unbilled order book Aug 2026) [R3, R8].
- **Price war zones** (R8): small C&I rooftops 50–300 kWp (RPVSPs pivoting from residential quote ~RM2.40/Wp), utility balance-of-plant subcontracting, and plain BESS hardware distribution without EMS.
- **Protected zones** (R8): zero-capex / EaaS peak shaving, data-centre ELP & switchgear, HV grid interconnection.

## 1. Master company table
Type: EPCC = turnkey EPCC/developer; ZC = offers zero-capex / EaaS / shared savings; INT = integrator / consultancy; OEM = hardware maker.
| Company | Type | Listing / owner | Scale (as reported) | BESS track record (as reported) | Business models | EMS / product | Sources |
|---|---|---|---|---|---|---|---|
| Solarvest Holdings Bhd | EPCC, ZC | KLSE: SLVEST (0215) | ~3,700 MWp (3.7 GWp); RM2.37B unbilled order book (Aug 2026), anchored by RM1.06B LSS5+ EPCC in Perak | Multiple C&I BESS with 20%–65% MD cuts; bidder in MyBeST 400 MW / 1,600 MWh utility auction; deployments 2024–2026 across plants, data centres, EV hubs | Outright capex; Zero-capex Powervest PPA; fintech financing; zero-capex BESS EaaS (Powervest 10–15 yrs, fee below MD savings); Powerflex Lite (7-yr payment for 20% downpayment, customer claims GITA) | AIES (AI-driven Energy Simulator) + EPMS real-time monitoring; "AI machine-learning EPMS" | R3, R8, R6 |
| Gentari Sdn Bhd | EPCC, ZC | Private (wholly PETRONAS) | ~9,100 MW (9.1 GW) global RE | Malaysia's 1st solar + BESS EV charging hub (Oct 2023); "~1.5 GW Gamuda CRESS BESS"; data-centre CRESS BESS firming | Zero-capex PPA; CRESS green power supply; outright EPCC; integrated EaaS; corporate PPAs, zero-capex leasing, co-investment | Integrated C&I EMS; EV ultra-fast charging (BYD partner) | R3, R8 |
| Ditrolic Energy Holdings | EPCC, ZC | Private (IFC & Sukuk backed) | 1,000+ MW constructed / 300 MW O&M (R8); >300 MW managed / >1 GW constructed (R3) | EnerPack behind-the-meter BESS for industrial & data centres; Johor RE Corridor utility BESS with IFC & PDT; 600 MW SJREC cross-border export approval (Aug 2026) | Outright EPC (EnerGreen); zero-capex PPA (EnerLoop); O&M; EaaS; CRESS tariffs | Net-Zero Energy OS, 15-min smart integrated dispatch; EnerGreen SolarPack (CRESS) | R3, R8 |
| Samaiden Group Bhd | EPCC, ZC | KLSE: SAMAIDEN | 700+ MWp cumulative | C&I BESS peak shaving & backup (2025–2026); projected 125–188 MW LSS6 BESS awards | Outright EPCC; zero-capex PPA framework; O&M; REC trading | Automated BESS peak-shaving & MD threshold dispatch controller | R8 |
| Sunview Group Bhd | EPCC, ZC | KLSE: SUNVIEW | ~650–800+ MWp portfolio (R8); >350 MWp completed across 150+ sites (R3) [C12]; ~RM1.17B backlog | 40% share of RM1.96B Lake Kenyir 595 MWac floating solar + BESS JV with Cypark for TNB Genco (Apr 2026); Uzbekistan BESS; SunBESS projects | Outright EPCC (SunVertax); zero-capex ownership (SunValue); solar + storage capex; asset ownership / PPA | SunBESS AIoT LFP storage for RP4 & SELCO; full MGTC/MIDA GITA advisory & O&M; helps clients with ST BESS licensing and GITA Tier 1 submissions | R3, R8 |
| Plus Xnergy Services | EPCC, ZC | KLSE: BMGREEN (parent BM GreenTech) | >400 MWp solar (R8) / >500 MWp (R3) [C12]; 100 MWh BESS | **20 MWh SELCO BESS at a Perak food/grain processing park (HyperStrong, operational Jun 2026, executed in 2.5 months)**; 1.45 MWh NaS BESS in Kedah (with Leader Energy); "RM1.25M/year savings per 10 MWh" | Outright EPCC; **15-yr zero-capex BESS partnership / Performance Sharing Agreement**; zero-capex PPA; discounted MD rate RM82.50/kW (client keeps 15%) | AI-driven BESS EMS + SOURCE platform (weekday 2–10 PM MD shaving) | R3, R4, R8, R6 |
| Cypark Resources Bhd | EPCC | KLSE: CYPARK | >400 MWp operational / hybrid | 60% JV lead in Lake Kenyir 595 MWac floating PV + BESS (RM1.96B, Apr 2026) | IPP asset ownership; turnkey EPCC; PPPs | Utility hybrid solar-storage dispatch & grid-firming SCADA | R8 |
| Pekat Group Bhd | EPCC, ZC | KLSE: PEKAT (0233) | ~300–400+ MWp; RM994M unbilled (Jul 2026) | Data-centre & factory BESS with EPE MV switchgear & ELP; RM47M data-centre wins Jul 2026 (Port Dickson RM20M, Johor RM27M) | Outright EPCC; zero-capex PPA / CGPP asset; BESS + O&M | Solar + BESS peak shaving & EPE MV distribution EMS; 60% Peninsular share of earthing & lightning protection (ELP) | R8 |
| GSPARX Sdn Bhd | EPCC, ZC | Private (wholly TNB) | 224 MW installed C&I | 76.8–170 kWh BESS at Elmina Ilham; C&I BESS partnership with EVE Energy (EVE built 36 MWh / 18 MW BESS at KLIA, Feb 2026) | Zero-capex SARE PPA (billed via TNB bill); outright EPCC | TNB smart-grid integrated BESS peak shaving | R8 |
| Progressture Solar | EPCC, ZC | Private | ~200–300+ MWp C&I | Turnkey C&I BESS for factories, commercial property, data centres | Outright EPCC; zero-upfront solar PPA; custom solar/BESS financing | BESS peak shaving, load shifting, power expansion EMS; 600+ Shell stations, ~100 Petron stations, 12 MWp Brunei plant (2026) | R8 |
| Founder Group Ltd | EPCC | NASDAQ: FGL (Reservoir Link) | ~200+ MWp EPCC | Iron-flow long-duration storage via JV RL ADS Power (MY, SG, ID 2025–2026) | Outright EPCC; BoP subcontracting; C&I rooftop investor | AI O&M; iron-flow LDES load-shifting | R8 |
| Northern Solar Holdings | EPCC, ZC | KLSE: NORTHERN (0340) | ~150+ MWp cumulative; RM119.4M LSS5 + C&I | **RM20.5M ground-mounted SELCO BESS award (~15–18 MWh)**; Sungrow / Huawei / EVE cabinets | Outright EPCC (96.7% of revenue); zero-capex PPA; GTFS 5.0 financing; turnkey RM1,150–1,600/kWh | Interval-meter-calibrated peak shaving; "~34.4% FY26 GP margin"; ST chargemen | R3, R8 |
| ERS Energy Sdn Bhd | EPCC, ZC | Private | ~150+ MWp C&I | 500 kWp solar + 200 kWh BESS at a Penang electronics plant: 35% MD cut, zero upfront capex | Direct purchase; zero-upfront PPA 15–25 yrs (fixed rate 25%–40% below TNB); green lease | Hybrid EMS with <20 ms UPS switchover; free mid-life inverter replacement; distributes Sungrow | R8, R3 |
| Cenergi SEA Bhd | ZC | Private (Khazanah / UEM) | ~100+ MWp clean energy | Operational C&I BESS with solar (>1 MWac SELCO) and biogas | Zero-capex BESS; zero-capex solar PPA (100% funded), 10–20 yrs | Background BESS controller for SELCO compliance and MD shaving | R8 |
| XPERTS.NRG (Green Xperts) | ZC | Private; partner of KLSE: KAB | 50 MW EPCC / 15 MW owned | Consortium partner with TNB for 1,000 MWh CRESS BESS | Zero-capex solar PPA; ESCO shared savings (after 12 months of interval-meter analysis); outright EPCC | Dedicated MD-shaving BESS dispatch & industrial EMS | R8 |
| EV Connection (EVC) | ZC | — | — | "First Zero-Capex BESS programme" | Shared savings 7–10 yrs, client keeps 15%–30%; sites curated via 12-month data logging by Registered Energy Managers | — | R8 |
| UniBess | ZC | — | — | — | Operating lease 7–10 yrs (fee < MD savings) with written performance SLAs and capped liquidated damages (availability, Year-10 capacity, round-trip efficiency) | — | R8, R6 |
| Kawan Renergy | ZC | — | — | — | BaaS & EaaS 10–15 yrs, backed by internal project fund | Turnkey transformer, PCS and BESS integration with automated peak discharge | R8 |
| Cheeding | EPCC (HV grid) | — | RM600M target | — | HV grid engineering; 500 kV TNB transmission licences | ~50% GP margin, 28.2% net margin | R8 |
| EVOLTS Integrators | INT | — | Engineering-led C&I projects | Dual-function MD shaving + 15–30 min ride-through for assembly, CNC, ovens; 15–20% MD reduction | Mandatory 30-day interval metering audit before sizing; turnkey delivery | — | R3 |
| VertexSol3 Compliance | INT | — | "BOMBA & ST regulatory rescues" | Gap audits of imported BESS against MS 2747:2024 2-hour fire enclosure rules; ST licensing | Consultancy & pre-procurement audits; GTFS 5.0 bankability dossiers | — | R3 |
| HO Energy Power | INT/OEM | — | — | 4.3 MW / 8.36 MWh at a shipbuilding & marine park (crane/welding spikes) | — | — | R4 |
| Elecod | INT/OEM | — | — | 1.5 MW / 2.60 MWh AC-coupled BESS at an aerospace component park | — | — | R4 |
| Tanand (EasiEMS) | EMS vendor | — | — | — | — | Early alerts (e.g. Telegram at 750 kW against an 800 kW ceiling) | R6 |
| Sungrow Power Supply | OEM | — | ">43 GWh shipped globally"; "Global #1 Tier-1 Storage OEM" | — | Supplied via Inverpower, ERS Energy, Northern Solar | PowerStack 255CS (125 kW / 257 kWh); PowerTitan 2.0 (2.5 MW / 5 MWh); liquid-cooled, ArcDefender, "Stem-Cell" grid-forming, up to 50°C without derating; EVC platform | R3 |
| Huawei Digital Power | OEM | — | — | — | Distributed via KVC Industrial Supplies, Northern Solar, Trexon | LUNA2000-215/241; LUNA2000-213KTL smart PCS; hybrid cooling; 92% VDE-certified round-trip efficiency; "One-Fits-All" | R3 |
| HyperStrong | OEM | — | Multi-GWh international | 20 MWh Plus Xnergy Perak site | Exclusively deployed via Plus Xnergy in Malaysia | HyperBlock III AC-coupled LFP; 2.5-month site execution | R3, R8 |
| LVK Power | OEM | — | — | 250 kW / 522 kWh cabinets at automotive stamping workshops | Direct supply & local integrators (e.g. Maju Antara) | LVK-GS-522ESSC-100 outdoor cabinet, IP54 liquid-cooled, integrated BMS/PCS | R3, R4 |
| EVE Energy | OEM | — | 36 MWh / 18 MW at KLIA (Feb 2026) | Partner of GSPARX | — | — | R8, R3 |
| Sigenergy | OEM | — | — | — | — | SigenStor (PV + ESS + EV microgrid) | R3 |
| Distributors / partners named | — | Inverpower, KVC Industrial Supplies, Trexon, Maju Antara; UOB U-Solar 2.0 bundles Huawei, Sungrow, Longi, Trina | — | — | — | — | R3, R6 |

## 2. Listed EPCC financials (R8 "Audited Financial Benchmarks")
| Company | Unbilled order book | Gross margin | Net margin |
|---|---|---|---|
| Northern Solar | RM119.4M LSS5 + C&I | 27.4%–37.8% | 10.1%–13.5% |
| Solarvest | RM2,370M (Aug 2026) | 28.3%–28.5% | 10.7%–12.5% |
| Pekat Group | RM994M (Jul 2026) | 25.2%–27.0% | 8.0%–10.5% |
| Sunview Group | ~RM1,169.5M | 12.0%–16.0% | 2.1%–2.8% |
| Founder Group | Active CGPP subcontracts | 6.5%–10.8% | −4.7% (pre-tax loss) |
| Cheeding (HV grid) | RM600M target | ~50.0% | 28.2% |

## 3. Zero-capex BESS provider comparison (R8; see T07 for mechanics)
| Provider | Tenure | Model | Key terms |
|---|---|---|---|
| Plus Xnergy | 15 years | Discounted MD tariff RM82.50/kW | Client keeps 15% of MD savings; provider funds 100% capex & O&M; AI EMS discharges Mon–Fri 2–10 PM |
| EV Connection (EVC) | 7–10 years | Shared savings | First zero-capex BESS programme; 15%–30% client split; 12-month data logging by REMs |
| Solarvest | 10–15 years | Powervest EaaS | Monthly fee below monthly MD savings; AI load simulator + EPMS, 20%–65% MD cuts |
| UniBess | 10 years | Operating lease + SLAs | Capped LDs for availability, Year-10 capacity, round-trip efficiency |
| ERS Energy | 15–25 years | Bundled hybrid PPA | Fixed rate 25%–40% below TNB; <20 ms backup switchover; free mid-life inverter replacement |
| Cenergi SEA | 10–20 years | Zero-capex SELCO BESS | Khazanah/UEM funding; automated controller for mandatory SELCO (≥1 MWac) storage |
| Kawan Renergy | 10–15 years | BaaS & EaaS | Internal project fund; transformer, PCS, BESS turnkey |
| XPERTS.NRG | 10–15 years | ESCO shared savings | Split on verified MD reductions after 12 months of interval analysis; partner on 1,000 MWh CRESS BESS |

## 4. Competition heatmap (R8)
Severe price competition (low barrier):
- Tier-2 utility balance-of-plant subcontracting — margins eroded to 6.5%–10.8%.
- **Small C&I rooftops (50–300 kWp)** — "Hundreds of RPVSPs pivoting from residential ATAP offer low-ball quotes (RM 2.40/Wp) by omitting roof reinforcement and structural warranties."
- **Standard BESS hardware distribution** — "Direct Chinese OEM cabinet importers face heavy price degradation without software EMS integration."

High-moat, margin-protected:
- Zero-capex / EaaS peak-demand shaving — protected by low-cost balance sheets, Sukuk facilities, REM engineers and performance guarantees.
- Hyperscale data-centre ELP & switchgear — Pekat ~30% GP in Johor / Port Dickson.
- HV grid interconnection — Cheeding (500 kV TNB transmission licences, ~50% GP, 28% net).

## 5. EMS as the moat (R8, R6)
"Top contractors rely on software moats to prevent 30-minute peak-shaving failures": Solarvest AI machine-learning EPMS; Ditrolic Net-Zero Energy OS with 15-minute interval dispatch; Plus Xnergy SOURCE weekday peak shaving [R8]. Tanand EasiEMS early alerts [R6]. EVOLTS and XPERTS.NRG / EVC require 30-day to 12-month interval-meter studies before sizing [R3, R8].
