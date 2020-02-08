import pandas as pd
from functools import reduce
from Processing.abstractprocessor import AbstractProcessor


class DataframeNormalizer(AbstractProcessor):

    def __init__(self, normalizer, dataframe):
        self.data_frame = self.method(normalizer, dataframe)

    def method(self, normalizer, dataframe):
        # print(dataframe)
        # print(normalizer)
        return dataframe / (normalizer + 1) * 1000

    def get_data_frame(self):
        return self.data_frame
