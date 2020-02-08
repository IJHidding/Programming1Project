"""
Author = "Iwan Hidding"

This is an abstract class from the abstract factory design pattern. It is used as a basis for the Processor functions in
this program.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd


class AbstractProcessor(ABC):

    @abstractmethod
    def method(self) -> pd.DataFrame:
        """
        None, overwritten by subclass.
        """
        pass

    @abstractmethod
    def get_data_frame(self) -> pd.DataFrame:
        """
        None, overwritten by subclass.
        """
        pass
