#Requires to install by pip the library cgroups
#pip install cgroups

from cgroups import Cgroup
from cgroups.user import create_user_cgroups
import os
import subprocess

#requires root permission
user=os.getlogin()
create_user_cgroups(user)

def in_cgroup():
    pid=os.getpid()
    print(pid)


#to read
cmd=['echo', 'Hello']
process = subprocess.Popen(cmd, preexec_fn=in_cgroup, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
stdout, stderr = process.communicate()
print (stdout.strip('\n'), stderr)