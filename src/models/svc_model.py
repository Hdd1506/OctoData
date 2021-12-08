from sklearn.svm import SVC

from src.models.base_model import BaseModel


class SVCModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(
            model=SVC(**kwargs)
        )
