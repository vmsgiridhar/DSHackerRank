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
    def insertNodeAtSpecificPosition(self, pos, newnode):
        i = 0
        node = self #firstnode
        while node != None: #traverse
            i = i + 1
            if i == pos: #insert newnode
                temp = node.next
                node.next = newnode
                newnode.next = temp
            else: #continue traversal
                node = node.next
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node0.next = node1
node1.next = node2

node_1 = Node(5)
node0.insertNodeAtSpecificPosition(2, node_1)
# test with node0.traverse()