from Visualizers import abstract_plotter
import bokeh


class Plotter(abstract_plotter):

    def __init__(self, title, dataframe):
        self.data_frame = dataframe
        self.plot = settings(title)

    def data_selection(self):
        pass

    def settings(self, title):
        plot = figure(plot_width=600, plot_height=600,
                      x_axis_type='datetime', title=title)
        return plot

    def plot(self):
        return self.plot

