# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:30:39 2018

@author: C5232886
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None #Pointer points to nothing initially

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3 