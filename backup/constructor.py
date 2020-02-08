import pandas as pd
from Processing.abstractprocessor import AbstractProcessor


class DFConstructor(AbstractProcessor):

    def __init__(self, *args):
        self.data_frame = self.method(args)

    def method(self, *args):
        print(*args)
        dataframe = pd.DataFrame.from_records(*args)
        return dataframe

    def get_data_frame(self):
        return self.data_frame
