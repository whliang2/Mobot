from abc import ABC, abstractmethod


class SourceInterface(ABC):
    """
        Define the interface of each source fetcher
    """

    @abstractmethod
    def fetch(self, source_directory: str):
        pass
