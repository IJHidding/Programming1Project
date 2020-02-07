from Visualizers.abstract_plotter import AbstractPlotter
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import LinearColorMapper, ColorBar, BasicTicker, PrintfTickFormatter
from bokeh.transform import transform

class Plotter(AbstractPlotter):

    def __init__(self, title, dataframe):
        self.data_frame = dataframe
        self.plot = self._settings(title)

    def _data_selection(self):
        pass

    def _settings(self, title):
        plot = figure(plot_width=600, plot_height=600,
                      title=title)

        source1 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV20  "])
        source2 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV24  "])
        mapper = LinearColorMapper(
            palette='Greys256',
            low=self.data_frame["TotaalAlleOnderliggendeDoodsoorzaken_1"].min(),
            high=self.data_frame["TotaalAlleOnderliggendeDoodsoorzaken_1"].max()
        )

        plot.circle(x='principal component 1', y='principal component 2',
                    size=10,
                    source=source1, line_color='Red', line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0, legend_label='Groningen')
        plot.circle(x='principal component 1', y='principal component 2',
                    size=10,
                    source=source2, line_color='Blue', line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0, legend_label='Flevoland')

        color_bar = ColorBar(color_mapper=mapper, location=(0, 0),
                             ticker=BasicTicker(desired_num_ticks=10),
                             formatter=PrintfTickFormatter(format="%d"))
        plot.add_layout(color_bar, 'right')
        plot.legend.location = 'top_center'
        return plot

    def get_plot(self):
        return self.plot

