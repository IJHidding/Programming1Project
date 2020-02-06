import pandas as pd
from functools import reduce

class DataframeNormalizer:

    def __init__(self, normalizer, dataframe):
        self.data_frame = self.Normalizer(normalizer, dataframe)

    def Normalizer(self, normalizer, dataframe):
        # print(dataframe)
        # print(normalizer)
        return dataframe / (normalizer + 1) * 1000

    def get_data_frame(self):
        return self.data_frame
