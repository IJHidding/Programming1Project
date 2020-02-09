from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label

from Visualizers.abstract_plotter import AbstractPlotter
from bokeh.plotting import figure


class TextPlotter(AbstractPlotter):

    def __init__(self, Provinces, PcaFactors):
        """
        The init runs the logic and creates the plot. It can then be accessed with the get_plot function.
        :param PcaFactors: A list of the main two PCA factors ratios
        :param Provinces: A list of provinces used in the analysis.
        """
        self.plot = self._settings(Provinces, PcaFactors)


    def _settings(self, Provinces, PcaFactors):
        """
        This plot makes a figure and then adds a label, this label explains what data is being shown.
        :param Provinces: A list of provinces used in the analysis.
        :param PcaFactors: A list of the main two PCA factors ratios
        :return: A plot filled with only text
        """

        p = figure(title='Description PCA and regression',
               width=500, height=50, toolbar_location=None, sizing_mode='fixed')
        PcaFactors[0] = round(PcaFactors[0], 2)
        PcaFactors[1] = round(PcaFactors[1], 2)
        text1 = f"The plots show a two component PCA of data for the following Dutch provinces: " \
                f"{', '.join([str(x) for x in [*Provinces]])}. " \
                f"With Principal Component One having a {PcaFactors[0]} fraction of variance explained"\
                f" and Principal Component Two having a {PcaFactors[1]} fraction of variance explained."\
                f" Next to the PCA is a Regression plot showing the most important factors which "\
                f"influence the number of deaths for all provinces selected."
        citation = Label(x=0, y=0, x_units='screen', y_units='screen',
                     text=text1, render_mode='css',
                     border_line_color='black', border_line_alpha=1.0,
                     background_fill_color='white', background_fill_alpha=1.0)

        p.add_layout(citation)

        return p

    def get_plot(self):
        """
        Access point to get the plot after initializing the object.
        :return: The created plot
        """
        return self.plot