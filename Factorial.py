# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:40:05 2017

@author: C5232886
"""

#!/bin/python3

import sys


n = int(input().strip())
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)
#print(factorial(n))
fact = 1
while(n>0):
    fact = fact * n
    n = n - 1
print(fact)
