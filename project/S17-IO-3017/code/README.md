### Setup VM

Following should be done for setting up VM on Cloudmesh. It is assumed that cloudmesh client is already setup.

    cm vm secgroup add pearth http 8081 8081 tcp 0.0.0.0/0
    cm vm secgroup add ssh http 22 22 tcp 0.0.0.0/0
    cm vm secgroup upload
    cm vm boot --secgroup pearth
    cm vm ip assign

### Clone or download repository on host system

git clone https://github.com/cloudmesh/cloudmesh.projectearth.git 

### Run ansible playbook
    Go to cloned project directory - cd cloudmesh.projectearth/ansible
    Update cloudmesh.projectearth/ansible/hosts file with IP address of VM
    Run ansible playbook - ansible-playbook -i hosts setup.yml 

### Login to VM
    cm vm ssh
    
### Activate python virtual environment on VM
    Change directory to projectearth
    Run command - source bin/activate

### Start web server
    python server.py
    
### Run application
    - Open web browser on your local machine
    - Type url: <ip of host VM>:8081/getdata
    This downloads the USGS earthquake data
    - Type url: <ip of host VM>:8081/plotmag
    Shows output on web page
    - Type url: <ip of host VM>:8081/plotlatlong
    Shows output on web page
    

    
    
