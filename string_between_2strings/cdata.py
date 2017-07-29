#!/usr/bin/env python3.4

import os
import sys
import re
from itertools import islice

reg1 = re.compile('/\w+/COMPANY_NAME/\d+.\d.+\d+/\w+/[a-zA-Z0-9]*.csv')

started = False
collected_lines = []
with open(os.getcwd()+'/logfile_20160324100401.log', "r") as fp:
    for i, line in enumerate(fp.readlines()):
        if line.rstrip() == "===========================================================================": 
            started = True
            f = open(os.getcwd()+'/linecount', 'w')
            f.write(str(i+1)+'\n')
            f.close
            continue
        if started and "ERROR Database error" in line:
            f = open(os.getcwd()+'/linecount', 'a')
            f.write(str(i+1)+'\n')
            f.close
            break

f = open(os.getcwd()+'/linecount', 'r')
fline = f.read()[0:-1].split('\n')[0]
f.seek(0)
lline = f.read()[0:-1].split('\n')[1]
f.close()

with open(os.getcwd()+'/logfile_20160324100401.log') as lines:
    for line in islice(lines, int(fline), int(lline)):
        match1 = reg1.search(line)
        if match1:
            print(match1.group(0))
