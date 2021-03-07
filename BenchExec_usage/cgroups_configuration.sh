#!/bin/bash
trap 'catch' ERR

catch() {
    echo "Restart your system"
}

if [ $(getent group benchexec) ]
then
    echo "benchexec group already exists"
    grep_output=`getent group benchexec | grep $USER`
    if [[ ! $grep_output ]] 
    then
        sudo adduser $USER benchexec
        echo "User '$USER' added to benchexec"
    else
        echo "User '$USER' already exists in benchexec group"
    fi   
else
    sudo groupadd benchexec
    sudo adduser $USER benchexec
    echo "benchexec group created and $USER added to it"
fi


file=/etc/systemd/system/benchexec-cgroup.service
if [[ ! -f  $file ]]
then
    if [[ `wget -S --spider https://raw.githubusercontent.com/sosy-lab/benchexec/master/debian/benchexec-cgroup.service  2>&1 | grep 'HTTP/1.1 200 OK'` ]]
    then
        sudo wget -O /etc/systemd/system/benchexec-cgroup.service  https://raw.githubusercontent.com/sosy-lab/benchexec/master/debian/benchexec-cgroup.service 
    else 
        echo "'benchexec-cgroup.service' file does not exist in the sosy-lab server"
    fi
else
    echo "'benchexec-cgroup.service' file already exists"
fi

systemctl daemon-reload
systemctl enable --now benchexec-cgroup

python3 -m benchexec.check_cgroups

if [[ "$?" = "0" ]]
then
    echo "cgroups have been set"
    echo "Please reboot your system"
else
    #version=`awk -F= '/^NAME/{print $2}' /etc/os-release`
    #if [[ $version == '"Ubuntu"' ]]
    #then
        #file_1=/sys/fs/cgroup/memory/memory.memsw.usage_in_bytes
        #if [[ ! -f  $file_1 ]]
        #then
            #echo 'GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} swapaccount=1"'> swapaccount-for-benchexec.cfg
            #sudo mv ./swapaccount-for-benchexec.cfg /etc/default/grub.d/swapaccount-for-benchexec.cfg
            #sudo update-grub
        #else
            #echo -e "\nSome probelms exist in setting up cgroups, please refer to https://github.com/sosy-lab/benchexec/blob/master/doc/INSTALL.md"
        #fi
    #else
        #echo -e "\nSome probelms exist in setting up cgroups. You are using a distrubution other than Ubuntu. Please adjust your boot loader configuration. Refer to https://github.com/sosy-lab/benchexec/blob/master/doc/INSTALL.md"
    #fi
    echo "Restart your system"
fi

