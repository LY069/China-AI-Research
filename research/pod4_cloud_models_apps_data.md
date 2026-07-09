# Pod 4 — Database-Ready Additions (Cloud, Foundation Models & Applications)

Mirrors `/database/schema.md`. All rows below are proposed additions/updates for the Research Director to merge into the master CSVs — **master CSVs were not edited directly.** Source IDs are pod-local (`WEB-4xx`) and map 1:1 to the numbered sources in `pod4_cloud_models_apps.md`; the Director should reconcile/renumber against the global `sources.csv` on merge.

---

## 1. `company_master.csv` — updates to existing rows

Existing `company_id`s are unchanged; only fields below differ from the current seed row. Full rows restated for merge convenience (unchanged fields carried over from seed).

| company_id | name_en | name_cn | layers | segment | ownership | listing_status | exchange_ticker | hq | founded | entity_list | investable_foreign | mkt_cap_usd_bn | fwd_pe | key_products | china_role | global_peer | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| alibaba | Alibaba Group | 阿里巴巴 | L4\|L6\|L7 | T-Head chips; Alibaba Cloud; Qwen models | private | listed | HKEX:9988 / NYSE:BABA | Hangzhou | 1999 | no | yes | 231 | n.a. | T-Head Zhenwu chips; Alibaba Cloud (~38.1% China AI-cloud share, 2026); Qwen3/3.7-Max family | national-champion | Amazon (AWS) + Google | WEB-401 | C | UPDATE: mkt cap ~$231bn as of Jul-2026 (Macrotrends); cloud AI-share extended from 35.8% (H1-25) to ~38.1% (2026); cloud revenue +38% YoY, AI subset triple-digit growth 11 straight quarters (up from 8 in prior seed note); RMB380bn 3-yr capex plan likely to be exceeded per mgmt |
| tencent | Tencent | 腾讯 | L6\|L7\|L8 | Tencent Cloud; Hunyuan; YuanBao app | private | listed | HKEX:0700 | Shenzhen | 1998 | no | yes | 520 | n.a. | Hunyuan/Hy3 (295B MoE, Apache 2.0, Jul-2026); Tencent Cloud; YuanBao (150m MAU Q1-26); CodeBuddy | national-champion | Microsoft + Meta | WEB-402 | D | UPDATE: mkt cap ~$520bn dated Jan-2026 (stale, D-grade pending refresh); 3 AI-compute/model price hikes in 2026 (Mar/May); YuanBao DAU peak 40.5m, MAU 150m Q1-26; Hy3 open-sourced Jul-6-2026 |
| baidu | Baidu | 百度 | L4\|L6\|L7 | Kunlunxin; Baidu AI Cloud; Ernie | private | listed | HKEX:9888 / NASDAQ:BIDU | Beijing | 2000 | no | yes | 38 | n.a. | Ernie 5.0/5.1 models; Baidu AI Cloud (+79% YoY Q1-26); Kunlunxin chips (spinning off to HKEX/STAR) | national-champion | Google + Microsoft | WEB-403 | C | UPDATE: mkt cap ~$37-39bn mid-Jun-2026; AI-cloud infra revenue +79% YoY Q1-26, GPU-subscription revenue +184%; AI now majority of total business revenue per co. statements; Ernie 5.1 (May-2026) #4 globally on LMArena Search Arena |
| bytedance | ByteDance | 字节跳动 | L4\|L6\|L7\|L8 | in-house silicon; Doubao models; Volcengine; apps | private | private | private | Beijing | 2012 | no | no | n.a. | n.a. | Doubao LLM; Volcengine (MaaS rev target RMB15bn 2026, 10x); in-house accelerators | national-champion | OpenAI + Meta | WEB-404 | C | UPDATE: added L6 (was L4\|L7\|L8) — Volcengine is a distinct AI-cloud franchise, #2 China AI-cloud by share (~13-15%); Doubao DAU peak 145m (Spring Festival 2026, up from >100m late-2025), MAU 260m+ Q1-26 (+300% YoY, overtook Baidu app); 2026 AI-capex raised to >RMB200bn |
| huawei | Huawei / HiSilicon | 华为/海思 | L4\|L5\|L6 | Ascend AI chips; optical interconnect; Huawei Cloud; CANN SW | private | private | private | Shenzhen | 1987 | yes | no | n.a. | n.a. | Ascend 910/950 series; CloudMatrix; Huawei Cloud (~17% China cloud-infra share Q4-25, #2 overall) | national-champion | Nvidia + AWS | WEB-405 | C | UPDATE: distinguish overall cloud-infra share (~17%, #2) from AI-cloud-specific share (~13.1% H1-25, #3 behind ByteDance); external cloud revenue -3.5% YoY to RMB32.16bn (2025) even as AI-chip revenue seen +60% YoY to ~$12bn (2026E) |
| deepseek | DeepSeek (High-Flyer) | 深度求索/幻方 | L7 | foundation models | private | private | private | Hangzhou | 2023 | no | no | ~52-59 (implied) | n.a. | DeepSeek V4-Pro (1.6T MoE, ~49B active) trained/served on Huawei Ascend 950 + Cambricon | national-champion | OpenAI / Anthropic | WEB-406 | C | UPDATE: first-ever external funding round 2026, ~RMB50bn ($7.4bn) at $52-59bn valuation, led by Tencent + CATL + National AI Industry Investment Fund; founder Liang Wenfeng contributed ~40% of round (LP vehicle, 5-yr lockup, no investor voting rights) to retain control; V4-Pro is first frontier-class model trained+served off Nvidia |
| zhipu | Zhipu AI (Z.ai) | 智谱 | L7 | foundation models | private | **listed** | **HKEX:2513** (STAR Market application filed Jun-2026) | Beijing | 2019 | no | restricted | ~87 (highly volatile) | n.a. | GLM-5.2 (MIT license, Jun-2026, #4 Artificial Analysis Intelligence Index) | national-champion | OpenAI / Anthropic | WEB-407 | C | UPDATE: listing_status changed from "IPO-approved" to "listed" — IPOed HKEX Jan-8-2026, raised HK$4.35bn ($560m), day-1 mkt cap ~HK$55.5bn ($7.1bn); surged to >HK$1tn peak Jun-2026 (~2,000% YTD) before follow-on HK$4bn raise announced Jul-8-2026; also filed for STAR Market (Shanghai) dual listing |
| minimax | MiniMax | 稀宇科技 | L7 | foundation models | private | **listed** | **HKEX:0100-W** (WVR structure) | Shanghai | 2021 | no | restricted | ~14 (down from ~53 peak) | n.a. | MiniMax M3 (open-weight) | national-champion | OpenAI / Anthropic | WEB-408 | C | UPDATE: listing_status changed from "IPO-approved" to "listed" — IPOed HKEX Jan-9-2026, raised HK$4.8bn ($620m), day-1 close +109% at HK$106.7bn ($13.7bn) mkt cap; peaked ~HK$410bn (~$53bn) Mar-2026; collapsed to ~HK$109bn (~$14bn) by early Jul-2026 (-70%+) around lock-up unlock (45% of shares tradable Jul-9-2026) |
| moonshot | Moonshot AI | 月之暗面 | L7 | foundation models | private | private | private | Beijing | 2023 | no | no | n.a. | n.a. | Kimi K2.6 / K2.7 Code / K2 Thinking (1T MoE, 32B active, 256k ctx) | national-champion | OpenAI / Anthropic | WEB-409 | C | UPDATE: Kimi surpassed xAI in OpenRouter token share shortly after K2 launch; K2.7 Code (Jun-2026) undercuts frontier coding-model pricing by ~an order of magnitude |

---

## 2. `metrics_timeseries.csv` — new rows

| metric_id | entity | layer | metric_name | unit | period | value | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|
| alibaba_cloud_share_2026 | alibaba | L6 | Alibaba China AI cloud market share | % | 2026 | 38.1 | WEB-401 | C | Up from 35.8% (H1-2025 seed row) |
| alibaba_cloud_growth_2026 | alibaba | L6 | Alibaba Cloud revenue growth YoY | % | 2026-Q1 | 38 | WEB-402 | B | FY26-Q4-equiv quarter; AI subset triple-digit growth 11 consecutive quarters |
| volcengine_ai_cloud_share | bytedance | L6 | Volcengine China AI cloud market share | % | 2025-H1 | 14.8 | WEB-401 | C | #2 by Omdia AI-cloud cut |
| volcengine_maas_revenue_2025 | bytedance | L6 | Volcengine MaaS revenue | rmb-bn | 2025 | 1.5 | WEB-426 | C | Base year before 10x 2026 target |
| volcengine_maas_target_2026 | bytedance | L6 | Volcengine MaaS revenue target | rmb-bn | 2026 | 15 | WEB-426 | C | 10x 2025; raised on Seedance 2.0 growth |
| bytedance_capex_2026 | bytedance | L6 | ByteDance AI data-center capex | rmb-bn | 2026 | 200 | WEB-427 | D | "Raised to over RMB200bn," ~60% of 2025 profit |
| huawei_cloud_share_overall | huawei | L6 | Huawei Cloud overall China cloud-infra market share | % | 2025-Q4 | 17 | WEB-403 | C | Distinct from AI-cloud-specific share (13.1%, H1-25) |
| huawei_cloud_ext_revenue_2025 | huawei | L6 | Huawei Cloud external-customer revenue | rmb-bn | 2025 | 32.16 | WEB-403 | C | -3.5% YoY |
| huawei_ai_chip_revenue_2026e | huawei | L4 | Huawei AI-chip (Ascend) revenue estimate | usd-bn | 2026 | 12 | WEB-404 (Tom's Hardware) | C | +60% YoY vs ~$7.5bn 2025; based on orders from Alibaba/ByteDance/Tencent |
| baidu_ai_cloud_growth_q1_2026 | baidu | L6 | Baidu AI-cloud infrastructure revenue growth YoY | % | 2026-Q1 | 79 | WEB-428 | B | GPU-computing subscription revenue +184% same quarter |
| baidu_ai_revenue_share | baidu | macro | AI share of Baidu total business revenue | % | 2026-Q1 | 50 | WEB-429 | C | "Majority" per co. statements; approximate |
| china_dc_grid_investment | China | L6 | National AI data-center grid investment plan | usd-bn | 2026 | 295 | WEB-411 | C | NDRC draft, ~RMB2tn/5-yr, 80% domestic-content mandate, ~2028 grid target |
| openrouter_china_share_2026 | China | L7 | Chinese-model share of OpenRouter tokens | % | 2026-05 | 61 | WEB-419 | C | UPDATE from seed's 33% (2026 baseline) — up from <2% mid-2025 |
| openrouter_us_share_2026 | US | L7 | US-lab (OpenAI+Anthropic+Google) share of OpenRouter tokens | % | 2026-06 | 30 | WEB-425 | C | Down from ~70% (Jun-2025) |
| deepseek_openrouter_share | deepseek | L7 | DeepSeek standalone share of OpenRouter tokens | % | 2026 | 17 | WEB-424 | C | Reported range 16-17.6%; largest single provider on platform |
| doubao_dau_peak_2026 | bytedance | L8 | Doubao daily active users (Spring Festival peak) | DAU-m | 2026 | 145 | WEB-421 | C | UPDATE from seed's 100m (late-2025) |
| qwen_dau_peak_2026 | alibaba | L8 | Qwen daily active users (Spring Festival peak) | DAU-m | 2026 | 73.5 | WEB-421 | C | UPDATE from seed's 60m; +940% YoY |
| yuanbao_dau_peak_2026 | tencent | L8 | YuanBao daily active users (Spring Festival peak) | DAU-m | 2026 | 40.5 | WEB-421 | C | UPDATE from seed's 60m (prior figure likely overstated/stale) |
| doubao_mau_q1_2026 | bytedance | L8 | Doubao monthly active users | MAU-m | 2026-Q1 | 260 | WEB-421 | C | +300% YoY; overtook Baidu app for first time |
| yuanbao_mau_q1_2026 | tencent | L8 | YuanBao monthly active users | MAU-m | 2026-Q1 | 150 | WEB-421 | C | |
| china_ai_apps_combined_mau | China | L8 | Combined MAU, top-5 Chinese AI chat/search apps | MAU-m | 2026-Q1 | 900 | WEB-422 | D | Doubao 260m + Ernie Bot 220m + Quark 180m + YuanBao 150m + Kimi 90m |
| zhipu_mkt_cap_2026 | zhipu | L7 | Zhipu (Z.ai) market capitalization | usd-bn | 2026-07 | 87 | WEB-445, WEB-446 | C | Highly volatile; peaked >HK$1tn (~$130bn) Jun-2026 |
| minimax_mkt_cap_2026 | minimax | L7 | MiniMax market capitalization | usd-bn | 2026-07 | 14 | WEB-447, WEB-448 | C | Down from ~$53bn peak (Mar-2026, HK$410bn) on lock-up unlock |
| deepseek_valuation_2026 | deepseek | L7 | DeepSeek implied valuation, first external round | usd-bn | 2026 | 55 | WEB-430, WEB-431 | C | Range reported $52-59bn; RMB50bn/$7.4bn raised |
| china_coding_copilot_share | China | L8 | GitHub Copilot share of China coding-assistant market | % | 2026 | 64.5 | WEB-423 | C | Vs. Tongyi Lingma (Alibaba) 12.9% — foreign tool still leads domestically |
| china_tongyi_lingma_share | alibaba | L8 | Tongyi Lingma share of China coding-assistant market | % | 2026 | 12.9 | WEB-423 | C | Leading domestic alternative to Copilot |
| enterprise_coding_agent_market | Global | L8 | Enterprise AI coding-agent market run-rate | usd-bn | 2026-04 | 10 | WEB-423 | D | Range $9.8-11.0bn annualized; global, not China-specific (benchmark) |

---

## 3. `model_catalog.csv` — new/updated rows

| model_id | developer | release_date | params | weights | modality | benchmark_notes | price_per_mtok | context_len | chips_optimized_for | source_id | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| deepseek-v4-pro | deepseek | 2026-04-24 | 1.6T MoE, ~49B active | open | text/multimodal | SWE-bench Verified 80.6% (vs Claude Opus 4.7 80.8%, GPT-5.5 74.9%); first frontier-class model trained+served off Nvidia | ~0.87 (output, est.) | 1M | Huawei Ascend 950 + Cambricon (Day-0 adaptation); also Hygon, Moore Threads | WEB-413, WEB-414 | C |
| qwen3.7-max | alibaba | 2026 | ~1T total, ~24B active | closed (API); Qwen3 open series Apache-2.0 | multimodal | Flagship DashScope API model; 145+ official model IDs; Qwen3 open series remains most-downloaded family on Hugging Face | 2.50 (input, flagship tier); Qwen3-Max: 0.78 in / 3.90 out | 1M | Nvidia + T-Head | WEB-420, WEB-421b | C |
| glm-5.2 | zhipu | 2026-06-16 | undisclosed MoE | open (MIT license) | multimodal | #4 globally on Artificial Analysis Intelligence Index (behind Claude "Fable" 5, Opus 4.8, GPT-5.5); within ~1pt of Opus 4.8 on agentic coding at ~1/5 the cost | low (implied ~1/5 of Opus 4.8) | undisclosed | undisclosed | WEB-423, WEB-424 | C |
| hunyuan-hy3 | tencent | 2026-07-06 | 295B MoE, 21B active, 3.8B MTP | open (Apache 2.0) | multimodal | SWE-Bench Verified 78.0, SWE-Bench Pro 57.9, BrowseComp 84.2 (matches GPT-5.5), GPQA Diamond 90.4 (vs GPT-5.5 93.6), CL-bench 23.8 (#1 among Chinese models, #2 overall behind Claude Opus 4.8's 24.8) | free 2-wk OpenRouter promo at launch | 256K | undisclosed | WEB-417, WEB-418 | C |
| ernie-5.0 | baidu | 2026-01-22 | 2.4T, native full-modality | closed (weights not released) | multimodal | LMArena text leaderboard 1460, global top-10 | undisclosed | undisclosed | Kunlunxin + Nvidia | WEB-434 | C |
| ernie-5.1 | baidu | 2026-05-08 | ~1/3 total params & 1/2 active params of Ernie 5.0 (MoE) | closed (weights not released) | multimodal | #4 globally on LMArena Search Arena (1223), behind 2 Claude Opus variants + GPT-5.5 Search; trained at ~6% compute cost of comparable frontier models | undisclosed | undisclosed | Kunlunxin + Nvidia | WEB-434 | C |
| kimi-k2.6 | moonshot | 2026 | trillion-param MoE class | open | multimodal | Long-horizon coding, coding-driven UI/UX generation, multi-agent orchestration | 0.66 in / 3.41 out | undisclosed | undisclosed | WEB-415 | C |
| kimi-k2.7-code | moonshot | 2026-06 | trillion-param MoE class | open | text (coding) | Near-frontier terminal/coding scores; undercuts frontier pricing by ~10x | low (order of magnitude below frontier) | undisclosed | undisclosed | WEB-433 | D |
| kimi-k2-thinking | moonshot | 2025-2026 | 1T MoE, 32B active | open | text | Agentic, long-horizon reasoning | undisclosed | 256K | undisclosed | WEB-415 | C |
| doubao (update) | bytedance | 2025-2026 | undisclosed | closed | multimodal | DAU peak 145m (Spring Festival 2026, up from >100m late-2025); MAU 260m+ Q1-2026 (+300% YoY) | undisclosed | undisclosed | in-house + Nvidia | WEB-421 | C |

*(`deepseek-v4` and `qwen3`, `doubao`, `kimi-k2`, `minimax-m`, `glm-zai`, `ernie`, `hunyuan` seed rows should be treated as superseded/generalized by the more specific rows above — Director's call whether to replace or append.)*

---

## 4. `policy_funding_tracker.csv` — new rows

| policy_id | name | level | type | amount_usd_bn | currency_note | date_announced | horizon | target_layers | summary | source_id | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| china_national_dc_grid | National AI Data-Center Grid (NDRC) | national | plan | 295 | ~RMB 2 trillion | 2026-06-09 (Bloomberg report of draft) | 5-yr investment window to ~2031; grid completion ~2028 | L6 | NDRC draft plan to connect thousands of data centers into a unified national computing grid; mandates ≥80% domestic-sourced technology incl. AI accelerators (favoring Huawei et al.), squeezing out Nvidia/AMD; state operators (China Mobile, China Telecom) to run bulk of DCs; builds on earlier "East Data West Compute" spatial initiative | WEB-411, WEB-412 | C |
| ai_plus_diffusion_targets | "AI Plus" Initiative diffusion targets | national | plan | n.a. | n.a. | 2025-08 (State Council opinion); reinforced 2026-01 (AI Plus Manufacturing) | 2027 / 2030 / 2035 | L7\|L8 | Targets next-gen intelligent application/agent adoption >70% by 2027, ~90% by 2030, "ubiquitous" by 2035; sector plans (AI Plus Manufacturing) and SOE pilot cohorts (Baosteel, XCMG, Haier — 15 "pioneer" smart factories, >70% AI-scenario coverage, 6,000+ deployed AI models) operationalize the targets; treated by analysts as directional signaling rather than hard KPIs | WEB-436, WEB-437, WEB-438 | C |

---

## 5. Sources (`sources.csv`-style, pod-local IDs)

| source_id | type | title | author_org | date | url_or_locator | notes |
|---|---|---|---|---|---|---|
| WEB-401 | analyst | Alibaba holds wide lead in China's AI cloud market | Ainvest/SCMP/Omdia data | 2025-09 / 2026 | ainvest.com/news/alibaba-leads-china-ai-cloud-market-35-8-share-outpacing-rivals-bytedance-huawei-tencent-2509 | 35.8% H1-25, extended to ~38.1% 2026 |
| WEB-402 | news | Alibaba's Cloud and AI Momentum Accelerates | MarketChameleon | 2026-05-14 | marketchameleon.com/articles/b/2026/5/14/alibaba-cloud-ai-revenue-growth-investment-strategy-2026 | 38% YoY cloud growth |
| WEB-403 | news | Huawei's cloud computing revenue dropped in 2025 | CNBC | 2026-03-31 | cnbc.com/2026/03/31/huawei-annual-report-2025-cloud-computing-revenue.html | 17% overall cloud-infra share; -3.5% ext revenue |
| WEB-404 | news | Huawei braces for $12 billion in AI chip revenue | Tom's Hardware | 2026 | tomshardware.com/tech-industry/huawei-expects-12-billion-in-ai-chip-revenue-this-year-as-nvidias-china-market-share-hits-zero | +60% YoY AI-chip revenue est. |
| WEB-405 | analyst | Omdia cloud infra spending +26% Q4 2025 | Omdia | 2026-04 | omdia.tech.informa.com/pr/2026/apr/mainland-china-cloud-infrastructure-spending-rises-26percent-in-q4-2025 | |
| WEB-406 | news | DeepSeek raises $7.4bn at $50bn-plus valuation | The Information (via Silicon Republic) | 2026 | siliconrepublic.com/business/the-information-deepseek-raises-7-4bn-at-50bn-plus-valuation | |
| WEB-407 | news | Zhipu Hong Kong debut / IPO | CNBC | 2026-01-08 | cnbc.com/2026/01/08/china-ai-tiger-goes-ipo-zhipu-hong-kong-debut-openai-knowledge-atlas-hsi-hang-seng-listing.html | |
| WEB-408 | news | MiniMax doubles in Hong Kong debut | CNBC | 2026-01-09 | cnbc.com/2026/01/09/minimax-hong-kong-ipo-ai-tigers-zhipu.html | |
| WEB-409 | news | Moonshot Kimi K2 surpasses xAI on OpenRouter | OpenRouter (X/Twitter) | 2025 | x.com/OpenRouterAI/status/1944466834167919043 | Directional; low-formality source |
| WEB-411 | news | China drafts $295bn plan for national AI data center grid | Bloomberg / Tom's Hardware | 2026-06-09 | bloomberg.com/news/articles/2026-06-09/china-prepares-295-billion-plan-to-fund-nationwide-ai-buildout | |
| WEB-412 | news | China AI Data Center Grid Locks Out Nvidia | TechTimes | 2026-06-22 | techtimes.com/articles/318868/20260622/china-ai-data-center-grid-locks-out-nvidia-295-billion-domestic-chip-mandate.htm | |
| WEB-413 | analyst | Huawei Ascend, Cambricon, Hygon Day-0 adaptation to DeepSeek-V4 | TrendForce | 2026-04-29 | trendforce.com/news/2026/04/29/news-huawei-ascend-cambricon-and-hygon-completed-day-0-adaptation-to-deepseek-v4 | |
| WEB-414 | blog | DeepSeek V4 specs/benchmarks/pricing | NxCode / MorphLLM | 2026 | nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026 ; morphllm.com/deepseek-v4 | D-grade aggregator |
| WEB-415 | product page | Kimi K2.6 / K2 Thinking specs | OpenRouter | 2026 | openrouter.ai/moonshotai/kimi-k2.6 ; openrouter.ai/moonshotai/kimi-k2-thinking | Primary product listing |
| WEB-417 | news | Tencent Launches Hunyuan 3.0: 295B rivals GPT-5.5 | BigGo Finance | 2026-07 | finance.biggo.com/news/b62ccd99-eb32-4232-b36c-3d28046eaa14 | |
| WEB-418 | blog | Tencent Hy3 295B Open MoE | Hy3AI / ExplainX | 2026-07 | hy3ai.com ; explainx.ai/blog/tencent-hy3-295b-moe-open-source-agentic-model-2026 | D-grade |
| WEB-419 | analyst | OpenRouter data shows 61% Chinese-model token share | KuCoin News | 2026-05/06 | kucoin.com/news/flash/openrouter-data-shows-61-of-token-consumption-by-chinese-ai-models | |
| WEB-420 | product page | Qwen pricing 2026 | eesel AI | 2026 | eesel.ai/blog/qwen-pricing | |
| WEB-421 | news | China's AI chatbots advanced and versatile | NPR | 2026-03-30 | npr.org/2026/03/30/nx-s1-5760939/china-chatbot-industry-doubao-qwen-yuanbao | DAU/MAU peaks |
| WEB-422 | blog | Top 5 Chinese AI Search Engines 2026 | SecondTalent | 2026 | secondtalent.com/resources/top-5-chinese-ai-search-engines | D-grade, combined MAU |
| WEB-423 | news | Chinese AI models gaining ground with US companies | CNBC | 2026-07-07 | cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html | GLM-5.2, Copilot vs Tongyi Lingma share, coding-agent market size |
| WEB-424 | analyst | China's Open-Weight Takeover | Data Gravity (Chris Zeoli) | 2026 | datagravity.dev/p/chinas-open-weight-takeover | DeepSeek 16-17.6% OpenRouter share |
| WEB-425 | analyst | Share of US models on OpenRouter collapsed 70%→30% | OfficeChai | 2026 | officechai.com/ai/share-of-us-models-being-used-on-openrouter-has-collapsed-from-70-to-30-over-the-past-year | |
| WEB-426 | news | ByteDance raises Volcano Engine's MaaS revenue target | KrAsia | 2026 | kr-asia.com/bytedance-raises-volcano-engines-maas-revenue-target-on-seedance-2-0-growth | |
| WEB-427 | blog | Volcengine consuming 50 trillion tokens daily | 36Kr (EU) | 2026 | eu.36kr.com/en/p/3602323540346114 | D-grade, ByteDance capex figure |
| WEB-428 | news | Baidu Q1 2026: AI Revenue Surpasses 50% | AlphaPilot | 2026-05 | alphapilot.tech/discover/baidu-q1-2026-ai-revenue-surpasses-50-as-cloud-and-ernie-5-1-drive-growth | |
| WEB-429 | news | Baidu Says AI Made Up Majority of Q1 2026 Business Revenue | Winbuzzer | 2026-05-19 | winbuzzer.com/2026/05/19/baidu-says-ai-is-now-the-majority-of-its-business-xcxwbn | |
| WEB-430 | news | DeepSeek could hit $45B valuation | TechCrunch | 2026-05-06 | techcrunch.com/2026/05/06/deepseek-could-hit-45b-valuation-from-its-first-investment-round | |
| WEB-431 | news | Tencent to back DeepSeek in $4B round at $50B valuation | TechFundingNews | 2026 | techfundingnews.com/tencent-to-back-deepseek-in-4b-round-at-50b-valuation-marking-first-external-funding-report | |
| WEB-433 | blog | Best Chinese AI Models for Coding 2026 | AIMadeTools | 2026 | aimadetools.com/blog/best-chinese-ai-coding-models-2026 | D-grade, Kimi K2.7 Code pricing |
| WEB-434 | company blog | ERNIE 5.1 Officially Released | Baidu (ERNIE Blog) | 2026-05-08 | ernie.baidu.com/blog/posts/ernie-5.1-0508-release | Primary company disclosure |
| WEB-436 | analyst | China's next five-year bet on AI | Merics | 2026 | merics.org/en/comment/chinas-next-five-year-bet-ai-self-reliance-diffusion-and-lot-hype | |
| WEB-437 | blog | China's Big AI Diffusion Plan is Here | Matt Sheehan (Substack) | 2026 | mattsheehan.substack.com/p/chinas-big-ai-diffusion-plan-is-here | |
| WEB-438 | analyst | The Inaugural Year of Industrial AI Agents | Tianxia Gongchang Research | 2026 | faxiangongchang.com/en/reports/china-industrial-ai-agent-2026 | Smart-factory SOE pilot data |
| WEB-445 | news | Zhipu AI market cap tops HK$1 trillion | SCMP | 2026-06 | scmp.com/tech/article/3357858/zhipu-ai-market-cap-tops-hk1-trillion-shares-glm-52-developer-soar | |
| WEB-446 | news | AI Firm Zhipu to Raise $4 Billion | Bloomberg | 2026-07-08 | bloomberg.com/news/articles/2026-07-08/ai-firm-zhipu-to-sell-4-billion-of-shares-after-1-500-rally | |
| WEB-447 | news | MiniMax's market cap drops from ~HK$410B to HK$109B | KuCoin News | 2026-07 | kucoin.com/news/flash/minimax-s-market-cap-plummets-from-41b-to-10b-hkd-in-six-months | Headline units ambiguous (bn HKD vs bn USD); reconciled against stockanalysis.com HKG:0100 |
| WEB-448 | data | MiniMax Group (HKG:0100) Market Cap & Net Worth | StockAnalysis.com | 2026-07 | stockanalysis.com/quote/hkg/0100/market-cap | |

**Confidence-grade key:** A = filed/audited · B = primary company disclosure/press covering an earnings call or filing · C = credible third-party analyst/press · D = single-source, estimate, blog aggregator, or inferred.
