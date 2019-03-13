# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:45:57 2018

@author: C5232886
"""

def f(x):
    return x % 2 == 0 and x % 3 == 0

a = range(20)

print(map(f,a))