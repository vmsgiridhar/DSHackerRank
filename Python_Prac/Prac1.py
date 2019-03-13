# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 18:10:37 2018

@author: C5232886
"""


class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def printmul(self):
        print( self.a * self.b)
obj = A(10,15)
print(obj.printmul())
        