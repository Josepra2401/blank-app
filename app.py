
import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("engine_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🔧 Engine Condition Predictor")
st.markdown("Predict if an engine is **Healthy (1)** or needs **Maintenance (0)** using sensor data.")

# Create inputs for each sensor
sensor_inputs = []
for i in range(1, 13):  # sensor_1 to sensor_12
    value = st.number_input(f"Sensor {i}", format="%.4f")
    sensor_inputs.append(value)

# Predict button
if st.button("🔍 Predict Engine Condition"):
    df = pd.DataFrame([sensor_inputs], columns=[f"sensor_{i}" for i in range(1, 13)])
    prediction = model.predict(df)[0]

    if prediction == 1:
        st.success("✅ Prediction: Engine is Healthy")
    else:
        st.error("⚠️ Prediction: Engine may FAIL - Maintenance Needed")
