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
