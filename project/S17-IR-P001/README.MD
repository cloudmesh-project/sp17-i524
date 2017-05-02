README
========
 
This Ansible Galaxy project collects realtime twitter streaming data and performs multiple text analysis including
identifying the sentiment of the tweet (using naiveBayes on a spark cluster), finding the top co-occuring word in the tweet
Projecting the sentiment of tweets across US States,etc.

Pre Requisites
================

You are expected to use a Linux machine which has the following packages installed:
- Git
- Cloudmesh Client (and having a valid cloudmesh.yml file for accessing Chameleon Cloud)
- Ansible

You are expected to create API keys in twitter to collect the data from Twitter. This can be achieved using the following steps:
```
1- Log into the Twitter Developers section.If you don't already have an account, you can login with your normal 
Twitter credentials
2- Go to "Create an app"
3- Fill in the details of the application you'll be using to connect with the API
4- Your application name must be unique. If someone else is already using it, you won't be able to register your 
application until you can think of something that isn't being used.
5- Click on Create your Twitter application
6- Details of your new app will be shown along with your consumer key and consumer secret.scroll down and click 
Create my access token.
```
These 2 keys and 2 tokens are necessary to run the Python script that fetches the data from Twitter streaming API.


Deployment
==========
It is necessary that the security groups are updated so that the ports "5025", "1234" and "1240" can be accessed from the local machine running the ansisble playbooks. This can be done using 

```
cm secgroup add groupName ruleName startPort endPort protocol 0.0.0.0/1
```

1- In order to install cloudmesh client hadoop-spark-playbook.yml. It runs on the local host and it creates a hadoop cluster with spark and establishes connection between the nodes. 
2- Then run the inv.yml playbook that generates the inventory file. This generates inventory file for the remaining playbooks
3- The code/ansible/test.yml playbook runs the the tasks for setting up the environment for pyspark, analysis, benchmarking and installling pre requisites such as node-js.

The following modifications have to be made to run the bechmarks
..* code/ansible/chameleon_ben1 obtains the benchmark for running the code in "cluster mode" using YARN on a 3 node spark cluster. 
..* code/ansible/chameleon_ben2 has the role to run spark in standalone mode with one worker node. 
..* code/ansible/chameleon_ben3 has the role to run spark in standalone mode with one worker node. 
..* Hadoop and spark jobs can be viewed in the web UI interface. While running spark in cluster mode, the application can be viewd in http://<ip_address>:8088/cluster/cluster where <ip_address> is the ip of the floating ip of the virtual machine.

..*For running spark jobs in standalone mode, the master and the slave must be started manually which had been included in the ansible code. However, the URL of the master may vary depending on the system started. In order to run the role in code/ansible/chameleon_ben2 and code/ansible/chameleon_ben3 , The master URL must be changed. The portion of code to be change is commented in each file(main.yml). An example s shown below. 
```
     chdir=/opt/spark-1.6.0-bin-hadoop2.6/ sudo ./sbin/start-slave.sh spark://stack-0050:7077 
```
In the code above, change the "stack-0050" to the the stack that was deployed in master node of spark.

4- To extract the data from twitter, first obtain the API keys from twitter https://apps.twitter.com/. Log in to the virtual machine under [master] in inventory.txt and go to /home/cc/visualization folder. Open Finalscript.py and update the API keys in lines 24-27.

5- Run ansible-vis-playbook.yml to enable the visualizations in the corresponding ports inside the virtual machine

Visualization
================

Below are the six different visualization that shows the output of the analysis performed. Each of the those can be accessed using the
public ip of the system as shown above each chart. It is necessary that the security groups are updated so that the ports "5025", "1234"
"1240" can be accessed from the local machine running the ansisble playbooks.

Vis Location: http://public_ip:1234

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/realtime.JPG" alt="Realtime Tweet" width="600" height="449"/>

Vis Location: http://public_ip:1240/US_heat_count

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/us_tweet.JPG" alt="US State Tweet Count" width="600" height="388"/>

Vis Location: http://public_ip:1240/map-pies

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/us_senti.JPG" alt="US State-wise Sentiment" width="600" height="388"/>

Vis Location: http://public_ip:1240/co_occur_new.html

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/cooccur.JPG" alt="Tweet token Co-occurence" width="727" height="727"/>

Vis Location: http://public_ip:1240/dynamic-master-detail

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/timechart.JPG" alt="Total Tweets vs Time" width="800" height="300"/>

Vis Location: http://public_ip:1240/heatmap

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/senticont.jpeg" alt="Sentiment Heatgrid" width="700" height="300"/>
