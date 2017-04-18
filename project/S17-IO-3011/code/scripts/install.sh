#!/bin/bash
#Move to correct directory
cd ansible

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false

#Run ansible playbook:
ansible-playbook -i inventory install_base.yml
ansible-playbook -i inventory install_master.yml
