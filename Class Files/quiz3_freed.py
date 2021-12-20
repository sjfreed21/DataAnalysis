# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:50:27 2021

@author: sjfre
"""

#%% Question 1
import urllib

t1 = []
t2= []
n1 = 0
n2 = 0

'''
Retrieving Data from 10/01/2021 and 10/02/2021
# n1 and t1 are for 10/01 alone, n2 and t2 are for the two-day series
'''
lines = urllib.request.urlopen("https://sundowner.colorado.edu/weather/atoc8/wxobs20211002.txt").readlines()
for l in lines[3:]:
    n2 += 1
    print(str(n2) + ":", l[0:22].decode())
    t2.append(float(l[18:22].decode()))
    if l[3:5].decode() == '01':
        n1 += 1
        t1.append(float(l[18:22].decode()))
        
#%% Question 2
import matplotlib.pyplot as plt
import numpy as np
''' Graphing One-Day Series '''
y1 = np.linspace(0, 24, n1)
plt.figure(1)
plt.plot(y1, t1)
plt.title("Mean Temperature, 10/01/2021")
plt.xlabel("Hour")
plt.xlim(0, 24)
plt.xticks(np.arange(0, 26, step=2))
plt.ylabel("Temperature, °F")
plt.tight_layout()

#%% Question 3
''' Graphing Two-Day Series '''
y2 = np.linspace(0, 48, n2)
plt.figure(2)
plt.plot(y2, t2)
plt.title("Mean Temperature, 10/01/2021 and 10/02/2021")
plt.xlabel("Hours after 00:00, 10/01")
plt.xlim(0,48)
plt.xticks(np.arange(0, 50, step=2))
plt.axvline(x=24, c='darkgray', ls='--', lw='0.8')
plt.ylabel("Temperature, °F")
plt.tight_layout()

#%% Question 4

ja = []
ju = []
na = 0
nu = 0

'''
Requesting Data for January
jal = lines from January file
na = line counter in January file
ja = list of values for January
'''
jal = urllib.request.urlopen("https://sundowner.colorado.edu/weather/atoc8/wxobs20210121.txt").readlines()
for l in jal[3:]:
    na += 1
    ja.append(float(l[18:22].decode()))

'''
Requesting Data for July
jul = lines from July file
nu = line counter in July file
ju = list of values for July    
'''    
jul = urllib.request.urlopen("https://sundowner.colorado.edu/weather/atoc8/wxobs20210721.txt").readlines()
for l in jul[3:]:
    nu += 1
    ju.append(float(l[18:22].decode()))

'''
As I was writing this code, I wanted to ensure that, in case the data sets
were uneven, the smaller dataset's max would be respected instead of one set
spanning longer than the other. This did not end up being an issue but would
be an important consideration for unequally sized data sets.
'''      
mi = 0
if na <= nu: mi = na
else: mi = nu

''' Graphing Both Data Series '''
y3 = np.linspace(0, 48, mi)
plt.figure(3)
plt.plot(y3, ja, 'b', label='01/20/21 - 01/21/21')
plt.plot(y3, ju, 'r', label='07/20/21 - 07/21/21')
plt.title("Temperature Comparison Across Seasons")
plt.xlabel("Hours after 00:00, XX/20/21")
plt.xlim(0, 48)
plt.xticks(np.arange(0, 50, step=2))
plt.axvline(x=24, c='darkgray', ls='--', lw='0.8')
plt.ylabel("Temperature, °F")
plt.legend()
plt.tight_layout()
