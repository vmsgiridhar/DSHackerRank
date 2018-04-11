# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:42:44 2017

@author: C5232886
"""

#rl, rh, k = int(input().strip().split(' '))
#count = 0
##rl = str(rl)
#for _ in range(rl, rh+1):
#    rev = 0
#    while(_ > 0):
#        rev = rev %10
#        rev = (rev *10) + rev
#        rev = rev //10
#    if abs(rl - rev)%k == 0:
#        count = (count + 1) 
#print(count)

i, j, k = [int(x) for x in input().split()]
bd = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
print(sum(bd))