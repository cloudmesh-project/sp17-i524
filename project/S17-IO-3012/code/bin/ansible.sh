#!/usr/bin/env bash

mongo_version=$1

SECONDS=0

cd ../work

echo "Beginning Ansible MongoDB deployment"

#create ansible.cfg since command line version isn't working
echo '[defaults]' > ansible.cfg
echo 'host_key_checking = False' >> ansible.cfg

echo "$(date +"%F--%k:%M:%S")...if python does not exist on VM, installing"
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/install-python.yaml > ../stdlist/install-python.log

echo "$(date +"%F--%k:%M:%S")...installing MongoDB"
#install the appropriate version of mongodb
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-install$mongo_version.yaml > ../stdlist/mongo-install$mongo_version.log
#ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-install34.yaml 

echo "$(date +"%F--%k:%M:%S")...distributing key file"
#add the mongo key to all servers
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/add-mongo-key.yaml > ../stdlist/add-mongo-key.log

echo "$(date +"%F--%k:%M:%S")...setting up config servers"
#setup and initialize the config servers
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-config.yaml > ../stdlist/mongo-config.log
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-config2.yaml > ../stdlist/mongo-config2log

echo "$(date +"%F--%k:%M:%S")...setting up mongos servers"
#setup and initialize the mongos servers and add users needed for subsequent steps
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-mongos.yaml > ../stdlist/mongo-mongos.log
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-users.yaml > ../stdlist/mongo-users.log

echo "$(date +"%F--%k:%M:%S")...setting up shards"
#setup and initialize the shards
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-shard.yaml > ../stdlist/mongo-shard.log
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/mongo-shard2.yaml > ../stdlist/mongo-shard2.log
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/add-shards.yaml > ../stdlist/add-shards.log

#capture time
ansible_deploy_time=$SECONDS
echo "ansible_deploy_time" > ansible_deploy_time.csv
echo "$ansible_deploy_time" >> ansible_deploy_time.csv
echo "Deployment via Ansible completed in $ansible_deploy_time seconds"

currentdate=$(date +"%Y%m%d%H%M")
paste -d, current_config_deploy1.csv ansible_deploy_time.csv > ../deploy/deployment_$currentdate.csv

echo "$(date +"%F--%k:%M:%S")...creating collection and getting data for benchmarking"
#create a collection for benchmarking and put the benchmarking data on the servers
#don't include in deploy time since this is benchmarking setup work
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/create-sharded-collection.yaml > ../stdlist/create-sharded-collection.log
ansible-playbook -e 'host_key_checking=False' -i inventory.txt ../playbooks/getdata.yaml > ../stdlist/getdata.log

exit 0
                      
