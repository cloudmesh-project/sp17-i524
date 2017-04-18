#!/bin/bash
#Move to correct directory:
cd ansible

#Run ansible playbook:
ansible-playbook deploy.yml -i inventory --extra-vars "num_nodes=3"

#Configure Default VM Image
#cm default image=Ubuntu-Server-14.04-LTS

#Configure Default VM Flavor
#cm default flavor=m1.large

#Run the following command to boot the virtual machine:
#cm vm boot

#To see all vms just use the command:
#cm vm list

#To login to the vm you need to have a publicly available (floating)
#ip. This can be achieved with the command:
#msg=$(cm vm ip assign)

#print out message
#echo -e $msg
#find line with IP
#line=$(echo -e $msg | grep "Floating IP assigned to")
#get IP
#IP=$(echo ${line#*is })
#IP=${IP%* info*}
#create inventory file
#echo -e "[remote]\n\n$IP\tansible_connection=ssh\tansible_user=cc" > inventory

#You can after this command has succeed login to the vm with the command:
#cm vm ssh

#Maybe run the following on VM:
#sudo dpkg --configure -a

#Edit inventory with IP's of VM's:
#emacs inventory


#cm cluster define --count 3 --image CC-Ubuntu14.04 --flavor m1.medium
#cm hadoop define
#cm hadoop avail
#cm hadoop use stack-004
#cm hadoop sync
#cm hadoop deploy
#cm cluster cross_ssh
#cm vm ssh scmcclar-014
#sudo su - hadoop
#export PATH=$JAVA_HOME/bin:$PATH
#export HADOOP_CLASSPATH=$JAVA_HOME/lib/tools.jar
#hadoop com.sun.tools.javac.Main WordCount.java
#jar cf wc.jar WordCount*.class
#hadoop fs -mkdir /wordcount
#hadoop fs -mkdir /wordcount/input
#echo Hello World Bye World > file01
#echo Hello Hadoop Goodbye Hadoop > file02
#hadoop fs -put file0* /wordcount/input/
#hadoop jar wc.jar WordCount /wordcount/input/ /wordcount/output/
#hadoop fs -cat /wordcount/output/part-r-00000
#yarn logs -applicationId application_1491583308734_0005
#hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /wordcount/input/ -output /wordcount/output/ -mapper /bin/cat -reducer "/usr/bin/wc -w"
#hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -D mapred.reduce.tasks=0 -input /wordcount/input/ -output /wordcount/output1/ -mapper /bin/cat
#hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /CDMS/input -output /CDMS/output -mapper /home/cc/cloudmesh.cdms-master/code/trap_analysis/trap_hadoop -reducer /bin/cat


#/home/cc/binary_to_text.sh
#hadoop fs -put /home/cc/cloudmesh.cdms-master/data/*.txt /cdms/input/
#hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -D mapreduce.input.fileinputformat.split.minsize=7090910 -input /cdms/input -output /cdms/output -mapper /home/cc/cloudmesh.cdms-master/code/trap_analysis/trap_hadoop -reducer /bin/cat
