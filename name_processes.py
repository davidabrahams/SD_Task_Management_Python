import psutil
import time

__author__ = 'davidabrahams'


def print_processes():
    for proc in psutil.process_iter():
        proc.get_cpu_percent()

    time.sleep(1)

    for proc in psutil.process_iter():
        memory_info, vms = proc.get_memory_info()
        print str(proc.get_cpu_percent()) + ', ' + str(memory_info) + ', ' + str(proc.name())


def get_procs():
    return [proc for proc in psutil.process_iter()]


if __name__ == '__main__':
    print_processes()