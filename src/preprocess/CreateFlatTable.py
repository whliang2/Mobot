import pandas as pd
import sys

sys.path.append('../../')

from functools import reduce
from src.preprocess.utils.Source.SourceManager import SourceManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface


class CreateFlatTable(PreprocessCommandInterface):
    def __init__(self, source_dir: str, info: dict):
        """
        Init CreateFlatTable
        :param source_dir:
        :param info: {
            merge_key: 'Country'
            from_type: 'csv'
        }
        """
        self._source_dir = source_dir
        self._info = info

    def exec(self) -> pd.DataFrame:
        """
        Create flat table from all the csv file within source folder
        :return: None
        """
        loader = SourceFactory(self._info['from_type']).generate()
        fetcher = SourceManager(loader)
        dfs = fetcher.exec(self._source_dir)
        result = self.merge_files(dfs, self._info['merge_key'])
        return result

    @staticmethod
    def merge_files(dataframe_list: list, merge_key: str):
        return reduce(lambda left, right: pd.merge(left, right, on=merge_key), dataframe_list)


if __name__ == '__main__':
    print('### CreateFlatTable ###')

    source_directory = '../../data/source'
    table_creator = CreateFlatTable(source_directory, {'merge_key': 'Country', 'from_type': 'csv'})
    df = table_creator.exec()
    print(df)
