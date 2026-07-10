# P4 — Talent & R&D — Database-ready data (v2)

Mirrors `database/schema.md`. No master CSVs edited; these are additions for the Research Director to merge. Source IDs use the WEB-8xx range reserved for P4 per `_conventions_v2.md`.

---

## 1. `metrics_timeseries.csv` — new rows

| metric_id | entity | layer | metric_name | unit | period | value | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|
| china_gatt_researcher_origin_share | China | T | Share of GATT-tracked elite AI researchers with China undergrad origin | % | 2022-2024 | 38 | WEB-801 | C | MacroPolo GATT; rose from 27% (2017)/29% (2019); reported via secondary source (MacroPolo site 403'd to fetch) |
| china_educated_researchers_in_us_share | China-educated researchers | T | Share of China-educated elite AI researchers currently working at US institutions | % | ~2022 | 72 | WEB-801 | C | MacroPolo GATT |
| china_educated_researchers_in_china_share | China-educated researchers | T | Share of China-educated elite AI researchers remaining in China | % | ~2022 | 11 | WEB-801 | C | Down from 16% in 2019; MacroPolo GATT |
| us_elite_researcher_employment_share | United States | T | US institutions' share of world's elite AI researchers (by employment) | % | 2022-2024 | 59 | WEB-801 | C | Up from 51% in 2017; MacroPolo GATT |
| us_china_origin_share_of_us_researchers | United States | T | Combined US- and China-origin share of elite researchers employed in US | % | 2022 | 75 | WEB-802 | C | Up from 58% in 2019; Paulson Institute press release on GATT |
| grad_school_stickiness_us | United States | T | Share of elite researchers who did graduate study in US and stayed in US | % | n.d. (GATT vintage) | 80 | WEB-801 | C | MacroPolo GATT |
| grad_school_stickiness_china | China | T | Share of elite researchers who did graduate study in China and stayed in China | % | n.d. (GATT vintage) | 90 | WEB-801 | C | MacroPolo GATT |
| ai_talent_migration_to_us_decline | United States | T | Decline in AI-talent migration into the US since 2017 | % | 2017-2025 | -89 | WEB-804 | C | Stanford AI Index 2026, reported via Fortune (primary PDF 403'd to fetch); 80% of decline in most recent year |
| deepseek_researchers_returned_from_us | DeepSeek | T | Share of DeepSeek researchers with 5+ yrs US experience who have returned to China | % | 2025 (roster analysis) | ~70 | WEB-813 | D | Analysis of public researcher roster, one company, not population-representative |
| deepseek_core_team_domestic_trained | DeepSeek | T | Share of DeepSeek's ~31 identified core researchers never trained/worked outside China | % | 2025 | ~33 | WEB-814 | D | Hoover Institution analysis |
| china_ai_publication_share | China | T | Share of global AI research publications | % | 2025 | 23.2 | WEB-804 | C | Stanford AI Index 2026 (secondary-reported) |
| china_ai_citation_share | China | T | Share of global AI research citations | % | 2025 | 20.6 | WEB-804 | C | Stanford AI Index 2026 |
| us_ai_publication_share | United States | T | Share of global AI research publications | % | 2025 | 12.6 | WEB-804 | C | Stanford AI Index 2026 |
| china_top100_cited_papers | China | T | China share of top 100 most-cited AI papers (count) | count /100 | 2024 | 41 | WEB-804 | C | Up from 33 in 2021; Stanford AI Index 2026 |
| china_pct_patent_applications | China | T | PCT international patent applications filed | count | 2025 | 73718 | WEB-816 | B | WIPO — named primary statistical source |
| us_pct_patent_applications | United States | T | PCT international patent applications filed | count | 2025 | 52617 | WEB-816 | B | WIPO |
| china_ai_patent_filing_share | China | T | Share of global AI patent filings | % | 2025 | 69.7 | WEB-804 | C | Stanford AI Index 2026 |
| china_genai_patent_families | China | T | Generative-AI patent families filed | count | n.d. (~2024-25) | 38210 | WEB-816 | C | ~6x US count (6,276); WIPO-adjacent reporting, not line-item verified by us |
| huawei_pct_filings_2024 | Huawei | T | Corporate PCT patent applications published (global #1 filer) | count | 2024 | 6600 | WEB-816 | B | WIPO |
| china_stem_phd_awarded | China | T | STEM doctorates awarded | count | 2022 | 50000 | WEB-807 | C | +13.7% YoY; Georgetown CSET, based on MOE/NBS data; engineering 59.1% of total |
| china_stem_phd_projected_2025 | China | T | Projected STEM PhDs/year | count | 2025 (projection) | 77000 | WEB-808 | D | CSET trend-line projection, not a filed count; vs. US ~40,000 projected |
| china_university_graduates_total | China | T | Total university graduates | million | 2026 | 12.7 | WEB-810 | B | MOE figure, +480k vs 2025, reported via Global Times |
| china_degree_programs_discontinued | China | T | Undergraduate degree programs discontinued/suspended | count | 2021-2025 | 12200 | WEB-811 | B | MOE data via Forbes; ~10,200 new programs introduced in same window, tech/digitalization-weighted |
| china_ai_research_workforce_total | China | T | Estimated national AI research workforce | count | 2024 | 52000 | WEB-815 | D | Single secondary-sourced report (TMTPost); up from <10,000 in 2015; methodology unverified |
| tsinghua_ai_researchers | Tsinghua University | T | AI researchers (self-identified) | count | 2024 | 2667 | WEB-815 | D | Same unverified source as above |
| pku_ai_researchers | Peking University | T | AI researchers (self-identified) | count | 2024 | 2123 | WEB-815 | D | Same unverified source as above |
| cas_ai_researchers | Chinese Academy of Sciences | T | AI researchers (self-identified) | count | 2024 | 3453 | WEB-815 | D | Same unverified source as above |
| neurips2025_china_poster_share | China | T | Share of NeurIPS/ICLR poster-track author affiliations | % | 2025-2026 | ~40 | WEB-823 | D | Secondary aggregator reporting; direction (China>US posters) more reliable than exact number |
| neurips2025_china_oral_share | China | T | Share of NeurIPS/ICLR oral-track author affiliations | % | 2025-2026 | ~30 | WEB-823 | D | US inverse pattern (~40 oral/~30 poster); see memo caveat |
| tsinghua_neurips2025_papers | Tsinghua University | T | NeurIPS 2025 accepted papers (institution total) | count | 2025 | 100+ | WEB-823 | C | Most of any single global institution per secondary reporting |
| china_semiconductor_talent_gap | China | T | Semiconductor/chip-design talent gap (IC design, EDA, packaging) | persons | 2025 | 200000-300000 | WEB-818 | D | Industry recruiter market report, not government statistic |
| china_advanced_node_design_leads | China | T | Technical-director-level design leads w/ sub-5nm experience | count | 2025 | <100 | WEB-818 | D | Same source; demand estimated >300 |
| china_ai_talent_shortfall_2030 | China | T | Projected AI professional shortfall | million | by 2030 | 4 | WEB-822 | D | McKinsey estimate via TechNode; primary report not accessed |
| bytedance_beijing_headcount | ByteDance | T | Beijing campus employees | count | 2025-2026 | ~30000 | WEB-828 | D | ~40% of global headcount per single blog-style source; unverified vs. company disclosure |
| tencent_ai_lab_researchers | Tencent AI Lab | T | Researchers | count | n.d. | 500+ | WEB-828 | D | Single unverified source |
| china_stem_phd_2022_engineering_share | China | T | Engineering share of STEM doctorates | % | 2022 | 59.1 | WEB-807 | C | Georgetown CSET |
| china_ai_engineer_recruitment_demand_growth | China | T | YoY growth in AI-engineer recruitment demand | % | 2025-Q3 | 25 | WEB-810 | D | Recruitment-portal data via SCMP-adjacent reporting |

---

## 2. `policy_funding_tracker.csv` — new rows

| policy_id | name | level | type | amount_usd_bn | currency_note | date_announced | horizon | target_layers | summary | source_id | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| china-k-visa-2025 | K-Visa for young STEM talent | national | mandate/visa | n.a. | n.a. | 2025-08-07 (effective 2025-10-01) | ongoing | T | Sponsor-free multi-entry visa for foreign STEM professionals aged roughly 18-45; positioned as response to US H-1B fee hikes; work/study/research/business permitted | WEB-821 | B |
| china-young-thousand-talents-successor | Young Thousand Talents / Qiming Program | national | subsidy/plan | n.a. | RMB 1-3m start-up grants per recruit | ongoing (rebranded program) | ongoing | T | Recruits under-40 STEM scientists with start-up grants, salary (RMB 300k-1m/yr), housing/insurance/education support; successor branding to original Thousand Talents Plan | WEB-825, WEB-827 | C |
| us-china-student-visa-tightening-2025 | State Dept student-visa scrutiny/revocation directive | national (US) | mandate | n.a. | n.a. | 2025-05-27/28 | ongoing | T | US paused new F/M/J visa interview scheduling pending expanded social-media vetting; announced "aggressive" scrutiny/revocation of visas for Chinese/HK students, esp. "critical fields" | WEB-819 | B |
| us-mcf-grad-student-proclamation-2025 | Presidential proclamation suspending entry for MCF-linked Chinese grad students/researchers | national (US) | mandate | n.a. | n.a. | 2025 | ongoing | T | Suspends F/J visa entry for Chinese graduate students/researchers with current/prior ties to China's military-civil fusion strategy in STEM fields; undergraduates exempted | WEB-820 | B |
| china-15fyp-ai-talent | 15th Five-Year Plan sci-tech talent priority | national | plan | n.a. | n.a. | 2025-2026 (plan period 2026-2030) | 2030 | T | Elevates sci-tech talent base to national strategic priority; mandates AI as basic public course from primary school; university "discipline optimization" toward AI/strategic fields; teacher AI-literacy standard | WEB (gov.cn / Merics / Strider, various) | C |

---

## 3. `sources.csv` — new WEB-8xx rows

| source_id | type | title | author_org | date | url_or_locator | notes |
|---|---|---|---|---|---|---|
| WEB-801 | analyst | Global AI Talent Tracker (2.0/3.0) — interactive project | MacroPolo (Paulson Institute) | 2024-03 (2.0) / 2025 (3.0 update, NeurIPS/ICML/ICLR data) | https://archivemacropolo.org/interactive/digital-projects/the-global-ai-talent-tracker | Returned HTTP 403 to automated fetch; figures relayed via secondary reporting (MIT Tech Review, Paulson press release) |
| WEB-802 | news | Study Finds US Remains a Magnet for World's Best and Brightest AI Talent... | Paulson Institute (press release) | 2024 | paulsoninstitute.org/press_release/study-finds-us-remains-a-magnet-... | Also 403'd to direct fetch; summarized via search snippet |
| WEB-803 | news | Four things you need to know about China's AI talent pool | MIT Technology Review | 2024-03-27 | technologyreview.com/2024/03/27/1090182/ai-talent-global-china-us/ | Secondary summary of GATT 2.0 |
| WEB-804 | analyst | The 2026 AI Index Report (R&D and Education chapters) | Stanford HAI | 2026 (report covers 2025 data) | hai.stanford.edu/ai-index/2026-ai-index-report | Primary PDF and web chapters returned HTTP 403 to automated fetch; all figures relayed via secondary press coverage |
| WEB-805 | news | Stanford AI Index 2026: China narrows US lead to 2.7%... | crypto.news / thenextweb.com | 2026 | thenextweb.com/news/stanford-ai-index-2026-china-us-performance-gap | Secondary summary of AI Index 2026 |
| WEB-806 | news | Stanford: China has 'nearly erased' U.S. AI lead as flow of tech experts to America slows | Fortune | 2026-04-16 | fortune.com/2026/04/16/stanford-study-how-has-china-gained-on-us-ai-war/ | Secondary summary incl. 89% migration-decline figure |
| WEB-807 | analyst | China is Fast Outpacing U.S. STEM PhD Growth (data brief) | Georgetown CSET | 2021-08 (2022 data referenced in later CSET pieces) | cset.georgetown.edu/publication/china-is-fast-outpacing-u-s-stem-phd-growth/ | Named primary think-tank data brief based on MOE/NBS statistics |
| WEB-808 | analyst | Should the US fear rising number of STEM PhDs in China? | Georgetown CSET | n.d. | cset.georgetown.edu/article/should-the-us-fear-rising-number-of-stem-phds-in-china/ | Contains 2025 projection figures (~77,000 China vs ~40,000 US) |
| WEB-809 | analyst | The Global Distribution of STEM Graduates: Which Countries Lead the Way? | Georgetown CSET | n.d. | cset.georgetown.edu/article/the-global-distribution-of-stem-graduates-which-countries-lead-the-way/ | Cross-country STEM graduate comparison |
| WEB-810 | news | China's 2026 college graduates to hit 12.7 million; localities mobilize quality employment: MOE | Global Times | 2025-11 | globaltimes.cn/page/202511/1348697.shtml | Reports official MOE figure |
| WEB-811 | news | China Cuts 12,200 University Programs, Replaces Many With AI Degrees | Forbes | 2026-06-23 | forbes.com/sites/annaesakismith/2026/06/23/china-cuts-12200-university-programs-replaces-many-with-ai-degrees/ | MOE program-reallocation data |
| WEB-812 | news | Chinese universities drop humanities majors for AI | Rest of World | 2026 | restofworld.org/2026/chinese-universities-drop-humanities-ai/ | Corroborates WEB-811 |
| WEB-813 | news | China's AI talent fueled DeepSeek's rise, challenging U.S. dominance | Rest of World | 2025 | restofworld.org/2025/china-ai-talent-deepseek-rise-us-dominance/ | Roster/case-study analysis, single company |
| WEB-814 | analyst | A Deep Peek Into DeepSeek AI's Talent And Implications For US Innovation | Hoover Institution | 2025 | hoover.org/research/deep-peek-deepseek-ais-talent-and-implications-us-innovation | Named think-tank analysis of DeepSeek public researcher roster |
| WEB-815 | news | China Narrows AI Talent Gap With U.S. as Research Enters Engineering Phase: Report | TMTPost | n.d. | en.tmtpost.com/post/7616647 | Could not access directly (403); relayed via search snippet only — lowest-confidence source in this pod, methodology unverified |
| WEB-816 | gov | World Intellectual Property Indicators 2025: Highlights (Patents) | WIPO | 2025 | wipo.int/web-publications/world-intellectual-property-indicators-2025-highlights/en/patents-highlights.html | Named primary international statistical agency |
| WEB-817 | news | China Remains Top Source of Patent Cooperation Treaty (PCT) Applications in 2024 | National Law Review / China IP Law Update | 2025-03 | natlawreview.com/article/china-remains-top-source-patent-cooperation-treaty-pct-applications-2024 | Corroborates WIPO figures |
| WEB-818 | analyst | China's Chip Industry on a Global Semiconductor Talent Hunt: A 250,000 Shortage... | hiredchina.com (recruiting-industry publisher) | 2025 | hiredchina.com/articles/semiconductor-talent-hunt-in-chinas-semiconductor-industry/ | Industry/recruiter estimate, not government statistic — D-grade throughout |
| WEB-819 | news | US to 'Aggressively Revoke' Visas Held by Chinese Students | AIP.org (American Institute of Physics, FYI newsletter) | 2025-05 | aip.org/fyi/us-to-aggressively-revoke-visas-held-by-chinese-students | Reports State Department policy directly |
| WEB-820 | analyst | The International Student Talent Pipeline: Changes in US Visa and Work Authorization Policies | Mayer Brown | 2025-05 | mayerbrown.com/en/insights/publications/2025/05/the-international-talent-pipeline-changes-in-us-visa-and-work-authorization-policies | Law-firm summary of presidential proclamation on MCF-linked grad students |
| WEB-821 | gov | China to launch new type of visa for young science, technology professionals | The State Council (gov.cn, English) | 2025-08-14 | english.www.gov.cn/policies/latestreleases/202508/14/content_WS689dd0d3c6d0868f4e8f4d1e.html | Primary official government announcement of K-visa |
| WEB-822 | news | China may face an AI talent shortage of four million by 2030 | TechNode | 2025-01-28 | technode.com/2025/01/28/china-may-face-an-ai-talent-shortage-of-four-million-by-2030/ | Reports McKinsey estimate; primary McKinsey report not independently accessed |
| WEB-823 | analyst | From Beijing to San Francisco: What NeurIPS 2025 reveals about AI leadership | AI World | 2025-2026 | aiworld.eu/story/from-beijing-to-san-francisco-what-neurips-2025-reveals-about-ai-leadership | Secondary aggregator analysis of conference-affiliation data |
| WEB-824 | analyst | Most ICLR papers written in China while top papers come from the US | AI World | 2025-2026 | aiworld.eu/story/most-iclr-papers-written-in-china-while-top-papers-come-from-the-us | Secondary aggregator; poster/oral split by country |
| WEB-825 | news | How China's bold talent recruitment has shaped science | Nature | 2025 | nature.com/articles/d41586-025-02336-w | Named science-journal reporting on Chinese talent programs |
| WEB-826 | analyst | Chinese Talent Program Tracker | Georgetown CSET | ongoing | chinatalenttracker.cset.tech | Named primary tracker of Chinese state talent-recruitment programs; referenced for context, not directly queried for figures in this memo |
| WEB-827 | analyst | Evaluating the Success of China's "Young Thousand Talents" STEM Recruitment Program | Stanford FSI (SCCEI) | n.d. | sccei.fsi.stanford.edu/china-briefs/evaluating-success-chinas-young-thousand-talents-stem-recruitment-program | Named academic research center |
| WEB-828 | analyst | Beijing AI Talent: Why the World's Deepest Research Bench Cannot... | KiTalent (recruiting-industry blog) | n.d. | kitalent.com/articles/beijing-ai-talent-hiring-crisis | Single blog-style source for ByteDance/Tencent headcount figures — D-grade, unverified vs. company disclosure |
| WEB-829 | news | In the race to attract the world's smartest minds, China is gaining on the US | CNN | 2025-09-29 | cnn.com/2025/09/29/china/china-reverse-brain-drain-science-tech-competition-us-intl-hnk | Context on reverse-brain-drain narrative |

---

## Notes for Research Director

- All entity names above ("China", "United States", "DeepSeek", "Huawei", "Tsinghua University", etc.) follow the free-text `entity` convention in `metrics_timeseries.csv`; `DeepSeek` and `Huawei` map to existing `company_id` values `deepseek` and `huawei` in `company_master.csv` if you want to join.
- No new `company_master.csv` rows are proposed — Talent & R&D is a workforce/output cross-cut, not a set of new named companies. Universities (Tsinghua, PKU, CAS) and corporate labs (Noah's Ark, DAMO, Tencent AI Lab) are referenced as `entity` values in `metrics_timeseries.csv` rather than added to `company_master.csv`, since they are not investable securities.
- Two sources (WEB-801/802 MacroPolo, WEB-804 Stanford HAI) could not be fetched directly by this pod (HTTP 403 on automated fetch to both domains) — all figures from them are relayed via secondary press coverage and graded C rather than the A/B they might otherwise merit as named primary studies. The Red-Team reviewer should re-attempt direct access if browser-based verification is available, since upgrading these to A/B would materially strengthen the pod's best data.
- WEB-815 (TMTPost, China AI research workforce/Tsinghua/PKU/CAS headcounts) is the single weakest source relied upon for a headline figure in this pod — recommend the Red-Team either find a corroborating primary source or downgrade/strike the 52,000/2,667/2,123/3,453 figures from the final report.
