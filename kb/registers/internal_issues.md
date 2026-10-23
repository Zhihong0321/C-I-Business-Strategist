---
id: REG-INTERNAL
title: Calculator errors and internal inconsistencies inside each report
covers: placeholder-vs-computed mismatches, hard-coded results, formula problems, self-contradictions — found while extracting each report (full detail in each source extract's "Extraction notes")
sources: [R1, R2, R3, R4, R5, R6, R7, R8, R9]
updated: 2026-10-23
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# Internal issues register

Rule for any AI reading this KB: **do not quote a report's calculator output or headline payback without checking it here.** Every interactive calculator in the 9 reports shows a static placeholder before its script runs, and most placeholders differ from what the code actually computes.

## Calculator results: placeholder vs computed at default inputs
| Report | Calculator | Placeholder on page | Computed by the code | Main problems |
|---|---|---|---|---|
| R1 | Load-curve / peak-shaving simulator | Hybrid: 800 kW billed, RM38,824/month | True window peak 750 kW → 450 kW shaved, RM43,677/month; solar-only peak 1,150 kW (not 1,200) | Billed MD hard-coded; solar never exceeds load (nothing to store); battery charging not modelled (2,700 kWh/day discharged) |
| R1 | Tax shield | — | GITA + 100% CA × 24% (38.4% solar, 48% BESS) as immediate cash | Ignores 70% statutory-income cap and CA timing |
| R1 | CRESS revenue | "RM 18.0 Mil" | RM18.00 Mil | Non-firm SAC at default PPA gives negative revenue with no warning; "gross cashflow" is net of SAC |
| R2 | BESS ROI | 1,825 kWh; RM1,642,500; 2.4 yrs | 2,288 kWh; RM2,745,098; 4.0 yrs; GITA RM658,824 | 3.5 h sizing vs "8-hour window" note; kWh input unused; 70% cap not modelled |
| R2 | 30-min interval simulator | — | Writes to the 13:30 slot (outside the ToU window) | Peak-window shading computed but never applied; bills a 13:30 block at the ToU rate |
| R3 | Bill & BESS ROI | RM229,693 → 170,748 (−25.7%); RM707,340/yr; 3.1 yrs | RM231,854 → 174,400 (−24.8%); RM689,448/yr; 1.8 yrs | Payback = BESS capex ÷ MD savings only; 2-hour battery assumed to shave full kW; GITA only 24% on BESS; HV retail fee RM200 vs table RM250 |
| R3 | Dispatch visualiser | — | Net peak stays 750 kW in all modes | Buttons swap in hard-coded arrays; battery discharges 1,050 kWh but charges 400 kWh |
| R3 | Case-study chart | — | Step bars imply 750 / 500 kW MD vs subtitle 900 kW | Energy charge rises when BESS is added |
| R4 | Bill & BESS simulator | RM135,420 → 113,102; RM267,810/yr; ~3.2 yrs | RM157,280 → 134,605; RM272,095/yr; ~2.0 yrs (at AFA 3.5 sen; 3.61 sen not selectable) | BESS RM1,800/kWh, flat 40% tax benefit; chart's BESS bar reuses base-case levy; GWh tooltip % uses a different base than the table |
| R5 | SELCO sizing & standby | "Tier 5 (RM 15,000 PSS)" | 1,500 kWh; RM18,000/month; RM396,000; "RM 15,000 (PSS)" | kWp slider and MWac dropdown independent; "mandatory" BESS shown at 0.8 MWac; CAS keyed on kWp; tariff chart static |
| R5 | Siting simulator | — | ≥3.0 m passes; with fire wall any distance down to 0.5 m passes | Wall type ignored at ≥3.0 m |
| R6 | 25-year cashflow | — | Hard-coded illustration | Yr 2→3 jump double-counts RM190,000; "financed" but no loan; RM196,000 GITA matches no stated rate; "15-yr" lease plotted for 25 yrs |
| R6 | Recommender | — | 36 branches | Pioneer firms told to buy outright to claim GITA; large branch ignores asset type; SME tenants get owner text |
| R7 | Tax engine | "48.0% of capex" | 5-yr cumulative RM912,000 (45.6%) at defaults | Unabsorbed CA discarded; 70% cap applied after CA (unlabelled); CA caption fixed at 34% |
| R7 | Cutoff audit checklist | — | — | Doesn't test RPVI conditions before granting GITE; BESS box ignored in pre-2027 branch |
| R8 | Project ROI & tax shield | RM391,800 tax; RM253,200/yr; 4.4 yrs | RM516,800 (34%); RM344,624/yr; 2.9 yrs | 34% / 24% tax factors hard-coded; gross savings (no charging cost, O&M, degradation); BESS savings at MV General rate |
| R9 | Post-solar bill simulator | RM163,144; 59.5%; "Pre-Solar Baseline" (= no-solar, no-BESS case) | RM121,829; 59.8%; RM24,265/month (solar + BESS both on by default) | Solar never cuts MD; fixed 40/60 peak/off-peak solar split; no export credit; savings = kW × RM97.06 even when kW shaved > peak (RM145,590/month on a RM200 bill); no battery size, capex or payback; "Shopping Mall" preset does nothing; static banner says 59.5% → 69.4% with solar, code gives 66.4% |

## Internal contradictions (non-calculator)
| Report | Issue |
|---|---|
| R1 | SELCO ≤1 MWac "ST Notification" vs licence required >72 kWac; "+115% to +201%" not reproducible (chart gives +115.2% to +194.6%); legacy tariff codes mixed with RP4; markdown `**bold**` shows literally |
| R2 | "+100% to +202%" not reproducible from RM30.30–45.10 (arithmetic +97.9% to +220.3%); raw LaTeX; design comment promises a PF calculator and 6 solutions (5 exist) |
| R3 | Dispatch note calls 10 AM–3 PM off-peak (overlaps the 2 PM peak); "15–30 minutes (2C)" inconsistent; RM1,350 "avg" ≠ midpoint of 1,150–1,600 |
| R4 | "Operational ~145–180 MWh" vs "85–110 MWh commissioned"; listed projects sum to 111.48 MWh; state shares sum to 89–99% and Pahang/Terengganu missing; "11 legacy tariffs" vs 12 codes listed; CRESS off-site farms counted in rooftop totals; office SME archetype bill (RM5,103) not reproducible from the stated rates (RM5,513) |
| R5 | "7 mandatory forms" lists 6; BOMBA "8–14 weeks" vs stages summing to 13–25 weeks; promised 16-week roadmap absent; spread "RM0.09–0.13/kWh" lower bound not derivable |
| R6 | Warranty peak window 08:00–22:00 vs 14:00–22:00; GTFS excludes standalone solar yet recommender finances solar via GTFS; CRESS (~26 + 20/40 sen) costs more than the grid rate it quotes, yet promises 10–30% savings; frames RP4 + ATAP as one 1 Jan 2026 shift (RP4 began 1 Jul 2025) |
| R7 | "Budget 2027 Enacted" vs its own note that gazette orders are still draft; relies on P.U. (A) 243/2024 which covers assets only to 31 Dec 2023; integrated system "current" rate stated three ways (60% split / 60% / 100%); EE-to-ACA shift unreconciled with ACA scope |
| R8 | "+162%" stated from RM30.30 but matches the RM37.00 bar; unexplained RM98.61 bar; 15 companies' MW sum (≥8,224 MW) exceeds the stated national 5,777 MW; ranking basis not stated; SELCO threshold ">72 kWp" vs "≥1 MWac"; payment stages sum to 80–110%; chart "net" ratios differ (76% / 68% / 66%) with no stated basis |
| R9 | Sector "Post-RP4 MD Share" values are its own simulator outputs, not data; design comment promises 9 case studies (7 exist), search and modals (absent); tiers don't follow its LF < 0.60 / > 0.75 rule (plastic 0.55 Tier 1, malls 0.52 Tier 2); UniBess "400 kW shaved (Capped at 200 kW target)"; Solarvest ">650 kW" from a 500 kW BESS and RM712k/yr below the RM757k its MD cut alone implies; Solarvest tax benefit 38.3% vs "~48%" in the same section; geography rows don't sum to the region cards or chart; MV General demand described as "inside peak window" |

## Figures recycled between reports
R9's case studies reuse numbers from earlier reports, so they are not independent confirmation:
| R9 case | Figures | Same as |
|---|---|---|
| Plus Xnergy zero-capex EaaS | 1,478 kW shaved; client nets RM21,520/month at RM82.50/kW vs RM97.06/kW | R8's illustrative "benchmark model" example |
| UniBess modular peak shaving | 400 kW shaved; RM38,824/month; RM465,888/year | R1's hard-coded simulator result (400 kW × RM97.06) |
| Avera Energy MV General → ToU | 500,000 kWh/month plant; RM58,945/month; 25.7% bill cut | R3's simulator placeholder (RM229,693 → RM170,748, −25.7%) |

## Common pattern
All 9 are AI-generated single-page dashboards (Tailwind + unversioned Chart.js CDN). Later reports can reuse earlier reports' numbers (see above). Design comments often promise features that are static or missing. Treat every number as a lead to verify, prioritising those in `conflicts.md`.
