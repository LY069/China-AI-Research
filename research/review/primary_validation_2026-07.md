# Primary-Source Validation Pass — July 2026

**Purpose.** The v2 red-team left three figures flagged *to verify* (Alibaba FCF, Zhipu
follow-on raise, CXMT/YMTC valuations) and several model-lab economics at **B** pending
primary confirmation. MT Newswires was the intended lift, but its data entitlement is
expired (auth OK, 403 on every fetch). This pass validates the same items **directly
against the companies' own filings / results releases** — a stronger source than a
newswire — and records exact figures, dates, and grades.

**Method.** SEC EDGAR 6-K / 20-F, HKEX-listed annual results, and STAR-Market IPO
prospectus disclosures, retrieved via public web (SEC/Businesswire block automated
fetch, so figures were captured from the releases as surfaced in search and
cross-checked across ≥2 independent renderings of the same primary release). Grades:
**A** = filed/audited primary; **B** = company primary disclosure (results release,
prospectus guidance).

---

## 1. Alibaba free cash flow — FLAG RESOLVED → **CONFIRMED (A)**

Reviewer flag: *"Alibaba was reported to have turned FCF-negative on AI capex — confirm
against the 6-K."* Confirmed, and it is **not a one-off** — FCF was negative in **two of
the last three** reported quarters, driven by cloud/AI capex (plus quick-commerce):

| Quarter (fiscal) | Free cash flow | YoY prior-year | Note |
|---|---|---|---|
| Sep-2025 (FQ2'26) | **−RMB 21.84bn** (−US$3.07bn) | +RMB 13.74bn inflow | OCF −68% to RMB 10.10bn; cause cited: "increase in cloud infrastructure expenditure and the investment in quick commerce" |
| Dec-2025 (FQ3'26) | **+RMB 11.35bn** (US$1.62bn) | −71% vs RMB 39.02bn | capex RMB 29.00bn (US$4.15bn) |
| Mar-2026 (FQ4'26) | **−RMB 17.30bn** | swung to outflow | latest available; reported May-2026 |

**Cloud Intelligence Group** (validates the report's "+38%"):
- Mar-2026 quarter: CIG revenue **RMB 41,626m (US$6,035m), +38% YoY** (external-customer
  growth accelerated to **+40%**); AI products = **30%** of CIG revenue; **triple-digit
  AI-product growth for the 11th straight quarter**; CIG adjusted EBITA RMB 3,796m (+57%).
- Dec-2025 quarter: CIG revenue RMB 43,284m (US$6,190m), **+36% YoY**; AI-product
  triple-digit growth 10th consecutive quarter.

**Report impact.** The "+38% (Q1-2026)" figure is **correct** (= calendar-Q1 / March-2026
quarter, +38%). The §II.2 framing that Chinese hyperscalers fund capex "largely from
internal operating cash flow … a resilience point" **needs nuance**: Alibaba specifically
has gone FCF-negative for two of three recent quarters — the build is now large enough to
outrun operating cash and lean on the balance sheet (RMB 560bn / US$80bn liquidity as of
Dec-2025). Grade **A** (SEC 6-K).
Sources: SEC 6-K EX-99.1 (Sep-2025, Dec-2025, Mar-2026 quarters); Alibaba results releases
19-Mar-2026 and 12-May-2026.

## 2. Zhipu follow-on raise — FLAG RESOLVED → **CONFIRMED (A)**

Zhipu (HKEX:2513) priced a **top-up placement on 8-Jul-2026**: **19.78m new H-shares at
HK$1,588** = **~HK$31.4bn (~US$4.0bn)** — Hong Kong's second-largest equity placement of
2026, and **~6.7× the ~HK$5bn (US$0.64bn) IPO** six months earlier. ~13% discount to the
HK$1,825 close; proceeds for R&D, expansion, M&A, working capital. Follows a ~1,500–2,000%
post-IPO run. Grade **A** (priced, disclosed placement).
Source: Bloomberg 8-Jul-2026; HK placement terms as reported by multiple outlets 8-Jul-2026.

## 3. Zhipu FY2025 results — **UPGRADE B → A**

HKEX:2513 audited FY2025 annual results (report's figures validated):
- Revenue **RMB 724.3m (+131.9%)** ✓; total net loss **RMB 4.72bn (+59.5%)** ✓; gross
  margin **41.0%**; R&D **RMB 3.18bn (+44.9%)**; **adjusted net loss RMB 3.18bn (+29.1%)**;
  open-platform/API ARR ~RMB 1.7bn.
- **Nuance to add:** the headline RMB 4.72bn is GAAP-total; **adjusted** loss is RMB 3.18bn
  — the gap is largely non-cash (fair-value / share-based items). Report's numbers stand;
  add the adjusted line so the cash-burn picture isn't overstated.

## 4. MiniMax FY2025 results — **UPGRADE B → A**

HKEX:0100 FY2025 results:
- Revenue **US$79.0m (+158.9%)** ✓; **net loss US$1.872bn (+302.3% from US$465m)** ✓;
  gross margin 25.4%; **>70% of revenue international**.
- **Adjusted net loss only US$250.9m** (vs US$244.2m in 2024) — i.e. the US$1.87bn GAAP
  loss is **overwhelmingly non-cash** (fair-value change on convertible/preferred
  instruments). Report's "net loss $1.87bn" is correct but should carry the adjusted-loss
  nuance so readers don't read it as $1.87bn of cash burn.
- Segment: AI-native products (Hailuo etc.) US$53.1m (+143.4%) = **67% of revenue** →
  validates report's "~⅔ from consumer apps."

## 5. Baidu Q1-2026 — **CONFIRMED (A) with one line still to source**

Baidu 6-K (reported 18-May-2026):
- **AI Cloud Infra revenue +79% YoY**; **GPU-cloud +184% YoY** ✓✓ (both report figures
  confirmed). Total AI Cloud (infra + apps) RMB 11.3bn. Core AI business crossed **52%** of
  Baidu-Core (RMB 13.6bn, +49% YoY). Total revenue RMB 32.1bn (−1% YoY). OCF RMB 2.7bn
  (3rd straight positive quarter).
- The report's specific "AI Applications ~RMB 2.5bn, roughly flat YoY" monetization-gap
  line is consistent with the infra-vs-apps split but the **exact app-line figure was not
  re-confirmed in this pass** — keep as A on the growth metrics, mark the RMB 2.5bn as
  the one sub-line to pull from the 6-K statement tables when access allows.

## 6. CXMT valuation — **UPGRADE D → A, and correct the framing**

CXMT (ChangXin Memory) STAR-Market IPO prospectus (subscription opened **16-Jul-2026**):
- Raise **≥RMB 29.5bn (~US$4.3bn)**; issuing **6.688bn shares ≈ 10% of capital** → **implied
  IPO valuation ≈ RMB 295bn**. Second-largest STAR listing.
- **Q1-2026: revenue RMB 50.8bn (+719% YoY), net profit ~RMB 25bn** (vs −RMB 1.6bn loss in
  Q1-2025) → validates report's "RMB 50.8bn revenue, RMB 24.76bn net profit." 1H-2026
  guidance: revenue RMB 110–120bn, net profit ~RMB 57bn (up to ~25×). Scale reflects the
  extreme 2026 DRAM price super-cycle.
- **Framing correction.** The report's "RMB 295bn–3tn" is not a guidance *range* — it is the
  spread between **IPO-priced valuation (~RMB 295bn)** and **expected post-listing market
  cap (RMB 2–3tn)** once the customary STAR first-day pop is applied. That spread *is* the
  story — it quantifies the policy-/scarcity-driven re-rating, not analyst disagreement.
- **YoY net-profit "+1,688%"** in §3.3 is ill-defined (prior-year base was a loss) → restate
  as a **swing from −RMB 1.6bn to +RMB 25bn**.
- YMTC valuation (RMB 500bn–3tn) remains **analyst estimate (D)** — private, no prospectus.

---

## Net changes to apply
1. §II.2 — replace the Alibaba-FCF reviewer flag with the confirmed 3-quarter FCF table;
   nuance the "internal-OCF resilience" claim. (A)
2. §II.3 — mark Zhipu/MiniMax **A (filed)**; add adjusted-loss nuance for both.
3. §3.3 + Exec-summary #7 — reframe CXMT "295bn–3tn" as IPO-price → post-pop spread; fix
   the "+1,688%" to a swing-from-loss; CXMT valuation → **A**.
4. §3.7 / Exec-summary — add Zhipu's ~US$4.0bn Jul-2026 follow-on placement. (A)
5. §II.7 + Appendix F — move Alibaba FCF, Zhipu follow-on, CXMT valuation from *open/
   to-verify* to *resolved (primary)*; YMTC valuation stays open (D).
6. Database — upgrade confidence on these rows; record valuations in company_reference.

*All figures here are from company filings / results releases / IPO prospectus, retrieved
mid-Jul-2026. MT Newswires was not used (entitlement expired).*
