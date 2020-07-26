#Just run this once

from cgroupspy import trees
import os
import subprocess

user=os.getlogin()

t=trees.Tree()
cset=t.get_node_by_path('/cpuset/')
cset.create_cgroup('prac') #requires root permission to setup

cmd='sudo chown -R ${USER} /sys/fs/cgroup/cpuset/prac' #giving permissions to current user

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
stdout, stderr = process.communicate()
print (stdout.strip('\n'), stderr)
