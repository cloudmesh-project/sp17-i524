#!/bin/bash
#move to correct directory
cd ansible

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false

#Make output directory
mkdir -p ../output

#Run ansible playbook:
ansible-playbook -i inventory.txt view.yml
