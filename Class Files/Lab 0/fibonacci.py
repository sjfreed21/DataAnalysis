# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:56:24 2021

@author: sjfre
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def ifib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a