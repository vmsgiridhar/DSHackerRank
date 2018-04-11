# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:59:56 2017

@author: C5232886
"""

#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0

topic_count = 0

for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)
   
for i in range(0,len(topic),1):
    for j in range(i+1,len(topic),1):
        temp = topic_count
        curcount = (topic[i] and topic[j]).count("1")
        if curcount > temp:
            topic_count = curcount
        