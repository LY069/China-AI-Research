# v2 Pod P3 — Data Appendix (Demand Mapping & What's Priced In)

Mirrors `database/schema.md`. New rows only; does not restate v1 pod1/pod2/pod3 `company_master.csv` rows (see those pods' `_data.md` files) except where a field is newly added (e.g., demand-split notes routed through `company_reference.csv`, which is a v2 addition).

---

## 1. `company_reference.csv` additions (v2 schema — index/classification/demand overlay)

All `demand_domestic_pct` / `demand_global_pct` figures are **estimates (D) unless marked otherwise** — see memo for basis. Where a filed split exists, confidence is noted per-row. GICS/MSCI/CSI300/HSI/ISIN fields are **out of scope for this pod** (owned by P6 — Index & Reference Data) and left blank here rather than guessed.

| company_id | isin | gics_sector | gics_industry | msci_china | msci_china_a | csi300 | hsi | hstech | approx_weight_note | mktcap_pct_market | demand_domestic_pct | demand_global_pct | ai_rev_share | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| naura | | | | | | | | | n/a — see P6 | n/a — see P6 | 90-95 | 5-10 | n/a (WFE, not AI-chip specific) | WEB-701,WEB-715 | D | Estimate; no filed geographic revenue split located. Inferred from Entity-List-restricted customer base. |
| amec | | | | | | | | | n/a — see P6 | n/a — see P6 | 85-90 | 10-15 | n/a | WEB-702,WEB-722 | D | Claimed TSMC 5nm/7nm etch-tool qualification unverified by TSMC; treat global share as upper-bound/optionality, not confirmed revenue. |
| acm | | | | | | | | | n/a — see P6 | n/a — see P6 | 95-100 | 0-5 | n/a | WEB-716 | B | Filed (ACMR 10-Q, 31-Mar-2026): "substantially all revenue" from mainland China customers. |
| smic | | | | | | | | | n/a — see P6 | n/a — see P6 | 86-89 | 11-14 | n/a | WEB-714 | C | China revenue share 85.6% (2025) → 88.9% (Q1-2026). |
| huahong | | | | | | | | | n/a — see P6 | n/a — see P6 | not verified | not verified | n/a | WEB-713 | D | No filed China/overseas split located this cycle; flagged unverified rather than estimated. |
| montage | | | | | | | | | n/a — see P6 | n/a — see P6 | 28-29 | 71-72 | high (core interconnect lines +93.8% YoY, AI-server-driven per co. reporting) | WEB-707 | C | Overseas revenue RMB3.90bn / RMB5.456bn total FY2025 = ~71.5%. Headline v2 finding for this pod. |
| cambricon | | | | | | | | | n/a — see P6 | n/a — see P6 | ~100 | ~0 | ~100 (pure-play AI NPU vendor) | Pod3 memo | C | No export channel; domestic cloud/gov/SOE customer base only. |
| moore-threads | | | | | | | | | n/a — see P6 | n/a — see P6 | 95-100 | 0-5 | ~100 | WEB-717 | C | Entity-Listed (2023); customers ByteDance/Tencent/state-backed vehicles + SOE procurement. |
| metax | | | | | | | | | n/a — see P6 | n/a — see P6 | 95-100 | 0-5 | ~100 | WEB-717 | C | Entity-Listed; receivables pattern consistent with gov't-budget-tied procurement per one report. |
| biren | | | | | | | | | n/a — see P6 | n/a — see P6 | 95-100 | 0-5 | ~100 | WEB-717 | C | Entity-Listed (2023) despite HK listing/foreign-investable status; revenue base still domestic. |
| iluvatar | | | | | | | | | n/a — see P6 | n/a — see P6 | 95-100 | 0-5 | ~100 | WEB-717 | C | Partial Entity List exposure; domestic customer base per reporting. |
| kunlunxin | | | | | | | | | n/a — see P6 | n/a — see P6 | ~100 | ~0 | ~100 | WEB-721 | C | Named customers China Mobile/Geely/China Southern Power Grid/China Merchants Bank; IPO investors reportedly required to pre-commit chip purchases. |
| cxmt | | | | | | | | | n/a — see P6 | n/a — see P6 | ~high, exact split unresolved | rising but small at real end-customer level | n/a (commodity DRAM, not AI-exclusive) | WEB-718 | D | Reported "mainland 42.79% / HK 57.21% / overseas 2.79%" split; HK line very likely re-export booking artifact, NOT genuine global end-demand — do not read as 57% global. |
| ymtc | | | | | | | | | n/a — see P6 | n/a — see P6 | presumed >90 | presumed <10 | n/a | Pod2 memo | D | On US Entity List since Dec-2022; no filed geographic split located. |
| innolight | | | | | | | | | n/a — see P6 | n/a — see P6 | ~13 | ~87 | very high (Nvidia/hyperscaler 800G-1.6T supply chain) | WEB-712 | C | Overseas revenue = 86.8% of 2024 total sales (most recent filed-adjacent figure located). |
| eoptolink | | | | | | | | | n/a — see P6 | n/a — see P6 | est. 10-20 | est. 80-90 | very high | WEB-719 | D | No exact filed % located; directional estimate from "booming overseas sales" reporting + shared ~60% Nvidia-800G-orders estimate with Innolight. |
| alibaba | | | | | | | | | n/a — see P6 | n/a — see P6 | n/a — see memo note on axis mismatch | n/a | ai_rev_share: ~30% of external cloud revenue (2026), guided >50% within ~1yr | WEB-710 | C | Alibaba is a domestic-demand-side AI consumer/cloud-seller, not a global-hardware-supply-chain name like Montage/Innolight — different axis, not directly comparable. |
| catl | | | | | | | | | n/a — see P6 | n/a — see P6 | not meaningful without segment split | not meaningful without segment split | n/a (AI-relevant slice = ESS/grid-storage only, 14.7% of total revenue per Pod 5) | Pod5 memo (WEB-006) | D | Included per brief's example list; core EV-battery business is a global-auto story unrelated to AI demand — do not compute a single domestic/global % for CATL as a whole. |

## 2. `metrics_timeseries.csv` additions

Metric IDs follow the v2 pattern `<co>_rev_growth_actual` / `_guidance` / `_consensus`, `<co>_demand_global_share`, `<co>_fwd_pe`.

| metric_id | entity | layer | metric_name | unit | period | value | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|
| naura_rev_growth_actual | naura | L1 | FY2025 revenue growth YoY | % | 2025 | 30.85 | WEB-701 | B | Filed annual report figure (RMB39.353bn total rev). |
| naura_profit_growth_actual | naura | L1 | FY2025 net profit growth YoY | % | 2025 | -1.77 | WEB-701 | B | Revenue/profit divergence — margin compression despite rev growth. |
| naura_rev_growth_consensus | naura | L1 | 2026 consensus revenue range | RMB bn | 2026 | 46.79-52.02 | WEB-701 | C | Sell-side "performance forecast" aggregation (Choyang Eternal Data via Tiger Brokers), wide range = low precision. |
| amec_rev_growth_actual | amec | L1 | FY2025 revenue growth YoY | % | 2025 | 36.6 | WEB-702 | C | $1.74bn / RMB12.38bn total. |
| amec_profit_consensus | amec | L1 | 2026E net profit consensus | RMB bn | 2026 | 3.0-3.1 | WEB-702 | C | Cross-checked across 2 sell-side notes; 2027E ~4.2bn, 2028E ~5.5bn implied. |
| acm_rev_growth_guidance | acm | L1 | FY2026 revenue guidance (reaffirmed) | $ bn | 2026 | 1.08-1.175 | WEB-716 | B | Company release; +20-30% YoY implied. |
| acm_rev_growth_actual | acm | L1 | Q1-2026 revenue growth YoY | % | 2026-Q1 | 34 | WEB-716 | B | 10-Q, $231.3m. |
| smic_rev_growth_guidance | smic | L2 | Q2-2026 revenue growth guidance QoQ | % | 2026-Q2 | 14-16 | WEB-703 | C | Roughly double the ~7% QoQ street consensus at time of guide. |
| smic_gpm_guidance | smic | L2 | Q2-2026 gross margin guidance | % | 2026-Q2 | 20-22 | WEB-703 | C | Midpoint above 20.5% consensus. |
| smic_china_rev_share | smic | L2 | China share of total revenue | % | 2026-Q1 | 88.9 | WEB-714 | C | Up from 85.6% (FY2025). |
| smic_trailing_pe | smic | L2 | Trailing P/E | x | 2026-mid | 105-140 | WEB-714,WEB-720 | D | Wide cross-source dispersion; forward P/E specifically not located. |
| tsmc_rev_growth_guidance | tsmc (external benchmark) | L2 | FY2026 revenue growth guidance | % | 2026 | >30 | WEB-704 | C | USD terms; raised from initial guide on AI demand. |
| tsmc_hpc_rev_share | tsmc (external benchmark) | L2 | HPC (AI) share of revenue | % | 2026-Q1 | 61 | WEB-704 | C | Up from 58% FY2025. |
| tsmc_fwd_pe | tsmc (external benchmark) | L2 | Forward P/E | x | 2026-mid | 23-27 | WEB-720 | C | Cross-source range. |
| amat_rev_growth_guidance | applied-materials (external benchmark) | L1 | Q3 FY2026 revenue growth guidance YoY | % | 2026-Q3 | ~23 | WEB-705 | C | Guide $8.95bn ±$0.5bn. |
| amat_china_rev_share | applied-materials (external benchmark) | L1 | China share of semi-systems+AGS revenue | % | 2026-Q2 | 24 | WEB-705 | C | Down from ~40% in prior years. |
| amat_fwd_pe | applied-materials (external benchmark) | L1 | Forward P/E | x | 2026-mid | 36-62 | WEB-720 | D | Wide cross-source dispersion. |
| lam_china_rev_share | lam-research (external benchmark) | L1 | China share of revenue | % | 2026-Q3 | 34 | WEB-706 | C | Down from ~43% in Q1 FY2026; guided <30% for 2026. |
| lam_fwd_pe | lam-research (external benchmark) | L1 | Forward P/E | x | 2026-mid | 39 | WEB-720 | C | |
| lam_wfe_market_forecast | lam-research (external benchmark) | L1 | Global WFE market size forecast | $ bn | 2026 | 140 | WEB-706 | C | Raised from prior forecast on AI-driven surge. |
| montage_rev_growth_actual | montage | L5 | FY2025 revenue growth YoY | % | 2025 | 49.9 | WEB-707 | C | RMB5.456bn total. |
| montage_profit_growth_actual | montage | L5 | FY2025 net profit growth YoY | % | 2025 | 58.4 | WEB-707 | C | RMB2.236bn. |
| montage_core_segment_growth | montage | L5 | Q1-2026 core interconnect-chip lines growth YoY | % | 2026-Q1 | 93.8 | Pod2 memo (WEB-009) | C | MRCD/MDB/Retimer/CKD/CXL MXC combined. |
| montage_overseas_rev_share | montage | L5 | Overseas share of FY2025 revenue | % | 2025 | 71.5 | WEB-707 | C | RMB3.90bn / RMB5.456bn. |
| montage_fwd_pe | montage | L5 | Forward P/E | x | 2026-mid | 47-50 | WEB-720 | C | Vs. ~42x China-semi-industry average. |
| astera_rev_growth_consensus | astera-labs (external benchmark) | L5 | 2026 consensus revenue growth YoY | % | 2026 | 54 | WEB-708 | C | Consensus revenue ~$1.5-1.54bn from 23 analysts. |
| astera_q2_growth_consensus | astera-labs (external benchmark) | L5 | Q2-2026 consensus revenue growth YoY | % | 2026-Q2 | ~88 | WEB-708 | D | Stepping to ~78% Q3 per same source. |
| astera_fwd_pe | astera-labs (external benchmark) | L5 | Forward P/E | x | 2026-mid | 120-125 | WEB-720 | C | |
| cambricon_rev_actual | cambricon | L4 | FY2025 revenue | RMB bn | 2025 | 6.5 | Pod3 memo | C | ~$900m. |
| cambricon_trailing_pe | cambricon | L4 | Trailing P/E (methodology-dependent) | x | 2026-mid | 527-4000+ | WEB-709 | D | Order-of-magnitude range across EV/adjusted-profit vs. raw-trailing methodologies — do not cite a single point figure. |
| cambricon_mktcap_peak | cambricon | L4 | Market cap peak (intraday, first STAR-listed >RMB1tn) | RMB bn | 2026-06-30 | 1000 | Pod3 memo | C | Corrected ~14% to ~RMB850bn by 2026-07-06. |
| nvidia_trailing_pe | nvidia (external benchmark) | L4 | Trailing P/E | x | 2026-mid | <60 | WEB-709 | C | |
| alibaba_cloud_rev_growth_actual | alibaba | L6 | Cloud Intelligence Group external revenue growth YoY | % | FY2026-Q4 | 38-40 | WEB-710 | C | AI products ~30% of external cloud revenue, 11 consecutive quarters of triple-digit AI-revenue growth. |
| alibaba_cloud_rev_growth_consensus | alibaba | L6 | FQ1-FY2027 Cloud Intelligence Group revenue growth consensus YoY | % | FY2027-Q1 | 45 | WEB-710 | C | Independently raised by Citi and UBS; RMB48.4bn forecast. |
| alibaba_group_rev_growth_consensus | alibaba | L6/group | FY2027 full-year group revenue consensus growth YoY | % | FY2027 | 14.3 | WEB-710 | C | Zacks consensus $166.24bn — group-level, blends e-commerce + cloud, not cloud-only. |
| alibaba_fwd_pe | alibaba | L6/group | Forward P/E | x | 2026-mid | 15.4 | WEB-720 | C | |
| aws_rev_growth_actual | amazon-aws (external benchmark) | L6 | Q1-2026 AWS revenue growth YoY | % | 2026-Q1 | 28 | WEB-711 | B | $37.6bn, beat $36.64bn street estimate; fastest growth in 15 quarters. |
| aws_backlog_growth | amazon-aws (external benchmark) | L6 | AWS order backlog growth YoY | % | 2026-Q1 | 40 | WEB-711 | C | Backlog $244bn. |
| aws_ai_rev_runrate | amazon-aws (external benchmark) | L6 | AWS AI revenue annualized run-rate | $ bn | 2026-Q1 | 15 | WEB-711 | C | |
| amazon_fwd_pe | amazon-aws (external benchmark) | L6/group | Forward P/E | x | 2026-mid | 30 | WEB-720 | C | |
| innolight_rev_growth_actual | innolight | L5 | FY2025 revenue growth YoY | % | 2025 | 60.25 | WEB-712 | C | RMB38.2bn. |
| innolight_rev_growth_actual_q1 | innolight | L5 | Q1-2026 revenue growth YoY | % | 2026-Q1 | 192 | WEB-712 | C | RMB19.5bn. |
| innolight_overseas_rev_share | innolight | L5 | Overseas share of 2024 revenue | % | 2024 | 86.8 | WEB-712 | C | Most recent filed-adjacent figure located; 2025/2026 not separately confirmed. |
| innolight_fwd_pe | innolight | L5 | Implied forward P/E (sell-side price target basis) | x | 2026 | 28 | WEB-712 | D | Single-source price-target methodology, not a market-derived multiple. |
| coherent_fwd_pe | coherent (external benchmark) | L5 | Forward P/E | x | 2026-mid | 44-60 | WEB-720 | D | Wide cross-source dispersion. |
| huahong_rev_actual | huahong | L2 | FY2025 revenue | $ m | 2025 | 2402.1 | WEB-713 | B | +19.9% YoY; GM 11.8%; net profit $54.9m; utilization 106.1%. |
| huahong_rev_guidance_q1 | huahong | L2 | Q1-2026 revenue guidance | $ m | 2026-Q1 | 650-660 | WEB-713 | B | Company guidance. |
| huahong_rev_guidance_q2 | huahong | L2 | Q2-2026 revenue guidance | $ m | 2026-Q2 | 690-700 | WEB-713 | B | GM guide 13-16%. |
| cxmt_h1_profit_guidance | cxmt | L3 | H1-2026 net profit guidance | RMB bn | 2026-H1 | 50-57 | Pod2 memo | C | |
| cxmt_hk_rev_booking_share | cxmt | L3 | "Hong Kong" share of reported revenue (booking-entity artifact, not end-demand) | % | 2025-26 | 57.21 | WEB-718 | D | Flagged explicitly as likely re-export/trading-entity booking, not genuine HK end-demand. |
| cxmt_mainland_rev_booking_share | cxmt | L3 | Mainland-China booking share of reported revenue | % | 2025-26 | 42.79 | WEB-718 | D | |

## 3. Sources (WEB-7xx range, per v2 pod P3 assignment)

| ID | Type | Title/Subject | Author/Org (as surfaced) | Date | Confidence |
|---|---|---|---|---|---|
| WEB-701 | news/aggregator | NAURA Technology 2026 revenue guidance, consensus, growth forecast | Tiger Brokers (itiger.com), Simply Wall St, MarketScreener, Quartr, Yahoo Finance | accessed 2026-07-10 | C |
| WEB-702 | news/aggregator | AMEC (中微公司) 2026 revenue/profit consensus, FY2025 actuals | Futubull/Futunn, TrendForce, Reportify, amec-inc.com | accessed 2026-07-10 | C |
| WEB-703 | news/analyst | SMIC Q2-2026 revenue/margin guidance vs. consensus | BigGo Finance, MarketScreener, TipRanks, Longbridge | 2026-05 | C |
| WEB-704 | news/analyst | TSMC 2026 revenue guidance, HPC/AI revenue share | BigGo Finance, SCMP, Bloomberg, MacroMicro, Investing.com | 2026-04 | C |
| WEB-705 | news/primary | Applied Materials FY2026 guidance, China revenue share | Alphastreet, Motley Fool (earnings transcript), TrendForce, Yahoo Finance | 2026-05 | B/C |
| WEB-706 | primary/news | Lam Research FY2026 guidance, China revenue share, WFE forecast | SEC 8-K (lrcx_exhibitx991), Yahoo Finance, BigGo Finance, Investing.com | 2026-04 to 2026-07 | B/C |
| WEB-707 | news/aggregator | Montage Technology FY2025 annual report — revenue, profit, overseas split | Minichart, Longbridge, HKEXnews filing PDF, Moomoo, stockanalysis.com | 2026-03/04 | C |
| WEB-708 | primary/news | Astera Labs Q1-2026 results, 2026 consensus revenue/EPS | Astera Labs IR release, Simply Wall St, Wedbush, Sherwood News, Futurum | 2026-Q1/Q2 | B/C |
| WEB-709 | news/analyst | Cambricon valuation, trailing P/E vs. Nvidia, market-cap correction | TechBuzzChina, CNBC, Fortune, BigGo Finance ("trillion-yuan day trip"), stockanalysis.com | 2025-08 to 2026-07 | C/D |
| WEB-710 | news/analyst | Alibaba Cloud Intelligence Group FY2027 growth forecasts (Citi/UBS), AI revenue share | TechTimes, TradingKey, Yahoo Finance/Zacks, DataCenterDynamics, Alibaba Cloud blog | 2026-07 | C |
| WEB-711 | primary/news | Amazon AWS Q1-2026 results, Q2 guidance, backlog, AI run-rate | CNBC, Betafinch, Futurum Group, TIKR | 2026-04/05 | B/C |
| WEB-712 | news/aggregator | Zhongji Innolight revenue, overseas revenue share, forward-PE price target | hellochinatech, BigGo Finance, The Wire China, Futunn | 2026 | C/D |
| WEB-713 | primary/news | Hua Hong Semiconductor FY2025 audited results, Q1/Q2-2026 guidance | TipRanks (co. release), BigGo Finance, MarketScreener, StocksFoundry | 2026-02 to 2026-05 | B/C |
| WEB-714 | news/analyst | SMIC revenue-by-geography (China vs. overseas share) | BigGo Finance, TrendForce (x2) | 2026-05 | C |
| WEB-715 | primary | NAURA 2025 annual report (searched for overseas revenue split — not located at required granularity) | cninfo.com.cn filing PDF, Eastmoney | 2026-04 | D — attempted, inconclusive |
| WEB-716 | primary | ACM Research / ACMR Q1-2026 10-Q, FY2026 guidance reaffirmation | SEC EDGAR (8-K, 10-Q), Stocktitan, Marketchameleon | 2026-05 | B |
| WEB-717 | news | Moore Threads/MetaX/Biren/Iluvatar customer base (ByteDance, state-backed investors, SOE procurement) | SCMP, TMTPost, Global Finance Magazine, byteiota | 2026 | C |
| WEB-718 | news/analyst | CXMT revenue geography breakdown, named customers, Western OEM DRAM adoption | BigGo Finance, SemiAnalysis, DSET.tw, Indoneo, Seoul Economic Daily | 2026-07 | C/D |
| WEB-719 | news | Eoptolink revenue growth, overseas sales momentum | BigGo Finance, Futunn, photoncap.net, Wikipedia | 2025-12 to 2026 | D |
| WEB-720 | aggregator | Forward P/E cross-comparison: AMAT, Lam, TSMC, SMIC(trailing), Montage, Astera Labs, Cambricon, Alibaba, Amazon, Innolight, Coherent | GuruFocus, Finbox, FinanceCharts, MacroTrends, YCharts, stockanalysis.com, valueinvesting.io | accessed 2026-07-10 | C/D (per-name dispersion noted in memo) |
| WEB-721 | news | Kunlunxin (Baidu) IPO valuation range, named customers, IPO chip-purchase pre-commitment structure | CNBC, SCMP, TrendForce, The Information, Digitimes | 2026-05 to 2026-07 | C |
| WEB-722 | news/primary (unconfirmed) | AMEC etch-tool qualification claim in TSMC 5nm/7nm lines | Wikipedia, Tom's Hardware (SMIC/AMEC CEO commentary), amec-inc.com global-network page | 2026 | D — claim not confirmed by TSMC |

**Note on source-quality convention:** per v2 hardening rules, every ID above that resolves to an "aggregator" or AI-generated search-summary product (as opposed to a named, dated, checkable primary document) is capped at C, and several are graded D where the underlying figure showed material cross-source dispersion or internal inconsistency (see memo LIMITATIONS for the two aggregator figures excluded outright as likely errors).
