# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 13:09:15 2017

@author: C5232886
"""

#!/bin/python3

for _ in range(int(input().strip())):
    a,b,c = map(int, input().strip().split(' '))
    dist_a = abs(c - a)
    dist_b = abs(c - b)
    print('Cat A' if dist_a < dist_b else 'Cat B' if dist_a > dist_b else 'Mouse C')