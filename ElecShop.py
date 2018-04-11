# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:52:10 2017

@author: C5232886
"""

#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    list = []
    for i in keyboards:
        for j in drives:
            if (i + j) <= s: 
                list.append(i+j)
    if len(list) == 0: 
        return -1
    else:
        return(max(list))
    

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
