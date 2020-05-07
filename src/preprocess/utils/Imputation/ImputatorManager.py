# ---
# The bridge class  that bind imputation object and client api for execution
# ---
import sys

import pandas as pd

sys.path.append('../../../../')

from typing import TypeVar
from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface
from src.preprocess.utils.Interface.ManagerInterface import ManagerInterface

ImputatorType = TypeVar('ImputatorType', object, ImputatorInterface)


class ImputatorManager(ManagerInterface):
    def __init__(self, imputation_type: ImputatorType):
        self._imputation_type = imputation_type

    def exec(self, data: pd.DataFrame, column_name: str) -> None:
        # execute imputation without copying a new dataframe
        self._imputation_type.impute(data, column_name)


if __name__ == '__main__':
    print('### ImputatorManager ###')
