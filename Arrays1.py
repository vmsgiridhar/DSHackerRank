# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 05:45:19 2018

@author: C5232886
"""

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for x in range(len(arr),0,-1):
    print(arr[x-1], end =' ')

print(arr[::-1])