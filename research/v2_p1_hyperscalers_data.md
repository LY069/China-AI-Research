# v2 P1 — Database-Ready Additions (Hyperscalers & Compute Capex)

Mirrors `/database/schema.md` (incl. v2 additions). All rows below are proposed additions/updates for the Research Director to merge — **master CSVs were not edited directly, no git commands were run.** Source IDs are pod-local (`WEB-5xx`, per the v2 numbering convention: P1 = WEB-5xx) and map 1:1 to the numbered sources in `v2_p1_hyperscalers.md` §Sources; the Director should reconcile/renumber against the global `sources.csv` on merge. Non-Chinese comparator entities (Microsoft, Alphabet, Amazon, Meta) are new to the database in this pod — they do not have existing `company_master` rows and are added here as reference/benchmark entities only (out of scope for the "China AI stack" investable-company set; included for the capex-comparison metrics only).

---

## 1. `company_master.csv` — updates to existing rows

Existing `company_id`s unchanged; only the `notes` field is extended below (financial detail this pod adds on top of the v1/seed row — full row not restated, Director should append to existing `notes`).

| company_id | field updated | v2 P1 addition | source_id | confidence |
|---|---|---|---|---|
| alibaba | notes (append) | FY2026 (FYE Mar-2026): total revenue ~RMB1.02tn; Cloud Intelligence Group Q4 revenue RMB41,626m (+38% YoY); AI-product revenue RMB8,971m Q4 (11th straight qtr triple-digit growth); FY2026 capex RMB126,063m (~$18.28bn, ~3.9x FY2024's RMB32,087m); **FY2026 free cash flow turned NEGATIVE for the first time (-RMB46,609m) vs +RMB73,870m FY2025**; funded partly via convertible/exchangeable bond net proceeds (~RMB32bn combined) against a RMB520,824m cash cushion; China E-commerce Group adjusted EBITA fell 44% YoY (instant-retail subsidy war compounding capex pressure, not funding it) | WEB-501, WEB-502, WEB-503 | B/C |
| tencent | notes (append) | Q1-2026 revenue RMB196.5bn (+9% YoY); non-IFRS net profit RMB67.9bn (+11% YoY); FinTech & Business Services segment RMB59.9bn (+9% YoY, cloud/AI sub-line +20% YoY); Q1-2026 capex RMB31.9bn (+63% QoQ); FY2025 capex RMB79.2bn (+3% YoY) vs FY2025 revenue RMB751.8bn (~10.5% capex intensity, derived); **FCF still comfortably exceeds capex**; first bond issuance (dim-sum) since Apr-2021 in 2026, characterized as refinancing/optionality rather than capex necessity; Tencent does not disclose a standalone AI-cloud revenue line (disclosure gap vs. Alibaba/Baidu) | WEB-504, WEB-506, WEB-507, WEB-528, WEB-529 | B/C |
| baidu | notes (append) | Q1-2026 revenue RMB32.1bn (-2% QoQ); AI Cloud Infra revenue RMB8.8bn (+79% YoY, +52% QoQ); Core AI-powered Business RMB13.6bn (+49% YoY, **52% of Core revenue for first time**); Online Marketing (legacy ads) RMB12.6bn (-22% YoY); Legacy Business RMB10.2bn (-29% YoY) — legacy is dragging, not funding, the AI pivot; OCF only RMB2.7bn Q1-2026 (3rd positive qtr since Q3-2025); cash/investments RMB279.3bn; **management stated explicitly on the earnings call that AI capex is funded via "a mix of financing channels...including operating leases, financial leases, and other low-cost bank borrowings"** — clearest company-level admission of external-financing dependence in the peer set; specific capex RMB figure not disclosed in sources reviewed (flagged gap) | WEB-508, WEB-509, WEB-510, WEB-511 | B |
| bytedance | notes (append) | 2025 revenue est. ~$186bn (+~20% YoY, Sacra estimate, unaudited/D); international revenue crossed 30% of total for first time 2025; 2025 net profit fell >70% YoY on AI spend (sourced reporting, unaudited); 2025 capex est. ~$25bn; **2026 capex guidance conflicting and unresolved between sources**: RMB200bn+ (~$29.4bn, SCMP/Seeking Alpha, +25% vs prior RMB160bn plan) vs. up to $70bn (Bloomberg, explicitly unconfirmed by company, Reuters could not verify); no public bond/debt disclosure found — profit compression is the only visible funding-source signal (D) | WEB-521, WEB-522, WEB-523, WEB-524, WEB-525 | C/D |

---

## 2. New reference rows — US hyperscaler comparators (not in `company_master.csv`; benchmark-only, added for metrics joins)

| company_id (proposed) | name_en | layers | segment | ownership | listing_status | exchange_ticker | entity_list | investable_foreign | china_role | global_peer | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| microsoft | Microsoft Corporation | n.a. (benchmark) | Azure / AI infra | private, listed | listed | NASDAQ:MSFT | n.a. | n.a. | benchmark-only | — | WEB-520 | C | FY runs Jul-Jun; FY2024 actual capex $44.48bn; FY2026 guidance tracking ~$120bn (~2.7x) |
| alphabet | Alphabet Inc. | n.a. (benchmark) | Google Cloud / AI infra | private, listed | listed | NASDAQ:GOOGL | n.a. | n.a. | benchmark-only | — | WEB-518, WEB-524, WEB-533 | A/B/C | CY2024 actual capex $52.54bn; 2026 guidance $175-190bn (~3.4-3.6x); raised $84.75bn (upsized to $90bn) equity offering Jun-2026 explicitly for AI capex; long-term debt quadrupled in 2025 to $46.5bn; ~15% of $180bn 2026 capex plan debt-financed |
| amazon | Amazon.com, Inc. | n.a. (benchmark) | AWS | private, listed | listed | NASDAQ:AMZN | n.a. | n.a. | benchmark-only | — | WEB-532 | C | CY2024 actual capex $83.0bn; 2026 guidance ~$200bn (~2.4x); FCF projected negative $17-28bn 2026 (analyst est., D) |
| meta | Meta Platforms, Inc. | n.a. (benchmark) | AI infra (non-cloud-service) | private, listed | listed | NASDAQ:META | n.a. | n.a. | benchmark-only | — | WEB-519 | A | CY2024 actual capex $39.23bn (incl. finance-lease principal payments, per 10-K/8-K); 2026 guidance $115-135bn (~2.9-3.4x) |

---

## 3. `metrics_timeseries.csv` — new rows

| metric_id | entity | layer | metric_name | unit | period | value | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|
| alibaba_cloud_rev_q4fy26 | alibaba | L6 | Cloud Intelligence Group revenue | rmb-mn | 2026-Q4(FYE Mar) | 41626 | WEB-501 | B | +38% YoY; external-customer growth accelerated to 40% |
| alibaba_ai_product_rev_q4fy26 | alibaba | L7 | AI-related product revenue | rmb-mn | 2026-Q4(FYE Mar) | 8971 | WEB-501 | B | 11th consecutive quarter of triple-digit YoY growth |
| alibaba_capex_fy26 | alibaba | L6 | Alibaba full-year capex | rmb-mn | FY2026(FYE Mar) | 126063 | WEB-502 | A | vs RMB85,972m FY2025, RMB32,087m FY2024; SEC 6-K |
| alibaba_capex_fy25 | alibaba | L6 | Alibaba full-year capex | rmb-mn | FY2025(FYE Mar) | 85972 | WEB-502 | A | SEC 6-K restated comparative |
| alibaba_capex_fy24 | alibaba | L6 | Alibaba full-year capex | rmb-mn | FY2024(FYE Mar) | 32087 | WEB-502 | A | SEC 6-K restated comparative |
| alibaba_capex_intensity_fy26 | alibaba | L6 | Capex as % of total revenue | % | FY2026(FYE Mar) | 12.4 | WEB-501, WEB-502 | C | Derived: capex ÷ ~RMB1.02tn FY2026 revenue; pod-calculated, not company-stated |
| alibaba_fcf_fy26 | alibaba | macro | Free cash flow | rmb-mn | FY2026(FYE Mar) | -46609 | WEB-503 | C | First FCF-negative year in this data set; vs +73870 FY2025 |
| alibaba_fcf_fy25 | alibaba | macro | Free cash flow | rmb-mn | FY2025(FYE Mar) | 73870 | WEB-503 | C | Comparative |
| alibaba_cash_investments_fy26 | alibaba | macro | Cash and liquid investments | rmb-mn | 2026-03-31 | 520824 | WEB-503 | C | ~$75.5bn |
| alibaba_debt_raise_fy26 | alibaba | macro | Convertible/exchangeable bond net proceeds | rmb-mn | FY2026(FYE Mar) | 31953 | WEB-503 | B | RMB20,967m convertible notes + RMB10,986m exchangeable bonds; SEC 6-K |
| alibaba_ecommerce_ebita_fy26 | alibaba | L8 | China E-commerce Group adjusted EBITA | rmb-mn | FY2026(FYE Mar) | 107509 | WEB-502, WEB-511 | B | -44% YoY; instant-retail subsidy war |
| tencent_fbs_rev_q1_2026 | tencent | L6 | FinTech & Business Services segment revenue | rmb-bn | 2026-Q1 | 59.9 | WEB-506 | B | +9% YoY; Business Services sub-line +20% YoY on cloud/AI demand + pricing |
| tencent_capex_q1_2026 | tencent | L6 | Tencent capex | rmb-bn | 2026-Q1 | 31.9 | WEB-507, WEB-530 | C | +63% QoQ, +16% YoY |
| tencent_capex_fy2025 | tencent | L6 | Tencent full-year capex | rmb-bn | 2025 | 79.2 | WEB-529 | C | +3% YoY |
| tencent_capex_intensity_fy2025 | tencent | L6 | Capex as % of total revenue | % | 2025 | 10.5 | WEB-529 | C | Derived: RMB79.2bn ÷ RMB751.8bn revenue; pod-calculated |
| tencent_revenue_fy2025 | tencent | macro | Tencent total revenue | rmb-bn | 2025 | 751.8 | WEB-529 | C | Record high per company framing |
| tencent_net_profit_q1_2026 | tencent | macro | Non-IFRS net profit | rmb-bn | 2026-Q1 | 67.9 | WEB-504 | B | +11% YoY |
| baidu_ai_cloud_infra_rev_q1_2026 | baidu | L6 | AI Cloud Infra revenue | rmb-bn | 2026-Q1 | 8.8 | WEB-508, WEB-509 | B | +79% YoY, +52% QoQ |
| baidu_core_ai_rev_share_q1_2026 | baidu | macro | Core AI-powered Business as % of Baidu Core (General Business) revenue | % | 2026-Q1 | 52 | WEB-508, WEB-510 | B | First time crossing 50% |
| baidu_legacy_ads_rev_q1_2026 | baidu | L8 | Online Marketing Services (legacy ads) revenue | rmb-bn | 2026-Q1 | 12.6 | WEB-510 | B | -22% YoY, -17% QoQ |
| baidu_ocf_q1_2026 | baidu | macro | Operating cash flow | rmb-bn | 2026-Q1 | 2.7 | WEB-508 | B | 3rd consecutive positive quarter since Q3-2025 |
| baidu_cash_investments_q1_2026 | baidu | macro | Cash and investments | rmb-bn | 2026-03-31 | 279.3 | WEB-508 | B | ~$40.5bn |
| bytedance_revenue_2025e | bytedance | macro | ByteDance total revenue (estimate) | usd-bn | 2025 | 186 | WEB-523 | D | Sacra equity-research estimate; unaudited private company |
| bytedance_revenue_2024e | bytedance | macro | ByteDance total revenue (estimate) | usd-bn | 2024 | 155 | WEB-523 | D | Comparative |
| bytedance_capex_2025e | bytedance | L6 | ByteDance capex (estimate) | usd-bn | 2025 | 25 | WEB-521 | D | Referenced within 2026 guidance reporting |
| bytedance_capex_2026e_low | bytedance | L6 | ByteDance capex guidance (lower estimate) | usd-bn | 2026 | 29.4 | WEB-522 | D | RMB200bn+, +25% vs prior RMB160bn plan |
| bytedance_capex_2026e_high | bytedance | L6 | ByteDance capex guidance (higher, unconfirmed estimate) | usd-bn | 2026 | 70 | WEB-521 | D | Bloomberg; explicitly unconfirmed by company, Reuters could not verify |
| bytedance_profit_decline_2025 | bytedance | macro | ByteDance net profit YoY change | % | 2025 | -70 | WEB-524, WEB-525 | D | "More than 70%" decline attributed to AI investment; unaudited, sourced reporting |
| microsoft_capex_fy2024 | microsoft | macro | Microsoft capex | usd-bn | FY2024(FYE Jun) | 44.48 | WEB-520 | C | Aggregator of 10-K data |
| microsoft_capex_fy2026e | microsoft | macro | Microsoft capex guidance | usd-bn | FY2026(FYE Jun) | 120 | WEB-516, WEB-517 | C | "Tracking toward approximately"; ~2.7x FY2024 |
| alphabet_capex_2024 | alphabet | macro | Alphabet capex | usd-bn | 2024 | 52.535 | WEB-518 | C | Aggregator of 10-K data |
| alphabet_capex_2026e | alphabet | macro | Alphabet capex guidance | usd-bn | 2026 | 182.5 | WEB-516, WEB-517 | C | Midpoint of $175-190bn range; raised mid-year |
| alphabet_equity_raise_2026 | alphabet | macro | Alphabet equity offering for AI capex | usd-bn | 2026-06 | 84.75 | WEB-524, WEB-525, WEB-533 | A/B | Upsized from $80bn; grew to $90bn with underwriter over-allotment; SEC 8-K/FWP |
| alphabet_debt_raise_2026 | alphabet | macro | Alphabet bond issuance (Feb-2026 tranche) | usd-bn | 2026-02 | 31.5 | WEB-536, WEB-537 | C | Incl. rare 100-yr bond; long-term debt quadrupled in 2025 to $46.5bn |
| alphabet_fcf_2026e | alphabet | macro | Alphabet FCF projection | usd-bn | 2026 | 8.2 | WEB-516 | D | Analyst estimate (Pivotal Research), vs $73.3bn 2025; NOT company guidance |
| amazon_capex_2024 | amazon | macro | Amazon capex | usd-bn | 2024 | 83.0 | WEB-532 | C | |
| amazon_capex_2026e | amazon | macro | Amazon capex guidance | usd-bn | 2026 | 200 | WEB-516, WEB-517 | C | ~2.4x 2024 |
| amazon_fcf_2026e | amazon | macro | Amazon FCF projection | usd-bn | 2026 | -22.5 | WEB-516 | D | Analyst estimate range -$17bn to -$28bn (Morgan Stanley/BofA); midpoint shown; NOT company guidance |
| meta_capex_2024 | meta | macro | Meta capex | usd-bn | 2024 | 39.23 | WEB-519 | A | Incl. finance-lease principal payments; SEC 8-K exhibit |
| meta_capex_2026e | meta | macro | Meta capex guidance | usd-bn | 2026 | 125 | WEB-516, WEB-517 | C | Midpoint of $115-135bn range |
| us_hyperscaler4_capex_2026e | US (MSFT+GOOGL+AMZN+META) | macro | Combined 2026 capex guidance | usd-bn | 2026 | 725 | WEB-518 | C | Goldman Sachs estimate via press; vs ~$410bn 2025; +77% YoY |
| us_hyperscaler4_debt_2026e | US (MSFT+GOOGL+AMZN+META) | macro | Combined planned 2026 debt issuance | usd-bn | 2026 | 400 | WEB-516 | C | vs $165bn 2025; more than doubled |
| us_hyperscaler4_ocf_capex_ratio_2026e | US (MSFT+GOOGL+AMZN+META) | macro | Capex as % of operating cash flow | % | 2026 | 90 | WEB-516 | C | Up from ~65% 2025 |

---

## 4. Sources (`sources.csv`-style, pod-local IDs, WEB-5xx range per v2 convention)

| source_id | type | title | author_org | date | url_or_locator | notes |
|---|---|---|---|---|---|---|
| WEB-501 | filing/press | Alibaba Group Announces March Quarter 2026 and Fiscal Year 2026 Results | Alibaba Group (Morningstar/BusinessWire mirror) | 2026-05-13 | morningstar.com/news/business-wire/20260512841182/alibaba-group-announces-march-quarter-2026-and-fiscal-year-2026-results | Official release; primary |
| WEB-502 | filing | Alibaba Group Holding Ltd — SEC Form 6-K, FY2026 results exhibit | Alibaba Group / SEC | 2026-05 | sec.gov/Archives/edgar/data/0001577552/000119312526274928/d133513dex991.pdf | Capex, FCF, debt detail; primary filing |
| WEB-503 | news | Alibaba (NYSE: BABA) boosts AI cloud but FY2026 cash flow turns negative | StockTitan (SEC filing summary) | 2026-05 | stocktitan.net/sec-filings/BABA/6-k-alibaba-group-holding-ltd-current-report-foreign-issuer-164c9931befd.html | Summarizes SEC 6-K figures |
| WEB-504 | filing/press | Tencent Announces 2026 First Quarter Results | Tencent Holdings (PRNewswire mirror) | 2026-05-13 | prnewswire.com/apac/news-releases/tencent-announces-2026-first-quarter-results-302770779.html | Official release; primary |
| WEB-506 | news | Tencent Fintech and Cloud Services Lift Q1 2026 Revenue 9% to US$8.68 Billion | Fintech News Hong Kong | 2026-05 | fintechnews.hk/38862/fintechchina/tencent-fintech-cloud-q1-2026-revenue | |
| WEB-507 | news | Tencent Q1 2026: Core Profits Bankroll AI Pivot | China Biz Insider | 2026-05 | chinabizinsider.com/tencent-isolates-ai-costs-in-q1-2026-revealing-resilient-core-bankrolling-generative-pivot | |
| WEB-508 | filing/press | Baidu Announces First Quarter 2026 Results | Baidu Inc. (PRNewswire mirror) | 2026-05-18 | prnewswire.com/news-releases/baidu-announces-first-quarter-2026-results-302774476.html | Official release; primary |
| WEB-509 | news | Baidu Q1 2026: AI Revenue Surpasses 50% as Cloud and ERNIE 5.1 Drive Growth | AlphaPilot | 2026-05 | alphapilot.tech/discover/baidu-q1-2026-ai-revenue-surpasses-50-as-cloud-and-ernie-5-1-drive-growth | |
| WEB-510 | news | Baidu Q1 2026: AI core is 52% of general business | StockTitan | 2026-05 | stocktitan.net/news/BIDU/baidu-announces-first-quarter-2026-s1pe0yett68v.html | |
| WEB-511 | news | Full Transcript: Baidu Q1 2026 Earnings Call | Benzinga | 2026-05 | benzinga.com/insights/news/26/05/52641413/full-transcript-baidu-q1-2026-earnings-call | Secondary transcript reproduction of mgmt statement on financing mix |
| WEB-512 | news | Alibaba, Tencent present a tale of two strategies for AI spending | SCMP | 2026 | scmp.com/tech/big-tech/article/3353573/alibaba-tencent-signal-ai-spending-surge-despite-earnings-pressure-china-chips-ramp | |
| WEB-513 | news | Tencent to double AI spending on 13% revenue growth as chip curbs reshape capex | Digitimes | 2026-03-19 | digitimes.com/news/a20260319VL209/tencent-revenue-growth-capex-investment.html | |
| WEB-514 | news | Tencent pledges higher AI investment in 2026 after chip curbs hit capex plans | Yahoo/Reuters | 2026 | finance.yahoo.com/news/tencent-books-13-rise-quarterly-084051132.html | |
| WEB-516 | news | Tech AI spending approaches $700 billion in 2026, cash taking big hit | CNBC | 2026-02-06 | cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html | Capex/OCF ratio, debt issuance, FCF analyst estimates |
| WEB-517 | news | Google, Microsoft, Meta, and Amazon capex spending to hit $725 billion in 2026, up 77% from last year | Tom's Hardware | 2026 | tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion | Goldman Sachs estimate |
| WEB-518 | data | Alphabet (GOOG) Capital Expenditures — Current & Historical Data | FinanceCharts | accessed 2026-07 | financecharts.com/stocks/GOOG/cash-flow/capital-expenditures | Aggregator of 10-K data; 2024 actual $52.535bn |
| WEB-519 | filing | Meta Reports Fourth Quarter and Full Year 2024 Results | Meta Platforms / SEC 8-K exhibit | 2025-01 | sec.gov/Archives/edgar/data/1326801/000132680125000014/meta-12312024xexhibit991.htm | Primary filing; FY2024 capex $39.23bn |
| WEB-520 | data | Microsoft (MSFT) Capital Expenditures — Current & Historical Data | FinanceCharts | accessed 2026-07 | financecharts.com/stocks/MSFT/cash-flow/capital-expenditures | Aggregator of 10-K data; FY2024 actual $44.477bn |
| WEB-521 | news | ByteDance Weighs Capex of as Much as $70 Billion in AI Push | Bloomberg | 2026-05-27 | bloomberg.com/news/articles/2026-05-27/bytedance-weighs-capex-of-as-much-as-70-billion-in-ai-push | Unconfirmed by company; Reuters could not independently verify |
| WEB-522 | news | ByteDance raises 2026 capex by at least 25% amid AI boom, rising memory costs, sources say | SCMP | 2026 | scmp.com/tech/article/3352906/bytedance-raises-2026-capex-least-25-amid-ai-boom-rising-memory-costs-sources-say | |
| WEB-523 | analyst | ByteDance revenue, funding & news | Sacra | updated 2026-06-15 | sacra.com/c/bytedance | Private-company equity-research estimate; D-grade |
| WEB-524 | news | ByteDance's 2025 Financial Report Revealed: Heavy AI Investment Slashes Profits | BigGo Finance | 2026 | finance.biggo.com/news/Li0bqZ0ByH9TLH69BBLF | |
| WEB-525 | news | ByteDance's Annual Profit Tumbles Over 70% on TikTok Owner's AI Investment, Source Says | Yicai Global | 2026 | yicaiglobal.com/news/tiktok-owner-bytedances-profit-plunges-over-70-last-year-on-ai-spending-push-insider-says | |
| WEB-528 | news | Is Deep-Pocketed Tencent Also Starting to Borrow Money? | 36Kr (EU) | 2026 | eu.36kr.com/en/p/3470581852099974 | First bond issuance since Apr-2021 |
| WEB-529 | news | Capital expenditure reached 79.2 billion yuan... Tencent's 2025 revenue projected at record RMB751.8bn | Futunn News | 2026 | news.futunn.com/en/post/70290793/capital-expenditure-reached-79-2-billion-yuan-with-the-new | Summarizes Tencent's official 2025 annual results release |
| WEB-530 | news | Tencent's First-Quarter Profit Jumps 21% as Capex Tops USD4.4 Billion on AI Spending | Yicai Global | 2026-05 | yicaiglobal.com/news/tencents-first-quarter-profit-jumps-21-while-ai-spending-exceeds-usd44-billion | |
| WEB-531 | news | Will Alibaba's Rising CapEx Pressure Weigh on Free Cash Flow Ahead? | press release mirror (Globe and Mail) | 2026 | theglobeandmail.com/investing/markets/stocks/BABA/pressreleases/35615834/will-alibabas-rising-capex-pressure-weigh-on-free-cash-flow-ahead | |
| WEB-532 | news | Amazon 2025 capex to reach $100bn, AWS 2024 revenue hit $100bn in 2024 | DataCenterDynamics | 2025 | datacenterdynamics.com/en/news/amazon-2025-capex-to-reach-100bn-aws-revenue-hit-100bn-in-2024 | 2024 actual capex $83bn reference |
| WEB-533 | news | Alphabet Upsizes Equity Offering to $85 Billion for AI Spending | Bloomberg | 2026-06-03 | bloomberg.com/news/articles/2026-06-03/alphabet-upsizes-equity-offering-to-85-billion-for-ai-spending | Reports on primary SEC filing event |
| WEB-534 | filing | Alphabet Inc. — SEC Form 8-K, pricing of concurrent equity offerings | Alphabet Inc. / SEC | 2026-06 | sec.gov/Archives/edgar/data/0001652044/000119312526257724/d83560dex991.htm | Primary filing |
| WEB-535 | news | Alphabet is Raising $84.75 Billion to Win the AI Wars. Should Investors Celebrate or Worry? | The Motley Fool | 2026-06-14 | fool.com/investing/2026/06/14/alphabet-is-raising-8475-billion-to-win-the-ai-war | |
| WEB-536 | news | Alphabet boosts debt sale again as total raise exceeds $30 billion, sources say | CNBC | 2026-02-10 | cnbc.com/2026/02/10/alphabet-set-to-raise-over-30-billion-in-global-debt-sale-sources.html | |
| WEB-537 | news | Google secures nearly $32bn in debt following major data center capex commitment | DataCenterDynamics | 2026-02 | datacenterdynamics.com/en/news/google-secures-nearly-32bn-in-debt-following-major-data-center-capex-commitment | ~15% of $180bn 2026 capex plan debt-financed; long-term debt quadrupled 2025 to $46.5bn |

**Confidence-grade key:** A = filed/audited · B = primary company disclosure/press covering a named earnings release or filing · C = credible third-party analyst/press · D = single-source, estimate, or unaudited/private-company figure.

**Merge note for Director:** Baidu's actual capex RMB figure is a genuine gap in this pod's data (see LIMITATIONS in the memo) — do not backfill with an estimate; Tencent's quarterly FCF figures came from a secondary aggregator with ambiguous period labeling and are used directionally only (not entered as a metrics_timeseries row for that reason). ByteDance rows are uniformly D-grade (private, unaudited) and the two 2026 capex estimates ($29.4bn vs $70bn) are presented as an unresolved range, not reconciled to one number.
