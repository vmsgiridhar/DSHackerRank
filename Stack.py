# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:06:07 2019

@author: C5232886
"""

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def top(self):
        return self.stack[(len(self.stack)-1)]
    def pop(self):
        if len(self.stack) <= 0:
            return self.stack.pop()
            
    def show(self):
        return self.stack