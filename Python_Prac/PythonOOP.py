# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:18:49 2018

@author: C5232886
"""

#Common inheritance

#class Parent:
#    def __init__(self):
#        print("Object created")
#    def parentDisplay(self):
#        print("Parent class display function")
#class Child(Parent):
#    #parent is inherited into child
#    def display(self):
#        print("C class display function")
#    def parentDisplay(self):
#        super().parentDisplay()
#        print("C class inherited Parent display function")
#a = Parent()
#b = Parent()
#c = Child()
#c.display()
#super(Child, c).parentDisplay()
#print(Child.__mro__)
#print(issubclass(Child,object))

class A:
    a = 5
    _b = 2
    __c = 4
class B(A):
    pass
def main():
    b = B()
    print(b._A__c)
if __name__ == "__main__":
    main()


