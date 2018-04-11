# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:26:38 2017

@author: C5232886
"""

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num = n
    count = 0
    for i in range(len(str(n))):
        d = num % 10
        if d!=0 and n % d == 0:
            count = count + 1
        num = num // 10
    print(count)