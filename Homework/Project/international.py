# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:18:48 2021

@author: sjfre
"""

#%% Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

#%% Get Data on Press Freedom
# Retrieved from https://rsf.org/en/ranking_table
df = pd.read_csv("data/press.csv")
dicf = df.to_dict()
c1 = dicf["EN_country"].values()
sc = dicf["Score 2020"].values()
pf = dict(zip(c1, sc))

#%% Get Data on Fragility
# Retrieved from https://fragilestatesindex.org/
df = pd.read_excel(io='data/fsi-2021.xlsx')
dicf = df.to_dict()
c2 = dicf["Country"].values()
tot = dicf["Total"].values()
fr = dict(zip(c2, tot))

#%% Secondary Plot: Scatter Plot w/ Trend
combine = {}
for k, v in pf.items():
    if k in fr:
        combine[k] = [float(v.replace(',','.')), round(fr[k],1)]
        
pairs = list(combine.values())
x = list()
y = list()
for i in range(len(pairs)):
    x.append(pairs[i][0])
    y.append(pairs[i][1])
x = np.array(x)
y = np.array(y)

fit = np.polyfit(x, y, 1)
pred = np.poly1d(fit)
R2 = r2_score(y, pred(x))

plt.scatter(x,y)
plt.plot(x, pred(x), 'r', label=str(round(fit[0],3)) + 'x + ' + str(round(fit[1],3)))
plt.xlabel('Press Freedom Score')
plt.ylabel('Fragility Score')
plt.title('Correlation between Press Freedom and Fragility')
plt.legend()
plt.text(65, 20, "R² = " + str(round(R2, 5)), bbox=dict(boxstyle='square', facecolor='white'))