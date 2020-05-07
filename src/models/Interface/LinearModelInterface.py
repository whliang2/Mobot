import pandas as pd

from abc import ABC, abstractmethod


class LinearModelInterface(ABC):
    """
    Interface for linear Model
    """
    @abstractmethod
    def __init__(self, criteria):
        pass

    def exec(self, dataframe: pd.DataFrame):
        pass