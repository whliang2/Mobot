from abc import ABC, abstractmethod


class FactoryInterface(ABC):
    @abstractmethod
    def generate(self) -> object:
        pass