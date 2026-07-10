# China's AI Stack — Framework v2 (refinement + v2 workstreams)

**Date:** 2026-07-10 · **Trigger:** client v1 review (14 suggestions) + director self-audit
**Status:** supersedes framework emphasis in `FRAMEWORK.md` (the 10-layer spine is retained; this adds the demand/financial dimensions and the review discipline).

---

## 1. Does the framework need refining? Yes — here's the diagnosis

v1 was a **supply-side technical map**: who makes what, capability vs. frontier, who's investable. It was strong on that axis and deliberately honest about confidence. Its structural gap — flagged in both the client review and my self-audit — is that it **never answered the demand/revenue question** that the Exponential View benchmark is built on: *who actually pays, is the revenue real, and what is priced in.* v2 closes that gap and hardens the evidence.

**What changes (v1 → v2):**
1. **Add a Demand & Revenue-Reality cross-cut.** For every key name/layer: split exposure into **domestic-substitution demand vs. global/external AI demand**; treat **open-source ≠ revenue**; quantify actual AI revenue/profit, not share/tokens. *(covers suggestions 1, 7)*
2. **Add a Financials & "What's-Priced-In" cross-cut.** Company financials, AI-segment contribution, capex scale & funding source (internal cash vs. external), **actual vs. guidance vs. consensus vs. global peers**, and what growth trajectory the market has priced. *(2, 4, 6, 11)*
3. **Broaden regulation to a global-investor lens** — beyond US Entity List/OISP to EU, Japan, UK, other Asia, EM restrictions. *(10)*
4. **Elevate Talent & R&D from a light dimension to a full workstream** with hard data (grad flows, researcher migration, patents). *(9)*
5. **Add index/reference-data rigor to the database** — GICS sector/industry, MSCI China / MSCI China A / CSI300 / HSI membership + (approx) weight, market-cap-as-%-of-market, ISIN. Enables an "AI exposure in major China indices" insight. *(12)*
6. **Accessibility upgrade** — inline footnotes for acronyms/units + a dedicated glossary/concept section, so non-industry readers can follow without dumbing down. *(3, 5)*
7. **Visualization upgrade** — replace the L0–L9 table with **relationship/flow charts** that show inter-layer dependency, and add charts wherever a paragraph is data-dense. *(13, 14)*

**The spine is unchanged:** the 10 layers (L0 Power → L9 Physical AI) remain the organizing structure. v2 adds *why the money is real* and *who can own it* on top of *who makes it*.

---

## 2. v2 workstreams (6 research pods + a standing Red-Team reviewer)

| Pod | Covers (suggestion #) | Core question |
|-----|----------------------|---------------|
| **P1 — Hyperscalers & Compute Capex** | 6, 11 | AI-cloud share of Alibaba/Tencent/Baidu/ByteDance revenue & profit; non-AI drag; capex scale/growth & **funding source** vs. US hyperscalers |
| **P2 — Models, Apps & Adoption Economics** | 7, 8 | Actual model-lab **revenue/profit** & open-source monetization; enterprise-adoption shift incl. **OpenClaw** and Alibaba/Tencent agent products |
| **P3 — Demand Mapping & What's Priced In** | 1, 2, 4 | Per-company **global vs domestic** AI-demand split; actual vs **guidance vs consensus** vs global peers; growth priced in |
| **P4 — Talent & R&D** | 9 | STEM/AI grad output, researcher migration (share of Chinese in US frontier labs), patents, lab headcounts |
| **P5 — Global Investability & Non-US Regulation** | 10 | Restrictions facing **non-US** investors (EU/Japan/UK/Asia/EM) + refined US picture |
| **P6 — Index & Reference Data** | 12 | GICS, MSCI/CSI300/HSI membership + weight, mkt-cap-%, ISIN → **index AI-exposure** insight |
| **RED-TEAM (standing)** | cross-cutting | Adversarially challenge every pod claim; force named/primary sources; police confabulation-risk items; honesty on limits |

**Director-owned (not pods):** framework, accessibility (footnotes + glossary), visualization (relationship & data charts), database schema v2, and the report/deck/DOCX rebuild.

---

## 3. The Red-Team review discipline (new in v2)

A dedicated reviewer runs **after each research batch and on the integrated v2 draft**. Its job is to disbelieve by default:
- Flag every **A/B-graded claim without a named, checkable source** → challenge or downgrade.
- Target **confabulation-prone items** — model benchmark scores, forward valuations, market caps, consensus numbers — with "**verify or mark unverified**."
- Flag **unsupported inferences / narrative leaps** (e.g. the v1 "power lets China outrun the US" claim).
- Hunt **internal contradictions & cross-pod conflicts** (e.g. Nvidia China share, Biren ticker).
- Flag **over-precision** (point figures on 10×-range estimates).
Output: a `research/review/` challenge log per pod + a final gate on the report. Nothing ships above **C** without a named source.

---

## 4. Honest scope & limitations (stated up front)
- **Consensus estimates & earnings-call transcripts** (2, 4): partial via web; `MT_Newswires` needs authorization. We use reported actuals + published guidance + credibly-sourced consensus; gaps flagged.
- **Private companies** (Huawei, ByteDance, DeepSeek, Moonshot): no audited financials — estimates only, D-confidence.
- **Exact MSCI/index weights** (12): membership is public; precise point-in-time weights are proprietary — approximate/known weights only, flagged.
- **Open-source model revenue** (7): largely indirect (cloud/API pull-through) — inherently estimate-heavy.
- **Point-13 screenshots** unavailable — relationship-chart design is our own.
- All figures remain source-tagged and A–D graded; the red-team is the honesty enforcement mechanism.
