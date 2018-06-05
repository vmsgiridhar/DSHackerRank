# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:38:34 2018

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
    def i_th_fromlast(self,n):
        cur = self
        follow = self
        for i in range(0,n):
            cur = cur.next
        #At this moment cur moves i places ahead of follow
        while cur.next != None:
            cur = cur.next
            follow = follow.next
        return follow
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
ret = node_1.i_th_fromlast(2)
print('The value is:',ret.val)