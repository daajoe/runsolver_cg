from cgroupspy import trees
import subprocess
import psutil

t=trees.Tree()

name_cg="test" #name of the cgroup
nodepath_cpuset='/cpuset/'+name_cg
nodepath_cpu='/cpu/'+name_cg
nodepath_memory='/memory/'+name_cg
nodepath_cpuacct='/cpuacct/'+name_cg

#assigning cpucores
cset=t.get_node_by_path(nodepath_cpuset)
cset.controller.cpus=[3]

#assigning hard limits on cpu bandwidth
#CPU time is divided by means of specifying how much time can be spent running in a given period
cpu=t.get_node_by_path(nodepath_cpu)
cpu.controller.cfs_quota_us=50000 #the total available run-time within a period, minimum=1ms
cpu.controller.cfs_period_us=50000 #the length of a period, minimum=1ms, maximum=1s

#assigning soft limits on cpu bandwidth
#provide tasks in a cgroup with a relative amount of CPU time, providing an opportunity for the tasks to run
cpu.controller.shares=60

#assigning memory limit
memory=t.get_node_by_path(nodepath_memory)
memory.controller.limit_in_bytes=10000000

#node for cpuacct
cpuacct=t.get_node_by_path(nodepath_cpuacct)

#adding PID
pid=None
path_cpuset="/sys/fs/cgroup/cpuset/"+name_cg+"/tasks"
#print(path_cpuset)
path_cpu="/sys/fs/cgroup/cpu/"+name_cg+"/tasks"
path_memory="/sys/fs/cgroup/memory/"+name_cg+"/tasks"
path_cpuset_mems="/sys/fs/cgroup/cpuset/"+name_cg+"/cpuset.mems"

tasklist=['gnome-mines']
for proc in psutil.process_iter():
    if any(task in proc.name() for task in tasklist):
        print(proc.pid)
        print(proc)
        #print(proc)
        #print(proc.cpu_times())
        pid=str(proc.pid)
#print(psutil.cpu_freq())
cmd="echo 0 > "+path_cpuset_mems
subprocess.run(cmd, shell=True)

cmd1='echo '+pid+' > '+path_cpuset
print("Added PID",pid,"to cpuset")
cmd2='echo '+pid+' > '+path_cpu
print("Added PID",pid,"to cpu")
cmd3='echo '+pid+' > '+path_memory
print("Added PID",pid,"to memory")
subprocess.run(cmd1, shell=True)
subprocess.run(cmd2, shell=True)
subprocess.run(cmd3, shell=True)


while(True):
    #bandwidth statistics 
        #nr_periods: No. of enforcement intervals that have elapsed
        #nr_throttled: No. of times the group has been throttled/limited
        #throttled_time: The total time duration for which entities of the group have been throttled.
    print("Bandwidth stats:",cpu.controller.stat) 

    #reports the total CPU time (in nanoseconds) spent in user and system mode by all the tasks in the cgroup
        #user: Time spent by tasks of the cgroup in user mode
        #system: Time spent by tasks of the cgroup in kernel mode
    print("User and System times:",cpuacct.controller.acct_stat)

    #reports the total CPU time (in nanoseconds) for all tasks in the cgroup
    print("Total CPU time:",cpuacct.controller.usage)

    #reports the total CPU time (in nanoseconds) on each CPU core for all tasks in the cgroup
    print("Total CPU time per core:",cpuacct.controller.usage_percpu)

    #wall clock time or real time elapsed
    cmd_time='command ps -p '+pid+' --no-headers -o etime'
    proc=subprocess.run(cmd_time, shell=True, capture_output=True, universal_newlines=True)
    print("Wall clock time:",proc.stdout.strip())

    #shows the usage of memory
    print("Memory used:",memory.controller.usage_in_bytes)

    #shows the maximum memory usage
    print("Maximum Memory used:",memory.controller.usage_in_bytes)

    #shows the number of memory usage hits limits
    print("No. of memory usage hits:",memory.controller.failcnt)

    #shows various statistics
    print("Stats:",memory.controller.stat)

    #shows the amount of Physical Memory used
    print("Physical Memory used:",memory.controller.stat['rss']+memory.controller.stat['mapped_file'])

    #show the OOM controls
    #print(memory.controller.oom_control)

    subprocess.run('sleep 5', shell=True)
    print("\nAfter 5 seconds")




