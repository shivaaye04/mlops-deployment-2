import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
import os

# Environment variable se URL uthayega, nahi toh local IP use karega
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://10.128.62.53:5000")
mlflow.set_tracking_uri(tracking_uri)

model = LogisticRegression()

with mlflow.start_run():
    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="MyModel"
    )