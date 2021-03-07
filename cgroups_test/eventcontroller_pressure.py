import sys
import linuxfd

buffersize = 256

efd=linuxfd.eventfd(0,0) #creates a event file descriptor efd for event notifications

cfd=open(sys.argv[1], mode='w') #opens the cgroup.event_control file

ofd=open(sys.argv[2], mode='r') #opens the memory.pressure_level file

buffer = str(efd.fileno())+" "+str(ofd.fileno())+" "+"critical" #adds values of file descriptors of event notifications and memory.pressure file to a buffer

cfd.writelines(buffer) #writes the event file descriptor efd and memory.pressure_level file desciptor to the cgroups.event_control file desciptor by a buffer
print(buffer)
cfd.close() #closes the cgroup.event_control file


#print(ofd.read())
i=1
while True:
    efd.read()
    print("mem_cgroup pressure event received")
    i=i+1
    print(i)


