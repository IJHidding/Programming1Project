"""
Author = "Iwan Hidding"

This class constructs the Scatter plot as part of the visualizing. It is build upon the abstract_plotter.py class.
It takes the data frame that is put out by the PCA analysis and plots component 1 vs component 2. The center of the
circles is used to display the relative deaths, with the outer circle being used to identify which province the point
belongs to.
"""
from Visualizers.abstract_plotter import AbstractPlotter
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import LinearColorMapper, ColorBar, BasicTicker, PrintfTickFormatter
from bokeh.transform import transform
from bokeh.palettes import Category20b


class ScatterPlotter(AbstractPlotter):

    def __init__(self, title, dataframe, provinces):
        """
        The init runs the logic and creates the plot. It can then be accessed with the get_plot function.
        :param title: Title to be given to the plot
        :param dataframe: Data frame containing the principal components and the provinces
        :param provinces: The provinces used in the analysis to be added to the legend after plotting.
        """
        self.data_frame = dataframe
        self.plot = self._settings(title, provinces)

    def _settings(self, title, provinces):
        """
        This function creates the scatter plot of the PCA analysis results. It loads data per province to split the
        colors. The line colors are used to indicate province, with the inside colors showing the relative amounts of
        deaths per 100.000 people per province. Range of the plot was set to get space for the legend.
        :param title: Data frame containing the principal components and the provinces
        :param provinces: The provinces used in the analysis to be added to the legend after plotting.
        :return: returns the PCA scatter plot.
        """
        plot = figure(plot_width=700, plot_height=550,
                      title=title,  x_range=(-7, 5))

        plot.xaxis.axis_label = "Principal Component 1"
        plot.yaxis.axis_label = "Principal Component 2"
        listofsources = []
        dict_of_provinces = {"Groningen": "PV20  ", "Friesland": "PV21  ", "Drenthe": "PV22  ", "Overijssel": "PV23  ",
                             "Flevoland": "PV24  ", "Gelderland": "PV25  ", "Utrecht": "PV26  ",
                             "Noord-Holland": "PV27  ",
                             "Zuid-Holland": "PV28  ", "Zeeland": "PV29  ", "Noord-Brabant": "PV30  ",
                             "Limburg": "PV31  "}
        for province in provinces:
            listofsources.append(ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == dict_of_provinces[province]]))

        mapper = LinearColorMapper(
            palette='Greys256',
            low=self.data_frame["TotaalAlleOnderliggendeDoodsoorzaken_1"].min(),
            high=self.data_frame["TotaalAlleOnderliggendeDoodsoorzaken_1"].max()
        )
        size = 10

        for source, count in zip(listofsources, range(0, len(listofsources))):
            plot.circle(x='principal component 1', y='principal component 2',
                        size=size,
                        source=source, line_color=Category20b[12][count], line_width=3,
                        fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                        legend_label=provinces[count])

        color_bar = ColorBar(color_mapper=mapper, location=(0, 0),
                             ticker=BasicTicker(desired_num_ticks=10),
                             formatter=PrintfTickFormatter(format="%d"))

        plot.add_layout(color_bar, 'right')
        plot.legend.location = 'top_left'
        return plot

    def get_plot(self):
        """
        Access point to get the plot after initializing the object.
        :return: The created plot
        """
        return self.plot

