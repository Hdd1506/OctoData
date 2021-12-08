import numpy as np
from joblib import dump, load

from src.models.estimator_interface import EstimatorInterface


class BaseModel(EstimatorInterface):
    def __init__(self, model: object = None):
        self.model = model

    def fit(self, x_train: np.ndarray, y_train: np.ndarray) -> object:
        return self.model.fit(x_train, y_train)

    def predict(self, x_test: np.ndarray) -> np.ndarray:
        return self.model.predict(x_test)

    def load(self, model_path: str):
        model = load(model_path)
        self.model = model

    @staticmethod
    def save(model: object, path: str = 'model.joblib'):
        dump(model, path)
