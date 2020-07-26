#Requires to install by pip the library cgroups #Not available in conda or its channels
#pip install cgroups


import os
import subprocess
import psutil

from cgroups import Cgroup
#from cgroups.user import create_user_cgroups
user=os.getlogin()

#A subcgroup 'testing' will be made under the root user
cg=Cgroup('test')
cg.set_cpu_limit(70) #gives 70% of CPU shares #gives 70% of CPU shares (CPU Bandwidth) #total is 1024 units
cg.set_memory_limit(100) # sets a memory of 100 Megabytes


process_pid=None
def in_cgroup(p_pid):
    cg=Cgroup("test")
    cg.add(p_pid)
    print("The pid added to the subcgroup:",p_pid)

#cmd=['echo','hey']
#cmd2=['ls']
tasklist=['firefox']
for proc in psutil.process_iter():
    if any(task in proc.name() for task in tasklist):
        #print(proc.pid)
        process_pid=proc.pid
        
in_cgroup(process_pid)


#cg.add(2958) #to add other PID while the previous process is running
#cg.remove(pid) #remove pid from tasks

#cg.set_cpu_limit() #Reset the cpu limit
#cg.set_memory_limit('testing') #reset the memory limit

#cg.delete() #delete the cgroup

print("CPU limit given:",cg.cpu_limit,'%') #print the cpu_limit
print("Memory limit given:",cg.memory_limit,'MB') #print the memory_limit
