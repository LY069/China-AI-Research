# Database build & reconciliation notes

## How the master CSVs are built
The six master tables are assembled by `build_master.py`, which merges the six
pod `_data.md` files (in `../research/`) into the seed tables with a
**field-level upsert**: for an existing key, only non-empty new values override;
missing columns are preserved. Pods are processed in filename order (pod1→pod6),
so **Pod 6 (Policy/Geopolitics/Capital Markets) wins on overlapping
listing/valuation/Entity-List fields** — by design, as it is the dedicated
capital-markets and investability pod. Re-run with `python3 database/build_master.py`.

Keys: company_master→`company_id`; metrics_timeseries→(`metric_id`,`entity`,`period`);
policy_funding_tracker→`policy_id`; model_catalog→`model_id`; chip_catalog→`chip_id`;
sources→`source_id`.

The pod `_data.md` files are retained in `../research/` as the **full evidence
annexes** — where the merged master keeps a single reconciled value, both pods'
detail (and confidence grades) remain in their source files.

## Known cross-pod conflicts (resolved; monitor)
These reflect genuine measurement differences, not errors — most resolve to
"same fact, different as-of date or basis." Flagged here for analyst transparency.

| Entity | Field | Pod values | Resolution |
|--------|-------|-----------|------------|
| Moore Threads | mkt cap | Pod 3 ~$44bn (current, 2026-07) vs Pod 6 ~$7.5bn (IPO post-issue) | Both valid; master carries Pod 6 IPO basis + note. Current market value ≫ IPO on +468% pop. |
| Biren | ticker | Pod 3 HKEX:9668 vs Pod 6 HKEX:6844 | Ticker verification pending; treat as C-confidence until a primary HKEX source confirms. |
| Iluvatar | mkt cap | Pod 3 n.a. vs Pod 6 ~$25.6bn (2026-06-24, +428% since IPO) | Master carries Pod 6 figure (D). |
| CXMT | valuation | Pod 2 ~$280-420bn guidance vs Pod 6 ~$43bn (RMB295bn conservative) | Huge dispersion; master carries conservative point (C) + note; bull case flagged D in metrics. |
| YMTC | valuation | RMB500bn–3tn (~$70-420bn) across sources | Pre-listing, D-confidence; do not treat any point estimate as firm. |
| Nvidia China share | — | <60% vs <40% vs "toward zero" vs ByteDance ~$14bn 2026 Nvidia orders | Left UNRECONCILED in memos/metrics; flagged as a key open question (see Pod 3 memo). |

## Confidence discipline
Every data row carries A/B/C/D. Pre-listing valuations, private-company figures,
and forward projections are largely C/D. Point market caps are as-of-dated in
`notes`. Treat all 2026 figures as provisional given the fast-moving environment.
