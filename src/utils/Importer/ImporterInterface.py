from abc import ABC, abstractmethod


class ImporterInterface(ABC):
    """
        Define the interface of each source fetcher
    """

    @abstractmethod
    def fetch(self, profiles: list):
        pass
