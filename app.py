import joblib
import streamlit as st
from fastapi import FastAPI

app = FastAPI()
model = joblib.load("regression.joblib")

@app.get("/predict")
async def predict(data: Dict):
    price = model.predict([data['size'], data['nb_bedrooms'], data['has_garden']])[0]
    return {"price": price}

