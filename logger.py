import psutil
import time
# print psutil.Process(80335)
code_processes = []
atom_processes = []
subl_processes = []


def get_processes():
    for item in psutil.pids():
        proc = psutil.Process(item)
        name = proc.name()
        if name == "Code Helper" or name == "Electron":
            code_processes.append(proc)
        elif "atom" in name.lower():
            atom_processes.append(proc)
        elif "Sublime" in name:
            subl_processes.append(proc)


def get_cpu_usage(proc_list):
    cpu_percent = 0
    for proc in proc_list:
        cpu_percent += proc.cpu_percent(interval=1.0)
    print cpu_percent


def get_memory_usage(proc_list):
    mem_percent = 0
    for proc in proc_list:
        mem_percent += proc.memory_percent()
    return mem_percent


def log_memory_usage(proc_list):
    try:
        maximum = 0
        total = 0
        ticks = 0
        while True:
            time.sleep(1)
            mem = get_memory_usage(proc_list)
            total += float(mem)
            ticks += 1
            if mem > maximum:
                maximum = mem
            print "Total memory usage is: {}%".format(mem)
    except KeyboardInterrupt:   
        print "Maximum reached memory usage was  : {}%".format(maximum)
        print "Average memory percentage used is: {}%".format(total/ticks)
        return


def log_cpu_usage(proc_list):
    try:
        maximum = 0
        total = 0
        ticks = 0
        with open(mem_log.txt, "w") as f:
            while True:
                time.sleep(1)
                cpu = get_cpu_usage(proc_list)
                total += float(cpu)
                ticks += 1
                if cpu > maximum:
                    maximum = cpu
                print "Total cpu usage is: {}%".format(mem)
                f.write(mem)
    except KeyboardInterrupt:
        print "\nMaximum reached cpu usage was  : {}%".format(maximum)
        print "Average memory percentage used is: {}%".format(total/ticks)
        return


get_processes()
