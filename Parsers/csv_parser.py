"""
Author = "Iwan Hidding"

This class builds upon the abstract data parser. It takes a filename and a province. Then uses a provinces translation
dictionary to go from province name to the code used in the CBS data. For future use, a perioden variable was added
which can change the year taken from the data. It is currently set the 2015 as data of air quality from this year is
used for the current analysis
"""
import pandas as pd
from Parsers.abstract_parser import AbstractDataParser


class CsvParser(AbstractDataParser):

    def __init__(self, filename: str, province: str, perioden="2015JJ00"):
        """
        Runs the logic within this class. The get_data_frame function can be used to pull the dataframe out of the class
        after the logic.
        :param filename: A filename in string format with a csv extention. In this case only from CBS as their csvs are
        ";" separated.
        :param province: A province name in string, Which is translated using a dictionary within the function.
        :param perioden: An optional variable used to select a year from the region. Currently unused, but lets the
        program be updated if more data is available.
        """
        self.data_frame = self.parse_file(filename)
        self.organize_data_types(province, perioden)

    def parse_file(self, filename: str):
        """
        Simple pd.read function with the right separator.
        :param filename: A filename in string format with a csv extention. In this case only from CBS as their csvs are
        ";" separated.
        :return: returns the csv as a pandas dataframe
        """

        return pd.read_csv(filename, sep=";", low_memory=False)

    def organize_data_types(self, province, perioden):
        """
        This function gets called from the init and selects the right data from the self.data_frame. It does not return
        anything as the self.data_frame gets updated from within.
        :param province: A province name in string, Which is translated using a dictionary within the function.
        :param perioden: An optional variable used to select a year from the region. Currently unused, but lets the
        program be updated if more data is available.
        """
        dict_of_provinces = {"Groningen": "PV20  ", "Friesland": "PV21  ", "Drenthe": "PV22  ", "Overijssel": "PV23  ",
                           "Flevoland": "PV24  ", "Gelderland": "PV25  ", "Utrecht": "PV26  ", "Noord-Holland": "PV27  ",
                           "Zuid-Holland": "PV28  ", "Zeeland": "PV29  ", "Noord_Brabant": "PV30  ", "Limburg": "PV31  "}

        self.data_frame = self.data_frame.loc[self.data_frame['RegioS'] == dict_of_provinces[province]]
        self.data_frame = self.data_frame.loc[self.data_frame['Perioden'] == perioden]

    def get_data_frame(self):
        """
        The function which gives a method to get the data frame from the class.
        :return: Returns final dataframe
        """
        return self.data_frame
