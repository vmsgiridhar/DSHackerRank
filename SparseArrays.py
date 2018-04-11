# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:35:23 2018

@author: C5232886
"""

n = int(input().strip())

#a = list([i for i in input().strip()])

b = []

for i in range(n):
    b.append(input().strip())
    
n1 = int(input().strip())

for i in range(n1):
    ele = input().strip()
    print(b.count(ele))


