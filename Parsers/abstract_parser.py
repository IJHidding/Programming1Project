"""
Author = "Iwan Hidding"

This is an abstract class from the abstract factory design pattern. It is used as a basis for the parser functions in
this program.
"""
import pandas as pd
from abc import ABC, abstractmethod


class AbstractDataParser(ABC):

    @abstractmethod
    def parse_file(self, filename: str) -> pd.DataFrame:
        """
        None, overwritten by subclass.
        """
        pass

    @abstractmethod
    def organize_data_types(self) -> None:
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
