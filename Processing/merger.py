import pandas as pd
from functools import reduce

class DataframeMerger:

    def __init__(self, *args):
        self.data_frame = self.merger(*args)

    def merger(self, *args):
        return reduce(lambda left, right: pd.merge(left, right, left_index=True, right_index=True,
                                                        how='outer'), args)

    def get_data_frame(self):
        return self.data_frame
