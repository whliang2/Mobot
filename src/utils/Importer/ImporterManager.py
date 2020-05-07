# ---
# The bridge class  that bind source drivers and client api for execution
# ---
import sys
sys.path.append('../../../')

from typing import TypeVar
from src.utils.Importer.ImporterInterface import ImporterInterface
from src.preprocess.utils.Interface.ManagerInterface import ManagerInterface

SourceType = TypeVar('SourceType', object, ImporterInterface)


class ImporterManager(ManagerInterface):
    def __init__(self, source_type: SourceType):
        self._source_type = source_type

    def exec(self, profile: list):
        return self._source_type.fetch(profile)


if __name__ == '__main__':
    print('### ImporterManager ###')


