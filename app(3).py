import streamlit as st
import pickle
import numpy as np
import joblib
# Load trained model
from sklearn.pipeline import Pipeline

pipeline = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection System")

st.write("Enter transaction details")

amount = st.number_input("Transaction Amount")
oldbalanceOrg = st.number_input("Old Balance Sender")
newbalanceOrig = st.number_input("New Balance Sender")
oldbalanceDest = st.number_input("Old Balance Receiver")
newbalanceDest = st.number_input("New Balance Receiver")

if st.button("Check Fraud"):
    features = np.array([[amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction!")
    else:
        st.success("✅ Legit Transaction")
