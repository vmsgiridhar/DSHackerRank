# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:58:14 2017

@author: C5232886
"""
import math
entries = int(input().strip())


for i in range(entries):
    a,b = input().strip().split(' ')
    a,b = [int(a), int(b)]
    count = 0
    for j in range(1,int(math.sqrt(b))+1,1):
        if j*j in range(a,b+1):
            count = count + 1
    print(count)
#25**(1/2) will also give the square root needed        