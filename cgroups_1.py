#Requires to install by pip the library cgroups
#pip install cgroups


import os
import subprocess

from cgroups import Cgroup
from cgroups.user import create_user_cgroups

#requires root permission to setup
user=os.getlogin()
create_user_cgroups(user)

#permiss=subprocess.Popen('~/Project_runsolver_cg/Coding/permission.sh', shell=True)


cg=Cgroup('testing')
cg.set_cpu_limit(50) #gives 50% of CPU shares #gives 50% of CPU shares (CPU Bandwidth)
cg.set_memory_limit(500) # sets a memory of 500 Megabytes
""" run_once=False
if not run_once:
    ff=subprocess.call('~/Project_runsolver_cg/Coding/bashfile.sh')
    run_once=True """

def in_cgroup():
    pid=os.getpid()
    cg=Cgroup("testing")
    #cg.set_cpu_limit(50) #gives 50% of CPU shares (CPU Bandwidth)
    #cg.set_memory_limit(500) # sets a memory of 500 Megabytes
    cg.add(pid)
    print(pid)


#to read
cmd=['echo','hey']
#process = subprocess.Popen(cmd, preexec_fn=in_cgroup, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
process = subprocess.Popen(cmd, preexec_fn=in_cgroup)
#process.wait()
#stdout, stderr = process.communicate()
#print (stdout, stderr)
#cg=Cgroup('testing')
cg.add(2958) 
#cg.remove(pid)#remove pid from tasks
#cg.set_cpu_limit() #Reset the cpu limit
#cg.set_memory_limit('testing') #reset the memory limit
#cg.delete() #delete the cgroup

print(cg.cpu_limit)
print(cg.memory_limit)