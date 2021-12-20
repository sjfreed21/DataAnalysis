# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:07:49 2021

@author: sjfre
"""

i = int(input("Income = "))
c = int(input("Cost = "))
if c > i:
    print("Loss = ", c - i)
else:
    print("Profit = ", i - c)