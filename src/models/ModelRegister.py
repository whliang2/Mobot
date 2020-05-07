import pandas as pd
import sys
sys.path.append('../../')

from src.models.Interface.LinearModelInterface import LinearModelInterface

class ModelRegister:
    """
    This class is for registering preprocess command
    """
    def __init__(self):
        self._models = {}

    @property
    def get_models(self):
        return self._models

    def register(self, model_name, model, predictor_name: list, response_name: list):
        self._models[model_name] = model(predictor_name, response_name)

    def exec(self, model_name, data: pd.DataFrame, criteria: dict = None):
        if model_name in self._models.keys():
            return self._models[model_name].exec(data, criteria)
        else:
            print(f"Command [{model_name}] not recognised")