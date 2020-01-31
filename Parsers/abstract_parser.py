import pandas as pd
from abc import ABC, abstractmethod


class AbstractDataParser(ABC):

    @abstractmethod
    def parse_file(self, filename: str) -> pd.DataFrame:
        """
        None, overwritten by subclass.
        :param filename: Path to filename in zipfile.
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
