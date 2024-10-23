import streamlit as st
import joblib

model = joblib.load("regression.joblib")
size = st.number_input("Size")
nb_bedrooms = st.number_input("Number of bedrooms")
has_garden = st.number_input("Has a garden")

price = model.predict([size, nb_bedrooms, has_garden])[0]

st.write(f"The price of the house is {price}.")
