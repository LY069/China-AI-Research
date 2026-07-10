# P4 — Talent & R&D (v2)

**Pod:** P4 · **Scope:** Talent & R&D (T) cross-cut · **Prepared:** 2026-07-10
**Data as-of:** figures dated individually below; most recent hard data is 2024–2025 (conference/graduation cycles lag ~12–18 months; 2026 figures are mostly projections or in-year policy announcements).

---

## Scope

v1 treated Talent & R&D as a light cross-cutting dimension (T in FRAMEWORK.md §2) with no dedicated pod and almost no hard data. v2 elevates it to a full workstream, answering four questions: (1) how big/fast-growing is China's STEM/AI graduate pipeline; (2) where do China's best AI researchers actually work — the stock-and-flow question that determines whether raw output converts into frontier capability; (3) what does China produce in papers/patents, and who has the deep organizational benches; and (4) what talent bottlenecks still bind, especially chip-design/EDA — the layer (L1) v1 flagged as the stack's most binding technical constraint. Throughout, flow (graduates/year) is distinguished from stock (researchers currently active), and volume (papers filed) from quality/selectivity (top-tier acceptance, most-cited papers) — collapsing these is the most common error in talent commentary.

This pod carries no "investability" table in the P1–P3 sense — talent is an input factor, not a security — but closes with a short read on which named entities in `company_master.csv` the data implies have the deepest or thinnest benches, relevant to underwriting the durability of their model/chip-design output.

---

## 1. Supply: the STEM/AI graduate pipeline

China's scale advantage in STEM output is real, but a single clean "AI graduates/year" series does not exist — MOE does not publish one. What exists: (a) total STEM PhD counts, (b) total university graduates, (c) a fast degree-reclassification push toward AI-labeled majors.

- **STEM PhDs:** ~50,000 STEM doctorates in 2022 (+13.7% YoY; engineering 59.1% of the total) — Georgetown CSET, based on MOE/NBS statistics (WEB-807, C). Trend-line projections put China at **~77,000/year by 2025 vs. ~40,000 in the US** (WEB-807/WEB-808, D — a projection, not a filed count; CSET flags it as directional). Ex-foreign-nationals, the domestic US STEM-PhD count would be roughly 3x smaller than China's — CSET's framing for why the US's historical AI-talent edge runs through *importing* Chinese-educated researchers rather than out-producing China (ties to §2).
- **Total university graduates:** 12.7 million expected for 2026 (MOE, +480,000 vs. 2025) (WEB-810, B).
- **Curriculum shift toward AI:** 2021–2025, Chinese universities discontinued/suspended 12,200 undergraduate programs and introduced ~10,200 new ones, tech/digitalization-weighted; 38 new majors approved for 2026-27, mostly AI/digitalization (WEB-811/WEB-812, B/C). This is a **policy action, not yet a graduation-count** — AI-labeled cohorts under the new majors won't show in output data until ~2028–2030.
- **National AI research workforce:** one secondary report (via TMTPost, unverifiable methodology, **D**) claims China's AI research workforce grew from <10,000 (2015) to ~52,000 (2024), led by CAS (~3,453), Tsinghua (~2,667), PKU (~2,123). Flagged D — not a clean census.
- **Talent-gap (demand side):** McKinsey is cited (via TechNode) projecting a shortfall of **up to 4 million AI professionals by 2030** (WEB-822, C, primary report not accessed). A separate "~30M digital-economy gap by 2025 / ~6M AI professionals by 2030" claim in secondary China-policy commentary is weaker-sourced — flagged D, not relied upon.

**Read:** "China out-produces the US in STEM PhDs" is well-supported directionally (C, trending B via CSET's 2022-vintage data); any specific 2025/2026 graduate count, or any talent-gap figure (4M/5M/30M), is D.

---

## 2. Stock & flow: where do China's best AI researchers actually work?

This is the highest-value and best-sourced part of the pod, via **MacroPolo's Global AI Talent Tracker** (GATT) — the canonical dataset the brief pointed to. GATT's methodology: it identifies authors publishing at the three most competitive AI/ML venues (NeurIPS, ICML, ICLR), classifies each by country of undergraduate education, and tracks current institutional affiliation. This is a **stock-and-flow census of elite researchers**, not a survey of the whole AI workforce — a distinction to keep central, since headline numbers ("38% of top researchers are China-educated") are frequently misquoted as "China has 38% of AI talent."

**Production (where they were educated):** the share of GATT's tracked elite researchers with a China undergraduate degree rose **27% (2017) → 29% (2019) → 38% (2022–2024 vintage)** (WEB-801/802/803, C — MacroPolo's own site 403'd to automated fetch, so relayed via MIT Technology Review's summary of GATT 2.0/3.0). China overtaking the US as the largest single undergraduate-origin source of elite AI researchers is the most robust finding in this literature, repeated consistently across tracker versions.

**Retention/location (the more decision-relevant number):** **72% of China-educated elite researchers now work at US institutions; only 11% remain in China** (down from 16% in 2019) (WEB-801/803, C) — historically most of the flow left. **US institutions employ 59% of the world's elite AI researchers** (up from 51% in 2017), built almost entirely on imported talent: US- and China-origin researchers together made up 75% of the US researcher pool in 2022, up from 58% in 2019 (WEB-801/802, C). Graduate-school "stickiness" is strong both ways — ~80% of US-grad-school researchers stay in the US, ~90% of China-grad-school researchers stay in China (WEB-801, C) — meaning *where the graduate degree happens*, not the undergrad degree, best predicts eventual location; this favors future retention as China's own PhD training scales up.

**Recent reflow signal — DeepSeek as a case study, not yet a national trend:** analysis of DeepSeek's public researcher roster (Hoover Institution, Rest of World) finds ~70% of researchers with 5+ years' US experience have returned to China; the most common individual path is "China → US → China" (38.8%), vs. 12.5% "China → US → stayed" (WEB-813/814, C/D — single-company roster analysis, not population-representative). One-third of DeepSeek's ~31 core researchers never left China. We treat this as **suggestive evidence of reflow in a specific high-profile cohort, not proof of a broad national reversal** of the 72%-stay-in-US pattern — GATT's aggregate retention figures predate DeepSeek's 2025 breakout and have not been re-measured at population scale since.

Policy is trying to convert the anecdote into structure: China's **K-visa** (effective 1-Oct-2025) is a new sponsor-free visa for young global STEM talent, explicitly pitched against the US's 2025 H-1B fee hike (WEB-821, B); rebranded "Thousand Talents" successor programs ("Young Thousand Talents"/"Qiming") offer RMB 1–3m start-up grants plus housing/salary to under-40 recruits (WEB-825/827, C). On the US side, May 2025 saw a State Department pause on new student-visa interviews pending expanded vetting, announced "aggressive" scrutiny/revocation of visas for Chinese/HK students in "critical fields," and a proclamation suspending entry for Chinese grad students/researchers tied to military-civil fusion (undergrads exempt) (WEB-819/820, B). Independently, Stanford's 2026 AI Index reports **AI-talent migration into the US down 89% since 2017, 80% of that decline in the most recent year** (WEB-804/806, C — primary PDF 403'd, relayed via Fortune). Two independent 2025-26 signals (US visa policy + measured migration decline) point the same direction as China's pull policies, but **the size of any reflow remains unquantified (D)** beyond the single-company DeepSeek data point.

**Read:** the pre-2025 stock data (72%/11% US/China split) is the best-sourced number in this pod (C, named public methodology). The current-year reflow narrative is directionally corroborated but not population-quantified — flag any "X% of researchers have returned" claim beyond DeepSeek as unverified.

---

## 3. Output: papers, top-conference share, patents, and the organizational bench

**Publications & citations:** Stanford's 2026 AI Index reports Chinese researchers produced **23.2% of global AI publications and 20.6% of citations in 2025**, vs. 12.6% publication share for the US (WEB-804/806, C — primary PDF 403'd to fetch). China's share of the *top 100 most-cited* AI papers grew from 33 (2021) to 41 (2024) (same source, C) — the volume lead is translating into rising influence, not just count.

**Elite-conference share — a nuanced picture:** at NeurIPS 2025/ICLR 2026, Chinese-institution affiliations are reported at roughly **40% of poster-track vs. ~30% of oral-track** (the more selective slot), with the US pattern inverted (~30% poster/~40% oral) (WEB-823/824, C — secondary aggregator reporting, not conference-published statistics; treat as directional). Tsinghua alone is reported to have had 100+ NeurIPS 2025 papers, more than any other global institution (WEB-823, C). Read: **China now leads on volume/breadth at top-tier venues; the US still over-indexes on the most selective (oral) slots** — a quality/selectivity gap layered atop a reversed volume gap. Treat the exact 40/30 split as D, the direction as C.

**Patents:** China filed **73,718 PCT applications in 2025 vs. 52,617 for the US**, a lead held since 2019 (WIPO, WEB-816/817, B — named primary statistical source). Huawei was the single largest corporate PCT filer globally in 2024 (6,600 applications) (WEB-816, B). In generative-AI patent families, China filed ~38,210 vs. ~6,276 for the US (~6x); Stanford's AI Index separately reports China filing 69.7% of all AI patents worldwide (WEB-816/WEB-804, C). **Caveat: patent-filing volume is a weak proxy for commercial value** — China's own regulators and outside academics have flagged utility-model/low-value filings inflating the raw count, and WIPO/Stanford commentary both note the US still produces more commercially influential IP. Patent-count leadership is well-sourced (B); "China leads on patent *value*" is an inference we explicitly do not make.

**Corporate & academic labs (organizational bench depth):** thin, inconsistent data — flagged D throughout. ByteDance is reported the largest single AI employer in Beijing (~30,000 on its Beijing campus, ~40% of global headcount; a "Top Seed" frontier-research group in the low thousands); Tencent AI Lab is reported at 500+ researchers (WEB-828, D, single blog-style source, unverified against company disclosure). Huawei Noah's Ark Lab (founded 2012; Beijing/Shenzhen/Shanghai/HK/London/Paris/Edmonton) and Alibaba DAMO Academy have no reliable current headcount in open sources. Tsinghua's newly consolidated College of AI (Apr-2024, led by Turing laureate Andrew Yao) and PKU's AI institute correspond to the ~2,667 / ~2,123 self-identified-researcher figures flagged D in §1.

**Read:** national output data (publications, citations, patents) is reasonably well sourced (C/B) and shows a genuine, multi-year China lead in volume, now rising in quality/influence too. Organization-level bench depth is poorly disclosed across the board — none of Huawei, Alibaba, Tencent or ByteDance publish audited researcher headcounts, so no reliable "biggest bench" ranking is possible; only ByteDance and Tencent have any (unverified) public figure at all.

---

## 4. Bottlenecks: where the talent gap still binds

The clearest, most consequential bottleneck is not general AI/ML talent (where China now has scale) but **advanced chip-design and EDA talent** — directly relevant to L1 (semi equipment & EDA), which v1 flagged as the single most binding technical constraint in the whole stack.

- Industry sources (recruiting-firm market reports, not government statistics) put China's semiconductor talent gap at **200,000–300,000 professionals**, concentrated in IC design, EDA tool development and advanced packaging (WEB-818, D — industry/recruiter estimate, not independently audited). The same reporting states technical-director-level talent with hands-on experience at sub-5nm design nodes numbers **under 100 people nationally**, against demand for 300+ (WEB-818, D).
- EDA specifically is flagged as facing a "severe shortage of high-end algorithm talent" capable of building a full-flow, internationally competitive toolchain — consistent with v1's finding (Empyrean and peers) that Chinese EDA remains behind Synopsys/Cadence at the most advanced nodes; the bottleneck is as much human capital (the small number of engineers who have actually built production EDA flows at leading nodes) as it is IP/tooling.
- Compensation is spiking as a symptom: AI-engineer recruitment demand reportedly rose 25% YoY in Q3 2025, with average monthly AI-engineer salaries near RMB 21,370 and robotics/algorithm engineers near RMB 27,000 (+10% YoY) (WEB via search, D) — consistent with a tight, bidding-up labor market at the applied end, even as elite-research-conference output (§3) shows abundance at the academic end. **The bottleneck is concentrated in a narrow band of senior, production-proven chip-design/EDA specialists, not in AI/ML researchers broadly** — a distinction the market commentary around "China's talent shortage" frequently blurs.

---

## 5. What this means for the named companies in the database

Talent depth is an input, not a security, so this is a short qualitative read rather than a pricing call:
- **DeepSeek** (`deepseek`) is the clearest current example of a China-domestic-plus-reflow research bench converting directly into frontier model output — but its ~31-person "core team" scale (per the public-roster analyses in §2) also means its bench is small and concentration risk (key-person dependency) is real, unlike a large corporate lab.
- **Huawei** (`huawei`) is the best-evidenced organizational patent filer (WIPO #1 corporate PCT filer) and runs the broadest multi-city/multi-country lab footprint (Noah's Ark), but we could not verify headcount, so bench-depth claims about Huawei beyond patent volume remain unverified.
- **Alibaba, Tencent, ByteDance, Baidu** (`alibaba`, `tencent`, `bytedance`, `baidu`) each run named corporate AI labs (DAMO, Tencent AI Lab, Seed/Top Seed, ERNIE-linked teams); of these only ByteDance and Tencent have any (D-grade) public headcount figure — investors relying on "which platform has the deepest AI research bench" should treat all four as **data-poor** on this specific dimension.
- **Cambricon, Empyrean, and the broader L1/L4 chip-design cohort** are the names most directly exposed to the EDA/advanced-node design-talent bottleneck in §4 — this is a genuine, still-binding constraint on China's ability to scale indigenous chip design independent of talent imports or long training pipelines (5+ years to produce a sub-5nm-experienced design lead).

---

## Key figures (summary table)

| Metric | Value | Period | Source | Confidence |
|---|---|---|---|---|
| China share of GATT elite AI researchers (by undergrad origin) | 38% | 2022–2024 vintage | MacroPolo GATT (via MIT Tech Review) | C |
| Share of China-educated elite researchers now working in US | 72% | ~2022 | MacroPolo GATT | C |
| Share of China-educated elite researchers remaining in China | 11% (down from 16% in 2019) | ~2022 | MacroPolo GATT | C |
| US institutions' share of world's elite AI researchers | 59% (up from 51% in 2017) | 2022–2024 | MacroPolo GATT | C |
| AI-talent migration into US, decline since 2017 | -89% | to 2025 | Stanford AI Index 2026 (via Fortune) | C |
| China share of global AI publications / citations | 23.2% / 20.6% | 2025 | Stanford AI Index 2026 | C |
| China share of top-100 most-cited AI papers | 41 of 100 (up from 33 in 2021) | 2024 | Stanford AI Index 2026 | C |
| China PCT patent applications | 73,718 vs. US 52,617 | 2025 | WIPO | B |
| China share of global AI patent filings | 69.7% | 2025 | Stanford AI Index 2026 | C |
| China STEM PhDs awarded | ~50,000 (+13.7% YoY) | 2022 | Georgetown CSET (MOE/NBS data) | C |
| Projected China STEM PhDs/year | ~77,000 vs. US ~40,000 | 2025 (projection) | CSET | D |
| China total university graduates | 12.7 million | 2026 | MOE (via Global Times) | B |
| China semiconductor/EDA talent gap | 200,000–300,000 | 2025 | Industry recruiter reporting | D |
| McKinsey-estimated AI professional shortfall | up to 4 million | by 2030 | McKinsey (via TechNode) | D |
| DeepSeek researchers with 5+ yrs US experience who returned to China | ~70% | 2025 (roster analysis) | Hoover Institution / Rest of World | D |

---

## Sources

See `research/v2_p4_talent_data.md` for the full WEB-8xx source log with URLs. All figures above are individually tagged with confidence grades; where we could not access a primary document directly (multiple 403 responses from MacroPolo's own site and Stanford HAI's site to automated fetch), figures are marked as relayed via secondary reporting rather than primary-verified, per v2 sourcing rules.

---

## GLOSSARY

- **GATT (Global AI Talent Tracker):** MacroPolo's dataset tracking elite AI researchers (authors at NeurIPS/ICML/ICLR) by undergraduate-origin country and current institutional affiliation.
- **NeurIPS / ICML / ICLR:** the three most competitive, most-cited annual AI/machine-learning research conferences; publication there is the field's standard marker of elite research output.
- **PCT (Patent Cooperation Treaty) application:** an international patent filing route administered by WIPO that lets an applicant seek protection in many countries via one application; PCT filing counts are the standard global cross-country patent-activity benchmark.
- **WIPO:** World Intellectual Property Organization, the UN agency that administers the PCT and publishes official global patent statistics.
- **Stock vs. flow (talent):** "flow" = graduates or migrants per year; "stock" = researchers currently active/resident. A country can lead on flow (graduates) while trailing on stock (working researchers) if net migration runs outward.
- **K-visa:** China's new (effective Oct-2025) sponsor-free visa category for young foreign STEM professionals, positioned as a response to the US's 2025 H-1B fee increase.
- **Young Thousand Talents / Qiming Program:** successor brandings of China's original "Thousand Talents Plan," offering grants/salary/housing packages to recruit under-40 STEM researchers, including from overseas.
- **EDA (Electronic Design Automation):** software used to design and verify integrated circuits (chip layout, simulation, verification); dominated globally by Synopsys and Cadence (both US), with China's Empyrean and peers still behind at the most advanced process nodes.
- **Military-civil fusion (MCF):** a Chinese state strategy to integrate military and civilian technology development; the term appears in recent US visa policy as grounds for restricting entry of researchers with MCF-linked institutional ties.
- **Reflow (talent):** researchers who trained/worked abroad (typically in the US) subsequently relocating back to their country of origin; distinct from "retention" (never having left).

---

## LIMITATIONS

- **MacroPolo's and Stanford HAI's own sites both returned HTTP 403 to automated fetch.** Every GATT and AI Index figure here is relayed via secondary reporting (MIT Technology Review, Paulson Institute, Fortune, etc.), graded C rather than A/B even though the underlying study is named/primary, per the v2 rule that A/B requires our own direct check.
- **No official "AI-specific graduates per year" series exists from MOE**; STEM-PhD totals and total-graduate counts are proxies. Treat any precise "X AI graduates in year Y" figure as an estimate.
- **The 2024 China AI-workforce figure (52,000; Tsinghua 2,667; PKU 2,123; CAS 3,453) is single-sourced (TMTPost) with unverifiable methodology** — D-grade, illustrative order-of-magnitude only, not a census.
- **No corporate lab (Huawei, Alibaba, Tencent, ByteDance) publishes an audited researcher headcount**; the figures cited come from single blog/recruiter-style sources and are not comparable across companies or current by design.
- **The 2025-26 "reflow" narrative is directionally corroborated (US visa tightening + Stanford's 89% migration-decline stat) but not population-quantified** — the only granular return-rate (~70%) is DeepSeek's roster alone; do not extrapolate to China generally.
- **Patent-count leadership (WIPO, B) should not be read as value/quality leadership** — no evidence found that volume translates to commercially influential IP at US parity.
- **Chip-design/EDA talent-gap figures are industry-recruiter estimates**, not government statistics; only the direction (acute, senior-level shortage) is corroborated, not the magnitude.
- **No forward-looking talent projection here is tradeable** — McKinsey's 4M shortfall, CSET's 77,000 2025-PhD projection, and similar figures are D-grade, directional context only.
