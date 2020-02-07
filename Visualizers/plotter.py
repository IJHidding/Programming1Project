from Visualizers.abstract_plotter import AbstractPlotter
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import LinearColorMapper, ColorBar, BasicTicker, PrintfTickFormatter
from bokeh.transform import transform
from bokeh.palettes import Category20b


class Plotter(AbstractPlotter):

    def __init__(self, title, dataframe):
        self.data_frame = dataframe
        self.plot = self._settings(title)

    def _data_selection(self):
        pass

    def _settings(self, title):
        plot = figure(plot_width=600, plot_height=600,
                      title=title)
        print(self.data_frame['principal component 1'], self.data_frame['principal component 2'])
        source1 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV20  "])
        source2 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV21  "])
        source3 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV22  "])
        source4 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV23  "])
        source5 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV24  "])
        source6 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV25  "])
        source7 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV26  "])
        source8 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV27  "])
        source9 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV28  "])
        source10 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV29  "])
        source11 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV30  "])
        source12 = ColumnDataSource(self.data_frame[self.data_frame['RegioS'] == "PV31  "])

        mapper = LinearColorMapper(
            palette='Greys256',
            low=self.data_frame["TotaalAlleOnderliggendeDoodsoorzaken_1"].min(),
            high=self.data_frame["TotaalAlleOnderliggendeDoodsoorzaken_1"].max()
        )
        size = 5
        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source1, line_color=Category20b[12][1], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0, legend_label='Groningen')
        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source2, line_color=Category20b[12][2], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0, legend_label='Friesland')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source3, line_color=Category20b[12][3], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Drenthe')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source4, line_color=Category20b[12][4], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Overijssel')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=10,
                    source=source5, line_color=Category20b[12][5], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Flevoland')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source6, line_color=Category20b[12][6], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Gelderland')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source7, line_color=Category20b[12][7], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Utrecht')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source8, line_color=Category20b[12][8], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Noord-Holland')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source9, line_color=Category20b[12][9], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Zuid-Holland')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source10, line_color=Category20b[12][10], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Zeeland')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source11, line_color=Category20b[12][11], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Noord-Brabant')

        plot.circle(x='principal component 1', y='principal component 2',
                    size=size,
                    source=source12, line_color=Category20b[12][0], line_width=1,
                    fill_color=transform('TotaalAlleOnderliggendeDoodsoorzaken_1', mapper), fill_alpha=1.0,
                    legend_label='Limburg')

        color_bar = ColorBar(color_mapper=mapper, location=(0, 0),
                             ticker=BasicTicker(desired_num_ticks=10),
                             formatter=PrintfTickFormatter(format="%d"))
        plot.add_layout(color_bar, 'right')
        plot.legend.location = 'top_left'
        return plot

    def get_plot(self):
        return self.plot

