from bokeh._glyph_functions import circle
from bokeh.models import HBox
from matplotlib import pyplot as plt
import seaborn as sns
import time
from ProcessManager import ProcessManager

__author__ = 'davidabrahams & tomheale'

class PyChartApp:

    def __init__(self):
        self.proc_manager = ProcessManager()

    def plot(self):
        plt.clf()
        data = self.proc_manager.data
        keys = data.keys()

        # Only display processes with more than 1.0 CPU
        indices_to_remove = []
        vals = []
        for i, k in enumerate(keys):
            cpu, ram =  data[k]
            if cpu < 1.0:
                indices_to_remove.append(i)
            else:
                vals.append(cpu)
        # Iterate backward in order to remove correct indices.
        for i in reversed(indices_to_remove):
            keys.pop(i)

        # Make a pie graph
        plt.pie(vals, labels=keys)
        plt.show()

    def update(self):
        self.proc_manager.update()

if __name__ == '__main__':
    p = PyChartApp()
    while True:
        # This doesn't work. Execution hangs at p.plot() because execution hangs at plt.show(), so the plot doesn't update.
        p.update()
        p.plot()
        time.sleep(0.1)
