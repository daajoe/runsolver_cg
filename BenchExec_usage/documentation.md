# BenchExec Documentation
## Summary
BenchExec is a benchmarking tool which uses the features of the kernel, namely cgroups, for its
reliable measurements and resource management. It limits resources like CPU time and memory and,
can be run in isolation (container) without interfering with other running processes. BenchExec can
be executed on large sets of input files and can generate the results in tabular and graph plotting form.
It consists of 3 programs:
1. runexec: For benchmarking a single tool execution.
2. benchexec: For benchmarking several executions of a tool; and
3. table-generator: For generating result tables.
