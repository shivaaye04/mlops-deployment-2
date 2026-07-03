from fastapi import FastAPI
import mlflow
import os

app = FastAPI()

model = mlflow.pyfunc.load_model("mlartifacts/0/models/m-8b217a65e6c0426bb9ddd83fbda5e258")

@app.get("/")
def home():
    return {"message": "MLflow Model API Running"}

@app.get("/predict")
def predict():
    return {"prediction": "Model prediction will come here"} 