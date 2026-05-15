# Decisions Log — Case 3

## Assumptions I made

1. Timestamps are in local city timezone — because no UTC offset was provided in the dataset, and city-level demand patterns only make sense in local time.
2. `surge_applied` is a binary flag — because the column had only 0/1 values; treated as on/off rather than a multiplier.
3. Historical demand patterns remain stable over short forecasting horizons — because the dataset covers only 90 days, so training on the full window and forecasting 7 days forward is reasonable.
4. City is the right granularity for forecasting — because cuisine-level demand was too sparse to produce reliable Prophet fits.

---

## Trade-offs

| Choice | Alternative | Why I picked this |
|---|---|---|
| Prophet | LSTM | Simpler, explainable, and requires far less data to converge on a short horizon |
| Streamlit | Full React Dashboard | Faster deployment and no frontend build tooling needed |
| City-level forecasting | Cuisine-level forecasting | Reduced data sparsity and produced stronger, more stable signals |
| Static dataset | Live API ingestion | Keeps the scope achievable; real-time layer is a production concern |

---

## What I de-scoped and why

- Real-time streaming ingestion — requires Kafka/Flink infrastructure; not justified for a static 90-day dataset
- Weather and traffic integration — no API key available and would introduce significant data-prep overhead
- Rider-route optimization — needs geospatial coordinates which are absent from the dataset
- Cuisine-level forecasting — data too sparse per cuisine per city for Prophet to fit reliably

---

## What I'd do differently with another day

- Add per-city model versioning so forecasts can be retrained independently as new data arrives.
- Integrate a drift-detection step that flags when actuals deviate significantly from forecast confidence bands.
- Replace the static CSV with a live Postgres table fed by a streaming pipeline.
- Build a lightweight alerting layer that pings ops when a city is forecast to breach SLA thresholds.
