import pandas as pd
import sys

sys.path.append('../../')

from typing import Any
from src.preprocess.utils.Transform.TransformFactory import TransformFactory
from src.preprocess.utils.Transform.TransformManager import TransformManager
from src.preprocess.utils.Source.CsvFetcher import CsvFetcher
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface


class Transformation(PreprocessCommandInterface):
    def __init__(self, info: dict):
        """
        Create Transformation
        :param info: {
            type: 'log'
            data: pd.DataFrame
        }
        """
        self._info = info

    def exec(self, columns: list, dataframe: pd.DataFrame = None) -> pd.DataFrame:
        transform = TransformFactory(self._info['type']).generate()
        transformer = TransformManager(transform)
        for column in columns:
            transformer.exec(dataframe, column)
        return dataframe


if __name__ == '__main__':
    print('### Transformation ###')
    source_directory = '../../data/preprocessed'
    target_directory = '../../data/imputed'

    csv_fetcher = CsvFetcher()
    data = csv_fetcher.fetch(source_directory)[0]
    print(data)

    # create csv fetcher object
    log_transformation = TransformFactory('log').generate()

    # execute get resource
    transform = TransformManager(log_transformation)

    # impute missing value (N/A) with mean
    transform.exec(data, 'Literacy....')
    print(data)
