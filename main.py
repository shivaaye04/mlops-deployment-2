from fastapi import FastAPI
import mlflow
import os

app = FastAPI()

# Environment variable se URL uthayega, nahi toh local IP use karega
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://10.128.62.53:5000")
mlflow.set_tracking_uri(tracking_uri)

model = mlflow.pyfunc.load_model("models:/MyModel/1")

@app.get("/")
def home():
    return {"message": "MLflow Model API Running"}

@app.get("/predict")
def predict():
    return {"prediction": "Model prediction will come here"}