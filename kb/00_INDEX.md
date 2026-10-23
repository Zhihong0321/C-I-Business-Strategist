---
id: INDEX
title: Malaysia C&I Solar + BESS knowledge base — start here
owner: Eternalgy Sdn Bhd (solar EPCC + BESS, West Malaysia)
built: 2026-10-23
built_from: 8 AI-generated HTML research reports in raw/reports/ (R1–R8); R9 pending
purpose: AI-readable, lossless distillation of the research, plus cross-report synthesis, for planning Eternalgy's C&I market entry
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../RULES.md) yet, read it first.

# Start here

## What this is
**AI readers: read `../RULES.md` and `../MIND_MAP.md` before this file.**

A markdown knowledge base built from the research reports in `../raw/reports/`. It has three layers:
1. **`sources/`** — one complete extract per report (R1–R8). Lossless: every number, table row, chart value, calculator formula and link from the HTML is here. Each was checked with a script that compares every number and link in the HTML with the markdown (0 missing; leftovers were Tailwind class names only).
2. **`topics/`** — cross-report synthesis by subject (T01–T10). Every fact carries its source tag, e.g. `[R4]`; disputed facts carry a conflict tag, e.g. `[C01]`.
3. **`registers/`** — conflicts between reports, calculator errors and internal inconsistencies, every citation with a quality grade, and a glossary.
Plus `01_BIG_PICTURE.md` (the whole market on one page) and `context/` (Eternalgy's profile and the planning session's conclusions — analysis, not report content).

## Reading order
- **Need the whole picture fast:** `01_BIG_PICTURE.md`.
- **Need a specific fact:** the relevant topic file, then its source extract for exact wording.
- **Before relying on a number:** check `registers/conflicts.md` (cross-report disputes) and `registers/internal_issues.md` (calculator errors).
- **Planning for Eternalgy:** `context/eternalgy_profile_and_analysis.md`, then `topics/T10_strategy_playbooks_from_reports.md`.

## File map
| Path | Contents |
|---|---|
| `01_BIG_PICTURE.md` | 10-point market story, key-numbers cheat sheet with confidence grades, solid vs shaky, top open questions |
| `topics/T01_tariff_rp4_and_maximum_demand.md` | RP4 rates, legacy mapping, ToU window, MD measurement, PF surcharge, General↔ToU switch maths, typical bills |
| `topics/T02_solar_schemes_atap_selco_cress.md` | NEM 3.0 closure, Solar ATAP, Enhanced SELCO (mandatory BESS, standby), CRESS terms and agreements, utility tenders, scheme volumes |
| `topics/T03_tax_incentives_gita_gite.md` | GITA Asset/Project, GITE, Budget 2027 changes (disputed), 31 Dec 2026 cutoff, utilisation rules, exclusions, ACA/SVA/GSF 2.0 |
| `topics/T04_market_size_and_geography.md` | Macro indicators, accounts and GWh by RP4 category, solar additions, installed BESS, TAM by voltage tier, state-level MV concentration |
| `topics/T05_competitors_and_providers.md` | Master table of ~30 companies (EPCCs, zero-capex providers, integrators, OEMs), listed financials, competition heatmap, EMS moats |
| `topics/T06_pricing_margins_payment_terms.md` | Solar RM/Wp, BESS RM/kWh, O&M, warranty adders, margins by segment, payment milestones, payback/IRR claims, calculator outputs |
| `topics/T07_financing_and_business_models.md` | BNM facilities, GTFS 5.0, bank products, SARE / bilateral / CRESS PPAs, zero-capex BESS models, guarantees and LDs, preferences by size, decision logic |
| `topics/T08_bess_technical_and_sizing.md` | Why BESS, load-curve examples, topologies and models, sizing rules, EMS, MD mitigation ladder, site suitability |
| `topics/T09_regulation_safety_compliance.md` | Agencies, licensing thresholds, GP/ST/No.62/2026, competencies, standards, forms, BOMBA, TNB CAS and fees, insurance, readiness checklist, EECA 2024 |
| `topics/T10_strategy_playbooks_from_reports.md` | Each report's recommended strategies, archetypes and roadmaps |
| `registers/conflicts.md` | C01–C20: where reports disagree, severity, what would settle it |
| `registers/internal_issues.md` | Placeholder vs computed calculator results and self-contradictions in each report |
| `registers/citations.md` | All 26 hyperlinks (graded A–D) and all named laws, guidelines and standards |
| `registers/glossary.md` | Acronyms and terms |
| `context/eternalgy_profile_and_analysis.md` | Company profile; working conclusions; what the new research changes for Eternalgy (analysis) |
| `sources/R1…R8_*.md` | Lossless per-report extracts (front matter, key-claims index, full body, charts, calculators with computed outputs, data tables, links, extraction notes) |

## Source registry
| ID | Extract | Original HTML (`raw/reports/`) | Modified | Answers | Links | Notes |
|---|---|---|---|---|---|---|
| R1 | `sources/R1_strategy_hub.md` | malaysia_c_i_solar_bess_executive_intelligence.html | 13:27 | First-round report (pre-prompts): strategy hub for an RPVSP + RPVI EPCC | 0 | Oldest; frames 31 Dec 2026 as a full "tax cliff"; no Budget 2027 |
| R2 | `sources/R2_md_mitigation_portal.md` | malaysia_tnb_maximum_demand_c_i_mitigation_portal.html | 14:15 | First-round: TNB Maximum Demand mechanics and mitigation | 0 | Best MD maths; LaTeX unrendered |
| R3 | `sources/R3_bess_solutions_dashboard.md` | malaysia_c_i_bess_solutions_dashboard.html | 14:15 | First-round: BESS market, provider directory, architectures | 0 | 12-provider directory, unsourced |
| R4 | `sources/R4_market_explorer.md` | malaysia_c_i_solar_bess_market_explorer.html | 14:51 | Research prompt #2 — market size by tariff segment | 23 | Most-cited report; several weak/stale sources |
| R5 | `sources/R5_bess_compliance_navigator.md` | malaysia_bess_compliance_navigator.html | 14:51 | Research prompt #5 — BESS regulation and fire safety | 3 (st.gov.my) | Quotes guideline clauses |
| R6 | `sources/R6_financing_2026.md` | malaysia_c_i_solar_bess_financing_2026.html | 14:53 | Research prompt #6 — financing and business models | 0 | Recommender with 36 branches |
| R7 | `sources/R7_green_tax_portal.md` | malaysia_green_tax_incentives_portal.html | 15:02 | Research prompt #1 — green tax incentives after Budget 2027 | 0 (names legal docs) | Primary source for Budget 2027; lists 5 unconfirmed items |
| R8 | `sources/R8_market_benchmark_2026.md` | malaysia_c_i_solar_bess_market_2026.html | 15:07 | Research prompt #3 — competitors and pricing | 0 | Top 15 competitors, prices, margins |
| R9 | — | (pending) | — | Research prompt #4 — load profiles and target industries | — | Still running at build time; add as `sources/R9_*.md` and update T08 |
Research prompts: `../research/round2_research_prompts.md`. Internal material (MD audit tool spec, strategy notes) is in `../private/`, which is not published.

## Conventions
- `[R#]` = source report; `[C##]` = entry in `registers/conflicts.md`; `[T##]` = topic file.
- Text quoted in "double quotes" is the report's wording.
- "Analysis note" or anything under `context/` = Claude's analysis, not report content.
- Dates are absolute; "today" at build time = 23 Oct 2026.
- Nothing here has been checked against official sources yet. All 8 reports are AI-generated; treat figures as leads, especially those graded C or D in `01_BIG_PICTURE.md`.

## Maintenance
- New report: extract it to `sources/R#_*.md` with the same template; run the coverage checker; then update the topic files it touches, `registers/conflicts.md`, `registers/citations.md`, the cheat sheet and this registry.
- Verified a disputed fact: update its conflict entry's Status, then the topic file and cheat-sheet grade.
