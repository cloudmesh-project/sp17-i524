python loader.py \
 -d /mnt/vol/Antelope_data/sampledata \
 -i 192.168.0.30 -p 27017 \
 -t arrival \
 -t assoc \
 -t event \
 -t origin \
 -t site \
 -t sitechan \
 -t snetsta \
 -t wfdisc 
 > /dev/null 2>&1 &
