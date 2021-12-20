# -*- coding: utf-8 -*-
"""
Created on Thu Sep 2 17:55:15 2021

@author: sjfre
"""
#%% Question 1
def star(data):
    lst = data.split(' ')
    print(" ".join(lst[0:4]))
    print("\t", " ".join(lst[4:10]))
    print("\t\t", " ".join(lst[10:16]))
    print("\t\t", " ".join(lst[16:22]))
    print(" ".join(lst[22:26]))
    print("\t", " ".join(lst[26:32]))
    
    return

star('Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are')

#%% Question 2
data = input("Input comma-separated values here: ")
l = list(data.split(','))
t = tuple(l)
print(l, t)

#%% Question 3
file = input("Filename: ")
print(file.split('.')[-1], "\n")

#%% Question 4
def inside(val, group):
    for i in group:
        if i == val:
            return True
    return False

print(inside(1, [1,2,3]))
print(inside(4, [1,2,3]))
print(inside(1, (1,2,3)))
print(inside(4, (1,2,3)))
print(inside(1, {1,2,3}))
print(inside(4, {1,2,3}), "\n")

#%% Question 5

def concat(d1, d2, d3):
    d1.update(d2)
    d1.update(d3)
    return d1

d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}
print(concat(d1,d2,d3), "\n")

#%% Question 6
# --- Taken from Question 4 ---
def inside(val, group):
    for i in group:
        if i == val:
            return True
    return False
# --- Taken from Question 4 ---

def addDict(d1, d2):
    k1 = list(d1.keys())
    k2 = list(d2.keys())
    k3 = list(set(k1 + k2))
    d3 = dict({})
    
    for i in k3:
        # Using inside function from above
        if inside(i, k1) and inside(i, k2):
            d3.update({i: d1[i] + d2[i]})
        elif inside(i, k1) and not inside(i, k2):
            d3.update({i: d1[i]})
        else:
            d3.update({i: d2[i]})
    return d3

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(addDict(d1,d2), "\n")

#%% Question 7
def myMax(data):
    maxVal = data[0]
    for i in data:
        if i > maxVal:
            maxVal = i
    return maxVal

def myMin(data):
    minVal = data[0]
    for i in data:
        if i < minVal:
            minVal = i
    return minVal

def myMean(data):
    sum = 0
    for i in data:
        sum += i
    return sum/len(data)

def myMed(data):
    while len(data) > 2:
        data.pop(0)
        data.pop(-1)
        print(data)
    if len(data) == 1:
        return data[0]
    else:
        return (data[0] + data[1])/2

def myDev(data):
    mean = myMean(data)
    var = 0
    for i in data:
        var += (i - mean)**2
    var /= (len(data))
    return var**0.5

#%% Question 8
# --- From text_read.py ---
import re
test_txt = open("C:/Users/sjfre/Documents/DataAnalysis/Homework/climate.txt").read().lower()
words = re.findall(r"\b[\w-]+\b", test_txt)
print("The test file contains " + str(len(words)))
# --- From text_read.py ---

wordsDict = {words[i] : 0 for i in range(len(words))}

for i in words:
    wordsDict[i] += 1

sort = sorted(wordsDict.items(), key=lambda x:x[1])[::-1]

for i in range(10):
    print('Word \'{}\' occured {} times.'.format(sort[i][0], sort[i][1]))

    

    

