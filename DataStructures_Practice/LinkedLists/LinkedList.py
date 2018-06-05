# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:24:07 2018

@author: C5232886
"""

#A class for Node 
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None #Pointer points to nothing initially
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
    def removeduplicates(self):
        val = [] #to store values while traversing
        temp = None
        node = self
        while node != None:
            if node.val in val: #the existing value is duplicate
                temp.next = node.next
            else:
                val.append(node.val)
            temp = node
            node = node.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3 
#1 -> 2-> 3 -> Null

#Traversing a node
node1.traverse()

#Removing duplicates from a Linked list
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(1)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_1.removeduplicates()

#Get the i th to last element in a linked list
# Best explanation : Youtube video link: https://www.youtube.com/watch?v=i7v1UWlaYrI
# Using two pointers

node__1 = Node(1)
node__2 = Node(2)
node__3 = Node(3)
node__4 = Node(4)
node__1.next = Node(2)
node__2.next = Node(3)
node__3.next = Node(4)


