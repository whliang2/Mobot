import pandas as pd

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface


class MedianImputator(ImputatorInterface):
    """
        Substitute missing value by median value
    """

    @staticmethod
    def impute(data: pd.DataFrame, column_name: str) -> None:
        data[column_name].fillna((data[column_name].median()), inplace=True)
