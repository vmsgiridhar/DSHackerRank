<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:01:50 2018

@author: C5232886
"""

# Creating a single linked list datastructure using python
# Node is the building block of a linked list. It represents elements in the linked list
class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    # setter function
    def setData(self,val):
        self.data = val
    # getter function
    def getData(self):
        return self.data
    # setter function
    def setNextNode(self, val):
        self.nextNode = val
    # getter function
    def getNextNode(self):
        return self.nextNode

class LinkedList:
    def __init__(self,head = None):
       self.head = head
       self.size = 0
    # getter function
    def getSize(self):
       return self.size
    # function for adding a node
    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True
    def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()
    def findNode(self,val):
        curr = self.head
        while curr:
            if curr.getData() == val:
                return True
            curr = curr.getNextNode()
        return False
    def removeNode(self,value):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True
            prev = curr
            curr = curr.getNextNode()
        return False
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:01:50 2018

@author: C5232886
"""

# Creating a single linked list datastructure using python
# Node is the building block of a linked list. It represents elements in the linked list
class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    # setter function
    def setData(self,val):
        self.data = val
    # getter function
    def getData(self):
        return self.data
    # setter function
    def setNextNode(self, val):
        self.nextNode = val
    # getter function
    def getNextNode(self):
        return self.nextNode

class LinkedList:
    def __init__(self,head = None):
       self.head = head
       self.size = 0
    # getter function
    def getSize(self):
       return self.size
    # function for adding a node
    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True
    def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()
    def findNode(self,val):
        curr = self.head
        while curr:
            if curr.getData() == val:
                return True
            curr = curr.getNextNode()
        return False
    def removeNode(self,value):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True
            prev = curr
            curr = curr.getNextNode()
        return False
>>>>>>> 8c3007786dc1f3bcd56e76272543c37edc7394a0
                