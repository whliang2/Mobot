# ***************************************************************************************
# *    Title: Linear Regression
# *    Author: Seabold, Skipper, and Josef Perktold
# *    Date: 2010
# *    Code version: v0.11.1
# *    Availability: https://www.statsmodels.org/stable/regression.html
# *
# ***************************************************************************************

import statsmodels.api as sm
import pandas as pd
import sys

from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from src.models.Interface.LinearModelInterface import LinearModelInterface

sys.path.append('../../../')


class SimpleLm(LinearModelInterface):
    def __init__(self, predictor_name: list, response_name: list):
        self._predictor_name = predictor_name
        self._response_name = response_name

    def exec(self, data: pd.DataFrame, criteria: dict = None) -> list:
        X = data[self._predictor_name]
        Y = data[self._response_name]
        model = sm.OLS(Y, X).fit()
        est_y = model.predict(X).to_frame()
        est_y_list = list(est_y.values)
        est_y = pd.DataFrame(est_y_list)
        resid = model.resid.to_frame()
        resid_list = list(resid.values)
        resid = pd.DataFrame(resid_list)
        y_list = list(Y.values)
        Y = pd.DataFrame(y_list)
        result_df = pd.concat([Y, est_y, resid], axis=1, sort=False)
        result_df.columns = ['  Y   ', 'Y_Predicted','Residual']
        predictor = model.params.index.to_list()

        return (model, predictor, result_df)


if __name__ == '__main__':
    print('### Simple Linear Model')

    # get source
    loader = SourceFactory('csv').generate()
    data = SourceManager(loader).exec('../../../data/preprocessed')[0]

    # initialize split object
    ratio_splitter = SplitFactory('ratio').generate()
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

    importer_object = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer_object)

    files = [{
        'dir': '../../../data/preprocessed/',
        'files': ['covid19_preprocessed.csv']
    }]
    data = importer_manager.exec(files)[0]

    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

    predictor_name = ["Health.expenditures....of.GDP.", "Literacy...."]
    response_name = ['Recovery Rate']


    model = SimpleLm(predictor_name, response_name)
    result = model.exec(data)
    print(result)