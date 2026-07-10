# v2 Pod Briefs (each pod: read _conventions.md + _conventions_v2.md + your section)

---
## P1 — Hyperscalers & Compute Capex  (podfile: `v2_p1_hyperscalers`)  [suggestions 6, 11]
Read v1 `research/pod4_cloud_models_apps.md` first (don't repeat it — extend financially).
Research (prefer filings/earnings/IR):
- **AI-cloud contribution:** For **Alibaba, Tencent, Baidu, ByteDance/Volcengine** — total revenue & operating profit, the **cloud segment**'s revenue/profit, and within cloud, the **AI-related** portion (e.g. Alibaba "AI-related product revenue"). Quantify AI cloud as % of group revenue and profit.
- **Non-AI drag:** For Alibaba & Tencent specifically — do the legacy segments (e-commerce, gaming, ads) **drag or fund** the AI build-out? Segment growth, margins, cash generation.
- **Capex vs US hyperscalers:** AI/DC capex 2024→2026 for the Chinese majors vs **Microsoft, Alphabet, Amazon, Meta** (absolute $, growth %, capex/revenue intensity). Alibaba's ~RMB 380bn+ 3-yr plan; ByteDance's capex.
- **Funding source (critical):** Is each name's capex funded by **internal operating cash flow** or **external debt/equity**? FCF, net cash, debt issuance. Ability to sustain rising capex. Contrast with US hyperscalers' increasingly externally-financed marginal dollar.
Data: add/extend company_master financial fields + metrics rows (AI-cloud %, capex, FCF, capex/rev). GLOSSARY: RPO, MaaS, capex intensity, FCF.

---
## P2 — Models, Apps & Adoption Economics  (podfile: `v2_p2_model_econ`)  [suggestions 7, 8]
Read v1 `research/pod4_cloud_models_apps.md` first.
Research:
- **Model-lab economics (revenue/profit, not share):** For DeepSeek, Zhipu, MiniMax, Moonshot, Qwen(Alibaba), Doubao(ByteDance) — actual/estimated **revenue** (API + subscription + enterprise), gross margin, burn/profitability. **Open-source monetization reality:** how (if at all) open-weight labs make money (cloud pull-through, enterprise support, closed tiers). Emphasize market-share ≠ revenue.
- **Enterprise adoption shift & OpenClaw:** Research **OpenClaw** (the agent that went viral per the Exponential View reference) — what it is, its enterprise traction, and **products Alibaba & Tencent have released based on/around OpenClaw**. Has Chinese enterprise AI adoption inflected recently? Coding agents, agentic workflows, SOE deployments.
Data: extend model_catalog with a revenue/monetization note field; metrics for lab revenue (flag confidence hard — mostly D). GLOSSARY: open-weight, MaaS, agentic, inference vs training, token.

---
## P3 — Demand Mapping & What's Priced In  (podfile: `v2_p3_demand_priced`)  [suggestions 1, 2, 4]
THE HEAVIEST POD. Read v1 pod1/pod2/pod3 memos for the names.
Research (prefer filings/consensus where available; flag hard where not):
- **Global vs domestic demand split:** For each major listed name (NAURA, AMEC, ACM, SMIC, Hua Hong, Montage, Cambricon, the GPU names, CXMT/YMTC, Innolight/Eoptolink, CATL, Alibaba, etc.) estimate **what share of revenue is driven by domestic-substitution vs global/external AI demand**. E.g. Montage & optical modules sell into the GLOBAL AI supply chain (Nvidia servers) — very different from a pure domestic-substitution play like Cambricon. This is the key v2 insight suggestion 1 wants.
- **Actual vs guidance vs consensus vs peers:** For the top ~10 investable names, compile **reported revenue/EPS growth, company guidance, and sell-side consensus** for FY26/27, and compare **growth priced in vs global peers** (e.g. NAURA vs AMAT/Lam; Montage vs Astera; SMIC vs TSMC/UMC; Alibaba vs AWS). What trajectory is the market pricing?
- Note where consensus is unavailable/proprietary — say so.
Data: metrics rows for domestic/global demand split (est., flag D) and growth-priced-in; company_master notes. GLOSSARY: consensus, forward P/E, PEG, urban-NOA.

---
## P4 — Talent & R&D  (podfile: `v2_p4_talent`)  [suggestion 9]
v1 barely covered this — build it properly with hard data.
Research (prefer MacroPolo, Stanford AI Index, OECD, MOE stats, credible think-tanks):
- **Supply:** China STEM & AI-specific graduates per year (bachelor/master/PhD); trend.
- **Researcher migration:** share of top-tier AI researchers who are **Chinese-origin**; share **working in US frontier labs** vs staying/returning to China (MacroPolo "Global AI Talent Tracker" is the canonical source); recent reflows and China's talent-retention/restriction moves.
- **Output:** AI papers, top-conference share, patents; leading labs/universities (Tsinghua, PKU) & corporate labs headcounts where knowable.
- **Bottlenecks:** what talent gaps remain (e.g. chip-design, EDA, advanced-process engineers).
Data: metrics rows (grads/yr, researcher shares, paper/patent shares). GLOSSARY: any terms. LIMITATIONS: be clear which figures are dated/estimated.

---
## P5 — Global Investability & Non-US Regulation  (podfile: `v2_p5_global_reg`)  [suggestion 10]
Read v1 `research/pod6_policy_geopolitics_capital.md` (US Entity List/OISP) — now go GLOBAL.
Research:
- **Non-US investor restrictions on Chinese AI/tech:** EU (FDI screening, any outbound-investment rules/proposals), UK (NSI Act), Japan, other Asia (Korea, Singapore, Taiwan, India), EM. What can a European / Japanese / Middle-East / EM investor actually hold that a US investor cannot (and vice-versa)?
- **Access mechanics:** Stock Connect (Northbound), QFII/RQFII, ADR delisting risk (HFCAA), HK vs A-share access differences, index-inclusion effects.
- **The global-client view:** a practical "who-can-own-what by investor domicile" matrix for the key names.
Data: company_master investability refinement by domicile; metrics/policy rows for non-US regimes (WEB-85x). GLOSSARY: FDI screening, NSI Act, HFCAA, Stock Connect, QFII, ADR.

---
## P6 — Index & Reference Data  (podfile: `v2_p6_refdata`)  [suggestion 12]
Mostly structured data lookup — accuracy over prose.
For every LISTED company in `database/company_master.csv`, compile:
- **ISIN** code (verify per listing line; HK vs A-share differ).
- **GICS** sector & industry (standard classification).
- **Index membership:** MSCI China, MSCI China A (Onshore), CSI 300, HSI, HSTECH — yes/no, and **approximate weight %** where known (flag proprietary/point-in-time as D).
- **Market cap as % of its listed market** (of the exchange/relevant index).
Then derive the headline insight: **how much AI-stack exposure sits in MSCI China / MSCI China A / CSI300 / HSI** (sum of member weights).
Output the memo `v2_p6_refdata.md` PLUS a data file with a clean table keyed by company_id and columns: isin, gics_sector, gics_industry, msci_china, msci_china_a, csi300, hsi, hstech, approx_weight_note, mktcap_pct_market, source, confidence. Be explicit where a value is unavailable. GLOSSARY: GICS, ISIN, MSCI China vs China A, free-float.
