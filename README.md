# runsolver_cg

cgroups_1 file:
	
	Uses library - "cgroups". Can handle cpu (cpu bandwidth or the minimum % of CPU time) and memory cgroups using the library's functions. Also adds PID(s) by its functions. I can add limitations further through subprocess and cmd, not by using the cgroups library.

setup1 file:

	Solved problems with user access for the cgroup_1 file. Run the setup1.py only once as a root user. Subcgroups can be made and changed without root access.
	
cgroups_2 file:
	
	Uses library - "cgroupspy". The library is just a way to structure cgroups via trees and add limits, not essentially add PID(s). I added PID(s) by using my commands through subprocess and cmd.
	
setup2 file:

	Gives the existing user access to modify and run cgroups. Just run the script once.
