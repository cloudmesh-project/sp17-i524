
Automated deployment of storm cluster using ansible:

    To install cloudmesh client for the first time 'playbook-cloudmesh-first-time-install.yml' with following command(Skip the step if the cloudmesh client is already installed):

     ansible-playbook playbook-cloudmesh-first-time-install.yml --ask-sudo-pass -vvvv

    Update the contents of cloudmesh client configuration file ~/.cloudmesh/cloudmesh.yaml :

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

