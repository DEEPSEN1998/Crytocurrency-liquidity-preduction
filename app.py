import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🔍 Crypto Liquidity Predictor")
st.write("Enter the following market metrics to predict liquidity class")

# Replace with actual selected feature names
feature_names = ['total_volume', 'market_cap', 'liquidity_ratio', 'log_volume',
                 'log_market_cap', 'log_price', 'price_change_pct', 
                 'volume_rolling_mean_3d', 'volume_rolling_std_3d', 
                 'price_volatility_7d']

inputs = []

for feat in feature_names:
    val = st.number_input(f"{feat}", format="%.6f")
    inputs.append(val)

if st.button("Predict"):
    prediction = model.predict(np.array(inputs).reshape(1, -1))[0]
    st.success(f"Predicted Liquidity Class: {'High' if prediction == 1 else 'Low'}")
