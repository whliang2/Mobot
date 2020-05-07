import pandas as pd
import sys

sys.path.append('../../')

from typing import Any
from src.preprocess.utils.Imputation.ImputatorFactory import ImputatorFactory
from src.preprocess.utils.Imputation.ImputatorManager import ImputatorManager
from src.preprocess.utils.Source.CsvFetcher import CsvFetcher
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface


class Imputation(PreprocessCommandInterface):
    def __init__(self, info: dict):
        """
        Create Imputation object
        :param info: {
            type: 'mean'
        }
        """
        self._info = info

    def exec(self, columns: list, dataframe: pd.DataFrame = None) -> pd.DataFrame:
        imputation = ImputatorFactory(self._info['type']).generate()
        imputator = ImputatorManager(imputation)
        for column in columns:
            imputator.exec(dataframe, column)

        return dataframe

if __name__ == '__main__':
    print('### Imputation ###')
    source_directory = '../../data/preprocessed'
    target_directory = '../../data/imputed'

    csv_fetcher = CsvFetcher()
    data = csv_fetcher.fetch(source_directory)[0]
    print(data)

    # create csv fetcher object
    mean_imputation = ImputatorFactory('mean').generate()

    # execute get resource
    imputator = ImputatorManager(mean_imputation)

    # impute missing value (N/A) with mean
    imputator.exec(data, 'Pop_Density')
    print(data)
