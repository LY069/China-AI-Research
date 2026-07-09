# Pod 6 — Database-Ready Additions (Policy, Geopolitics & Capital Markets)

These are proposed additions/updates mirroring `database/schema.md`. Master CSVs are **not** edited directly — the Research Director / DB owner should reconcile and merge. Where a row updates an existing `company_id`/`policy_id`, the full row is given so it can replace the existing one; changed fields are noted.

---

## 1. `company_master.csv` — updated rows

```csv
company_id,name_en,name_cn,layers,segment,ownership,listing_status,exchange_ticker,hq,founded,entity_list,investable_foreign,mkt_cap_usd_bn,fwd_pe,key_products,china_role,global_peer,source_id,confidence,notes
moore-threads,Moore Threads,摩尔线程,L4,"GPGPU",private,listed,SSE:688795,Beijing,2020,yes,restricted,7.5,n.m. (pre-profit),"MTT full-featured GPUs (graphics+compute)",challenger,Nvidia,WEB-643,B,"UPDATE from IPO-filed: listed STAR Market 2025-12-05; raised RMB8bn ($1.13bn); post-issue mkt cap ~RMB54bn (~$7.5bn); +468% day-1 to RMB650; IPO price RMB114.28/sh, most expensive 2025 A-share IPO"
metax,MetaX,沐曦,L4,"GPGPU",private,listed,SSE:688000-series (ticker TBD at filing),Shanghai,2020,yes,restricted,5.2,n.m. (pre-profit; net loss RMB345.5m pre-IPO),"Xisi/Xiyun GPU series",challenger,Nvidia,WEB-646,B,"UPDATE from IPO-filed: STAR Market listing 2026; offer price RMB104.66/sh raised RMB4.2bn ($596m); implied mkt cap RMB37.7bn (~$5.2bn) vs RMB21.07bn pre-IPO (Mar-2026); +693% day-1"
biren,Biren Technology,壁仞科技,L4,"GPGPU",private,listed,HKEX:6844,Shanghai,2019,yes,restricted,6.0,n.m. (pre-profit),"BR-series training GPUs",challenger,Nvidia,WEB-641,B,"UPDATE from IPO-filed: listed HKEX 2026-01-02; raised HK$5.58bn (~$715m) at HK$19.60/sh; offer-price mkt cap HK$46.9bn (~$6.0bn); +75% day-1 close; first of China's 'four little dragons' GPU IPOs to list"
iluvatar,Iluvatar CoreX,天数智芯,L4,"GPGPU",private,listed,HKEX:not yet confirmed ticker,Shanghai,2015,partial,restricted,25.6,n.m. (pre-profit),"Tiangai/Zhikai GPUs",challenger,Nvidia,WEB-642,C,"UPDATE from IPO-filed: listed HKEX 2026-01-08; raised ~HK$3.7bn (~$475m); mkt cap ~$25.6bn as of 2026-06-24 (+428% since IPO); seeking ~$850m follow-on raise (2026-07); reported ByteDance supply talks for >=50k inference chips"
kunlunxin,Kunlunxin (Baidu),昆仑芯,L4,"AI accelerators",SOE-linked,IPO-filed,"private (HK confidential filing + STAR guidance, not yet listed)",Beijing,2021,partial,restricted,50.0,n.m.,"Kunlun P-series AI chips",national-champion,Nvidia,WEB-651,D,"UPDATE: confidential HKEX filing 2026-01-01, STAR Market guidance started 2026-05-07; target valuation escalated from $14.7bn (May-2026) to ~$50bn (Jun-2026); Baidu holds 57.67% stake; unusual investor terms reportedly requiring chip-purchase commitments 3-7x investment"
zhipu,Zhipu AI (Z.ai),智谱,L7,"foundation models",private,listed,HKEX:not yet confirmed ticker,Beijing,2019,no,restricted,75.0,n.m. (pre-profit),"GLM family; Z.ai",national-champion,"OpenAI / Anthropic",WEB-649,B,"UPDATE from IPO-approved: listed HKEX 2026-01-08 at HK$116.20/sh; day-1 mkt cap HK$57.9bn (~$7.4bn); surged to HK$585.8bn (~$75bn) by Jun-2026; STAR Market 5th-standard secondary-listing candidate; beat OpenAI to IPO"
minimax,MiniMax,稀宇科技,L7,"foundation models",private,listed,HKEX:not yet confirmed ticker,Shanghai,2021,no,restricted,20.0,n.m. (pre-profit),"MiniMax M-series (open-weight)",national-champion,"OpenAI / Anthropic",WEB-649,B,"UPDATE from IPO-approved: listed HKEX 2026-01-09 at HK$165/sh; raised HK$4.8bn (~$620m); day-1 close HK$345 (+109%); day-1 mkt cap HK$106.7bn (~$13.7bn); mkt cap HK$159.3bn (~$20bn) by Jun-2026 -- lagged Zhipu's re-rating"
montage,Montage Technology,澜起科技,L5,"memory-interface chips; PCIe/optical/Ethernet",private,listed,SSE:688008 / HKEX:6809,Shanghai,2004,no,yes,,,"#1 global memory-interface chips (~1/3 share); MRCD/MDB; CXL",incumbent,"Rambus / Renesas",WEB-654,B,"UPDATE: H-share listing confirmed HKEX:6809 (2026-02-08/09); raised ~$902m; H priced at 41% discount to A, then FLIPPED to ~14% H-share premium by Apr-2026 -- reversal of typical A>H premium pattern"
cxmt,ChangXin Memory Technologies,长鑫存储,L3,"DRAM (→HBM path)",state,IPO-filed,"private (STAR Market review cleared ~2026-05-27, not yet listed)",Hefei,2016,yes,restricted,43.0,n.m.,"DDR/LPDDR DRAM; building toward HBM",national-champion,"Micron / SK hynix / Samsung",WEB-655,C,"UPDATE: STAR Market review cleared ~27-May-2026; targeting RMB29.5bn (~$4.3bn) raise; pre-IPO valuation RMB150bn; post-IPO estimates disperse widely from RMB295bn (~$43bn, conservative) to RMB1-3tn bull case (20x P/E) -- high end is D-confidence"
ymtc,Yangtze Memory Technologies,长江存储,L3,"NAND (→DRAM/TSV)",state,IPO-filed,"private (IPO-counseling filing accepted 2026-05-19, Hubei CSRC)",Wuhan,2016,yes,restricted,150.0,n.m.,"3D NAND; Phase-3 pivot ~50% DRAM + TSV packaging",national-champion,"Samsung / SK hynix / Micron / Kioxia",WEB-658,D,"UPDATE: IPO-counseling filing accepted 2026-05-19 (sponsors CITIC Securities, CSC Financial); targeting STAR Market; valuation estimates disperse RMB500bn-3tn (~$70-420bn); formal application expected mid/late-2026"
```

## 2. `metrics_timeseries.csv` — new/updated rows

```csv
metric_id,entity,layer,metric_name,unit,period,value,source_id,confidence,notes
china_ai_diffusion_2027_fyp15,China,macro,15th FYP AI economic penetration target,%,2027,70,WEB-601,C,"Confirms/aligns with existing china_ai_diffusion_target_2027 row"
china_ai_diffusion_2030_fyp15,China,macro,15th FYP AI economic penetration target,%,2030,90,WEB-601,C,"Confirms/aligns with existing china_ai_diffusion_target_2030 row"
china_core_ai_industry_size,China,macro,Core AI industry size,usd-bn-equiv,2025,168,WEB-601,D,"~RMB1.2tn (2025); FX approx; target >RMB10tn by 2030"
dc_grid_295_domestic_share,China,L6,Domestic-technology mandate for national DC grid,%,2026,80,WEB-605,B,"NDRC-led plan; grid completion targeted 2028"
big_fund_phase1_rmb,China,L1|L2|L3,Big Fund Phase I registered capital,rmb-bn,2014,138.7,WEB-603,C,
big_fund_phase2_rmb,China,L1|L2|L3,Big Fund Phase II registered capital,rmb-bn,2019,204,WEB-603,C,
big_fund_phase3_rmb,China,L1|L2|L3,Big Fund Phase III registered capital,rmb-bn,2024,344,WEB-604,C,"~$47.5bn at 2024 FX; established 2024-05-24"
hbm_control_threshold,US-BIS,L3,HBM export-control bandwidth-density threshold,gb-per-mm2,2024,2,WEB-615,B,"All HBM above this density restricted country-wide to China, effective Dec-2024"
h200_tariff_rate,US-BIS,L4,Tariff on approved H200/MI325X exports to China,%,2026,25,WEB-624,B,"Case-by-case license review from presumption-of-denial, effective 2026-01-15/16"
rare_earth_suspension_window,China,macro,Rare-earth/gallium/germanium/antimony export-control suspension (vs US),months,2025-2026,12,WEB-622,C,"Suspension 2025-11-07 to ~2026-11-10/27; reversible, not a repeal"
equity_pivot_date,China,K,Equity-market policy pivot date ('slow bull'),date-flag,2024-09-24,1,WEB-620,C,"PBOC/CSRC/NFRA stimulus + governance package"
hstech_fwd_pe,HSTECH-index,K,Hong Kong Tech Index forward P/E (China AI-basket proxy),x,2026-Q2,19.9,WEB-660,C,"5-yr average ~22.5x; basket proxy incl. AI/tech-adjacent names"
ah_premium_montage,montage,K,H-share premium (or discount) vs A-share,%,2026-04,14,WEB-654,C,"POSITIVE = H-premium (reversal of typical A>H pattern); at IPO (2026-02) H priced at 41% discount to A"
openrouter_china_share_update,China,L7,Chinese-model share of OpenRouter tokens (updated),%,2026-Q1-Q2,55,WEB-663,C,"Range 51-61% Feb-Apr 2026; supersedes/updates existing openrouter_china_share row (33%, dated 2026, source REF-BW-01) -- flag for reconciliation, up from <2% in late 2024"
china_ai_overseas_presence,China,W,Chinese AI firms with commercial presence abroad,countries,2026-Q1,170,WEB-664,D,"Per Digital Silk Road / BRI-adjacent reporting; single-source estimate"
zhipu_mktcap,zhipu,L7,Market capitalization,hkd-bn,2026-06,585.8,WEB-649,B,"~$75bn; up from HK$57.9bn day-1 (2026-01-08)"
minimax_mktcap,minimax,L7,Market capitalization,hkd-bn,2026-06,159.3,WEB-649,B,"~$20bn; up from HK$106.7bn day-1 (2026-01-09)"
biren_mktcap_offer,biren,L4,Market capitalization at IPO offer price,hkd-bn,2026-01,46.9,WEB-641,B,
iluvatar_mktcap,iluvatar,L4,Market capitalization,usd-bn,2026-06,25.6,WEB-642,C,"+428% since 2026-01-08 IPO"
moore_threads_mktcap,moore-threads,L4,Market capitalization post-issue,rmb-bn,2025-12,54,WEB-643,B,
kunlunxin_target_valuation,kunlunxin,L4,Target IPO valuation,usd-bn,2026-06,50,WEB-651,D,"Escalated from $14.7bn ask in May-2026; not yet listed"
cxmt_ipo_target_raise,cxmt,L3,Targeted STAR Market IPO raise,usd-bn,2026,4.3,WEB-655,C,"RMB29.5bn; review cleared ~2026-05-27"
```

## 3. `policy_funding_tracker.csv` — new rows

```csv
policy_id,name,level,type,amount_usd_bn,currency_note,date_announced,horizon,target_layers,summary,source_id,confidence
big-fund-1,National IC Industry Investment Fund Phase I,national,fund,22,RMB138.7bn (2014),2014,,L1|L2|L3,"First phase of the Big Fund; backed early fab/equipment/memory investment",WEB-603,C
big-fund-2,National IC Industry Investment Fund Phase II,national,fund,29,RMB204bn (2019),2019,,L1|L2|L3,"Second phase; broadened scope across equipment, materials, memory",WEB-603,C
big-fund-3,National IC Industry Investment Fund Phase III,national,fund,47.5,RMB344bn (2024),2024-05-24,,L1|L2|L3,"Third phase, largest to date; six state banks contributed RMB114bn (33.14% stake)",WEB-604,C
ai-plus-2025,"Artificial Intelligence+ Initiative",national,plan,,,2025-08-26,2025-2035,all,"State Council Opinion [2025] No.11; targets >70% penetration of new-gen smart terminals/agents by 2027, >90% by 2030, full 'intelligent economy' by 2035",WEB-610,B
soe-ai-mandate-2027,SOE AI-Adoption Mandate,national,mandate,,,2025,2027,all,"Mandated AI integration across state-owned enterprises; ~70% AI penetration target across key industrial sectors by 2027",WEB-609,D
provincial-compute-vouchers,Provincial/Municipal Computing-Power Vouchers,provincial,subsidy,,"Shanghai ~RMB600m + RMB100m (2025-26)",2024-2026,,L6|L7,"Beijing, Shanghai, Shenzhen, Henan, Shandong, Chengdu, Ningbo issue vouchers covering up to 80% of AI compute-rental costs for SMEs, plus data/LLM-training subsidies",WEB-611,C
star-5th-standard-2026,STAR Market Fifth Listing Standard Extension,national,standard,,,2026-06-17,,L4|L7,"Extends pre-profit IPO access to large-model developers and quantum-tech firms; requires ~$591m market cap and government approval of core technology",WEB-631,C
us-hbm-fdpr-controls-2024,HBM & FDPR/SME Export Control Expansion,national,mandate,,,2024-12-02,,L3|L1,"US BIS: first-ever country-wide HBM controls (>2GB/mm2 density); new Footnote-5 and SME Foreign Direct Product Rules extending US jurisdiction to non-US-made SME destined for China; ~140 entities added",WEB-616,B
us-h200-caseby-case-2026,H200/MI325X Case-by-Case Export Review,national,mandate,,,2026-01-15,,L4,"US BIS shifts H200/MI325X China export license review from presumption-of-denial to case-by-case, 25% tariff, subject to security conditions",WEB-624,B
china-rare-earth-suspension-2025,Rare-Earth/Gallium/Germanium Export-Control Suspension,national,mandate,,,2025-11-07,2026-11 (1yr),macro,"China suspends (not repeals) export controls on rare earths, gallium, germanium, antimony, superhard materials toward the US as part of the Busan trade truce",WEB-622,C
us-oisp-outbound-investment,US Outbound Investment Security Program,national,mandate,,,2025-01-02,ongoing,all,"Treasury final rule restricting/screening US investment into Chinese AI, semiconductor, and quantum entities; broadened by Dec-2025 NDAA/COINS Act to add sectors (HPC, supercomputing, hypersonics) and countries",WEB-635,A
```

## 4. Sources (WEB-xxx, this pod)

See the numbered source list (WEB-601 through WEB-664) in `pod6_policy_geopolitics_capital.md` §10 for full title/author/date/URL/confidence detail — reproduced here in `sources.csv` shape for direct import:

```csv
source_id,type,title,author_org,date,url_or_locator,notes
WEB-601,news,China's next five-year bet on AI,Merics,2026,merics.org/en/comment/chinas-next-five-year-bet-ai-self-reliance-diffusion-and-lot-hype,"15th FYP AI framing"
WEB-603,news,China Integrated Circuit Industry Investment Fund,Wikipedia,2026,en.wikipedia.org/wiki/China_Integrated_Circuit_Industry_Investment_Fund,"Big Fund phase sizes"
WEB-604,news,China Piles $47.5 Billion Into Big Fund III,Caixin Global,2024-05-28,caixinglobal.com/2024-05-28/china-piles-475-billion-into-big-fund-iii-to-boost-chip-development-102200633.html,"Big Fund III size"
WEB-605,news,China Plans $295 Billion Investment to Build Nationwide AI Data Centers,Bloomberg,2026-06-09,bloomberg.com/news/articles/2026-06-09/china-prepares-295-billion-plan-to-fund-nationwide-ai-buildout,"DC grid plan"
WEB-607,news,China Launches $138B State-Backed Fund,The AI Insider,2025-03-27,theaiinsider.tech/2025/03/27/china-launches-138b-state-backed-fund-to-accelerate-ai-and-robotics-innovation/,"AI+robotics fund"
WEB-609,news,China AI Data Center Grid Locks Out Nvidia,TechTimes,2026-06-22,techtimes.com/articles/318868/20260622/china-ai-data-center-grid-locks-out-nvidia-295-billion-domestic-chip-mandate.htm,"SOE mandate figure"
WEB-610,gov,China AI+ Opinions 2025,CSET / State Council,2025-08-26,cset.georgetown.edu/publication/china-ai-plus-opinions-2025/,"AI+ Initiative primary translation"
WEB-611,news,From Vouchers to Visas,FPRI,2025-09,fpri.org/article/2025/09/from-vouchers-to-visas-chinas-innovative-plan-for-ai-dominance/,"Provincial compute vouchers"
WEB-614,gov,U.S. Export Controls and China: Advanced Semiconductors,Congressional Research Service,2025-08-22,congress.gov/crs-product/R48642,"Master export-control timeline"
WEB-615,news,What is HBM and why is the US trying to block China's access,CNN Business,2024-12-08,cnn.com/2024/12/08/tech/us-china-hbm-chips-hnk-intl,"HBM controls detail"
WEB-616,analyst,Commerce Strengthens Export Controls,Covington & Burling,2024-12,cov.com/en/news-and-insights/insights/2024/12/us-department-of-commerce-strengthens-export-controls-on-advanced-computing-and-semiconductor-manufacturing-items,"FDPR/SME/HBM Dec-2024 rule"
WEB-618,gov,Additions and Revisions to the Entity List,Federal Register,2025-09-16,federalregister.gov/documents/2025/09/16/2025-17893/additions-and-revisions-to-the-entity-list,"Sept-2025 Entity List additions"
WEB-620,news,Xi Is Overcoming His Dislike of the Stock Market,Foreign Policy,2024-10-29,foreignpolicy.com/2024/10/29/xi-china-stock-market-rally-slow-bull-stimulus/,"Slow bull pivot"
WEB-622,analyst,China Hits Pause on Rare-Earth Export Controls,Clark Hill,2025-11,clarkhill.com/news-events/news/china-hits-pause-on-rare-earth-export-controls-and-what-it-means-for-supply-chains/,"Rare earth suspension"
WEB-624,analyst,BIS Export Policy Shift,Introl,2026,introl.com/blog/bis-export-policy-h200-mi325x-china-case-by-case-2026,"H200 case-by-case rule"
WEB-630,analyst,Xi's Taiwan scorecard: why 2026 is not the year,ASPI Strategist,2026,aspistrategist.org.au/xis-taiwan-scorecard-why-2026-is-not-the-year/,"Taiwan risk assessment"
WEB-631,news,China Expands Pre-Profit IPO Access to AI and Quantum,TechTimes,2026-06-18,techtimes.com/articles/318621/20260618/china-expands-pre-profit-ipo-access-ai-quantum-star-market-rules-now-live.htm,"STAR Market 5th standard"
WEB-635,gov,Outbound Investment Security Program,US Treasury,2025,home.treasury.gov/policy-issues/international/outbound-investment-program,"OISP primary source"
WEB-637,analyst,Trump Signs COINS Act,Baker McKenzie,2025-12,sanctionsnews.bakermckenzie.com/president-trump-signs-coins-act-codifying-and-expanding-outbound-investment-regulations/,"NDAA FY26 OISP expansion"
WEB-639,news,China mulls limiting foreign access to advanced AI models,Fortune / Reuters,2026-07-08,fortune.com/2026/07/08/china-mulls-limiting-foreign-access-advanced-ai-models/,"Single-source/developing; D confidence"
WEB-641,news,Biren IPO debut coverage,RTHK/SCMP,2026-01-02,news.rthk.hk/rthk/en/component/k2/1838353-20260102.htm,"Biren mkt cap and pricing"
WEB-643,news,Moore Threads files IPO raises $1.1 billion,Jon Peddie Research,2025-2026,jonpeddie.com/news/moore-threads-files-ipo-raises-1-1-billion/,"Moore Threads IPO size"
WEB-646,news,MetaX set for Shanghai debut,SCMP,2026,scmp.com/tech/tech-trends/article/3336611/metax-set-shanghai-debut-amid-market-frenzy-over-ai-chip-stocks-nvidia-uncertainty,"MetaX IPO pricing/valuation"
WEB-649,news,Zhipu vs MiniMax valuation gap,SCMP,2026-06,scmp.com/tech/big-tech/article/3356390/minimax-once-led-zhipu-hong-kongs-ai-stock-race-how-tables-have-turned,"Zhipu/MiniMax mkt cap evolution"
WEB-651,news,Baidu shares jump as Kunlunxin targets $50 billion HK IPO,CNBC,2026-06-29,cnbc.com/2026/06/29/baidu-kunlunxin-hong-kong-ipo-50-billion-ai-chips.html,"Kunlunxin valuation escalation"
WEB-654,analyst,China A-H share premium narrows,IndexBox / Smartkarma,2026-04,indexbox.io/blog/h-a-share-premium-narrows-as-global-investors-rethink-chinese-tech-stocks/,"Montage AH premium reversal"
WEB-655,news,Inside CXMT's US$4.3b IPO,SCMP,2026,scmp.com/tech/big-tech/article/3359168/inside-cxmts-us43b-ipo-soaring-profits-meet-us-export-threat-and-high-stakes-hbm-race,"CXMT IPO detail"
WEB-658,news,Chinese Chipmaker YMTC Moves Toward IPO,Caixin Global,2026-05-20,caixinglobal.com/2026-05-20/tech-brief-may-20-chinese-chipmaker-ymtc-moves-toward-ipo-102445848.html,"YMTC filing detail"
WEB-660,analyst,New era for China technology - Investment Outlook 2026,UBP,2026,ubp.com/en/news-insights/newsroom/new-era-for-chinese-technology-investment-outlook-2026,"HSTECH fwd P/E"
WEB-663,news,Chinese AI Models Hit 61% Market Share On OpenRouter,Dataconomy,2026-02,dataconomy.com/2026/02/25/chinese-ai-models-hit-61-market-share-on-openrouter/,"Updated OpenRouter share"
WEB-664,analyst,AI cooperation under the shadow of China's Digital Silk Road,DFRLab,2026-02,dfrlab.org/2026/02/25/china-digital-silk-road-report/,"BRI/Digital Silk Road diffusion"
```

**Note:** the full WEB-601–WEB-664 ID range (including entries not reproduced in the CSV block above, e.g. WEB-602/606/608/612/613/617/619/621/623/625-629/632-634/636/638/640/642/644-645/647-648/650/652-653/656-657/659/661-662) is documented with title/author/date/URL/confidence in the memo's numbered source list (§10 of `pod6_policy_geopolitics_capital.md`) and should be merged into `sources.csv` alongside the rows above.
