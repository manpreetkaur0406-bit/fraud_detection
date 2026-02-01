import streamlit as st
import pandas as pd
import joblib   # ✅ missing import added

# Load trained model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")

# User Inputs
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT"])
amount = st.number_input("Amount", min_value=0.0, value=100.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=0.0)
newbalanceOrg = st.number_input("New Balance (Sender)", min_value=0.0, value=0.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Prediction Button
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrg": newbalanceOrg,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:   # ✅ colon added
        st.error("🚨 This transaction may be FRAUD!")
    else:
        st.success("✅ This transaction looks SAFE.")
