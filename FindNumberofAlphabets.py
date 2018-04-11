# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:28:32 2017

@author: C5232886
"""

#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))



###
#It counts the number of "a" in a full string, and in the last, potentially partial string, and calculates the total amount of "a" based on that.
#"a" count of full string * number of string repeats + "a" count of last string.
###