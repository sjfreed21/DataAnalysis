#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:19:35 2020

@author: zhwa2432
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft 
from numpy import genfromtxt
import pandas as pd
from datetime import date
from datetime import datetime as dt 
import time

path='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 1/'
'''
fname='sunspot.long.data.txt'
file_id= open(path+fname,'r')

y1=1749
y2=2018
n_years=y2-y1+1
x_bin=np.linspace(y1,y2+1,n_years*12)
#xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
D=np.loadtxt(path+fname,max_rows=n_years,skiprows=1,usecols=[1,2,3,4,5,6,7,8,9,10,11,12])
#Syntax: numpy.loadtxt(fname, dtype=’float’, comments=’#’, delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
D.shape=(1,n_years*12)
print(D[:, :10])
print(np.shape(D),n_years,type(D))

years=np.loadtxt(path+fname,max_rows=n_years,skiprows=1,usecols=[0])
print(years)

plt.figure(0)  # start a new window
plt.plot(x_bin,D[0,:], label='Orignial')  # Plot some data on the (implicit) axes.
plt.xlabel('Year',size=18)
plt.ylabel('Sun Spot Numbers',size=15)
plt.title("Simple Plot",size=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(0)

def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction
'''

fname='weekly_in_situ_co2_mlo.csv'
data=genfromtxt(path+fname,delimiter=',',skip_header=44)
print(data)
df=pd.read_csv(path+fname, sep=',',header=44)
CO2=[]
TIME=[]
'''
for i in df.values[:,0]:
    a=date.fromisoformat(i)
    day2=dt(a.year,a.month,a.day)
    #print(i,toYearFraction(day2))
    TIME.append(toYearFraction(day2))
'''
for i in df.values[:,0]:
    a=date.fromisoformat(i)   
    day2=dt(a.year,a.month,a.day)   
    day0=dt(a.year,1,1)   
    days=day2-day0   
    Fraction_year=(days.days)/365.   
    TIME.append(a.year + Fraction_year)

for i in df.values[:,1]:
    CO2.append(i)
    
#print(df.values[1,0])
#print(CO2)
# print(TIME)

plt.plot(TIME, CO2, '-b')
# plt.show()
# plt.figure(0)

'''
print('Temperature')
y1=1880
y2=2018
n_years=y2-y1+1
x_bin=np.linspace(y1,y2+1,n_years*12)
T_fname='GLB.Ts+dSST.txt'
DT=np.loadtxt(path+T_fname,max_rows=n_years,skiprows=13,usecols=[1,2,3,4,5,6,7,8,9,10,11,12])
#Syntax: numpy.loadtxt(fname, dtype=’float’, comments=’#’, delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
DT.shape=(1,n_years*12)
#print(D[:, :10])
print(np.shape(DT),n_years,type(DT))

plt.plot(x_bin,DT[0,:]/100.,'.r', label='Orignial')  # Plot some data on the (implicit) axes.
plt.xlabel('Year',size=18)
plt.ylabel('Temperature Index',size=15)
print(x_bin)
'''

fit = np.polyfit(TIME, CO2, 2, full=True)
lfit = np.polyfit(TIME, CO2, 1, full=True)
pred = np.poly1d(fit[0])
lin = np.poly1d(lfit[0])
plt.plot(TIME, pred(TIME),'-r')
plt.plot(TIME, lin(TIME),'-g')
plt.show()
# print('\n', fit, '\n', lfit)

plt.figure(0)
co2D = CO2 - pred(TIME)
plt.plot(TIME, co2D)

plt.figure(1)
TIME_1=[]
for i in df.values[:,0]:
    a=date.fromisoformat(i)   
    day2=dt(a.year,a.month,a.day)   
    day0=dt(a.year,1,1)   
    days=day2-day0   
    Fraction_year=(days.days)/365. 
    TIME_1.append(Fraction_year)
    
plt.plot(TIME_1, co2D, 'or')

bin_size = 0.02
season_bin = np.arange(0,1.01, bin_size)

mean = []
for i in season_bin:
    res = np.where(np.logical_and(TIME_1 >= i-bin_size/2., TIME_1 <= i+bin_size/2.))
    mean.append(np.mean(co2D[res]))
    
plt.plot(season_bin, mean, '-g')
