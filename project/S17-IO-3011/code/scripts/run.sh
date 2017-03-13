#!/bin/bash
#move to correct directory
cd ansible

#Run ansible playbook:
ansible-playbook -i inventory cdms.yml
