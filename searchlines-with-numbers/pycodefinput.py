#!/usr/bin/env python

import fileinput
import sys

for line in fileinput.input("file.txt"):
    if "babat" in line:
        print('Line number is: {0} and string is: {1}'.format(fileinput.lineno(), line).rstrip())
        #sys.stdout.write("-> ")
        #sys.stdout.write(line)
