__author__ = 'davidabrahams & tomheale'


from bokeh.models import HBox
import bokeh.plotting as bk
import numpy as np

bk.output_file('plot.html')

x = np.linspace(-6, 6, 100)
y = np.random.normal(0.3*x, 1)

print bk

bk.Figure.circle(x, y, color="red", plot_width=500, plot_height=500)
bk.show()

class PyChartApp(HBox):
    @classmethod
    def create(cls):
        pass
