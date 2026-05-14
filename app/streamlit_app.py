import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Food Delivery Demand Pulse",
    page_icon="🍔",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/processed/final_orders.csv")

forecast_df = pd.read_csv("outputs/forecast/7_day_forecast.csv")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📌 Filters")

city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(list(df['city'].unique()))
)

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    ["All"] + sorted(list(df['cuisine'].unique()))
)

# =====================================================
# FILTER DATA
# =====================================================

filtered_df = df.copy()

if city != "All":
    filtered_df = filtered_df[
        filtered_df['city'] == city
    ]

if cuisine != "All":
    filtered_df = filtered_df[
        filtered_df['cuisine'] == cuisine
    ]

# =====================================================
# TITLE SECTION
# =====================================================

st.title("🍔 Food Delivery Demand Pulse")

st.markdown("""
Operational analytics dashboard for identifying peak demand windows,
delivery bottlenecks, surge inefficiencies, and short-term forecasting opportunities.
""")

st.markdown("---")

# =====================================================
# KPI SECTION
# =====================================================

total_orders = filtered_df.shape[0]

avg_delivery = round(
    filtered_df['delivery_time_min'].mean(),
    2
)

avg_order_value = round(
    filtered_df['order_value'].mean(),
    2
)

surge_percent = round(
    filtered_df['surge_applied'].mean() * 100,
    2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📦 Total Orders",
    f"{total_orders:,}"
)

col2.metric(
    "⏱ Avg Delivery Time",
    f"{avg_delivery} min"
)

col3.metric(
    "💰 Avg Order Value",
    f"₹{avg_order_value}"
)

col4.metric(
    "⚡ Surge Orders",
    f"{surge_percent}%"
)

st.markdown("---")

# =====================================================
# KEY INSIGHTS
# =====================================================

st.subheader("📌 Key Operational Insights")

st.markdown("""
- Evening demand significantly exceeds lunch demand across all cities.
- Bangalore and Mumbai contribute the highest operational load.
- Surge pricing alone does not fully reduce delivery delays.
- Delivery times remain concentrated between 30–50 minutes.
- Demand patterns remain relatively stable over short forecasting horizons.
""")

st.markdown("---")

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3 = st.tabs([
    "📊 Demand Analytics",
    "📈 Forecasting",
    "🚀 Recommendations"
])

# =====================================================
# TAB 1 — ANALYTICS
# =====================================================

with tab1:

    st.subheader("📈 Peak Demand by Hour")

    hourly_orders = (
        filtered_df.groupby('hour')
        .size()
        .reset_index(name='orders')
    )

    fig1 = px.line(
        hourly_orders,
        x='hour',
        y='orders',
        title='Peak Demand by Hour',
        markers=True
    )

    fig1.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="Total Orders"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🌆 City-Wise Peak Demand Heatmap")

    heatmap_data = filtered_df.pivot_table(
        index='city',
        columns='hour',
        values='order_id',
        aggfunc='count'
    )

    fig2 = px.imshow(
        heatmap_data,
        title='City vs Hour Demand Heatmap',
        aspect='auto',
        color_continuous_scale='plasma'
    )

    fig2.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="City"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🚴 Delivery SLA Distribution")

    fig3 = px.histogram(
        filtered_df,
        x='delivery_time_min',
        nbins=30,
        title='Delivery Time Distribution'
    )

    fig3.update_layout(
        xaxis_title="Delivery Time (Minutes)",
        yaxis_title="Order Count"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# =====================================================
# TAB 2 — FORECASTING
# =====================================================

with tab2:

    st.subheader("📈 7-Day Demand Forecast")

    forecast_display = forecast_df.tail(7).copy()

    forecast_display.columns = [
        "Date",
        "Predicted Orders"
    ]

    forecast_display["Predicted Orders"] = (
        forecast_display["Predicted Orders"]
        .round(0)
        .astype(int)
    )

    st.dataframe(
        forecast_display,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📊 Projected Demand Trend")

    forecast_chart = px.line(
        forecast_display,
        x="Date",
        y="Predicted Orders",
        title="Projected Daily Orders",
        markers=True
    )

    forecast_chart.update_layout(
        xaxis_title="Date",
        yaxis_title="Predicted Orders"
    )

    st.plotly_chart(
        forecast_chart,
        use_container_width=True
    )

    st.markdown("---")

    st.info("""
    Forecasts indicate relatively stable short-term demand patterns,
    making rider scheduling and operational planning more predictable.
    """)

# =====================================================
# TAB 3 — RECOMMENDATIONS
# =====================================================

with tab3:

    st.subheader("🚀 Executive Recommendations")

    st.markdown("""
    ## 1. City-Specific Rider Allocation

    Peak demand windows vary significantly across cities.

    Implement city-wise rider scheduling instead of uniform staffing models
    to improve operational efficiency during peak hours.
    """)

    st.markdown("---")

    st.markdown("""
    ## 2. Dynamic Surge Optimization

    Surge pricing alone does not sufficiently reduce delivery delays.

    Combine surge activation with proactive rider balancing and demand forecasting
    to reduce operational bottlenecks.
    """)

    st.markdown("---")

    st.markdown("""
    ## 3. Forecast-Driven Operations

    Demand patterns remain predictable over short forecasting horizons.

    Use rolling demand forecasts to improve rider positioning and reduce SLA breaches
    during lunch and dinner peaks.
    """)

    st.markdown("---")

    st.success("""
    Expected Operational Outcomes:
    - Improved delivery SLA adherence
    - Reduced peak-hour rider shortages
    - Better surge pricing efficiency
    - Improved customer experience
    """)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Built using Streamlit, Plotly, Pandas, and Prophet for operational demand analytics and forecasting."
)