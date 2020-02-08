import pandas as pd
from functools import reduce
from Processing.abstractprocessor import AbstractProcessor


class DataframeMerger(AbstractProcessor):

    def __init__(self, *args, on):
        # print(on)
        self.data_frame = self.method(*args, on=on)

    def method(self, *args, on):
        return reduce(lambda left, right: pd.merge(left, right, left_on=[on],
                                                   right_on=[on],
                                                   how='outer'), args)

    def get_data_frame(self):
        return self.data_frame
