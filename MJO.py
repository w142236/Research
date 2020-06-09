# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:40:19 2020

@author: willk
"""

import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

import calendar as clndr
from datetime import datetime
from dateutil.parser import parse
import pandas as pd

import matplotlib.cm as cm
import itertools

filename = "C:/Users/willk/desktop/omi.1x[2864].txt"

f = open(filename, 'r')

MJO_dict = {}


for lines in f:
    date  = ""
    coords = ""
    for i in range(13):
        date = date + lines[i]
    for j in range(17,25):
        if(lines[j] != " "):
            coords = coords + lines[j]
    if("-" in coords == True):
        xcoords = float(coords) * -1
    else:
        xcoords = float(coords)
    coords = ""
    for k in range(29,37):
        if(lines[k] != " "):
            coords = coords + lines[k]
    if("-" in coords == True):
        ycoords = float(coords) * -1
    else:
        ycoords = float(coords)
    coords = ""
    for l in range(41,49):
        if(lines[k] != " "):
            coords = coords + lines[l]
    if("-" in coords == True):
        zcoords = float(coords) * -1
    else:
        zcoords = float(coords)
        
    MJO_dict.update({date:tuple([xcoords,ycoords,zcoords])})
    
## PLotting
    
from mpl_toolkits import mplot3d

#%matplotlib inline
fig = plt.figure(figsize = (18,16))
#ax = plt.axes(projection='3d')
ax = plt.axes()

# Data for a three-dimensional line
data = np.array([MJO_dict[dates] for dates in MJO_dict])

#zline = np.linspace(0, 15, 1000)
#zline = np.linspace(np.min([data[i][2] for i in range(len(MJO_dict))]),np.max([data[i][2] for i in range(len(MJO_dict))]), 1000)
#xline = np.sin(zline)
#yline = np.cos(zline)
#ax.plot3D(xline, yline, zline, 'gray')
# Data for three-dimensional scattered points


#zdata = np.array([data[i][2] for i in range(1000)])
#xdata = np.array([data[i][0] for i in range(1000)])
#ydata = np.array([data[i][1] for i in range(1000)])
#xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
#ydata = np.cos(zdata) + 0.1 * np.random.randn(100)

format = "%Y\t%m\t%d %H"

xdata = [data[dates][0] for dates in range(len(data))]
ydata = [data[dates][1] for dates in range(len(data))]

xdata = np.array([])
ydata = np.array([])
colors = cm.rainbow_r(np.arange(1,10000,1))
currentmonth = 1
for dates in MJO_dict:
    currentdate = datetime.strptime(dates,format)
    if(currentdate.month == currentmonth):
        xdata = np.append(arr=xdata,values=MJO_dict[dates][0])
        ydata = np.append(arr = ydata,values = MJO_dict[dates][1])
    else:
        ax.scatter(xdata,ydata,s = 10, color = colors[currentmonth*20])
        plt.xlim(-4,4)
        plt.ylim(-4,4)
        plt.xticks(ticks = np.arange(-4,4,.5))
        plt.yticks(ticks = np.arange(-4,4,.5))
        plt.plot(xdata,ydata,color = colors[currentmonth*20])
        plt.text(xdata[0],ydata[0],"{}".format(currentdate.month))
        currentmonth = currentdate.month
        xdata = np.array([])
        ydata = np.array([])
        if(currentdate.year >= 1980):
            break
        else:
            pass
plt.savefig("MJO_path_1979")
        
