# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:15:04 2017

@author: C5232886
"""

#!/bin/python3

import sys
import string

s = [int(i) for i in input().split()]
w = [s[ord(c)-ord('a')] for c in input()]
print(max(w)*len(w))