# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:08:47 2019

@author: C5232886
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.headval = None
    
    def traverse(self):
        #traversal of the linkedlist
        nodeinpresent = self.headval
        while(nodeinpresent is not None):
            print(nodeinpresent.data)
            prev_node = nodeinpresent
            nodeinpresent = nodeinpresent.next
    def inserting_at_end(self, value):
        newnode = Node(value)
        currentnode = self.headval
        while(currentnode is not None):
            lastnode = currentnode
            currentnode = currentnode.next
        lastnode.next = newnode