import pandas as pd

class DFConstuctor:

    def __init__(self, *args):
        self.data_frame = self.constructor(args)

    def constructor(self, *args):
        print(*args)
        dataframe = pd.DataFrame.from_records(*args)
        return dataframe

    def get_data_frame(self):
        return self.data_frame
