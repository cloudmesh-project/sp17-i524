## Predicting Customer Churn Using Apache Spark Machine Learning

### Pre-requisites
In order to run the application on hadoop cluster, you need to have a cluster already deployed onto the cloud. To deploy a hadoop cluster on chameleon cloud, please follow this [tutorial](https://cloudmesh.github.io/classes/lesson/devops/hadoop.html).

### Clone or download sp17-i524 repository to local machine
```
git clone https://github.com/cloudmesh/sp17-i524.git

 ```
 ### After cloning the copy to local, Go to Directory 'sp17-i524/project/S17-IR-P016/ansible-predict'
 ```
 cd sp17-i524/project/S17-IR-P016/ansible-predict
```

### update host file with the IP of your primary node on the cluster
```
vi hosts
```

### execute 'run' script to deploy and run spark application on the cloud.
```
cd ansible-predict
./run.sh
```
This will setup environment,deploy code and other dependencies, submit spark application, and finally fetch result from remote to local machine.

### Finaly look at the result in /tmp directory of your local.

### Troubleshooting
 1. Setting up the environment, installing dependencies on the remote host can take upto **15 minutes**.
 
 2. The ```run.sh``` script might fail in between due various issues like connectivity, ssh, etc. In such events simply re-trigger   the the ```run.sh``` script again.

