#!/usr/bin/env bash
timestamp=$(date +"%Y%m%d%H%M%S")

. $(dirname "$_")/cloudmesh.config

#number of instances within the cluster
cluster_num=$1
log=deploy_$timestamp.log


function usage
{
    echo "usage: deploy [number of instances]"
}

function generate_inventory
{
    if [ "$1" -lt 1]
      then
        echo "Instance number must be large than 0"
        return;
    fi
}
if [ $# -eq 0 ]
  then
    usage
    return
fi

if [ -z "$1" ]
  then
    usage
    return
fi

#cloudmesh client toolkit setup
cm reset
cm key add --ssh > /dev/null
cm key list
cm refresh on > /dev/null
cm debug off > /dev/null

#create customized security group
cm secgroup add  $security_group ssh 22 22 tcp  0.0.0.0/0
cm secgroup add  $security_group http 80 80 tcp  0.0.0.0/0
cm secgroup add  $security_group https 443 443 tcp  0.0.0.0/0
cm secgroup add  $security_group icmp 0 0 icmp  0.0.0.0/0
for i in $(seq -f %02g 1 $cluster_num);
do 
  cm secgroup add $security_group mongo$i 270$i 270$i tcp 0.0.0.0/0;
done
cm secgroup list
cm key upload --cloud=$cloud
cm secgroup upload --cloud=$cloud

#cluster define and allocate
cm cluster define \
--count=$cluster_num \
--image=$image \
--flavor=$flavor \
--username=$root_user \
--cloud=$cloud \
--secgroup=$security_group

cm cluster avail

while true; do
    read -p "Do you wish to allocate cluster with above setting? " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) return;;
        * ) echo "Please answer yes or no.";;
    esac
done

cm cluster allocate
cm cluster inventory > $(pwd)/inventory.txt 

export ANSIBLE_HOST_KEY_CHECKING=False
ansible all -m ping -i $(pwd)/inventory.txt
