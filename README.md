# 📊 Cryptocurrency Liquidity Prediction for Market Stability

This project builds a machine learning pipeline to predict cryptocurrency **liquidity** for improving market **stability and forecasting**. It uses historical data from CoinGecko and is deployed with **Streamlit** for real-time usage.

---

## 🧩 System Overview

This system uses machine learning techniques to analyze trends in cryptocurrency markets and predict liquidity, a crucial indicator of financial market stability.

---

## 🧱 System Modules

### 1. 📥 Data Ingestion
- Load historical data from CSV (CoinGecko).
- Parse and standardize columns, including date formats.

### 2. 🧼 EDA & Preprocessing
- Handle missing values using mean/mode imputation.
- Clip outliers (Winsorization from 5th–95th percentile).
- Generate summary statistics and visualizations.

### 3. 🏗️ Feature Engineering
- Derive relevant statistical and time-series features.
- Identify and retain features correlated with liquidity.

### 4. 🤖 Model Training
- Use ML models like:
  - RandomForestRegressor
  - XGBoost
  - LSTM (for time-series)
- Train models on historical data and tune hyperparameters.

### 5. 📈 Evaluation & Prediction
- Measure performance using RMSE, MAE, and R².
- Generate liquidity predictions and assess accuracy.

### 6. 🚀 Deployment
- The model is deployed using **Streamlit**.
- Users can upload new CSV files, trigger predictions, and visualize the results via an interactive web app.

---

## 🔁 ML Pipeline Architecture

```plaintext
┌────────────────┐
│ Data Ingestion │
└──────┬─────────┘
       ↓
┌────────────────────┐
│ Data Preprocessing │ ← Handle NA, date, outliers
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Feature Selection  │
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Model Training     │ ← LogisticRegression / ARIMA  etc.
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Evaluation & Tuning│
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Prediction & Report│
└────────────────────┘
