# runsolver_cg

cgroups_1 file:
	
	Uses library - "cgroups". Can handle cpu (cpu bandwidth or the minimum % of CPU time) and memory cgroups using the library's functions. Also adds PID(s) by its functions.

setup1 file:

	Solved problems with user access. Run the setup1.py only once as a root user. Subcgroups can be amde and changed without root access.
	
cgroups_2 file:
	
	Uses library - "cgroupspy". The library is just a way to structure cgroups via trees, not essentially work with cgroups. I tried it by using my own commands through subprocess and cmd to add PID(s).
