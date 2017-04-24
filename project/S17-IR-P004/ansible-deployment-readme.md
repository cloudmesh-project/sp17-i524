Automated deployment spark cluster using ansible:

1. To install cloudmesh client for the first time 'playbook-cloudmesh-first-time-install.yml' with following command(Skip the step if the cloudmesh client is already installed):

        ansible-playbook playbook-cloudmesh-first-time-install.yml --ask-sudo-pass -vvvv


2. Update the contents of cloudmesh client configuration file ~/.cloudmesh/cloudmesh.yaml : 

2.1 Edit the following section,the entry with < > should be customized as per your credentials:

	profile:
	     firstname: <first name>
	     lastname: <last name>
	     email: <email id>
	     user: <chameleon/jetsream/other cloud username>


2.2. Change the entry of active cloud to use your favorite cloud,for example chameleon shown here:


	active:
	- chameleon
	clouds:
	...


2.3.Under the preferred cloud(chameleon/jestream/..) change the following entry, the entry with < > should be customized as per your credentials:

	credentials:
	OS_PASSWORD: <cloud password>
	OS_TENANT_NAME: CH-818664
	OS_TENANT_ID: CH-818664
	OS_PROJECT_NAME: CH-818664
	OS_USERNAME: <username>


2.4. (Step only for Chameleon cloud configuration) Also change, the type of OS and flavor you want for hadoop/spark cluster(recommended) under your preferred cloud:

	default:
		flavor: m1.medium
		image: CC-Ubuntu14.04

2.5 (Step only for Jetstream cloud configuration) Change the type of OS and flavor you want for hadoop/spark cluster(recommended) under your preferred cloud:

	default:
		flavor: m1.small
		image: ubuntu-14.04-trusty-server-cloudimg


3. Edit the file 'hadoop-spark-playbook.yml' under the area: '-name:Preparing cloudmesh- setting default user', the entry with < > should be customized as per user credentials: 

     - name: Preparing cloudmesh- setting default user
       become_user: "{{ lookup('env','USER') }}"
       shell: cm default user=<chameleon/jetstream user>


4. Run the following command to deploy hadoop/spark cluster which will run the hadoop-spark-playbook.yml. It will again upgrade cloudmesh client, so that we are up to date with any changes:

       ansible-playbook  hadoop-spark-playbook.yml --ask-sudo-pass -vvvv

5. Type the following to display the machine belong to you. :

      'cm vm list | < username>' 

   The machines with the least numerical index is the master node for spark cluster

6. Copy the python code and input file to the master node:
 
   edit the file 'copy-files-remotely.yml' with entry of master node for spark cluster:

	---
	 - hosts: remotehosts
	   tasks:
	     - name: Transfer file from local to remote master node
	       synchronize:
		 src: <source file name with absolute directory path>
		 dest: /home/hadoop/
		 mode: push
	       delegate_to: 127.0.0.1  


7. Run the 'copy-files-remotely.yml' ansible-playbook:

        ansible-playbook copy-files-remotely.yml --ask-sudo-pass -vvvv

Now your spark cluster is ready for analysis


 








