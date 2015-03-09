from bokeh._glyph_functions import circle
from matplotlib import pyplot as plt
import seaborn as sns
import time
from ProcessManager import ProcessManager

__author__ = 'davidabrahams & tomheale'

class PyChartApp:

    def __init__(self):
        self.proc_manager = ProcessManager()
        plt.show(block = False)
        plt.close()
        plt.ion()       


    def update(self):
        while True:
            self.proc_manager.update()
            data = self.proc_manager.data
            keys = data.keys()

            # Only display processes with more than 1.0 CPU
            indices_to_remove = []
            vals = []
            for i, k in enumerate(keys):
                cpu, ram =  data[k]
                if ram < 20.0:
                    indices_to_remove.append(i)
                else:
                    vals.append(ram)
            # Iterate backward in order to remove correct indices.
            for i in reversed(indices_to_remove):
                keys.pop(i)

            # Make a pie graph
            plt.clf()
            plt.pie(vals, labels=keys)
            plt.pause(0.1)
            time.sleep(0.05)


if __name__ == '__main__':
    p = PyChartApp()
    p.update()