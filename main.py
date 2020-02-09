"""
Author= "Iwan Hidding"
Version= "1.0"

This is the main.py script of the Programming1project program. This program calls all the other parts of the program
which parses the files, processes the data and then visualizes the result. It can be run from inside any python IDE
or from the command line. By default it uses all the provinces, but by setting any number of Dutch provinces from the
command line any combination can be set.
"""

import pandas as pd
from bokeh.plotting import show
from bokeh.layouts import gridplot, row, column
import argparse
import sys
from Parsers.csv_parser import CsvParser
from Parsers.Onlineparser import OnlineParser
from Processing.SingleColumnConcer import DataframeConcer
from Processing.SingleColumnAdder import DataframeAdder
from Processing.agemerger import AgeMerger
from Processing.pca_analyzer import PcaAnalysis
from Visualizers.plotter import ScatterPlotter
from Visualizers.barplot import BarPlotter
from Visualizers.textplot import TextPlotter


def ProvinceSelector(province):
    """
    As the data can be selected per province a function was created to load all the files with an option for province.
    It takes the province as a string, additional translation into data codes is done in the parsers.
    It returns a data frame containing all data available for the province in the current dataset.
    :param province: Any Dutch province as a string
    :return: A data frame containing all the data from that province from the raw data.
    """
    Bevolking_leeftijd = CsvParser('Data/03759ned_UntypedDataSet_07022020_153926.csv',
                                   province).get_data_frame().iloc[:, [2, 6]][1:]

    Bevolking_leeftijd_correction = CsvParser('Data/03759ned_UntypedDataSet_07022020_153926.csv',
                                              province).get_data_frame().iloc[:, [2, 6]][:1]

    Bevolking_leeftijd_corrected = (Bevolking_leeftijd['BevolkingOp1Januari_1'].astype(int).div(
        int(Bevolking_leeftijd_correction['BevolkingOp1Januari_1'].iloc[0]))) * 100

    Bevolking_percentage = AgeMerger(Bevolking_leeftijd_corrected).get_data_frame()

    Deaths = CsvParser('Data/80202ned_UntypedDataSet_31012020_123258.csv',
                       province).get_data_frame().drop(columns=["ID", "Geslacht", "Leeftijd", "RegioS", "Perioden"])[1:]

    Deaths_corrected = (Deaths['TotaalAlleOnderliggendeDoodsoorzaken_1'].fillna(0).astype(int).div(
        int(Bevolking_leeftijd_correction['BevolkingOp1Januari_1'].iloc[0]))) * 100000

    Nature_recreation = CsvParser('Data/70262ned_UntypedDataSet_05022020_180935.csv',
                                  province).get_data_frame().iloc[:, [1, 3, 4]]

    Distances = CsvParser('Data/80305ned_UntypedDataSet_31012020_124042.csv',
                          province).get_data_frame().iloc[:, [3, 7, 8, 9]]

    tablequality = OnlineParser("https://www.rivm.nl/media/milieu-en-leefomgeving/hoeschoonisonzelucht/",
                                province).get_data_frame().iloc[:, [2, 3]]

    finaldataframe = pd.DataFrame(Deaths_corrected)

    finaldataframe['Leeftijd verhouding van bevolking'] = Bevolking_percentage['Age'].values.tolist()

    combined_single_rows = DataframeConcer(Distances, tablequality).get_data_frame()
    combined_single_rows = DataframeConcer(combined_single_rows, Nature_recreation).get_data_frame()
    singlerowsadded = DataframeAdder(finaldataframe, combined_single_rows).get_data_frame()

    return singlerowsadded


def main():
    """
    This function is the main, it contains all the logic and calls the functions when the program is run from either the
    command line or from within a IDE. It contains an argparser to read command line arguments and a default list of
    all the provinces.
    """
    backuplistofprovinces = ["Groningen", "Friesland", "Drenthe", "Gelderland",
                       "Flevoland", "Overijssel", "Utrecht", "Noord-Holland",
                       "Zuid-Holland", "Zeeland", "Noord-Brabant", "Limburg"]
    parser = argparse.ArgumentParser(
        description='PCA and regression analyzer on deaths and related data in the twelve provinces.')

    parser.add_argument('-p', '--provinces', action="extend", nargs="+", type=str,
                        help='select Dutch provinces of interest')
    args = parser.parse_args()

    if str(args) != "Namespace(provinces=None)":
        listofprovinces = getattr(args, 'provinces')
    else:
        listofprovinces = backuplistofprovinces

    listofprofdata = []
    for province in listofprovinces:
        listofprofdata.append(ProvinceSelector(province))

    Big_Frame = pd.concat(listofprofdata, ignore_index=True)
    Big_Frame.to_csv('Data/outputfile.csv')
    pca = PcaAnalysis(Big_Frame)
    scatterplot = ScatterPlotter("PCA with grey scaling based on deaths",
                                 pca.get_data_frame(), listofprovinces).get_plot()
    barplot = BarPlotter(pca.get_scores(), pca.get_features()).get_plot()
    text = TextPlotter(listofprovinces, pca.get_variance()).get_plot()
    left = scatterplot
    right = column(barplot, text)
    show(row(left, right))


if __name__ == "__main__":
    sys.exit(main())
