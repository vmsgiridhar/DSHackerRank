# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:19:45 2017

@author: C5232886
"""

#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

numSameChars = min(len(s), len(t))
for i in range(len(t)):
    if s[:i] != t[:i]:
        numSameChars = i-1
        break

diff = len(s)-numSameChars + len(t)-numSameChars
print('Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No')