#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:06:51 2020

@author: zhwa2432
"""


import re

# we don't care about case sensitivity and therefore use lower:

test_txt = open("C:/Users/sjfre/Documents/DataAnalysis/Homework/climate.txt").read().lower()
# change the path "/Users/zhwa2432/documents/CUB/ATOC4815_programing/' to fit your computer
# test_txt='This number is the sum of all the words, together with the many words that occur multiple times'

words = re.findall(r"\b[\w-]+\b", test_txt)
print("The test file contains " + str(len(words)))

