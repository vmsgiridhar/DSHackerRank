# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:46:01 2018

@author: C5232886
"""

#!/bin/python3

import sys
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]

#list = [0 for x in range(n)]
list = [0] * n
    
for a0 in range(m):
    a, b, k = input().strip().split(' ')
    a, b, k = [int(a), int(b), int(k)]
    for i in range(a-1,b):
        list[i] = list[i] + k
print(max(list))




