# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:14:15 2018

@author: C5232886
"""

class Node:
    """This is the Node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    """This is the class for the Linked List
    """
    def __init__(self):
        self.headval = None
    
    def traverse(self):
        node_in_present = self.headval
        while node_in_present is not None:
            print(node_in_present.data)
            node_in_present = node_in_present.next
            
    def reverse_print(self):
        curr = self.headval #1
        prev = None
        next_node = None
        while curr is not None: #1
            next_node = curr.next #2
            curr.next = prev #None
            prev = curr #1
            curr = next_node #2
        self.headval = prev #1
    
    def insert_at_beginning(self, newnode):
        presentfirst = self.headval
        self.headval = newnode
        newnode.next = presentfirst
    
    def insert_at_last(self, newnode):
        node_in_present = self.headval
        while node_in_present is not None:
            node_in_present = node_in_present.next
        lastnode = node_in_present
        print(lastnode)
    
    def insert_node_at_pos(self, newnode, pos):
        count = 0
        node_in_present = self.headval
        if pos == 1:
                newnode.next = node_in_present
                self.headval = newnode
                node_in_present = self.headval
        #traverse till inserting position
        while node_in_present is not None:
            count = count + 1
            if count == pos:
                #inserting logic
                prev = node_in_present
                next_node = node_in_present.next
                prev.next = newnode
                newnode.next = next_node
            else:
                node_in_present = node_in_present.next
        
            
            
            
        
        
            
            
        
        
        
    

    