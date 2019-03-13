# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:51:52 2019

@author: C5232886
"""

class Queue:
    def __init__(self):
        self.data = []
    def push(self, data):
        self.data.append(data)
        print(self.data)
    def pop(self):
        #FIFO
        if len(self.data) != 0:
            self.data.remove(self.data[0])
        else:
            print('Queue is empty!')