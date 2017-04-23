#!/usr/bin/env bash

ip_address=$(head -n 1 ../work/mongos_main_ip.txt)
user_name=$(head -n 1 ../work/clouduser.txt)
path=$(head -n 1 ../work/clouddir.txt)

ssh $user_name@$ip_address "mongo < $path/shard_distribution.js" > ../work/distribution

cat ../work/distribution | grep -v "shell version" | grep -v "connecting to" | grep -v "server version" | grep -v "switched to" | grep -v "bye" | tail -n +2
