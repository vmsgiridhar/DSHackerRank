# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:41:38 2017

@author: C5232886
"""

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ') 
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')] 
    
    stud = 0
    for _ in a:
        if _ <= 0:
            stud = stud + 1
    print('NO' if k <= stud else 'YES')