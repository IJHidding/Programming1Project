import pandas as pd


class DataframeConcer:

    def __init__(self, df1, df2):
        self.data_frame = self.concer(df1, df2)

    def concer(self, df1, df2):
        # print(dataframe)
        # print(df2)
        conceddf = pd.concat(
            [df1.reset_index().iloc[:, [i for i in range(1, len(df1.columns)+1)]],
             df2.reset_index().iloc[:, [i for i in range(1, len(df2.columns)+1)]]], axis=1)
        return conceddf

    def get_data_frame(self):
        return self.data_frame
