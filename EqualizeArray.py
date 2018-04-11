# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:17:44 2017

@author: C5232886
"""

#import sys
#
#
#n = int(input().strip())
#c = [int(num) for num in input().strip().split(' ')]
#
#countsdict = dict((x,c.count(x)) for x in set(c))
#
##if len(countsdict) == 1:
##    print(1)
##else:
#print(len(c)-max(countsdict.keys()))

n = int(input().strip())
c = list(map(int, input().split()))

print ( n - max( [ c.count(t)  for t  in set(c) ]) )