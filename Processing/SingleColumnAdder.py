"""
Author = "Iwan Hidding"

The class builds upon the abstract processor. It takes a data frame with multiple rows and a data frame with a single
row and adds the single row data behind each row of the larger data frame. This is used as the chosen structure for the
data is multiple rows per province with columns consisting of age ranges and deaths per age range. Then constant values
like air quality and average distance to hospitals can be added for each rows as the are the same for each age.
"""
from Processing.abstractprocessor import AbstractProcessor


class DataframeAdder(AbstractProcessor):

    def __init__(self, dataframe, singles):
        """
        Runs the logic within this class. The get_data_frame function can be used to pull the data frame out of the class
        after the logic.
        :param dataframe: Any data frame containing multiple rows
        :param singles:  Any data frame containing only one row
        """
        self.data_frame = self.method(dataframe, singles)

    def method(self, dataframe, singles):
        """
        This function adds the single rowed data frame behind the multiple rowed data frame so that it gets added to
        every row.
        :param dataframe: Any data frame containing multiple rows
        :param singles: Any data frame containing only one row
        :return: returns the data frame with added columns
        """
        for column in singles.columns:
            dataframe[column] = singles.iloc[0][column]
        return dataframe

    def get_data_frame(self):
        """
        The function which gives a method to get the data frame from the class.
        :return: Returns final data frame
        """
        return self.data_frame