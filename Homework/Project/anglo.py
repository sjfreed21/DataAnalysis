# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 01:37:26 2021

@author: sjfre
"""

#%% Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%% Initialize Country Data
us = list(pd.read_csv('data/US.csv').to_dict()["Measure Values"].values())
au = list(pd.read_csv('data/AU.csv').to_dict()["Measure Values"].values())
ca = list(pd.read_csv('data/CA.csv').to_dict()["Measure Values"].values())
nz = list(pd.read_csv('data/NZ.csv').to_dict()["Measure Values"].values())
uk = list(pd.read_csv('data/UK.csv').to_dict()["Measure Values"].values())

#%% US Analysis
x = ['2017', '2018', '2019', '2020', '2021']
assault = [48, 41, 41, 435, 141]
arrest = [39, 13, 9, 142, 57]

x1 = np.arange(len(x))

fig, ax1 = plt.subplots()
ax1.bar(x1 - 0.2, assault, 0.4, label="Assaults")
ax1.bar(x1 + 0.2, arrest, 0.4, label="Arrests")
ax1.set_xticks(x1)
ax1.set_xticklabels(['2017', '2018', '2019', '2020', '2021'])
ax1.set_ylabel("# of Incidents")

ax2 = ax1.twinx()
ax2.plot(us[-5:], 'r-o')
ax2.tick_params(axis='y', labelcolor='r')
ax2.set_ylabel("Fragility Score", color='r')

ax1.set_xlabel("Year")
ax1.set_title("Attacks on Journalists vs Fragility (US)")
ax1.legend(loc='upper left')

#%% Comparison Plot
plt.figure()
x2 = list(range(2006, 2022))
plt.plot(x2, us, label = 'US')
plt.plot(x2, au, label = 'AU')
plt.plot(x2, ca, label = 'CA')
plt.plot(x2, nz, label = 'NZ')
plt.plot(x2, uk, label = 'UK')

plt.xlabel("Year")
plt.ylabel("Fragility Score")
plt.title("Comparison Across the Anglosphere")
plt.legend(bbox_to_anchor=(1,1), loc="upper left")