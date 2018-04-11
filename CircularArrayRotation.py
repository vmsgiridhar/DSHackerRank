# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:07:11 2017

@author: C5232886
"""

#!/bin/python3

import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for rep in range(k):
    temp = a[-1]
    for inrep in range(len(a)-1,-1, -1):
        a[inrep] = a[inrep - 1]
    a[inrep] = temp
        
for a0 in range(q):
    m = int(input().strip())
    print(a[m])
###############################################################
# mod method
###############################################################

ls = [int(x) for x in input().split()]
n = ls[0]
k = ls[1]
queries = ls[2]
array = [int(x) for x in input().split()]
result = []
for q in range(queries):
    q = int(input())
    result.append(array[q-k % n])
for e in result:
    print(e)
        
            