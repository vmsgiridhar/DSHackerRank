# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:05:06 2018

@author: C5232886
"""

def powerAB(a,b):
    global calls
    calls += 1
    print('Called: ', calls)
    if(b < 0):
        return 0
    elif(b == 1):
        return a
    else:
        return a * powerAB(a, b-1)
calls = 0
print(powerAB(5,3))
#TimeComplexity of O(b)

def integerDivision(a,b):
    sum = 5
    count = 0
    while(sum <=a):
        sum += b
        count +=1
    return count
print(integerDivision(10,5))

#!/usr/bin/python3

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (' Arg 1 is ',arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )


def show():
    global b
    b = b + 10
    print(b)
    b = 6
    print(b)

show()
b = 40
print(b)

 #global
    