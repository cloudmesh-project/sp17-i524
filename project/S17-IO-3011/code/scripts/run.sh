#!/bin/bash
#move to correct directory
cd ansible

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false

#Supress warnings
export ANSIBLE_DEPRECATION_WARNINGS=false
export ANSIBLE_COMMAND_WARNINGS=false

#Run ansible playbook:
ansible-playbook -i inventory.txt --timeout=2 cdms.yml
