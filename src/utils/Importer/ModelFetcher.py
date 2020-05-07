import os
import pandas as pd
import sys
sys.path.append('../../../')
from joblib import dump, load
from src.utils.Importer.ImporterInterface import ImporterInterface


class ModelFetcher(ImporterInterface):

    def fetch(self, profiles:list):
        model_list=[]
        for profile in profiles:
            for file_name in profile['files']:
                    file = profile['dir']+file_name
                    model = load(file)
                    model_list.append(model)

        return model_list


if __name__ == '__main__':
    print("Hello")
    print("=====")

    files = [{
        'dir': '../../../data/model/models/',
        'files': ["sklearn_AIC.pkl","statsmodels_SimpleLm","statsmodels_StepWise_0.1","statsmodels_StepWise_0.01","statsmodels_StepWise_0.02"]
    }]


    model_fetcher = ModelFetcher()
    aic_test = model_fetcher.fetch(files)
    print(aic_test)