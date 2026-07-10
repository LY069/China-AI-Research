# v2 P2 — Database-ready additions (Models, Apps & Adoption Economics)

Mirrors `database/schema.md`. All new source IDs in the WEB-6xx range (P2 block) — see full list with URLs in `research/v2_p2_model_econ.md#sources`. Do NOT edit master CSVs directly; these are proposed additions for the director to merge.

---

## 1. `model_catalog.csv` — new field: `revenue_monetization_note`

v2 adds a `revenue_monetization_note` column to `model_catalog.csv` per the P2 brief. Proposed values for existing/updated rows (joins on `model_id`):

| model_id | developer | revenue_monetization_note | source_id | confidence |
|---|---|---|---|---|
| deepseek-v4-pro | deepseek | No standalone model revenue disclosed. Parent (DeepSeek/High-Flyer) revenue estimates for FY2025-26 range $13.4m–$1.1bn+ across sources with no named methodology agreeing; company's own Mar-2025 disclosure computed a "theoretical" 545% cost-profit margin but stated actual realized revenue is "substantially lower." Treat as unverified. | WEB-609, WEB-611, WEB-612 | D |
| qwen3.7-max | alibaba | No standalone Qwen P&L; monetized via DashScope/Model Studio pay-per-token API (with batch-call 50% discount) and a fixed-fee "Coding Plan" subscription bundling Qwen/GLM/Kimi/MiniMax access; revenue is folded into Alibaba Cloud segment reporting, not separately disclosed. | WEB-632, WEB-636 | C |
| glm-5.2 | zhipu | Zhipu (parent) FY2025 revenue RMB 724.33m (+131.9% YoY), net loss RMB 4.72bn; cloud-API/MaaS ARR RMB 1.7bn (60x YoY, small base); H1-2025 mix was 84.8% localized/on-prem deployment vs 15.2% cloud API — majority of disclosed revenue is enterprise/government on-prem contracts, not open-weight-driven API pull-through. | WEB-600, WEB-603, WEB-604 | B (headline) / C (mix) |
| hunyuan-hy3 | tencent | No standalone Hunyuan P&L; monetized via Tencent Cloud API (Mar-2026 price hike up to 463% off promo rates) and enterprise integration (150+ mainland enterprises on Hunyuan 3D via Tencent Cloud, incl. Unity China, Bambu Lab, Liblib) plus OpenClaw-derived agent products (ClawPro, WorkBuddy) that indirectly monetize Hunyuan inference. | WEB-621, WEB-622 | C |
| kimi-k2.6 | moonshot | No filed financials. Press-reported ARR crossed $100m (Mar-2026) → $200m+ (Apr-2026), unnamed source/methodology. Valuation ($4.3bn end-2025 → $20bn May-2026 → in talks for $30bn Jun-2026) implies ~100-150x disclosed ARR if figures hold — flagged as momentum/strategic-investor valuation, not revenue-multiple-justified. | WEB-613, WEB-614, WEB-615, WEB-616 | D |
| minimax-m | minimax | FY2025 revenue $79.0m (+158.9% YoY): AI-native consumer apps (Talkie, Hailuo) ~67% ($53.1m, +143.4% YoY); Open Platform/enterprise API ~33% ($26.0m, +197.8% YoY, ~69.4% gross margin). >70% of revenue international. Net loss $1.87bn FY2025 (incl. IPO-related valuation adjustments); 9M-2025 operating loss $512m on $53.4m revenue (~10:1 ratio). | WEB-605, WEB-606, WEB-608 | B |
| doubao (update) | bytedance | No standalone Doubao P&L (ByteDance private, no consolidated financials filed). Parent Volcengine's MaaS revenue *target* RMB 15bn for 2026 vs ~RMB 1.5bn 2025 actual (10x) — explicitly framed by company/press as a deliberate near-term margin sacrifice to seed token consumption, not a profit center. | WEB-636 (framing); v1 pod4 sources for the RMB figures | C (target, not actual) |
| ernie-5.1 (NEW row) | baidu | developer: baidu; release_date: 2026; weights: closed (API); modality: multimodal; benchmark_notes: core driver of Baidu's Q1-2026 "AI Applications" revenue line; chips_optimized_for: Kunlunxin + Nvidia legacy. **Monetization note:** Baidu SEC 6-K names "Revenue from AI Applications" as a distinct line: RMB 2.5bn in Q1-2026, ~flat YoY, even as GPU-cloud subscription revenue +184% YoY and total AI-related revenue crossed 50% of group revenue for the first time — clearest primary-source evidence of an adoption/monetization gap (200m+ Ernie MAU, 26,000+ active enterprise customers, but applications-revenue line not growing). | WEB-633, WEB-634 | A/B |

---

## 2. `metrics_timeseries.csv` — new rows

| metric_id | entity | layer | metric_name | unit | period | value | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|
| zhipu_revenue | zhipu | L7 | Annual revenue | RMB m | 2025 | 724.33 | WEB-600, WEB-604 | B | +131.9% YoY; ~$104.8m at contemporaneous FX |
| zhipu_net_loss | zhipu | L7 | Annual net loss | RMB bn | 2025 | 4.72 | WEB-602, WEB-604 | B | +59.5% YoY |
| zhipu_rd_spend | zhipu | L7 | R&D expense | RMB bn | 2025 | 3.18 | WEB-604 | B | +44.9% YoY |
| zhipu_maas_arr | zhipu | L7 | MaaS/cloud-API ARR | RMB bn | 2025 | 1.7 | WEB-603, WEB-604 | C | 60x YoY off small base |
| zhipu_gross_margin | zhipu | L7 | Overall gross margin | % | 2025 | 41.0 | WEB-604 | C | down from 56.3% (2024); mix-shift to lower-margin on-prem deployment |
| zhipu_cloud_api_gross_margin | zhipu | L7 | Cloud-API segment gross margin | % | 2025 | 18.9 | WEB-603, WEB-604 | C | up from 3.3% (2024) |
| zhipu_onprem_rev_share | zhipu | L7 | Share of revenue from localized/on-prem deployment | % | 2025-H1 | 84.8 | WEB-603 | C | 88.4% of this from mainland China customers |
| zhipu_loss_to_rev_ratio | zhipu | L7 | Net loss / revenue ratio | ratio | 2025 | ~6.5:1 | WEB-608 (framing), WEB-600/WEB-602 (derived) | C | derived from B-grade headline figures; H1-2025 in isolation was worse (~12:1) |
| minimax_revenue | minimax | L7 | Annual revenue | $ m | 2025 | 79.0 | WEB-605 | B | +158.9% YoY |
| minimax_net_loss | minimax | L7 | Annual net loss | $ bn | 2025 | 1.87 | WEB-605 | B | includes IPO-related valuation/share-based adjustments |
| minimax_ai_native_rev | minimax | L7 | AI-native consumer product revenue (Talkie, Hailuo) | $ m | 2025 | 53.1 | WEB-605, WEB-606 | B | +143.4% YoY; ~67% of total revenue |
| minimax_open_platform_rev | minimax | L7 | Open Platform (enterprise/API) revenue | $ m | 2025 | 26.0 | WEB-605, WEB-606 | B | +197.8% YoY; ~69.4% gross margin |
| minimax_9m_net_loss | minimax | L7 | 9-month net loss | $ m | 2025-Q3(9mo) | 512 | WEB-608 | C | on $53.4m 9-month revenue, ~10:1 ratio |
| deepseek_revenue_est_low | deepseek | L7 | Annual revenue (low estimate) | $ m | 2025 | 13.4 | WEB-611 | D | aggregator extrapolation from headcount; unverified |
| deepseek_revenue_est_mid | deepseek | L7 | Annual revenue run-rate (mid estimate) | $ m | 2025-mid | 220 | (unnamed source, see memo) | D | unverified, no named methodology |
| deepseek_revenue_est_high | deepseek | L7 | Annual revenue (high estimate) | $ bn | 2026 | 1.1 | WEB-612 | D | unverified, aggregator, no named methodology |
| deepseek_theoretical_margin | deepseek | L7 | "Theoretical" cost-profit margin (if fully billed at list price) | % | 2025-03 | 545 | WEB-609, WEB-610 | C | company-disclosed but explicitly caveated as not realized revenue |
| moonshot_arr | moonshot | L7 | Annualized recurring revenue | $ m | 2026-04 | 200+ | WEB-616 | D | press-reported, unnamed source; crossed $100m Mar-2026 |
| moonshot_valuation | moonshot | L7 | Private-round valuation | $ bn | 2026-05 | 20 | WEB-613, WEB-614 | C | $2bn round led by Meituan's Long-Z Investments |
| moonshot_valuation_talks | moonshot | L7 | Reported valuation in active funding talks | $ bn | 2026-06 | 30 | WEB-615 | C | in talks, not closed |
| volcengine_maas_target_2026 | bytedance | L6/L7 | Volcengine MaaS revenue target | RMB bn | 2026 | 15 | v1 pod4 sourcing; framing WEB-636 | C | target vs ~RMB 1.5bn 2025 actual; 10x |
| baidu_ai_app_revenue | baidu | L7 | "Revenue from AI Applications" (named 6-K line item) | RMB bn | 2026-Q1 | 2.5 | WEB-633 | A | ~flat YoY; SEC primary filing |
| baidu_gpu_cloud_rev_growth | baidu | L6 | GPU-cloud subscription revenue growth | % YoY | 2026-Q1 | 184 | WEB-633, WEB-634 | A | SEC primary filing |
| baidu_ernie_enterprise_customers | baidu | L7 | Active enterprise customers on Ernie ecosystem | count | 2026-Q1 | 26,000+ | WEB-634 | C | |
| tencent_hunyuan_3d_enterprise_integrations | tencent | L7 | Mainland enterprises integrated with Hunyuan 3D via Tencent Cloud | count | 2026-mid | 150+ | (Tencent official; see memo) | B | named examples: Unity China, Bambu Lab, Liblib |
| tencent_clawpro_beta_orgs | tencent | L8 | Organizations using ClawPro during internal beta | count | 2026-Q1 | 200+ | WEB-621, WEB-622 | C | finance, government, manufacturing sectors |
| tencent_workbuddy_pilot_users | tencent | L8 | Employees piloting WorkBuddy | count | 2026-Q1 | 2,000+ | WEB-623 | C | HR/admin/ops, non-technical |
| alibaba_wukong_dingtalk_reach | alibaba | L8 | Organizations reachable via DingTalk (Wukong distribution base) | count (m) | 2026-03-17 | 20 | WEB-625, WEB-626 | C | launch date; runs on Qwen, not Western model |
| openclaw_github_stars | openclaw (non-Chinese OSS project) | L8 | GitHub stars | count (k) | 2026-04 | 250-350 | WEB-617, WEB-618, WEB-620 | C | range across sources; MIT license |
| china_industrial_ai_agent_application_rate_2024 | China | L8 | Industrial enterprises applying large models/AI agents | % | 2024 | 9.6 | WEB-628 | C | |
| china_industrial_ai_agent_application_rate_2025 | China | L8 | Industrial enterprises applying large models/AI agents | % | 2025 | 47.5 | WEB-628 | C | up from 9.6% in 2024 |

---

## 3. `company_master.csv` — notes-field updates (no new companies; existing rows only)

| company_id | notes addition | source_id | confidence |
|---|---|---|---|
| zhipu (or equivalent v1 slug) | FY2025 filed financials: revenue RMB 724.33m (+131.9% YoY), net loss RMB 4.72bn (+59.5% YoY); loss/revenue ratio ~6.5:1; 84.8% of H1-2025 revenue from on-prem/localized deployment (88.4% mainland China customers) vs 15.2% cloud API. First Chinese model lab with filing-grade financials. | WEB-600, WEB-602, WEB-603, WEB-604 | B |
| minimax | FY2025 filed/press-released financials: revenue $79.0m (+158.9% YoY), net loss $1.87bn (incl. IPO valuation adjustments); revenue is majority consumer-app-driven (Talkie/Hailuo, ~67%) not enterprise-API-driven (~33%); >70% of revenue international — the one lab in this set whose revenue is predominantly non-domestic. | WEB-605, WEB-606, WEB-608 | B |
| tencent | Built OpenClaw-derived enterprise agent suite in Mar-2026: WorkBuddy (2,000+ employee pilot), ClawBot (WeChat-native, 1bn+ MAU reach), ClawPro (200+ beta orgs, finance/govt/manufacturing). Hunyuan Hy3 (295B MoE, Apache 2.0, Jul-2026) has 150+ enterprise integrations via Tencent Cloud (Unity China, Bambu Lab, Liblib named). No standalone Hunyuan model P&L disclosed. | WEB-621, WEB-622, WEB-623 | C |
| alibaba | Launched Wukong (Mar-17-2026), DingTalk-unit multi-agent enterprise platform reaching ~20m organizations via existing DingTalk install base, running on Qwen (not a Western model); explicitly framed as an OpenClaw-era competitive response alongside Tencent/ByteDance/Baidu. No standalone Qwen model P&L; monetized via DashScope/Model Studio API bundled into Alibaba Cloud segment revenue. | WEB-625, WEB-626, WEB-627, WEB-632 | C |
| baidu | Q1-2026 SEC 6-K names "Revenue from AI Applications" as a distinct line item: RMB 2.5bn, approximately flat YoY, even as GPU-cloud subscription revenue grew 184% YoY and total AI-related revenue crossed 50% of group revenue for the first time — best-disclosed adoption/monetization-gap data point among the cloud-parented labs (200m+ Ernie MAU, 26,000+ active enterprise customers, but applications-revenue line not growing). | WEB-633, WEB-634 | A/B |
| bytedance | Volcengine (cloud unit) MaaS revenue target RMB 15bn for 2026 vs ~RMB 1.5bn actual 2025 (10x) — company/press frame this as deliberate near-term margin sacrifice to seed Doubao-family token consumption, not a profit center. ByteDance remains private with no consolidated financial disclosure; Doubao model-level revenue cannot be isolated. | v1 pod4 sourcing; WEB-636 (framing) | C |
| deepseek | No filed financials as of 2026-07-10. Revenue estimates across third-party sources span $13.4m to >$1.1bn for overlapping FY2025-26 periods with no named/consistent methodology — treat as unverified/unknowable rather than as a bounded range. Company's own Mar-2025 disclosure of a "theoretical" 545% cost-profit margin explicitly stated actual realized revenue is substantially lower. | WEB-609, WEB-610, WEB-611, WEB-612 | D |
| moonshot | No filed financials. Press-reported ARR crossed $100m (Mar-2026) → $200m+ (Apr-2026); valuation trajectory $4.3bn (end-2025) → $10bn (Jan-2026) → $20bn (May-2026, Meituan-led) → in talks for $30bn (Jun-2026) — implies ~100-150x disclosed ARR if figures hold; flag valuation as momentum/strategic-investor-driven, not revenue-multiple-justified. | WEB-613, WEB-614, WEB-615, WEB-616 | D |

---

## Sources list (WEB-6xx, P2 block)

See `research/v2_p2_model_econ.md`, "## Sources" section, for the full numbered list with titles, dates, confidence grades, and URLs (WEB-600 through WEB-636). Reproduced here in compact form for `sources.csv` ingestion:

| source_id | type | title | author_org | date | url | confidence |
|---|---|---|---|---|---|---|
| WEB-600 | news | Zhipu AI revenue jumps 132% in first post-IPO report, missing estimates | SCMP | 2026 | https://www.scmp.com/tech/tech-trends/article/3348555/zhipu-ai-revenue-jumps-132-first-post-ipo-report-missing-estimates | C |
| WEB-601 | news | Zhipu's Stock Soars After Chinese AI Startup's Annual Revenue More Than Doubles | Yicai Global | 2026 | https://www.yicaiglobal.com/news/zhipus-stock-soars-after-chinese-ai-startups-annual-revenue-more-than-doubles | C |
| WEB-602 | news | Zhipu Gains $14 Billion Value After AI Fever Overrides Big Loss | Bloomberg | 2026-03-31 | https://www.bloomberg.com/news/articles/2026-03-31/zhipu-s-losses-climb-60-after-chinese-ai-rivalry-worsens | C |
| WEB-603 | news | Zhipu's revenue skyrocketed by 132% in 2025, with cloud service income increasing nearly threefold | Futunn News | 2026 | https://news.futunn.com/en/post/70896593/zhipu-s-revenue-skyrocketed-by-132-in-2025-with-cloud | C |
| WEB-604 | news | Zhipu AI's First Annual Report: Revenue Doubles, Losses Widen | BigGo Finance | 2026 | https://finance.biggo.com/news/aShTSp0BvthpMgHBHzpO | C |
| WEB-605 | press-release | MiniMax Global Announces Full Year 2025 Financial Results | MiniMax (official) | 2026 | https://www.minimax.io/news/minimax-global-announces-full-year-2025-financial-results | B |
| WEB-606 | filing | Global Offering prospectus, MiniMax Group Inc. | HKEXnews | 2025-12-31 | https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1231/2025123100025.pdf | B |
| WEB-607 | analyst | MiniMax revenue seen rising to $219M in 2026, reaching $5.8B by 2030 | S&P Global Market Intelligence | 2026-04 | https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/minimax-revenue-seen-rising-to-usd219m-in-2026-reaching-usd6b-by-2030 | C |
| WEB-608 | news | China's Zhipu AI and MiniMax burn $10 for every $1 in revenue | CIW | 2026 | https://www.ciw.news/p/zhipu-ai-minimax-ipo | C |
| WEB-609 | news | DeepSeek claims 'theoretical' profit margins of 545% | TechCrunch | 2025-03-01 | https://techcrunch.com/2025/03/01/deepseek-claims-theoretical-profit-margins-of-545/ | C |
| WEB-610 | news | DeepSeek shows power of V3, R1 models with theoretical 545% profit margin | SCMP | 2025 | https://www.scmp.com/tech/big-tech/article/3300734/deepseek-shows-power-v3-r1-models-theoretical-545-profit-margin | C |
| WEB-611 | aggregator | How DeepSeek hit $13.4M revenue with a 122-person team in 2025 | Latka | 2026 | https://getlatka.com/companies/deepseek.com | D |
| WEB-612 | aggregator | DeepSeek Revenue and Usage Statistics (2026) | Business of Apps | 2026 | https://www.businessofapps.com/data/deepseek-statistics/ | D |
| WEB-613 | news | China's Moonshot AI raises $2B at $20B valuation | TechCrunch | 2026-05-07 | https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/ | C |
| WEB-614 | news | Kimi chatbot maker Moonshot AI Valued at $20 Billion in Meituan-Led Round | Bloomberg | 2026-05-07 | https://www.bloomberg.com/news/articles/2026-05-07/kimi-chatbot-maker-moonshot-ai-valued-at-20-billion-in-meituan-led-round | C |
| WEB-615 | news | China's Moonshot AI Seeks $30 Billion Value in New Funding Talks | Bloomberg | 2026-06-08 | https://www.bloomberg.com/news/articles/2026-06-08/china-s-moonshot-ai-seeks-30-billion-value-in-new-funding-talks | C |
| WEB-616 | news | Moonshot AI Closes $2B Funding Round at $20B Valuation (ARR figures) | The AI Insider | 2026-05-08 | https://theaiinsider.tech/2026/05/08/moonshot-ai-closes-2b-funding-round-at-20b-valuation-as-kimi-models-rival-openai-and-anthropic/ | D |
| WEB-617 | newsletter | EV #559: OpenClaw & agentic breakthrough | Exponential View | 2026 | https://www.exponentialview.co/p/ev-559 | C |
| WEB-618 | article | OpenClaw: Anatomy of a viral open source AI agent | All Things Open | 2026 | https://allthingsopen.org/articles/openclaw-viral-open-source-ai-agent-architecture | C |
| WEB-619 | reference | OpenClaw | Wikipedia | accessed 2026-07 | https://en.wikipedia.org/wiki/OpenClaw | C |
| WEB-620 | blog | OpenClaw Complete Guide 2026 (347K Stars) | Jitendra Zaa | 2026-04 | https://www.jitendrazaa.com/blog/ai/clawdbot-complete-guide-open-source-ai-assistant-2026/ | D |
| WEB-621 | news | Tencent launches ClawPro enterprise AI agent platform built on OpenClaw | TheNextWeb | 2026 | https://thenextweb.com/news/tencent-clawpro-openclaw-enterprise-ai-agents | C |
| WEB-622 | news | Tencent expands OpenClaw suite with enterprise tool amid China's 'lobster' craze | SCMP | 2026 | https://www.scmp.com/tech/article/3348942/tencent-expands-openclaw-suite-enterprise-tool-amid-chinas-lobster-craze | C |
| WEB-623 | news | Tencent launches OpenClaw-like workplace AI agent WorkBuddy | TechNode | 2026-03-09 | https://technode.com/2026/03/09/tencent-launches-openclaw-like-workplace-ai-agent-workbuddy/ | C |
| WEB-624 | news | Column: OpenClaw ignites China's AI agent land grab | Digitimes | 2026-03-19 | https://www.digitimes.com/news/a20260319PD207/china-ai-agent-software-alibaba-bytedance-tencent-2026.html | C |
| WEB-625 | news | Alibaba Joins OpenClaw-Driven AI Agent Race With Wukong Platform | Caixin Global | 2026-03-18 | https://www.caixinglobal.com/2026-03-18/alibaba-joins-openclaw-driven-ai-agent-race-with-wukong-platform-102424061.html | C |
| WEB-626 | news | Alibaba launches agentic AI tool for businesses with Slack, Teams integration plans | CNBC | 2026-03-17 | https://www.cnbc.com/2026/03/17/alibaba-wukong-ai-enterprise-tool-restructuring-qwen-exits.html | C |
| WEB-627 | news | Alibaba joins AI agent race with Wukong launch | Computer Weekly | 2026-03 | https://www.computerweekly.com/news/366640461/Alibaba-joins-AI-agent-race-with-Wukong-launch | C |
| WEB-628 | analyst | The Inaugural Year of Industrial AI Agents | Tianxia Gongchang Research | 2026 | https://faxiangongchang.com/en/reports/china-industrial-ai-agent-2026 | C |
| WEB-629 | analyst | How China Turned Its Platform Economy Into an AI Deployment Machine | Council on Foreign Relations | 2026 | https://www.cfr.org/articles/chinas-platform-economy-is-an-ai-deployment-engine-the-u-s-is-still-looking-for-its-own | C |
| WEB-630 | survey | Deloitte-HKU AI Adoption Index 2026: The Paradox of Promise and Performance | Deloitte / HKU CAMO | 2026 | https://camo.hku.hk/ai-adoption-survey/ | B |
| WEB-631 | synthesis | AI Agent Adoption in 2026: What the Analysts Data Shows | Joget (synth. Gartner/IDC) | 2026 | https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/ | D |
| WEB-632 | official docs | Model Studio / DashScope pricing & product documentation | Alibaba Cloud (official) | accessed 2026-07 | https://www.alibabacloud.com/help/en/model-studio/model-pricing | B |
| WEB-633 | filing | Form 6-K, FY2026 Q1 results | Baidu, Inc. / SEC | 2026-05 | https://www.sec.gov/Archives/edgar/data/1329099/000119312526110843/d34060dex991.pdf | A |
| WEB-634 | news | Baidu Q1 2026: AI Revenue Surpasses 50% as Cloud and ERNIE 5.1 Drive Growth | AlphaPilot | 2026-05 | https://www.alphapilot.tech/discover/baidu-q1-2026-ai-revenue-surpasses-50-as-cloud-and-ernie-5-1-drive-growth | C |
| WEB-635 | analyst | Where China's AI models make their money | Bamboo Works | 2026 | https://thebambooworks.com/where-chinas-ai-models-make-their-money/ | C |
| WEB-636 | news | From commodity to currency: How Alibaba is monetizing the AI moment | CRN Asia | 2026 | https://www.crnasia.com/news/2026/artificial-intelligence/from-commodity-to-currency-how-alibaba-is-monetizing-the-ai | C |
