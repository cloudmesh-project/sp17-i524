#!/bin/bash
#move to correct directory
cd ansible

#Configure Default VM Image
cm default image=Ubuntu-Server-14.04-LTS

#Configure Default VM Flavor
cm default flavor=m1.large

#Run the following command to boot the virtual machine:
cm vm boot

#To see all vms just use the command:
cm vm list

#To login to the vm you need to have a publicly available (floating)
#ip. This can be achieved with the command:
msg=$(cm vm ip assign)

#print out message
echo -e $msg
#find line with IP
line=$(echo -e $msg | grep "Floating IP assigned to")
#get IP
IP=$(echo ${line#*is })
IP=${IP%* info*}
#create inventory file
echo -e "[remote]\n\n$IP\tansible_connection=ssh\tansible_user=cc" > inventory

#You can after this command has succeed login to the vm with the command:
#cm vm ssh

#Maybe run the following on VM:
#sudo dpkg --configure -a

#Edit inventory with IP's of VM's:
#emacs inventory
