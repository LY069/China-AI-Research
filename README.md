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

## Status — v1 complete
All six analyst pods delivered; outputs integrated. Deliverables live:
- **Report:** `report/China_AI_Stack_Report.md` (~4,500 words; 10-layer map + synthesis)
- **Deck:** `presentation/deck.html` (15 slides, self-contained, theme-aware)
- **Database:** `database/` — 43 companies, 192 metrics, 36 policies, 21 models, 26 chips, 119 sources; build via `python3 database/build_master.py`
- **Evidence annexes:** `research/pod1…pod6_*.md`

Known open questions and cross-pod conflicts are tracked in `database/RECONCILIATION.md`.
Next-pass enrichment (optional): primary-filing verification of pre-listing valuations
and tickers; `MT_Newswires` connector requires authorization for newswire data.
