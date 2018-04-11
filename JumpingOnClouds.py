# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:58:52 2017

@author: C5232886
"""

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
E = 100
for _ in range(0, n, k):
    E = E - 1 #Basic jump cost
    step = (_+k)%n
    if _ == n:
        _ = 0
    if c[step] == 1:
        E = E - 2
print(E)
print(step)
    

#
#n, k  = map(int, input().strip().split())
#clouds = list(map(int, input().strip().split()))
#print(100 - sum(1 + 2 * clouds[i] for i in range(0, n, k)))
#