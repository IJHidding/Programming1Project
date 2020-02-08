"""
Author = "Iwan Hidding"

This class builds upon the abstract data parser. It takes a sitename and a province. For future use, a table variable is
added as this functions downloads data from an online website when run. As this website might change by adding or
removing a table, this variable can be changed to fix this. Also if more data is taken from different websites this can
easily be incorporated to any website containing tables.
"""
import pandas as pd
from Parsers.abstract_parser import AbstractDataParser


class OnlineParser(AbstractDataParser):

    def __init__(self, sitename: str, province: str, table=4):
        """
        Runs the logic within this class. The get_data_frame function can be used to pull the dataframe out of the class
        after the logic.
        :param sitename: A name of a website containing data tables.
        :param province: The name of a Dutch province for data selection.
        :param table: An integer variable which selects the table number from the website can be updated if the website
        changes
        """
        self.data_frame = self.parse_file(sitename, table)
        self.organize_data_types(province)

    def parse_file(self, sitename: str, table):
        """
        Simple function that reads the website using the pd.read_html function. Then grabs the table which corresponds
        with the numbered variable.
        :param sitename: A name of a website containing data tables.
        :param table: An integer variable which selects the table number from the website can be updated if the website
        changes
        :return: returns the table as a pandas data frame.
        """
        return pd.read_html(sitename)[table]

    def organize_data_types(self, province):
        """
        Selects the province from the datatable to only take that province.
        :param province: The name of a Dutch province for data selection.
        """
        self.data_frame = self.data_frame.loc[self.data_frame['provincie'] == province]

    def get_data_frame(self):
        """
        The function which gives a method to get the data frame from the class.
        :return: Returns final dataframe
        """
        return self.data_frame
