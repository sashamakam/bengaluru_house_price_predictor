from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React runs here by default with Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('models/house_price_model.pkl')
model_columns = joblib.load('models/model_columns.pkl')
locations = joblib.load('models/locations.pkl')


class inputdetails(BaseModel):
    location :str
    total_sqft: float
    bath: int
    bhk: int


@app.get("/locations")
async def getlocations():
    return {"locations": "locations"}


@app.post("/predict")
async def predict(request: inputdetails):
    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0

    input_df['total_sqft'] = request.total_sqft
    input_df['bhk'] = request.bhk
    input_df['bath'] = request.bath

    location_column = f"location_{request.location}"
    if location_column in model_columns:
        input_df[location_column] = 1

    predicted_price = model.predict(input_df)[0]

    return {
        "predicted_price": round(float(predicted_price), 2),
        "location": request.location,
        "total_sqft": request.total_sqft,
        "bhk": request.bhk,
        "bath": request.bath,
        "unit": "lakhs"
    }


