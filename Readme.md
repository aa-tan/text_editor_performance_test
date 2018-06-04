# Text Editor Performance Measure
#### As part of Operating Systems class final project
This script can be used to measure the CPU and Memory usage of an application.

### Usage

Start the program

```bash
python -i logger.py
```

Make sure either Sublime Text, Atom, VS Code, or a combination of the three is open. If they were not open prior to starting the script, open them. Then run this function in the python interpreter next:

```bash
get_processes()
```

The following functions ask for a process list as an argument. Assuming one of the three text editors was opened and the get_process() function worked as intended, the process list variable for each can be called as such:

|Application|Variable name
|---|---
|VS Code|code_processes
|Atom|atom_processes
|Sublime Text|subl_processes

The following functions can be then called, replace proc_list with the above mentioned variable names:

|Function call|Description
|---|---
|get_memory_usage(proc_list)| Returns the current memory usage of a given process list.
|get_cpu_usage(proc_list)| Returns the current CPU usage of a given process list.
|log_memory_usage(proc_list)| Logs the memory usage of given process list.Stopped via ctrl-c.
|log_cpu_usage(proc_list)| Logs the CPU usage of given process list. Stopped via ctrl-c.
|log_all(proc_list, limit)| Logs both memory and CPU usage of given process list. Limit can be sent to the number of logs made. Default is 120.
