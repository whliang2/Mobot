from abc import ABC, abstractmethod


class SplitInterface(ABC):
    @abstractmethod
    def split(self, *args):
        pass
