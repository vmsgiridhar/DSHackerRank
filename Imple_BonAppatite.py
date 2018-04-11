# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 21:57:08 2017

@author: C5232886
"""

#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this 
    ar.pop(k)
    if (sum(ar)//2 == b):
        return("Bon Appetit")
    else:
        return(b - (sum(ar)//2))
    

n, k = input().strip().split(' ') #Reading as string
print ("n:",n , "k:",k)
n, k = [int(n), int(k)] #Convert to numbers
print ("n:",n , "k:",k)
ar = list(map(int, input().strip().split(' '))) #Reading as arrays
print(ar)
b = int(input().strip()) # Reading the next number
print(b)
result = bonAppetit(n, k, b, ar)
print(result)
