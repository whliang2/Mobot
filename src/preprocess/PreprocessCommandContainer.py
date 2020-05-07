from typing import Any
from typing import TypeVar
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface


class PreprocessCommandContainer:
    """
    This class is for registering preprocess command
    """
    def __init__(self):
        self._steps = {}

    def register(self, step_name, step: PreprocessCommandInterface):
        self._steps[step_name] = step

    def get(self, step_name):
        if step_name in self._steps.keys():
            return self._steps[step_name]
        else:
            print(f"Command [{step_name}] not recognised")