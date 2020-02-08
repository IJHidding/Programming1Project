"""
Author = "Iwan Hidding"

This class builds upon the abstract processor class. It takes a data frame with population data and merges the age
columns into the same values that are used for the data in the deaths data frame. I can only apologize for the current
state of the row selection. As the data about the years are all set in meta data files which are difficult to parse
it is easier to hard code it this way. This function will very specifically get the sum of population data.
"""
import pandas as pd
from Processing.abstractprocessor import AbstractProcessor


class AgeMerger(AbstractProcessor):

    def __init__(self, populationdf):
        """
        Runs the logic within this class. The get_data_frame function can be used to pull the dataframe out of the class
        after the logic.
        :param populationdf: A data frame containing population data from the CBS website
        """
        self.data_frame = self.method(populationdf)

    def method(self, populationdf):
        """
        This function creates a data frame with the age percentages from a province summed to match the ages from the
        deaths data frame.
        :param populationdf: A data frame containing population data from the CBS website
        :return: A data frame containing summed columns according to the age values.
        """
        row1 = sum(populationdf[:50])
        row2 = sum(populationdf[50:60])
        row3 = sum(populationdf[60:65])
        row4 = sum(populationdf[65:70])
        row5 = sum(populationdf[70:75])
        row6 = sum(populationdf[75:80])
        row7 = sum(populationdf[80:85])
        row8 = sum(populationdf[85:90])
        row9 = sum(populationdf[90:])
        dataframe = pd.DataFrame([row1, row2, row3, row4, row5, row6, row7, row8, row9], columns=['Age'])
        return dataframe

    def get_data_frame(self):
        """
        The function which gives a method to get the data frame from the class.
        :return: Returns final dataframe
        """
        return self.data_frame
