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
        cpu_percent += proc.cpu_percent(interval=0)
    return cpu_percent


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
        fname = ""
        for proc in proc_list:
            name = proc.name()
            if "Electron" in name:
                fname = "vscode"
            elif "atom" in name.lower():
                fname = "atom"
            elif "Sublime" in name:
                fname = "sublime"
        with open("./logs/memory_log_{}.csv".format(fname), "w") as f:
            while True:
                time.sleep(1)
                mem = get_memory_usage(proc_list)
                total += float(mem)
                ticks += 1
                if mem > maximum:
                    maximum = mem
                f.write(str(mem)+"\n")
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
        fname = ""
        for proc in proc_list:
            name = proc.name()
            if "Electron" in name:
                fname = "vscode"
            elif "atom" in name.lower():
                fname = "atom"
            elif "Sublime" in name:
                fname = "sublime"
        with open("cpu_usage_{}.csv".format(name), "w") as f:
            while True:
                time.sleep(1)
                cpu = get_cpu_usage(proc_list)
                total += float(cpu)
                ticks += 1
                if cpu > maximum:
                    maximum = cpu
                f.write(str(cpu)+"\n")
                print "Total cpu usage is: {}%".format(cpu)
    except KeyboardInterrupt:
        print "\nMaximum reached cpu usage was  : {}%".format(maximum)
        print "Average memory percentage used is: {}%".format(total/ticks)
        return


def log_all(proc_list):
    try:
        max_mem = 0
        max_cpu = 0
        total_mem = 0
        total_cpu = 0
        ticks = 0
        fname = ""
        for proc in proc_list:
            name = proc.name()
            if "Electron" in name:
                fname = "vscode"
            elif "atom" in name.lower():
                fname = "atom"
            elif "Sublime" in name:
                fname = "sublime"
        with open("./logs/full_log_{}.csv".format(fname), "w") as f:
            f.write("cpu percent, memory percent\n")
            counter = 0
            while counter < 120:
                time.sleep(1)
                cpu = get_cpu_usage(proc_list)
                mem = get_memory_usage(proc_list)
                total_cpu += cpu
                total_mem += mem
                ticks += 1
                if cpu > max_cpu:
                    max_cpu = cpu
                if mem > max_mem:
                    max_mem = mem
                f.write("{},{}\n".format(cpu, mem))
                print "Total cpu usage is: {}%".format(cpu)
                print "Total mem usage is: {}%".format(mem)
                counter += 1
            return
    except:
        print "\nMaximum reached cpu usage was   : {}%".format(max_cpu)
        print "Average cpu percentage used was   : {}%".format(total_cpu/ticks)
        print "\nMaximum reached memory usage was: {}%".format(max_mem)
        print "Average memory percentage used was: {}%".format(total_mem/ticks)
        print("done")
get_processes()
