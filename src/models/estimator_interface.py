import pandas as pd


class EstimatorInterface:
    def fit(self, x_train: pd.DataFrame, y_train: pd.DataFrame) -> object:
        pass

    def predict(self, x_test: pd.DataFrame) -> pd.DataFrame:
        pass

    @staticmethod
    def save(model: object, path: str = 'model.joblib'):
        pass

    @staticmethod
    def load(model_path: str):
        pass
