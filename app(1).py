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
