# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:32:03 2018

@author: C5232886
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None #Pointer points to nothing initially
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3 
#Traversing a node
node1.traverse()
