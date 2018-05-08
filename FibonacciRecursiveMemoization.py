# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:14:15 2018

@author: C5232886
"""

#Fibonacci Recursive
n = int(input('Enter N (Recursive Call):'))
def fib_Recursive(n):
    global callsRecursive
    callsRecursive +=1
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return(fib_Recursive(n-1)+fib_Recursive(n-2))
#print(fib_Recursive(n))
callsRecursive = 0
print(n, ' th Fibonacci Number is ', fib_Recursive(n), ' and calls are: ', callsRecursive)
#End of Fibonacci Recursive

#Fibonacci Memoization
n = int(input('Enter N (Memoization):'))
def FibonacciMemoization(n, src):
    global callsMemoization
    callsMemoization += 1
    if n not in src:
        src[n] = FibonacciMemoization(n - 1, src) + FibonacciMemoization(n - 2, src)
    return src[n]

src = {1:0, 2:1}
callsMemoization = 0  
print(n, ' th Fibonacci Number is ', FibonacciMemoization(n, src), ' and calls are: ', callsMemoization)
#End of Memoization  


    
