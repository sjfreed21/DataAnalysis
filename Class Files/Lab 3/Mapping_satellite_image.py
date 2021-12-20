#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:40:13 2020

@author: zhwa2432
"""
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt
'''
Showing Images
We can plot a satellite image easily on a map if we know its extent
'''
fig = plt.figure(figsize=(8, 12))

# this is from the cartopy docs
wdir='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 3/'
fname = 'Miriam.A2012270.2050.2km.jpg'
#https://www.visibleearth.nasa.gov/images/123103/tropical-storm-miriam-13e-off-mexico/123106l

img_extent = (-120.67660000000001, -106.32104523100001, 13.2301484511245, 30.766899999999502)
extent = list(img_extent)
extent[3] += 5
img = plt.imread(wdir+fname)
print(img.shape)
ax = plt.axes(projection=ccrs.Robinson(globe=None))

# set a margin around the data
ax.set_xmargin(0.05)
ax.set_ymargin(0.10)
ax.set_extent(extent)   # Needed when in different projection
# add the image. Because this image was a tif, the "origin" of the image is in the
# upper left corner
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax.coastlines(resolution='50m', color='black', linewidth=1)

# mark a known place to help us geo-locate ourselves
ax.plot(-117.1625, 32.715, 'bo', markersize=7, transform=ccrs.Geodetic())
ax.text(-117, 33, 'San Diego', transform=ccrs.Geodetic())

