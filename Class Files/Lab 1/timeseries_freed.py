# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 22:17:33 2021

@author: sjfre
"""
#%% Import & Data Setup - MUST RUN
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
import pandas as pd
from datetime import date
from datetime import datetime as dt 
from scipy import interpolate

path='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 1/'
fname='weekly_in_situ_co2_mlo.csv'
data=genfromtxt(path+fname,delimiter=',',skip_header=44)
df=pd.read_csv(path+fname, sep=',',header=44)

#%% Figure 1: Year Data + Linear & Quadratic Fit
CO2=[]
TIME=[]
for i in df.values[:,0]:
    a=date.fromisoformat(i)   
    day2=dt(a.year,a.month,a.day)   
    day0=dt(a.year,1,1)   
    days=day2-day0   
    Fraction_year=(days.days)/365.   
    TIME.append(a.year + Fraction_year)

for i in df.values[:,1]:
    CO2.append(i)
    
plt.plot(TIME, CO2, '-b')

fit = np.polyfit(TIME, CO2, 2, full=True)
lfit = np.polyfit(TIME, CO2, 1, full=True)
pred = np.poly1d(fit[0])
lin = np.poly1d(lfit[0])
plt.plot(TIME, pred(TIME),'-r')
plt.plot(TIME, lin(TIME),'-g')
plt.title("Year Data With Fit")
plt.legend(['Year', 'Quadratic Fit', 'Linear Fit'])

#%% Figure 2: Year Data De-Trended
plt.figure()
co2D = CO2 - pred(TIME)
plt.plot(TIME, co2D, '-r')
plt.title("Year Data, De-Trended")

#%% Figure 3: Fractional Year Cycles + Mean
plt.figure()
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
plt.title("Fractional Year Cycles")
plt.legend(['Fractional Year Values', 'Mean'])

#%% Figure 4: Mean Mapped to Original Years
plt.figure()
inter = interpolate.interp1d(season_bin, mean)
season = inter(TIME_1)
plt.plot(TIME, season, '-g')
plt.title("Mean Mapped to Original Years")

#%% Figure 5: Year Data Offset from Mean
plt.figure()
plt.plot(TIME, co2D - season, 'og')
plt.title("Year Data Relative to Mean")

#%% Stationary Tests
from statsmodels.tsa.stattools import adfuller

print('\nADF stationary test for the original data')
result = adfuller(CO2)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))
    
# With a p-value of 0.9968, the data is 99.68% likely to be non-stationary
# and we cannot reject that there is a unit root.

#%% Histograms
plt.figure()
import seaborn as sns
sns.histplot(data=CO2,  kde=True,bins=50)
plt.xlabel('CO2 Concentration (ppb)',size=25)
plt.ylabel('Density',size=25)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title("CO2 Original",size=20)

plt.figure()
sns.histplot(data=co2D,  kde=True,bins=50)
plt.xlabel('CO2 Concentration (ppb)',size=25)
plt.ylabel('Density',size=25)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title("CO2 De-Trend and De-Season",size=20)

#%% Gaussian Noise
from random import gauss, seed
seed(1)
y1 = []
for i in range(1000):
    value = gauss(0,1)
    y1.append(value)
  
y2 = []
for i in range(10000):
    value = gauss(0,1)
    y2.append(value)

plt.figure()
sns.histplot(data=y1, kde=True,bins=100)
plt.title("1000 Sample")

plt.figure()
sns.histplot(data=y2, kde=True,bins=100)
plt.title("10000 Sample")

#%% FFT of Noise
from scipy.fft import fft
def smooth(y, box_pts):    
    box = np.ones(box_pts)/box_pts    
    y_smooth = np.convolve(y, box, mode='same')    
    return y_smooth

plt.figure()
y2_g = fft(y2)
N_g = len(y2)
T = 1./52
x2_g = np.linspace(0., 1./(2.*T), N_g//2)
plt.loglog(x2_g[1:N_g//2], 2.0/N_g * np.abs(y2_g[1:N_g//2]), '-g')
plt.loglog(x2_g[1:N_g//2], smooth(2.0/N_g * np.abs(y2_g[1:N_g//2]),10), '-r')

#%% Smoothing CO2 Data
plt.figure()
co2D_s = smooth(co2D - season, 110)
plt.plot(TIME, co2D - season, '-y')
plt.plot(TIME, co2D_s, '-r')

#%% FFT of CO2
plt.figure()

yf = fft(co2D - season)
yf_s = fft(co2D_s)
N = len(co2D)
xf = np.linspace(0., 1./(2.*T), N//2)
plt.loglog(x2_g[1:N_g//2], 2.0/N_g * np.abs(y2_g[1:N_g//2]), '-g')
plt.loglog(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), '-b')
plt.loglog(xf[1:N//2], 2.0/N * np.abs(yf_s[1:N//2]), '-r')
plt.title("FFT Comparison of Noise Levels")
plt.xlabel("1/Year Frequency")
plt.ylabel("Power")
plt.legend(['Random Gaussian distribution','De-trended/seasoned CO2', 'Smoothed De-trended/seasoned CO2'])
