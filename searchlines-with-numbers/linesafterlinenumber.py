#!/bin/env python3

import os

lookup = 'Salam Alekum'

filename = '/root/fileoperations/newfile'

with open(filename) as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            print ('found at line:', num)
            f = open('/root/fileoperations/setirsayi', 'w') 
            f.write(str(num))
            f.close

ssay = '/root/fileoperations/setirsayi'
f = open(ssay)
linenum = int(f.read())
f.close()


with open(filename) as f:
    siyahi = f.readlines()[linenum:]
    for i in siyahi:
        print(i.splitlines())
