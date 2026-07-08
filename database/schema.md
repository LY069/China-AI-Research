# Evidence Database — Schema

All tables are CSV for portability (load into Excel / pandas / SQLite). Every data row references a `source_id` in `sources.csv` and carries a `confidence` grade.

**Confidence grades:** `A` filed/audited · `B` primary disclosure (co. statement, prospectus) · `C` credible 3rd-party · `D` single-source / estimate.

---

## 1. `company_master.csv` — backbone
One row per company. The spine everything joins to.

| Field | Description |
|-------|-------------|
| company_id | short slug (e.g. `amec`, `smic`) |
| name_en / name_cn | English / Chinese name |
| layers | pipe-delimited stack layers (e.g. `L1\|L2`) |
| segment | finer segment (e.g. "etch equipment", "DRAM", "GPU") |
| ownership | state / SOE-linked / private / listed-public / mixed |
| listing_status | listed / IPO-filed / IPO-approved / private |
| exchange_ticker | e.g. `SSE:688012`, `HKEX:0981`, `private` |
| hq | city |
| founded | year |
| entity_list | US Entity List / restricted flag: yes / no / partial / n.a. |
| investable_foreign | can non-Chinese public investors hold: yes / restricted / no |
| mkt_cap_usd_bn | market cap (dated in notes) |
| fwd_pe | forward P/E |
| key_products | core products |
| china_role | national-champion / challenger / incumbent |
| global_peer | closest US/global comparable |
| source_id | primary source |
| confidence | A-D |
| notes | free text incl. figure dates |

## 2. `metrics_timeseries.csv` — tracked metrics over time
| Field | Description |
|-------|-------------|
| metric_id | e.g. `china_inference_gw`, `smic_7nm_yield` |
| entity | company / country / "China" / "US" |
| layer | stack layer or `macro` |
| metric_name | human label |
| unit | GW, $bn, %, units, tokens/mo, DAU-m, nm |
| period | date or quarter (e.g. `2026-Q1`, `2026`) |
| value | numeric |
| source_id | |
| confidence | A-D |
| notes | |

## 3. `policy_funding_tracker.csv`
| Field | Description |
|-------|-------------|
| policy_id | slug |
| name | program / fund / mandate |
| level | national / provincial / municipal |
| type | fund / mandate / subsidy / plan / standard |
| amount_usd_bn | size if applicable |
| currency_note | original currency & amount |
| date_announced | |
| horizon | target years |
| target_layers | which stack layers |
| summary | |
| source_id / confidence | |

## 4. `model_catalog.csv`
| Field | Description |
|-------|-------------|
| model_id | e.g. `deepseek-v4`, `qwen3` |
| developer | company_id |
| release_date | |
| params | parameters / MoE active |
| weights | open / closed / hybrid |
| modality | text / multimodal / etc. |
| benchmark_notes | key eval scores |
| price_per_mtok | blended $/1M tokens |
| context_len | |
| chips_optimized_for | e.g. Ascend, Cambricon, Nvidia |
| source_id / confidence | |

## 5. `chip_catalog.csv`
| Field | Description |
|-------|-------------|
| chip_id | e.g. `ascend-950`, `cambricon-590` |
| vendor | company_id |
| type | GPU / NPU / ASIC / CPU |
| node_nm | process node |
| fab | foundry |
| flops_notes | FP16/FP8/INT8 throughput |
| memory | HBM/GB & bandwidth |
| interconnect | scale-up/out fabric |
| release_status | shipping / sampling / announced |
| global_analog | e.g. "H100-class" |
| source_id / confidence | |

## 6. `sources.csv`
| Field | Description |
|-------|-------------|
| source_id | e.g. `REF-BW-01`, `WEB-001` |
| type | reference-report / filing / prospectus / news / analyst / gov |
| title | |
| author_org | |
| date | |
| url_or_locator | |
| notes | |
