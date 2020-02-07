import pandas as pd
from bokeh.plotting import show
import numpy as np
import sys
from Parsers.csv_parser import CsvParser
from Parsers.Onlineparser import OnlineParser
from Processing.SingleColumnConcer import DataframeConcer
from Processing.SingleColumnAdder import DataframeAdder
from Processing.merger import DataframeMerger
from Processing.agemerger import AgeMerger
from Processing.pca_analyzer import PcaAnalysis
from Processing.normalizer import DataframeNormalizer
from Processing.constructor import DFConstuctor
from Visualizers.plotter import Plotter

def ProvinceSelector(Province):
    Bevolking_leeftijd = CsvParser('Data/03759ned_UntypedDataSet_05022020_161839.csv',
                                   Province).get_data_frame().iloc[:, [2, 6]][1:]
    Bevolking_leeftijd_correction = CsvParser('Data/03759ned_UntypedDataSet_05022020_161839.csv',
                                              Province).get_data_frame().iloc[:, [2, 6]][:1]

    Bevolking_leeftijd_corrected = (Bevolking_leeftijd['BevolkingOp1Januari_1'].astype(int).div(
        int(Bevolking_leeftijd_correction['BevolkingOp1Januari_1'].iloc[0]))) * 100

    Bevolking_percentage = AgeMerger(Bevolking_leeftijd_corrected).get_data_frame()

    # Deaths
    Deaths = CsvParser('Data/80202ned_UntypedDataSet_31012020_123258.csv',
                       Province).get_data_frame().drop(columns=["ID","Geslacht","Leeftijd","RegioS","Perioden"])
    # .iloc[:, [1, 2, 3, 4, 5]]
    Deaths_corrected = (Deaths.fillna(0).astype(int).div(
        int(Bevolking_leeftijd_correction['BevolkingOp1Januari_1'].iloc[0]))) * 100000
    # print(Deaths_corrected)

    Nature_recreation = CsvParser('Data/70262ned_UntypedDataSet_05022020_180935.csv',
                                  Province).get_data_frame().iloc[:, [1, 3, 4]]
    # print(Nature_recreation)

    # print(Deaths)
    Distances = CsvParser('Data/80305ned_UntypedDataSet_31012020_124042.csv',
                          Province).get_data_frame().iloc[:, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
    # print(Distances)
    tablequality = OnlineParser("https://www.rivm.nl/media/milieu-en-leefomgeving/hoeschoonisonzelucht/",
                                Province).get_data_frame().iloc[:, [2, 3]]
    # print(tablequality)
    # print(tablequality)
    # Population = CsvParser("Data/70072ned_UntypedDataSet_29122019_191739.csv",
    #                        Province).get_data_frame().iloc[:, [15, 16, 17, 18, 19, 20, 21, 22, 23]]
    # print(Bevolking_percentage.values.tolist())

    finaldataframe = Deaths_corrected[1:]
    finaldataframe['Age'] = Bevolking_percentage
    # finaldataframe['Deaths'] = Deaths_corrected[1:].values.tolist()
    # print(finaldataframe)
    # print(DFConstuctor(Bevolking_percentage.iloc[:, [0]].values.tolist(), Deaths["TotaalAlleOnderliggendeDoodsoorzaken_1"][1:].values.tolist()).get_data_frame())

    # print(Population.columns)
    # print(Bevolking_leeftijd)
    # column1 = Population.iloc[0].tolist()
    ##### Change bevolking to groups per deaths
    ### change column "Leeftijd" to value below and add column "deaths" with the sum of these groups.
    ## Directly add column of sum of deaths to df with the sum of the ages.

    # print(numbersofdistance)
    combined_single_rows = DataframeConcer(Distances, tablequality).get_data_frame()
    # combined_single_rows = DataframeConcer(combined_single_rows, ).get_data_frame()
    combined_single_rows = DataframeConcer(combined_single_rows, Nature_recreation).get_data_frame()
    # print(combined_single_rows)
    # combined_single_rows = pd.concat([Distances.reset_index().iloc[:, [i for i in range(1, len(Distances.columns))]],
    # tablequality.reset_index().iloc[:, [1, 2]]], axis=1)
    # print(combined_single_rows.columns)
    singlerowsadded = DataframeAdder(finaldataframe, combined_single_rows).get_data_frame()
    return singlerowsadded



def main():
    Gron_dataframe = ProvinceSelector("Groningen")
    Flev_dataframe = ProvinceSelector("Flevoland")
    # Dren_dataframe = ProvinceSelector("Drenthe")
    # Geld_dataframe = ProvinceSelector("Gelderland")
    # Over_dataframe = ProvinceSelector("Overijssel")
    # Fries_dataframe = ProvinceSelector("Friesland")
    # Noord_dataframe = ProvinceSelector("Noord-Holland")

    # print(Gron_dataframe, Flev_dataframe)

    # print(singlerowsadded)
    # Merged1 = DataframeMerger(Deaths, singlerowsadded, on="Leeftijd").get_data_frame()
    # print(Merged1)
    # print(DataframeMerger(Distances, tablequality, on=0))
    # NormalizerGron = CsvParser("Data/03759ned_UntypedDataSet_31012020_123704.csv", "Groningen").get_data_frame()
    # Gron1 = CsvParser("Data/80202ned_UntypedDataSet_31012020_123258.csv", "Groningen").get_data_frame()[:5]
    # Gron2 = CsvParser("Data/80305ned_UntypedDataSet_31012020_124042.csv", "Groningen").get_data_frame()
    # NormalizerFlev = CsvParser("Data/03759ned_UntypedDataSet_31012020_123704.csv", "Flevoland").get_data_frame()
    # Flev1 = CsvParser("Data/80202ned_UntypedDataSet_31012020_123258.csv", "Flevoland").get_data_frame()[:5]
    # Flev2 = CsvParser("Data/80305ned_UntypedDataSet_31012020_124042.csv", "Flevoland").get_data_frame()

    # # normalizer
    # NormalizedGron1 = DataframeNormalizer(NormalizerGron['BevolkingOp1Januari_1'], Gron1, 14)
    # NormalizedGron2 = DataframeNormalizer(NormalizerGron['BevolkingOp1Januari_1'], Gron2)
    # NormalizedFlev1 = DataframeNormalizer(NormalizerFlev['BevolkingOp1Januari_1'], Flev1, 14)
    # NormalizedFlev2 = DataframeNormalizer(NormalizerFlev['BevolkingOp1Januari_1'], Flev2)


    # merging data
    #dataframe = parser.get_data_frame()
    # Gron_merged = DataframeMerger(Gron1, Gron2).get_data_frame()
    # Flev_merged = DataframeMerger(Flev1, Flev2).get_data_frame()
    #
    Big_Frame = pd.concat([Gron_dataframe, Flev_dataframe], ignore_index=True)
    #
    pca_dataframe = PcaAnalysis(Big_Frame).get_data_frame()
    plot = Plotter("PCA", pca_dataframe).get_plot()
    show(plot)
    # print(parser)
    # csv parser
    # merger
    # pca analyzer
    # plotter

    pass


if __name__ == "__main__":
    sys.exit(main())
