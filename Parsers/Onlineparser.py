import pandas as pd
from Parsers.abstract_parser import AbstractDataParser


class OnlineParser(AbstractDataParser):

    def __init__(self, filename: str, province: str):
        self.data_frame = self.parse_file(filename)
        self.organize_data_types(province)


    def parse_file(self, sitename: str):

        return pd.read_html(sitename)[4]

    def organize_data_types(self, province):

        self.data_frame = self.data_frame.loc[self.data_frame['provincie'] == province]


    def get_data_frame(self):

        return self.data_frame
