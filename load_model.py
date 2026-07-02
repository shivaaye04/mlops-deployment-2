import mlflow
import pickle

# Environment variable backup ke liye
model = mlflow.pyfunc.load_model("mlartifacts")

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")