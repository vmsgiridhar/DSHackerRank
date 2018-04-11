# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:03:37 2017

@author: C5232886
"""

#!/bin/python3

import sys


#t = int(input().strip())
#for a0 in range(t):
    #n = list(map(int, int(input().strip())))
n = 3

height = 1
#for a0 in range(n):
def spring(h):
    h = h * 2
    return h
def summer(h):
    h = h + 1
    return h
if n % 2 == 0:
        for _ in range(n//2):
            height = spring(height)
            height = summer(height)
else:
    for _ in range(n//2):
        height = spring(height)
        height = summer(height)
    for _ in range(n%2):
        height = spring(height)    
print(height)