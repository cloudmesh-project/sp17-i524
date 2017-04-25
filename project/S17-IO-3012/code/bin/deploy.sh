#!/usr/bin/env bash

if [ -z "$1" ]
  then
    echo "Cloud must be specified" >&2; exit 1
fi
if [ -z "$2" ]
  then
    echo "Mongo version must be specified" >&2; exit 1
fi
if [ -z "$3" ]
  then
    echo "Config count must be specified" >&2; exit 1
fi
if [ -z "$4" ]
  then
    echo "Mongos count must be specified" >&2; exit 1
fi
if [ -z "$5" ]
  then
    echo "Shard count must be specified" >&2; exit 1
fi
if [ -z "$6" ]
  then
    echo "Shard replication must be specified" >&2; exit 1
fi


cloud=$1
mongo_version=$2
config_count=$3
mongos_count=$4
shard_count=$5
replica_count=$6

# Validate Parameters

if  [ $cloud != "chameleon" ] && [ $cloud != "kilo" ] && [ $cloud != "jetstream" ]
then
  echo "Cloud must be chameleon or kilo or jetstream" >&2; exit 1
fi

if  [ $mongo_version != 34 ] && [ $mongo_version != "32" ] 
then
  echo "Mongo version must be 34 or 32" >&2; exit 1
fi

# check if number
re='^[0-9]+$'
if ! [[ $config_count =~ $re ]] ; then
   echo "error: Config replica size must be a number" >&2; exit 1
fi
re='^[0-9]+$'
if ! [[ $mongos_count =~ $re ]] ; then
   echo "error: Number of Mongos instances must be a number" >&2; exit 1
fi
re='^[0-9]+$'
if ! [[ $shard_count =~ $re ]] ; then
   echo "error: Number of shards must be a number" >&2; exit 1
fi
re='^[0-9]+$'
if ! [[ $replica_count =~ $re ]] ; then
   echo "Shard replication size must be a number" >&2; exit 1
fi

# check if positive
if [[ $config_count -lt 1 ]] ; then
   echo "error: -c must be a positive number" >&2; exit 1
fi
if [[ $mongos_count -lt 1 ]] ; then
   echo "error: -m must be a positive number" >&2; exit 1
fi
if [[ $shard_count -lt 1 ]] ; then
   echo "error: -s must be a positive number" >&2; exit 1
fi
if [[ $replica_count -lt 1 ]] ; then
   echo "error: -r must be a positive number" >&2; exit 1
fi

#http://stackoverflow.com/questions/806906/how-do-i-test-if-a-variable-is-a-number-in-bash

echo "Cloud: $cloud"
echo "MongoDB Version: $mongo_version"
echo "Config Replica Set Size: $config_count"
echo "Mongos Instances: $mongos_count"
echo "Shards: $shard_count"
echo "Shard Replication Size: $replica_count"

./cluster.sh $cloud $mongo_version $config_count $mongos_count $shard_count $replica_count

./ansible.sh $mongo_version

exit 0
