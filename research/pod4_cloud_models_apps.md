# Pod 4 — Cloud, Foundation Models & Applications (L6, L7, L8)

**Analyst pod:** Pod 4 · **Date:** 2026-07-08 · **Horizon:** mid-2026 snapshot, 2027/2030 read-through

---

## Scope

This memo covers the top three layers of China's AI stack: **L6 cloud/data-center hosting** (Alibaba Cloud, Huawei Cloud, Tencent Cloud, Baidu AI Cloud, ByteDance Volcengine, plus the national East-Data-West-Compute grid), **L7 foundation models** (DeepSeek, Qwen, Doubao, Ernie, Hunyuan, GLM/Z.ai, MiniMax, Kimi), and **L8 applications & adoption** (consumer super-apps, enterprise/SOE diffusion, coding agents). It closes with the two 2026 foundation-model IPOs (Zhipu, MiniMax) and an investability read across all three layers.

---

## Market structure & value chain

**L6 — Cloud is an oligopoly of five, now organized around AI-cloud share rather than legacy IaaS share.** By Omdia's AI-cloud-specific H1-2025 cut, Alibaba Cloud led with 35.8% share, ByteDance's Volcengine second at 14.8%, Huawei Cloud third at 13.1%, Tencent Cloud 7%, Baidu AI Cloud 6.1% [1]. Alibaba's AI-cloud share reportedly extended to ~38.1% into 2026 as its scale advantage compounds [16]. Note the definitional split: on *overall* cloud infrastructure (not AI-specific), Huawei Cloud is China's clear #2 with ~17% share in Q4 2025, even as its *external* cloud revenue fell 3.5% YoY to RMB 32.16bn in 2025 — Huawei's cloud growth increasingly comes from AI-chip-attached and internal/government demand rather than third-party IaaS [3][4]. China's overall cloud-infrastructure spend grew ~24-26% YoY through Q3/Q4 2025 on Omdia data, an unusually strong re-acceleration after two soft years [5].

**Pricing regime has flipped from a multi-year discount war to a synchronized hike cycle.** Through Q1-Q2 2026, Alibaba, Tencent and Baidu all raised AI-compute list prices, and Tencent alone executed three separate hikes in 2026: a March 11 repricing of Hunyuan-series model API tokens (some SKUs up as much as 463% off promotional/free-beta pricing), a May 9 uniform 5% list-price increase across AI compute/container/EMR products, and a May 15 hike to AI coding-assistant seats (CodeBuddy/WorkBuddy enterprise tier +154%, RMB78→RMB198/user/month) [7][8][9][10]. Zhipu also raised model API prices again in the same window [7]. The proximate cause cited across sources is tight GPU/accelerator hardware supply meeting surging inference demand — a genuine price-signal of compute scarcity, not just margin repair.

**National infrastructure layer:** Beijing is moving beyond the 2022-era "East Data West Compute" spatial policy to a far larger, chip-sovereign build. The NDRC is reportedly drafting a five-year, ~RMB 2 trillion (~$295bn) program to knit thousands of data centers into a single national computing grid, mandating that **≥80% of underlying technology — including AI accelerators — be domestically sourced**, effectively squeezing out Nvidia/AMD from new state-linked capacity. State operators (China Mobile, China Telecom) run the bulk of the physical estate; the grid-completion target is ~2028 inside a 2031 investment window [11][12]. This is the clearest policy signal that L6 capacity growth in China will be a **Huawei-Ascend/Cambricon/Hygon-denominated** market for the state-adjacent tranche of demand, distinct from the hyperscaler-run commercial cloud where some Nvidia legacy stock persists.

**L7 — foundation models are converging technically while diverging financially.** Six to eight labs now field frontier-class or near-frontier models: DeepSeek (V3.x/V4), Alibaba Qwen, ByteDance Doubao, Baidu Ernie, Tencent Hunyuan, Zhipu/Z.ai GLM, MiniMax, Moonshot Kimi. All ship open-weight variants (Apache 2.0 or MIT) alongside closed commercial APIs — a "hybrid" strategy that maximizes both global developer mindshare (Hugging Face downloads, OpenRouter token share) and monetizable enterprise/API revenue. The single most important 2026 development is that **the compute constraint has stopped being a hard capability ceiling**: DeepSeek-V4-Pro (released April 24, 2026, ~1.6T-parameter MoE, ~49B active) was trained and now runs in production on Huawei Ascend 950 and Cambricon accelerators rather than Nvidia — the first frontier-class model to do so — with Ascend/Cambricon/Hygon/Moore Threads all completing "Day-0" inference adaptation on release day [13][14]. V4-Pro scores 80.6% on SWE-bench Verified, essentially tied with Claude Opus 4.7 (80.8%) and ahead of GPT-5.5 (74.9%) on that benchmark [14].

**L8 — consumer AI has scaled faster than the brief's baseline data implied.** During the Spring Festival 2026 peak, Doubao hit 145m DAU, Qwen 73.5m DAU (+940% YoY), YuanBao 40.5m DAU [21][22]. By Q1 2026, Doubao's MAU surpassed Baidu's own app for the first time at 260m+ (+300% YoY), YuanBao MAU reached 150m, and the five leading Chinese AI chat/search apps (Doubao, Baidu Ernie Bot ~220m, Alibaba Quark ~180m, YuanBao ~150m, Moonshot Kimi ~90m) collectively exceed 900m MAU domestically [21][22]. **These are materially higher than the brief's seed figures (Doubao >100m, Qwen/YuanBao 50-70m peak)** — treat the seed database's DAU rows as stale by roughly two quarters; updated rows are supplied in the companion data file.

---

## Capability vs. global frontier (+ timeline)

The framing that mattered in 2024-2025 — "China is N months behind the US frontier" — is now explicitly contested by mid-2026 commentary. Two distinct gaps should be tracked separately:

1. **Single-best-model gap:** narrowed from a widely-cited 6-18 months (2024) to an estimated **6-9 months**, per China AI-strategy analysts, with GLM-5.2 (Z.ai, MIT-licensed, released June 16, 2026) ranking #4 globally on Artificial Analysis's Intelligence Index — behind only Claude "Fable" 5, Claude Opus 4.8, and GPT-5.5 — and scoring within ~1 point of Opus 4.8 on a widely-watched agentic-coding benchmark while running at roughly one-fifth the inference cost [23][24]. Tencent's Hunyuan Hy3 (295B MoE/21B active, Apache 2.0, released July 6, 2026) posts GPQA-Diamond 90.4 (vs. GPT-5.5's 93.6) and matches GPT-5.5 on BrowseComp (84.2) [17][18].
2. **Token-supply / distribution gap:** this is the axis China has already won. On OpenRouter — the largest neutral LLM router, processing 20tn+ tokens/week — **Chinese-origin models rose from <2% of tokens in mid-2025 to ~61% by May 2026**, while the combined US-lab share (OpenAI + Anthropic + Google) fell from ~70% to ~30% over the same twelve months [19][20][25]. DeepSeek alone is now the single largest provider on the platform at ~16-17.6% of all tokens, ahead of any individual US lab. Six Chinese models (DeepSeek, GLM-5.2, Qwen, Kimi K2.6, MiniMax-M3, Hunyuan) now outrank Anthropic's Claude by token volume [19][20]. **This is a materially larger and faster shift than the brief's seed figure of ~⅓ Chinese share — update the openrouter_china_share metric.**

**Timeline read:** on frontier single-model capability, base case is continued narrowing to near-parity (sub-6-month lag) by 2027, driven by efficiency innovation (MoE sparsity, smaller active-parameter counts, domestic-chip-native training) more than raw compute scale — Huawei's aggregate compute output is estimated at only ~4% of Nvidia's 2026 total (a D-grade, single-source estimate, flagged as such) [24], yet Chinese labs are closing the gap regardless, implying compute-per-unit-of-capability efficiency is the actual battleground. On token-supply / open-weight distribution, China has structural, likely durable leadership because its labs treat open-weighting as the default distribution strategy (cost, geopolitics-hedging, developer capture) in a way US labs have not matched.

---

## Moats & unit economics

- **Cloud:** Alibaba's moat is scale + vertical integration (own T-Head silicon, own Qwen models, dominant share) letting it defend the highest price realization even amid the 2026 hike cycle; its FY26-Q4-equivalent cloud revenue grew 38% YoY with the AI subset posting triple-digit growth for an 11th consecutive quarter, though full-company margins are compressed by the RMB 380bn three-year AI-capex commitment (management signaling it will likely overshoot) [2][6]. ByteDance's Volcengine is pursuing a deliberately margin-light MaaS (Model-as-a-Service) land-grab: MaaS revenue target for 2026 is RMB 15bn, a 10x jump off a 2025 base of ~RMB 1.5bn, explicitly sacrificing near-term GPU-rental economics to seed token consumption and lock developers into Doubao-family models [26][27]. Baidu's AI-cloud infrastructure revenue grew 79% YoY in Q1 2026 (GPU-subscription revenue +184%), and the company now states AI-related revenue is a majority of its total business — the clearest evidence yet that a legacy-search company can pivot its P&L structure around AI cloud [28][29].
- **Models:** open-weighting is now the dominant Chinese moat strategy — not withholding IP, but using near-zero-marginal-cost distribution to capture developer/enterprise mindshare and OpenRouter volume, then monetizing via cloud API attach-rate (Alibaba/Tencent/Baidu bundling their own models into their own cloud) rather than per-token model margin alone. DeepSeek is the exception proving the rule on capital structure: it raised its *first-ever* external round in 2026 (~RMB 50bn / $7.4bn, reported valuation $52-59bn), led by Tencent and CATL plus the National AI Industry Investment Fund, with founder Liang Wenfeng contributing ~40% of the round himself to retain effective control — a structure (LP vehicle, 5-year lockup, no investor voting rights) that keeps DeepSeek's governance unusually founder-centric even after taking outside capital [30][31][32].
- **Apps:** unit economics remain consumer-subsidized. DAU/MAU growth (Doubao, Qwen, YuanBao) has been extraordinary, but monetization lags — this is consistent with the brief's flagged "enterprise/SaaS weakness." The clearest enterprise monetization signal is coding agents: Tencent's CodeBuddy reports 60%+ retention among active users and >80% among *paying* users, evidence of real productivity value once conversion happens — but conversion is the bottleneck, and even inside China, GitHub Copilot reportedly still holds ~64.5% share of the coding-assistant market vs. Alibaba's Tongyi Lingma at ~12.9%, undercutting a simple "domestic substitution" narrative for enterprise dev tools specifically [33].

---

## Bottlenecks & dependencies

1. **Compute scarcity is now a first-order price signal, not just a supply story** — the synchronized 2026 cloud/model price hikes across Alibaba, Tencent, Baidu and Zhipu are the clearest market evidence that GPU/accelerator supply (Ascend, Cambricon, residual Nvidia stock) is the binding constraint on both L6 margins and L7 API pricing power [7][8].
2. **Regulatory risk to consumer AI apps:** new rules on AI "companion"/humanlike agents take effect July 15, 2026, reportedly requiring Doubao, Qwen and similar apps to delete certain agent/companion interaction data — a fresh compliance and product-design constraint on the consumer layer that could dent engagement metrics just as DAU growth has peaked [34][35].
3. **Enterprise monetization gap (L8):** State Council's "AI Plus" initiative (Aug 2025) targets >70% adoption of next-gen intelligent applications/agents by 2027 and ~90% by 2030, reinforced by sector plans (AI Plus Manufacturing, Jan 2026) and SOE pilot cohorts (Baosteel, XCMG, Haier — 15 "pioneer" smart factories with >70% AI scenario coverage and 6,000+ deployed AI models) [36][37][38]. These are policy-signaling targets, not hard KPIs, and the gap between *adoption* (fast) and *monetization* (slow, workflow-redesign-dependent) is explicitly flagged by industry trackers as the key execution risk into 2027 [39].
4. **IPO-driven volatility now a two-way risk for the newly-listed model labs** — see below.

---

## Named companies

| Company | Layer/segment | Ownership | Listing / ticker | Entity List | Foreign-investable | Mkt cap (as of) | Global peer |
|---|---|---|---|---|---|---|---|
| Alibaba Group | L6 cloud (Alibaba Cloud, ~35.8-38.1% China AI-cloud share) + L7 (Qwen) | Private, listed | HKEX:9988 / NYSE:BABA | No | Yes | ~$231bn (Jul-2026, C) [40] | AWS + Google |
| Tencent | L6 (Tencent Cloud) + L7 (Hunyuan) + L8 (YuanBao) | Private, listed | HKEX:0700 | No | Yes | ~$520bn (Jan-2026, D — stale date) [41] | Microsoft + Meta |
| Baidu | L6 (Baidu AI Cloud) + L7 (Ernie) + L4 (Kunlunxin, spinning off) | Private, listed | HKEX:9888 / NASDAQ:BIDU | No | Yes | ~$37-39bn (mid-Jun-2026, C) [42][43] | Google + Microsoft |
| ByteDance | L6 (Volcengine) + L7 (Doubao) + L8 apps | Private | private | No | No | n.a. (private) | OpenAI + Meta |
| Huawei | L4/L5/L6 (Huawei Cloud, Ascend) | Private (employee-owned) | private | Yes | No | n.a. (private) | Nvidia + AWS |
| DeepSeek (High-Flyer) | L7 | Private | private | No | No | ~$52-59bn implied (2026 first raise, C) [30][31] | OpenAI / Anthropic |
| Zhipu AI / Z.ai (Knowledge Atlas Tech) | L7 (GLM) | Private, **now listed** | HKEX:2513 (IPO Jan-8-2026); STAR Market application filed Jun-2026 | No | Restricted | ~HK$1tn peak (Jun-2026) / ~$87bn (early Jul-2026, C, highly volatile) [44][45][46] | OpenAI / Anthropic |
| MiniMax | L7 | Private, **now listed** | HKEX:0100-W (IPO Jan-9-2026, WVR structure) | No | Restricted | ~HK$109bn / ~$14bn (early Jul-2026, down >70% from Mar-2026 peak of ~HK$410bn on lock-up unlock, C) [47][48] | OpenAI / Anthropic |
| Moonshot AI | L7 (Kimi K2 series) | Private | private | No | No | n.a. (private) | OpenAI / Anthropic |

*(Ownership/listing/Entity-List/peer columns reconfirm existing `company_master.csv` fields; market caps and listing status for Zhipu/MiniMax are updates — both have moved from "IPO-approved" to "listed" since the seed database was built.)*

---

## Investability read

- **Cleanest listed exposure remains Alibaba, Tencent, Baidu** — all foreign-investable, all with disclosed AI-cloud and model P&L lines, all NYSE/HKEX/NASDAQ accessible. Alibaba is the highest-conviction pure-play on the AI-cloud oligopoly given its #1 share and full-stack (chip+cloud+model) integration, but faces the largest near-term margin compression from its own capex super-cycle.
- **Zhipu and MiniMax are now direct listed proxies for L7 model-lab economics** — a genuinely new investable category (first LLM-developer-as-listed-entity) — but exhibit extreme volatility (MiniMax -70%+ from peak within four months; Zhipu +1,500-2,000% YTD before a follow-on raise) that looks more like retail-momentum/lock-up mechanics than steady-state model-lab fundamentals. Treat both as high-beta, low-liquidity-float, sentiment-driven instruments rather than value plays; the imminent (Jul-9-2026) MiniMax lock-up unlock is a live near-term supply/technical risk.
- **DeepSeek, ByteDance, Moonshot remain private** and inaccessible to public investors directly; DeepSeek's 2026 funding round (Tencent + CATL + National AI Industry Investment Fund) offers indirect exposure via Tencent's balance sheet.
- **Kunlunxin's pending Hong Kong/STAR spinoff from Baidu** (tutoring initiated May 2026) is a name to watch for a pure-play L4 chip listing but sits outside this pod's core L6-L8 remit (see Pod 3).
- **Basket framing:** a China cloud+model basket today should overweight Alibaba (integration), keep Tencent/Baidu as diversified cloud+model+ads hedges, and treat Zhipu/MiniMax as small, volatile satellite positions rather than core holdings pending 2-3 more quarters of post-IPO price discovery.

---

## Key figures

- Alibaba Cloud AI-cloud market share: 35.8% (H1-2025, B) → ~38.1% (2026, C)
- Alibaba Cloud revenue growth: 38% YoY (most recent quarter, B); AI subset triple-digit growth for 11 straight quarters (B)
- Volcengine MaaS revenue target: RMB 15bn (2026) vs ~RMB 1.5bn (2025) — 10x (C)
- Baidu AI-cloud infrastructure revenue growth: +79% YoY (Q1-2026, B); GPU-subscription revenue +184% (B)
- Huawei AI-chip revenue: ~$12bn (2026E, +60% YoY, C)
- National DC grid plan: ~$295bn / RMB 2tn, 80% domestic-content mandate, ~2028 grid-completion target (C)
- OpenRouter Chinese-model token share: ~61% (May-2026, C) vs. <2% (mid-2025) — up sharply from the brief's ~⅓ baseline
- DeepSeek-V4-Pro: 1.6T-param MoE, ~49B active, SWE-bench Verified 80.6% (near Claude Opus 4.7's 80.8%), trained/served on Huawei Ascend 950 + Cambricon (C)
- Doubao DAU: 145m (Spring Festival 2026 peak, C) vs. brief's baseline >100m; Doubao MAU 260m+ (Q1-2026, C)
- Zhipu (Z.ai) market cap: ~$87bn (early Jul-2026, C, high volatility); MiniMax: ~$14bn (early Jul-2026, down >70% from March peak, C)
- AI Plus diffusion targets: 70% adoption of next-gen AI apps/agents by 2027, 90% by 2030 (policy target, not hard KPI, C)

---

## Sources

1. Ainvest / SCMP / Yahoo — "Alibaba holds wide lead over rivals ByteDance, Huawei, Tencent in China's AI cloud market" (Omdia H1-2025 data), 2025-09/2026, C. https://www.ainvest.com/news/alibaba-leads-china-ai-cloud-market-35-8-share-outpacing-rivals-bytedance-huawei-tencent-2509/
2. MarketChameleon — "Alibaba's Cloud and AI Momentum Accelerates, But Investments Drag," 2026-05-14, C. https://marketchameleon.com/articles/b/2026/5/14/alibaba-cloud-ai-revenue-growth-investment-strategy-2026
3. CNBC — "Huawei's cloud computing revenue dropped in 2025 as Chinese AI lagged U.S. rivals," 2026-03-31, C. https://www.cnbc.com/2026/03/31/huawei-annual-report-2025-cloud-computing-revenue.html
4. Omdia — "Mainland China cloud infrastructure spending rises 26% in Q4 2025," 2026-04, C. https://omdia.tech.informa.com/pr/2026/apr/mainland-china-cloud-infrastructure-spending-rises-26percent-in-q4-2025-driven-by-ai-and-agent-growth
5. Omdia — "Mainland China's cloud infrastructure market accelerates to 24% growth in Q3 2025," 2026-02, C. https://omdia.tech.informa.com/pr/2026/feb/mainland-chinas-cloud-infrastructure-market-accelerates-to-24percent-growth-in-q3-2025
6. CNBC — "Alibaba shares rise as AI drives 34% cloud sales jump," 2025-11-25, B. https://www.cnbc.com/2025/11/25/alibaba-shares-rise-as-ai-drives-cloud-sales-jump-earnings.html
7. TrendForce — "AI Compute Prices Rise Across China: Tencent Joins Alibaba, Baidu in Hikes; Zhipu Raises Prices Again," 2026-04-10, C. https://www.trendforce.com/news/2026/04/10/news-ai-compute-prices-rise-across-china-tencent-joins-alibaba-baidu-in-hikes-zhipu-raises-prices-again/
8. Caixin Global — "Alibaba, Tencent Hike Cloud Prices as AI Boom Drives Up Hardware Costs," 2026-03-19, C. https://www.caixinglobal.com/2026-03-19/alibaba-tencent-hike-cloud-prices-as-ai-boom-drives-up-hardware-costs-102424744.html
9. Tencent Cloud (official) — "Price Adjustment Notice for AI Compute, Container..." 2026, B (primary). https://www.tencentcloud.com/announce/detail/101085
10. Futunn News — "Tencent Cloud Announces Third Price Hike This Year: AI Code Assistant Sees Up to 150% Increase," 2026, C. https://news.futunn.com/en/post/72174644/tencent-cloud-announces-third-price-hike-this-year-ai-code
11. Bloomberg (via Tom's Hardware/Techtimes summary) — "China drafts $295 billion plan to build national AI data center grid running on 80% homemade silicon," 2026-06-09/22, C. https://www.bloomberg.com/news/articles/2026-06-09/china-prepares-295-billion-plan-to-fund-nationwide-ai-buildout ; https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips
12. TechTimes — "China AI Data Center Grid Locks Out Nvidia With $295 Billion Domestic Chip Mandate," 2026-06-22, C. https://www.techtimes.com/articles/318868/20260622/china-ai-data-center-grid-locks-out-nvidia-295-billion-domestic-chip-mandate.htm
13. TrendForce — "Huawei Ascend, Cambricon and Hygon Completed Day 0 Adaptation to DeepSeek-V4," 2026-04-29, C. https://www.trendforce.com/news/2026/04/29/news-huawei-ascend-cambricon-and-hygon-completed-day-0-adaptation-to-deepseek-v4/
14. NxCode — "DeepSeek V4 (2026): 1T Parameters, 81% SWE-bench, $0.30/MTok — Full Specs," 2026, D (aggregator/estimate). https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026 ; MorphLLM — "DeepSeek V4: 1.6T MoE, 1M Context," 2026, D. https://www.morphllm.com/deepseek-v4
15. ChinaTalk — "DeepSeek V4," 2026, C. https://www.chinatalk.media/p/deepseek-v4
16. AInvest (2026 update reference within source 1's family) — Alibaba AI-cloud share extension to ~38.1%, C.
17. BigGo Finance — "Tencent Launches Hunyuan 3.0: 295B-Parameter Model Rivals GPT-5.5," 2026-07, C. https://finance.biggo.com/news/b62ccd99-eb32-4232-b36c-3d28046eaa14
18. Hy3AI / ExplainX — "Tencent Hy3: 295B Open MoE for Agentic Coding," 2026-07, D. https://hy3ai.com/ ; https://www.explainx.ai/blog/tencent-hy3-295b-moe-open-source-agentic-model-2026
19. KuCoin News — "OpenRouter Data Shows 61% of Token Consumption by Chinese AI Models," 2026-05/06, C. https://www.kucoin.com/news/flash/openrouter-data-shows-61-of-token-consumption-by-chinese-ai-models
20. Data Gravity (Chris Zeoli) — "China's Open-Weight Takeover," 2026, C. https://www.datagravity.dev/p/chinas-open-weight-takeover
21. NPR — "China's AI chatbots are advanced and versatile — and begging for more users," 2026-03-30, C. https://www.npr.org/2026/03/30/nx-s1-5760939/china-chatbot-industry-doubao-qwen-yuanbao
22. SecondTalent — "Top 5 Chinese AI Search Engines in 2026" (900m MAU aggregate), 2026, D. https://www.secondtalent.com/resources/top-5-chinese-ai-search-engines/
23. CNBC — "Chinese AI models are gaining ground with U.S. companies as OpenAI, Anthropic costs surge," 2026-07-07, C. https://www.cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html
24. USCC / Anthropic / CNBC synthesis on frontier-gap framing ("6-9 months," Huawei ~4% of Nvidia 2026 aggregate compute — D, single-source estimate), 2026-03/06. https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf
25. OfficeChai — "Share Of US Models Being Used On OpenRouter Has Collapsed From 70% To 30%," 2026, C. https://officechai.com/ai/share-of-us-models-being-used-on-openrouter-has-collapsed-from-70-to-30-over-the-past-year/
26. KrAsia — "ByteDance raises Volcano Engine's MaaS revenue target on Seedance 2.0 growth," 2026, C. https://kr-asia.com/bytedance-raises-volcano-engines-maas-revenue-target-on-seedance-2-0-growth
27. 36Kr (EU) — "Volcengine's Battle in the AI Consumer Goods Market: Consuming 50 Trillion Tokens Daily," 2026, D. https://eu.36kr.com/en/p/3602323540346114
28. AlphaPilot — "Baidu Q1 2026: AI Revenue Surpasses 50% as Cloud and ERNIE 5.1 Drive Growth," 2026-05, C. https://www.alphapilot.tech/discover/baidu-q1-2026-ai-revenue-surpasses-50-as-cloud-and-ernie-5-1-drive-growth
29. Winbuzzer — "Baidu Says AI Made up a Majority of Its Q1 2026 Business Revenue," 2026-05-19, C. https://winbuzzer.com/2026/05/19/baidu-says-ai-is-now-the-majority-of-its-business-xcxwbn/
30. TechCrunch — "DeepSeek could hit $45B valuation from its first investment round," 2026-05-06, C. https://techcrunch.com/2026/05/06/deepseek-could-hit-45b-valuation-from-its-first-investment-round/
31. Silicon Republic (via The Information) — "DeepSeek raises $7.4bn at $50bn-plus valuation," 2026, C. https://www.siliconrepublic.com/business/the-information-deepseek-raises-7-4bn-at-50bn-plus-valuation
32. TechFundingNews — "Tencent to back DeepSeek in $4B round at $50B valuation," 2026, C. https://techfundingnews.com/tencent-to-back-deepseek-in-4b-round-at-50b-valuation-marking-first-external-funding-report/
33. CNBC (source 23, same article) — GitHub Copilot 64.5% vs. Tongyi Lingma 12.9% China coding-assistant share; enterprise coding-agent market $9.8-11bn annualized (Apr-2026), C.
34. TechTimes — "China AI Companion Law Arrives July 15: Doubao and Qwen Agent Data Will Be Deleted," 2026-07-04, C. https://www.techtimes.com/articles/319703/20260704/china-ai-companion-law-arrives-july-15-doubao-qwen-agent-data-will-deleted.htm
35. Michael Brian Cotter — "China's AI companion rules: what Beijing is really going after," 2026-07-06, D. https://michaelbriancotter.wordpress.com/2026/07/06/chinas-ai-companion-rules-what-beijing-is-really-going-after/
36. Merics — "China's next five-year bet on AI: Self-reliance, diffusion, and a lot of hype," 2026, C. https://merics.org/en/comment/chinas-next-five-year-bet-ai-self-reliance-diffusion-and-lot-hype
37. Matt Sheehan (Substack) — "China's Big AI Diffusion Plan is Here. Will it Work?," 2026, C. https://mattsheehan.substack.com/p/chinas-big-ai-diffusion-plan-is-here
38. Tianxia Gongchang Research — "The Inaugural Year of Industrial AI Agents," 2026, C. https://faxiangongchang.com/en/reports/china-industrial-ai-agent-2026
39. Joget/Gartner/IDC synthesis on adoption-vs-monetization gap, 2026, D (global, not China-specific). https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
40. Macrotrends — "Alibaba Market Cap 2013-2026," accessed 2026-07, C. https://www.macrotrends.net/stocks/charts/BABA/alibaba/market-cap
41. Motley Fool — "Best Stock to Buy Right Now: Alibaba vs. Tencent," 2026-01, D (dated). https://www.fool.com/investing/2026/01/01/best-stock-to-buy-right-now-alibaba-vs-tencent/
42. Macrotrends — "Baidu Market Cap 2012-2026," accessed 2026-07, C. https://www.macrotrends.net/stocks/charts/BIDU/baidu/market-cap
43. StockAnalysis.com — Baidu (BIDU) market cap, 2026-06, C. https://stockanalysis.com/stocks/bidu/market-cap/
44. CNBC — "The first of China's 'AI tigers' goes public as Zhipu climbs in Hong Kong debut," 2026-01-08, B. https://www.cnbc.com/2026/01/08/china-ai-tiger-goes-ipo-zhipu-hong-kong-debut-openai-knowledge-atlas-hsi-hang-seng-listing.html
45. SCMP — "Zhipu AI market cap tops HK$1 trillion as shares of GLM-5.2 developer soar," 2026-06, C. https://www.scmp.com/tech/article/3357858/zhipu-ai-market-cap-tops-hk1-trillion-shares-glm-52-developer-soar
46. Bloomberg — "AI Firm Zhipu to Raise $4 Billion With Hong Kong Share Offering," 2026-07-08, C. https://www.bloomberg.com/news/articles/2026-07-08/ai-firm-zhipu-to-sell-4-billion-of-shares-after-1-500-rally
47. CNBC — "MiniMax doubles in Hong Kong debut, marking yet another Chinese AI listing," 2026-01-09, B. https://www.cnbc.com/2026/01/09/minimax-hong-kong-ipo-ai-tigers-zhipu.html
48. KuCoin News — "MiniMax's market cap drops from HK$41B [sic, ~HK$410bn] to HK$109bn in six months," 2026-07, C. https://www.kucoin.com/news/flash/minimax-s-market-cap-plummets-from-41b-to-10b-hkd-in-six-months

**Confidence-grade key:** A = filed/audited · B = primary company disclosure/press covering an earnings call or filing · C = credible third-party analyst/press · D = single-source, estimate, blog aggregator, or inferred.

**Major caveats:** (i) several 2026 market-cap and valuation figures move fast (Zhipu +1,500-2,000% YTD, MiniMax -70% from peak) and should be treated as point-in-time, not stable; (ii) benchmark scores (SWE-bench, LMArena, GPQA) are self-reported or third-party-aggregated and methodology varies by source — treat relative rankings as more reliable than absolute point comparisons across different reporting sources; (iii) the "80% domestic content" DC-grid mandate is reported pre-finalization (drafting stage per Bloomberg) and could change before formal promulgation; (iv) DeepSeek's funding-round valuation ($52-59bn) is consistently reported across multiple outlets but ultimately traces to a small number of original sources (The Information) — graded C rather than B pending a primary filing.
