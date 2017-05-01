cd ../benchmark

echo "cloud,config_replicas,mongos_instances,shard_replicas,shards_per_replica,mongo_version,test_size,import_time,find_time,mapreduce_time" > combined_benchmark.csv
cat benchmark_*csv | grep -v "cloud,config_replicas,mongos_instances,shard_replicas,shards_per_replica,mongo_version,test_size,import_time,find_time,mapreduce_time" >> combined_benchmark.csv

cd ../deploy		

echo "cloud,config_replicas,mongos_instances,shard_replicas,shards_per_replica,mongo_version,cluster_deploy_time,ansible_deploy_time" > combined_deployment.csv
cat deployment_*csv | grep -v "cloud,config_replicas,mongos_instances,shard_replicas,shards_per_replica,mongo_version,cluster_deploy_time,ansible_deploy_time" >> combined_deployment.csv
