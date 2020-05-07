import pandas as pd

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface


class ZeroImputator(ImputatorInterface):
    """
        Substitute missing value by 0
    """

    @staticmethod
    def impute(data: pd.DataFrame, column_name: str) -> None:
        data[column_name].fillna(0, inplace=True)
