import unittest
import pandas as pd
from Parsers.Onlineparser import OnlineParser
from Parsers.csv_parser import CsvParser
from Processing.SingleColumnConcer import DataframeConcer


class MyTestCase(unittest.TestCase):
    def test_online_table(self):
        self.assertEqual(OnlineParser("https://www.rivm.nl/media/milieu-en-leefomgeving/hoeschoonisonzelucht/",
                                "Groningen").get_data_frame().iloc[:, [2, 3]].sum(numeric_only=True).sum(), pd.read_csv('Unittest/UnittestComparisonData/Onlinetester_groningen.csv', index_col=0).sum(numeric_only=True).sum(), msg="The site might have been changed for Groningen")
        self.assertEqual(OnlineParser("https://www.rivm.nl/media/milieu-en-leefomgeving/hoeschoonisonzelucht/",
                                "Flevoland").get_data_frame().iloc[:, [2, 3]].sum(numeric_only=True).sum(), pd.read_csv('Unittest/UnittestComparisonData/Onlinetester_flevoland.csv', index_col=0).sum(numeric_only=True).sum(), msg="The site might have been changed for Flevoland")

    def test_csv_parser(self):
        self.assertEqual(CsvParser('Data/03759ned_UntypedDataSet_07022020_153926.csv',
                                   "Groningen").get_data_frame().iloc[:, [2, 6]][1:].sum(numeric_only=True).sum(), pd.read_csv('Unittest/UnittestComparisonData/CsvTester_groningen.csv', index_col=0)['Leeftijd'].sum(), msg="Csv Parser is not working for Groningen")
        self.assertEqual(CsvParser('Data/03759ned_UntypedDataSet_07022020_153926.csv',
                                   "Flevoland").get_data_frame().iloc[:, [2, 6]][1:].sum(numeric_only=True).sum(), pd.read_csv('Unittest/UnittestComparisonData/CsvTester_flevoland.csv', index_col=0)['Leeftijd'].sum(), msg="Csv Parser is not working for Flevoland")

    def test_column_concer(self):
        self.assertEqual(DataframeConcer(CsvParser('Data/70262ned_UntypedDataSet_05022020_180935.csv',
                                  "Groningen").get_data_frame().iloc[:, [1, 3, 4]], CsvParser('Data/70262ned_UntypedDataSet_05022020_180935.csv',
                                  "Groningen").get_data_frame().iloc[:, [1, 3, 4]]).get_data_frame().sum(numeric_only=True).sum(), pd.read_csv('Unittest/UnittestComparisonData/Concertester_groningen.csv').sum(numeric_only=True).sum(), msg="Something is not adding up...")


if __name__ == '__main__':
    unittest.main()
