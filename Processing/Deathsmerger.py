# 10000	Totaal alle leeftijden
# 10010	0 jaar
# 51300	1 tot 5 jaar
# 70200	5 tot 10 jaar
# 70300	10 tot 15 jaar
# 70400	15 tot 20 jaar
# 70500	20 tot 25 jaar
# 70600	25 tot 30 jaar
# 70700	30 tot 35 jaar
# 70800	35 tot 40 jaar
# 70900	40 tot 45 jaar
# 71000	45 tot 50 jaar
# 71100	50 tot 55 jaar
# 71200	55 tot 60 jaar
# 71300	60 tot 65 jaar
# 71400	65 tot 70 jaar
# 71500	70 tot 75 jaar
# 71600	75 tot 80 jaar
# 71700	80 tot 85 jaar
# 71800	85 tot 90 jaar
# 71900	90 tot 95 jaar
# 22000	95 jaar of ouder

grouped_deaths = {"10000": "Totaal alle leeftijden",
                  "51300": "1-5",
                  "70200": "5-10",
                  "70300": "10-15",
                  "70400": "15-20",
                  "70500": "20-25",
                  "70600": "25-30",
                  "70700": "30-35",
                  "70800": "35-40",
                  "70900": "40-45",
                  "71000": "45-50",
                  "71100": "50-55",
                  "71200": "55-60",
                  "71300": "60-65",
                  "71400": "65-70",
                  "71500": "70-75",
                  "71600": "75-80",
                  "71700": "80-85",
                  "71800": "85-90",
                  "71900": "90-95",
                  "22000": "95-",
                  }

# Key	Title
# 10000	Totaal
# 10010	0 jaar
# 10100	1 jaar
# 10200	2 jaar
# 10300	3 jaar
# 10400	4 jaar
# 10500	5 jaar
# 10600	6 jaar
# 10700	7 jaar
# 10800	8 jaar
# 10900	9 jaar
# 11000	10 jaar
# 11100	11 jaar
# 11200	12 jaar
# 11300	13 jaar
# 11400	14 jaar
# 11500	15 jaar
# 11600	16 jaar
# 11700	17 jaar
# 11800	18 jaar
# 11900	19 jaar
# 12000	20 jaar
# 12100	21 jaar
# 12200	22 jaar
# 12300	23 jaar
# 12400	24 jaar
# 12500	25 jaar
# 12600	26 jaar
# 12700	27 jaar
# 12800	28 jaar
# 12900	29 jaar
# 13000	30 jaar
# 13100	31 jaar
# 13200	32 jaar
# 13300	33 jaar
# 13400	34 jaar
# 13500	35 jaar
# 13600	36 jaar
# 13700	37 jaar
# 13800	38 jaar
# 13900	39 jaar
# 14000	40 jaar
# 14100	41 jaar
# 14200	42 jaar
# 14300	43 jaar
# 14400	44 jaar
# 14500	45 jaar
# 14600	46 jaar
# 14700	47 jaar
# 14800	48 jaar
# 14900	49 jaar
# 15000	50 jaar
# 15100	51 jaar
# 15200	52 jaar
# 15300	53 jaar
# 15400	54 jaar
# 15500	55 jaar
# 15600	56 jaar
# 15700	57 jaar
# 15800	58 jaar
# 15900	59 jaar
# 16000	60 jaar
# 16100	61 jaar
# 16200	62 jaar
# 16300	63 jaar
# 16400	64 jaar
# 16500	65 jaar
# 16600	66 jaar
# 16700	67 jaar
# 16800	68 jaar
# 16900	69 jaar
# 17000	70 jaar
# 17100	71 jaar
# 17200	72 jaar
# 17300	73 jaar
# 17400	74 jaar
# 17500	75 jaar
# 17600	76 jaar
# 17700	77 jaar
# 17800	78 jaar
# 17900	79 jaar
# 18000	80 jaar
# 18100	81 jaar
# 18200	82 jaar
# 18300	83 jaar
# 18400	84 jaar
# 18500	85 jaar
# 18600	86 jaar
# 18700	87 jaar
# 18800	88 jaar
# 18900	89 jaar
# 19000	90 jaar
# 19100	91 jaar
# 19200	92 jaar
# 19300	93 jaar
# 19400	94 jaar
# 19500	95 jaar
# 19600	96 jaar
# 19700	97 jaar
# 19800	98 jaar
# 19900	99 jaar
# 19901	100 jaar
# 19902	101 jaar
# 19903	102 jaar
# 19904	103 jaar
# 19905	104 jaar
# 22000	95 jaar of ouder
# 22300	105 jaar of ouder

import pandas as pd
from functools import reduce

class DeathAgeMerger:

    def __init__(self, dataframe1, dataframe2):
        self.data_frame = self.agemerger(dataframe1, dateframe2)

    def agemerger(self, dataframe1, dataframe2):
        # print(dataframe)

        return dataframe

    def get_data_frame(self):
        return self.data_frame