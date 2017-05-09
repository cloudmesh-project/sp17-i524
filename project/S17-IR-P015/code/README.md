# Deployment of Storm cluster 

## Prerequisites:
1. Cluster with ip addresses
2. Ansible software

## Steps to create a storm cluster:
1. Go to hosts file in the ansible working directory and add the IP address under the group “cluster”. 

Create the hosts file if necessary.
>> 1.a. Add a variable to each IP address with the host name under ‘host’

```
E.g. node1 ansible_host=“#ip” ansible_user=“cc” host=“abalaga-081”
```
(Note, we did not know about the cm cluster inventory command earlier and hence could not incorporate it into the code)
>> 1.b. Create two new groups, nimbus and supervisors.

>> 1.c. Nimbus group contains the ip address of the storm master node using the same format as above.

>> 1.d. supervisors group contains a list of ip addresses of the storm worker nodes using the same format as above.

__Running Ansible Playbook__

*  Run the ansible playbook on the terminal using the following command, by using the command we have fixed the roles issue which we had earlier
```
ansible-role cloudmesh.storm
```
Alternatively  ansible-playbook may be used as follows:
```
ansible-playbook ./tasks/main.yml
```
Also, the above can be run by the following command, replace chameleon with different clouds:
```
ansible-playbook main.yml --extra-vars "cloud=chameleon"
```

Command to install the software on all the nodes and configures the nodes

* Run the start zookeeper.yml file
```
ansible-playbook startzookeeper.yml
```
Command to start the zookeeper server cluster

* Create another host file with only ip addresses (nimbus should be first) and run the startStorm.sh file using the following command
```
bash -s startStorm.sh
```
This command ssh’s to all the nodes and starts the storm processes (nimbus on master and supervisor on workers)

* Any topology may be submitted to the cluster using the submit.sh file.
>> a. Create a jar file containing the topology. Ensure that StormSubmitter() is used in the Topology class (to deploy on a production cluster).

>> b. Move the jar to the ansible folder or download the jar file on GitHub.

>> c. Run the submit.sh file with the following command
```
bash -s submit.sh <nimbus ip> <jar file> <name of topology> <name of the job to submit>
```
```
E.g. bash -s submit.sh “#ip” storm-starter.jar storm.starter.ExclamationTopology exclamation-topology
```
This job copies the jar file to the nimbus and runs the storm command to submit to the cluster.

The storm cluster is set up and a job is being run on the cluster.

### Storm UI
To check cluster statistics, storm ui may be enabled.
> 1. Type the IP address of the nimbus into a browser along with the port 8080.
> 2. This opens the storm ui and the cluster details are mentioned.
> 3. Currently running jobs are displayed.

