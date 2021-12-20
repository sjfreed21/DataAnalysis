#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:19:56 2020
https://rabernat.github.io/research_computing_2018/maps-with-cartopy.html

https://scitools.org.uk/cartopy/docs/latest/gallery/index.html

https://scitools.org.uk/cartopy/docs/latest/crs/projections.html


Projection-- >  to built a map

transform--> how the data is represented now-- needed to know this 
   to project the data correctly.
   
https://xgcm.readthedocs.io/en/latest/

http://gallery.pangeo.io/repos/pangeo-data/pangeo-tutorial-gallery/xarray.html


@author: zhwa2432
"""
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt

#ccrs.PlateCarree()
'''
Drawing a map
Cartopy optionally depends upon matplotlib, and each projection knows 
how to create a matplotlib Axes (or AxesSubplot) that can represent 
itself.

The Axes that the projection creates is a cartopy.mpl.geoaxes.GeoAxes. 
This Axes subclass overrides some of matplotlib's existing methods, and adds a number of extremely useful ones for drawing maps.
'''
plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

'''
We could just as equally created a matplotlib subplot with one of the many 
approaches that exist. For example, the plt.subplots function could 
be used:
'''
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()

ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
ax.coastlines()

'''
Useful methods of a GeoAxes
The cartopy.mpl.geoaxes.GeoAxes class adds a number of useful methods.

Let's take a look at:

set_global - zoom the map out as much as possible
set_extent - zoom the map to the given bounding box
gridlines - add a graticule (and optionally labels) to the axes
coastlines - add Natural Earth coastlines to the axes
stock_img - add a low-resolution Natural Earth background image to the axes
imshow - add an image (numpy array) to the axes
add_geometries - add a collection of geometries (Shapely) to the axes

'''

# Some More Examples of Different Global Projections

projections = [ccrs.PlateCarree(),
               ccrs.Robinson(),
               ccrs.Mercator(),
               ccrs.Orthographic(),
               ccrs.InterruptedGoodeHomolosine()
              ]


for proj in projections:
    plt.figure()
    ax = plt.axes(projection=proj)
    ax.stock_img()
    ax.coastlines()
    ax.gridlines(draw_labels=True)
    ax.set_title(f'{type(proj)}')

'''
Regional Maps
To create a regional map, we use the set_extent method of GeoAxis to limit the size of the region.
'''
# example 1
# Europe/Atlantic
central_lon, central_lat = -10, 45
extent = [-40, 20, 30, 60]

# SE Asia/Oceania
# central_lon, central_lat = 120, 0
# extent = [80, 160, -30, 30]

#projection=ccrs.Orthographic(central_lon, central_lat)
ax = plt.axes(projection=ccrs.Orthographic(central_lon, central_lat))
ax.gridlines()
ax.coastlines(resolution='50m')
ax.set_extent(extent)
ax.gridlines(draw_labels=True)


# Example 2 
cm = 180 
proj = ccrs.PlateCarree(central_longitude=cm)
fig = plt.figure(figsize=[5, 8])
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines()

maxlon = -60 + cm
minlon = +60 + cm
ax.set_extent([minlon, maxlon, -45, 45], ccrs.PlateCarree())
'''
#If you want to have ordinary geographic longitude labels 
# in the plot above, you can't simply use
#ax.gridlines(draw_labels=True, crs=proj)
'''
ax.gridlines(draw_labels=False, crs=ccrs.PlateCarree(), xlocs=[120,140,160,180,200,220,240])
ax.gridlines(draw_labels=True, crs=ccrs.PlateCarree(), xlocs=[120,140,160,180,-160,-140,-120])


plt.show()


'''
Adding Features to the Map
To give our map more styles and details, we add cartopy.feature objects. Many useful features are built in. These "default features" are at coarse (110m) resolution.

cartopy.feature.BORDERS	Country boundaries
cartopy.feature.COASTLINE	Coastline, including major islands
cartopy.feature.LAKES	Natural and artificial lakes
cartopy.feature.LAND	Land polygons, including major islands
cartopy.feature.OCEAN	Ocean polygons
cartopy.feature.RIVERS	Single-line drainages, including lake centerlines
cartopy.feature.STATES	(limited to the United States at this scale)
'''
import cartopy.feature as cfeature
import numpy as np

central_lat = 37.5
central_lon = -96
extent = [-120, -70, 24, 50.5]
central_lon = np.mean(extent[:2])
central_lat = np.mean(extent[2:])

plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)

ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND, edgecolor='black')
ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
ax.add_feature(cartopy.feature.RIVERS)
ax.gridlines()


'''
Adding Data to the Map
Now that we know how to create a map, let's add our data to it! That's the whole point.

Because our map is a matplotlib axis, we can use all the familiar maptplotlib commands to make plots. By default, the map extent will be adjusted to match the data. We can override this with the .set_global or .set_extent commands.

In [13]:

    
'''
# create some test data
new_york = dict(lon=-74.0060, lat=40.7128)
honolulu = dict(lon=-157.8583, lat=21.3069)
lons = [new_york['lon'], honolulu['lon']]
lats = [new_york['lat'], honolulu['lat']]

'''
Key point: the data also have to be transformed to the projection space. This is done via the transform= keyword in the plotting method. The argument is another cartopy.crs object. If you don't specify a transform, Cartopy assume that the data is using the same projection as the underlying GeoAxis.

From the Cartopy Documentation

The core concept is that the projection of your axes is independent of the coordinate system your data is defined in. The projection argument is used when creating plots and determines the projection of the resulting plot (i.e. what the plot looks like). The transform argument to plotting functions tells Cartopy what coordinate system your data are defined in.
'''

ax = plt.axes(projection=ccrs.PlateCarree())
ax.plot(lons, lats, label='Equirectangular straight line')
ax.plot(lons, lats, label='Great Circle', transform=ccrs.Geodetic())
ax.coastlines()
ax.legend()
ax.set_global()

'''
Plotting 2D (Raster) Data
The same principles apply to 2D data. Below we create some example data defined in regular lat / lon coordinates.

'''
import numpy as np
lon = np.linspace(-80, 80, 25)
lat = np.linspace(30, 70, 25)
lon2d, lat2d = np.meshgrid(lon, lat)
data = np.cos(np.deg2rad(lat2d) * 4) + np.sin(np.deg2rad(lon2d) * 4)
plt.contourf(lon2d, lat2d, data)

'''
Now we create a PlateCarree projection and plot the data on it without any transform keyword. This happens to work because PlateCarree is the simplest projection of lat / lon data.
'''
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data)

'''
However, if we try the same thing with a different projection, we get the wrong result.
'''
projection = ccrs.RotatedPole(pole_longitude=-177.5, pole_latitude=37.5)
ax = plt.axes(projection=projection)
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data)
plt.show()
'''
To fix this, we need to pass the correct transform argument to contourf:
'''
projection = ccrs.RotatedPole(pole_longitude=-177.5, pole_latitude=37.5)
ax = plt.axes(projection=projection)
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data, transform=ccrs.PlateCarree())