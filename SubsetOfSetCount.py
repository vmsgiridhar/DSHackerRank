# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 19:08:15 2017

@author: C5232886
"""


n,k = input().strip().split(' ')
n,k = [int(n), int(k)]
arr = [int(arr_element) for arr_element in input().strip().split(' ')]
count = 0
ini = arr[0]
arr2=[]
for i in range(1,len(arr),1):
    pre = arr[i]
    if ((ini+pre)%k == 0):
            arr2.append(pre)
print(len(arr) - len(arr2))
    
    