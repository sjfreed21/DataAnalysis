#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:01:01 2020

In this notebook I give a very simple (and rather uncommented) example of
 how to use scikit-learn to perform an Empirical Orthogonal Function 
 decomposition (EOF analysis, often referred to as well as Principal 
 Component Analysis or PCA) of a climate field, in this case the monthly
 Sea Surface Temperature (SST) anomalies in the Pacific.
http://nicolasfauchereau.github.io/climatecode/posts/eof-analysis-with-scikit-learn/

"""

import pandas as pd
import numpy as np
from numpy import ma
from matplotlib import pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
#Import for colortables
from metpy.plots import colortables

'''
from mpl_toolkits.basemap import Basemap as bm

#
#A small function to plot a 2D field on a map with basemap
#
def plot_field(m, X, lats, lons, vmin, vmax, step, cmap=plt.get_cmap('jet'), \
               ax=False, title=False, grid=False):
    if not ax: 
        f, ax = plt.subplots(figsize=(8, (X.shape[0] / float(X.shape[1])) * 8))
    m.ax = ax
    im = m.contourf(lons, lats, X, np.arange(vmin, vmax+step, step), \
                    latlon=True, cmap=cmap, extend='both', ax=ax)
    m.drawcoastlines()
    if grid: 
        m.drawmeridians(np.arange(0, 360, 30), labels=[0,0,0,1])
        m.drawparallels(np.arange(-80, 80, 20), labels=[1,0,0,0])
    m.colorbar(im)
    if title: 
        ax.set_title(title)
'''
        
'''
load the SST data
'''

wdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 5/'
dset = xr.open_dataset(wdir+'sst.mnmean.v3.nc')

print(dset)
lat = dset['lat'].values
lon = dset['lon'].values
sst = dset['sst'].values
print(lat.shape)
'''
Selects the period 1950 - 2013 and the tropical Pacific domain

'''
dsub = dset.sel(time=slice('1950','2013'), lat=slice(40,-40), lon=slice(120,290))
lat = dsub['lat'].values
lon = dsub['lon'].values
sst = dsub['sst'].values
# need to calculate annomaly here
sst_anom = sst
print(sst_anom[0:10,0,0])
lons, lats = np.meshgrid(lon, lat)
#print(dsub)
print(sst.shape)
dim=sst.shape
#print(len(lat))
#print(sst[:,0,0])
#print(sst[:,0,0].mean())
ilon=len(lon)
ilat=len(lat)
print(ilon,ilat)
print(type(sst))
Mean_season=np.ndarray(shape=(12,41,86),dtype=float)
print(Mean_season.shape)
Mean_season[:,:,:]=np.nan
for i in range(len(lat)):
    for j in range(len(lon)):
        for imon in range(12):
            data=[]
            for iyear in range(64):
                ii=iyear*12+imon
                #
                if np.isnan(sst[ii,i,j]):  
                    continue
                else:
                    data.append(sst[ii,i,j])
                    #print(ii,sst[ii,i,j])
            if len(data) > 0:
                Mean_season[imon,i,j]=sum(data)/len(data)
            
print(Mean_season[0:10,0,0])
print(sst[0:10,0,0])

for i in range(len(lat)):
    for j in range(len(lon)):
        for imon in range(12):
            for iyear in range(64):
                ii=iyear*12+imon
                sst_anom[ii,i,j]=sst[ii,i,j]-Mean_season[imon,i,j]

print(sst_anom[0:10,0,0])
'''
reshape in 2D (time, space)
'''
X = np.reshape(sst, (sst.shape[0], len(lat) * len(lon)), order='F')
np.any(np.isnan(X))

'''
Mask the land points
'''
type(X)
X = ma.masked_array(X, np.isnan(X))
type(X)
land = X.sum(0).mask
ocean = ~ land 

'''
keep only oceanic grid-points
'''
X = X[:,ocean]

'''
Standardize SST using the fit and transform methods of the sklearn.preprocessing.scaler.StandardScaler¶
'''

from sklearn import preprocessing
scaler  = preprocessing.StandardScaler()
scaler_sst = scaler.fit(X)

'''
Once the scaler object has been 'trained' on the data, we can save it as a pickle object
'''
import joblib
joblib.dump(scaler_sst, './scaler_sst.pkl', compress=9)
scaler_sst = joblib.load('./scaler_sst.pkl')

'''
scales: use the transform method of the scaler object¶
'''
X = scaler_sst.transform(X)

'''
verify that mean = 0 and std = 1
'''
print(X.mean())
print(X.std())
X.shape

'''
EOF decomposition
'''
from sklearn.decomposition import PCA
skpca = PCA() #instantiates the PCA object
skpca.fit(X) #fit

'''
Now saves the (fitted) PCA object for reuse in operations¶
'''
joblib.dump(skpca, '../EOF.pkl', compress=9)

f, ax = plt.subplots(figsize=(5,5))
ax.plot(skpca.explained_variance_ratio_[0:10]*100)
ax.plot(skpca.explained_variance_ratio_[0:10]*100,'ro')
ax.set_title("% of variance explained", fontsize=14)
ax.grid()

'''
keep number of PC sufficient to explain 70 % of the original variance
'''
ipc = np.where(skpca.explained_variance_ratio_.cumsum() >= 0.70)[0][0]
print(ipc)

'''
The Principal Components (PCs) are obtained by using the transform method of the pca object (skpca)
'''
PCs = skpca.transform(X)
PCs = PCs[:,:ipc]

'''
The Empirical Orthogonal Functions (EOFs) are contained in the components_ attribute of the pca object (skpca)
'''
EOFs = skpca.components_
#EOFs = EOFs[:ipc,:]
EOFs.shape

'''
we can the reconstruct the 2D fields (maps)
'''
EOF_recons = np.ones((ipc, len(lat) * len(lon))) * -999.
for i in range(ipc): 
    EOF_recons[i,ocean] = EOFs[i,:]
EOF_recons = ma.masked_values(np.reshape(EOF_recons, (ipc, len(lat), len(lon)), order='F'), -999.)
EOF_recons.shape

type(EOF_recons)
EOF_recons *= 100

fig = plt.figure(figsize=(10,8))
central_lon, central_lat = 180, 0
extent=[lons.min(), lons.max(), -40, 40]
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_lon))
ax.coastlines()
ax.gridlines()
ax.set_extent(extent)
im = ax.imshow(EOF_recons[0,:,:],extent=(lons.min(), lons.max(), lats.min(), lats.max())
                   ,vmin=-5, vmax=5,transform=ccrs.PlateCarree(),origin='upper',interpolation='bilinear')
plt.show()


