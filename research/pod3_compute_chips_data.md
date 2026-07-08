# Pod 3 — Compute & AI Chips — Database-Ready Additions

Mirrors `/home/user/China-AI-Research/database/schema.md`. Rows below are additions/updates to be merged into the master CSVs by the Research Director; master CSVs were NOT edited directly per convention.

---

## 1. `company_master.csv` — updates & additions

Existing rows (huawei, cambricon, moore-threads, metax, biren, iluvatar, kunlunxin, alibaba, bytedance, baidu) already exist in the seed CSV; below are **field updates** (mkt_cap_usd_bn, fwd_pe, listing/exchange refresh, notes) plus no wholly-new company rows (seed already covers the Pod 3 universe).

| company_id | name_en | name_cn | layers | segment | ownership | listing_status | exchange_ticker | hq | founded | entity_list | investable_foreign | mkt_cap_usd_bn | fwd_pe | key_products | china_role | global_peer | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| huawei | Huawei / HiSilicon | 华为/海思 | L4\|L5\|L6 | Ascend AI chips; optical interconnect; Huawei Cloud; CANN SW | private | private | private | Shenzhen | 1987 | yes | no | n.a. (private) | n.a. | Ascend 910C/950PR/950DT; CloudMatrix 384; Atlas 950 SuperPoD; CANN/MindSpore | national-champion | Nvidia + AMD | WEB-002,WEB-003,WEB-004,WEB-038 | C | Bernstein est. ~60% domestic AI-chip share by end-2026 (D-grade sub-estimate); openPangu 2.0 (2026-06-12) first reported frontier model trained fully on Ascend |
| cambricon | Cambricon Technologies | 寒武纪 | L4 | AI accelerators (NPU) — Siyuan/MLU | private | listed | SSE:688256 | Beijing | 2016 | yes | restricted | ~120 (2026-07-06) | n.a. — trading at extreme premium post risk-warning correction | Siyuan MLU290/370/590/690 | national-champion | Nvidia | WEB-005,WEB-006,WEB-040,WEB-041 | C | Briefly crossed RMB1tn mkt cap 2026-06-30 (first STAR co. to do so), corrected ~14% to RMB862bn after co. risk warning; FY2025 rev ~RMB6.5bn, net profit ~RMB2.06bn |
| moore-threads | Moore Threads | 摩尔线程 | L4 | GPGPU (MTT series) | private | listed | SSE:688795 | Beijing | 2020 | yes | restricted | ~44 (2026-07-08) | n.a. | MTT S4000/S5000; Huashan (announced) | challenger | Nvidia | WEB-007,WEB-008,WEB-042 | C | STAR IPO 2025-12-05, raised ~RMB8bn ($1.1bn); Day-1 +468.78%; cut off from TSMC post-2023 Entity List, dependent on SMIC |
| metax | MetaX | 沐曦 | L4 | GPGPU (C-series/Xisi/Xiyun) | private | listed | SSE (STAR) | Shanghai | 2020 | yes | restricted | ~42.6 (2025-12-17, Day-1 close) | n.a. | C-series GPU | challenger | Nvidia | WEB-009,WEB-010 | C | STAR IPO 2025-12-17, raised RMB4.2bn ($596m) at RMB104.66/sh; FY2025 rev RMB1.6bn (+121% YoY); pursuing HK H-share listing as of mid-2026 |
| biren | Biren Technology | 壁仞科技 | L4 | GPGPU (BR-series) | private | listed | HKEX:9668 | Shanghai | 2019 | yes (2023) | yes (HK-listed) | ~10.6 (2026-01-02, Day-1 close) | n.a. | BR100 (chiplet, 7nm TSMC, 64GB HBM2e)/BR104 | challenger | Nvidia | WEB-011,WEB-012,WEB-044 | C | First mainland GPU designer to list in HK; IPO offer HK$46.9bn ($6bn) mkt cap, Day-1 +75.8%; pre-IPO valuation RMB14bn (June 2025) |
| iluvatar | Iluvatar CoreX | 天数智芯 | L4 | GPGPU (Tiangai/Zhikai, 7nm) | private | listed | HKEX:9903 | Shanghai | 2015 | partial | yes (HK-listed) | n.a. (raised HK$3.68bn IPO; seeking add'l ~$850m as of 2026-07-08) | n.a. | Tiangai/Zhikai GPUs | challenger | Nvidia | WEB-013,WEB-014 | C | HK IPO 2026-01-08 at HK$144.60/sh; stock +428% since IPO; follow-on raise priced HK$476-498.40/sh; in talks to supply ByteDance 50k+ inference chips (mid-2026) |
| kunlunxin | Kunlunxin (Baidu) | 昆仑芯 | L4 | AI accelerators (Kunlun P-series) | SOE-linked | IPO-filed (dual STAR+HKEX) | private (pre-listing) | Beijing | 2021 | partial | restricted (pending listing) | target ~50 (reported HK IPO valuation, 2026-06-29) | n.a. | Kunlun P800 | national-champion | Nvidia | WEB-017,WEB-018,WEB-019 | C | Confidential HKEX filing 2026-01-01; STAR listing guidance launched 2026-05-07; valuation target rose from ~$14.7bn to ~$50bn; P800 took 70-100% share in select gov/SOE bid segments (China Mobile, Geely, China Southern Power Grid, China Merchants Bank) |
| alibaba | Alibaba Group | 阿里巴巴 | L4\|L6\|L7 | T-Head (PingTouGe) Zhenwu chips; Alibaba Cloud; Qwen | private | listed | HKEX:9988 / NYSE:BABA | Hangzhou | 1999 | no | yes | n.a. (group-level, chip unit not separately valued) | n.a. | Zhenwu ASIC | national-champion | Amazon (AWS) + Google | WEB-036 | C | Chip unit not separately disclosed; TSMC-fabless where accessible |
| bytedance | ByteDance | 字节跳动 | L4\|L7\|L8 | in-house inference ASIC (Groq-inspired, Arm/RISC-V candidate); Doubao | private | private | private | Beijing | 2012 | no | no | n.a. (private) | n.a. | In-house ASIC (concept/design stage); Doubao LLM | national-champion | Broadcom (custom-ASIC model) + OpenAI | WEB-033,WEB-034,WEB-035 | C/D | Partnering w/ InnoStar Semiconductor on memory to reduce HBM dependence; targeting 100k+ in-house units 2026; reported parallel 2026 orders: ~$5.6-5.7bn Huawei Ascend + ~$14bn Nvidia (H200-class, conflicting w/ "Nvidia zero share" reporting — flagged uncertainty) |

---

## 2. `metrics_timeseries.csv` — additions

| metric_id | entity | layer | metric_name | unit | period | value | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|
| china_nvidia_dc_share | China | L4 | Nvidia data-center accelerator share in China | % | 2023 (pre-controls) | 95 | WEB-038 | C | Baseline pre-Entity-List-escalation share |
| china_nvidia_dc_share | China | L4 | Nvidia data-center accelerator share in China | % | 2025-H2 | <60 | WEB-038 | C | Domestic chipmakers reported delivering 1.65m AI GPUs domestically in same period |
| china_nvidia_dc_share | China | L4 | Nvidia data-center accelerator share in China | % | 2026 | ~0 (per CEO commentary) | WEB-039 | B | Jensen Huang public statement; conflicts with reported parallel $14bn ByteDance 2026 Nvidia order (WEB-035) — treat as contested, not reconciled |
| cambricon_mkt_cap | Cambricon | L4 | Market capitalization | $bn | 2026-06-30 (peak) | ~145 (RMB ~1,000bn) | WEB-040 | C | First STAR-listed co. to cross RMB1tn; corrected ~14% within 2 trading days |
| cambricon_mkt_cap | Cambricon | L4 | Market capitalization | $bn | 2026-07-06 | ~120 (RMB ~850bn) | WEB-041 | B | Exchange-derived market data |
| cambricon_revenue | Cambricon | L4 | Annual revenue | $bn | FY2025 | ~0.90 (RMB 6.5bn) | WEB-005,WEB-006 | C | Net profit ~RMB2.06bn same period |
| moore_threads_mkt_cap | Moore Threads | L4 | Market capitalization | $bn | 2026-07-08 | ~44 (RMB 314.45bn) | WEB-042 | B | Exchange-derived market data |
| moore_threads_ipo_raise | Moore Threads | L4 | IPO proceeds | $bn | 2025-12-05 | ~1.1 (RMB 8bn) | WEB-007 | B | STAR Market; approved 88 days after application |
| metax_revenue | MetaX | L4 | Annual revenue | $bn | FY2025 | 0.23 (RMB 1.6bn) | WEB-010 | C | +121% YoY; sold 33,600 C-series units (+147% YoY) |
| metax_ipo_mktcap | MetaX | L4 | Implied market cap, Day-1 close | $bn | 2025-12-17 | ~42.6 | WEB-009 | C | Day-1 close +693% vs. offer price |
| biren_ipo_mktcap | Biren | L4 | Implied market cap, Day-1 close | $bn | 2026-01-02 | ~10.6 (HK$82.6bn) | WEB-012 | C | Institutional bids ~26x oversubscribed; retail ~2,348x |
| iluvatar_ipo_raise | Iluvatar CoreX | L4 | IPO proceeds | $bn | 2026-01-08 | ~0.4725 (HK$3.68bn) | WEB-013,WEB-014 | B | Follow-on raise ~$850m sought as of 2026-07-08 after +428% rally |
| kunlunxin_ipo_target_valuation | Kunlunxin | L4 | Targeted IPO valuation (HK) | $bn | 2026-06-29 (reported) | ~50 | WEB-018 | C | Up from earlier ~$14.7bn (HK$100bn) target reported 2026-05-08 (WEB-017) |
| china_advanced_node_capacity | China | L2/L4-adjacent | 7nm/5nm-class wafer capacity | wafers/month (000s) | 2025 (current) | ~20-50 | WEB-024 | D | Range reflects source disagreement; SMIC alone approaching ~50k wpm advanced-node in 2025 per some reporting |
| china_advanced_node_capacity_target | China | L2/L4-adjacent | 7nm/5nm-class wafer capacity target | wafers/month (000s) | end-2027 (target) | ~150-160 | WEB-023,WEB-024 | C | "5x in two years" goal, SMIC + Hua Hong jointly |
| china_advanced_node_capacity_target | China | L2/L4-adjacent | 7nm/5nm-class wafer capacity target | wafers/month (000s) | 2030 (target) | ~500 | WEB-023 | D | Longer-horizon extrapolation |
| china_ai_dc_mandate_size | China | macro/L4 | National AI-computing-grid draft plan size | $bn | 2026 (drafted) | ~295 (up to ~740 incl. power) | WEB-020,WEB-022 | C | Targets 80% domestic-chip content by 2028 |
| ascend_910c_vs_h100_inference | Huawei/Nvidia | L4 | Ascend 910C inference throughput vs. H100 | % of H100 | 2025-2026 | ~60 | WEB-029 | C | Per DeepSeek internal benchmarking, as reported |
| cloudmatrix384_bf16_pflops | Huawei | L4 | CloudMatrix 384 supernode compute | PFLOPS (BF16) | 2025-2026 | ~300 | WEB-001 | C | vs. Nvidia GB200 NVL72 ~180 PFLOPS |

---

## 3. `chip_catalog.csv` — additions & updates

| chip_id | vendor | type | node_nm | fab | flops_notes | memory | interconnect | release_status | global_analog | source_id | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ascend-910c | huawei | NPU | 7 | smic | ~800 TFLOPS FP16 (~80% of H100 spec); ~60% of H100 inference throughput per DeepSeek benchmark | HBM (indigenous, unspecified gen) | CloudMatrix 384 (UB optical, all-to-all) | shipping | H100/H200-class (Jensen Huang: "probably comparable to H200") | WEB-028,WEB-029 | C |
| ascend-950pr | huawei | NPU | <7 | smic | Next-gen; monolithic compute die; targeted 1Q26 shipment | HiBL 1.0 (self-developed HBM) | Huawei optical scale-up | shipping (1Q26 per roadmap) | H100/H200-class (target) | WEB-002,WEB-004 | C |
| ascend-950dt | huawei | NPU | <7 | smic | Training+decode variant; Atlas 950 SuperPoD = 8,192x this chip, 8 FP8 ExaFLOPS / 16 FP4 ExaFLOPS | 144GB HiZQ 2.0 HBM, 4.0 TB/s bandwidth; Dual-Die UMA | Atlas 950 SuperPoD (20x CloudMatrix 384 unit count) | announced (targeted Aug 2026) | B200/next-gen-class (claimed) | WEB-002,WEB-003 | C |
| cloudmatrix-384 | huawei | supernode/system | 7 (910C-based) | smic | ~300 PFLOPS BF16 system-level; 384x Ascend 910C + 192x Kunpeng CPU | 48TB pooled HBM | Unified Bus (UB), fully non-blocking all-to-all optical | shipping (since Apr 2025, Inner Mongolia Ulanqab DC) | Exceeds Nvidia GB200 NVL72 (~180 PFLOPS) per vendor claim | WEB-001 | C |
| cambricon-mlu590 | cambricon | NPU | 7 (SMIC N+2) | smic | Flagship 2026 shipment volume chip; ~300k of ~500k total 2026 unit target | HBM/GDDR (unspecified gen) | proprietary | shipping | A100/H100-class (D-grade estimate) | WEB-005 | C |
| cambricon-mlu690 | cambricon | NPU | 7 (SMIC N+2, rumored next-gen) | smic | Next-gen; large-scale mass production reportedly slipping to H2 2026 | unspecified | proprietary | sampling/announced | Next-gen, unconfirmed | WEB-005 | D |
| mtt-s4000 | moore-threads | GPU | unspecified (3rd-gen MUSA arch) | smic (post-2023 Entity List; no TSMC access) | 128 Tensor Cores; used in 1,000-GPU "Intelligent Computing Center" clusters; reported competitive vs. unspecified Nvidia parts in LLM training | 48GB, 768 GB/s bandwidth | proprietary MUSA fabric | shipping | Ampere/Hopper-adjacent (D-grade estimate) | WEB-045 | C |
| mtt-s5000 | moore-threads | GPU | unspecified | smic | DeepSeek V3: ~1,000 tok/s decode, ~4,000 tok/s prefill (vendor-reported) | 80GB HBM | proprietary MUSA fabric | shipping/sampling (2026) | Hopper-class (vendor target) | WEB-045 | D |
| mtt-huashan | moore-threads | GPU | unspecified (announced) | smic (expected) | 2-chiplet design; claimed memory bandwidth exceeding Nvidia B200 | 8x HBM modules | proprietary | announced | Hopper/Blackwell-class (claimed) | WEB-045 | D |
| biren-br100 | biren | GPU | 7 (TSMC) | tsmc | 77bn transistors; 2 chiplets, 537mm2 each; ~2048 TOPS INT8, 1024 TFLOPS BF16, 256 TFLOPS FP32; 550W TDP; TSMC CoWoS 2.5D packaging | 64GB HBM2e, 4096-bit, ~1.6-2.3 TB/s (source variance) | chiplet-to-chiplet + PCIe/OAM | shipping | H100-class (2022-era competitive target) | WEB-044 | C |
| biren-br104 | biren | GPU | 7 (TSMC) | tsmc | Monolithic (non-chiplet); ~1024 TOPS INT8, 128 TFLOPS FP32; 300W TDP; ~half BR100 performance | 32GB HBM2e, 2048-bit, 819 GB/s | PCIe standard card | shipping | A100-class | WEB-044 | C |
| iluvatar-tiangai | iluvatar | GPGPU | 7 | tsmc (where accessible) | First Chinese chip designer to mass-produce both training and inference GPGPU on 7nm | unspecified | proprietary | shipping | Nvidia-class (unspecified generation) | WEB-014 | C |
| kunlun-p800 | kunlunxin | ASIC | unspecified | unspecified (SMIC likely) | Took 70-100% share in select gov/SOE procurement segments; billion-yuan-level order volume | unspecified | unspecified | shipping | Nvidia-class | WEB-019 | C |
| thead-zhenwu | alibaba | ASIC | unspecified | unspecified (TSMC historically, access uncertain) | Powering scale-up from 10k-chip to 100k-chip DC deployments (as previously catalogued) | unspecified | unspecified | deploying/designing | Nvidia-class | REF-BW-01 (seed) | C |

---

## 4. `policy_funding_tracker.csv` — additions

| policy_id | name | level | type | amount_usd_bn | currency_note | date_announced | horizon | target_layers | summary | source_id | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| china-ai-grid-2028 | National AI Computing Grid Plan | national | plan/mandate | 295 (up to ~740 incl. power infra) | draft plan; RMB-denominated original not confirmed in reviewed sources | 2026-06 (drafted/reported) | 2028 | L0\|L4\|L6 | Draft national plan for an AI computing grid run on 80% domestic chips; China Mobile/China Telecom to operate bulk of facilities; structurally excludes Nvidia/AMD from state-funded buildout | WEB-020,WEB-022 | C |
| china-dc-domestic-chip-mandate | State-funded Data Center Domestic Chip Mandate | national | mandate | n.a. | n.a. | 2025-08 (50% rule) escalated 2025-11 (full ban) | ongoing | L4\|L6 | Aug 2025: state-funded DCs required to source ≥50% chips domestically. Nov 2025: escalated to full ban on foreign accelerators in state-funded projects, including retrofit removal from <30%-complete builds. May 2026: 9 categories of domestic AI chips (Huawei, Alibaba, Biren, Moore Threads) cleared security review for gov/security-sensitive deployment | WEB-020,WEB-021 | C |
| us-h200-china-conditional-export | H200 Conditional Export Policy | national (US) | mandate/plan | n.a. | 25% export tax on approved sales | 2025-12 (Trump approval) | ongoing, case-by-case BIS licensing | L4 | H200 sales to China approved conditionally: 25% export tax, capped at ≤50% of total H200 units sold to US customers, BIS case-by-case license review; excludes current Blackwell/upcoming Rubin GPUs; by 2026-05, 10 China firms cleared for H200 purchase | WEB-016,WEB-015 | B |
| us-entity-list-2023-chip-additions | Entity List Additions — Chinese AI Chip Firms | national (US) | mandate | n.a. | n.a. | 2023-10-19 | ongoing | L4 | 13 Chinese entities added to US Entity List for advanced computing chip development, including Biren (multiple subsidiaries) and Moore Threads (multiple subsidiaries); bars access to advanced US foundries/EDA | WEB-043 | A |

---

## 5. `model_catalog.csv` — additions (chip-optimization relevant)

| model_id | developer | release_date | params | weights | modality | benchmark_notes | price_per_mtok | context_len | chips_optimized_for | source_id | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| openpangu-2.0 | huawei | 2026-06-12 | unspecified | unspecified | text/multimodal (unconfirmed) | Reported first frontier-scale model trained entirely on Ascend NPUs with zero Nvidia hardware involvement (vendor-adjacent reporting, not independently verified) | n.a. | unspecified | Ascend (CANN/MindSpore) | WEB-027 | D |
| glm-5 | zhipu (z.ai) | 2026 (reported) | unspecified | unspecified | text/multimodal (unconfirmed) | Reported every parameter trained on Huawei Ascend using MindSpore framework, zero Nvidia dependency | n.a. | unspecified | Ascend (MindSpore) | WEB-027 | D |

---

## 6. Sources (`sources.csv` additions — WEB-xxx)

| source_id | type | title | author_org | date | url_or_locator | notes |
|---|---|---|---|---|---|---|
| WEB-001 | analyst | Huawei AI CloudMatrix 384 – China's Answer to Nvidia GB200 NVL72 | SemiAnalysis | 2025-2026 | https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72 | CloudMatrix 384 specs, PFLOPS comparison |
| WEB-002 | news | Huawei announces annual release cadence for three new Ascend AI chips | DataCenterDynamics | 2026 | https://www.datacenterdynamics.com/en/news/huawei-announces-annual-release-cadence-for-three-new-ascend-ai-chips-unveils-supernode-offering-company-says-will-outperform-nvidias-nvl144/ | 950PR/950DT/Atlas 950 SuperPoD |
| WEB-003 | news | Huawei Unveils Atlas 950 SuperCluster | Tom's Hardware | 2026 | https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-unveils-atlas-950-supercluster-touting-1-fp4-zettaflops-performance-for-ai-inference-and-524-fp8-exaflops-for-ai-training-features-hundreds-of-thousands-of-950dt-apus | Atlas 950 SuperPoD perf claims |
| WEB-004 | social/news | Huawei chip roadmap 910C/950PR-DT/960/970 | Rui Ma (X) | 2025-2026 | https://x.com/ruima/status/1968592824380878931 | Roadmap cadence, secondary reporting |
| WEB-005 | analyst | Cambricon Remains China's Top AI Chip Startup; 2026 Output Faces SMIC Limits | TrendForce | 2025-12-15 | https://www.trendforce.com/news/2025/12/15/insights-cambricon-remains-chinas-top-ai-chip-startup-rumored-2026-triple-output-faces-smic-limits/ | MLU590/690, SMIC capacity constraint |
| WEB-006 | news | The Chinese chip company that's making Nvidia sweat | TechWireAsia | 2025-08 | https://techwireasia.com/2025/08/cambricon-technologies-record-profit-china-ai-chip-revolution/ | Cambricon revenue/profit |
| WEB-007 | news/gov | Moore Threads STAR Market IPO RMB8bn | SSE / Law.asia | 2025-09/12 | https://law.asia/moore-threads-star-market-ipo-chinas-first-gpu-listing/ | IPO mechanics, approval timeline |
| WEB-008 | news | Moore Threads Technology IPO Surges 400% | Cryptonomist | 2026-06-26 | https://en.cryptonomist.ch/2026/06/26/moore-threads-technology-ipo/ | Post-IPO stock performance |
| WEB-009 | news | MetaX soars 700% in debut | SCMP | 2025-12 | https://www.scmp.com/business/china-business/article/3336690/metax-soars-frenzied-debut-traders-snap-second-chinese-gpu-maker-go-public | MetaX Day-1 pop, mkt cap |
| WEB-010 | news | MetaX seeks Hong Kong listing after 700% Shanghai debut | Startup Fortune | 2026 | https://startupfortune.com/metax-seeks-a-hong-kong-listing-after-shocking-shanghai-with-a-700-percent-debut/ | Revenue, unit sales, HK listing plan |
| WEB-011 | news | Biren kicks off Hong Kong IPO | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/tech-industry/biren-kicks-off-hong-kong-ipo | IPO mechanics |
| WEB-012 | news | Biren shares soar as investors seize on first Chinese GPU start-up to list in HK | SCMP | 2026-01 | https://www.scmp.com/business/banking-finance/article/3338447/biren-shares-soar-hong-kong-investors-seize-chinas-first-gpu-start-list | Day-1 performance, oversubscription |
| WEB-013 | news | Iluvatar CoreX Seeks to Raise $850 Million After Stock Rally | Bloomberg | 2026-07-08 | https://www.bloomberg.com/news/articles/2026-07-08/iluvatar-corex-seeks-to-raise-850-million-after-stock-rally | Follow-on raise terms |
| WEB-014 | press release | Iluvatar CoreX's Hong Kong IPO | ACN Newswire | 2026 | https://www.acnnewswire.com/press-release/japanese/104499/iluvatar-corex's-hong-kong-ipo:-hardcore-breakthrough-battle-of-china's-general-purpose-gpu-'leader' | IPO details, ByteDance supply talks |
| WEB-015 | news | Nvidia prepares H200 shipments to China as chip war lines blur | Tom's Hardware | 2025-12 | https://www.tomshardware.com/tech-industry/semiconductors/nvidia-prepares-h200-shipments-to-china-as-chip-war-lines-blur | H200 25% export tax policy |
| WEB-016 | news | US clears H200 chip sales to 10 China firms | CNBC | 2026-05-14 | https://www.cnbc.com/2026/05/14/us-clears-h200-chip-sales-to-10-china-firms-as-nvidia-ceo-looks-for-breakthrough.html | BIS licensing progress |
| WEB-017 | analyst | Baidu Chip Unit Kunlunxin Launches STAR Market IPO Process | TrendForce | 2026-05-08 | https://www.trendforce.com/news/2026/05/08/news-baidu-chip-unit-kunlunxin-reportedly-launches-star-market-ipo-process-hk-listing-valuation-seen-near-hk100b/ | Dual listing, HK$100bn valuation |
| WEB-018 | news | Baidu shares jump as Kunlunxin targets $50bn HK IPO | CNBC | 2026-06-29 | https://www.cnbc.com/2026/06/29/baidu-kunlunxin-hong-kong-ipo-50-billion-ai-chips.html | Updated valuation target |
| WEB-019 | news | Kunlunxin Valued at $50 Billion, Surpassing Its Parent | BigGo Finance | 2026 | https://finance.biggo.com/news/06f12159-f752-4307-bb10-b4d7bab55651 | P800 bid share, customer list |
| WEB-020 | news | China AI Data Center Grid Locks Out Nvidia With $295bn Mandate | TechTimes | 2026-06-22 | https://www.techtimes.com/articles/318868/20260622/china-ai-data-center-grid-locks-out-nvidia-295-billion-domestic-chip-mandate.htm | $295bn plan details |
| WEB-021 | news | China bans foreign AI chips from state-funded data centers | Tom's Hardware | 2025-11 | https://www.tomshardware.com/tech-industry/semiconductors/china-bans-foreign-ai-chips-from-state-funded-data-centers | Nov 2025 mandate escalation |
| WEB-022 | news | China Drafts $295bn Plan for Domestic AI Data Centers, Mandating 80% Local Chips | MLQ News | 2026 | https://mlq.ai/news/china-drafts-295-billion-plan-for-domestic-ai-data-centers-mandating-80-local-chips/ | 80% domestic content target |
| WEB-023 | news | China to increase leading-edge chip output by 5x in two years | Tom's Hardware | 2026-02 | https://www.tomshardware.com/tech-industry/semiconductors/china-to-increase-leading-edge-chip-output-by-5x-in-two-years-report-claims-aims-to-lift-7nm-and-5nm-production-to-100-000-wafers-per-month-targeting-half-a-million-monthly-by-2030 | Capacity targets 2027/2030 |
| WEB-024 | analyst | China Aims to Boost 7nm, 5nm Output Fivefold in Two Years | TrendForce | 2026-02-25 | https://www.trendforce.com/news/2026/02/25/news-china-reportedly-aims-to-boost-7nm-5nm-output-fivefold-in-two-years-driven-by-smic-and-hua-hong/ | SMIC + Hua Hong capacity plan |
| WEB-025 | news | Huawei is making its Ascend AI GPU software toolkit open-source | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-is-making-its-ascend-ai-gpu-software-toolkit-open-source-to-better-compete-against-cuda | CANN open-sourcing |
| WEB-026 | blog | What Is openPangu 2.0? First Frontier Model Trained Without NVIDIA | andrew.ooo | 2026-06 | https://andrew.ooo/answers/what-is-openpangu-2-huawei-nvidia-free-june-2026/ | openPangu 2.0 claim |
| WEB-027 | analyst | Can Huawei Take On Nvidia's CUDA? | ChinaTalk | 2026 | https://www.chinatalk.media/p/can-huawei-compete-with-cuda | CANN/MindSpore ecosystem maturity; GLM-5 claim |
| WEB-028 | news | DeepSeek research suggests Ascend 910C delivers 60% of H100 inference performance | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-research-suggests-huaweis-ascend-910c-delivers-60-percent-nvidia-h100-inference-performance | 910C benchmark |
| WEB-029 | blog | Huawei Ascend 910C vs NVIDIA H100 | NexGen Compute | 2025-2026 | https://www.nexgen-compute.com/blog/huawei-ascend-910c-vs-nvidia-h100-ai-chip-comparison | Jensen Huang "H200-comparable" quote |
| WEB-030 | news | Super Micro office raided as Taiwan expands chip smuggling probe | Bloomberg | 2026-06-29 | https://www.bloomberg.com/news/articles/2026-06-29/super-micro-office-raided-as-taiwan-expands-chip-smuggling-probe | Smuggling investigation |
| WEB-031 | news | China's Nvidia Black Market Prices Surge as Chip Smuggling Routes Close | Digital Citizen | 2026 | https://www.digitalcitizen.life/chinas-nvidia-black-market-prices-surge-as-chip-smuggling-routes-close/ | Black-market pricing |
| WEB-032 | news | Nvidia chip shortages fuel underground market surge in China | TechBriefly | 2026-06-24 | https://techbriefly.com/2026/06/24/nvidia-chip-shortages-fuel-underground-market-surge-in-china/ | Gray-market demand |
| WEB-033 | news | ByteDance is reportedly developing its own custom AI CPUs | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/tech-industry/semiconductors/tiktok-owner-bytedance-is-reportedly-developing-its-own-custom-ai-cpus-company-looks-to-ease-chinas-dependence-on-us-chipmakers | In-house ASIC project |
| WEB-034 | news | ByteDance reportedly plans to purchase $5.6bn of Huawei's Ascend AI chips | TechNode | 2025-12-29 | https://technode.com/2025/12/29/bytedance-reportedly-plans-to-purchase-5-6-billion-worth-of-huaweis-ascend-ai-chips/ | Ascend procurement |
| WEB-035 | news | ByteDance to pour US$14bn into Nvidia chips in 2026 | SCMP | 2026 | https://www.scmp.com/tech/big-tech/article/3338191/bytedance-pour-us14-billion-nvidia-chips-2026-computing-demand-surges | Parallel Nvidia procurement |
| WEB-036 | analyst/blog | Where China's AI chip supply chain stands in 2026 | The Substrate | 2026 | https://www.the-substrate.net/p/where-chinas-ai-chip-supply-chain | Foundry relationships (TSMC vs SMIC) |
| WEB-037 | analyst/blog | Silicon Vanguard: Ranking China's Domestic Chip Leaders | Machine Yearning | 2026 | https://www.machineyearning.io/p/chinas-silicon-vanguard | SMIC share, node comparison |
| WEB-038 | news | Nvidia market share in China falls to less than 60% | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/tech-industry/nvidia-market-share-in-china-falls-to-less-than-60-percent-chinese-chip-makers-deliver-1-65-million-ai-gpus-as-the-government-pushes-data-centers-to-use-domestic-chips | Nvidia share trajectory |
| WEB-039 | news | Nvidia CEO Jensen Huang says company now has zero market share in China | Yahoo Finance | 2026 | https://finance.yahoo.com/sectors/technology/article/nvidia-ceo-jensen-huang-says-company-now-has-zero-market-share-in-china-150805330.html | CEO statement |
| WEB-040 | news | Cambricon's Trillion-Yuan Market Cap 'Day Trip' | BigGo Finance | 2026-07 | https://finance.biggo.com/news/98bc1a60-279a-4c01-9464-05c0a704b4fa | Mkt cap peak & correction |
| WEB-041 | market data | Cambricon Technologies Corporation (SHA:688256) Market Cap | StockAnalysis.com | 2026-07-06 | https://stockanalysis.com/quote/sha/688256/market-cap/ | Exchange-sourced market cap |
| WEB-042 | market data | Moore Threads (688795.SS) Market capitalization | CompaniesMarketCap | 2026-07-08 | https://companiesmarketcap.com/moore-threads/marketcap/ | Exchange-sourced market cap |
| WEB-043 | gov/official | Entity List Additions | US Federal Register | 2023-10-19 | https://www.federalregister.gov/documents/2023/10/19/2023-23048/entity-list-additions | Official Entity List action naming Biren, Moore Threads |
| WEB-044 | technical/news | Biren Technology Unveils BR100 7nm HPC GPU with 77 Billion Transistors | TechPowerUp | 2022 (specs, still current design) | https://www.techpowerup.com/297619/biren-technology-unveils-br100-7-nm-hpc-gpu-with-77-billion-transistors | BR100/BR104 specs |
| WEB-045 | news | China-made Moore Threads AI GPUs used for LLM training | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/pc-components/gpus/china-made-moore-threads-ai-gpus-used-for-three-billion-parameter-llm-training-mtt-s4000-appears-competitive-against-unspecified-nvidia-solutions | MTT S4000/S5000 specs |
