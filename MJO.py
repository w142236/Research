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
    

          