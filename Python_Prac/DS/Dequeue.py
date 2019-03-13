# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:43:13 2019

@author: C5232886
"""

# Dequeue is double ended queue which support adding and deleting at both ends
class Dequeue:
    def __init__(self):
        self.data = []
    def insert_at_left(self, ele):
        self.data.insert(0,ele)
    def insert_at_right(self,ele):
        self.data.insert(len(self.data) - 1, ele)
    def showdata(self):
        print(self.data)
    def pop_at_left(self):
        if len(self.data) > 0:
            self.data.pop(0)
        else:
            print('Queue is empty!')
    def pop_at_right(self):
        if len(self.data) > 0:
            self.data.pop(len(self.data) - 1)
        else:
            print('Queue is empty!')
        