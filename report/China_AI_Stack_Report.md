# The Stack China Is Building
### A Value-Chain Map of China's Indigenous AI Ecosystem

*Flagship research report · Data as-of mid-2026 · Audience: financial-market experts, economists, industry analysts*

> **Confidence discipline.** Every quantitative claim traces to the evidence database (`/database/`) with a source ID and an A–D confidence grade (A = filed/audited · B = primary disclosure · C = credible third-party · D = single-source / estimate). In a sector re-rating this fast, treat 2026 point figures — especially pre-listing valuations and private-company numbers — as provisional. Cross-source conflicts are documented in `/database/RECONCILIATION.md` rather than smoothed over.

---

## Executive summary

**The thesis in one line.** China is building a parallel, vertically-indigenized AI stack under export-control pressure; it is one to several years behind the US frontier at almost every layer, but the *direction, coordination, and capital* behind the build-out are creating a distinct investable ecosystem whose value is migrating from where investors still look (consumer internet) to where the work is actually happening (equipment, memory, compute, interconnect, power, and embodied AI).

**Seven things a professional investor should take away:**

1. **The binding constraint is lithography, and it is not close to resolved.** Without EUV, SMIC's 7nm-class (N+2) line runs at ~30–40% yield vs. TSMC's >80%, ~2.5× cost/wafer, and ~30× the lithography steps (WEB-014, C). Every downstream ambition — more Ascend chips, indigenous HBM — is rationed by this one chokepoint. The indigenous-EUV "2028 goal" is realistically a lab-prototype milestone, not volume parity (WEB-007, D).

2. **China's answer to a chip-level deficit is a system-level bet.** Huawei's Ascend 910C is ~60% of an H100 on inference (WEB-028, C), but CloudMatrix / Atlas 950 rack-scale designs lash together up to 8,192 NPUs (16 PB/s aggregate interconnect) to compete with Nvidia's GB200 NVL72 at the rack — at ~4× the power (metrics L4/L5, C). "Lose at the chip, win at the rack, pay for it with electricity."

3. **Power is China's one unambiguous structural advantage.** China generates ~10,000 TWh/yr vs. the US ~4,600 (WEB-001, C), added +1,840 GW of wind+solar (2025), and is engineering curtailment arbitrage into data centers. If — and only if — domestic silicon closes the compute gap, latent power lets the build-out run faster than most Western models assume (a conditional, D-grade inference, not a fact).

4. **The software moat (CUDA) is the deepest, slowest-closing gap** — 3–5+ years — even as Huawei open-sources CANN and Chinese labs (DeepSeek, Zhipu) demonstrate frontier training on domestic silicon.

5. **The capital-markets regime is the real 2026 catalyst.** A deliberate "slow-bull" equity policy (since Sept-2024) has produced an IPO cluster — Zhipu, MiniMax, Biren, Iluvatar and Montage's H-share all listing within ~5 weeks; Moore Threads/MetaX STAR debuts up +468%/+693% day-one — turning national champions into public, tradeable, and often extremely richly-valued securities.

6. **Investability ≠ listing.** The highest-momentum names (Moore Threads, MetaX, Biren, Kunlunxin) sit on the US Entity List and, increasingly, Treasury's outbound-investment (OISP) net — trading freely in Shanghai/Hong Kong yet **effectively closed to US capital**. The cleanest foreign-investable exposures are the platform incumbents (Alibaba, Tencent) and a handful of un-listed-constraint names (Montage, CATL).

7. **The valuation structure is policy-driven, not earnings-driven.** Cambricon briefly crossed a RMB 1tn market cap (first STAR company to do so) on ~$0.9bn revenue; CXMT's July-2026 STAR IPO prices the company at **~RMB 295bn** yet the market expects a **RMB 2–3tn** cap post-pop — a ~7–10× subscription-to-trading spread that quantifies the re-rating. This is a market pricing *captive demand and national-champion sponsorship*, not current cash flows — the opportunity and the risk are the same fact.

**How to read the map.** Sections 3.0–3.9 walk the stack bottom-up; each layer resolves into market structure → capability vs. the global frontier (with a timeline) → moats & economics → bottlenecks → named players → an investability read. Section 5 synthesizes: where value is captured, a China-vs-US scorecard, the stack-mapped basket, scenarios, and risks.

---

## 1. Why China's AI stack is its own investment universe

**Two doctrines.** US frontier labs treat AI as a race to superintelligence, where a few months' lead may compound into permanent advantage; the effort concentrates on the frontier model. China treats AI as *infrastructure* — like electricity, water, or the internet — to be diffused across the whole economy, with a pronounced tilt toward the physical world (manufacturing, robotics) where China is already dominant (REF-BW-03). This is not merely rhetorical: it shapes where capital goes (systems and diffusion, not only frontier training), what "winning" looks like (90% economy-wide AI penetration targeted by 2030; ~70% by 2027 — L8 metrics, C), and why China tolerates a chip-level deficit while racing on rack-scale systems, power, and embodied AI.

**The self-sufficiency imperative.** US export controls — on advanced chips, EUV lithography, HBM, and semiconductor equipment — reframed every foreign dependency as a weaponizable vulnerability. China's response is to indigenize *every* choke point. This is the origin of the investment opportunity that Sands Capital and Bridgewater both identify: policy manufactures **captive domestic demand** and **national-champion sponsorship** for any firm that can climb the technical curve. The corollary, per Bridgewater, is that this is a *diversifying* bet — the indigenous names do not price off the global AI supply chain, because their fortunes turn on Chinese policy and domestic substitution, not on Nvidia's order book.

**The macro backdrop (context).** China's economy is deliberately uneven: a ~4.5% headline growth target (about half the high-growth-era pace), weak property and consumption, but hyper-competitive strategic-export industries and a top-down reallocation of fiscal and financial resources toward AI, robotics, and the industrial build-out (REF-BW-03). The same mercantilist dynamic that pressures Europe and fuels the global tariff cycle is what funds the AI stack. For allocators, Chinese AI equities are attractive less as a growth-beta play than as a **diversifier** with a policy put ("slow bull") beneath the equity market.

---

## 2. The macro frame: compute supply–demand and the capex cycle

**A low base.** Bridgewater's triangulation puts total compute accessible to Chinese AI firms at ~3.8 GW (including capacity housed abroad), of which ~2.5 GW is available for inference (~65% split) — a fraction of the major US labs' fleets (C→D, REF-BW-01). The supply gap is stark at the device level too: the US and allies consume ~12m AI chips/year; China produces ~2m domestically against demand that may already exceed 5m (REF-SANDS-01, C).

**The squeeze is showing up in prices.** After years of aggressive discounting, Alibaba, Baidu and Tencent all *raised* AI-compute list prices in 2026, and Chinese model vendors priced their latest flagships *above* predecessors — behavior consistent with compute (not demand) as the binding constraint (REF-BW-01). Zhipu, in its first post-IPO print, named compute capacity as the limiting factor on its business.

**The capex response is captive.** The 15th Five-Year Plan (Mar-2026) elevated AI to the primary national objective; a draft ~$295bn national AI data-center grid mandates ≥80% domestic technology (L6 metrics, B/C). Because policy guarantees demand, the domestic build-out does not face the demand uncertainty that haunts early-stage tech elsewhere — the risk migrates from "will there be customers?" to "can the technology scale?" That is the single most important reframing for valuing these names.

**The efficiency offset.** Chinese models are unusually compute-efficient in inference (DeepSeek's architecture work is the emblem), partially offsetting the hardware deficit. Even doubling the effective compute requirement, China's inference fleet remains well below the US majors' — but the gap in *deliverable intelligence* is narrower than the raw GW gap implies.

---

## 3. The stack, layer by layer

### 3.0 Energy & Power (L0)

**Market structure.** The one layer where China leads outright. Generation ~10,000 TWh (2024) vs. US ~4,600, +~500 TWh added in 2025 alone (WEB-001, C). Installed data-center capacity ~32 GW (2025), forecast to ~40 GW (2026) and ~60 GW (2030) (Rystad, WEB-002, C). A $580bn 15FYP grid-capex program and 15 new UHV lines move power from the renewable-rich west to demand centers (WEB-005, C). Wind+solar installed base hit ~1,840 GW in 2025, surpassing thermal for the first time (WEB-024, C).

**The arbitrage.** Curtailed renewables (solar ~9.2%, wind ~8.5% early-2026) are being routed into data centers via the "East-Data-West-Compute" program (63% hub occupancy; ~$33bn cumulative investment) (WEB-003/004, C). Green-DC policy targets PUE ≤1.25 and ≥80% renewable sourcing for new builds (WEB-023).

**Capability vs. frontier / the conditional edge.** The US faces a *power ceiling*: data-center demand ~31 GW (2025) → ~66 GW (2027), with a forecast ~49 GW delivery shortfall by 2028 (Morgan Stanley/Grid Strategies, WEB-021, D). China faces no such near-term ceiling. **But** abundant power is necessary, not sufficient: the payoff to China's energy advantage is *gated on domestic silicon* closing the compute gap (L1/L3/L4). This is the report's central conditional — a D-grade inference, not a citable fact.

**Investability.** State Grid is unlisted (uninvestable). The cleanest listed proxy is **CATL** (SZSE:300750 / HKEX:3750, ~$420bn; grid-storage revenue ~$8.6bn, 121 GWh shipped 2025) — foreign-investable, no Entity-List flag. Nuclear (110 GW target by 2030) and the UHV/grid-equipment complex are secondary plays for a dedicated pod to size.

### 3.1 Semiconductor equipment & EDA (L1)

**Market structure.** A broad domestic roster is climbing segment by segment: **NAURA** (SZSE:002371, ~$82.5bn) is the breadth champion (etch, deposition, clean, thermal); **AMEC** (SSE:688012, ~$29.8bn) the etch specialist with a genuine world-class ambition; **ACM Research** (SSE:688082 / NASDAQ:ACMR, ~$6.4bn) in cleaning; plus Piotech (deposition), Kingsemi (track/coat), Hwatsing (CMP). In EDA, **Empyrean** (SZSE:301269) and Primarius (SSE:688206) anchor a consolidating sector. **SMEE** (state, unlisted) carries the lithography burden, and **SiCarrier** (Huawei-linked, unlisted, ~$9bn est., D) is the wild-card full-stack entrant.

**Capability vs. frontier.** Overall equipment self-sufficiency ~35% (Jan-2026, C), but wildly uneven: etch and clean ~55%, deposition only ~25% (the weakest major sub-segment), and lithography/EDA the widest gaps. Collectively, Chinese WFE vendors are still only ~6.5% of the *global* WFE market (up from 1.2% in 2021) (WEB-009/010, C→D). EDA is the widest gap by market value — Empyrean+Primarius vs. Synopsys+Cadence is a ~20×+ mismatch — and the May-2025 US EDA ban acted as a demand subsidy: Empyrean's H1 revenue grew but profit fell ~92% on import-substitution spend (WEB-011, C).

**EUV, quantified.** The indigenous LPP light source measured ~100–150W mid-2025 vs. >250W needed for high-volume manufacturing; a separate SSMB/synchrotron effort at Tsinghua/Xiong'an is years from product (WEB-007, D). Read the 2028 target as a lab demo. Meanwhile DUV multipatterning imposes the ~2.5× cost and ~30–40% yield penalty that rations everything above it.

**Moats & economics.** Two moat types: AMEC's *process-knowledge compounding* (every wafer run improves the next tool — not purchasable, not reverse-engineerable), and NAURA's *breadth-as-lock-in* (a fab qualified on NAURA across four process steps faces years of switching cost). The 50% domestic-equipment mandate for new fabs converts these into near-guaranteed order books (WEB-018, C).

**Investability.** All the pure-plays are A-share/STAR listed and **Stock-Connect/QFII-restricted** for foreign capital; NAURA's subsidiary and SMIC R&D units were added to the Entity List in Mar-2025, and the proposed MATCH Act names NAURA/AMEC/ACM/SMIC/Hua Hong explicitly (WEB-016, C). ACMR (the US-listed parent line) is the one partial exception. Net: high strategic conviction, constrained access.

### 3.2 Fabrication & advanced packaging (L2)

**Market structure.** Two national champions: **SMIC** (HKEX:0981 / SSE:688981, ~$90bn) and **Hua Hong** (HKEX:1347 / SSE:688347, ~$23.5bn). SMIC runs the 7nm-class (N+2) line that fabs Huawei's Ascend; Hua Hong's Huali JV targets initial 7nm output (a few thousand wpm) by end-2026, which would make it China's second advanced-node line.

**Capability vs. frontier.** Stuck at 7nm-class for the foreseeable future without EUV; 5nm-class exists only in pilot and at punishing yield. SMIC's advanced-node yield ~20–46% (cross-checked ~35%) vs. TSMC >80% (C). 2026 capex ~$8.1bn, mostly for *mature*-node expansion (~340k wpm across four new fabs) — capacity, not frontier. Advanced packaging (TSV, CoWoS-analogs, hybrid bonding) is a co-binding constraint, ~3 years behind the frontier (WEB-015, D) and pivotal to any indigenous HBM.

**Economics & investability.** Foundry is the scarce shared resource behind nearly every L4 chip vendor — SMIC capacity is the system chokepoint, and China's own 5× 7nm-and-under capacity target by end-2027 is already constraining 2026 shipment plans. Both are dual-listed (HK + STAR); SMIC is Entity-Listed. HK lines offer the most (still-restricted) foreign access.

### 3.3 Memory — DRAM / NAND / HBM (L3)

**Market structure.** **CXMT** (DRAM; global share risen to ~7.7%, #4 behind Samsung/SK hynix/Micron) and **YMTC** (3D NAND; ~14.5% share) are the two champions, both pivoting toward the AI memory stack. CXMT's Q1-2026 was a coming-of-age print, confirmed in its **STAR IPO prospectus**: **RMB 50.8bn revenue (+719% YoY)**, a **swing from a −RMB 1.6bn loss (Q1-2025) to ~RMB 25bn net profit**, 95.7% utilization, ~80% DDR5 (G3) yield — with 1H-2026 guidance of RMB 110–120bn revenue / ~RMB 57bn profit. The magnitude reflects the extreme 2026 DRAM price super-cycle as much as share gains (prospectus, **A**).

**The HBM path.** HBM is the acute AI-memory bottleneck. Indigenous HBM requires both a domestic DRAM base *and* TSV/hybrid-bonding packaging — YMTC's Phase-3 (~50% of capacity to DRAM + TSV via its XMC unit) is building toward exactly this. CXMT targets HBM2E in 2026 as a bridge, with HBM3 slipping toward 2027 on yield/thermal issues (WEB-003, D). China's global HBM share today is negligible against SK hynix (~62%), Samsung (~21%), Micron (~17%) (metrics L3, C).

**Capital markets — the next big test.** CXMT opened STAR subscriptions **16-Jul-2026**: **≥RMB 29.5bn (~$4.3bn) raise** for **~10% of the company → an IPO-priced valuation of ~RMB 295bn** (prospectus, A). The widely-cited **RMB 2–3tn** is not a separate "guidance" — it is the **expected post-listing market cap** once the customary STAR first-day pop is applied; that ~7–10× gap between subscription price and expected trading value *is* the policy-/scarcity-driven re-rating in one number. **YMTC** is in IPO counseling (analyst estimates RMB 500bn–3tn, **D** — private, no prospectus). Both are Entity-Listed (YMTC since Dec-2022, litigating; CXMT added to DoD 1260H in Jun-2026), so foreign access will be restricted even post-listing.

### 3.4 AI chips & software ecosystems (L4)

**Market structure.** The most crowded, most strategically-central, and most-constrained layer. **Huawei Ascend** is the flagship (private; est. ~$12bn AI-chip revenue 2026, C). Listed challengers: **Cambricon** (SSE:688256, ~$120bn), the four "little dragon" GPU firms — **Moore Threads** (SSE:688795), **MetaX**, **Biren** (HKEX:6844), **Iluvatar** (HKEX) — plus **Baidu Kunlunxin** and Alibaba's **T-Head** (captive) and ByteDance's in-house silicon.

**Capability vs. frontier — the two-level story.** At the *device* level China is ~1–2 generations behind: Ascend 910C ≈ 60% of H100 inference (DeepSeek's own benchmark, WEB-028, C). At the *system* level Huawei's CloudMatrix 384 / Atlas 950 SuperPoD scales to 8,192 NPUs (~300 PFLOPS BF16; 16 PB/s interconnect) and claims to match/exceed GB200 NVL72 at the rack — at ~4× the power. The **software gap is the deep one**: CANN/MindSpore vs. CUDA is a 3–5+ year moat, though Huawei has open-sourced CANN and DeepSeek/Zhipu have shown frontier training without Nvidia (WEB-026/027, C→D).

**The procurement mandate is the demand engine.** 50% domestic-chip rule for state-funded DCs (Aug-2025) → full foreign-accelerator ban in state projects (Nov-2025) → the draft ≥80%-domestic national grid (2026). Nvidia's China data-center share fell from ~95% (2023) to <60% (H2-2025) toward the CEO's "~0" 2026 framing — yet reporting is *unreconciled* (ByteDance alone reportedly planned ~$14bn of 2026 Nvidia purchases). This contradiction is a flagged open question, not resolved.

**Investability — the sharpest constraint in the report.** Nearly every merchant GPU name is Entity-Listed (Biren and Moore Threads named in the Oct-2023 action) and increasingly OISP-flagged. HK-listed Biren/Iluvatar are the most open; STAR-listed Cambricon/Moore Threads/MetaX are Connect/QFII-restricted; Huawei/ByteDance are fully closed. Valuations are policy-driven: Cambricon briefly hit RMB 1tn on ~$0.9bn revenue then corrected ~14% on its own risk warning; the GPU IPOs popped +468% to +693% day-one. **The purest exposure is the least accessible to US capital.**

### 3.5 Interconnect & networking (L5)

**Market structure.** The quiet chokepoint where China has a genuine global leader. **Montage** (SSE:688008 / HKEX:6809) holds ~36.8% of the global memory-interface market (MRCD/MDB, CKD, PCIe/CXL retimers) — an oligopoly with Rambus/Renesas, high qualification barriers, long lifecycles, a JEDEC board seat. FY2025 revenue RMB 5.456bn (+50%), gross margin ~62%; interconnect-segment revenue +93.8% YoY in Q1-2026; 1m+ cumulative PCIe retimers shipped (WEB-007/008, B/C). **Huawei** supplies the scale-up optical fabric (8,192-NPU clusters, 16 PB/s). Optical-module names **Innolight** and **Eoptolink** ride Nvidia/global 800G demand (Innolight ~60% of Nvidia 800G orders, C).

**Why it matters.** As models scale, the binding constraint migrates from compute to *data movement* — memory bandwidth and node-to-node latency. Montage is expanding from memory-interface into PCIe/optical/Ethernet exactly as that layer becomes the bottleneck. It is the rare China name that is a global *incumbent* leader, not a substitute.

**Investability — a bright spot.** Montage carries **no Entity-List flag and is foreign-investable** (esp. via HKEX:6809). Its H-share IPO (Feb-2026) priced at a 44% discount to the A-share, popped +64% on debut, and by mid-2026 A/H had converged to near-parity — a notable reversal of the historical A-premium and a signal of international conviction. Optical-module names are A-share-restricted.

### 3.6 Data center & cloud (L6)

**Market structure.** **Alibaba Cloud** leads China's AI cloud (~35.8% 2025 → ~38.1% 2026; revenue growth re-accelerated to +38% YoY in Q1-2026) and is the closest China analog to a Western hyperscaler — its own chips (T-Head), its own models (Qwen), and deep enterprise integration (WEB, B/C). **Huawei Cloud** is #2 in overall China cloud-infra (~17% Q4-2025; external revenue ~RMB 32bn). **ByteDance's Volcengine** is the fastest-rising AI-cloud (~14.8% AI-cloud share; MaaS revenue targeting RMB 15bn in 2026 from RMB 1.5bn, and ~RMB 200bn AI capex, D). **Baidu AI Cloud** grew AI-infrastructure revenue +79% YoY (Q1-2026, B). **Tencent Cloud** rounds out the majors.

**Capability & economics.** Structurally behind the US hyperscalers on scale and unit cost (global benchmark: ~$7.9bn to own+operate 1 GW; $2tn cumulative hyperscaler capex through 2026 — REF-EV-01), but growing off a low base with a captive market and the national data-center grid (~$295bn, ≥80% domestic) as a demand floor. The cloud layer is where Alibaba's "compounding infrastructure" thesis lives: every enterprise that builds on Alibaba Cloud + Qwen deepens a switching-cost moat the retail narrative ignores.

**Investability.** Alibaba (HKEX:9988 / NYSE:BABA, ~$231bn), Tencent (HKEX:0700, ~$520bn), Baidu (HKEX:9888 / NASDAQ:BIDU, ~$38bn) are the **most liquid, foreign-investable AI exposures in China**, trade at a discount to global hyperscaler peers (weighed down by non-AI legacy lines), and are not Entity-Listed. Huawei Cloud and Volcengine are trapped inside private/closed parents.

### 3.7 Foundation models (L7)

**Market structure.** A vibrant, largely **open-weight** field: **DeepSeek** (R1 the Jan-2025 catalyst; V4 co-optimized for Ascend/Cambricon), Alibaba **Qwen** (open+closed; 180k+ derivative models by Oct-2025 — the largest open-model ecosystem globally), ByteDance **Doubao**, Zhipu **GLM/Z.ai**, **MiniMax**, Moonshot **Kimi**, Baidu **Ernie**, Tencent **Hunyuan**.

**Capability vs. frontier.** Behind OpenAI/Anthropic/Google at the very frontier, but the gap is measured in months on many benchmarks and the open-weight tier is globally competitive. Chinese models now take a striking share of third-party token demand: ~33% → as high as ~55–61% of OpenRouter tokens in 2026 (DeepSeek alone ~17%), as US-lab share fell toward ~30% among those self-selecting, cost-sensitive users (metrics L7, C). The strategic play is *commoditize the model layer* — cheap, open, good-enough intelligence as infrastructure — which simultaneously pressures Western labs' pricing power.

**Investability.** The listed exposures are the platform parents (Alibaba, Tencent, Baidu). Among pure model labs, **Zhipu** (~$75–87bn) and **MiniMax** (~$14–20bn) IPO'd in HK in Jan-2026 (Zhipu beat OpenAI to market and re-rated ~10× intra-year) but are Connect-restricted; **DeepSeek** (implied ~$52–59bn first external round), **ByteDance**, and **Moonshot** remain private. The re-rating of Zhipu is the sharpest illustration of the policy-driven valuation regime — and it monetized that re-rating directly: a **~US$4.0bn top-up placement on 8-Jul-2026** (19.78m H-shares at HK$1,588), Hong Kong's second-largest of the year and **~6.7× its own IPO**, converting the paper re-rating into R&D and M&A firepower (A).

### 3.8 Applications, agents & adoption (L8)

**Market structure & adoption.** ~602m generative-AI users, all on domestic platforms (C). Consumer scale is real: Doubao ~100m DAU (145m Spring-Festival peak), ~260m MAU; Qwen and YuanBao 50–75m DAU at peak; combined top-5 chat/search apps ~900m MAU (D). For scale reference, ChatGPT ~190m DAU globally.

**The weak spot.** Enterprise SaaS/monetization is thin relative to the US — China's software economy is smaller and less willing to pay per-seat, so the US "AI takes business services" playbook translates poorly. Policy is pushing the other lever: SOE-adoption mandates and the 15FYP diffusion targets (70% by 2027, 90% by 2030). Coding is an instructive gap — GitHub Copilot still leads China's coding-assistant market (~64.5%) with Alibaba's Tongyi Lingma at ~12.9% (C).

**Investability.** Captured mainly through the platform incumbents (Alibaba, Tencent, ByteDance-private) rather than standalone app equities; the enterprise-AI opportunity is more a *margin story for the clouds* than a separate investable tier today.

### 3.9 Physical AI & embodied (L9)

**Market structure — China's chosen battleground.** The layer most aligned with China's manufacturing edge and infrastructure doctrine. Humanoids: **Unitree** (STAR IPO approved in a record 104 days, ~$6bn target; 2025 revenue RMB 1.69bn, +335%), **UBTech** (HKEX:9880; U-series orders >13,361), **AgiBot/Zhiyuan** (~$6.4bn, HK IPO planned H2-2026), **Galbot** (~$3bn), **Fourier** (~$1.1bn). Robotaxi/AV — a direct EV-chain spillover: **Baidu Apollo Go** (>22m cumulative rides, 27 cities), **Pony.ai** (NASDAQ:PONY), **WeRide** (NASDAQ:WRD, ~$2.4bn), **Momenta** (HKEX:6880, ~$9bn IPO, debuted Jul-2026; ~64.5% of the independent urban-NOA market). Supporting silicon: **Horizon Robotics** (HKEX:9660).

**Capability & economics.** China leads on *volume and price* (295k industrial robots installed in 2024, ~54% of global; humanoids shipping at price points far below Figure/1X) but not yet on *profitability* — every name is loss-making (Horizon: RMB 10.5bn loss on RMB 3.8bn revenue). Backed by the ~$138bn AI+robotics state fund and ~¥1tn robotics program. US humanoid peers (Figure ~$39bn) carry far higher valuations on far less revenue — a valuation asymmetry worth watching.

**Investability — the most open China-AI layer for foreigners.** Several names are US- or HK-listed and *not* obviously Entity-flagged: WeRide, Pony.ai, Momenta, UBTech, Horizon Robotics. This is where a foreign investor can get relatively clean embodied-AI exposure — with the caveat that these are early, cash-burning, and volatile.

---

## 4. The horizontal overlay

### 4.1 Policy & industrial strategy
Four reinforcing tracks: (1) the **15th FYP** (AI as primary national objective; diffusion targets); (2) **mega-funds** — ~$295bn national DC grid, ~$138bn AI+robotics fund, the "Big Fund" Phase III at RMB 344bn (~$47.5bn, largest phase, now explicitly covering HBM/AI-semis); (3) **mandates** — 50% domestic equipment for new fabs, escalating domestic-chip rules for state DCs (50% → full foreign-accelerator ban → ≥80% grid), SOE adoption; (4) the Aug-2025 **"AI+"** State Council initiative. The through-line: policy converts technical uncertainty into demand certainty.

### 4.2 Export controls & geopolitics (timeline)
Controls turned **bidirectional** in 2025–26. Tightening peaked with Dec-2024 HBM + Foreign-Direct-Product-Rule controls and rolling Entity-List additions (Mar-2025 tranche hit NAURA/SMIC units). But H20 (banned Apr-2025, restored with a 15% fee Aug-2025) and H200 (case-by-case since Jan-2026 with a 25% tariff, capped at ≤50% of US-customer volume) both *loosened* — while China paused (not repealed) its rare-earth/gallium/germanium leverage through ~Nov-2026 as part of a post-summit truce. The proposed **MATCH Act** would ban all ASML DUV to China (~20% of ASML 2026 revenue) and names the champions explicitly. Taiwan remains the tail risk: not the modal 12-month outcome per the reference analysts, but a portfolio-defining scenario whose mere possibility is itself an inflationary, spending-inducing force.

### 4.3 Talent & R&D
China's edge is *applied* engineering density and open-source contribution (DeepSeek, Qwen, Kimi, MiniMax all ship influential open weights). The state has grown protective as the stack has gained value — credible reports of intervening against talent/IP moving abroad (e.g., via Singapore vehicles) and restrictions on staff at leading labs. Treat the talent layer as a strategic asset that is increasingly *managed* like one.

### 4.4 Capital markets, the IPO wave & the investable basket
The **Sept-2024 "slow-bull" pivot** reframed the equity market as a strategic financing tool for national champions and a savings vehicle to replace property. The result is the 2025–26 **IPO cluster**: Zhipu, MiniMax, Biren, Iluvatar and Montage's H-share all listing within ~5 weeks; Moore Threads/MetaX on STAR with +468%/+693% day-one pops; CXMT and YMTC the next, much larger tests. Montage's A/H premium *inverted* (H went from a 44% discount to a premium), a marker of international conviction. Forward P/Es for the broad China-AI set sit ~18–19 — similar to global peers — but off a far lower earnings base, which is the bull case *and* the reason earnings are unstable enough to make multiples unreliable (REF-BW-01).

**The access overlay (decisive for allocators).** Treasury's OISP (broadened by the Dec-2025 NDAA/COINS Act) now overlaps heavily with Entity-List flags on Moore Threads, MetaX, Biren, and Kunlunxin — making the highest-momentum GPU IPOs **effectively closed to US capital even while they trade freely in Hong Kong**. Foreign-investable, non-flagged exposures cluster in the platform incumbents (Alibaba, Tencent, Baidu), Montage, CATL, and parts of L9 (WeRide, Pony.ai, Momenta, UBTech, Horizon).

---

## 5. Synthesis

### 5.1 Where value is captured — bottleneck economics
Margin pools where a scarce, hard-to-replicate capability meets captive demand. Today that is: **lithography/EUV** (the ultimate chokepoint, but not yet investable domestically), **advanced foundry** (SMIC — the shared scarce resource), **memory interface/interconnect** (Montage — a genuine global incumbent), **advanced packaging/HBM** (emerging), and **power** (China's structural edge, best played via CATL/grid). The model and app layers are *commoditizing by design* — China's strategy is to make intelligence cheap infrastructure, which caps value capture there and pushes it down into hardware and up into physical AI.

### 5.2 China-vs-US scorecard (capability gap · timeline · access)

| Layer | Gap to frontier | Timeline to parity | Foreign-investable? |
|-------|----------------|--------------------|--------------------|
| L0 Power | China **ahead** | — | Yes (CATL) |
| L1 Equipment/EDA | 1–3 gen (EUV/EDA widest) | EUV: lab ~2028, HVM 2030s | Restricted |
| L2 Foundry | ~2–3 nodes | Gated on EUV | Restricted (HK) |
| L3 Memory/HBM | HBM ~3–4 yr; DRAM closing | HBM3 ~2027+ | Restricted post-IPO |
| L4 AI chips | ~1–2 gen device; closer at rack | SW (CUDA) 3–5 yr | Mostly **closed** to US |
| L5 Interconnect | China **at frontier** (Montage) | — | **Yes** (Montage) |
| L6 Cloud | Behind on scale/cost | 3–5 yr | **Yes** (BABA/Tencent) |
| L7 Models | Months at frontier; open-weight competitive | Rolling | Parents yes; labs restricted |
| L8 Apps | Consumer ahead; enterprise behind | — | Via parents |
| L9 Physical AI | Volume-lead; profitability-behind | — | **Most open** |

### 5.3 The investable basket (stack-mapped)
- **Core, foreign-investable, high-conviction:** Alibaba (L4/6/7), Tencent (L6/7), Montage (L5), CATL (L0), Baidu (L4/6/7).
- **High-conviction, access-constrained:** NAURA, AMEC, ACM (L1); SMIC, Hua Hong (L2); Cambricon (L4) — own via HK lines or Connect where eligible; watch Entity/OISP.
- **Event-driven / pipeline:** CXMT, YMTC (L3 IPOs); Kunlunxin (L4 IPO); Unitree, AgiBot (L9 IPOs).
- **Cleaner embodied-AI access:** WeRide, Pony.ai, Momenta, UBTech, Horizon (L9).
Construct as a *diversifier* (low correlation to the global AI supply chain), sized for the Entity-List/OISP overlay and the policy put beneath the market — not as concentrated growth beta.

### 5.4 Scenarios (2027 / 2030)
- **Base:** Indigenization advances unevenly — foundry/memory/interconnect/power progress, EUV lags. China fields competitive rack-scale systems and open models; capex cycle sustained by policy. China-AI equities compound off a low base with high dispersion.
- **Bull:** A domestic EUV or HBM breakthrough, or a decisive rack-scale win, closes the compute gap; power advantage converts into a build-out that outpaces US expectations. Champions re-rate toward global peers; the diversifier becomes a growth engine.
- **Bear:** EUV stalls, yields stay low, the demand mandate outruns deliverable technology; a Taiwan/rare-earth flashpoint or an OISP tightening strands foreign capital. Policy-inflated multiples de-rate hard.

### 5.5 Risk register
Policy reversal (low — commitment is structural); **technology failure at EUV/HBM (the key gating risk)**; demand-mandate outrunning capability; overbuild/valuation air-pocket (policy-inflated multiples); geopolitical flashpoint (Taiwan/rare earths); **investability/regulatory risk (Entity-List + OISP stranding US capital)** — the most underappreciated practical risk for Western allocators.

### 5.6 Second-order effects
Global-equity valuation convergence (US↔non-US risk-premium compression); a structural bid under the **memory cycle** (indigenous HBM demand); **energy/commodities** (China's power/grid/storage build); downward pressure on **global token pricing** as China commoditizes open-weight intelligence; and a persistent **mercantilist** impulse as strategic-sector strength coexists with weak domestic demand.

---

# Part II — Demand, Economics & Access (v2 deepening)

> **Reader's note.** Part I mapped the *supply* stack — who builds each layer. Part II answers the three questions a capital allocator actually asks: **where is the demand, is the revenue real, and who is allowed to own it.** Industry terms (EUV, WFE, HBM, OISP, MSCI China A, …) are defined in the **Glossary** (`report/GLOSSARY.md`). Every figure keeps its A–D confidence grade; this section leans on **filed financials and primary disclosures** wherever they exist, and refuses to invent numbers where they don't.

## II.1 The demand split that changes the bet *(P3)* ‹Fig. II-1›

The single most consequential v2 refinement: **not all "China-AI" names are a bet on China.** Demand divides into three buckets:

- **Global-demand-led** — sell into the *world* AI build-out, not the domestic mandate: **Montage** (memory-interface chips inside global AI servers), **Innolight / Eoptolink** (optical modules — Innolight ~60% of Nvidia's 800G orders), **CATL** (global energy-storage). These price off the **global** AI-capex cycle (Nvidia, hyperscalers) and are foreign-investable.
- **Domestic-substitution** — demand *manufactured* by import-substitution and the 80%-domestic mandate: **Cambricon, Moore Threads, Biren, CXMT, YMTC, Kunlunxin**. Fortunes turn on Chinese policy; mostly Entity-Listed / closed to US capital.
- **Mixed / dual** — **Alibaba, SMIC, Hua Hong, ACM**: exposed to both the global cycle and domestic substitution.

**Investment consequence:** the "diversifying, low-correlation-to-global-AI" thesis (Bridgewater) applies **only to the domestic-substitution bucket**. The global-demand bucket is *correlated* with Nvidia and the world cycle — it is a lever on the global build-out that happens to be listed in Shanghai/HK, not a China-policy diversifier. Confusing the two is the most common error in the China-AI trade.

*Actual-vs-consensus (P3):* for the top listed names we compiled reported growth, guidance, and where available sell-side consensus (NAURA vs AMAT/Lam; Montage vs Astera Labs; SMIC vs TSMC/UMC; Alibaba vs AWS). The market is pricing **high forward growth off a low base** for the domestic-substitution names (semis on premium multiples vs global peers) and **catch-up re-rating** for the platforms. Precise consensus for many A-share names is proprietary/thin — flagged where unavailable rather than fabricated.

## II.2 Hyperscaler economics & capex funding *(P1)*

- **AI-cloud contribution & the non-AI question.** Alibaba Cloud re-accelerated to **+38% YoY (Q1-2026)**; Baidu AI-cloud infrastructure revenue **+79% YoY**. For Alibaba and Tencent the legacy segments (e-commerce, gaming, ads) still **fund** rather than drag the build-out — they throw off the cash that pays for capex.
- **Funding source — the real contrast with the US, now with a caveat.** Chinese hyperscalers still fund the *bulk* of AI capex from internal cash, versus a US marginal AI dollar that is **increasingly externally financed** (debt/equity — e.g. Alphabet's large 2026 equity raise). But the "pure internal-cash resilience" framing needs qualifying: **Alibaba's own 6-Ks show group free cash flow swinging *negative* in two of the last three quarters** — **−RMB 21.8bn** (Sep-2025), +RMB 11.3bn (Dec-2025, −71% YoY), **−RMB 17.3bn** (Mar-2026) — as cloud/AI capex (plus quick-commerce) outran operating cash flow. The build is now large enough to lean on the **balance sheet** (RMB 560bn / ~US$80bn liquidity), not just the P&L. Still off a **far smaller absolute base** than the US (~$2T hyperscaler+neocloud cumulative capex through 2026). *(SEC 6-K, A.)*
- **The sharpest primary find — a monetization gap.** Baidu's SEC **6-K** (Q1-2026) confirms **AI-cloud infrastructure revenue +79% YoY and GPU-cloud +184% YoY** — yet "AI Applications" revenue is only ~**RMB 2.5bn, roughly flat YoY**, despite 200m+ Ernie MAU. Usage is real; **direct monetization lags** (growth metrics A; the flat app-line to be lifted from the 6-K statement tables).

## II.3 Model & app economics — share ≠ revenue *(P2)* ‹Fig. II-2›

- **Filed reality (now A — audited results).** **Zhipu** (HKEX:2513) FY2025: revenue **RMB 724m (+132%)**, GAAP net loss **RMB 4.72bn** — but **adjusted net loss RMB 3.18bn** (the gap is largely non-cash), gross margin 41%. **MiniMax** (HKEX:0100) FY2025: revenue **$79m (+159%)**, GAAP net loss **$1.87bn** — but **adjusted net loss only $251m**; the headline loss is overwhelmingly a **non-cash fair-value charge on convertible/preferred instruments**, not cash burn. ~⅔ (AI-native products $53m) from consumer apps (Talkie/Hailuo), >70% of revenue international. *The distinction matters: on GAAP these labs look catastrophically loss-making; on cash the burn is an order of magnitude smaller.*
- **Open-weight monetization reality.** Open models win **token share** but earn little **directly**; monetization is indirect (cloud pull-through, enterprise support, closed tiers). **DeepSeek, Moonshot and ByteDance model-level revenue are not reliably disclosed** — DeepSeek estimates span ~80–100× across sources — so we **decline to state a figure** rather than launder an estimate into a fact.
- **OpenClaw & the enterprise inflection.** The viral **OpenClaw** agent spurred **Alibaba (Wukong)** and **Tencent (ClawPro / WorkBuddy / ClawBot)** to ship enterprise-agent products in 2026. Traction (200+ ClawPro beta orgs, 2,000+ WorkBuddy pilots) is **vendor-self-reported** — a directional inflection, not audited demand.

## II.4 Talent & R&D *(P4)* ‹Fig. II-3›

- **China leads on research *output*:** **69.7%** of global AI patent filings, **23.2%** of publications, and produces **38%** of the world's elite AI researchers by origin. **But historically 72%** of China-educated elite researchers ended up at **US** institutions (only ~11% stayed).
- **The 2025–26 reflow signal:** US visa tightening + Stanford AI Index's finding that AI-talent migration *into* the US fell **~89% since 2017** + China's new K-visa point to talent returning — but this is a **signal, not yet a measured stock** (DeepSeek's ~70% US-experienced returnees is one firm, not a population statistic).
- **The gap that binds:** a chip-design / EDA talent shortage (recruiter estimates of 200–300k, **D**) — the human-capital mirror of the EUV/EDA tooling gap.

## II.5 Global investability — the US is the outlier *(P5)*

For a **globally-distributed client base**, the key correction to Part I: **the US is uniquely constrained, not the norm.**

- **EU / UK / Japan / Korea / Singapore / Gulf** investors face **no domicile-specific legal bar** on most listed China-AI names — *including the Entity-Listed GPU IPOs.* Access is gated by **market mechanics** (Stock Connect seasoning, STAR/ChiNext professional-investor-only rules, QFII licensing, ~20% A-share inclusion factor), not national law.
- **US persons** are the exception (Entity List + Treasury **OISP**) — though OISP carries a **passive-index exemption** for small, non-controlling holdings (a correction to v1's stronger "US persons excluded" framing).
- **Taiwan** is the one **symmetric legal barrier** (restricting its *own* capital into mainland tech). Japan's **GPIF** voluntarily excluding China A-shares (2025–30) is a checkable **prudential de-risking** signal.
- **The swing factor to monitor:** a single-sourced Reuters report (Jul-2026) that Beijing may curb **foreign access to Chinese AI models and which investors may back homegrown AI firms** — if enacted, the **first China-side capital wall** on the sector (D; undecided per its own sources). A full *who-can-own-what by investor domicile* matrix is in `research/v2_p5_global_reg.md`.

## II.6 Index exposure — you may already own the stack *(P6)* ‹Fig. II-4›

AI-stack names are **structurally over-represented** in every major China benchmark: **~23.5%** of MSCI China sits in just **Tencent + Alibaba**; **~17.9%** of **HSTECH** in **SMIC + Tencent**; **Innolight** is the single **largest CSI 300 weight (~5%)**, having overtaken CATL. Implication for allocators: **passive China exposure already carries heavy AI-stack beta** — the active decision is *tilt*, not *initiation*. Full ISIN / GICS / index-membership table: `database/company_reference.csv` (all C/D — index-provider PDFs were inaccessible to automated fetch).

## II.7 What the red-team changed

An adversarial reviewer challenged every load-bearing claim (`research/review/redteam_v2.md`); a follow-up **primary-source pass** then closed the flags it raised (`research/review/primary_validation_2026-07.md`). Result: **fit to integrate with fixes** — Biren's ticker corrected (→ **HKEX:6082**); and the three "to-verify" items now **resolved against company filings (A)**: **(i) Alibaba FCF** confirmed negative in two of the last three quarters (−RMB 21.8bn / +RMB 11.3bn / −RMB 17.3bn); **(ii) Zhipu's follow-on** confirmed as the ~US$4.0bn 8-Jul-2026 placement; **(iii) CXMT's valuation** reframed from a vague "295bn–3tn range" to the IPO-price (~RMB 295bn) vs expected post-pop cap (RMB 2–3tn) spread, straight from the STAR prospectus. Zhipu & MiniMax FY2025 economics upgraded **B→A** with an adjusted-loss nuance (GAAP losses are largely non-cash). A standing caveat remains that **all index weights are search-mediated (C/D)** and **YMTC's valuation stays D** (private). The batch's defining strength, per the review, was **confidence honesty** — the pods flagged their own weak data instead of inventing precision, and the flags proved verifiable.

---

## Appendix
- **A. Methodology & confidence grading** — see `/database/schema.md` and `/database/RECONCILIATION.md`.
- **B. Company master & data** — `/database/company_master.csv`, `company_reference.csv` (ISIN/GICS/index membership), `metrics_timeseries.csv`, `policy_funding_tracker.csv`, `model_catalog.csv`, `chip_catalog.csv`, `sources.csv`.
- **C. Analyst pod memos** — Part I: `/research/pod1…pod6_*.md`. Part II (v2): `/research/v2_p1…p6_*.md` (hyperscaler economics, model economics, demand-split & priced-in, talent, global regulation, index/reference data).
- **D. Glossary** — `/report/GLOSSARY.md` (also appended to the .docx).
- **E. Adversarial review** — `/research/review/redteam_v2.md` (challenge log + must-fixes).
- **F. Resolved vs still-open.** *Resolved against primary filings (Jul-2026, grade A — see `research/review/primary_validation_2026-07.md`):* Alibaba FCF; Zhipu follow-on (~$4.0bn placement); CXMT valuation/prospectus economics; Zhipu & MiniMax FY2025 (B→A); Biren ticker (→ HKEX:6082). *Still open (C/D):* Nvidia's true China share; **YMTC** valuation (private); indigenous-EUV timeline; DeepSeek/Moonshot model revenue; Baidu's exact "AI Applications" sub-line. See `RECONCILIATION.md`.
- **G. Reference scaffolding** — Bridgewater ×3, Sands Capital, Exponential View (`sources.csv` REF-*).
