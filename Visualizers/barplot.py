"""
Author = "Iwan Hidding"

This class constructs the Bar plot as part of the visualizing. It is build upon the abstract_plotter.py class. It takes
the scores and the features from the PCA analysis and uses those as a basis for the bar plot.
"""
from Visualizers.abstract_plotter import AbstractPlotter
from bokeh.plotting import figure
import numpy as np


class BarPlotter(AbstractPlotter):

    def __init__(self, scores, features):
        """
        The init runs the logic and creates the plot. It can then be accessed with the get_plot function.
        :param scores: The scores as output from the regression.
        :param features: The features used in the regression
        """
        self.plot = self._settings(scores, features)

    def _settings(self, scores, features):
        """
        Simple bar plot by setting the features as the x axis and the height is determined by the scores.
        :param scores: The scores as output from the regression.
        :param features: The features used in the regression
        :return: Returns the created bar plot
        """
        p = figure(x_range=features, plot_height=500, title="Results of Regression Tests",
                   toolbar_location=None, tools="")

        p.vbar(x=features, top=scores, width=0.5)

        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.xaxis.major_label_orientation = np.pi / 2

        return p

    def get_plot(self):
        """
        Access point to get the plot after initializing the object.
        :return: The created plot
        """
        return self.plot

