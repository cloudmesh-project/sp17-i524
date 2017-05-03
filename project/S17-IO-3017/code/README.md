### Setup VM

Following should be done for setting up VM on chameleon or jetsream cloud. It is assumed that user already has the cloud access. Default cloud should have been setup as chameleon or jetstream. While booting the VM, mention pearth as secgroup.

    cm secgroup add pearth http 8081 8081 tcp 0.0.0.0/0
    cm secgroup add ssh http 22 22 tcp 0.0.0.0/0
    cm secgroup upload
    cm vm boot --secgroup pearth
    cm vm ip assign
    cm vm ssh

### Clone the git repository on host system

    git clone https://github.com/cloudmesh/earth.git 

### Change Host IPs

    cd ~/earth/ansible
    vi hosts 

### Confirm VM's Username
Update username in appserver in front of uname. 

    cd ~/earth/ansible/group_vars
    vi appserver 

### Run ansible playbook

    cd ~/earth/ansible
    ansible-playbook -i hosts setup.yml 

### Activate python virtual environment on VM
On the VM change directory to projectearth and activate virtual environment.

    cd ~/projectearth
    source bin/activate

### Start web server
    python server.py
    
### Run application
Open web browser on your local machine

See the application usage
    
    <ip of host VM>:8081/

Download the USGS earthquake data
    
    <ip of host VM>:8081/getdata

See the analysis of magnitude and depth
    
    <ip of host VM>:8081/plotmag

See the analysis of lat long of eqrthquake epicenter

    <ip of host VM>:8081/plotlatlong

