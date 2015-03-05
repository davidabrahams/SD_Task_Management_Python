from collections import OrderedDict
from pprint import pprint
import psutil
import time


class ProcessManager:

    def __init__(self):
        self.data = self.init_process_data()

    def get_process_data(self):
        """
        :return: an OrderedDict of process_name:(cpu_percent, ram_usage_mb) key value pairs
        """
        process_names = []
        process_usages = []

        for proc in psutil.process_iter():
            # Iterate through the processes and add the name:(cpu, ram) pairs to lists
            memory_info, vms = proc.get_memory_info()
            process_names.append(str(proc.name()))
            process_usages.append((proc.get_cpu_percent(), (int(memory_info)) / (1024.0 ** 2)))

        # create a dict out of the lists
        return OrderedDict(zip(process_names, process_usages))



    def init_process_data(self):
        """
        :return: an OrderedDict of process_name:(cpu_percent, ram_usage_mb) key value pairs
        """

        # Check the initial usage of all processes
        for proc in psutil.process_iter():
            proc.get_cpu_percent()

        time.sleep(0.5)

        return self.get_process_data()

    def update(self):

        # Create references to the old data and the data to update to
        data = self.data
        new_dict = self.get_process_data()

        # Make a list of keys to remove from data
        keys_to_del = []
        for key in data:
            # Update the keys already in the dictionary
            if key in new_dict:
                data[key] = new_dict[key]
            # Remove the processes that are no longer running
            else:
                keys_to_del.append(key)

        # Delete them
        for k in keys_to_del:
            data.pop(k)

        # Add the processes that weren't previously running
        keys_to_add = []
        vals_to_add = []

        for key in new_dict:
            if key not in data:
                keys_to_add.append(key)
                vals_to_add.append(new_dict[key])

        for k, v in zip(keys_to_add, vals_to_add):
            data[k] = v


    def print_process_data(self):
        pprint(dict(self.data))


if __name__ == '__main__':
    proc_manager = ProcessManager()
    for i in range(100):
        proc_manager.update()
        proc_manager.print_process_data()
        time.sleep(1)