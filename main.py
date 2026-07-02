from fastapi import FastAPI
import mlflow
import os

app = FastAPI()

model = mlflow.pyfunc.load_model("mlartifacts")

@app.get("/")
def home():
    return {"message": "MLflow Model API Running"}

@app.get("/predict")
def predict():
    return {"prediction": "Model prediction will come here"}