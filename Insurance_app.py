import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Title
st.title("Insurance Charges Predictor")

st.write("Enter the details below to predict insurance charges.")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)

children = st.number_input("Children", min_value=0, max_value=10, value=0)

sex = st.selectbox("Sex", ["male", "female"])

smoker = st.selectbox("Smoker", ["yes", "no"])

# Predict Button
if st.button("Predict Insurance Charges"):

    # Feature Engineering
    is_female = 1 if sex == "female" else 0
    is_smoker = 1 if smoker == "yes" else 0

    bmi_category_Obese = 1 if bmi >= 30 else 0

    # Default region value
    region_southeast = 1

    # EXACT SAME COLUMN ORDER AS TRAINING
    input_data = pd.DataFrame([[ 
        age,
        is_female,
        bmi,
        children,
        is_smoker,
        region_southeast,
        bmi_category_Obese
    ]], columns=[
        'age',
        'is_female',
        'bmi',
        'children',
        'is_smoker',
        'region_southeast',
        'bmi_category_Obese'
    ])

    # Prediction
    prediction = model.predict(input_data)

    # Output
    st.success(f"Estimated Insurance Charges: ${prediction[0]:.2f}")