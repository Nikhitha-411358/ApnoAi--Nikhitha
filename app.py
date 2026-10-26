import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title='ApnoMart Executive Dashboard', page_icon='📊', layout='wide')
DATA_PATH = Path(__file__).with_name('apnomart-sales-data.csv')
@st.cache_data
def load_data():
    d = pd.read_csv(DATA_PATH)
    d['Order_Date'] = pd.to_datetime(d['Order_Date'], errors='coerce')
    d['Profit_Margin_Calc'] = d['Profit'] / d['Sales'].replace(0, pd.NA) * 100
    return d

df = load_data()
st.title('ApnoMart Q2 2026 Executive Dashboard')
st.caption('Built by [Your Name] · ApnoAI Data Analytics Intern · October 2026')
st.info('Executive takeaway: Office Supplies delivers the strongest profit margin, while Electronics generates the weakest margin and deserves a focused pricing/discount review.')

with st.sidebar:
    st.header('Dashboard filters')
    regions = st.multiselect('Region', sorted(df['Region'].dropna().unique()), default=sorted(df['Region'].dropna().unique()))
    categories = st.multiselect('Category', sorted(df['Category'].dropna().unique()), default=sorted(df['Category'].dropna().unique()))
    date_min, date_max = df['Order_Date'].min().date(), df['Order_Date'].max().date()
    dates = st.date_input('Order date range', value=(date_min, date_max), min_value=date_min, max_value=date_max)

filtered = df[df['Region'].isin(regions) & df['Category'].isin(categories)].copy()
if isinstance(dates, (tuple, list)) and len(dates) == 2:
    filtered = filtered[filtered['Order_Date'].dt.date.between(dates[0], dates[1])]

sales = filtered['Sales'].sum(); profit = filtered['Profit'].sum(); orders = filtered['Order_ID'].nunique()
margin = profit / sales * 100 if sales else 0
k1,k2,k3,k4 = st.columns(4)
k1.metric('Total Sales', f'₹{sales:,.0f}')
k2.metric('Total Profit', f'₹{profit:,.0f}')
k3.metric('Total Orders', f'{orders:,}')
k4.metric('Profit Margin %', f'{margin:.2f}%')
st.caption(f'Showing {len(filtered):,} records · Profit Margin % calculated as SUM(Profit) / SUM(Sales).')

c1,c2 = st.columns(2)
with c1:
    cat = filtered.groupby('Category', as_index=False).agg(Sales=('Sales','sum')).sort_values('Sales', ascending=True)
    st.plotly_chart(px.bar(cat, x='Sales', y='Category', orientation='h', title='Sales by Category', color_discrete_sequence=['#2878B5'], labels={'Sales':'Sales (₹)','Category':''}), use_container_width=True)
with c2:
    trend = filtered.set_index('Order_Date').resample('W')['Sales'].sum().reset_index()
    st.plotly_chart(px.line(trend, x='Order_Date', y='Sales', markers=True, title='Weekly Sales Trend', labels={'Order_Date':'Week','Sales':'Sales (₹)'}, color_discrete_sequence=['#2878B5']), use_container_width=True)

c3,c4 = st.columns(2)
with c3:
    reg = filtered.groupby('Region', as_index=False).agg(Profit=('Profit','sum')).sort_values('Profit', ascending=True)
    reg['Profit status'] = reg['Profit'].apply(lambda x: 'Positive' if x >= 0 else 'Negative')
    st.plotly_chart(px.bar(reg, x='Profit', y='Region', orientation='h', title='Profit by Region', color='Profit status', color_discrete_map={'Positive':'#269E63','Negative':'#D9534F'}, labels={'Profit':'Profit (₹)','Region':''}), use_container_width=True)
with c4:
    pay = filtered.groupby('Payment_Method', as_index=False).agg(Orders=('Order_ID','nunique')).sort_values('Orders', ascending=False)
    st.plotly_chart(px.pie(pay, names='Payment_Method', values='Orders', hole=.45, title='Orders by Payment Method'), use_container_width=True)

c5,c6 = st.columns(2)
with c5:
    cm = filtered.groupby('Category', as_index=False).agg(Sales=('Sales','sum'), Profit=('Profit','sum'), Discount=('Discount','mean'))
    cm['Profit Margin %'] = cm['Profit'] / cm['Sales'] * 100
    st.plotly_chart(px.bar(cm.sort_values('Profit Margin %'), x='Profit Margin %', y='Category', orientation='h', title='Calculated Profit Margin by Category', labels={'Category':'','Profit Margin %':'Profit Margin (%)'}, color_discrete_sequence=['#269E63']), use_container_width=True)
with c6:
    seg = filtered.groupby('Customer_Segment', as_index=False).agg(Sales=('Sales','sum'), Profit=('Profit','sum'))
    st.plotly_chart(px.bar(seg, x='Customer_Segment', y='Sales', title='Sales by Customer Segment', labels={'Customer_Segment':'Customer Segment','Sales':'Sales (₹)'}, color_discrete_sequence=['#6D5BD0']), use_container_width=True)

st.subheader('Category performance detail')
detail = filtered.groupby('Category', as_index=False).agg(Orders=('Order_ID','nunique'), Sales=('Sales','sum'), Profit=('Profit','sum'), Avg_Discount=('Discount','mean'))
detail['Profit Margin %'] = detail['Profit'] / detail['Sales'] * 100
st.dataframe(detail.sort_values('Sales', ascending=False).style.format({'Sales':'₹{:,.2f}','Profit':'₹{:,.2f}','Avg_Discount':'{:.1f}%','Profit Margin %':'{:.2f}%'}), use_container_width=True, hide_index=True)
st.caption('Note: The supplied dataset contains orders dated 1 May–28 October 2026. The requested dashboard title is retained from the assignment brief; interpret the time range using the selected dates.')
