# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:46:27 2017

@author: C5232886
"""

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#while(len(arr) > 0):
#    cutlength = min(arr)
#    arr = [int(i - cutlength) for i in arr]
#    list(filter(lambda a: a != 0, arr))
#    print(len(arr))
#    
while(len(arr)):
    print(len(arr))
    arr = [x - min(arr) for x in arr if x - min(arr)>0]    
    