import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load("fraud_model.pkl")

# Title
st.title("Credit Card Fraud Detection")
st.markdown("Enter transaction details to predict if it's fraud or not.")

# Input features
st.header("Input Transaction Data")

# Manual input for all 30 features
time = st.number_input("Time", min_value=0.0, step=1.0)
amount = st.number_input("Amount", min_value=0.0, step=0.01)

# PCA features V1 to V28
v_features = {}
for i in range(1, 29):
    v_features[f"V{i}"] = st.number_input(f"V{i}", value=0.0, step=0.01)

# Prepare input dataframe
input_data = {
    "Time": time,
    **v_features,
    "Amount": amount
}

# Make prediction
if st.button("Predict"):
    X_input = pd.DataFrame([input_data])  # Convert to DataFrame
    prediction = model.predict(X_input)[0]
    prob = model.predict_proba(X_input)[0][1]

    if prediction == 1:
        st.error(f"🚨 Fraud Detected! Probability: {prob:.2f}")
    else:
        st.success(f"✅ Legitimate Transaction. Probability of fraud: {prob:.2f}")
