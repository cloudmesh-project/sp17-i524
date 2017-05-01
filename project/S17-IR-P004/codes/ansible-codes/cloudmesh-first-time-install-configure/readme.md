1. Open the inventory file:
   a. replace the <username> with your preferred localhost username

2. Make sure ansible is installed using the command : <apt-get install ansible>

3. Run the ansible playbook using : 
   
    ansible-playbook -i inventory playbook-cloudmesh-first-time-install.yml -vvvv

4. Run the following command :
       $ cm 
       
       exit out by typing ctrl+c
5. Open the file ~/.cloudmesh/cloudmesh.yml and edit the following entry:

       2.1 Edit the following section,the entry with < > should be customized as per your credentials:

	 profile:
	      firstname: <first name>
	      lastname: <last name>
	      email: <email id>
	      user: <chameleon/jetsream/other cloud username>

       2.2. Change the entry of active cloud to use your preferred cloud,only( perform only for chameleon cloud):
 

        a. only for chameleon cloud:

		 active:
		 - chameleon
		 clouds:
		 ...

		                                       
	 		                                            
        b. only for jetstream cloud:

		 active:
		 - jetstream
		 clouds:
		 ...


        c. for both jetstream and chameleon cloud: 


	         active:
		 - chameleon
                 - jetstream
		 clouds:
		 ...



      2.3.Under the preferred cloud change the following entry, the entry with < > should be customized as per your credentials:

        a. for chameleon:

		 credentials:
		 OS_PASSWORD: <cloud password>
		 OS_TENANT_NAME: CH-818664
		 OS_TENANT_ID: CH-818664
		 OS_PROJECT_NAME: CH-818664
		 OS_USERNAME: <cloud username>
 
        b. for jetstream 
                
                credentials:
		OS_PROJECT_DOMAIN_NAME: tacc
		OS_USER_DOMAIN_NAME: tacc
		OS_PROJECT_NAME: TG-CIE170003
		OS_TENANT_NAME: TG-CIE170003
		OS_USERNAME: <cloud username>
		OS_PASSWORD: <cloud password>
		OS_AUTH_URL: https://jblb.jetstream-cloud.org:35357/v3
		OS_IDENTITY_API_VERSION: 3
		OS_VERSION: kilo




      2.4. (Step only for Chameleon cloud configuration for hadoop/spark deployment) Change the type of OS and flavor you want for hadoop/spark cluster(recommended) under your preferred cloud:

	 default:
	 	flavor: m1.medium
	 	image: CC-Ubuntu14.04

      2.5 (Step only for Jetstream cloud configuration for hadoop/spark deployment) Change the type of OS and flavor you want for hadoop/spark cluster(recommended) under your preferred cloud:
 
	 default:
	 	flavor: m1.small
	 	image: ubuntu-14.04-trusty-server-cloudimg


