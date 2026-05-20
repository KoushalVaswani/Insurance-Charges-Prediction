import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Insurance Charges Predictor")

age = st.number_input("Age", 18, 100)
bmi = st.number_input("BMI", 10.0, 50.0)
children = st.number_input("Children", 0, 10)

smoker = st.selectbox("Smoker", ["yes", "no"])
sex = st.selectbox("Sex", ["male", "female"])

# Convert categorical values
smoker = 1 if smoker == "yes" else 0
sex = 1 if sex == "male" else 0

input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Charges: ${prediction[0]:.2f}")