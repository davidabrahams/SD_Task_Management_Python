import psutil
import bokeh
import time

__author__ = 'davidabrahams & tomheale'


def get_process_data():
    """
    :return: a dict of process_name:(cpu_percent, ram_usage_mb) key value pairs
    """

    # Check the initial usage of all processes
    for proc in psutil.process_iter():
        proc.get_cpu_percent()
    process_names = []
    process_usages = []

    # Sleep an arbitrary amount of time in between processes checks
    time.sleep(0.5)

    for proc in psutil.process_iter():
        # Iterate through the processes and add the name:(cpu, ram) pairs to lists
        memory_info, vms = proc.get_memory_info()
        process_names.append(str(proc.name()))
        process_usages.append((proc.get_cpu_percent(), (int(memory_info)) / (1024.0 ** 2)))

    #create a dict out of the lists
    return dict(zip(process_names, process_usages))


def print_processes():
    process_data = get_process_data()
    for key in process_data:
        print process_data[key], key


if __name__ == '__main__':
    print_processes()