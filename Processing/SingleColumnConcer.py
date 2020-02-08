"""
Author = "Iwan Hidding"

This class builds upon the abstract processor. It takes two data frames and adds the rows behind each other. This is
used here the add all the single rows together to then run the SingleColumnAdder.py only once. It would be better if
this function could take more than two data frames and concat but so far this implementation has not been completed.
"""
import pandas as pd
from Processing.abstractprocessor import AbstractProcessor


class DataframeConcer(AbstractProcessor):

    def __init__(self, df1, df2):
        """
        Runs the logic within this class. The get_data_frame function can be used to pull the dataframe out of the class
        after the logic.
        :param df1: Any data frame
        :param df2: Any data frame
        """
        self.data_frame = self.method(df1, df2)

    def method(self, df1, df2):
        """
        This adds any two data frames together by concatenating the second one behind the first.
        :param df1: Any data frame
        :param df2: Any data frame
        :return: The combined data frames
        """
        conceddf = pd.concat(
            [df1.reset_index().iloc[:, [i for i in range(1, len(df1.columns)+1)]],
             df2.reset_index().iloc[:, [i for i in range(1, len(df2.columns)+1)]]], axis=1)
        return conceddf

    def get_data_frame(self):
        """
        The function which gives a method to get the data frame from the class.
        :return: Returns final dataframe
        """
        return self.data_frame
