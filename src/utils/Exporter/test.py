import sys
import pandas as pd
from src.utils.Exporter.ExportManager import ExportManager
from src.utils.Exporter.ExportFactory import ExportFactory
sys.path.append('../../../')

data = {'First_Name':  ["Henry","Andy","Jane"],
        'Last_name': ["Liang", "Lin","Su"],
        }

df_test = pd.DataFrame(data, columns = ['First_Name','Last_name'])
target_directory = '../../../data/raw'


if __name__ == '__main__':
    exporter_object = ExportFactory('csv').generate()
    exporter_manager = ExportManager(exporter_object)
    exporter_manager.exec(df_test, target_directory, 'test')


