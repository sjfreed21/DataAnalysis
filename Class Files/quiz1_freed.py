# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:14:56 2021

@author: sjfre
"""

while True:
    num = int(input('Input random integer, or 0 to exit: '))
    if num % 2:
        print('Odd number!')
    elif not num:
        print('Exit')
        break
    else:
        print('Even number!')