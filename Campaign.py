# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:48:06 2017

@author: C5232886
"""

n = int(input().strip())
totlikes = 0
m = 5
for _ in range(n):
    #iterate n times
    likes = m // 2
    totlikes = totlikes + likes
    m = likes * 3
print(totlikes)
    