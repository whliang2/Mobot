# ***************************************************************************************
# *    Title: Akaike’s Information Criterion: Definition, Formulas
# *    Author: Stephanie
# *    Date: Sep 7, 2015
# *    Availability: https://www.statisticshowto.com/akaikes-information-criterion/
# *
# ***************************************************************************************

import ast
import pandas as pd
import statsmodels.api as sm
import sys

from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from math import log
from sklearn.metrics import mean_squared_error
from itertools import combinations
from src.models.Interface.LinearModelInterface import LinearModelInterface

sys.path.append('../../../')

# calculate aic for regression
def calculate_aic(n, mse, num_params):
    aic = n * log(mse) + 2 * num_params
    return aic


def train_aic_model(X, y):
    # Train model
    model = sm.OLS(y, X).fit()
    num_params = len(model.params.to_numpy()) + 1

    yhat = model.predict(X)
    # calculate the error
    mse = mean_squared_error(y, yhat)
    # print('MSE: %.3f' % mse)
    # calculate the aic
    aic = calculate_aic(len(y), mse, num_params)
    # print('AIC: %.3f' % aic)
    return aic, model


def rSubset(arr, r):
    return list(combinations(arr, r))


class AIC(LinearModelInterface):
    def __init__(self, predictor_name: list, response_name: list):
        self._predictor_name = predictor_name
        self._response_name = response_name

    def exec(self, df: pd.DataFrame, criteria: dict = None) -> list:

        aic_info_dict = {}

        for x in range(len(self._predictor_name)):
            for column_tuple in rSubset(self._predictor_name, x):
                column_list = list(column_tuple)
                X = df[column_list]
                y = df[self._response_name]
                if X.shape[1] != 0:
                    aic_score, model = train_aic_model(X, y)
                    aic_info_dict[str(column_list)] = aic_score, model

        result_columns = min(aic_info_dict, key=aic_info_dict.get)
        result_column_name_list = ast.literal_eval(result_columns)

        # result_aic_score = aic_info_dict[result_columns][0]
        result_model = aic_info_dict[result_columns][1]
        est_y = result_model.predict(df[result_column_name_list])
        y_list = list(df[self._response_name].values)
        y = pd.DataFrame(y_list)
        est_y_list = list(est_y)
        est_y = pd.DataFrame(est_y_list)

        resid = [x - y for x, y in zip(y_list, est_y_list)]
        resid = pd.DataFrame(resid)

        result_df = pd.concat([y, est_y, resid], axis=1)
        result_df.columns = ['  Y   ', 'Y_Predicted', 'Residual']

        return (result_model, result_column_name_list, result_df)


if __name__ == '__main__':
    print('### AIC ###')

    ratio_splitter = SplitFactory('ratio').generate()
    importer_object = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer_object)
    files = [{
        'dir': '../../../data/preprocessed/',
        'files': ['new_covid19.csv']
    }]
    data = importer_manager.exec(files)[0]

    training, testing = SplitManager(ratio_splitter).exec(data, {'ratio': 0.8})

    selected_column = ['health_expend', 'literacy', 'physicians_density', 'obesity',
                       'life_expect', 'h_bed_density', 'imigrate_rate']

    aic_object = AIC(selected_column, ['recovery_rate'])
    result = aic_object.exec(training)
    print(result)
