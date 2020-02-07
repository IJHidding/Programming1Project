import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_regression, f_classif




class PcaAnalysis:

    def __init__(self, dataframe):
        self.data_frame = dataframe
        self.data_frame = self.data_frame[self.data_frame.TotaalAlleOnderliggendeDoodsoorzaken_1.notnull()]
        # print(self.data_frame['TotaalAlleOnderliggendeDoodsoorzaken_1'])
        # print(list(self.data_frame.columns))
        self.features = list(self.data_frame.columns)

        self.features.remove('TotaalAlleOnderliggendeDoodsoorzaken_1')
        # self.features.remove('RegioS_x')
        # self.features.remove('RegioS_y')
        self.features.remove('RegioS')
        # self.features.remove('Geslacht_x')
        # self.features.remove('Geslacht_y')
        # self.features.remove('Geslacht')
        # self.features.remove('Perioden')
        # self.features.remove('Perioden_x')
        # self.features.remove('Perioden_y')
        # self.features.remove('ID')
        # self.features.remove('ID_x')
        # self.features.remove('ID_y')
        # print(self.features)
        # print(self.features)
        for feature in self.features:
            self.data_frame.loc[:, (feature)] = pd.to_numeric(self.data_frame[feature], errors='coerce')
        # print(self.data_frame['RegioS'])
        self.data_frame = self.data_frame.replace(np.nan, 0, regex=True)
        # self.data_better_frame = self.data_frame.drop(['RegioS_x', 'RegioS_y', 'RegioS'])
        # self.targets = ["PV20  ", "PV24  "]
        self.target = ["TotaalAlleOnderliggendeDoodsoorzaken_1"]
        self.final_data_frame = self.analysis()
        self.find_var(self.data_frame)
        # self.find_var(self.data_frame[self.data_frame['RegioS'] == "PV20  "])
        # self.find_var(self.data_frame[self.data_frame['RegioS'] == "PV24  "])
        self.final_data_frame['RegioS'] = self.data_frame['RegioS']
        # self.test_plot()

    def analysis(self):
        x = self.data_frame.loc[:, self.features].values  # Separating out the target
        # print(x)
        # y = self.data_frame.loc[:, [self.target]].values  # Standardizing the features
        x = StandardScaler().fit_transform(x)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)

        principalDf = pd.DataFrame(data=principalComponents,
                                   columns=['principal component 1', 'principal component 2'])
        # print(self.data_frame)
        print(pca.explained_variance_ratio_)
        # print(pd.concat([principalDf, self.data_frame[self.target]], axis=1))
        return pd.concat([principalDf, self.data_frame[self.target]], axis=1)


    def test_plot(self):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('Principal Component 1', fontsize=15)
        ax.set_ylabel('Principal Component 2', fontsize=15)
        ax.set_title('2 component PCA', fontsize=20)

        norm = colors.Normalize(vmin=self.final_data_frame[self.target].max(), vmax=self.final_data_frame[self.target].min())
        ax.scatter(self.final_data_frame[self.final_data_frame.columns[0]].values,
                   self.final_data_frame[self.final_data_frame.columns[1]].values,
                   s=50, c=self.final_data_frame[self.target].replace(np.nan, 0, regex=True).astype(float).values, cmap='hot', norm=norm)
        # targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        # colors = ['r', 'b'] self.final_data_frame[self.target].replace(np.nan, 0, regex=True).astype(int).values.tolist()
        # for target, color in zip(self.targets, colors):
        #     # print(self.data_frame['RegioS'] == target)
        #     indicesToKeep = (self.final_data_frame['RegioS_x'] == target).tolist()
        #     # print(indicesToKeep)
        #     print(self.final_data_frame.loc[indicesToKeep, 'principal component 1'])
        #     ax.scatter(self.final_data_frame.loc[indicesToKeep, 'principal component 1']
        #                , self.final_data_frame.loc[indicesToKeep, 'principal component 2']
        #                , c=color
        #                , s=50)
        ax.legend(self.target)
        ax.grid()
        plt.show()

    def find_var(self, data_frame):

        df = data_frame.loc[:, self.features].values
        # print(df)
        print(np.std(df, axis=0) == 0)
        # names = df.columns
        scaler = StandardScaler()
        standardizeddf = scaler.fit_transform(df)
        standardizeddf = pd.DataFrame(standardizeddf, columns=self.features)
        bestfeatures = SelectKBest(score_func=f_regression, k=10)
        fit = bestfeatures.fit(standardizeddf, np.ravel(data_frame[self.target]))
        # print(fit.scores_)
        scores = fit.scores_
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(self.features)), scores)
        plt.xticks(range(len(self.features)), self.features,
                   rotation='vertical', fontsize=14)
        plt.title("Results of Regression Tests")
        plt.ylabel("Correlation Scores", fontsize=15)
        plt.show()

    def get_data_frame(self):
        return self.final_data_frame

