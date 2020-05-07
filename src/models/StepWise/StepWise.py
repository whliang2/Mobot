# ***************************************************************************************
# *    Title: Applying Wrapper Methods in Python for Feature Selection
# *    Author: Usman Malik
# *    Date: NA
# *    Availability: https://stackabuse.com/applying-wrapper-methods-in-python-for-feature-selection/
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


class StepWise(LinearModelInterface):
    def __init__(self, predictor_name: list, response_name: list):
        self._predictor_name = predictor_name
        self._response_name = response_name

    def exec(self, data: pd.DataFrame, criteria: dict = None) -> list:
        while True:
            X = data[self._predictor_name]
            Y = data[self._response_name]
            model = sm.OLS(Y, X).fit()

            results_as_html = model.summary().tables[1].as_html()
            result = pd.read_html(results_as_html, header=0, index_col=0)[0]
            not_satisfy_predictor = result[result['P>|t|'] > criteria['p_value']]
            if len(not_satisfy_predictor) > 0:
                max_p = not_satisfy_predictor['P>|t|'].max()
                new_predictor_df = result[result['P>|t|'] != max_p]
                new_predictor = list(new_predictor_df.index)
                self._predictor_name = new_predictor

            else:
                # build result
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
    print('### StepWise ###')

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
    # print(training.columns)


    # here we have 2 variables for the multiple linear regression.
    # If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example
    criteria = {
        'p_value': 0.05
    }
    predictor_name = ["Health.expenditures....of.GDP.", "Literacy...."]
    response_name = ['Recovery Rate']


    model = StepWise(predictor_name, response_name)
    result = model.exec(training, criteria)
    print(result)
