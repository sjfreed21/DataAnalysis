# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:09:18 2021

@author: sjfre
"""

#%% Question 1
import numpy as np
arr = np.array([12,21,99,9,13,21])
for i in range(0,6):
    print(arr[i])
    
arr = np.append(arr, [21,9,18])
print(arr)

arr = np.flip(arr)
print(arr)

#%% Question 2
file = open('Lorem.txt','a')
file.write("\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
file.close()

file = open('Lorem.txt','r')
print(file.read())

#%% Question 3
file = open('Lorem.txt','r')
txt = file.read()
txt = txt.strip()
tArr = txt.split(' ')
maxLen = len(tArr[0])
word = tArr[0]
for i in tArr:
    if len(i) > maxLen:
        maxLen = len(i)
        word = i
        
print("Longest word is:", word, "with a length of", maxLen)

#%% Question 4
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in alpha:
    file = open(i + '.txt', 'x')
    file.close()
    
#%% Question 5
import time

def hour(inH, outH):
    if inH < outH:
        return (outH - inH, False)
    else:
        return (outH - inH + 24, True)
    
e = time.strptime(input('Enter entrance time in format MM/DD/YYYY HH:MM: '), '%m/%d/%Y %H:%M')
t = time.localtime()
print('Entrance time:', e.tm_mon,'/', e.tm_mday, '/', e.tm_year, e.tm_hour,':', e.tm_min)
print('Exit time:', t.tm_mon,'/', t.tm_mday, '/', t.tm_year, t.tm_hour,':', t.tm_min)
tDays = t.tm_yday - e.tm_yday
tHours, over =  hour(e.tm_hour, t.tm_hour)
if over:
    tDays -= 1
print('Total time:', tDays, 'days,', tHours, 'hours.')
cost = 0
l = input('Lost ticket? (y/n): ')
if l == 'y':
    cost += 17
    print('\nLost ticket fee $17')
else:
    print()
    
if tDays > 2:
    cost += tDays * 18
    print(tDays, '* $18/day')
    if tHours < 6:
        cost += tHours * 3
        print(tHours, '* $3/hour')
    else:
        cost += 18
        print('Daily max of $18 for 6+ hours')
else:
    cost += tDays * 24
    print(tDays, '* $24/day')
    if tHours < 8:
        cost += tHours * 3
        print(tHours, '* $3/hour')
    else:
        cost += 24
        print('Daily max of $24 for 8+ hours')
 
if tDays > 13:
    cost *= 0.9
    print('+ 10% discount')

print('Total: $'+str(cost))
