# Food Delivery Demand Pulse

## Problem Statement
A food delivery platform wants to understand demand spikes, surge inefficiencies, and operational bottlenecks across cities.

---

## Dataset
- ~50,000 synthetic food delivery orders
- 7 cities
- 9 cuisines
- 90-day period

---

## Tech Stack
- Python
- Pandas
- Plotly
- Streamlit
- Prophet

---

## Key Insights
- Evening demand significantly exceeds lunch demand.
- Bangalore and Mumbai show highest operational load.
- Surge pricing alone does not fully reduce delivery delays.

---

## Forecasting
Implemented a 7-day short-horizon demand forecast using Prophet.

---

## Executive Recommendations

### 1. City-Specific Rider Allocation
Optimize rider staffing based on city-level demand patterns.

### 2. Dynamic Surge Optimization
Combine surge pricing with proactive rider balancing.

### 3. Forecast-Driven Operations
Use demand forecasts to improve peak-hour rider positioning.

---

## Dashboard Features
- KPI tracking
- Demand heatmaps
- Delivery time analysis
- Forecast table
- City and cuisine filters

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

---

## Live Demo
https://case3-food-delivery-demand-pulse-9fpkaptmq5vyvjecwa963k.streamlit.app/

---

## Repository Structure

```text
data/
notebooks/
outputs/
app/
README.md
DECISIONS.md
```

---

## Dashboard Preview

### Main KPI
![dashboard](assets/screenshots/kpis.png)

### Demand Heatmap
![heatmap](assets/screenshots/heatmap.png)

### Forecast Section
![forecast](assets/screenshots/forecast.png)