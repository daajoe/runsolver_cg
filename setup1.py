#Just run this once

#from cgroups import Cgroup
from cgroups.user import create_user_cgroups
import os



#requires root permission to setup
user=os.getlogin()
create_user_cgroups(user)
print("The root user is ",user," . Now subgroups can be made under this user which will not require root access")