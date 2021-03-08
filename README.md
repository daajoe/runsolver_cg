# runsolver_cg
BenchExec is a benchmarking tool which uses the features of the kernel, namely cgroups, for its
reliable measurements and resource management. It limits resources like CPU time and memory and,
can be run in isolation (container) without interfering with other running processes. BenchExec can
be executed on large sets of input files and can generate the results in tabular and graph plotting form.
It consists of 3 programs:
- runexec: For benchmarking a single tool execution.
- benchexec: For benchmarking several executions of a tool; and
- table-generator: For generating result tables.

1. [Installation guide for BenchExec](BenchExec_usage/documentation.md)
2. [Run instances of *runexec*](BenchExec_usage/run_instances_runexec.md)
3. [Important informration and limitations with regards to BenchExec](BenchExec_usage/info_limit.md)
