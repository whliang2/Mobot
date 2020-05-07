import pandas as pd

from abc import ABC, abstractmethod


class TransformInterface(ABC):
    """
        Define the interface of each transformer
    """

    @abstractmethod
    def transform(self, data: pd.DataFrame, column_name: str) -> None:
        pass
