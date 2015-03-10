from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import seaborn as sns
import time
from ProcessManager import ProcessManager

__author__ = 'davidabrahams & tomheale'


class PyChartApp:
    def __init__(self):
        self.proc_manager = ProcessManager()
        self.fig = plt.figure('Active Process RAM Usage')
        self.ax = self.fig.add_subplot(111)
        self.selected_pid = None
        self.viewing_ram = True
        self.running = True
        self.sleep_time = 1.0


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
            if (self.viewing_ram and ram < 20.0) or (not self.viewing_ram and cpu < 1.0):
                indices_to_remove.append(i)
            else:
                if self.viewing_ram:
                    vals.append(ram)
                else:
                    vals.append(cpu)
        # Iterate backward in order to remove correct indices.
        for i in reversed(indices_to_remove):
            keys.pop(i)

        names = self.shorten_names([data[k][0] for k in keys])

        explode_list = [0] * len(keys)
        if self.selected_pid in keys:
            explode_list[keys.index(self.selected_pid)] = 0.2

        # Make a pie graph
        plt.clf()
        wedges, pie_labels = plt.pie(vals, labels=names, explode=explode_list)
        self.wedge_dict = dict(zip(wedges, keys))
        self.make_picker(self.fig, wedges)

        # Make a button
        term_button_ax = plt.axes([0.52, 0.01, 0.2, 0.07])
        button = Button(term_button_ax, 'Terminate')
        button.on_clicked(self.terminate)

        #Make another button
        switch_button_ax = plt.axes([0.28, 0.01, 0.2, 0.07])
        if not self.viewing_ram:
            button_switch = Button(switch_button_ax, 'Switch to RAM')
        else:
            button_switch = Button(switch_button_ax, 'Switch to CPU')
        button_switch.on_clicked(self.switch)

        close_button_ax = plt.axes([0.79, 0.92, 0.2, 0.07])
        button_close = Button(close_button_ax, 'Close')
        button_close.on_clicked(self.finish)

        self.ax.axis('equal')

        toc = time.clock()
        plt.pause(max([self.sleep_time - (toc - tic), 0.0001]))


    def run(self):
        while self.running:
            self.update()



    def make_picker(self, fig, wedges):

        def onclick(event):
            wedge = event.artist
            pid = self.wedge_dict[wedge]
            self.selected_pid = pid

        # Make wedges selectable
        for wedge in wedges:
            wedge.set_picker(True)

        fig.canvas.mpl_connect('pick_event', onclick)

    def terminate(self, event):
        self.proc_manager.terminate_process(self.selected_pid)

    def switch(self, event):
        self.viewing_ram = not self.viewing_ram

    def finish(self, event):
        self.running = False


if __name__ == '__main__':
    p = PyChartApp()
    p.run()