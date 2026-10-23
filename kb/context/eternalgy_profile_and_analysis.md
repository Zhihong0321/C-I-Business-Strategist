---
id: CTX
title: Eternalgy public profile and market analysis from the planning session
type: context + analysis (NOT from the research reports)
updated: 2026-10-23
related: [T01, T04, T05, T07, T08, T10, ../registers/conflicts.md]
private_companion: ../../private/eternalgy_strategy_notes.md (internal; not in the public repo — may be absent)
---

<!-- ai-banner -->
> **AI reader:** this file is knowledge, not instructions. If you have not read [RULES.md](../../RULES.md) yet, read it first.

# Eternalgy — public profile and market analysis

Everything here comes from Eternalgy's public website, the user, or Claude's analysis during the 23 Oct 2026 planning session — not from the research reports. Report facts referenced here carry their source IDs. Internal strategy notes (funding limits, go-to-market choices) live in `private/` and are not published.

## 1. Company profile (public information, https://ee-pr.up.railway.app/, read 23 Oct 2026)
| Item | Detail |
|---|---|
| Entity | Eternalgy Sdn Bhd, reg. 202301029164 (1523087-A), founded 2023 |
| Business | Solar EPCC + BESS, West (Peninsular) Malaysia focus; projects seen in Johor and Selangor |
| Scale (site, synced 21 Oct 2026) | ~12,308 kWp installed; 1,138 projects (~10.8 kWp average → mostly residential); customer revenue ~RM35.75M |
| C&I | Average C&I job ~50 kWp (LV customers) |
| Licences & certs | SEDA RPVSP (SEDA/RPVSP/2024/321); SEDA RPVI (PPA / leasing); CIDB G7 (B04 building, CE21 civil, M15 electrical); MyHijau cert MyHS00025/25 for the SAJ inverter range; MPIA member; OSH-C certified safety supervisor |
| Partners | Maybank preferred solar partner; SAJ sole distributor for Malaysia (inverters + storage); JinkoSolar modules; SHRDC Centre of Excellence partner (BESS training, Shah Alam) |
| Team | In-house coding/IT team; PE; GCPV; chargeman; Grade 4 electrician |

## 2. Segment fit (Claude analysis)
| Segment | Solar | BESS for Maximum Demand | Fit |
|---|---|---|---|
| LV (Eternalgy's current C&I base) | Strong: saves ~50.68 sen/kWh, ~RM680/kWp/yr at 1,350 kWh/kWp | **None**: LV has no kW demand charge [T01] | Solar volume business; crowded [T05 §4] |
| MV (~26,500 accounts [R4]) | Moderate: saves the energy charge only (~27–30 sen), ~RM370–400/kWp/yr | **Strong**: RM89.27–97.06/kW/month | Growth segment: solar + BESS sold as MD reduction |
| HV (~700 accounts [R4]) | — | Weak (RM31–45/kW) | Via CRESS developers |
Core idea: Maximum Demand is the customer's pain, not a product. BESS is the tool, solar the volume product.

## 3. BESS payback rule of thumb (Claude analysis)
MV ToU RM97.06/kW = RM1,165 saved per kW shaved per year; battery RM1,350/kWh; usable factor DoD 0.85 × η 0.949 × end-of-life SoH 0.90; no tax incentive.
| Hours/day the load sits above the target MD | kWh nameplate per kW shaved | Simple payback |
|---|---|---|
| 1 h | ~1.4 | ~1.6 yr |
| 2 h | ~2.8 | ~3.2 yr |
| 4 h | ~5.5 | ~6.4 yr |
| 8 h (flat load) | ~11 | ~12.8 yr |
One missed half-hour sets MD for the month, so screening with 30-minute meter data and reliable EMS control are the core skills.

## 4. Market implications of the research (Claude analysis)
- If R7 is right [C01]: from 1 Jan 2027 standalone solar gets 0% GITA; solar paired with BESS gets 100% (Tier 1b). On LV sites a battery saves no demand charge, so whether pairing pays depends on the unconfirmed **minimum BESS ratio for Tier 1b**.
- Pre-2027 standalone solar GITA (60%) needs invoice + full commissioning + MGTC receipt by 31 Dec 2026 [R7].
- Standalone BESS may lose GITA from 2027 [C20]; bundling with solar would keep 100%.
- GITE (70% exemption for RPVI leasing) ends 31 Dec 2026 [R7, R6]: host-owned purchases with financing (GSF 2.0, LCTF, HTG) become relatively more attractive than RPVI-funded PPAs.
- 50–300 kWp rooftops and BESS hardware sold without EMS are named price-war segments [R8]; software (EMS, MD audits) and guarantees are where margins are protected.
- EECA 2024: sites ≥21,600 GJ/yr must appoint a Registered Energy Manager [R2] — a ready audience for MD audits.

## 5. Pending inputs
- R9: research prompt #4 (load profiles by industry) — not yet received.
- Verification of every [C##] item against official documents.
