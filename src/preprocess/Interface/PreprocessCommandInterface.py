import pandas as pd

from abc import ABC, abstractmethod
from typing import Any


class PreprocessCommandInterface(ABC):
    """
        This interface is for framing the action preprocess action
    """
    @abstractmethod
    def exec(self, *args: Any) -> pd.DataFrame:
        pass
