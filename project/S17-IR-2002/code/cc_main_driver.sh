#!/bin/bash

DATE="$(date +"%Y.%m.%d_%H.%M.%S")"

#COPY ALL FOLLOWING SCRIPTS [CC_MAIN_DRIVER.SH, CC_ETL_DATA.SH AND CC_ANALYZE_DATA.PY] TO YOUR HOME DIRECTORY (~/)
#INITIATE ANSIBLE AND IMAGES/OUTPUT DIRECTORY ON THE HOST
cd ~
mkdir -p ~/ansible
mkdir -p ~/images

#INSTALL ANSIBLE AND PYTHON ON HOST MECHINE
sudo apt-get update
sudo apt-get -y install ansible
sudo apt-get -y install python-dev python-setuptools python-numpy python-scipy
sudo apt-get -y install python-matplotlib
sudo apt-get -y install python-numexpr
sudo apt-get -y install python-pip
sudo apt-get -y install python-pandas

#INSTALL CLOUDMESH CLIENT ON HOST MECHINE
pip install cloudmesh_client
cm reset
pip uninstall cloudmesh_client
pip install -U cloudmesh_client
cm key add --ssh
cm refresh on


#BUILD CHAMELEON CLUSTER USING CLOUDMESH
cm cluster define --count 3 --image CC-Ubuntu14.04
cm hadoop  define spark pig 
cm hadoop sync
cm hadoop deploy
cm cluster cross_ssh


#GENERATE INVENTORY FILE
cd ~/ansible
cm cluster nodes cluster-001 > cluster_nodes.txt 
awk -F " "  '{print $NF}' cluster_nodes.txt > inventory
chmod 770 inventory
rm cluster_nodes.txt

#GENERATE HOST FILE
echo "[local]" >> hosts; echo "localhost" >> hosts
echo "[master]" >> hosts ;  sed '1q;d'  inventory | sed 's/$/\ ansible_ssh_user=cc/' >> hosts
echo "[slave1]" >> hosts ;  sed '2q;d'  inventory | sed 's/$/\ ansible_ssh_user=cc/' >> hosts
echo "[slave2]" >> hosts ;  sed '3q;d'  inventory | sed 's/$/\ ansible_ssh_user=cc/' >> hosts
chmod 770 hosts

#COPY PY TO THE CLUSTER
ansible master -m copy -a "src=~/cc_analyze_data.py dest=~/cc_analyze_data.py mode=770" 
ansible master -m copy -a "src=~/cc_etl_data.sh dest=~/cc_etl_data.sh mode=770"
ansible master -a "./cc_etl_data.sh"
ansible master -m fetch -a "src=~/images/wage.png dest=~/images/wage.png"
ansible master -m fetch -a "src=~/images/cc_analyze_data.out dest=~/images/cc_analyze_data.out"






