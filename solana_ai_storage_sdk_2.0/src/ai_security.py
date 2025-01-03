from joblib import load
import numpy as np
from src.utils.ai_helpers import analyze_file_for_anomalies

class AISecurity:
    def __init__(self, model_path="models/ai_security_advanced.pkl"):
        self.model = load(model_path)

    def analyze_file(self, file_path: str) -> bool:
        return analyze_file_for_anomalies(file_path, self.model)
