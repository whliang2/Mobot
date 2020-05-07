from abc import ABC, abstractmethod
from typing import Any


class ManagerInterface(ABC):
    @abstractmethod
    def exec(self, *args, **kwargs) -> Any:
        pass
