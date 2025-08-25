import streamlit as st
import pandas as pd
import joblib
import pickle

# ===============================
# Load Data and Model
# ===============================
DATA_PATH = "quickr_car_cleaned_by_shaunak.csv"
MODEL_PATH = "LinearRegressionModel_Shaunak.pkl"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Load model safely (try joblib first)
try:
    model = joblib.load(MODEL_PATH)
except:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

# ===============================
# Streamlit UI
# ===============================
st.title("Shaunak's 🚗 Car Price Predictor")
st.markdown("### This app uses Machine Learning Model to estimate your car price.")
st.markdown("Note: Predictions are based on Quikr’s used car dataset and may contain some margin of error")

# First dropdown → company
company = st.selectbox("Select Company", sorted(df["company"].unique()))

# Filter models for that company only
filtered_models = df[df["company"] == company]["name"].unique()
car_model = st.selectbox("Select Model", sorted(filtered_models))

# Fuel type dropdown
fuel_type = st.selectbox("Fuel Type", sorted(df["fuel_type"].unique()))

# Numerical inputs
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2015)
kilometers = st.number_input("Kilometers Driven", min_value=0, value=30000)

# ===============================
# Prediction
# ===============================
if st.button("Predict Price"):
    try:
        # Match training format
        input_data = pd.DataFrame(
            [[car_model, company, year, kilometers, fuel_type]],
            columns=["name", "company", "year", "kms_driven", "fuel_type"]
        )

        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Car Price: ₹{prediction:,.2f}")

    except Exception as e:
        st.error(f"Error in prediction: {e}")








