import os
import pandas as pd
import sys
sys.path.append('../../../')

from src.preprocess.utils.Source.SourceInterface import SourceInterface


class CsvFetcher(SourceInterface):
    def fetch(self, source_directory: str) -> list:
        '''
            return a list of dataframe inside the source folder or empty dataframe if error happened
        '''
        source_name = os.listdir(os.path.abspath(source_directory))
        source_files = [f'{source_directory}/{name}' for name in source_name]
        result = []

        # read file to df and append to result list
        # TODO: handle huge files
        for file in source_files:
            if file.endswith('.csv'):
                try:
                    # use latin-1 encoding method
                    df = pd.read_csv(file, encoding="ISO-8859-1", index_col=0)
                    result.append(df)

                except Exception as e:
                    # append empty list if error happened
                    print(e)
                    result.append(pd.DataFrame())

        return result


if __name__ == '__main__':
    print('### CsvFetcher ###')
    csv_fetcher = CsvFetcher()
    df_list = csv_fetcher.fetch('../../../data/source')
    print(df_list)