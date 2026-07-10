# Red-Team Review — v2 Pods P1–P6

**Reviewer:** adversarial research reviewer · **Date:** 2026-07-10
**Scope reviewed:** `v2_p1_hyperscalers.md`, `v2_p2_model_econ.md`, `v2_p3_demand_priced.md`, `v2_p4_talent.md`, `v2_p5_global_reg.md`, `v2_p6_refdata.md` (+ data files), cross-checked against `report/China_AI_Stack_Report.md`, `database/company_master.csv`, `database/RECONCILIATION.md`, and v1 pods.
**Method:** source-quality assessment of every load-bearing claim; spot web-verification of the four highest-risk / most surprising figures (Biren ticker, CXMT financials, Innolight CSI-300 weight, Zhipu market cap). This is a triage of the most consequential claims, not an exhaustive log.

**Headline:** The v2 batch is, on the whole, unusually disciplined about confidence grading and about admitting what it could not verify (MT_Newswires unavailable; multiple 403s honestly disclosed). The single genuine **must-fix** is a factual ticker contradiction inside the batch (P5 vs P6 on Biren). Most other challenges are hedging/over-precision refinements, not corrections. Four surprising headline claims that I spot-verified all held up.

---

## Challenge Log

| # | Claim (short) | Location | Grade claimed | Issue | Recommended action | Severity |
|---|---|---|---|---|---|---|
| 1 | Biren ticker **HKEX:6844** | P5 §4 matrix + `company_master` | B (P5) | **Wrong ticker.** Verified real ticker is **HKEX:6082** (Shanghai Biren Class H). P6 (same v2 batch) independently and correctly flags 6082; Pod3(v1) had 9668; master has 6844. Three different values in-program. | **VERIFY→correct to 6082** in P5, master, Pod3; adopt P6's finding | **High** |
| 2 | Zhipu market cap "peaked above HK$1tn" | P2 (Moats), pod4 | C | **Correct** — verified HK$1tn on 2026-06-22 (GLM-5.2 surge). But `company_master` still carries stale HK$585.8bn/~$75bn (Jun-2026) and P6 cites a HK$400bn press headline. Pod is right; DB is stale/contradictory. | KEEP pod claim; **update master** to reconcile | Med |
| 3 | Zhipu "follow-on **$4bn** raise in July 2026" | P2 (Moats) | C (per v1) | Verified public reporting shows a **~US$560m** Zhipu share placement (HK$1,588/sh), not $4bn. $4bn looks like an error carried from v1. | **VERIFY / correct or cut** the $4bn figure | Med |
| 4 | CXMT "IPO **valuation guidance** CNY2–3tn (~$280–420bn)" | P3 matrix + §domestic table; Pod2 | C / D | Figure magnitude is now defensible (H1 profit guide RMB57bn → 20× ≈ RMB2–3tn). But calling it official "valuation **guidance**" over-states what is analyst-estimate dispersion. Master frames the RMB2–3tn end as D bull-case. | **HEDGE** wording ("analyst valuation range," not "guidance") | Med |
| 5 | CXMT H1-26 net profit **RMB50–57bn**; global DRAM share **~7.7%** | P3 matrix; Pod2 | C | Profit figure **VERIFIED** (RMB57bn 1H guide corroborated across sources) — not confabulation. But internal tension: H1 revenue guide RMB110–120bn (~$17.6bn) annualizes to ~$35bn, hard to square with a "7.7% global share" (a stale 4Q25 unit-share). Both traced to single source chain (WEB-001/019). | KEEP figures; **HEDGE** the share/revenue juxtaposition; note 7.7% is 4Q25 unit-share | Med |
| 6 | Alibaba FY2026 FCF **-RMB46,609m** (first negative) | P1 (funding, key figures) | C | The entire "self-funding is ending" thesis rests on a **C-grade aggregator (StockTitan) summary** of the 6-K, while the capex input (RMB126,063m) is A. Load-bearing narrative on second-hand FCF. | **VERIFY** FCF directly in the SEC 6-K (source [2]) | Med |
| 7 | Alibaba group adj. net profit **-99.7% YoY to RMB86m** (Mar qtr) | P1 (non-AI drag) | B (co. release) | Dramatic single figure driving the "two capital wars" narrative. B-grade but arresting enough to deserve a direct-filing confirm before it headlines the report. | VERIFY (light) | Low |
| 8 | Innolight = **CSI 300 top weight ~5.0%**, overtaking CATL | P6 (CSI 300); P3 | C | **VERIFIED** (Bloomberg/SCMP: 5.0–5.3%, top constituent Jun-2026, CATL 4.1%). Striking but true. | KEEP | — (solid) |
| 9 | MSCI China: Tencent **13.35%** + Alibaba **10.17%** = 23.52%; HSTECH SMIC **9.54%** + Tencent 8.35% | P6 | C | Every index weight in P6 is search-engine-mediated (all provider PDFs 403'd) — pod is transparent about this. Plausible and internally consistent, but **no weight is primary-verified**; precise decimals imply more certainty than the sourcing supports. | KEEP with the pod's own C caveat; avoid quoting 2-decimal precision as fact in the report | Med |
| 10 | DeepSeek revenue estimates span **$13.4m–$1.1bn+** (80–100×) | P2 (Moats, bottlenecks) | D (flagged hard) | Exemplary handling — the spread is presented as evidence of *unknowability*, not a range. | KEEP | — (solid) |
| 11 | Zhipu FY2025 rev **RMB724.33m**, net loss **RMB4.72bn** (~6:1) | P2 | B headline / C segment | Headline sourced to filed annual report via press (SCMP/Yicai/Bloomberg), segment mix explicitly downgraded to C. Correctly disciplined. | KEEP | — (solid) |
| 12 | MiniMax FY2025 rev **$79.0m**, net loss **$1.87bn** | P2 | B (co. press release) | Loss is ~24× revenue; pod correctly notes it is "substantially IPO-related valuation/share-based adjustments," not cash burn. Reasonable. | KEEP (ensure report repeats the adjustment caveat) | Low |
| 13 | Moonshot ARR "$100m (Mar) → $200m+ (Apr-2026)"; valuation to $30bn talks | P2 | D | Single unnamed-source ARR; ~100–150× ARR multiple flagged. Honestly D. | KEEP as D | Low |
| 14 | Baidu "AI Applications revenue **RMB2.5bn, ~flat YoY**" despite 200m+ MAU | P2; P1 | B (6-K) | Best primary-source monetization-gap datapoint in the batch. | KEEP | — (solid) |
| 15 | OpenClaw: renamed Clawdbot→Moltbot→OpenClaw; ~250–350k GitHub stars; creator → OpenAI | P2 | C/D | High confabulation surface (precise naming history, star counts, personnel move), but tangential to any investment thesis and hedged. Star count is D (347k vs 250–350k spread). | KEEP but treat star count / naming detail as D; don't foreground in report | Low |
| 16 | GATT: **72%** of China-educated elite researchers work in US, **11%** stay; **38%** China-undergrad share | P4 §2 | C | Load-bearing headline numbers relayed **second-hand** (MacroPolo site 403'd → via MIT Tech Review). Named/primary methodology but not directly checked; figures also shift across GATT versions. | KEEP at C; flag "relayed, not primary-verified" in report | Low |
| 17 | Stanford AI Index: China **23.2%** of AI publications; migration into US **-89%** since 2017 | P4 §3, §2 | C | Same second-hand-relay issue (HAI PDF 403'd → via Fortune). Honestly graded. | KEEP at C | Low |
| 18 | China semiconductor/EDA talent gap **200k–300k**; sub-5nm design leads "<100 nationally" | P4 §4 | D | Recruiter-estimate, not audited; pod says only the direction is reliable. Correct posture. | KEEP as D | Low |
| 19 | AMEC etch tools qualified into **TSMC 5nm/7nm**, >100 fabs | P3 (domestic split); Pod1 | D | Single-sourced to AMEC/press, **unconfirmed by TSMC**; pod explicitly refuses to build any valuation on it. Correct handling. | KEEP as D; do not upgrade | Low |
| 20 | Japan **GPIF** excludes China A-shares from benchmark 2025–2030 | P5 §2 | C | Consequential "bellwether" claim; C-grade (one source). Plausible; would benefit from a second source before the report leans on it. | VERIFY (light) | Low |
| 21 | China contemplating curbs on **foreign investors backing homegrown AI cos** | P5 §3, §7; also cross-ref | D (single Reuters, 7-Jul-2026) | Correctly flagged as the single biggest tail-risk AND as single-sourced/undecided. Good discipline. | KEEP as D; do not let it harden into a base-case in the report | Low |
| 22 | Combined US-hyperscaler 2026 capex **$700–725bn** (+77%) | P1 | C (Goldman via press) | Fine as a C-grade sizing figure; note the four-vs-five-company scope ($700bn incl. Oracle in one source) so the comparison base to Chinese majors stays apples-to-apples. | KEEP; footnote scope | Low |
| 23 | Alphabet **$84.75–90bn** equity raise for AI capex (Jun-2026) | P1 | A/B (SEC 8-K + Bloomberg) | Properly sourced to the primary filing event. | KEEP | — (solid) |
| 24 | Iluvatar market cap **~$25.6bn** (in P5/P6 universe, from master) | `company_master`/Pod6 (D); appears in P5 matrix scope | D | Not a v2-pod headline claim, but implausibly high vs peers (Biren $6bn, MetaX $5.2bn, Moore $7.5bn) for a co. that raised ~$475m. Master already flags D. | FLAG for DB scrutiny (out of P5/P6 authorship scope) | Low |
| 25 | MetaX ticker: P5 "TBD" vs P6 "**SSE:688802**" | P5 vs P6 | C | Minor intra-batch inconsistency; P6's confirmed ticker should propagate. | Reconcile to 688802 | Low |

---

## Solid core (well-supported — trust these)

- **Alphabet's $84.75–90bn June-2026 equity raise** for AI capex (P1) — sourced to SEC 8-K/FWP; the batch's cleanest A/B external-financing datapoint.
- **Baidu "AI Applications revenue RMB2.5bn, ~flat YoY" despite 200m+ Ernie MAU** (P1/P2) — primary 6-K line item; the single best adoption-vs-monetization-gap evidence in the program.
- **Zhipu & MiniMax filed financials** (P2) — RMB724m rev / RMB4.72bn loss and $79m rev / $1.87bn loss; correctly separated into B-grade headlines vs C-grade segment splits.
- **DeepSeek revenue "$13m–$1.1bn, unknowable" handling** (P2) — model example of "market share ≠ revenue" discipline the v2 brief demanded.
- **Innolight = CSI 300 top weight ~5.0%** (P6) — independently verified; a genuinely striking, true concentration signal.
- **Biren correct ticker 6082** (P6) — P6 caught a real error in the master and in P5.
- **CXMT Q1/H1 financials** (P3/Pod2) — extraordinary figures (RMB50.8bn Q1 rev, RMB57bn H1 profit guide) corroborated across multiple independent sources; real, not confabulated.
- **WIPO PCT patent counts** (P4) — 73,718 vs 52,617; named primary statistical source, B-grade.
- **ACM Research "substantially all revenue from mainland China" (10-Q)** (P3) — the one filed, B-grade domestic-substitution split.
- **OISP passive-investment-exemption refinement** (P5) — correctly softens v1's over-categorical "US persons excluded," a real improvement on v1.
- **The two excluded aggregator errors** (Cambricon "$1.79bn 2026 rev", Hua Hong "$5bn consensus") in P3 — active confabulation-catching, exactly the v2 posture.

---

## Must-fix before publish (High severity)

1. **Biren ticker (Challenge #1).** P5's matrix and `company_master` use HKEX:6844; the verified ticker is **HKEX:6082** (P6 is correct). Program currently carries three different Biren tickers (6844 / 9668 / 6082). Correct to 6082 everywhere before any table with Biren ships. This is the one unambiguous factual error in the batch and it is in a reference field an investor would act on.

*(No other item rises to High. Items #2–#6 — Zhipu $4bn raise, Zhipu master staleness, CXMT "guidance" wording, CXMT share/revenue tension, Alibaba FCF sourced from an aggregator — are Medium: fix wording/sourcing, but none is a load-bearing thesis breaker.)*

---

## Verdict by pod

- **P1 Hyperscalers — fit to integrate with minor fixes.** Strong on the disclosure-asymmetry and funding-trajectory thesis; the one soft spot is that the marquee "Alibaba FCF turned negative" claim rests on a C-grade aggregator rather than the A-grade 6-K it cites alongside (#6). Verify that one figure; ByteDance D-grades are honestly bounded.
- **P2 Model econ — fit to integrate, strongest-disciplined pod.** Exemplary separation of token-share from revenue and of B vs D sources. Fix the stray **$4bn** Zhipu raise (#3) and keep OpenClaw detail (#15) out of the report's load-bearing spine.
- **P3 Demand & priced-in — fit with fixes.** Excellent confabulation hygiene (excluded two aggregator errors). Soften CXMT "valuation guidance" wording (#4) and flag the CXMT revenue-vs-share tension (#5); consensus figures are honestly C/D throughout given the MT_Newswires gap.
- **P4 Talent — fit as-is (context, not pricing).** Best-graded pod for confidence discipline; every headline is appropriately C/D and the flow-vs-stock and volume-vs-quality distinctions are handled well. Only caveat: the load-bearing GATT/Stanford numbers are second-hand relays (#16/#17) — label as such.
- **P5 Global reg — fit with ONE required fix.** Analytically the sharpest refinement of v1 (US-is-the-outlier). But it must inherit P6's Biren 6082 correction (#1) and MetaX ticker (#25). China-side curb risk (#21) is well-flagged as D.
- **P6 Refdata — fit as-is on findings, with a standing caveat.** Caught the Biren error, and its two spot-verified headline claims (Innolight CSI-300, index-concentration thesis) held up. The standing caveat is structural and honestly disclosed: **zero index weights are primary-verified** (all provider PDFs 403'd) — so 2-decimal weights should not be quoted as hard fact in the report.

## Overall verdict

**Fit to integrate with fixes.** No pod needs re-research. One High-severity factual correction (Biren ticker → 6082) is mandatory; a handful of Medium wording/sourcing fixes (Zhipu $4bn raise, Zhipu master staleness, CXMT "guidance" phrasing, Alibaba FCF aggregator-sourcing) should be cleared before the numbers headline the report. The batch's defining strength is confidence honesty — it repeatedly flags its own D-grades and unverifiable private-company financials rather than laundering them into false precision, which is exactly what the v2 hardening mandate asked for.
