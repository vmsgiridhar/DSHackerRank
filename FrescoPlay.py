## -*- coding: utf-8 -*-
#"""
#Created on Sun Jan  7 15:57:40 2018
#
#@author: C5232886
#"""
#
#s = 'tata consultancy services limited'
##count = 0
##i = 0
##vowels = ['a', 'e', 'i', 'o', 'u']
##while (s[i] in vowels and i < len(s)):
##    count = count + 1
##    i = i + 1
##print(count,i)
#
#vowels = ['a', 'e', 'i', 'o', 'u']
#
#str = "tata consultancy services limited"
#
#print(sum([str.count(elem) for elem in vowels]))


#!/bin/python3

import sys

def leftRotation(a, d):
    # Complete this function
    return a[d:] + a[:d]

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))


