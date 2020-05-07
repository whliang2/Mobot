import os
import pandas as pd
import sys
sys.path.append('../../../')

from src.utils.Importer.ImporterInterface import ImporterInterface


class CsvFetcher(ImporterInterface):
    def fetch(self, profiles: list) -> list:
        '''
            return a list of dataframe inside the source folder or empty dataframe if error happened
        '''
        result = []
        # read file to df and append to result list
        # TODO: handle huge files
        for profile in profiles:
            for file_name in profile['files']:
                try:
                    file = profile['dir']+file_name
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
    files = [{
        'dir': '../../../data/source/',
        'files': ['he_li_pd.csv', 'death_recovery_gdp_unemp_withnan.csv']
    }, {
        'dir': '../../../data/preprocessed/',
        'files': ['covid_19.csv']
    }]
    df_list = csv_fetcher.fetch(files)
    print(df_list)