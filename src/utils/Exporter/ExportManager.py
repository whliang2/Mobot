import sys
sys.path.append('../../../')

from typing import TypeVar, Any
from src.utils.Exporter.ExportInterface import ExportInterface
from src.utils.Interface.ManagerInterface import ManagerInterface

ExportType = TypeVar('ExportType', object, ExportInterface)


class ExportManager(ManagerInterface):
    def __init__(self, export_type: ExportType):
        self._export_type = export_type

    def exec(self,target: Any, target_dir: str, file_name: str):
        return self._export_type.save_file(target, target_dir, file_name)


if __name__ == '__main__':
    print('### ExportManager ###')