import pandas as pd

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface


class MeanImputator(ImputatorInterface):
    """
        Substitute missing value by mean value
    """

    @staticmethod
    def impute(data: pd.DataFrame, column_name: str) -> None:
        data[column_name].fillna((data[column_name].mean()), inplace=True)

