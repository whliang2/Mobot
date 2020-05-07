import pandas as pd
from abc import ABC, abstractmethod
from typing import Any


class ExportInterface(ABC):
    """
        Define the interface of each exporter
    """
    @staticmethod
    @abstractmethod
    def save_file(target: Any, target_dir: str, file_name: str):
        pass