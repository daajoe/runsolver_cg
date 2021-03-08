# runsolver_cg
BenchExec is a benchmarking tool which uses the features of the kernel, namely cgroups, for its
reliable measurements and resource management. It limits resources like CPU time and memory and,
can be run in isolation (container) without interfering with other running processes. BenchExec can
be executed on large sets of input files and can generate the results in tabular and graph plotting form.
It consists of 3 programs:
- runexec: For benchmarking a single tool execution.
- benchexec: For benchmarking several executions of a tool; and
- table-generator: For generating result tables.

1. [Installation guide for BenchExec](BenchExec_usage/documentation.md)
2. [Run instances of *runexec*](BenchExec_usage/run_instances_runexec.md)
3. [Important information and limitations with regards to BenchExec](BenchExec_usage/info_limit.md)

## cgroups_test
A bit of experimentation with cgroups was done to see how resources were monitored and limited.

[main.py](cgroups_test/main.py) script:
	
	Uses library - "cgroupspy". Can handle cpu bandwidth, cpusets and memory cgroups using the library's functions. Gives different statistics.

[setup file](cgroups_test/setup.py) script:

	Run the setup.py only once as a root user to grant future access.
	
[delete.py](cgroups_test/delete.py) script:

	Run the delete_cg.py only once as a root user to delete cgroups.

[eventcontroller.py](cgroups_test/eventcontroller.py) and [eventcontroller_pressure.py](cgroups_test/eventcontroller_pressure.py) scripts:

	These scripts handle the memory.oom_control and memory.pressure_level featurs respectively provided by the memory resource controller of the cgroups.
