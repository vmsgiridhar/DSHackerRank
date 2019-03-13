# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:40:52 2018

@author: C5232886
"""
import sys
from array import *

#read the string as array characters

def processor():
    strEntered = input("Enter the String:")
    for i in strEntered:
        if strEntered.count(i) > 1:
            return 1
if __name__ == '__main__':
    a = processor()
    if a == 1:
        print("Not Unique")
    else:
        print("Unique")
    