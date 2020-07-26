from cgroupspy import trees
import os
import subprocess
import psutil

user=os.getlogin()
t=trees.Tree()

""" print("Root:",t.root,"of type",type(t.root))
print("Root children",t.root.children,"of type",type(t.root.children))
cset=t.get_node_by_path('/cpuset/')
print("A specific node",cset,"of type",type(cset))
print("Specific node children",cset.children,"of type",tzype(cset.children))
print("Specific node controller",cset.controller,"of type",type(cset.controller))
print(cset.controller.cpus) """

#cset1=t.get_node_by_path('/cpuset/test/')

#print("A specific node",cset1,"of type",type(cset1))
#print("Specific node children",cset1.children,"of type",type(cset1.children))
#print("Specific node controller",cset1.controller,"of type",type(cset1.controller))
#print(cset1.controller.cpus)
#cmd=['echo ','2810','>','/sys/fs/cgroup/cpuset/test/tasks']

pid=None

tasklist=['firefox']
for proc in psutil.process_iter():
    if any(task in proc.name() for task in tasklist):
        #print(proc.pid)
        pid=str(proc.pid)

cmd='echo '+pid+' > /sys/fs/cgroup/cpuset/prac/tasks'
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
stdout, stderr = process.communicate()
print (stdout.strip('\n'), stderr)
#test=cset.create_cgroup('test')
#test.controller.cpus=[1]
#print(test.controller.cpus)

cset1=t.get_node_by_path('/cpuset/prac/')
cset1.controller.cpus=[3] #sets cpu cores

#print(cset1)
#print(cset1.controller)
#print(cset1.controller.cpus)
#test1=cset1.create_cgroup('test1')
