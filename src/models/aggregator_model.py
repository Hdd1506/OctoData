import numpy as np
from joblib import load

from src.models.base_model import BaseModel


class AggregatorModel(BaseModel):
    def __init__(self, models: list = None):
        super().__init__()
        self.models = models

    def fit(self, x_train: np.ndarray, y_train: np.ndarray) -> object:
        return [
            model.fit(x_train, y_train) for model in self.models
        ]

    def predict(self, x_test: np.ndarray) -> np.ndarray:
        return (np.mean([
            model.predict(x_test) for model in self.models
        ], axis=0) == 1).astype(int)

    def load(self, model_path: str):
        models = load(model_path).models
        self.models = models
