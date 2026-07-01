import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model1.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🍇 Raisin Classification")

st.write("Enter the details below")

# User Inputs
Area = st.number_input("Area", value=80000.0)

MajorAxisLength = st.number_input("Major Axis Length", value=400.0)

MinorAxisLength = st.number_input("Minor Axis Length", value=250.0)

Eccentricity = st.number_input(
    "Eccentricity",
    min_value=0.0,
    max_value=1.0,
    value=0.80
)

ConvexArea = st.number_input("Convex Area", value=85000.0)

Extent = st.number_input(
    "Extent",
    min_value=0.0,
    max_value=1.0,
    value=0.70
)

Perimeter = st.number_input("Perimeter", value=1100.0)

# Predict Button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Area":[Area],
        "MajorAxisLength":[MajorAxisLength],
        "MinorAxisLength":[MinorAxisLength],
        "Eccentricity":[Eccentricity],
        "ConvexArea":[ConvexArea],
        "Extent":[Extent],
        "Perimeter":[Perimeter]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Prediction : Kecimen Raisin")
    else:
        st.success("Prediction : Besni Raisin")
