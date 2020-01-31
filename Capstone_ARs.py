# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:19:55 2020

@author: willk
"""
from netCDF4 import Dataset
import numpy as np
#Task 1: Read in the data file 
filename = "C:/Users/willk/Desktop/Capstone.nc"

fh = Dataset(filename, mode =  "r")
lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]

time = fh.variables['time'][:] #360 day calendar [1 1 1 0] #47 days (exclusively)
Temp = fh.variables['ta'][:] #47 days (48, 32, 64)
surf_T = fh.variables['tas'][:] #time, lat, lon #Also 2m temp
u_wind = fh.variables['ua'][:] #[48][6][32][64]
v_wind = fh.variables['va'][:]
spec_humidity = fh.variables['hus'][:]#same dims
heights = fh.variables['zg'][:]#same dims
rel_humidity = fh.variables['hur'][:]#same dims

#Task 2: Build the data structure
u_wind_dict = {}
for i in range(len(time)):
    #u_wind_dict.update({time[i]:{}})
    u_wind_dict.update({time[i]:np.array([])})
for i in range(len(time)):
    print(u_wind_dict[time[i]])
    
#Task 3: Build map

#Task 4: plot

#Task 5: Sorting Algorithm

 
