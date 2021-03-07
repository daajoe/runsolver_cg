# cgroups_test
A bit of experimentation with cgroups is done here.

main.py file:
	
	Uses library - "cgroupspy". Can handle cpu bandwidth, cpusets and memory cgroups using the library's functions. Gives different statistics.

setup file.py:

	Run the setup.py only once as a root user to grant future access.
	
delete.py file:

	Run the delete_cg.py only once as a root user to delete cgroups.

eventcontroller.py and eventcontroller_pressure.py:

	These files handle the memory.oom_control and memory.pressure_level featurs respectively provided by the memory resource controller of the cgroups.
	
