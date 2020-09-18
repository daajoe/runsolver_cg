from cgroupspy import trees
import os
import subprocess

user=os.getlogin() #name of the user

t=trees.Tree()

name_cg="test" #name of the cgroup


#Creating cgroups for cpuset
cset=t.get_node_by_path('/cpuset/')
cset_cg=cset.create_cgroup(name_cg)

#creating cgroups for cpu
cpu=t.get_node_by_path('/cpu/')
cpu_cg=cpu.create_cgroup(name_cg)

#creating cgroups for memory
memory=t.get_node_by_path('/memory/')
memory_cg=memory.create_cgroup(name_cg)

#paths of the cgroups
path_cpuset="/sys/fs/cgroup/cpuset/"+name_cg
path_cpu="/sys/fs/cgroup/cpu/"+name_cg
path_memory="/sys/fs/cgroup/memory/"+name_cg

#giving permissions to current user
cmd1=["sudo","chown","-R",user,path_cpuset]
cmd2=["sudo","chown","-R",user,path_cpu]
cmd3=["sudo","chown","-R",user,path_memory]
subprocess.run(cmd1)
subprocess.run(cmd2)
subprocess.run(cmd3)