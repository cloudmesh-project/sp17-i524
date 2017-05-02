from __future__ import print_function
import glob
import yaml
from pprint import pprint
import sys
import re
import os

makes = glob.glob("S*/report/Makefile")

os.system("echo > ~/all.log ")    
for make in makes:
    d = make.replace("/Makefile", "")
    print (70 * "=")
    print (d)
    os.system("cd " + d + "; rm report.pdf >> ~/all.log ")    
    os.system("cd " + d + "; make clean >> ~/all.log")
    os.system("cd " + d + "; make >> ~/all.log")
    print (70 * "=")

os.system("make all >> ~/all.log")
