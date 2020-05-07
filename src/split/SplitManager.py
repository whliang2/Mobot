import pandas as pd
import sys
sys.path.append('../../')

from typing import TypeVar, Any
from src.split.SplitInterface import SplitInterface
SplitType = TypeVar('SplitType', object, SplitInterface)


class SplitManager:
    def __init__(self, split_type: SplitType):
        self._split_type = split_type

    def exec(self, dataframe: pd.DataFrame, criteria: Any):
        return self._split_type.split(dataframe, criteria)


if __name__ == '__main__':
    print('### Split Manager ###')