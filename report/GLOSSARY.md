# Glossary & Concept Primer

*For readers who are not semiconductor or AI-infrastructure specialists. Terms are grouped by where they sit in the stack. Each entry explains what the thing **is** and why it **matters** to the investment case.*

---

## The manufacturing stack (how a chip gets made)

- **Node (e.g. "7nm", "5nm")** — a shorthand for a chip-manufacturing generation. Smaller numbers = denser, faster, more power-efficient transistors. China is largely stuck at **7nm-class**; the global frontier is ~2–3nm. *Why it matters: node = how good your chips can be.*
- **WFE (Wafer Fab Equipment)** — the machines inside a chip factory ("fab") that build chips layer by layer: lithography, etch, deposition, cleaning, etc. *A fab is only as capable as its WFE.*
- **Lithography** — the step that prints circuit patterns onto the silicon wafer using light. The most critical and hardest-to-replicate tool.
  - **EUV (Extreme Ultra-Violet lithography)** — the most advanced lithography, using 13.5nm-wavelength light; required to make sub-7nm chips economically. Made **only by ASML** (Netherlands) and **banned from export to China**. *This is the single binding chokepoint in China's stack.*
  - **DUV (Deep Ultra-Violet lithography)** — the previous-generation, longer-wavelength lithography China *can* access (with restrictions). *China's workaround for the EUV ban.*
  - **Multipatterning** — using DUV several times over to fake the resolution of one EUV pass. It works but costs more steps, lower yield, higher cost. *The "tax" China pays for lacking EUV.*
- **Etch / Deposition / Cleaning** — the other core fab steps (carving patterns, laying down material, removing residue). Where China's own tool-makers (AMEC, NAURA, ACM) are strongest.
- **EDA (Electronic Design Automation)** — the software used to *design* chips before they're built (Synopsys, Cadence, Siemens). China depends on foreign EDA; a wide gap.
- **Yield** — the percentage of chips on a wafer that come out working. Higher = cheaper. China's advanced-node yield (~35%) is far below TSMC's (>80%). *Low yield = expensive, scarce chips.*
- **Foundry** — a factory that manufactures chips designed by others (e.g. **SMIC**, **TSMC**). *The shared bottleneck behind almost every Chinese AI chip.*
- **Fabless** — a chip company that designs but does not manufacture (e.g. Montage, most GPU firms); it outsources to a foundry.

## Memory & packaging

- **DRAM / NAND** — the two main memory types. DRAM = fast working memory; NAND = storage. China's champions: **CXMT** (DRAM), **YMTC** (NAND).
- **HBM (High-Bandwidth Memory)** — DRAM chips stacked vertically to feed AI accelerators at very high speed. The **acute bottleneck** for AI hardware; dominated by SK hynix/Samsung/Micron. China is ~3–4 years behind.
- **TSV (Through-Silicon Via)** — tiny vertical wires that connect stacked memory dies; a prerequisite for building HBM.
- **Hybrid bonding** — an advanced way to fuse chip layers directly (no solder bumps), enabling denser stacking; key to next-gen HBM and chiplets.
- **Advanced packaging / CoWoS** — assembling multiple chips + memory into one high-performance module. **CoWoS** is TSMC's version (Nvidia's GPUs depend on it). China is building analogs.

## Compute & software

- **GPU / NPU / ASIC** — types of AI accelerator chips. **GPU** = general-purpose (Nvidia); **NPU** = neural-processing unit (Huawei Ascend, Cambricon); **ASIC** = custom-built for one job. *These run AI models.*
- **CUDA** — Nvidia's software platform that lets developers program its GPUs. Its huge ecosystem is Nvidia's deepest moat.
  - **CANN / MindSpore** — Huawei's attempt at a CUDA alternative. *Replicating CUDA's ecosystem is a 3–5+ year challenge — the hardest gap to close.*
- **Rack-scale / SuperPoD (e.g. CloudMatrix, Atlas 950)** — lashing thousands of chips into one giant "logical" computer. China's strategy: *lose at the single-chip level, win at the rack level* (at the cost of more power).
- **Interconnect** — the wiring/fabric that moves data between chips and memory. As models scale, this becomes the bottleneck. Includes:
  - **Memory-interface chip / retimer** — small chips that keep high-speed signals clean between the processor and memory. **Montage** is the global #1. *An unglamorous but durable chokepoint.*
  - **Optical modules / PCIe / CXL / Ethernet** — different data-movement standards; the plumbing of an AI data centre.

## Models & applications

- **Foundation model / LLM** — a large AI model (e.g. DeepSeek, Qwen, GLM) trained on vast data, adaptable to many tasks.
- **Open-weight vs closed-weight** — *open* = the model's parameters are downloadable/free to run (China's strategy: DeepSeek, Qwen, Kimi); *closed* = accessible only via a paid API (OpenAI). *Open-weight wins share but earns little direct revenue — a key v2 insight.*
- **MoE (Mixture-of-Experts)** — a model design where only part of the network activates per query, cutting compute cost. Common in Chinese models.
- **Token** — the unit AI models read/write (roughly ¾ of a word). AI is billed per token. *The "meter" of the AI economy.*
- **Training vs inference** — *training* = building the model (compute-hungry, needs frontier chips); *inference* = running it for users (needs less-advanced chips). *China is more constrained on training than inference.*
- **Agentic / agents** — AI that takes multi-step actions autonomously (not just chat). Multiplies token use. **OpenClaw** is a viral agent framework referenced in the demand data.
- **MaaS (Model-as-a-Service)** — renting model access via the cloud (e.g. ByteDance Volcengine).
- **DAU / MAU** — Daily / Monthly Active Users — adoption metrics for consumer apps (Doubao, Qwen).

## Cloud, capex & company financials

- **Hyperscaler** — a mega-scale cloud provider (US: Microsoft/Amazon/Google/Meta; China: Alibaba/Huawei/Tencent/Baidu/ByteDance).
- **Capex (capital expenditure) / capex intensity** — spending on physical assets (data centres, chips); *intensity* = capex as % of revenue. *The AI build-out is a capex story.*
- **FCF (Free Cash Flow)** — cash left after capex; shows whether a company can *self-fund* its build-out or must borrow. *Central to the "who can sustain the spend" question.*
- **RPO (Remaining Performance Obligations)** — contracted future revenue not yet delivered; a demand-backlog signal for clouds.
- **East-Data-West-Compute** — China's policy of siting data centres in the renewable-rich, cheap-power west and piping compute east.
- **PUE (Power Usage Effectiveness)** — data-centre energy efficiency (1.0 = perfect). China targets ≤1.25 for new builds.

## Policy, geopolitics & export controls

- **Entity List** — a US Commerce Department blacklist; listed firms can't buy US-origin tech without a licence. Covers most Chinese AI-chip makers.
- **OISP (Outbound Investment Security Program)** — US Treasury rules restricting **US persons from investing** in certain Chinese AI/chip firms — *distinct from the Entity List, and the reason some HK-listed names are off-limits to US capital* (note: a passive-index exemption exists for small holdings).
- **FDPR (Foreign Direct Product Rule)** — extends US controls to foreign-made goods that use US technology.
- **MATCH Act** — proposed US legislation that would ban ASML DUV shipments to China (still pending).
- **Rare-earth leverage** — China's counter-measure: restricting exports of rare earths/gallium/germanium critical to Western tech.

## Capital markets & investability

- **A-share vs H-share** — a Chinese company's mainland listing (**A**, in RMB, on Shanghai/Shenzhen) vs its Hong Kong listing (**H**, in HKD). **A/H premium** = the price gap between them.
- **STAR Market / ChiNext / SSE / SZSE / HKEX** — Chinese exchanges/boards. STAR (Shanghai) and ChiNext (Shenzhen) are tech-growth boards, often **restricted to professional investors**.
- **Stock Connect** — the pipe that lets foreign investors buy eligible mainland A-shares via Hong Kong (with seasoning rules).
- **QFII / RQFII** — licence schemes for foreign institutions to access mainland markets.
- **HFCAA** — US law that can delist Chinese ADRs whose auditors the US can't inspect.
- **ADR (American Depositary Receipt)** — a US-traded proxy for a foreign share (e.g. BABA, BIDU).
- **NSI Act (UK) / FDI screening (EU)** — inbound-investment national-security reviews (not outbound bans).
- **GICS** — the standard Global Industry Classification Standard (sector/industry taxonomy).
- **ISIN** — the unique 12-character global identifier for a security.
- **MSCI China vs MSCI China A** — index families: *MSCI China* spans all share classes (incl. HK/ADR); *MSCI China A* covers mainland A-shares only. *How much AI-stack weight sits in each is a key v2 finding.*
- **Free-float / inclusion factor** — the share of a company actually available to foreign investors; A-shares enter global indices at a partial (~20%) factor.
- **"Slow bull"** — Beijing's post-Sept-2024 policy of engineering a gradual, supported equity-market rise.

## Physical AI

- **Embodied / physical AI** — AI in the real world: robots, autonomous vehicles, industrial automation. China's chosen edge.
- **Humanoid robot** — general-purpose bipedal robots (Unitree, UBTech, AgiBot).
- **Robotaxi / urban-NOA** — driverless taxis / "Navigate-on-Autopilot" for city driving (Apollo Go, Pony.ai, WeRide, Momenta).

---
*Confidence grades (A filed/audited · B primary · C credible third-party · D single-source/estimate) apply to every figure in the report and database. See `/database/schema.md`.*
