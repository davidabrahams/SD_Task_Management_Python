import psutil
import time


class ProcessManager:

    def get_process_data(self):
        """
        :return: a dict of process_name:(cpu_percent, ram_usage_mb) key value pairs
        """
        process_names = []
        process_usages = []

        for proc in psutil.process_iter():
            # Iterate through the processes and add the name:(cpu, ram) pairs to lists
            memory_info, vms = proc.get_memory_info()
            process_names.append(str(proc.name()))
            process_usages.append((proc.get_cpu_percent(), (int(memory_info)) / (1024.0 ** 2)))

            # create a dict out of the lists
        return dict(zip(process_names, process_usages))



    def init_process_data(self):
        """
        :return: a dict of process_name:(cpu_percent, ram_usage_mb) key value pairs
        """

        # Check the initial usage of all processes
        for proc in psutil.process_iter():
            proc.get_cpu_percent()

            time.sleep(0.5)

        return self.get_process_data(self)

    def update(self):
        data = self.data
        new_dict = self.get_process_data()
        for key in data:
            if key in new_dict:
                data[key] = new_dict[key]
            else:
                data.pop(key)
        for key in new_dict:
            if key not in data:
                data[key] = new_dict[key]

    def __init__(self):
        self.data = self.init_process_data(self)


if __name__ == '__main__':
    proc_manager = ProcessManager()