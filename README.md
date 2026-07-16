# China's AI Stack & Ecosystem — Deep Research

A layer-by-layer value-chain map of China's indigenous AI stack, built for financial-market experts, economists, and industry analysts. Primary lens: **industry & value-chain map**, resolving into a **security-level investable read** at every layer.

## Deliverables
1. **Long-form report** → [`/report/`](./report/)
2. **Presentation materials** → [`/presentation/`](./presentation/)
3. **Evidence database** → [`/database/`](./database/)

## Structure
| Path | Contents |
|------|----------|
| `FRAMEWORK.md` | The research framework (10-layer stack × cross-cutting dimensions × synthesis) |
| `database/` | CSV evidence base — company master (backbone), metrics time-series, policy/funding tracker, model & chip catalogs, source log. Schema in `database/schema.md` |
| `research/` | Analyst pod memos (one per pod) |
| `report/` | The long-form research report |
| `presentation/` | Executive deck |

## Method & conventions
- Bottom-up stack model (L0 energy → L9 physical AI) with 6 horizontal dimensions (policy, compute S/D, geopolitics, capital markets, talent, global diffusion).
- Every figure carries a `source_id` and confidence grade (A filed/audited · B primary · C credible 3rd-party · D single-source/estimate).
- Benchmarked vs US/global at every layer; base/bull/bear scenarios at 2027 & 2030 horizons; data as-of mid-2026.
- Investability & US-Entity-List constraints flagged on every named entity.

## Reference scaffolding
Bridgewater (×3), Sands Capital, and Exponential View reports seed the framework and are cited in `database/sources.csv`; conclusions rest on independently-sourced evidence.

## Status — v2 complete
v1 (10-layer value-chain map) refined per client suggestions. Added:
- **6 v2 analyst pods** — hyperscaler economics & capex funding, model/app economics + OpenClaw, global-vs-domestic demand split & priced-in, talent & R&D, non-US/global investability, index & reference data.
- **Adversarial red-team review** (`research/review/redteam_v2.md`) — verdict: fit to integrate with fixes; confidence-honesty confirmed. Biren ticker corrected (HKEX:6082).
- **Report Part II** (demand, economics, access) + **Glossary** (`report/GLOSSARY.md`) for non-experts.
- **company_reference.csv** — ISIN/GICS/index membership (Suggestion 12).
- **4 new charts** + value-chain flow diagram; DOCX rebuilt (12 charts + glossary).

**Primary-source validation (Jul-2026)** — `research/review/primary_validation_2026-07.md`. MT Newswires entitlement was expired (403), so the flagged figures were validated **directly against company filings** instead (stronger source): Alibaba FCF (confirmed negative in 2 of last 3 quarters, SEC 6-K), Zhipu's ~$4.0bn follow-on placement, CXMT's STAR prospectus (IPO ~RMB295bn vs RMB2-3tn post-pop), and Zhipu/MiniMax FY2025 economics — all upgraded to **grade A**. Still open (C/D): YMTC valuation (private), Nvidia China share, EUV timeline.

Outstanding / next: native `.pptx` deck built (`presentation/China_AI_Stack_Deck.pptx`); YMTC remains private (no prospectus).