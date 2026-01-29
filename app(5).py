import streamlit as st
import numpy as np
import joblib

st.title("Fraud Detection System")

# LOAD MODEL
pipeline = joblib.load("fraud_detection_model.pkl")

# Example inputs (change according to your dataset)
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = pipeline.predict(input_data)

    if prediction[0] == 1:
        st.error("Fraud Transaction Detected 🚨")
    else:
        st.success("Normal Transaction ✅")
