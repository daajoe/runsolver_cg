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
