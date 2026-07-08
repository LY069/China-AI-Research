# China's AI Stack & Ecosystem — Research Framework (v1)

**Program:** China AI Stack Deep Research
**Prepared by:** Research Director (orchestrator)
**Date:** 2026-07-08
**Audience:** Financial-market experts, economists, industry analysts

---

## 0. Mandate & lens

**Primary lens — Industry & value-chain map.** The flagship output is a definitive, layer-by-layer map of China's AI stack: market structure, who's-who, competitive moats, supply–demand, and unit economics at every layer. Every layer resolves into **named companies** and a **security-level investable read** (tickers, listing/Entity-List status, valuations, a stack-mapped basket — framed as analysis, not advice).

**In scope:** the 10-layer core digital stack **+ Physical AI/embodied (L9) + Talent & R&D (T)**.
**Contextual wrappers (light, not full pods):** macro/mercantilism, global diffusion/soft power.

**Standing conventions**
- Benchmark every layer against US/global peers (capability gap · timeline · market-cap gap).
- Scenarios: base / bull / bear on indigenization, at **2027 (tactical)** and **2030 (5YP)** horizons.
- Data as-of **mid-2026**; **every figure carries a source ID and a confidence grade** (A=filed/audited, B=primary disclosure, C=credible 3rd-party, D=single-source/estimate).
- Investability & Entity-List constraints flagged on **every** named entity.
- Reference PDFs (Bridgewater ×3, Sands, Exponential View) are analytical scaffolding and are cited, but conclusions rest on independently-sourced, citable evidence in the database.

---

## 1. Vertical spine — the stack, bottom-up

| Layer | Name | What it does | Anchor players (China) | Global benchmark | Binding constraint |
|-------|------|--------------|------------------------|------------------|--------------------|
| **L0** | Energy & Power | Powers & cools the buildout | State Grid, gencos, CATL (storage) | US grid | Advantage (China) |
| **L1** | Semi equipment & EDA | Builds the fabs | NAURA, AMEC, SMEE, ACM, Empyrean (EDA) | ASML, AMAT, Lam, KLA, Synopsys/Cadence | **EUV litho (most binding)**, EDA |
| **L2** | Fabrication / foundry | Prints the chips | SMIC, Hua Hong | TSMC, Samsung | Node ≤7nm, yield, packaging |
| **L3** | Memory (HBM/DRAM/NAND) | Feeds the compute | CXMT, YMTC | SK hynix, Samsung, Micron | HBM, TSV |
| **L4** | AI chips & software | Converts energy→tokens | Huawei Ascend, Cambricon, Moore Threads, Biren, MetaX, Iluvatar, Kunlunxin, T-Head | Nvidia, AMD | Chip supply + CUDA-equivalent SW |
| **L5** | Interconnect & networking | Moves the data | Montage, Huawei (optical) | Nvidia NVLink, Broadcom, Astera | Bandwidth/latency |
| **L6** | Data center & cloud | Hosts the fleet | Alibaba Cloud, Huawei Cloud, Tencent, Baidu | AWS, Azure, GCP, CoreWeave | Compute availability |
| **L7** | Foundation models | Converts tokens→intelligence | DeepSeek, Qwen, Doubao, Zhipu, MiniMax, Moonshot, Ernie, Hunyuan | OpenAI, Anthropic, Google | Compute + frontier gap |
| **L8** | Applications & agents | Converts intelligence→value | Consumer super-apps, vertical SaaS, coding, agents | ChatGPT, Cursor, Harvey | Enterprise adoption |
| **L9** | Physical AI / embodied | AI into the real world | Unitree, UBTech, EV/AV stacks, industrial AI | Tesla, Figure, Waymo | Integration / China edge |

## 2. Horizontal cross-cutting dimensions

- **P — Policy & industrial strategy:** 15th FYP; national funds (~$138bn AI+robotics, ~$295bn DC network, ~¥1T high-tech, the "Big Fund"); domestic-content mandates (50% equipment); SOE adoption; provincial competition.
- **C — Compute supply–demand:** GW accounting (training vs inference vs R&D); price signals (cloud list-price hikes, model price hikes).
- **G — Export controls & geopolitics:** US sanctions (chips/EUV/HBM/SME); Entity List; gray market; rare-earth leverage; Taiwan flashpoint; third-country routing.
- **K — Capital markets & investability:** IPO wave (STAR/HK/ChiNext/BSE); valuations; A/H premium; national-champion sponsorship; "slow bull"; foreign-investor access & Entity-List overlap.
- **T — Talent & R&D:** researchers, papers/patents, open-source contribution, talent-flow restrictions.
- **W — Global diffusion (context):** China model share abroad (OpenRouter ~⅓), Global South/BRI, standards diplomacy.

## 3. Synthesis layer (deliverable payload)

1. **Value-capture & bottleneck economics** across the stack — where margin pools, who has pricing power.
2. **China-vs-US benchmark** at every layer — capability gap, timeline to parity, market-cap gap.
3. **Investable universe + basket** — stack-mapped, with valuations and positioning read.
4. **Scenarios** — base/bull/bear on indigenization → implications for each layer.
5. **Risk register** — policy reversal, flashpoint, EUV/tech failure, demand shortfall, overbuild.

---

## 4. Analyst pod structure

| Pod | Covers | Primary deliverable |
|-----|--------|---------------------|
| **Pod 1 — Silicon & Equipment** | L1, L2, export-control/EUV | Memo + company/chip rows |
| **Pod 2 — Memory & Interconnect** | L3, L5 | Memo + company/spec rows |
| **Pod 3 — Compute & Chips** | L4 + CUDA-equivalent SW | Memo + chip catalog rows |
| **Pod 4 — Cloud, Models & Apps** | L6, L7, L8 + adoption | Memo + model catalog rows |
| **Pod 5 — Power & Physical-AI** | L0, L9 | Memo + company rows |
| **Pod 6 — Policy, Geopolitics & Capital Markets** | P, G, K, W | Memo + policy/funding + investability rows |
| **Pod 7 — Macro & Synthesis** | C + Synthesis (§3) | Supply-demand model, valuations, scenarios |

Each pod returns: (a) a structured markdown memo under `/research/`, (b) database rows in the schema of `/database/`, (c) a source-logged bibliography with confidence grades.

---

## 5. Deliverables

1. **Long-form research report** (`/report/`) — the layer-by-layer value-chain map + synthesis.
2. **Presentation materials** (`/presentation/`) — executive deck for the audiences above.
3. **Evidence database** (`/database/`) — Company Master (backbone) + metric time-series + policy/funding tracker + model & chip spec catalogs + source log.
