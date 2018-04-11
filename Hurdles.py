# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:57:26 2017

@author: C5232886
"""

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
maxh = max(height)
print(maxh - k if maxh > k else 0)