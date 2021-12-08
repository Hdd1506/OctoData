from sklearn.tree import DecisionTreeClassifier

from src.models.base_model import BaseModel


class DecisionTreeModel(BaseModel):
    def __init__(self, max_depth: int = 4, criterion: str = 'entropy'):
        self.max_depth = max_depth
        self.criterion = criterion

        super().__init__(
            model=DecisionTreeClassifier(
                max_depth=self.max_depth,
                criterion=self.criterion
            )
        )
