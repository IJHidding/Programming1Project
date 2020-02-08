"""
Author = "Iwan Hidding"

This is an abstract class from the abstract factory design pattern. It is used as a basis for the plotting functions in
this program.
"""
from abc import ABC, abstractmethod


class AbstractPlotter(ABC):

    @abstractmethod
    def _settings(self, title: str) -> object:
        """
        None, overwritten by subclass.
        """
        pass

    @abstractmethod
    def get_plot(self):
        """
        None, overwritten by subclass.
        """
        pass
