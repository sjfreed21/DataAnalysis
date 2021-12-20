#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:47:23 2020

@author: 
https://github.com/Unidata/python-workshop/blob/master/notebooks/Satellite_Data/PlottingSatelliteData.ipynb

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

# Import for the bonus exercise
from metpy.plots import add_timestamp

mpl.rcParams['animation.embed_limit'] = 50

# List used to store the contents of all frames. Each item in the list is a tuple of
# (image, text)
artists = []
channel = ['Channel13']
case_date = 'current'

# Get the IRMA case study catalog
'''
cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog/casestudies/irma'
                 f'/goes16/Mesoscale-1/Channel{channel:02d}/{case_date:%Y%m%d}/'
                 'catalog.xml')
'''

cat = TDSCatalog('https://thredds.ucar.edu/thredds/catalog/satellite/'
                 'goes/east/grb/ABI/Mesoscale-2/Channel13/current/catalog.xml')

datasets = cat.datasets #.filter_time_range(datetime(2017, 9, 9), datetime(2017, 9, 9, 6))

# Grab the first dataset and make the figure using its projection information
ds = datasets[0]
ds = ds.remote_access(use_xarray=True)
print(ds)
dat = ds.metpy.parse_cf('Rad')
proj = dat.metpy.cartopy_crs

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1, projection=proj)
plt.subplots_adjust(left=0.005, bottom=0.005, right=0.995, top=0.995, wspace=0, hspace=0)
ax.add_feature(cfeature.COASTLINE, linewidth=2)
ax.add_feature(cfeature.BORDERS, linewidth=2)

#wv_norm, wv_cmap = colortables.get_with_range('WVCIMSS_r', 195, 265)
wv_norm, wv_cmap = colortables.get_with_range('WVCIMSS_r', 0, 150)

# Loop over the datasets and make the animation
for ds in datasets[::-60]:
    print(ds)
    # Open the data    ds = ds.remote_access(use_xarray=True)
    ds = ds.remote_access(use_xarray=True)
    dat = ds.metpy.parse_cf('Rad')
    #dat = ds.metpy.parse_cf('Sectorized_CMI')

    x = dat['x']
    y = dat['y']
    #img_data = ds['Sectorized_CMI']
    img_data = ds['Rad']

    im = ax.imshow(dat, extent=(x.min(), x.max(), y.min(), y.max()), origin='upper',
                   cmap=wv_cmap, norm=wv_norm)

    artists.append([im])

# Create the animation--in addition to the required args, we also state that each
# frame should last 200 milliseconds
anim = ArtistAnimation(fig, artists, interval=200., blit=False)
anim.save('GOES_Animation_current.gif')
HTML(anim.to_jshtml())