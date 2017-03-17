from __future__ import print_function
import glob
import yaml
from pprint import pprint
import sys
import re
import os

dirs = glob.glob("*/report.tex")

for d in dirs:
    directory = d.replace("/report.tex","")
    os.system ("cd " + directory + "; make")

