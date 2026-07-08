# Pod 1 — Silicon & Equipment (L1: Semi Equipment/EDA, L2: Fabrication/Foundry)

**Analyst pod:** Pod 1 · **Date:** 2026-07-08 · **Data as-of:** mid-2026 unless noted
**Layers:** L1 (WFE, EDA, materials) + L2 (foundry, advanced packaging) + the export-control/EUV technical detail that binds both.

---

## 1. Scope

This memo covers China's semiconductor manufacturing stack from tool-building (L1: lithography, etch, deposition, cleaning, CMP, metrology, ion-implant, thermal; EDA software) through wafer fabrication and advanced packaging (L2: SMIC, Hua Hong, TSV/chiplet/CoWoS-analog capacity). It assesses the EUV chokepoint specifically (indigenous LPP/SSMB efforts, SMEE, the ~2028 domestic-prototype goal) and quantifies the cost/yield penalty of DUV-multipatterning workarounds. It closes with the investability read on the six named tickers in the brief (NAURA, AMEC, ACM, Empyrean, SMIC, Hua Hong) plus adjacent names (SiCarrier, Piotech, Kingsemi, Hwatsing, Primarius) that matter for the value-chain map.

## 2. Market structure & value chain

**WFE (wafer fab equipment).** China's own equipment vendors (NAURA, AMEC, ACM Research/Shanghai, Hwatsing, Piotech, Kingsemi) collectively held **~6.5% of the global $41.4bn WFE market in 2025**, up from 5.6% (2024) and 1.2% (2021) — a fast but still small share [WEB-010, C]. Domestically, self-sufficiency is highly uneven by segment as of Jan 2026 [WEB-009, C]:
- **Etch:** ~50–60% domestic (AMEC CCP etch qualified in TSMC 5nm/7nm lines; NAURA ICP etch qualified at SMIC 14nm) — most indigenized segment.
- **Cleaning:** ~50–60% domestic (ACM Research/Shanghai dominant).
- **Resist stripping:** >80% domestic, but only on mature lines.
- **Deposition (thin film/PVD-CVD-ALD):** ~20–30% domestic — a clear gap.
- **Lithography:** **0% domestic for EUV** (completely unavailable, blocked by Dutch export licensing); DUV is majority-foreign (ASML) with SMEE the only domestic scanner maker, confined to older nodes.
- Overall China equipment self-sufficiency reached **~35%** by Jan 2026 per one industry tracker [WEB-009, C], though the share of *China's own* WFE spend captured by NAURA/AMEC/ACM specifically is smaller and rising: ~20% (2025) → ~24% (2026E) → ~31% (2027E) [WEB-009, C].

A new entrant, **SiCarrier** (Shenzhen-government-backed, Huawei-linked, est. 2021), is attempting a "Huawei-style full-stack" WFE push spanning litho (subsidiary Zetop), photoresist (Cornerstone) and etch/deposition (Ueascend); it debuted a 5nm-capable etch tool at a Shanghai trade fair and was reportedly valued at ~RMB65bn (~$9bn) in Sept 2025, with ex-lithography revenue projected to rise from RMB4.5bn (2025E) to RMB7.5bn (2026E) to RMB16.9bn (2028E) [WEB-008, C/D — single-sourced, unlisted, treat projections as D]. SiCarrier is private/unlisted and not directly investable.

**EDA.** Global incumbents Synopsys, Cadence and Siemens EDA held **~78–80% of China's EDA market as of 2024** [WEB-019, C]. This became an acute chokepoint in **May 2025** when BIS ordered the "Big Three" to suspend software/support to Chinese customers and later required case-by-case licensing for all China EDA sales [WEB-011, C]. Domestic EDA has >100 companies but is led by **Empyrean Technology** (~half of the addressable domestic-vendor market; full-process-tool penetration among domestic fabless firms reached ~35%, up 22pp since 2020) and **Primarius Technologies** (SSE:688206), which has been consolidating the sector via M&A (acquired stakes in ACTT and Naneng Micro through 2025) [WEB-011, WEB-017, C]. Despite the tailwind, Empyrean's H1 numbers show the gap still binds economically: revenue +13% YoY to RMB501m but profit -92% to RMB3m [WEB-011, C] — indicative of heavy R&D spend to close functional gaps rather than of pricing power.

**Foundry/L2.** SMIC remains the sole domestic advanced-logic foundry at scale; its **N+2** process (roughly 7nm-class density) uses **self-aligned quadruple patterning (SAQP) on DUV immersion tools** in the absence of EUV, and the company is running 5nm pilot lines targeting mass production sometime in 2026 [WEB-013, C]. **Hua Hong**, via its Huali JV, is preparing a 7nm process at its Shanghai fab — which would make it China's second 7nm-capable fab after SMIC — targeting initial output of a few thousand wafers/month by end-2026 [WEB-006, C]. SMIC's 2026 capex guide is ~$8.1bn, roughly flat vs. $7.5bn in 2025, funding four new 12-inch fabs (Shanghai Lin-Gang, Shenzhen, Beijing, Tianjin) aimed mainly at ~340,000 wpm of **28nm-and-above** capacity — i.e., most of the incremental capacity is mature-node, not advanced-node [WEB-013, C].

**Advanced packaging.** This is now a co-binding constraint alongside lithography for AI-chip output. Tongfu Semiconductor has reportedly mastered 4nm-chiplet mass production, but **HBM packaging in China remains pre-mass-production** (tech reserve/customer-validation stage) as of mid-2026, even as CXMT is reported running ~60,000 wpm of HBM3-capable DRAM [WEB-015, C]. The China-vs-frontier gap in advanced packaging has reportedly narrowed from ~5 years (2022) to ~3 years (2025) [WEB-015, D].

## 3. Capability vs. global frontier (+ timeline)

| Sub-layer | China capability today | Global frontier | Gap | Timeline to parity |
|---|---|---|---|---|
| Litho (EUV) | None in production; lab-stage LDP source (Harbin Institute of Technology) reported at 100–150W mid-2025 vs. >250W needed for HVM; separate SSMB (synchrotron) effort at Tsinghua/Xiong'an targeting >1kW theoretical [WEB-007, D] | ASML NXE/High-NA EUV, HVM since 2019 (High-NA since 2024) | ~7–10 years, possibly longer for HVM-grade throughput | Government target: working chips off a domestic EUV **prototype** by ~2028 [seed: euv-2028, D] — plausible for a lab demonstration, NOT for volume manufacturing; treat 2028 as a prototype milestone, not a parity date |
| Litho (DUV, mature) | SMEE ships immersion DUV for older nodes; ASML DUV still dominant | ASML DUV (mature, decades of yield tuning) | Narrowing on mature nodes; wide on immersion-DUV-multipatterned advanced nodes | 3–5 years to close mature-node DUV gap; advanced-node DUV workaround already "works" but at high cost (see §4) |
| Etch/clean | AMEC/NAURA/ACM qualified into leading-edge lines (AMEC in TSMC N5/N7 tools); ~50-60% domestic share | Lam/TEL/AMAT/KLA | Narrow-to-moderate | 2–4 years for full domestic substitution in etch/clean |
| Deposition | ~20-30% domestic | AMAT/Lam/TEL ALD/CVD/PVD | Wide | 4–6 years |
| EDA | Domestic tools cover mature-node/analog flows; digital full-flow for advanced nodes still gapped | Synopsys/Cadence/Siemens | Wide, especially for advanced-node digital & verification | 5+ years — export ban accelerates substitution demand but not underlying tool maturity |
| Foundry (logic) | SMIC N+2 (~7nm-class), 5nm pilot 2026; yields 20-46% (advanced) [seed: metrics_timeseries] vs. 30-40% per other estimates [WEB-014, C] | TSMC N3/N2, EUV-based, >80% yield [seed] | 3–5 nodes equivalent (accounting for DUV penalty) | 5nm-class volume ~2026-27; true EUV-parity node (sub-3nm) likely 2030+ |
| Advanced packaging | Chiplet 4nm mastered (Tongfu); HBM packaging pre-mass-production | TSMC CoWoS (120-130k wpm by 2026) | ~3 years and narrowing [WEB-015, D] | 2027-28 for HBM-grade 2.5D at scale |

## 4. Moats & unit economics

- **AMEC/NAURA moat-in-formation**: breadth (NAURA) and etch-specific technical leadership (AMEC, founded by ex-Lam engineer Gerald Yin) give both pricing power *domestically* as SMIC/Hua Hong are directed toward local sourcing — but neither yet competes on cost or throughput internationally.
- **ACM Research's dual-listing arbitrage**: SSE:688082 (ACM Shanghai) trades at a large premium to the NASDAQ-listed parent ACMR because the A-share vehicle captures pure China-cleaning-equipment exposure investable domestically, while ACMR carries US-listing/export-control overhang; one analysis pegs the discount on ACMR to its ACM-Shanghai stake at ~64% [WEB-003, D/C].
- **The DUV-workaround economics are the central unit-economics story of the layer.** SMIC's N+2 (7nm-class) via SAQP-DUV reportedly requires ~34 lithography steps vs. 9 for an EUV-based equivalent process, runs at roughly **30x lower throughput** and **2-3x higher cost per wafer** than TSMC's EUV-based N3, with yields around **30-40%** vs. TSMC's >80% [WEB-014, C]; some estimates put SMIC 5nm wafer cost ~50% above TSMC's and yield as low as 33% [WEB-014, C]. This is the quantitative core of "the EUV gap is the most binding constraint" — it is not that China cannot print sub-10nm features at all, but that doing so without EUV destroys the cost structure and caps volume, which is precisely why Huawei/SMIC-linked Ascend chip supply remains rationed relative to demand (seed: china_aichips_produced 2m vs. demand >5m units, 2026, REF-SANDS-01/C).
- **EDA margin dynamics inverted by policy**: the export ban is a demand subsidy for Empyrean/Primarius, but near-term profitability is being sacrificed to R&D and M&A to close functional gaps (Empyrean profit -92% YoY even as revenue grew) — a classic "policy tailwind, margin compression" pattern investors should not mistake for near-term earnings power [WEB-011, C].
- **SiCarrier is the wildcard on moat formation**: state-backed, opaque financials, unlisted — its full-stack ambition (litho + photoresist + etch in one group) echoes Huawei's HiSilicon playbook and could compress the addressable market for NAURA/AMEC/ACM if scaled, but 2025-26 revenue (RMB4.5-7.5bn) is still a fraction of NAURA's scale.

## 5. Bottlenecks & dependencies

1. **EUV remains the single most binding chokepoint** for L1/L2 — confirmed unavailable to mainland fabs by Dutch export licensing, with no domestic HVM-capable substitute before the 2030s at the earliest [WEB-007, WEB-012].
2. **EDA advanced-node digital/verification flows** — despite the export ban accelerating substitution, Chinese fabless firms doing leading-edge digital design still lack a full domestic tool chain [WEB-011, WEB-019].
3. **Deposition tools** are the weakest WFE sub-segment (~20-30% domestic) — a second-order chokepoint behind litho.
4. **Advanced packaging / HBM integration** — pre-mass-production status in China threatens to become the new binding constraint for AI-chip output even if logic fabrication catches up, mirroring the global CoWoS bottleneck (TSMC CoWoS fully booked into 2026, Nvidia ~60% of allocation) [WEB-015, C].
5. **The 50% domestic-equipment mandate** (informal, unpublished decree; fab-expansion approvals reportedly rejected if under threshold) is real in effect but has case-by-case flexibility for advanced lines "where domestically developed tools are not yet fully available" — i.e., it binds hardest on mature-node fabs and is explicitly a floor en route to a 100% domestic long-term goal, not yet enforceable at the leading edge [WEB-018, C].
6. **Entity List overhang widening, not narrowing.** March 2025 additions included Shenzhen Naura Microelectronics Equipment Co. and SMIC Advanced Technology R&D (Shanghai), part of a 42-PRC-entity tranche [WEB-016, C]. A pending US legislative proposal (MATCH Act, H.R.8170) would extend multilateral controls and explicitly reference Hua Hong, SMIC, NAURA, AMEC and ACM Research, and would also ban ASML DUV shipments to China (~20% of ASML's 2026 revenue) [WEB-012, WEB-016, C]. Separately, US Commerce Secretary Lutnick raised concerns in mid-2026 that ASML EUV components may have reached China via indirect routing — an active investigation as of the data date, unresolved [WEB-012, C].

## 6. Named companies

| Company | Layer/segment | Ownership | Listing/ticker | Entity List | Foreign-investable | Global peer | Mkt cap (as of) | Role |
|---|---|---|---|---|---|---|---|---|
| NAURA Technology (北方华创) | L1 — etch/deposition/clean/thermal (broad WFE) | Listed-public | SZSE:002371 | Partial (subsidiary Shenzhen Naura Microelectronics Equipment added Mar-2025) | Restricted (A-share) | Applied Materials / Lam | ~CNY590bn / **~US$82bn** (2026-06-29) [WEB-001, C] | National champion |
| AMEC (中微公司) | L1 — plasma etch, MOCVD | Listed-public | SSE:688012 | Partial | Restricted (A-share) | Lam Research | **~US$29.8bn** (Apr-2026); 2026E revenue RMB15.7-15.9bn [WEB-002, C] | National champion, moat-in-formation |
| ACM Research (Shanghai) | L1 — wafer cleaning | Listed-public | SSE:688082 / NASDAQ:ACMR | No (ACMR parent); flagged risk given ACM Shanghai entity-list exposure noted in some filings | Restricted (A-share) / Yes (ACMR, but China-revenue-concentration risk) | SCREEN / Lam | ACMR **~US$6.4bn** (2026-06-26, volatile — was ~$3.1bn Mar-2026) [WEB-003, C] | Challenger, dominant in China wet-clean |
| Empyrean Technology (华大九天) | L1 — EDA | State-linked | SZSE:301269 | Partial | Restricted | Synopsys / Cadence | ~CNY45-70bn / **~US$7-10bn** (June 2026, wide variance across sources) [WEB-004, D] | National champion; policy-tailwind beneficiary |
| Primarius Technologies (概伦电子) | L1 — EDA (analog/parasitic extraction, consolidating via M&A) | Private/listed | SSE:688206 | n.a. (not confirmed) | Restricted | Synopsys / Siemens EDA | Not verified this cycle | Consolidator — absorbing ACTT, Naneng Micro (2025) [WEB-017, C] |
| SMIC | L2 — foundry (logic) | SOE-linked | HKEX:0981 / SSE:688981 | Yes | Restricted | TSMC | ~HKD702bn / **~US$90bn** (2026-05-15) [WEB-005, C] | National champion; Ascend foundry |
| Hua Hong Semiconductor | L2 — foundry (mature + emerging 7nm via Huali) | SOE-linked | HKEX:1347 / SSE:688347 | Partial | Restricted | UMC / GF / TSMC | **~US$23.5bn** (2026-03-18) [WEB-006, C] | Challenger, 2nd China 7nm line |
| SiCarrier | L1 — full-stack WFE (litho/photoresist/etch) | State/Huawei-linked | Private | Presumed high exposure (unconfirmed formal listing) | No | Applied Materials (aspirational) | ~RMB65bn est. (Sept-2025, D) | Emerging national champion, unlisted |
| Piotech / Kingsemi / Hwatsing | L1 — etch/deposition/CMP/cleaning niches | Listed-public | SSE-listed (various) | Not confirmed this cycle | Restricted | Lam/AMAT/TEL | Not independently verified | Second-tier domestic WFE — collectively (with NAURA/AMEC/ACM) ~6.5% of global WFE 2025 [WEB-010, C] |

*Global peers for benchmark (not China entities):* ASML ~$675bn (2026-06-26), Applied Materials ~$475bn (Jul-2026), Lam Research ~$464-493bn (Jun-2026), KLA ~$308-348bn (Jul-2026), Synopsys ~$84bn (Jul-2026), Cadence ~$103bn (Jul-2026) [WEB-020, C]. **Market-cap gap:** NAURA (~$82bn) vs. Applied Materials (~$475bn) is ~6x; AMEC (~$30bn) vs. Lam (~$480bn) is ~16x; Empyrean (~$8bn) vs. Synopsys+Cadence combined (~$187bn) is ~23x — the EDA cap gap is the widest of the layer, consistent with EDA being the least-indigenized sub-segment.

## 7. Investability read

- **NAURA and AMEC** are the cleanest pure-play, listed, large-cap exposure to China's WFE indigenization theme; both are A-share only (SZSE/SSE STAR), so **foreign portfolio access is restricted** to Stock Connect/QFII channels, and both carry partial Entity-List taint on subsidiaries — this constrains passive index inclusion and some ETF mandates but does not block A-share trading itself.
- **ACM Research** is the one name in this pod with a US-listed vehicle (NASDAQ:ACMR), making it the most foreign-accessible pure play, but that also means it is most exposed to US regulatory/export-control headline risk and has shown high market-cap volatility in 2026 (~$3.1bn to ~$6.4bn within a quarter).
- **Empyrean** is a policy-driven growth story with weak near-term profitability (margin compression from R&D/M&A) — best read as a multi-year option on EDA import substitution rather than a current-earnings story.
- **SMIC and Hua Hong** are H+A dual-listed, full Entity-List exposure, restricted to foreign investors via HK/Stock Connect only; SMIC's re-rating (+~49% over the trailing year per one data point) reflects AI-driven pricing power (Q2 2026 revenue guided +14-16% QoQ) even as advanced-node yields lag TSMC by a wide margin — the stock is trading on strategic-scarcity/national-champion premium as much as on fundamentals.
- **SiCarrier and Primarius** are not currently accessible to portfolio investors (private/thinly documented); watch for a future IPO as the clearest signal of how the government intends to monetize/scale the SiCarrier full-stack model.
- Basket framing: a "China WFE + EDA" basket (NAURA, AMEC, ACM-Shanghai, Empyrean, Piotech, Kingsemi, Hwatsing) is a levered bet on the 50%-mandate policy holding and on SMIC/Hua Hong capex continuing near $8bn/yr; a "China foundry" pair (SMIC, Hua Hong) is a bet on AI-chip pricing power outrunning yield/cost disadvantages.

## 8. Key figures

| Metric | Entity | Value | Period | Source | Confidence |
|---|---|---|---|---|---|
| China equipment vendors' share of global WFE market | NAURA+AMEC+ACM+Hwatsing+Piotech+Kingsemi | 6.5% (up from 5.6% in 2024, 1.2% in 2021) | 2025 | WEB-010 | C |
| China overall semiconductor-equipment self-sufficiency | China | ~35% | Jan-2026 | WEB-009 | C |
| China EDA market share held by Synopsys/Cadence/Siemens | China | ~78-80% | 2024 | WEB-019 | C |
| SMIC advanced-node yield (DUV multipatterned) | SMIC | 30-40% (vs. TSMC >80%) | 2026 | WEB-014 | C |
| SMIC 7nm-class cost/throughput penalty vs. TSMC N3 | SMIC | ~2-3x cost/wafer, ~30x lower throughput | 2026 | WEB-014 | C |
| SMIC 2026 capex guide | SMIC | ~$8.1bn (vs $7.5bn 2025) | 2026 | WEB-013 | C |
| ASML DUV share of 2026 revenue (China-exposed) | ASML | ~20% | 2026 | WEB-012 | C |
| Indigenous EUV LDP source power (lab) | China (HIT/SMEE/Huawei effort) | 100-150W (need >250W for HVM) | mid-2025 | WEB-007 | D |
| SiCarrier valuation | SiCarrier | ~RMB65bn (~$9bn) | Sept-2025 | WEB-008 | D |
| TSMC CoWoS capacity | TSMC (global benchmark) | 80k → 120-130k wpm | 2026 | WEB-015 | C |

## 9. Sources

1. **WEB-001** — NAURA Technology market cap/price data. stockanalysis.com, investing.com, Yahoo Finance (aggregated), accessed 2026-07-08, data as of 2026-06-29. Confidence: C.
2. **WEB-002** — AMEC market cap and 2026 revenue estimates. companiesmarketcap.com, Futunn analyst notes, accessed 2026-07-08, data as of Apr-2026. Confidence: C.
3. **WEB-003** — ACM Research / ACMR market cap, 2026 guidance, China-exposure analysis. companiesmarketcap.com, MacroTrends, ACM Research IR (Q4/FY2025 results release), Bamboo Works, SemiAnalysis newsletter, accessed 2026-07-08. Confidence: C.
4. **WEB-004** — Empyrean Technology market cap. Investing.com, Stock Events, Macroaxis, accessed 2026-07-08, data June 2026 (wide cross-source variance). Confidence: D.
5. **WEB-005** — SMIC market cap and Q1 2026 results. stockanalysis.com, Investing.com, accessed 2026-07-08, data as of 2026-05-15 / 2026-07-08. Confidence: C.
6. **WEB-006** — Hua Hong Semiconductor market cap and Huali 7nm Shanghai fab status. Eulerpool, Yahoo Finance, PitchBook, accessed 2026-07-08, data as of 2026-03-18. Confidence: C.
7. **WEB-007** — Indigenous EUV lithography progress (LDP source, SSMB project). blog.aifutures.org ("A forecast of Chinese DUV and EUV photolithography progress"); Tom's Hardware; FinancialContent, accessed 2026-07-08. Confidence: D.
8. **WEB-008** — SiCarrier company profile, valuation, revenue projections. SCMP, TrendForce, TechInsights, DigiTimes, Wikipedia, accessed 2026-07-08. Confidence: C/D.
9. **WEB-009** — China WFE self-sufficiency by segment. TechWireAsia, EE Times ("How China Struggles to Reach WFE Self-Sufficiency"), Wedbush investor note, accessed 2026-07-08, data as of Jan-2026. Confidence: C.
10. **WEB-010** — Piotech/Kingsemi/Hwatsing 2026 revenue and collective China-vendor global WFE share. NineScrolls, SCMP, 24/7 Wall St., accessed 2026-07-08. Confidence: C.
11. **WEB-011** — EDA export restrictions (BIS May-2025 order) and Empyrean/Primarius response. SCMP (x2), Yicai Global, EE Times, TrendForce, accessed 2026-07-08. Confidence: C.
12. **WEB-012** — ASML China export-control status, MATCH Act, EUV-component investigation. TechCrunch, CNBC (x2), Tom's Hardware, MarketWise, Motley Fool, accessed 2026-07-08. Confidence: C.
13. **WEB-013** — SMIC 2026 capex/capacity guidance. TrendForce ("SMIC 2026 Action Plan"), Yole Group, Tiger Brokers/CITIC SEC note, accessed 2026-07-08. Confidence: C.
14. **WEB-014** — DUV multipatterning cost/yield penalty quantification. EE Times, abhs.in blog analyses, TrendForce, accessed 2026-07-08. Confidence: C (cross-corroborated across independent estimates, but underlying figures are analyst estimates, not company-disclosed).
15. **WEB-015** — Advanced packaging / CoWoS / HBM China status. Oplexa, SupplyICs, GlobalSMT, Silicon Analysts, accessed 2026-07-08. Confidence: C/D.
16. **WEB-016** — Entity List additions and MATCH Act (H.R.8170) text. Federal Register (2025-05427), Congress.gov, DigiTimes, accessed 2026-07-08. Confidence: C (primary/gov source for Entity List; C for bill text pending passage).
17. **WEB-017** — Primarius Technologies ticker, M&A activity, 2025 results. Futunn, DigiTimes, Crunchbase, accessed 2026-07-08. Confidence: C.
18. **WEB-018** — 50% domestic equipment mandate mechanics and exemptions. Yahoo Finance (Reuters-sourced "Exclusive"), Tom's Hardware, Modern Diplomacy, accessed 2026-07-08. Confidence: C.
19. **WEB-019** — China EDA market share by vendor. SemiAnalysis newsletter ("EDA Market Primer"), 36kr, accessed 2026-07-08, data as of 2024. Confidence: C.
20. **WEB-020** — Global peer (ASML/AMAT/Lam/KLA/Synopsys/Cadence) market caps. companiesmarketcap.com, statista, stocktwits, accessed 2026-07-08, data late-June/July 2026. Confidence: C.

**Major uncertainties / things NOT independently verified this cycle:** exact current market caps for Piotech (SSE:688072), Kingsemi and Hwatsing individually; Empyrean's precise market cap (sources disagreed by ~35% within the same week); whether Primarius carries any Entity List flag; the authenticity/scale of the SiCarrier valuation and revenue figures (single-sourced, unlisted company, no audited disclosure); whether the ASML EUV-component-reached-China allegation is substantiated (active/unresolved investigation as of data date). All figures above should be treated as directional given the fast-moving policy and market environment in 2026.
