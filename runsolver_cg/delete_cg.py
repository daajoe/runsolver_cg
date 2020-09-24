from cgroupspy import trees
import setup
t=setup.t
name="hey"

""" cset=t.get_node_by_path('/cpuset/')
f=cset.children
s=str(f[0])
if "test" in s:
    cset=t.get_node_by_path('/cpuset/')
    cset.delete_cgroup(name)

    cpu=t.get_node_by_path('/cpu/')
    cpu.delete_cgroup(name)

    memory=t.get_node_by_path('/memory/')
    memory.delete_cgroup(name) """

cset=t.get_node_by_path('/cpuset/')
cset.delete_cgroup(name)

cpu=t.get_node_by_path('/cpu/')
cpu.delete_cgroup(name)

memory=t.get_node_by_path('/memory/')
memory.delete_cgroup(name)

print("Cgroup",name,"deleted")
