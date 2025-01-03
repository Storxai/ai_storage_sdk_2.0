from joblib import load
from PIL import Image
import numpy as np
from src.utils.ai_helpers import handle_compression

class AICompression:
    def __init__(self, model_path="models/ai_compression_advanced.pkl"):
        self.model = load(model_path)

    def compress_file(self, input_file: str, file_type: str, output_file: str) -> str:
        return handle_compression(input_file, file_type, self.model, output_file)
