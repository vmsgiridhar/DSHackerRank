# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:38:05 2017

@author: C5232886
"""

#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

pos = 0 # initial position on cloud 0
jump = 0
#while(pos < (n - 1) and pos != (n - 2)):
while(pos < (n - 2)):
    #if c[pos+2] != 1 (pos+2 < n):
    if c[pos + 2] != 1:
            pos = pos + 2
            jump = jump + 1
    else:
        pos = pos + 1
        jump = jump + 1
if pos == (n - 2):
    jump = jump + 1

print(jump)
    