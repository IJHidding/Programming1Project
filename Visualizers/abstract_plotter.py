from abc import ABC, abstractmethod


class AbstractPlotter(ABC):

    @abstractmethod
    def _data_selection(self, colnames: str) -> None: pass

    @abstractmethod
    def _settings(self, title: str) -> object: pass

    @abstractmethod
    def get_plot(self):
        pass
