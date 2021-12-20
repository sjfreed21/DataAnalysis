# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:12:07 2021

@author: sjfre
"""
import numpy as np
#%% Question 1
def zeroCheck(arr):
    for i in np.nditer(arr):
        if i:
            return True
    return False

#%% Question 2
thirtySeventy = np.array(range(30,72,2))

#%% Question 3
check = np.zeros((8,8))
for i in range(8):
    for j in range(8):
        if not i % 2:
            if not j % 2:
                check[i][j] = 1
        else:
            if j % 2:
                check[i][j] = 1
   
print(check)
#%% Question 4
arr1 = np.array([0,10,20,40,60,80])
arr2 = np.array([10,30,40,50,70])

# Not sure if this counts since it's a NumPy function, but the directions
# say to "write a NumPy program" so I think it's good!
union = np.union1d(arr1, arr2)
print(union)

#%% Question 5
# A)
data = np.loadtxt('sunspot.long.data.txt', skiprows=1, max_rows=271)

# B)
import matplotlib.pyplot as plt
x = np.linspace(1749,2019,(2020-1749)*12)
    
y = list(np.delete(data,0,1).flat)
plt.plot(x,y)
plt.ylim(0)
plt.title('Sunspot Cycle 1749-2019')
plt.xlabel('Year')
plt.ylabel('# of Sunspots')
plt.show()

# C)
from scipy.fft import fft
plt.semilogy(fft(y))
plt.ylim(100)
plt.title('Fourier Analysis of Sunspot Cycle')
plt.xlabel('Freq (Hz)')
plt.ylabel('Amplitude')

#%% Question 6
class Robot:
 
    def __init__(self, name=None, build_year=None):
        self.name = name
        # a)
        self.build_year = build_year
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        # b)
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("I don't know when I was built!")
            
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    # a)
    def set_year(self, year):
        self.build_year = year
    
    def get_year(self):
        return self.build_year
    
x = Robot()
x.set_name("Henry")
x.say_hi()
x.set_year(2021)
x.say_hi()
y = Robot()
y.set_name(x.get_name() + "2")
y.set_year(x.get_year() + 2)
print(y.get_name())
print(y.get_year())
