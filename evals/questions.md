# Evaluation questions

Use these after loading the strategist into any AI (Claude, ChatGPT, Gemini, NotebookLM, a coding agent). Ask them in a fresh chat. A good setup passes at least 13 of 15. Re-run after every rebuild or platform change.

## Pass criteria for every answer
- First reply begins "C&I Strategist loaded — knowledge as of 23 Oct 2026."
- Cites report IDs (e.g. [R4]) and file paths.
- Disputed items name the conflict ID and give both sides.
- Nothing from outside the repo unless marked "Outside repo — unverified".
- Uses the answer format: Answer / Why / Confidence / Gaps.

## Questions and what a correct answer contains
| # | Question | Must contain | Must NOT do |
|---|---|---|---|
| 1 | What is the MV ToU demand charge and when is it measured? | RM97.06/kW (30.19 capacity + 66.87 network); 14:00–22:00 weekdays; MD = 2 × max 30-min kWh; T01 | Give legacy rates as current |
| 2 | A shop on LV General wants solar + battery to cut its maximum demand charge. Good idea? | LV has no kW demand charge (capacity + network are per kWh, 23.65 sen); battery won't cut MD; solar saves ~50.68 sen/kWh | Promise MD savings on LV |
| 3 | Does standalone solar still get GITA in 2027? | Disputed [C01]: R7/R6 say 0% from 1 Jan 2027, R3 says 60%; integrated solar + BESS 100% (Tier 1b); unverified; verify Appendix 25 | State one answer as settled |
| 4 | What must be done by 31 Dec 2026 to keep 60% GITA on standalone solar? | Invoice/capex incurred, full commissioning, MGTC application received — all by 31 Dec 2026 [R7]; 24-month window from invoice | Say "just sign the contract" |
| 5 | We plan a 1.5 MWac SELCO system. What extra obligations apply? | Mandatory BESS (≥1 h × kWp per R5, [C08]); RM12/kWp/month standby; CAS/PSS ~RM15,000; ST licence; BESS ≥5 kW licence | Omit standby charge |
| 6 | How many MV customers are there in Peninsular Malaysia? | ~26,500 (MV General ~19,120 + MV ToU ~7,380) [R4]; ~12,200 industrial; single modelled source (grade C) | Present as official TNB data |
| 7 | Which state should we target first for MV factories? | Selangor 33–35%, Johor 21–23% [R4]; weak/stale sources noted | — |
| 8 | What does Plus Xnergy's zero-capex BESS offer? | RM82.50/kW vs TNB RM97.06/kW; client keeps ~15%; 15 years; provider funds capex & O&M [R6, R8] | — |
| 9 | What does a C&I battery cost per kWh? | RM1,150–1,450 cabinets, RM1,000–1,350 containers [R8]; RM1,150–1,600 [R3, R6]; [C10] | Quote RM1,800 as typical |
| 10 | R3's calculator says BESS payback is 3.1 years. Can I tell the customer? | No — placeholder; code computes 1.8 yrs with flawed method; check internal_issues.md; payback depends on hours above target; recompute with real data | Quote 3.1 years |
| 11 | What is the CRESS system access charge? | Disputed [C03]: 14 / 20 / 25 sen firm; 40 / 45 sen non-firm; unverified | Give one number as fact |
| 12 | What licences and approvals does a 500 kWh factory BESS need? | ST licence (≥5 kW, GP/ST/No.62/2026); IEC 62619 / 63056 / UL 9540A; PEPC; Forms G & H; BOMBA MS 2747 2-hr FRR + Fire Certificate; TNB CAS if >72 kW [T09] | — |
| 13 | What will TNB demand charges be under RP5 in 2028? | Not covered; RP4 ends 31 Dec 2027; cites existing gap `rp5-tariffs-2028` (or logs one) | Invent RP5 rates |
| 14 | Who are the main competitors in C&I BESS? | Plus Xnergy, Solarvest, Sunview, Samaiden, Ditrolic, Northern Solar, Cenergi, Gentari… with figures flagged as unverified [T05, C12] | — |
| 15 | Which factories must appoint an energy manager? | EECA 2024: ≥21,600 GJ over 12 months; REM Class 1 (21,600–50,000 GJ) / Class 2 (≥50,000 GJ) [R2] | — |

## Gap logging check
After question 13, a chat AI should print a GAP block (or cite the existing gap). A coding agent with write access should create or cite a file in `gaps/open/`.
