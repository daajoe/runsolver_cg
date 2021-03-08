# BenchExec Documentation

## Summary
[BenchExec](https://github.com/sosy-lab/benchexec) is a benchmarking tool which uses the features of the kernel, namely cgroups, for its
reliable measurements and resource management. It limits resources like CPU time and memory and,
can be run in isolation (container) without interfering with other running processes. BenchExec can
be executed on large sets of input files and can generate the results in tabular and graph plotting form.
It consists of 3 programs:
1. runexec: For benchmarking a single tool execution.
2. benchexec: For benchmarking several executions of a tool; and
3. table-generator: For generating result tables.

## Installation guide (Debian or Ubuntu)
### To configure BenchExec

#### pip installation
1. pip3 install benchexec coloredlogs
2. sudo groupadd benchexec
3. sudo adduser *username* benchexec

#### From PPA
1. sudo add-apt-repository ppa:sosy-lab/benchmarking
2. sudo apt install benchexec
3. sudo adduser *username* benchexec

#### Manual installation
1. Download the .deb package from the [releases](https://github.com/sosy-lab/benchexec/releases) by of sosy-lab and install it manually.
2. Then execute the following command:
   - sudo apt install --install-recommends ./benchexec_*.deb
3. sudo adduser *username* benchexec

### To configure cgroups
Most distributions today use systemd which uses cgroups. If your system does not have systemd then
you should mount the cgroup virtual system and adjust the necessary permission accordingly.

Assuming you have systemd,
1. Place the file [benchexec-cgroup.service](https://github.com/sosy-lab/benchexec/blob/master/debian/benchexec-cgroup.service) into /etc/systemd/system/
2. Run the following commands:
   - systemctl daemon-reload
   - systemctl enable --now benchexec-cgroup
3. Check by running:
   - python3 -m benchexec.check_cgroups
   - If something is missing the above command will result in warnings and exit with code 1. If your machine supports swapping it might be turned off by default. Also the memory cgroup may also be disabled by default. You need to enable them both by doing the following:
     - Create the file /etc/default/grub.d/sawpaccount-for-benchexec.cfg with the following content:
       - GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} swapaccount=1"
     - Update grub:
       - sudo update-grub
     - reboot the system

In some Debian kernels the memory cgroup controller is disabled by default and can be enabled by setting cgroup_enable=memory on the kernel command line, similar to swapaccount=1 above.

The following dependencies will be installed upon installing BenchExec:
- benchexec
- lxcfs
- python3-coloredlogs
- python3-humanfriendly
- cpu-energy-meter (recommended)
- libseccomp2 (recommended)
- pqos library (recommended)
- pqos_wrapper (recommended) - It is currently not available as a Debian package and needs
- to be installed manually according to its documentation

## Run instances of runexec
There are several command line parameters that can be given to runexec. Some of the important parameters are:
* --help (gives a list of all the parameters that can be given)
* --memlimit <100> (memory limit in bytes)
* --timelimit <10s> (CPU time after which the tool is forcefully killed)
* --softtimelimit <10s> (CPU time after which the tool is sent a kill/TERM signal)
* --walltimelimit <20s> (Wall clock time after which the tool is forcefully killed)
* --cores <1-3, 7-12> (list of CPU cores to use)
* --memoryNodes <0> (a list of memory nodes in a NUMA system to use)
* --output <name of the file> (where the output of the tool is written)
* --no-container (to run without using the container)
* --maxOutputSize <100> (the number of bytes to which the output of the tool should be truncated approximately if there is too much output)
* --set-cgroup-value <cpu.shares=100> (additional enforcement to use in cgroups)

Some test cases:
* *runexec --walltimelimit 10s --cores 2-4 ./sample.sh*
* *runexec --softtimelimit 15s --timelimit 20s --memlimit 1200 ./sample1.sh*
Here sample1.sh is a script file given as an argument to run.

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
