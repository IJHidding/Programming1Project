import pandas as pd
from Parsers.abstract_parser import AbstractDataParser


class CsvParser(AbstractDataParser):

    def __init__(self, filename: str, province: str, Perioden="2015JJ00"):
        self.data_frame = self.parse_file(filename)
        self.organize_data_types(province, Perioden)


    def parse_file(self, filename: str):

        return pd.read_csv(filename, sep=";", low_memory=False)

    def organize_data_types(self, province, Perioden):

        dict_of_provinces = {"Groningen": "PV20  ", "Friesland": "PV21  ", "Drenthe": "PV22  ", "Overijssel": "PV23  ",
                           "Flevoland": "PV24  ", "Gelderland": "PV25  ", "Utrecht": "PV26  ", "Noord-Holland": "PV27  ",
                           "Zuid-Holland": "PV28  ", "Zeeland": "PV29  ", "Noord_Brabant": "PV30  ", "Limburg": "PV31  "}

        self.data_frame = self.data_frame.loc[self.data_frame['RegioS'] == dict_of_provinces[province]]
        self.data_frame = self.data_frame.loc[self.data_frame['Perioden'] == Perioden]
        #self.data_frame = self.data_frame.set_index('Perioden', 'Leeftijd')


    def get_data_frame(self):

        return self.data_frame
