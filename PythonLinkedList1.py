# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:50:59 2018

@author: C5232886
"""

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)