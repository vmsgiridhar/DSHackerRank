# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:22:04 2017

@author: C5232886
"""

n = int(input().strip())
p = [int(listitem) for listitem in input().strip().split(' ')]

for i in range(n):
	 print(p.index(p.index(i+1)+1)+1)
    #Search for i in list
#    y = list.index(i) + 1 # p(y)
#    z = list.index(y) + 1
#    print(z)