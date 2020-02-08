"""
Author = "Iwan Hidding"

This class contains the PCA analysis and the regression analysis as well. It does the main analysis and its data is used
to visualize the data. It contains three get_data functions as three different data sets are required for the
visualisation. The regression and PCA are in the same class as they have similar steps and separating them would likely
increase the amount of work done needlessly.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_regression


class PcaAnalysis:

    def __init__(self, dataframe):
        """
        Runs the logic within this class. The get_data_frame function can be used to pull the dataframe out of the class
        after the logic.
        :param dataframe: A dataframe containing all the data from the provinces combined
        """
        self.data_frame = dataframe
        self.data_frame = self.data_frame[self.data_frame.TotaalAlleOnderliggendeDoodsoorzaken_1.notnull()]
        self.features = list(self.data_frame.columns)
        self.features.remove('TotaalAlleOnderliggendeDoodsoorzaken_1')
        self.features.remove('RegioS')
        for feature in self.features:
            self.data_frame.loc[:, (feature)] = pd.to_numeric(self.data_frame[feature], errors='coerce')
        self.data_frame = self.data_frame.replace(np.nan, 0, regex=True)
        self.target = ["TotaalAlleOnderliggendeDoodsoorzaken_1"]
        self.final_data_frame = self.analysis()
        self.scores = self.find_var()
        self.final_data_frame['RegioS'] = self.data_frame['RegioS']

    def analysis(self):
        """
        This function runs the PCA analysis.
        :return: The data after the analysis with the provinces added again. Two principal components and the provinces.
        """
        x = self.data_frame.loc[:, self.features].values
        x = StandardScaler().fit_transform(x)
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(x)

        principalDf = pd.DataFrame(data=principalComponents,
                                   columns=['principal component 1', 'principal component 2'])
        return pd.concat([principalDf, self.data_frame[self.target]], axis=1)

    def find_var(self):
        """
        This function runs the regression using the sklearn regression package.
        :return: A list of the scores indicated by the regression fit function.
        """
        df = self.data_frame.loc[:, self.features].values
        scaler = StandardScaler()
        standardizeddf = scaler.fit_transform(df)
        standardizeddf = pd.DataFrame(standardizeddf, columns=self.features)
        bestfeatures = SelectKBest(score_func=f_regression, k=9)
        fit = bestfeatures.fit(standardizeddf, np.ravel(self.data_frame[self.target]))
        scores = fit.scores_
        return scores

    def get_data_frame(self):
        """
        The function which gives a method to get the data frame from the class.
        :return: Returns final dataframe
        """
        return self.final_data_frame

    def get_scores(self):
        """
        The function which gives a method to get the scores values from the class.
        :return: Returns a list containing scores
        """
        return self.scores

    def get_features(self):
        """
        The function which gives a method to get the features from the class.
        :return: Returns a list containing features.
        """
        return self.features
