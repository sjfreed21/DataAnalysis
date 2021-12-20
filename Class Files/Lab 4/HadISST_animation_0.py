#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:26:51 2020

@author: zhwa2432
"""

import os.path
import sys
from IPython.display import HTML
import matplotlib as mpl
from matplotlib.animation import ArtistAnimation
from datetime import datetime
from siphon.catalog import TDSCatalog
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
#Import for colortables
from metpy.plots import colortables
import numpy as np
import xarray as xr

'''
read netcdf
1- SST
'''
wdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 3/'

ds = xr.open_dataset(wdir+'HadISST1_SST_update.nc')#'NOAA_NCDC_ERSST_v3b_SST.nc')
print(ds)

time=ds.time.values
print('\n Data:',time[:])

sst = ds.sst.sel(time='2020-02-16', method='nearest')
print('\n SST:\n',sst)
ds.longitude.values[0]=999
ds.assign_coords(longitude=ds.longitude+180)
print(ds.longitude.values[0])

fig = plt.figure(figsize=(9,6))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()
ax.gridlines()
sst.plot(ax=ax, transform=ccrs.PlateCarree(),
         vmin=2, vmax=30, cbar_kwargs={'shrink': 0.5})

plt.show()
'''
sst.plot(vmin=2, vmax=30,levels=8)
plt.show()
sst.plot(levels=[0,5,8,10,15,20,25,30])
plt.show()
'''
#proj = dat.metpy.cartopy_crs

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
#im = ax.imshow(sst[0,:,:],vmin=2, vmax=30,transform=ccrs.PlateCarree())
im = ax.imshow(ds.sst[3,:,:],vmin=2, vmax=30,transform=ccrs.PlateCarree())

plt.show()


imon=[0,1,2,3,4]
ims = []
for i in imon:
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
    im = ax.imshow(ds.sst[i,:,:],vmin=2, vmax=30,transform=ccrs.PlateCarree())
    ims.append([im])
    # plt.show()

ani = animation.ArtistAnimation(fig, ims, interval=1000, blit=True,
                                repeat_delay=1000)
ani.save("HadISST_animation_0.gif")