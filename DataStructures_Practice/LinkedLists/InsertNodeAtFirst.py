# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:29:23 2018

@author: C5232886
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
    def insertNodeAtLast(self,valueOfLastNode):
        node = self
        while node != None:
            temp = node
            node = node.next
        newnode = Node(valueOfLastNode)
        temp.next = newnode
    def insertNodeAtFirst(self,nextnode):
        node = self
        node.next = nextnode
        
node0 = Node(0)
node1 = Node(1)
node0.insertNodeAtFirst(node1)
node2 = Node(2)
node1.next = node2