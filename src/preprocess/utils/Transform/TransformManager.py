# ---
# The bridge class  that bind transform object and client api for execution
# ---
import sys
import pandas as pd
sys.path.append('../../../../')

from typing import TypeVar
from src.preprocess.utils.Interface.ManagerInterface import ManagerInterface
from src.preprocess.utils.Transform.TransformInterface import TransformInterface

TransformType = TypeVar('TransformType', object, TransformInterface)


class TransformManager(ManagerInterface):
    def __init__(self, transform_type: TransformType):
        self._transform_type = transform_type

    def exec(self, data: pd.DataFrame, column_name: str):
        return self._transform_type.transform(data, column_name)


if __name__ == '__main__':
    print('### TransformManager ###')



