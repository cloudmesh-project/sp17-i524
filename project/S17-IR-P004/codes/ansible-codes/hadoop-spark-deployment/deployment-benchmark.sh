#!/bin/bash

#ipaddress=$(cm vm list | grep satyam | awk '{print $11}'| head -1)
#sed -i "s/<remote-master-node>/$ipaddress/" inventory


touch benchmark_deployment_jetstream

starttime_deploy=$(date +%s)
ansible-playbook -i inventory playbook.yml --ask-sudo-pass -vvvv
endtime_deploy=$(date +%s)
totaltime_deploy=$((endtime_deploy-starttime_deploy))

echo $totaltime_deploy

echo "deployment file time $(($totaltime_deploy / 60)) minutes and $(($totaltime_deploy % 60)) seconds elapsed." >> benchmark_deployment_jetstream





