import pandas as pd
from bokeh.plotting import show
import numpy as np
import sys
from Parsers.csv_parser import CsvParser
from Parsers.Onlineparser import OnlineParser
from Processing.SingleColumnConcer import DataframeConcer
from Processing.SingleColumnAdder import DataframeAdder
from Processing.merger import DataframeMerger
from Processing.Deathsmerger import DeathAgeMerger
from Processing.pca_analyzer import PcaAnalysis
from Processing.normalizer import DataframeNormalizer
from Visualizers.plotter import Plotter



def main():
    # returns a dataframe from that province.
    Bevolking_leeftijd = CsvParser('Data/03759ned_UntypedDataSet_05022020_161839.csv',
                                   "Groningen").get_data_frame()[1:]
    # print(Bevolking_leeftijd)
    Nature_recreation = CsvParser('Data/70262ned_UntypedDataSet_05022020_180935.csv',
                                  "Groningen").get_data_frame().iloc[:, [3, 4]]
    # print(Nature_recreation)
    Deaths = CsvParser('Data/80202ned_UntypedDataSet_31012020_123258.csv',
                       "Groningen").get_data_frame().iloc[:, [1, 2, 3, 4, 5]]
    print(Deaths)
    Distances = CsvParser('Data/80305ned_UntypedDataSet_31012020_124042.csv',
                          "Groningen").get_data_frame().iloc[:, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16]]
    # print(Distances)
    tablequality = OnlineParser("https://www.rivm.nl/media/milieu-en-leefomgeving/hoeschoonisonzelucht/",
                                'Groningen').get_data_frame().iloc[:, [2, 3]]
    # print(tablequality)


    ##### Change bevolking to groups per deaths
    ### change column "Leeftijd" to value below and add column "deaths" with the sum of these groups.
    ## Directly add column of sum of deaths to df with the sum of the ages.




    # print(numbersofdistance)
    combined_single_rows = DataframeConcer(Distances, tablequality).get_data_frame()
    # combined_single_rows = DataframeConcer(combined_single_rows, ).get_data_frame()
    combined_single_rows = DataframeConcer(combined_single_rows, Nature_recreation).get_data_frame()
    # combined_single_rows = pd.concat([Distances.reset_index().iloc[:, [i for i in range(1, len(Distances.columns))]],
                                      # tablequality.reset_index().iloc[:, [1, 2]]], axis=1)
    # print(combined_single_rows.columns)
    singlerowsadded = DataframeAdder(Bevolking_leeftijd, combined_single_rows).get_data_frame()

    # print(singlerowsadded)
    Merged1 = DataframeMerger(Deaths, singlerowsadded, on="Leeftijd").get_data_frame()
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
    # Big_Frame = pd.concat([Gron_merged, Flev_merged], ignore_index=True)
    #
    # pca_dataframe = PcaAnalysis(Big_Frame).get_data_frame()
    # plot = Plotter("PCA", pca_dataframe).get_plot()
    # show(plot)
    # print(parser)
    # csv parser
    # merger
    # pca analyzer
    # plotter

    pass


if __name__ == "__main__":
    sys.exit(main())
