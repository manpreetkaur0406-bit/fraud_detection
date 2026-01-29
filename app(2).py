import streamlit as st
import numpy as np
import joblib

st.title("Fraud Detection System")

# LOAD MODEL
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

MODEL_FILE = "fraud_detection_model.pkl"

if os.path.exists(MODEL_FILE):
    pipeline = joblib.load(MODEL_FILE)
else:
    # Create and save a simple model if file missing
    X_dummy = np.random.rand(100, 3)
    y_dummy = np.random.randint(0, 2, 100)

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ])

    pipeline.fit(X_dummy, y_dummy)
    joblib.dump(pipeline, MODEL_FILE)

# Example inputs (change according to your dataset)
features = np.array([amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest])
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Transaction Amount", 0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance Sender", 0.0, value=1000.0)
newbalanceOrig = st.number_input("New Balance Sender", 0.0, value=900.0)
oldbalanceDest = st.number_input("Old Balance Receiver", 0.0, value=0.0)
newbalanceDest = st.number_input("New Balance Receiver", 0.0, value=0.0)


if st.button("Check Fraud"):
    features = np.array([[amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction!")
    else:
        st.success("✅ Legit Transaction")

