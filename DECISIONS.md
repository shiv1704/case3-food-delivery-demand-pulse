# Decisions Log — Food Delivery Demand Pulse

## Assumptions
- Assumed timestamps are in local city timezone.
- Assumed surge_applied is binary.
- Assumed historical demand patterns remain stable over short forecasting horizons.

---

## Trade-offs

| Choice | Alternative | Reason |
|---|---|---|
| Prophet | LSTM | Simpler and more explainable for short-horizon forecasting |
| Streamlit | Full React Dashboard | Faster deployment and lower engineering overhead |
| City-Level Forecasting | Cuisine-Level Forecasting | Reduced sparsity and stronger signal |

---

## What I De-scoped
- Real-time rider tracking
- Weather integration
- Live streaming ingestion
- Rider-route optimization

---

## What I Would Improve Next
- Add real-time streaming pipeline
- Add city-level forecasting models
- Integrate weather and traffic datasets
- Add SLA breach monitoring