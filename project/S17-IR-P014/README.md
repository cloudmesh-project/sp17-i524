## Analysis of Airline delays data using Spark and HDFS

### Pre-requisites
The prerequisites for the project includes:
-Installation of Cloudmesh-client
-Deployment of a cluster
The cluster must be a three-node hadoop cluster with Spark as an addon.

### Cloning the sp17-i524 repository

Once you are able to ssh into the nodes of the cluster

```
git clone https://github.com/cloudmesh/sp17-i524.git
```

After cloning the repository, Go to Directory 'sp17-i524/project/S17-IR-P014/ansible'

### Updating host file with the IP of the master node on the cluster
```
vi hosts
```
### Running the ansible playbook 
 ```
 ansible-playbook deploy.yml
```
This will setup environment and deploys code and other dependencies.
### Launching Hadoop

ssh into the master node and run the following command
```
sudo su - hadoop
```
### Running the spark application
Change the directory to the airlines folder that contains the code
```
cd /tmp/airlines/code/
```
Run the following command for executing the Spark job
```
spark-submit --master yarn --deploy-mode client --executor-memory 1g \ delay.py \
hdfs://localipaddressOfMasterNode:8020/fltdata/airlines.csv \
hdfs://localipaddressOfMasterNode:8020/fltdata/flights.csv \
hdfs://localipaddressOfMasterNode:8020/fltdata/airports.csv \
```
### Results 
The results can be found in the hadoop folder
```
cd ~/hadoop/
```


