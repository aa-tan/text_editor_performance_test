import psutil
import time

# Use these variable names to pass to any function that requires proc_list
# as an argument
code_processes = []
atom_processes = []
subl_processes = []


def get_processes():
    '''
        Gets the process objects from psutil of the three applications.
        Application must be running at the time this function is called.
    '''
    for item in psutil.pids():
        proc = psutil.Process(item)
        name = proc.name()
        if name == "Code Helper" or name == "Electron":
            print name
            code_processes.append(proc)
        elif "atom" in name.lower():
            print name
            atom_processes.append(proc)
        elif "Sublime" in name:
            print name
            subl_processes.append(proc)


def get_name(proc_list):
    '''
        Determines what string to return for file name appending purposes
    '''
    for proc in proc_list:
        name = proc.name()
        if "Electron" in name:
            return "vscode"
        elif "atom" in name.lower():
            return "atom"
        elif "Sublime" in name:
            return "sublime"


def get_cpu_usage(proc_list):
    '''
        Returns the cumulative usage of CPU for each process in proc_list.
        This applies mainly to Atom and VS Code as they run on Electron
        and use helper processes.
    '''
    cpu_percent = 0
    for proc in proc_list:
        cpu_percent += proc.cpu_percent(interval=0)
    return cpu_percent


def get_memory_usage(proc_list):
    '''
        The same of get_cpu_usage, returns memory usage.
    '''
    mem_percent = 0
    for proc in proc_list:
        mem_percent += proc.memory_percent()
    return mem_percent


def log_memory_usage(proc_list):
    '''
        Used for logging only the memory usage of an application. Runs until
        keyboard interrupt. Then outputs maximum and average.
    '''
    try:
        maximum = 0
        total = 0
        ticks = 0
        fname = get_name()
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
    '''
        Same as log_memory_usage but for the CPU.
    '''
    try:
        maximum = 0
        total = 0
        ticks = 0
        fname = get_name()
        for proc in proc_list:
            name = proc.name()
            if "Electron" in name:
                fname = "vscode"
            elif "atom" in name.lower():
                fname = "atom"
            elif "Sublime" in name:
                fname = "sublime"
        with open("./log/cpu_usage_{}.csv".format(fname), "w") as f:
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


def log_all(proc_list, limit=120):
    '''
        logs both CPU and Memory usage of an application. Runs for 120 seconds
        by default. Can be changed by altering limit variable.
    '''
    try:
        max_mem = 0
        max_cpu = 0
        total_mem = 0
        total_cpu = 0
        ticks = 0
        fname = get_name(proc_list)
        with open("./logs/full_log_{}.csv".format(fname), "w") as f:
            f.write("cpu percent, memory percent\n")
            counter = 0
            while counter < limit:
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
        print "Exception occurred, terminating program."
        print "\nMaximum reached cpu usage was   : {}%".format(max_cpu)
        print "Average cpu percentage used was   : {}%".format(total_cpu/ticks)
        print "\nMaximum reached memory usage was: {}%".format(max_mem)
        print "Average memory percentage used was: {}%".format(total_mem/ticks)

get_processes()
