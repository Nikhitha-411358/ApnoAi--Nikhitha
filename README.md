# ApnoMart — The Insight Board

Interactive executive sales dashboard built for the ApnoAI Business Intelligence task.

## Tool used
Python, Streamlit, Pandas, and Plotly.

## Dashboard features
- KPI cards: Total Sales, Total Profit, Total Orders, and calculated Profit Margin %.
- Sales by category and weekly sales trend.
- Profit by region.
- Orders by payment method.
- Calculated profit margin by category and sales by customer segment.
- Interactive Region, Category, and Order Date filters.
- Category performance detail table.

## Key findings
1. Furniture has the highest sales (₹3.52M), but Office Supplies has the highest profit (₹1.18M) and category margin (34.80%).
2. Electronics has the lowest category profit margin (18.88%) and the highest average discount (about 14.06%); test pricing changes before scaling.
3. Corporate customers contribute ₹4.31M sales (26.5% of total), and payment methods are broadly distributed.

## Run locally
1. Install Python 3.10+.
2. In this folder, run `pip install -r requirements.txt`.
3. Run `streamlit run app.py`.

Keep `apnomart-sales-data.csv` in the same folder as `app.py`.

## Files
- `app.py` — interactive dashboard source.
- `apnomart-sales-data.csv` — supplied source dataset.
- `insights.md` — executive insights and strategic recommendation.
- `dashboard.png` — static dashboard preview for the submission.

## Data note
The supplied dataset spans 1 May–28 October 2026. The dashboard title retains the exact title specified in the assignment brief.

Prepared by: [Your Name]
