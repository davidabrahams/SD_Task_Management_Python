import psutil
import bokeh
import time

__author__ = 'davidabrahams & tomheale'


def get_process_data():

    for proc in psutil.process_iter():
    	proc.get_cpu_percent()
    process_names = []
    process_usages = []

    time.sleep(0.5)

    for proc in psutil.process_iter():
        memory_info, vms = proc.get_memory_info()
        item = [int(proc.get_cpu_percent()), (int(memory_info))/(1024.0**2)]
        process_names.append(str(proc.name()))
        process_usages.append(item)
    process_data = dict(zip(process_names,process_usages))
    return process_data

def print_processes():
    process_data = get_process_data()
    for key in process_data:
        print key, process_data[key]

# So I got rid of print_processes(). It's in older versions if we need it. I didn't do it deliberately...


if __name__ == '__main__':
    print_processes()