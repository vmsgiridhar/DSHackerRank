# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:23:12 2017

@author: C5232886
"""

#!/bin/python3

import sys
from collections import Counter
pairs = 0
n = int(input().strip())
#ar = Counter(map(int, input().strip().split(' ')))
#print(ar)
#for i in ar: 
#    pairs += ar[i]//2
#    
#result = pairs
#print(result)

ar = input().strip().split(' ')
print(ar)
pairs = 0

for element in set(ar):
	pairs += ar.count(element) // 2
print(pairs)

# Solution
#from collections import Counter
#input()
#socks, pairs = Counter(map(int,input().strip().split())), 0
#for s in socks: pairs += socks[s]//2
#print(pairs)