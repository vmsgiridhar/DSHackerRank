# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:30:03 2018

@author: C5232886
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
    def deleteAnode(self, value):  
        # traversal and deletion
        node = self
        prev = None
        while node != None:
            # start travesal
            if node.val == value:
                # logic for skip of a node
                if prev:
                    prev.next = node.next
                else:
                    node = node.next
                return True # user prompt
            prev = node
            node = node.next
        return False # user prompt
    def printInReverse(self):
        node = self
        prev = None
        next_ = None
        c = 0
        while node != None:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
# Linked List is like: 1 -> 2 -> 0 -> 3
