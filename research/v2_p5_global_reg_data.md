# v2 Pod 5 — Database Additions: Global Investability & Non-US Regulation

Mirrors `database/schema.md`. All new source IDs use the **WEB-85x** range per `_conventions_v2.md` (P5 block). Confidence grades follow the tightened v2 rule: A/B require a named, checkable primary source.

---

## 1. `company_master.csv` — investability-by-domicile note updates (NOT full row replacements)

These are **additive notes** refining the existing `investable_foreign` field with a domicile breakdown. Apply as an appended note to each company's existing row; do not overwrite other fields. Field `investable_foreign_by_domicile` is a new v2-suggested sub-field (free text) if the director wants to formalize it in `company_reference.csv` (P6-owned) or as a `notes` append here.

| company_id | investable_foreign_by_domicile (append note) | source_id | confidence |
|---|---|---|---|
| smic | US: no (EL). EU/UK/Japan/Korea/Singapore/India/Gulf: yes via HK-line (HKEX:0981), no domicile-specific legal bar identified. A-line (SSE:688981) subject to 30% FOL + QFII/Connect mechanics for all foreign holders alike. Taiwan: outbound-scrutiny risk on Taiwanese capital (not a confirmed bar). | WEB-851,WEB-861,WEB-869 | C |
| cambricon | US: no (EL). All other researched domiciles: access via QFII/Connect-eligible-if-included mechanics only (A-share, no HK line) — same friction for every foreign holder regardless of domicile; no domicile-specific legal bar found outside US/Taiwan. | WEB-867 | C |
| moore-threads | US: no (EL). Non-US: A-share (SSE:688795) via QFII; STAR Market professional-investor-only gate applies to all foreign retail regardless of domicile. | WEB-865,WEB-867 | C |
| metax | US: no (EL). Non-US: same STAR/QFII gate as Moore Threads; no domicile-specific bar identified. | WEB-865,WEB-867 | C |
| biren | US: no (EL). EU/UK/Japan/Korea/Singapore/India/Gulf: yes via HKEX:6844, no domicile-specific bar. Verified cornerstone list (Ping An, 3W Fund, Qiming, UBS, Lion Global, Eastspring) shows Asian/Chinese capital, no confirmed Gulf participant. | WEB-864 | C/D |
| iluvatar | US: constrained (EL partial). Non-US: yes via HKEX, no domicile-specific bar identified. | WEB-865 | C |
| kunlunxin | US: constrained (EL partial). Non-US: yes (pending HK listing), no domicile-specific bar identified. | WEB-865 | D |
| cxmt | US: no (EL, pending listing). Non-US: will require QFII/Connect-eligibility once listed on STAR Market; same mechanics for all foreign holders. | WEB-865,WEB-867 | D |
| ymtc | US: no (EL, pending listing). Non-US: same as CXMT once listed. | WEB-865,WEB-867 | D |
| montage | US: yes. Non-US: yes, H-line (HKEX:6809) preferred — no FOL, now trades at a premium to the A-line (SSE:688008), a reversal of the typical A>H pattern reflecting foreign-capital preference for the unrestricted line. | WEB-869 (Pod-6 WEB-654 cross-ref) | B |
| alibaba | US: yes (NYSE:BABA carries HFCAA/PCAOB risk-factor disclosure; risk currently dormant post Dec-2022 PCAOB access restoration). Non-US: yes, HKEX:9988 line unaffected by HFCAA. Japan: GPIF's benchmark exclusion targets onshore China A-shares — BABA (HK/NYSE only) is likely unaffected, but this was not independently confirmed against GPIF's exact exclusion methodology. | WEB-868,WEB-875 | B/D |
| tencent | US: yes. Non-US: yes, no domicile-specific bar identified (no US ADR line, no HFCAA exposure). | — | C |
| baidu | US: yes (NASDAQ:BIDU carries same dormant HFCAA risk-factor as Alibaba). Non-US: yes via HKEX:9888. | WEB-868 | B |
| zhipu | US: constrained (dual-use AI overlay per Pod 6). Non-US: yes via HKEX, no domicile-specific bar identified; not yet Stock-Connect-eligible per Pod-6 seasoning finding. | WEB-866 | C |
| minimax | Same profile as Zhipu. | WEB-866 | C |
| catl | US: yes. Non-US: yes, no domicile-specific bar identified. | — | C |
| naura | US: constrained (partial EL/OISP overlap). Non-US: A-share only (SZSE:002371); same QFII/FOL mechanics for all foreign holders; no additional domicile-specific bar found. | WEB-867,WEB-869 | C |
| amec | Same profile as NAURA (SSE:688012). | WEB-867,WEB-869 | C |
| empyrean | Same profile as NAURA (SZSE:301269). | WEB-867,WEB-869 | C |

---

## 2. `policy_funding_tracker.csv` — non-US regimes

| policy_id | name | level | type | amount_usd_bn | currency_note | date_announced | horizon | target_layers | summary | source_id | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| eu-fdi-screen-2026 | EU Foreign Investment Screening Regulation (2026 overhaul) | supranational (EU) | mandate | n/a | n/a | 2026-05-19 | in force ~summer 2026 + 18mo implementation | L1-L9 (inbound) | Mandatory Union-level screening for critical sectors incl. semiconductors, quantum, "certain AI"; extends to non-EU-controlled EU entities. Governs China→EU capital, not EU→China. | WEB-851 | B |
| eu-outbound-monitor-2026 | EU Outbound Investment (SAIQ) Monitoring Recommendation | supranational (EU) | plan | n/a | n/a | 2025-01 (recommendation) | monitoring through 2026-06-30, pre-legislative | L1,L4,L7 (semiconductor/AI/quantum) | Member states track outbound EU investment into SAIQ tech since Jan-2021; comprehensive report due 30-Jun-2026; evidence-gathering toward a possible future outbound-screening rule — not yet binding. | WEB-850 | B |
| uk-nsia-2026-reform | UK NSIA semiconductor/AI schedule reform | national (UK) | mandate | n/a | n/a | 2026-03-12 | ongoing | L1,L4 (inbound) | Standalone semiconductor sector carved out (adv. packaging, design); AI schedule narrowed to exclude routine/licensed third-party use. No UK outbound-screening regime exists or is yet planned. | WEB-854,WEB-856 | B/C |
| uk-ftdi-divestment | FTDI forced divestment order | national (UK) | mandate (enforcement) | 0.414 (original 2021 deal) | $414m acquisition unwound | 2026-02 (order) | n/a | L1 | UK ordered JAC Capital-led Chinese consortium to sell its stake in Scottish chipmaker FTDI, unwinding an already-completed Dec-2021 acquisition — rare post-closing NSIA reversal. | WEB-855 | B |
| japan-fefta-2026 | Japan FEFTA reform (semiconductor/AI core sectors, high-risk investor category) | national (Japan) | mandate | n/a | n/a | 2026-05-29 (passed) | ongoing | L1,L4 (inbound) | Adds semiconductor-equipment mfg and AI to core sectors; "high-risk foreign investor" (SWFs, Chinese investors per commentary) subject to 1% notification threshold vs. 50% standard. | WEB-857,WEB-858 | B |
| japan-gpif-china-a-exclusion | GPIF exclusion of China A-shares from equity benchmark | national (Japan) | plan (institutional policy, not law) | 1870 (fund AUM, not exclusion size) | ¥277tn AUM ($1.87tn) | 2025 (5-yr policy period start) | 2025-2030 | L4,L7 (portfolio) | World's largest public pension fund voluntarily excludes mainland China A-shares from its foreign-equity benchmark for the current policy period — prudential, not legally mandated. | WEB-875 | C |
| taiwan-prc-positive-list | Taiwan Positive List for PRC-controlled capital | national (Taiwan) | mandate | n/a | n/a | ongoing (strengthened through 2026) | ongoing | L1-L9 (inbound to Taiwan) | Capital identified as >30% PRC-controlled (incl. disguised routing) restricted to explicitly approved sectors (inverse of standard Negative List); CCP/military-linked entities barred outright. | WEB-861 | C |
| taiwan-outbound-china-scrutiny | Taiwan tightened scrutiny of outbound investment into mainland China tech | national (Taiwan) | mandate | n/a | n/a | 2026-07 (reported) | ongoing | L1,L4 (outbound from Taiwan) | New law increases scrutiny of Taiwanese firms' own investments into mainland China technology sectors — constrains a natural capital source for China's AI/chip buildout. | WEB-862 | C |
| india-press-note-3-2026 | India Press Note 3 amendment (China-linked FDI) | national (India) | mandate | n/a | n/a | 2026-03-10 (Cabinet approval) | ongoing | n/a (inbound to India) | Non-controlling stakes ≤10% by China-linked capital via non-land-border vehicles now use automatic route; direct China-domiciled FDI remains under full approval-required curbs — govt explicitly denied broader relaxation. | WEB-859,WEB-860 | B |
| australia-firb-critical-minerals-2026 | Australia FIRB critical-minerals mandatory-notification reform | national (Australia) | mandate | n/a | n/a | 2026-05-19 | ongoing | L0/adjacent (rare earths feeding L3/L4/L9) | Critical-minerals investment made mandatory-notification; follows Jan-2026 A$14m penalty upheld against a China-linked investor defying a Northern Minerals forced-divestment order (17.58% combined stake ordered sold). | WEB-871 | B |
| china-foreign-ai-access-curbs-prospective | China prospective restriction on foreign access to AI models / foreign investors in AI firms | national (China) | plan (undecided, prospective) | n/a | n/a | 2026-07-07 (reported) | undecided — no timeline | L7 (models), all layers (investor access) | Reuters: Beijing met Alibaba/ByteDance/Z.ai to discuss curbing overseas access to advanced (incl. unreleased/open-weight) Chinese AI models, and separately weighed limits on which investors may back homegrown AI companies — a prospective China-side mirror of US OISP. Single-sourced, developing, unconfirmed. | WEB-873 | D |
| eo13959-cmic-index-removal | EO 13959 (amended EO 14032) — CMIC index-provider removals | national (US, globally propagated) | mandate | n/a | n/a | 2020-11-12 (EO); Jan-2021 (index removal effective) | ongoing | cross-layer | US executive order forced MSCI/FTSE Russell/S&P Dow Jones to strip "Communist Chinese Military Company"-designated names from global benchmark indices — a US-triggered channel that structurally divests non-US index-benchmarked capital too, regardless of the investor's home jurisdiction. | WEB-870 | B |

---

## 3. `metrics_timeseries.csv` — access-mechanics figures

| metric_id | entity | layer | metric_name | unit | period | value | source_id | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|
| china_a_share_fol | China (A-share market) | macro | Aggregate foreign ownership limit, A-shares | % | 2026 | 30 | WEB-869 | B | Applies to all foreign holders of any domicile equally. |
| msci_china_a_inclusion_factor | China (A-share market) | macro | MSCI China A inclusion factor | % of free float | 2026 | 20 | WEB-869 | B | Raised over time from an initial 5%; caps index-driven passive flow into China-A AI names even when "foreign-investable." |
| japan_gpif_aum | GPIF (Japan) | macro | Total AUM | $tn | 2025 | 1.87 | WEB-875 | C | ¥277tn; benchmark now excludes mainland China A-shares for 2025-2030 policy period. |
| temasek_china_exposure_change | Temasek (Singapore) | macro | YoY change in China exposure | $bn | 2025-2026 | 7.7 | WEB-863 | B | Largest one-year increase since 2021; explicitly AI-hardware/infrastructure/robotics-weighted. |
| gulf_swf_ai_deal_value_h1_2026 | Gulf SWFs (PIF+Mubadala/MGX+QIA) | macro | AI-related deal value, H1 2026 | $bn | 2026-H1 | 53.9 | WEB-864 | C | Across 108 deals; overwhelmingly into US labs/infrastructure — no confirmed direct China AI-stack IPO participation found. |
| australia_firb_divestment_penalty | Northern Minerals investor (China-linked) | macro | FIRB divestment-order non-compliance penalty | $A m | 2026-01-30 | 14 | WEB-871 | B | Federal Court penalty upheld against Indian Ocean International Shipping and Service Co. for defying a forced-divestment order. |
| taiwan_prc_control_threshold | Taiwan (regulatory) | macro | PRC-control identification threshold for Positive-List regime | % | 2026 | 30 | WEB-861 | C | Direct or indirect PRC ownership/control above this level triggers Taiwan's restrictive Positive-List regime, including disguised third-country routing. |
| japan_fefta_highrisk_threshold | Japan (regulatory) | macro | "High-risk foreign investor" notification threshold | % voting rights | 2026-05-29 | 1 | WEB-857,WEB-858 | B | vs. 50% standard threshold for ordinary foreign investors; category includes SWFs and (per commentary) Chinese investors. |
| india_pn3_noncontrol_threshold | India (regulatory) | macro | Automatic-route threshold for China-linked non-controlling stakes (via non-land-border vehicles only) | % | 2026-03-10 | 10 | WEB-859,WEB-860 | B | Does not apply to direct China-domiciled or majority-China-beneficial-owned investors, who remain under full approval. |

---

## 4. Sources (WEB-85x range)

1. [WEB-850] Sidley Austin, "EU Addresses Technology Leakage Through Outbound Investment Monitoring," 2025-02 — sidley.com/en/insights/newsupdates/2025/02/eu-addresses-technology-leakage-through-outbound-investment-monitoring — B
2. [WEB-851] A&O Shearman, "EU adopts mandatory foreign investment screening overhaul," 2026 — aoshearman.com/en/insights/eu-adopts-mandatory-foreign-investment-screening-overhaul — B
3. [WEB-852] Centre for European Reform, "Europe's door to Chinese tech investment is still ajar" — cer.eu/insights/europes-door-chinese-tech-investment-still-ajar — C
4. [WEB-853] Mayer Brown, "Shaping investments into EU strategic sectors: FDI Screening Reform and the Industrial Accelerator Act," 2026-03 — mayerbrown.com/en/insights/publications/2026/03/shaping-investments-into-eu-strategic-sectors-the-fdi-screening-reform-and-the-industrial-accelerator-act — C
5. [WEB-854] Skadden, "UK Proposes Updates to Scope of National Security and Investment Act Regime," 2026-03 — skadden.com/insights/publications/2026/03/uk-proposes-updates-to-scope-of-national-security — B
6. [WEB-855] Caixin Global, "Chinese Consortium Forced to Sell U.K. Chipmaker FTDI in National Security Crackdown," 2026-02-05 — caixinglobal.com/2026-02-05/chinese-consortium-forced-to-sell-uk-chipmaker-ftdi-in-national-security-crackdown-102411619.html — B
7. [WEB-856] Hogan Lovells / Lexology, "China and the UK National Security and Investment Act – Implications for Business and Investors," 2025 — hoganlovells.com/en/publications/china-and-the-uk-national-security-and-investment-act-implications-for-business-and-investors — C
8. [WEB-857] Orrick, "Japan Passes Major Reform of Foreign Investment Screening Regime Under FEFTA," 2026-06 — orrick.com/en/Insights/2026/06/Japan-Passes-Major-Reform-of-Foreign-Investment-Screening-Regime-Under-FEFTA — B
9. [WEB-858] Lexology, "Japan's 2025 FEFTA Amendments: Rules and Implications With a Focus on Investments by Chinese Investors" — lexology.com/library/detail.aspx?g=5e6022be-3f1e-40e0-9b3c-19834a4b4251 — B
10. [WEB-859] Carnegie Endowment for International Peace, "India's Press Note 3 Gamble: Opening the FDI Door to China," 2026-04 — carnegieendowment.org/research/2026/04/indias-press-note-3-gamble-opening-the-fdi-door-to-china — B
11. [WEB-860] India Briefing, "How India Press Note 3 Revision Unlocks China-Linked Capital in 2026" — india-briefing.com/news/how-india-press-note-3-revision-unlocks-china-linked-capital-2026-43449.html — C
12. [WEB-861] law.asia, "Taiwan's cross-border semiconductor controls: Export, security and investment regulations" — law.asia/taiwan-semiconductor-export-controls — C
13. [WEB-862] Digitimes, "Taiwan firms face tighter China investment scrutiny after new law," 2026-07-06 — digitimes.com/news/a20260706PD202/taiwan-investment-legal-business-beijing.html — C
14. [WEB-863] CNBC, "Singapore's Temasek boosts China exposure by $7.7 billion, biggest rise in five years, in AI-driven pivot," 2026-07-08 — cnbc.com/2026/07/08/temaseks-china-investment-jumps-most-in-five-years-artificial-intelligence-.html — B
15. [WEB-864] Forbes, "MGX's $49B AI Fund vs HUMAIN, Qai, GIC: Four Sovereign Bets," 2026-07-03 — forbes.com/sites/guneyyildiz/2026/07/03/abu-dhabis-49-billion-ai-fund-and-its-sovereign-rivals — C
16. [WEB-865] HKEX, "Stock Connect Frequently Asked Questions," version 2026-03-02 — hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Getting-Started/Information-Booklet-and-FAQ/FAQ/FAQ_En.pdf — B
17. [WEB-866] Shanghai Stock Exchange, "Stock Connect — Eligibility" — english.sse.com.cn/access/stockconnect/eligibility — B
18. [WEB-867] Norton Rose Fulbright, "China releases revised rules to ease investment through the QFII regime" — nortonrosefulbright.com/en/knowledge/publications/32e693be/china-releases-revised-rules-to-ease-investment-through-the-qfii-regime — B
19. [WEB-868] SEC EDGAR, Alibaba Group Holding Ltd, Form 20-F FY2026 (HFCAA/PCAOB risk factor) — sec.gov/Archives/edgar/data/0001577552/000119312526231755/baba-20260331.htm — A
20. [WEB-869] MSCI, "MSCI China A Inclusion Index" factsheet & consultation documents — msci.com/indexes/index/716566 — B
21. [WEB-870] SIFMA, "Amended Executive Order 13959: Issuers and Securities"; Wikipedia, "Executive Order 13959" — sifma.org/resources/guides-playbooks/executive-order-13959-issuers-and-securities ; en.wikipedia.org/wiki/Executive_Order_13959 — B
22. [WEB-871] Discovery Alert / McCullough Robertson, "Northern Minerals: Chinese Investors Face New Disposal Orders in 2026" and "Critical minerals update: FIRB Enforcement," 2026-05 — discoveryalert.com.au/northern-minerals-chinese-investors-disposal-orders-firb-2026 ; mccullough.com.au/2026/05/11/critical-minerals-update-firb-enforcements-and-us-australia-critical-minerals-framework — B/C
23. [WEB-872] CNBC, "MetaX, Moore Threads IPOs exploded, but it's not easy for foreigners to join the party," 2025-12-22 — cnbc.com/2025/12/22/metax-moore-threads-ipos-exploded-but-its-not-easy-for-foreigners-to-join-the-party.html — C
24. [WEB-873] Reuters, via Yahoo/Quartz/PYMNTS/Benzinga syndication, "China weighs restrictions on overseas access to its most advanced AI models" / "Beijing is looking at curbing overseas access to China's top AI models," 2026-07-07/08 — finance.yahoo.com/technology/ai/articles/exclusive-beijing-looking-curbing-overseas-101644780.html — D (single-sourced, developing; officials describe as undecided)
25. [WEB-874] CSIS, "Understanding U.S. Allies' Current Legal Authority to Implement AI and Semiconductor Export Controls" (EU lacks Entity-List equivalent); EU Sanctions Tracker / Global Sanctions, "China adds 7 EU companies to export control list," 2026-04 — csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export ; globalsanctions.com/2026/04/china-adds-7-eu-companies-to-export-control-list — C
26. [WEB-875] AsianFin, "Japan's $1.7 Trillion State Pension Fund to Exclude Investments in Onshore Chinese Shares" — asianfin.com/articles/126345 — C
27. [WEB-876] Merics, "New EU screening framework also targeting Chinese FDI is finally in place" — merics.org/en/comment/new-eu-screening-framework-also-targeting-chinese-fdi-finally-place — C

**Cross-referenced Pod-6 (v1) sources reused for context, not re-numbered:** WEB-635, WEB-636 (US Treasury OISP), WEB-637 (COINS Act), WEB-654 (Montage A/H premium reversal), WEB-661-664 (foreign access channels). See `research/pod6_policy_geopolitics_capital.md` §10 for full citations.
