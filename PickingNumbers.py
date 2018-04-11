# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:19:27 2017

@author: C5232886
"""

#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(set(a))
maximum=0
for i in a:
    c=a.count(i)
    d=a.count(i-1)
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)

#n,a = input(),list(map(int,input().split()))
#print(max(a.count(x)+a.count(x+1) for x in set(a)))