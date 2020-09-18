from cgroupspy import trees

t=trees.Tree()
""" 
def del_cg(name):
    cset=t.get_node_by_path('/cpuset/')
    cset.delete_cgroup(name)

    cpu=t.get_node_by_path('/cpu/')
    cpu.delete_cgroup(name)


    memory=t.get_node_by_path('/memory/')
    memory.delete_cgroup(name) """

name="test"

cset=t.get_node_by_path('/cpuset/')
cset.delete_cgroup(name)

cpu=t.get_node_by_path('/cpu/')
cpu.delete_cgroup(name)

memory=t.get_node_by_path('/memory/')
memory.delete_cgroup(name)
