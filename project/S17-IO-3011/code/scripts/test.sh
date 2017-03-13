#!/bin/bash
msg="Assign IP to scmcclar-009 /Users/scottmcclary/Documents/Spring17/i524/ENV2/lib/python2.7/site-packages/keystoneauth1/adapter.py:136: UserWarning: Using keystoneclient sessions has been deprecated. Please update your software to use keystoneauth1.  warnings.warn('Using keystoneclient sessions has been deprecated. 'DEBUG: Set counter vm_counter to 10 Floating IP assigned to scmcclar-009 is 129.114.33.156 info. OK."
#print out message
echo -e $msg
#find line with IP
line=$(echo -e $msg | grep "Floating IP assigned to")
#get IP
IP=$(echo ${line#*is })
IP=${IP%* info*}
#create inventory file
echo -e "[remote]\n\n$IP\tansible_connection=ssh\tansible_user=cc"
