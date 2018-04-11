#!/bin/python3

import sys


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here
for a in alice:
    scores.append(a)
    b = list(set(scores))
    b.sort(reverse=True)
    print(b.index(a) + 1)
    b.remove(a)
    
#Another solution

#from bisect import bisect_right
#
#n = int(input())
#scores = sorted(set(map(int,input().split())))
#m = int(input())
#alice = map(int,input().split())
#
## your code goes here
#for i in alice:
#    print(len(scores)-bisect_right(scores,i)+1)