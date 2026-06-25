import os
import pickle

# Environment variable backup ke liye
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "./mlruns")

# Direct model.pkl file se model load ho raha hai
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")