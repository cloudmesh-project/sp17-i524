#!/bin/bash

scp $2 cc@$1:/home/cc/

ssh cc@$1 "/home/cc/apache-storm-1.1.0/bin/storm jar /home/cc/$2 $3 $4"

exit 0
