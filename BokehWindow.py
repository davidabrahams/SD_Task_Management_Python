__author__ = 'davidabrahams & tomheale'

import bokeh.plotting as bk

bk.output_notebook()

import numpy as np

x = np.linspace(-6, 6, 100)
y = np.random.normal(0.3*x, 1)

bk.circle(x, y, color="red", plot_width=500, plot_height=500)
bk.show()