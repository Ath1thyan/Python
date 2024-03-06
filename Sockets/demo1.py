#!/usr/bin/env python3

# import os
# os.system('sysctl hw.cpufrequency')

import sys

for i in range(100):
    if i%2 == 0:
        print(i, file=sys.stderr)
    else:
        print(i)
# To print the output and error in various files
# python3 demo1.py > pyout.log 2> pyerr.log 
