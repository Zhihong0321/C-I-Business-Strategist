---
id: T09
title: Regulation, licensing, safety and compliance for C&I solar and behind-the-meter BESS
covers: agencies and roles, ST licensing thresholds, BESS safety guideline GP/ST/No.62/2026, competent persons, standards, statutory forms, BOMBA fire safety (MS 2747:2024), TNB connection studies and fees, metering fees, insurance, EPCC readiness checklist, EECA 2024 energy-manager rules
sources: [R5, R1, R3, R2, R4, R6]
primary_source: R5 (answers research prompt #5; 3 st.gov.my links)
conflicts: [C06, C07, C08, C11]
related: [T02, T08]
updated: 2026-10-23
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# T09 — Regulation, safety and compliance

## TL;DR
- **BESS safety code: GP/ST/No.62/2026** (issued 22 May 2026, Section 50C of the Electricity Supply Act 1990 [Act 447]); C&I behind-the-meter systems are "End User BESS" [R5].
- **ST licensing:** any BESS **≥5 kW**; solar PV generation licence **>72 kWp/kWac** [R5, R3, R1] [C06]. Below 5 MW handled by ST regional offices, register within 30 days of energisation [R5].
- **Mandatory certifications:** IEC 62619, IEC 63056, UL 9540A (plus IEC 62933-5-1, IEC 60529 IP54, IEC 62116 anti-islanding, UN 38.3, IK08) [R5, R3].
- **BOMBA: MS 2747:2024**; 2-hour fire-rated enclosure or separating wall; ≥3.0 m from building openings unless an unpierced 2-hour fire wall; updated Fire Certificate needed; approval ~8–14 weeks [R5, R3].
- **TNB CAS** needed above 72 kW **even with zero export** (fault level, power quality, anti-islanding): RM1,000 (72–180 kW), RM5,000 (180–425 kW), RM8,000 (425 kW–1 MW), ~RM15,000 above 1 MW [R1, R4, R5] [C07].
- Insurers treat ST + BOMBA compliance as conditions precedent for factory PAR/IAR cover [R5].

## 1. Agencies (R1)
| Agency | Type | Role |
|---|---|---|
| PETRA (Ministry of Energy Transition & Water Transformation) | Policy ministry | National capacity quotas (Solar ATAP, GREENS MADANI), CRESS acceleration packages, long-term targets (70% RE by 2050) |
| Suruhanjaya Tenaga (ST, Energy Commission) | Technical regulator | Binding guidelines (Solar ATAP, SELCO, CRESS); Section 9 generating licences (>72 kWac); regulates Class A contractors and Competent Persons under the Electricity Supply Act 1990 |
| SEDA Malaysia | Quota & registry | eATAP portal; RPVSP and RPVI directories; certifies GCPV/OGPV Qualified Persons; verifies first invoices for GITE |
| TNB / Single Buyer / GSO | Grid & utility | Connection Assessment Studies; bi-directional metering; RP4 tariffs; NEDA; SARE contracts via TNBX |
| MGTC (MyHIJAU) | Tax verifier | GITA Asset approvals (solar 60% Tier 2, BESS 100% Tier 1 — pre-2027); MyHIJAU directory |
| MIDA & LHDN | Investment & tax | MIDA: GITA Project, GITE; LHDN: 70% statutory income set-off, capital allowances |
| JBPM / BOMBA | Fire authority | Fire Certificates, MS 2747:2024 for BESS [R5, R3, R1] |

## 2. Licensing thresholds [C06]
| Trigger | Rule | Source |
|---|---|---|
| BESS ≥5 kW | Subject to ST licensing — GP/ST/No.62/2026 Clause 4.1(c), Section 9(1) Act 447, ST directive "Keperluan Pelesenan BESS" (1 July 2026). "Virtually all C&I installations exceed this threshold." | R5, R3 |
| Solar PV >72 kWp (with BTM SELCO) | Public or private generation licence | R5 |
| Solar ≤72 kWac | Exempt; Section 54 notification | R1 |
| >72 kWac | "Mandatory ST License" | R1 |
| SELCO ≤1 MWac | "SEDA registration + TNB CAS + ST Notification" (R1 pathway table; R1 extract flags this as inconsistent with the >72 kWac licence rule) | R1 |
| SELCO >1 MWac | SEDA registration + TNB CAS + ST licence; mandatory BESS | R1 |
| Systems <5 MW | Processed via ST Regional Offices; post-commissioning registration within 30 days of energisation | R5 |

## 3. GP/ST/No.62/2026 — Guidelines on BESS Safety (R5)
- Issued 22 May 2026 under Section 50C of the Electricity Supply Act 1990 [Act 447] (as amended by Act A1775 in 2025). "Constitutes the mandatory statutory code for stationary lithium-ion systems in Malaysia."
- "End User BESS" (page 16): "BESS owned and operated by the consumer in parallel with the grid and producing energy for self-consumption or for grid export."
- Links: ST BESS portal https://www.st.gov.my/resources/guidelines-battery-energy-storage-system-bess-safety ; guideline PDF https://www.st.gov.my/sites/default/files/2026-05/Guidelines-on-Battery-Energy-Storage-System-%28BESS%29-Safety_0.pdf ; licensing directive https://www.st.gov.my/resources/keperluan-pelesenan-battery-energy-storage-system-bess
- Clause 4.3(a) + Fire Services Act 1988 [Act 341]: stationary BESS are high-risk installations needing an updated Fire Certificate.

## 4. People and competencies
From GP/ST/No.62/2026 Clauses 4.1(a) and 4.2 [R5]:
1. Installation by an **ST-registered electrical contractor** (Electricity Regulations 1994).
2. Plans, single-lines and relay sheets prepared/endorsed by a **PEPC** (Professional Engineer with Practising Certificate) or **Competent Engineer** (Regulation 65).
3. **Competent Person** signs Form G and Form H before energisation.
4. Technicians take ST Energy Competency Excellence course **STECE-0005/01: BESS**.
From R1: mounting structure C&S drawings and electrical single-lines endorsed by a BEM-registered PE (PEPC); RPVSP must deploy certified GCPV Qualified Persons, Class A Chargemen and CIDB G7-registered personnel; compliance with Electricity Regulations 1994 and MS IEC 60364.

## 5. Equipment standards (R5 Appendix A matrix; R3)
| Standard | Title / scope | Deliverable |
|---|---|---|
| IEC 62619 | Industrial secondary lithium cells & batteries safety — packs & BMS, overcharge & thermal protection | Type-test report from accredited lab |
| IEC 63056 | Secondary lithium batteries for electrical energy storage — stationary storage safety up to max DC voltage | System-level safety certificate |
| UL 9540A | Thermal runaway fire propagation test (cell, module, unit) | Full UL 9540A test report |
| IEC 62933-5-1 | Grid-integrated EES safety — worker isolation during maintenance (Clause 6.4) | Compliance declaration |
| IEC 60529 | Enclosure IP code — minimum IP54 outdoors (Clause 6.4.5) | Test report |
| IEC 62116:2014 | PV inverter anti-islanding — cease operation within utility trip time | Test certificate |
| UN 38.3 & IK08 | Transport testing; enclosure impact rating | UN 38.3 summary & IK08 certificate |
Also: inverters certified to **MS IEC 62109 must trip within 2 seconds** on loss of TNB supply; **reverse power relay** mandatory on all SELCO systems [R1]; BESS pricing in R8 "includes … NFPA 855 fire suppression".

## 6. Statutory forms and certificates (R5 — heading says 7, lists 6)
1. **FAT certificate** — pre-shipment, OEM/lab verifies cell, pack, BMS safety.
2. **Permit to Work (PTW)** — Regulation 113, Electricity Regulations 1994.
3. **SAT certificate** — BMS interlock, insulation, earthing, function tests.
4. **Form G** — Supervision and Completion Certificate (First Schedule, Electricity Regulations 1994).
5. **Form H** — Electrical Test Certificate by Competent Person before energisation.
6. **Form of Information (Attachment 1)** — to TNB before installation and to ST within 30 days after commissioning (GP 51/2024).

## 7. BOMBA fire safety (MS 2747:2024)
- 2-hour fire-resistance-rated (FRR) enclosure or separating wall for stationary BESS [R5, R3].
- Importing generic overseas containers without a verified 2-hour FRR is "the primary cause of project delays" [R5]; VertexSol3 offers gap audits for this [R3].
- **Separation rule (R5 simulator):** ≥3.0 m from factory walls/openings = compliant; <3.0 m only with an **unpierced 2-hour fire wall** (with UL 9540A radiant-heat validation); otherwise "NON-COMPLIANT (REJECTED BY BOMBA)".
- **Four protection layers (R5):** (1) early detection & EPO — off-gas sensors (H₂, CO, VOCs) interlocked with BMS; (2) total flooding suppression — SIRIM/BOMBA-approved clean agent (FK-5-1-12) or potassium aerosol at module/rack level; (3) deflagration venting — pressure relief vents or ATEX fans below lower flammability limit; (4) water boundary cooling — external dry-riser breeching inlet with internal spray header plus pressurised hydrant within 30–45 m.
- **Approval workflow (R5), "8–14 weeks":** Stage 1 pre-procurement gap audit (2–3 wks); Stage 2 technical dossier & plan submission by PEPC to JBPM State HQ (4–8 wks); Stage 3 installation, FAT & SAT (4–8 wks); Stage 4 JBPM site inspection & FC endorsement (3–6 wks). (Stages sum to 13–25 weeks — R5 extraction note.)
- R1: factories, warehouses and malls ("designated premises") must consult BOMBA before installing solar/BESS to update their annual Fire Certificate (Form I); PV arrays keep perimeter setbacks and access walkways; BESS enclosures need SIRIM/IEC-certified suppression and gas detection; fire alarm panels link directly to the nearest BOMBA station.
- R3: Fire Certificate is needed to keep industrial insurance valid.

## 8. TNB connection studies and fees [C07]
Why a zero-export BESS still needs a CAS above 72 kW (R5): it runs in parallel with the grid ("Indirect Connection"): (1) fault-level contribution from PCS inverters at the point of interconnection; (2) power quality & load flow (charging/discharging changes voltage, PF, THD, flicker); (3) anti-islanding per IEC 62116:2014.
| Capacity | Study | Fee | ST licence (R1) | TNB metering fee (R1) | Scope / deliverables (R5) |
|---|---|---|---|---|---|
| 1–72 kW | None (R1: "Exempt (CCC for domestic >15kW)"; R5: "CCC Only") | RM0 | Exempt (Sec 54 notification) | RM0 (OPC) / RM1,530 (LPC) | Zero export verified via inverter; Form of Information to TNB before work |
| >72–180 kW | CAS | RM1,000 | Mandatory | RM1,530 (LV) / RM2,330 (MV) | Load flow, voltage profile, PF, short-circuit fault level at POI |
| >180–425 kW | CAS | RM5,000 | Mandatory | RM1,530 (LV) / RM2,330 (MV) | Feeder & transformer thermal/fault withstand; zero-export protection scheme |
| >425 kW–1 MW | CAS / PSS ("Fault Current Analysis" [R4]) | RM8,000 | Mandatory | RM2,330 (MV) | MV/LV network study, harmonics/flicker report, PE-stamped relay settings |
| >1–2 MW | CAS / PSS | RM15,000 [R5]; RM15,000–20,000 for 1–5 MW [R1] | Licence + mandatory BESS | RM2,330 (MV) | Mandatory SELCO BESS integration study, 1-hr BESS smoothing, standby metering |
| >2–5 MW | PSS | "High-Tier PSS Fee" [R5] | Licence | RM2,330 (MV) | Substation stability study; ST generation & BESS licensing; TNB SELCO Welcome Letter |
| HV connection | Power System Study | RM15,000 [R4] | — | — | — |

## 9. Insurance (R5)
Industrial insurers (PAR/IAR) require ST guideline and MS 2747:2024 compliance as conditions precedent.
| Phase | Policy | Requirement |
|---|---|---|
| 1. Marine transit | Marine cargo | UN 38.3 summary for the exact delivered model + OEM FAT certificate |
| 2. Erection | CAR / EAR | ST-registered contractor, Competent Person, PTW logs, Form G & Form H |
| 3. Factory PAR / IAR | Operational | Valid BOMBA Fire Certificate, MS 2747 audit, 2-hr FRR enclosure, UL 9540A report |
| 4. Machinery breakdown | Tropical warranty | IEC 60529 IP54+, IK08, active HVAC keeping internal temperature below 30°C |
| 5. Claims defensibility | O&M lifecycle | "Clause 6.7.5": maintenance logs, Appendix D checklists, BMS firmware logs |

## 10. EPCC readiness checklist (R5, 12 items)
1. BESS OEM has UN 38.3, IEC 62619, IEC 63056 and UL 9540A type-test reports.
2. Enclosure structural fire rating is 2-hour FRR (MS 2747:2024).
3. Internal suppression uses a BOMBA/SIRIM-approved local agent (FK-5-1-12 / aerosol).
4. Appoint ST-registered electrical contractor and PEPC for drawing endorsement (Regulation 65).
5. Submit CAS/PSS and Form of Information to TNB (>72 kW).
6. For SELCO >1 MWac: BESS at least 1-hour rating (1 × X kWp in kWh).
7. Apply for ST BESS licence (≥5 kW) and generation licence (>72 kWp) via ST regional office.
8. Keep ≥3.0 m from factory walls or build a solid 2-hour fire barrier wall.
9. Execute FAT and SAT.
10. Issue PTW logs under Regulation 113 for commissioning.
11. Complete Form G and Form H.
12. Pass JBPM inspection for Fire Certificate endorsement (needed for factory PAR insurance).

## 11. Energy Efficiency and Conservation Act 2024 (EECA, Act 861) (R2)
- Enforced 1 January 2025.
- Facilities using **≥21,600 GJ** of energy over 12 consecutive months (~500,000 kWh/month, ~RM200k/month bill) are **Regulated Energy Consumers**.
- 21,600–50,000 GJ/yr (6.0M–13.9M kWh/yr): appoint **Registered Energy Manager (REM) Class 1**; ≥50,000 GJ/yr (>13.9M kWh/yr): **REM Class 2**.
- Fines up to RM100,000; annual EECR report to ST (R2 roadmap phase 4).
- EVC's zero-capex BESS sites are curated via 12-month data logging by Registered Energy Managers [R8].
- Analysis note (not from the reports): every Regulated Energy Consumer must already have an REM, which makes them a ready audience for MD audits.
