#!/bin/bash
#Move to correct directory:
cd ansible

#Parse input (if exists) otherwise default to 3 nodes
if [ "$#" -eq 0 ]; then
    num_nodes=3
else 
    num_nodes=$1
fi

#define some variables
image=CC-Ubuntu14.04
flavor=m1.medium
cloud=chameleon

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false

#Run ansible playbook:
ansible-playbook deploy.yml -i inventory --extra-vars "num_nodes=$num_nodes image=$image flavor=$flavor cloud=$cloud"
