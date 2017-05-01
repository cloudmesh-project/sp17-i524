#!/bin/bash

DATE="$(date +"%Y.%m.%d_%H.%M.%S")"

#DOWNLOAD DATASET
wget --no-check-certificate -O h1b_m3Rows.csv http://www.icnbm.org/files/h1b_m3Rows.csv
#wget --no-check-certificate -O h1b_m2Rows.csv http://www.icnbm.org/files/h1b_m2Rows.csv
#wget --no-check-certificate -O h1b_m1Rows.csv http://www.icnbm.org/files/h1b_m1Rows.csv
#wget --no-check-certificate -O h1b_DataScienceOnly.csv http://www.icnbm.org/files/h1b_DataScienceOnly.csv



#CREATE IMAGES OR OUTPUT FOLDER
dir='images'

if [ -d "${dir}" ]
  then
     echo "Directory already exist"
     rm -fr ~/images/*
  else
    mkdir -p  "${dir}"
    chmod 770 ~/images
fi

#UPDATE PYTHON MODULES
sudo apt-get -y install python-dev python-setuptools python-numpy python-scipy
sudo apt-get -y install python-matplotlib
sudo apt-get -y install python-numexpr
sudo apt-get -y install python-pip
sudo apt-get -y install python-pandas

#RUN PYTHON JOB
time python ./cc_analyze_data.py >> ~/images/cc_analyze_data.out

