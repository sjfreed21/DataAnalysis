# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:38:01 2021

@author: sjfre
"""

import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt

#%% Ortho Boulder-centered
central_lon, central_lat = -105, 40
extent = [220, 300, 20, 60]

ax = plt.axes(projection=ccrs.Orthographic(central_lon, central_lat))
ax.gridlines()
ax.coastlines(resolution='50m')
ax.set_extent(extent)
ax.gridlines(draw_labels=True)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.LAKES)
ax.add_feature(cartopy.feature.RIVERS)

ax.plot(central_lon, central_lat, 'bo', markersize=7, transform=ccrs.Geodetic())
ax.text(central_lon+1, central_lat, 'Boulder, CO', transform=ccrs.Geodetic())

#%% Plate Carree Boulder-centered

ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=central_lon))
ax.gridlines()
ax.coastlines(resolution='50m')
ax.set_extent(extent)
ax.gridlines(draw_labels=True)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.LAKES)
ax.add_feature(cartopy.feature.RIVERS)

ax.plot(central_lon, central_lat, 'bo', markersize=7, transform=ccrs.Geodetic())
ax.text(central_lon+1, central_lat, 'Boulder, CO', transform=ccrs.Geodetic())