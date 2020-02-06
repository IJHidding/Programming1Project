import pandas as pd
from functools import reduce

class DataframeAdder:

    def __init__(self, dataframe, singles):
        self.data_frame = self.adder(dataframe, singles)

    def adder(self, dataframe, singles):
        # print(dataframe)

        for column in singles.columns:
            # print(singles.iloc[0][column])
            # print('test1')
            dataframe[column] = singles.iloc[0][column]
        return dataframe

    def get_data_frame(self):
        return self.data_frame