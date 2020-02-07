import pandas as pd

class AgeMerger:

    def __init__(self, populationdf):
        self.data_frame = self.agemerger(populationdf)

    def agemerger(self, populationdf):
        # print(dataframe)
        # print(populationdf)
        row1 = sum(populationdf[:50])
        # print(row1)
        row2 = sum(populationdf[50:60])
        row3 = sum(populationdf[60:65])
        row4 = sum(populationdf[65:70])
        row5 = sum(populationdf[70:75])
        row6 = sum(populationdf[75:80])
        row7 = sum(populationdf[80:85])
        row8 = sum(populationdf[85:90])
        row9 = sum(populationdf[90:])
        dataframe = pd.DataFrame([row1, row2, row3, row4, row5, row6, row7, row8, row9], columns=['Age'])
        # print(dataframe)
        return dataframe

    def get_data_frame(self):
        return self.data_frame
