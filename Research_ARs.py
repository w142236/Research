# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 00:43:16 2020

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



filename = "C:/Users/willk/desktop/cluster_dates.txt"
f = open(filename, "r")
S_cluster_datetimes = []
N_cluster_datetimes = []
i = 0
for lines in f:
    if lines[0] is not " ":
        #if lines.strip() != "Northern cluster:":
        try:
            if lines[0].isnumeric() and int(lines[0:4]) >= 1979 and i < 63:
                dt = datetime.strptime(lines.strip(),'%Y-%m-%d %H:%M:%S')
                dt = dt.date()
                S_cluster_datetimes.append(dt)
            elif lines[0].isnumeric() and int(lines[0:4]) >= 1979 and i >= 63:
                dt = datetime.strptime(lines.strip(),'%Y-%m-%d %H:%M:%S')
                dt = dt.date()
                N_cluster_datetimes.append(dt)
                
        except:
            pass
    else:
        break
    #print("{}, {}".format(lines, i))
    i+=1
    #else:
     #   print("break")
    
        
#Southern Cluster#################################################################
S_date = S_cluster_datetimes[0]
S_fileDates = {datetime.strftime(S_date,"%Y%m"):{'days':[]}} #{Date:{'days':[]}}

for dates in S_cluster_datetimes:
    #print("before: {}, {}".format(date, dates))

    if(dates.month != S_date.month):                  
        str = datetime.strftime(dates,"%Y%m")
        S_fileDates.update({str:{'days':[]}})
        #S_fileDates[S_date]['days'].append(dates.day)
        S_date = dates
        #print("if after: {}, {}, {}".format(date, dates, i))
    else:
        str = datetime.strftime(dates,"%Y%m")
        S_fileDates.update({str:{'days':[]}})
        S_date = dates
        #print("else after: {}, {}, {}".format(date, dates, i))
        #i += 1
for dates in S_cluster_datetimes:
    S_fileDates[datetime.strftime(dates,"%Y%m")]['days'].append(dates.day-1) #had to subtract 1 day since indices start at 0
#Completed
#################################################################################

#Northern Cluster################################################################        
N_date = N_cluster_datetimes[0]
N_fileDates = {datetime.strftime(N_date,"%Y%m"):{'days':[]}} #{Date:{'days':[]}}

for dates in N_cluster_datetimes:
    #print("before: {}, {}".format(date, dates))
    if(dates.month != N_date.month):                  #It "sees" the 1990 file, but does not update it
        str = datetime.strftime(dates,"%Y%m")
        N_fileDates.update({str:{'days':[]}})
        N_date = dates
        #print("if after: {}, {}, {}".format(date, dates, i))
    else:
        str = datetime.strftime(dates,"%Y%m")
        N_fileDates.update({str:{'days':[]}})
        N_date = dates
for dates in N_cluster_datetimes:
    N_fileDates[datetime.strftime(dates,"%Y%m")]['days'].append(dates.day-1) #had to subtract 1 day since indices start at 0
#################################################################################
#Completed    

#################################################################################
#Plot############################################################################
my_example_nc_file = 'C:/Users/willk/Desktop/raw_height_data/hgt.197901.nc'
fh = Dataset(my_example_nc_file, mode='r')
level = fh.variables['level'][:] #1000-100hPa
lats = fh.variables['lat'][:]
lons = fh.variables['lon'][:]
x = fh.variables['x'][:]
y = fh.variables['y'][:]
time = fh.variables['time'][:]#in hours. Not necessary
height = fh.variables['hgt'][:]#[time][level][y][x]
#print(height.shape)
fh.close()

llcrnrlat, llcrnrlon = 5, -179
urcrnrlat, urcrnrlon = np.max(lats), -40
#lons = np.arange(llcrnrlon,urcrnrlon,10)
#lats = np.arange(llcrnrlat,urcrnrlat,10)
projection = 'lcc' #lambert conformal conical projection
resolution = {'crude':'c','low':'l','intermediate':'i','high':'h','full':'f'}
#area_thresh = {'10000km':'c','1000km':'l','':'','':'','':''} 

#Southern Cluster
S_dates = np.array([Dates for Dates in S_fileDates])
#S_dates = [Dates for Dates in S_dates if (int(Dates)>=197901)] 
Strings = np.array(['hgt.{}.nc'.format(Dates) for Dates in S_dates])
S_fh = np.array([Dataset('C:/Users/willk/Desktop/raw_height_data/{}'.format(strings),mode = 'r') for strings in Strings])

#Northern Cluster
N_dates = np.array([Dates for Dates in N_fileDates])
#S_dates = [Dates for Dates in S_dates if (int(Dates)>=197901)] 
Strings = np.array(['hgt.{}.nc'.format(Dates) for Dates in N_dates])
N_fh = np.array([Dataset('C:/Users/willk/Desktop/raw_height_data/{}'.format(strings),mode = 'r') for strings in Strings])


#Southern Cluster####################################################################################
#
#S_heights_dict = {}
#for Dates in S_dates:
#    S_heights_dict.update({Dates:{}})
#    for days in S_fileDates[Dates]['days']:
#        S_heights_dict[Dates].update({days:np.array([])})
#height_dict = {'dates':[fh.variables()}
#print(S_heights_dict)

#Takes ~ 2:00
#S_year_month_heights = np.array([S_fh[i].variables['hgt'][:] for i in range(len(S_dates))])
#np.ma.set_fill_value(S_year_month_heights,None)
#yearmonth = 0
#for YearMonth in S_heights_dict:
#    for days in S_heights_dict[YearMonth]:
#Had to use try except to avoid out-of-bounds
#        try:
            #heights_dict[YearMonth][days] = array[iter]
#            S_heights_dict[YearMonth][days] = S_year_month_heights[yearmonth][days][16]
#        except:  
#            pass
#    yearmonth += 1
#number = 1   
#####################################################################################
#Problem            
#m = Basemap(llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,projection,resolution['low'])
#####################################################################################
#for yearmonth in S_heights_dict:
    #print(yearmonth)
#    for days in S_heights_dict[yearmonth]:
        #if (heights_dict[yearmonth][days] > 0.0) > 0.0:
        #    data = np.array(heights_dict[yearmonth][days])
        #data = np.array(heights_dict[yearmonth][days])
        #print(yearmonth,days)
#        if (int(yearmonth) < 198012):
        #    print("true")
#            cs = m.pcolor(xi,yi,S_heights_dict[yearmonth][days])
            
#            m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
#            m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)


#            m.drawcoastlines()
#            m.drawstates()
#            m.drawcountries()


#            cbar = m.colorbar(cs, location='right', pad="5%")
#            cbar.set_label('meters')


#            plt.title('Southern Cluster Map {}: YearMonth: {} Day: {}'.format(number, yearmonth, days))
#            plt.show()
#            number += 1
            
#Northern Cluster#######################################################################################
N_heights_dict = {}
for Dates in N_dates:
    N_heights_dict.update({Dates:{}})
    for days in N_fileDates[Dates]['days']:
        N_heights_dict[Dates].update({days:[]})
#height_dict = {'dates':[fh.variables()}
#print(N_heights_dict)

#Takes ~ 2:00
N_year_month_heights = np.array([N_fh[i].variables['hgt'][:] for i in range(len(N_dates))])

yearmonth = 0
for YearMonth in N_heights_dict:
    for days in N_heights_dict[YearMonth]:
#Had to use try except to avoid out-of-bounds
        try:
            #heights_dict[YearMonth][days] = array[iter]
            N_heights_dict[YearMonth][days] = N_year_month_heights[yearmonth][days][16]
        except:  
            pass
    yearmonth += 1
number = 1
#############################################
lon_0 = fh.centerlon
lat_0 = fh.centerlat    
m = Basemap(width=np.max(x),height=np.max(y),
           resolution='l',projection='lcc',\
            lat_ts=40,lat_0=lat_0,lon_0=lon_0)
#############################################
#m = Basemap(llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,projection,resolution['high'])
#xi, yi = m(lons, lats)
for yearmonth in N_heights_dict:
    #print(yearmonth)
    for days in N_heights_dict[yearmonth]:
        #if (heights_dict[yearmonth][days] > 0.0) > 0.0:
        #    data = np.array(heights_dict[yearmonth][days])
        #data = np.array(heights_dict[yearmonth][days])
        #print(yearmonth,days)
        #if (int(yearmonth) < 200012):
        #    print("true")
            #N_heights_dict[yearmonth][days] = N_heights_dict[yearmonth][days].filled(np.mean(N_heights_dict[yearmonth][days]))
            #cs = m.pcolor(xi,yi,np.squeeze(N_heights_dict[yearmonth][days]), cmap = 'hsv')
        cs = m.pcolor(x, y , np.squeeze(N_heights_dict[yearmonth][days]), cmap = 'hsv')
        m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
        m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)


        m.drawcoastlines()
        m.drawstates()
        m.drawcountries()


        cbar = m.colorbar(cs, location='right', pad="10%")
        cbar.set_label('meters')


        plt.title('Northern Cluster Map {}: YearMonth: {} Day: {}'.format(number, yearmonth, days))
        plt.show()
        number += 1
        #
#341 - 348 are NaN

#End################################################################################################
####################################################################################################