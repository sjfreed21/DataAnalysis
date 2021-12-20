#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:55:53 2020

@author: zhwa2432
https://github.com/Unidata/python-workshop/blob/master/notebooks/Satellite_Data/PlottingSatelliteData.ipynb

/opt/anaconda3/bin/pip install vcrpy
/opt/anaconda3/bin/conda install --name pyaos-lesson -c conda-forge vcrpy-unittest
https://thredds.ucar.edu/thredds/catalog.html
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html


"""


# from datetime import datetime
# import cartopy # as ccrs
# import cartopy.crs as ccrs
# import matplotlib.pyplot as plt
# import metpy  # noqa: F401
# import numpy as np
# import xarray
# from metpy.cbook import get_test_data
# from metpy.io import GiniFile
# from metpy.plots import add_metpy_logo, add_timestamp, colortables
# Required Modules

from siphon.catalog import TDSCatalog # Code to support reading and parsing catalog files from a THREDDS Data Server (TDS)
import urllib.request # Defines functions and classes which help in opening URLs


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
warnings.simplefilter(action='ignore', category=ResourceWarning)

# This is currently a placeholder for a better example
#from __future__ import print_function

# from siphon.http_util import session_manager

cat = TDSCatalog('http://thredds.ucar.edu/thredds/catalog.xml')
print(list(cat.catalog_refs))

# Unidate THREDDS Data Server Catalog URL
base_cat_url = 'https://thredds-test.unidata.ucar.edu/thredds/catalog/satellite/{satellite}/{platform}/{dataset}/{sector}/{channel}/{date}/catalog.xml'
base_cat_url = 'https://thredds.ucar.edu/thredds/catalog/satellite/goes/east/grb/ABI/FullDisk/{channel}/{date}/catalog.xml'
base_cat_url = 'https://thredds.ucar.edu/thredds/catalog/satellite/goes/east/grb/ABI/{sector}/{channel}/{date}/catalog.xml'

# Desired data
satellite = 'goes16'
platform = 'GRB16'
dataset = 'ABI'
channel = ['Channel13','Channel07']
channel = ['Channel13','Channel02','Channel08','Channel09','Channel10']
#sector = 'FullDisk'
sector = 'Mesoscale-1'
date = 'current'
#date='20201005' # 
'''
 ABI 13 --Infrared
 ABI 2 -- visible
 ABI 8 -- Upper Level WV
 ABI 9 Mid-level Water Vapor
 ABI 10 Low Level WV
 
'''
# Output directory
# outdir = "~\\dataset\\"
outdir ='/Users/sjfre/Documents/DataAnalysis/Class Files/Lab 3/Data Sources/dat/'
#outdir ='/Volumes/CRL_Data/data/satellite/'
# For each channel
for channel in channel:
    cat_url = base_cat_url.format(satellite = satellite, platform = platform, dataset = dataset, sector = sector, date = date, channel=channel)
    #cat_url = base_cat_url.format( date = date, channel=channel)

    # Access the catalog
    print(cat_url)
    cat = TDSCatalog(cat_url)
    #print(cat.datasets)
    # Get the latest dataset available
    ds = cat.datasets[-1]
    print('\n',ds)
    # Get the URL
    url = ds.access_urls['HTTPServer']
    print('\nurl',url)
    # Download the file
    urllib.request.urlretrieve(url, outdir + str(ds))
    num=0
    ifiles=[0,1,2,3]
    #for i in cat.datasets:
    for i in ifiles:
        ds = cat.datasets[i]
        print('\n',ds)
        # Get the URL
        url = ds.access_urls['HTTPServer']
        # Download the file
        urllib.request.urlretrieve(url, outdir + str(ds))
        
        

'''
OPTIONS:
satellite:
goes16
goes17
 
platform:
GRB16
GRB17
 
dataset:
ABI
EXIS
GLM
MAG
Products
SEIS
SUVI
 
product:
EXIS: SFEU, SFXR
GLM:  LCFA
MAG:  GEOF
SEIS: EHIS, MPSH, MPSL, SGPS
SUVI: Fe093, Fe131, Fe171, Fe195, Fe284, He303
Products: (please see below)
 
product:
AerosolDetection
AerosolOpticalDepth
CloudAndMoistureImagery
CloudMask
CloudOpticalDepth
CloudParticleSize
CloudTopHeight
CloudTopPhase
CloudTopPressure
CloudTopTemperature
DerivedMotionWinds
DerivedStabilityIndices
FireHotSpot
GeostationaryLightningMapper
LandSurfaceTemperature
LegacyVerticalMoistureProfile
LegacyVerticalTemperatureProfile
RainRateQPE
SeaSurfaceTemperature
TotalPrecipitableWater
VolcanicAshDetection
 
sector:
CONUS, FullDisk, Mesoscale-1, Mesoscale-2
 
channel:
Channel01 - Channel16
 
date:
current (last 24 hours)
YYYYMMDD
'''


