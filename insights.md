# ApnoMart — Executive Insights

**Dashboard:** ApnoMart Q2 2026 Executive Dashboard  
**Prepared by:** [Your Name]  
**Dataset:** ApnoMart sales dataset (1,200 order records; 1 May–28 October 2026)

## KPI snapshot

- **Total sales:** ₹16,261,998.30
- **Total profit:** ₹4,419,736.17
- **Orders:** 1,200 unique Order_IDs
- **Overall profit margin:** 27.18% (`SUM(Profit) / SUM(Sales) × 100`)

## Three strategic insights

### 1. Revenue pattern — Furniture leads sales, but not profit efficiency

Furniture generated **₹3.52M in sales**, the largest category total and about **21.6% of overall revenue**. However, Office Supplies generated **₹1.18M profit** at a **34.80% margin**, compared with Furniture’s **26.00% margin**. The pattern shows that the biggest revenue category is not the most profitable per rupee sold.

**So what:** Keep Furniture visible as a revenue driver, but prioritize merchandising and growth campaigns for Office Supplies where the dataset shows stronger margin efficiency.

### 2. Profitability pattern — Electronics is the clearest margin improvement opportunity

Electronics generated **₹2.96M in sales** but only **₹558.4K profit**, with an **18.88% margin**—the lowest among the five categories. Office Supplies’ margin is **15.92 percentage points higher**. Electronics also has the highest average discount in the dataset at approximately **14.06%** (category average; other categories are around 12.3–12.8%). This is a useful signal to investigate, not proof that discounts alone caused the lower margin.

**So what:** Run a controlled Electronics pricing/discount test by product. Compare conversion, sales, and profit before rolling out changes; avoid blanket discount cuts without testing demand effects.

### 3. Customer behavior — Corporate customers contribute the largest segment sales; payment mix is spread

Corporate customers generated **₹4.31M in sales** (**26.5% of total sales**) across **307 orders**, the highest segment totals in this dataset. Small Business was close behind at **₹4.15M** across **306 orders**. Cash was the most-used payment method with **258 orders** (about **21.5%** of all orders), while no payment method dominates the order mix.

**So what:** Protect corporate retention with targeted account offers and test cross-sell campaigns for Small Business customers. Keep checkout options broad because order volume is distributed across payment methods.

## Strategic recommendation for next quarter

**Prioritize a measured Electronics margin-recovery pilot while scaling high-margin Office Supplies.** Test lower or more selective Electronics discounts on a product-level basis, monitor profit margin and conversion weekly, and shift incremental campaign budget toward Office Supplies products that can scale without eroding margin. Use region and date filters to compare results, and expand only if profit improves without an unacceptable sales decline.

## Method and data notes

- The CSV has **1,200 rows**, **1,200 unique Order_IDs**, and no missing values in the supplied columns.
- Dates span **1 May through 28 October 2026**, not only Q2. The dashboard title follows the assignment's required wording, but trend interpretations should use the full dataset/date filter.
- Calculated overall profit margin is `SUM(Profit) / SUM(Sales) × 100`; it is not the simple average of row-level `Profit_Margin` values.
- Insights describe associations and observed totals. For example, higher average Electronics discounts and lower margins co-occur, but this dataset alone does not establish that discounts caused the margin gap.

## AI-use disclosure

Used ChatGPT to assist with dashboard code structure, SQL/data-analysis interpretation, and editing the executive narrative. Metrics and observations were calculated from the supplied CSV and should be rechecked against the final dashboard before submission.
