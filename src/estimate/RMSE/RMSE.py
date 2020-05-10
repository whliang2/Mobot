import pandas as pd
import numpy as np
import sys

sys.path.append('../../../')

from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from numba import jit


@jit(nopython=True)
def cal_rmse(y_pred: np.array, y_true: np.array):
    result = np.sqrt(np.mean((y_pred - y_true) ** 2))
    return result


class RMSE:
    @staticmethod
    def get_rmse(testing_data: pd.DataFrame, predictors: list, response: list, model):
        y_pred = model.predict(testing_data[predictors]).to_numpy()
        y_true = testing_data[response].to_numpy()
        rmse = cal_rmse(y_true, y_pred)
        return rmse


if __name__ == '__main__':
    print("### RMSE ###")

    # get source
    source_dir = [{
        'dir': '../../../data/split/',
        'files': ['training.csv']
    }, {
        'dir': '../../../data/split/',
        'files': ['testing.csv']
    }]
    importer = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer)
    training, testing = importer_manager.exec(source_dir)

    # Import Model
    model_files = [{
        'dir': '../../../data/model/models/',
        'files': ["SimpleLm"]
    }]
    fetcher_object = ImporterFactory('model').generate()
    model_object = ImporterManager(fetcher_object)
    model_obj = model_object.exec(model_files)[0]

    # Test Parameters
    predictors_list = ['Health.expenditures....of.GDP.', 'Literacy....',
                       'Physicians.density..physicians.1.000.population.',
                       'Obesity - adult prevalence rate (%)',
                       'Life expectancy at birth (years)', 'H_bed_density',
                       'Imigrate_Rate', 'Pop_Density', 'GDP - per capita (PPP) (US$)',
                       'Unemployment rate (%)']
    response_list = ['Recovery Rate']

    # Test Class Static Method
    RMSE_Object = RMSE()
    answer = RMSE_Object.get_rmse(testing, predictors_list, response_list, model_obj)
    print(answer)
