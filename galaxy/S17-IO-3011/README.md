README
========
 
This simple Ansible Galaxy project installs emacs on one or more VM's in the Chameleon Cloud

How to use
================

Configure Default VM Image
```
$ cm default image=Ubuntu-Server-14.04-LTS
```

Configure Default VM Flavor
```
$ cm default flavor=m1.small
```

Run the following command to boot the virtual machine:
```
$ cm vm boot
```

To see all vms just use the command:
```
$ cm vm list
```

To login to the vm you need to have a publicly available (floating) ip. This can be achieved with the command:
```
$ cm vm ip assign
```

Edit inventory with IP's of VM's:
```
$ emacs inventory
```

Run ansible playbook:
```
$ ansible-playbook -i inventory playbook.yml
```

DONE!
