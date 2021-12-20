# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:49:56 2021

@author: sjfre
"""

#%% Question 1
import re
test_txt = open("C:/Users/sjfre/Documents/DataAnalysis/Homework/climate.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", test_txt)

# Find longest words
maxL = len(words[0])
maxS = {words[0]}
for i in words:
    if len(i) > maxL:
        maxS = {i}
        maxL = len(i)
    elif len(i) == maxL:
        maxS.add(i)
        
# Find shortest words
minL = len(words[0])
minS = {words[0]}
for i in words:
    if len(i) < minL:
        minS = {i}
        minL = len(i)
    elif len(i) == minL:
        minS.add(i)
        
print('Longest words:', maxS, 'of length', maxL)
print('Shortest words:', minS, 'of length', minL)
# 's' is from "Earth's", 'a' is a word, 'u' is from 'U.S.', 'i' is from "Hawai'i",
# and 'â' is from a reading error of the copyright symbol. Not sure if these really 
# count as words, but according to the Regex they do, so I think that's fine!


#%% Question 2
# Display linear and log
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1,100,1000)
y1 = 0.2 * np.exp(2 * x)
y2 = 2 + (2 * x) + (x ** 3)

fig, ax = plt.subplots(2,2)
fig.tight_layout()

ax[0, 0].plot(x,y1)
ax[0, 0].set_title('Y1 Linear')

ax[0, 1].loglog(x,y1)
ax[0, 1].set_title('Y1 Log')

ax[1, 0].plot(x,y2)
ax[1, 0].set_title('Y2 Linear')

ax[1, 1].loglog(x,y2)
ax[1, 1].set_title('Y2 Log')
# These plots look right to me, even though the y-scale is so heavily raised
# to powers of 10!