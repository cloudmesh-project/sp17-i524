#!/usr/bin/env bash

cloud=$1
mongo_version=$2
config_count=$3
mongos_count=$4
shard_count=$5
replica_count=$6

SECONDS=0

cd ../work

rm -f *
#rm -f mongod.conf.shard*.run
#rm -f ip_list.*
#rm -f mongo_work.*
#rm -f mongo_shard_work.*
#rm -f shard_*.list
#rm -f ip_shard.list.*
#rm -f *txt
#rm -f initiate_shard_*
#rm -f ../json/initiate_shard_*
#rm -f add_shard*.js
#rm -f ../json/add_shard*.js

echo "cloud,config_replicas,mongos_instances,shard_replicas,shards_per_replica,mongo_version" > current_config.csv
echo "$cloud,$config_count,$mongos_count,$shard_count,$replica_count,$mongo_version" >> current_config.csv

if [ $cloud == "chameleon" ]
 then
        echo 'cc' > clouduser.txt
        user_name=cc
        echo '/home/cc/mongo-project' > clouddir.txt
        mongodir=/home/cc/mongo-project
#	image=CC-Ubuntu16.04
elif [ $cloud == "jetstream" ]
 then
        echo 'root' > clouduser.txt
	user_name=root
        echo '/root/mongo-project' > clouddir.txt
	mongodir=/root/mongo-project
#	image='\"Ubuntu 16.04 LTS\"'
elif [ $cloud == "kilo" ]
 then
        echo 'ubuntu' > clouduser.txt
	user_name=ubuntu
        echo '/home/ubuntu/mongo-project' > clouddir.txt
	mongodir=/home/ubuntu/mongo-project
#	image=Ubuntu-16.04-64
 else
        echo "Invalid Cloud Specified"
	exit 0
fi

vm_count=$(expr $config_count + $mongos_count + $shard_count \* $replica_count)
#echo $vm_count

cm refresh on > /dev/null
cm debug off > /dev/null

cm default cloud=$cloud

echo "$(date +"%F--%k:%M:%S")...adding security group and rules to cloud"

#cm_username=cloudmesh.profile.user
security_group=mccombe-mongo-proj

cm secgroup add  $security_group http 80 80 tcp  0.0.0.0/0
cm secgroup add  $security_group ssh 22 22 tcp  0.0.0.0/0
#cm secgroup add  $security_group icmp -1 -1 icmp  0.0.0.0/0
cm secgroup add  $security_group https 443 443 tcp  0.0.0.0/0
cm secgroup add  $security_group mongo1 27017 27017 tcp  0.0.0.0/0
cm secgroup add  $security_group mongo2 27018 27018 tcp  0.0.0.0/0
cm secgroup add  $security_group mongo3 27019 27019 tcp  0.0.0.0/0
cm secgroup add  $security_group mongo4 28017 28017 tcp  0.0.0.0/0

cm secgroup upload --cloud=$cloud > ../stdlist/secgroup_upload.log

#cm secgroup upload $security_group

cm default secgroup=$security_group

#Create mongo.key
openssl rand -base64 755 > mongo.key
chmod 700 mongo.key

if [ $cloud == "chameleon" ]
 then
        cm cluster define --count $vm_count --image CC-Ubuntu16.04
elif [ $cloud == "jetstream" ]
 then
        cm cluster define --count $vm_count --image \"Ubuntu 16.04 LTS\"
elif [ $cloud == "kilo" ]
 then
        cm cluster define --count $vm_count --image Ubuntu-16.04-64

fi

echo "$(date +"%F--%k:%M:%S")...allocating cluster"
echo "Depending on size of cluster, may take several minutes"
cm cluster allocate  > ../stdlist/cluster_allocate.log
echo "$(date +"%F--%k:%M:%S")...cluster allocation complete"
cm cluster nodes > node.list

cut -d ' ' -f 2 node.list > ip.list
cat ip.list > mongo_all.txt
echo '[mongodb_all]' > inventory.txt
cat mongo_all.txt >> inventory.txt

head -$config_count ip.list > config.list
tail -n +$(expr $config_count + 1) ip.list > ip.list.1
head -$config_count mongo_all.txt > config.txt
tail -n +$(expr $config_count + 1) mongo_all.txt > mongo_work.1
echo '[mongodb_config]' >> inventory.txt
sed 's/$/ REPSET_NM=repset_config/' config.txt > config1.txt
cat config1.txt >> inventory.txt
echo '[mongodb_config_1]' >> inventory.txt
head -1 config.txt >> inventory.txt

head -$config_count ip.list.1 > mongos.list
tail -n +$(expr $config_count + 1) ip.list.1 > ip_shard.list.1
head -$mongos_count mongo_work.1 > mongos.txt
tail -n +$(expr $mongos_count + 1) mongo_work.1 > mongo_shard_work.1
echo '[mongodb_mongos]' >> inventory.txt
one_config_ip_address=$(head -n 1 config.list)
sed "s/$/ CONFIG_REPSET=repset_config CONFIG_HOSTNAME=$one_config_ip_address/" mongos.txt > mongos1.txt
cat mongos1.txt >> inventory.txt
echo '[mongodb_mongos_1]' >> inventory.txt
head -1 mongos.txt >> inventory.txt
head -1 mongos.txt > mongos_main_ip.txt

current_shard=1
echo "[mongodb_shard]" >> inventory.txt 
while [ $current_shard -le $shard_count ]
do
	head -$replica_count ip_shard.list.$current_shard > shard_$current_shard.list
	tail -n +$(expr $replica_count + 1) ip_shard.list.$current_shard > ip_shard.list.$(expr $current_shard + 1)
	head -$replica_count mongo_shard_work.$current_shard > shard_$current_shard.txt
	tail -n +$(expr $replica_count + 1) mongo_shard_work.$current_shard > mongo_shard_work.$(expr $current_shard + 1)
#####        echo "[mongodb_shard$current_shard]" >> inventory.txt
	sed "s/$/ REPSET_NM=repset_shard$current_shard/" shard_$current_shard.txt > shard_$current_shard.1.txt
	cat shard_$current_shard.1.txt >> inventory.txt

cut -d ' ' -f 1 shard_$current_shard.txt > initiate_ips_shard${current_shard}.txt

	current_shard=$(expr $current_shard + 1)
done


#build the shard initiate file
rm -f initiate_shard*.js

shard_number=$shard_count

echo '[mongodb_shard_1]' >> inventory.txt
echo "db.getSiblingDB(\"admin\").auth(\"cluster_admin_user\", \"cluster_admin_password\" )" > add_shard$shard_number.js

while [[ $shard_number -gt 0 ]]
do
        echo "rs.initiate(
          {
            _id: \"repset_shard${shard_number}\",
            members: [" > initiate_shard$shard_number.js1

        counter=0
        while read ip_address
        do
		if [[ counter -eq 0 ]]
		then
			echo "$ip_address INITIATE_FILE=initiate_shard$shard_number.js" >> inventory.txt
			echo "sh.addShard(\"repset_shard$shard_number/$ip_address:27018\")" >> add_shard$shard_number.js
			cat add_shard$shard_number.js >> add_shards.js
		fi

                echo "      { _id : $counter, host : \"$ip_address:27018\" }," >> initiate_shard$shard_number.js1
                ((counter++))
        done < initiate_ips_shard$shard_number.txt #>> initiate_shard$shard_number.js1

        sed '$ s/.$//' initiate_shard$shard_number.js1 > initiate_shard$shard_number.js

        echo '    ]
          }
        )' >> initiate_shard$shard_number.js

	cp initiate_shard$shard_number.js ../json/initiate_shard$shard_number.js

        ((shard_number--))
done

cp add_shards.js ../json/add_shards.js

echo "[all:vars]" >> inventory.txt
echo "ansible_ssh_user=$user_name" >> inventory.txt
echo "MONGO_DIR=$mongodir" >> inventory.txt


sed 's/^/ssh-keygen -R /g' ip.list > sshkeygen.run
chmod 700 sshkeygen.run
./sshkeygen.run > ../stdlist/sshkeygen.log 2>&1 &

sleep 10

cluster_deploy_time=$SECONDS
echo "VM Cluster created in $cluster_deploy_time seconds"

echo "cluster_deploy_time" > cluster_deploy_time.csv
echo "$cluster_deploy_time" >> cluster_deploy_time.csv

paste -d, current_config.csv cluster_deploy_time.csv > current_config_deploy1.csv

exit 0
