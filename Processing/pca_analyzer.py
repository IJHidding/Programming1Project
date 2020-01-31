import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


class PcaAnalysis:

    def __init__(self, dataframe):
        self.data_frame = dataframe
        # print(list(self.data_frame.columns))
        self.features = list(self.data_frame.columns)

        self.features.remove('TotaalAlleOnderliggendeDoodsoorzaken_1')
        self.features.remove('RegioS')
        # print(self.features)
        #print(self.features)
        for feature in self.features:
            self.data_frame[feature] = pd.to_numeric(self.data_frame[feature], errors='coerce')
        self.data_frame = self.data_frame.replace(np.nan, 0, regex=True)

        self.targets = ["PV20", "PV24"]
        self.target = ["TotaalAlleOnderliggendeDoodsoorzaken_1"]
        self.final_data_frame = self.analysis()
        self.test_plot()

    def analysis(self):
        x = self.data_frame.loc[:, self.features].values  # Separating out the target
        # print(x)
        # y = self.data_frame.loc[:, ['target']].values  # Standardizing the features
        x = StandardScaler().fit_transform(x)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)

        principalDf = pd.DataFrame(data=principalComponents,
                                   columns=['principal component 1', 'principal component 2'])
        # print(self.data_frame)
        return pd.concat([principalDf, self.data_frame[self.target]], axis=1)


    def test_plot(self):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('Principal Component 1', fontsize=15)
        ax.set_ylabel('Principal Component 2', fontsize=15)
        ax.set_title('2 component PCA', fontsize=20)
        # targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        colors = ['r', 'b']
        for target, color in zip(self.targets, colors):
            indicesToKeep = (self.data_frame['RegioS'] == target).tolist()
            # print(indicesToKeep)
            print(self.final_data_frame.loc[indicesToKeep, 'principal component 1'])
            ax.scatter(self.final_data_frame.loc[indicesToKeep, 'principal component 1']
                       , self.final_data_frame.loc[indicesToKeep, 'principal component 2']
                       , c=color
                       , s=50)
        ax.legend(self.targets)
        ax.grid()
        plt.show()

    def get_data_frame(self):
        return self.final_data_frame



# features = ['sepal length', 'sepal width', 'petal length', 'petal width']# Separating out the features
#
# x = df.loc[:, features].values# Separating out the target
# y = df.loc[:, ['target']].values# Standardizing the features
# x = StandardScaler().fit_transform(x)
#
#
# pca = PCA(n_components=2)
#
# principalComponents = pca.fit_transform(x)
#
# principalDf = pd.DataFrame(data=principalComponents,
#                            columns=['principal component 1', 'principal component 2'])
#
# finalDf = pd.concat([principalDf, df[['target']]], axis = 1)
#
# ##plotting
#
# fig = plt.figure(figsize = (8,8))
# ax = fig.add_subplot(1,1,1)
# ax.set_xlabel('Principal Component 1', fontsize = 15)
# ax.set_ylabel('Principal Component 2', fontsize = 15)
# ax.set_title('2 component PCA', fontsize = 20)targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# colors = ['r', 'g', 'b']
# for target, color in zip(targets,colors):
#     indicesToKeep = finalDf['target'] == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c = color
#                , s = 50)
# ax.legend(targets)
# ax.grid()


#pca.explained_variance_ratio_
