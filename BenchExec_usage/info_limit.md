## Important information
* The default group name is “benchexec” and the permission is given to users in this group. This can be changed by modifying the benchexec-cgroup.service file in etc/systemd/system.

* A directory by the name of benchexec-cgroup.service is made under sys/fs/cgroup/*/system.slice/
  The benchexec group has recursive permission to this directory.
* When runexec runs a temporary directory is created under sys/fs/cgroup/*/system.slice/ benchexec-cgroup.service/
  The limits enforced and processes can be viewed here. As soon as the run ends, this temporary directory is deleted.
* BenchExec always limits the wall time (walltimelimit), too, if the CPU time (timelimit) is limited. This is done to prevent infinitely-long hanging runs if no CPU time is used, e.g., due to a deadlock of the tool.
  Default value of walltimelimit = timelimit/softtimelimit + a few seconds (The wall-time limit is set to value that is slightly higher than the CPU-time limit). For runexec this can be changed by explicitly specifying a wall-time limit, though the wall-time limit cannot be disabled completely if a CPU-time limit is given.
* When enforcing memory limit, swap memory limit is also automatically enforced if swap is enabled (set swapaccount=1 on your kernel command line).
* Soft limits give a time for the tool to end/shutdown gracefully when it exceeds it (including writing output files and generating statistics) before it is killed forcefully when the real time limit is reached. Hard limits forcefully kill.
* The amount of children processes created can be limited by the cgroup pid. The number of concurrent processes and threads is limited on Linux, thus a tool that creates a large number of them (a "fork bomb") can create problems for parallel runs and the rest of the system. BenchExec currently does not automatically handle this, but if runexec is used this can be done easily. Make the pids cgroup available in the same way as the other cgroups, and execute runexec with the additional parameter --set-cgroup-value pids.max=1000 (or any different number). This will limit the amounts of processes and threads that can exist at the same time.

## Limitations
1. The benchexec tool is complicated to run. An XML file with a benchmark definition has to be created. It defines the command(s) to execute, the resource limits, and the tasks for which the command should be run. [Here](https://github.com/sosy-lab/benchexec/blob/master/doc/benchmark.xml) is the complete definition of the input format.

2. If the container of your host machine does not work properly, there could be a directory problem. BenchExec gives an error and does not run. You must specify “--no-container” as a command to run without a container. If you want to run the container you can choose from the [Directory Access Modes](https://github.com/sosy-lab/benchexec/blob/master/doc/container.md).
