# BenchExec Documentation

## Summary
[BenchExec](https://github.com/sosy-lab/benchexec) is a benchmarking tool which uses the features of the kernel, namely cgroups, for its
reliable measurements and resource management. It limits resources like CPU time and memory and,
can be run in isolation (container) without interfering with other running processes. BenchExec can
be executed on large sets of input files and can generate the results in tabular and graph plotting form.
It consists of 3 programs:
1. runexec: For benchmarking a single tool execution.
2. benchexec: For benchmarking several executions of a tool; and
3. table-generator: For generating result tables.

## Installation guide (Debian or Ubuntu)
### To configure BenchExec

#### pip installation
1. pip3 install benchexec coloredlogs
2. sudo groupadd benchexec
3. sudo adduser *username* benchexec

#### From PPA
1. sudo add-apt-repository ppa:sosy-lab/benchmarking
2. sudo apt install benchexec
3. sudo adduser *username* benchexec

#### Manual installation
1. Download the .deb package from the [releases](https://github.com/sosy-lab/benchexec/releases) by of sosy-lab and install it manually.
2. Then execute the following command:
   - sudo apt install --install-recommends ./benchexec_*.deb
3. sudo adduser *username* benchexec

### To configure cgroups
Most distributions today use systemd which uses cgroups. If your system does not have systemd then
you should mount the cgroup virtual system and adjust the necessary permission accordingly.

Assuming you have systemd,
1. Place the file [benchexec-cgroup.service](https://github.com/sosy-lab/benchexec/blob/master/debian/benchexec-cgroup.service) into /etc/systemd/system/
2. Run the following commands:
   - systemctl daemon-reload
   - systemctl enable --now benchexec-cgroup
3. Check by running:
   - python3 -m benchexec.check_cgroups
   - If something is missing the above command will result in warnings and exit with code 1. If your machine supports swapping it might be turned off by default. Also the memory cgroup may also be disabled by default. You need to enable them both by doing the following:
     - Create the file /etc/default/grub.d/sawpaccount-for-benchexec.cfg with the following content:
       - GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} swapaccount=1"
     - Update grub:
       - sudo update-grub
     - reboot the system

In some Debian kernels the memory cgroup controller is disabled by default and can be enabled by setting cgroup_enable=memory on the kernel command line, similar to swapaccount=1 above.

The following dependencies will be installed upon installing BenchExec:
- benchexec
- lxcfs
- python3-coloredlogs
- python3-humanfriendly
- cpu-energy-meter (recommended)
- libseccomp2 (recommended)
- pqos library (recommended)
- pqos_wrapper (recommended) - It is currently not available as a Debian package and needs
- to be installed manually according to its documentation
