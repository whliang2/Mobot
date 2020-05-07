import pandas as pd
from abc import ABC, abstractmethod


class ImputatorInterface(ABC):
    """
        Define data cleaning process functions for replace missing value
    """
    @staticmethod
    @abstractmethod
    def impute(data: pd.DataFrame, column_name: str) -> None:
        pass
