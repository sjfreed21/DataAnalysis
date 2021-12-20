#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:38:45 2020

@author: zhwa2432
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# import matplotlib as mpl

#x,y,temp = np.loadtxt('data.txt').T #Transposed for easier unpacking
#nrows, ncols = 100, 100
#grid = temp.reshape((nrows, ncols))
grid=np.empty([100,100])
x=np.arange(0,100,1)
y=np.arange(1,201,2)

for i in x:
    for j in x:
        grid[i,j]=i+j
       
print(len(x),len(y),grid.shape)
'''
plt.imshow(grid, extent=(x.min(), x.max(), y.max(), y.min()),
           interpolation='nearest', cmap=cm.gist_rainbow)

plt.show()
Syntax: matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, shape=, filternorm=1, filterrad=4.0, imlim=, resample=None, url=None, \*, data=None, \*\*kwargs)

Parameters: This method accept the following parameters that are described below:

X: This parameter is the data of the image.
cmap : This parameter is a colormap instance or registered colormap name.
norm : This parameter is the Normalize instance scales the data values to the canonical colormap range [0, 1] for mapping to colors
vmin, vmax : These parameter are optional in nature and they are colorbar range.
alpha : This parameter is a intensity of the color.
aspect : This parameter is used to controls the aspect ratio of the axes.
interpolation : This parameter is the interpolation method which used to display an image.
origin : This parameter is used to place the [0, 0] index of the array in the upper left or lower left corner of the axes.
resample : This parameter is the method which is used for resembling.
extent : This parameter is the bounding box in data coordinates.
filternorm : This parameter is used for the antigrain image resize filter.
filterrad : This parameter is the filter radius for filters that have a radius parameter.
url : This parameter sets the url of the created AxesImage.
'''
fig, ax = plt.subplots()

img=ax.imshow(grid[:, :],extent=(x.min(), x.max(), y.min(), y.max()),
           interpolation='nearest', cmap=cm.gist_earth,aspect=0.5,origin ='lower')
ax.set_title("Test")
ax.set_xlabel('x',size=20)
ax.set_ylabel('y',size=20)
cbar=fig.colorbar(img, ax=ax,label='test',spacing='proportional') # we have to pass the current plot as an argument thus have to set it as a variable
#cbar.set_label('# of contacts', rotation=270)

#%% Lab Task
# import urllib
outdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 2/dat/'
 
t2 = np.empty([149,365])
r2 = np.empty([149,365])
hN = np.arange(100, 15000, 100)
mon=['01','02','03','04','05','06','07','08','09','10','11','12']

# days=['31','28','31','30','31','30','31','31','30','31','30','31']
# for i in range(12):
#     print(i)
#     url = 'http://weather.uwyo.edu/cgi-bin/sounding?region=np&'\
#     +'TYPE=TEXT%3ALIST&YEAR=2019&MONTH='+mon[i]+'&FROM=0100&TO='+days[i]+'12&STNM=72403'
#     urllib.request.urlretrieve(url, outdir + 'Sonde_'+mon[i]+'.txt')
    
for i in [1]:
    f = open(outdir + 'Sonde_' + '01' + '.txt', 'r')
    l = f.readlines()
    temp = []
    rh = []
    rtemp = []
    num = 0
    for j in l:
        if '</PRE>' in j:
            rtemp.append(l.index(j))
            if len(rtemp) >= 2:
                end = min(rtemp) + 1
                print(end)
                rtemp = []
        items = j.split()
        num += 1
        if 'at' in items:
            at = items.index('at')
            # print(items)
            if items[at + 1][-1] == 'Z':
                time = items[at + 1][0:2]
                date = items[at+2]
                print(time,  items[at+3], date, num, end)
            
            
# interp(h, t, ), T_n = f(H_n), T_2[:,idays] = T_n