### To copy files from code to $HOME/outbrain
1. cd <code_directory>/
2. sh copy_repository_files.sh
3. cd $HOME/outbrain/
### To deploy/redeploy cluster
  # for deploying fresh and provide #nodes as argument
3.  sh install_hadoop_pig.sh <#nodes>
  # for deploying another cluster
3.  sh re_deploy_cluster.sh <#nodes>

### login to namenode in a new terminal and execute following command
4.  cm vm ssh <namenode>
5.  sudo su - hadoop 
6.  tar -xzvf dataset.tgz
	
### move data to hdfs using ansible palybook
### run the following command from local machine
7. time ansible-playbook -i hosts move_data_hdfs.yml

### on namenode Run the benchmark_pig.sh script in the background using 
# 1)chek nohup for time lapase
# 2)check time_outputs.txt for pig console log
8. nohup bash benchmark_pig.sh &


