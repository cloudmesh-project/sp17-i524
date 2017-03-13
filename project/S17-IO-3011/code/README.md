README
========
 
This Ansible Galaxy project installs and runs a chemistry research
application on one or more VM's in the Chameleon Cloud

License Information
================
Please see LICENSE.txt

How to use
================

Configure Default VM Image
```
$ cm default image=Ubuntu-Server-14.04-LTS
```

Configure Default VM Flavor
```
$ cm default flavor=m1.large
```

Run the following command to boot the virtual machine:
```
$ cm vm boot
```

To see all vms just use the command:
```
$ cm vm list
```

To login to the vm you need to have a publicly available (floating)
ip. This can be achieved with the command: ``` $ cm vm ip assign ```

You can after this command has succeed login to the vm with the command:
```
$ cm vm ssh
```

Maybe run the following on VM:
```
sudo dpkg --configure -a
```

Edit inventory with IP's of VM's:
```
$ emacs inventory
```

Run ansible playbook:
```
$ ansible-playbook -i inventory playbook.yml
```

Maybe Connect to IU VPN
```
https://vt4help.service-now.com/kb_view_customer.do?sysparm_article=KB0010740#linux
```
Maybe Install Git
```
sudo apt-get install git
```
git clone git://git.infradead.org/users/dwmw2/openconnect.git


sudo apt-get install autotools-dev
sudo apt-get install automake
sudo apt-get install libtool
sudo apt-get install libxml2-dev
sudo apt-get install libssl-dev
sudo apt-get install pkg-config

wget http://http.debian.net/debian/pool/main/o/openconnect/openconnect_7.08.orig.tar.gz
tar -xvzf openconnect_7.08.orig.tar.gz
cd openconnect-7.08
wget http://git.infradead.org/users/dwmw2/vpnc-scripts.git/blob_plain/HEAD:/vpnc-script
sudo chmod 755 vpnc-script
sudo mkdir /etc/vpnc
sudo mv vpnc-script /etc/vpnc/
./configure --disable-nls
make 
sudo make install

sudo /home/cc/openconnect-7.08/openconnect -u scmcclar --cafile /etc/ssl/certs/ca-certificates.crt --juniper https://vpn.iu.edu


scp ansible/roles/scottmcclary1.intel/files/USE_SERVER.lic cc@129.114.33.156:
