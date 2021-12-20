#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:13:13 2020

@author: zhwa2432
"""


'''
Xarray Integration
Cartopy transforms can be passed to xarray! This creates a very quick path for creating professional looking maps from netCDF data.
http://gallery.pangeo.io/repos/pangeo-data/pangeo-tutorial-gallery/xarray.html

'''
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
warnings.filterwarnings("ignore", category=DeprecationWarning)

# creating a DataArray

data = np.random.rand(4, 3)
locs = ["IA", "IL", "IN"]
times = pd.date_range("2000-01-01", periods=4)
foo = xr.DataArray(data, coords=[times, locs], dims=["time", "space"])
foo
#DataArray properties
print('\nvalues:\n',foo.values)
print('\ncoords:\n',foo.coords)
print('\nattrs:\n',foo.attrs)
# fill in some of that missing metadata
foo.name = "foo-name"
foo.attrs["units"] = "meters"
print(foo.attrs)

#%%
# Creat a dataset
temp = 15 + 8 * np.random.randn(2, 2, 3)
precip = 10 * np.random.rand(2, 2, 3)
lon = [[-99.83, -99.32], [-99.79, -99.23]]
lat = [[42.25, 42.21], [42.63, 42.59]]

# for real use cases, its good practice to supply array attributes such as
# units, but we won't bother here for the sake of brevity
ds = xr.Dataset(
     {
         "temperature": (["x", "y", "time"], temp),
         "precipitation": (["x", "y", "time"], precip),
     },
     coords={
         "lon": (["x", "y"], lon),
         "lat": (["x", "y"], lat),
         "time": pd.date_range("2014-09-06", periods=3),
         "reference_time": pd.Timestamp("2014-09-05"),
     },
 )
ds
# Dataset contents
a="temperature" in ds # checking for presence, not data
print(a)
print('\ndata_vars\n',ds.data_vars)
print('\ndata_coords\n',ds.coords)
print('\ndata_attrs\n',ds.attrs)
ds.attrs["title"] = "example attribute"
print('\ndata_attrs\n',ds.attrs)

#%%
wdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 3/'

ds.to_netcdf(wdir+"saved_on_disk.nc")

#%%
'''
read netcdf
1- SST
'''
ds = xr.open_dataset(wdir+'HadISST1_SST_update.nc')
print(ds)

time=ds.time.values
print('\n Data:',time[0])

sst = ds.sst.sel(time='2020-06-16', method='nearest')
print('\n SST:\n',sst)

fig = plt.figure(figsize=(9,6))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()
ax.gridlines()
sst.plot(ax=ax, transform=ccrs.PlateCarree(),
         vmin=2, vmax=30, cbar_kwargs={'shrink': 0.5})

plt.show()

#%%
sst.plot(vmin=2, vmax=30,levels=8)
plt.show()
sst.plot(levels=[0,5,8,10,15,20,25,30])
plt.show()

#%%
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1, projection = ccrs.Robinson())
im = ax.imshow(ds.sst[1,:,:],vmin = 2, vmax = 30, transform = ccrs.PlateCarree())

plt.show()