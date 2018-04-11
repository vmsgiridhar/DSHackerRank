# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:53:53 2018

@author: C5232886
"""

# Dynamic array program

n,q = input().strip().split(' ')
[n,q] = [int(n),int(q)]
seqlist = []
reslist = []
lastAnswer = 0
for i in range(n):
    seqlist.append([])
for j in range(q):
    a, b, c = input().strip().split(' ')
    [a,b,c] = [int(a),int(b),int(c)]
    if a == 1:
        seqfind = seqlist[(b^lastAnswer)%n]
        seqfind.append(c)
    elif a == 2:
        seqfind = seqlist[(b^lastAnswer)%n]
        lastAnswer = seqfind[c%len(seqfind)]
        reslist.append(lastAnswer)
for i in range(len(reslist)):
    print(reslist[i])
    