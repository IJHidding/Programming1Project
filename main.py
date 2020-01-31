import pandas as pd
import bokeh
import numpy as np
import sys
from Parsers.csv_parser import CsvParser
from Processing.merger import DataframeMerger
from Processing.pca_analyzer import PcaAnalysis
# from Visualizers.plotter import Plotter


def main():
    # returns a dataframe from that province.
    Gron1 = CsvParser("Data/03759ned_UntypedDataSet_31012020_123704.csv", "Groningen").get_data_frame()
    Gron2 = CsvParser("Data/80202ned_UntypedDataSet_31012020_123258.csv", "Groningen").get_data_frame()
    Gron3 = CsvParser("Data/80305ned_UntypedDataSet_31012020_124042.csv", "Groningen").get_data_frame()
    Flev1 = CsvParser("Data/03759ned_UntypedDataSet_31012020_123704.csv", "Flevoland").get_data_frame()
    Flev2 = CsvParser("Data/80202ned_UntypedDataSet_31012020_123258.csv", "Flevoland").get_data_frame()
    Flev3 = CsvParser("Data/80305ned_UntypedDataSet_31012020_124042.csv", "Flevoland").get_data_frame()

    # merging data
    #dataframe = parser.get_data_frame()
    Gron_merged = DataframeMerger(Gron1, Gron2, Gron3).get_data_frame()
    Flev_merged = DataframeMerger(Flev1, Flev2, Flev3).get_data_frame()

    Big_Frame = pd.concat([Gron_merged, Flev_merged], ignore_index=True)

    pca = PcaAnalysis(Big_Frame).get_data_frame()
    # print(parser)
    # csv parser
    # merger
    # pca analyzer
    # plotter

    pass


if __name__ == "__main__":
    sys.exit(main())
