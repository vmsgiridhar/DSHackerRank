# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:56:32 2017

@author: C5232886
"""
#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    # If n is even and p is odd and less then subtract p from n
    # From front
    return(min(p//2, n//2 - p//2))
    # From back
    
    
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
