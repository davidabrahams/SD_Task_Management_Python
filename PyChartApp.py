from bokeh._glyph_functions import circle
from matplotlib import pyplot as plt
import seaborn as sns
import time
from ProcessManager import ProcessManager

__author__ = 'davidabrahams & tomheale'


class PyChartApp:
    def __init__(self):
        self.proc_manager = ProcessManager()
        plt.show(block=False)
        plt.close()
        plt.ion()

    def shorten_names(self, names):
        new_names = []
        for name in names:
            if ' ' in name:
                new_names.append(name[0:name.index(' ')])
            else:
                new_names.append(name)
        return new_names

    def update(self):

        tic = time.clock()

        self.proc_manager.update()
        data = self.proc_manager.data
        keys = data.keys()

        # Only display processes with more than 20Mb RAM
        indices_to_remove = []
        vals = []
        for i, k in enumerate(keys):
            pid, cpu, ram = data[k]
            if ram < 20.0:
                indices_to_remove.append(i)
            else:
                vals.append(ram)
        # Iterate backward in order to remove correct indices.
        for i in reversed(indices_to_remove):
            keys.pop(i)

        names = self.shorten_names([data[k][0] for k in keys])

        # Make a pie graph
        plt.clf()
        plt.pie(vals, labels=names)
        plt.title('Active Process RAM Usage')

        toc = time.clock()
        sleep_time = 0.25
        plt.pause(max([sleep_time - (toc - tic), 0.0001]))


if __name__ == '__main__':
    p = PyChartApp()
    while True:
        p.update()