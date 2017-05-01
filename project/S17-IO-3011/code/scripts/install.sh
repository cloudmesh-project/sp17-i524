#!/bin/bash
#Move to correct directory
cd ansible

#Turn off SSH authenticity checking
export ANSIBLE_HOST_KEY_CHECKING=false

#Run ansible playbooks:
ansible-playbook -i inventory.txt install_base.yml
ansible-playbook -i inventory.txt install_master.yml
