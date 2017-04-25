README
========
 
This Ansible Galaxy project installs and runs a chemistry research
application on one or more virtual machines in the Chameleon Cloud

License Information
================
Please see LICENSE

How to use
================

Run Benchmark for 1-3 virtual machines
```
$ make benchmark 
```

Run Benchmark for 1-$num_nodes nodes
```
$ make benchmark num_nodes=4
```

Deploy Hadoop Cluster
```
$ make deploy
```

Install Required Software
```
$ make install
```

Run Serial, OpenMP and Hadoop CDMS Applications
```
$ make run
```

View Output Results
```
$ make view
```

Delete virtual cluster
```
$ make delete
```

Remove local output files
```
$ make clean
```
