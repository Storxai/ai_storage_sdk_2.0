from joblib import load
from src.utils.ai_helpers import predict_cost_based_on_storage

class AICostPrediction:
    def __init__(self, model_path="models/ai_cost_prediction_advanced.pkl"):
        self.model = load(model_path)

    def predict_cost(self, storage_size: float) -> float:
        return predict_cost_based_on_storage(storage_size, self.model)
