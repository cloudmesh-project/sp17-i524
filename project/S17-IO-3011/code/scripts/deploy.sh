#!/bin/bash
#Move to correct directory:
cd ansible

#Parse input (if exists) otherwise default to 1 virtual machine
if [ "$#" -eq 0 ]; then
    export num_nodes=1
else 
    export num_nodes=$1
fi

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false

#Run ansible playbook:
ansible-playbook deploy.yml -i inventory.txt --extra-vars "num_nodes=$num_nodes"
