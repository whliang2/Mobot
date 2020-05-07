# ---
# The bridge class  that bind source drivers and client api for execution
# ---
import sys
sys.path.append('../../../../')

from typing import TypeVar
from src.preprocess.utils.Source.SourceInterface import SourceInterface
from src.preprocess.utils.Interface.ManagerInterface import ManagerInterface

SourceType = TypeVar('SourceType', object, SourceInterface)


class SourceManager(ManagerInterface):
    def __init__(self, source_type: SourceType):
        self._source_type = source_type

    def exec(self, directory):
        return self._source_type.fetch(directory)


if __name__ == '__main__':
    print('### SourceManager ###')


