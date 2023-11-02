# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:27:51 2023

@author: starv
"""
from matplotlib import pyplot as plt # import libraries
import pandas as pd # import libraries
import netCDF4 as nc # import libraries
import numpy as np
import sklearn
import scipy
import glob
import math 
import statsmodels
import statsmodels
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.signal import savgol_filter
from ambiance import Atmosphere
from pyatmos import coesa76
import seaborn as sns
import sys
from matplotlib import cm, ticker
""" Figure Opener """


Path1 = r'C:\Users\starv\Downloads\EastgateCL51_20230731_090305.nc'
Path2 = r'C:\Users\starv\Downloads\EastgateCL61_20230731_090300.nc'

nfile = nc.Dataset(Path2)
# print(nfile)

backsx = nfile['x_pol'][:]
backsp = nfile['p_pol'][:]
nega = backsx < 0 
negap = backsp < 0 
backsx[nega] = 0
backsp[negap] = 0
vol = backsx/(backsp + backsx)
levels = np.linspace(start = 0, stop = 0.9, num = 70)
plt.figure(figsize=(10,4))
plt.contourf(np.ndarray.transpose(vol),levels, cmap=plt.cm.jet)
plt.savefig('voldepol.png', dpi = 1000)

nfile = nc.Dataset(Path2)
# print(nfile)
levels = np.linspace(start = 0, stop = 0.9, num = 70)
backs1 = nfile['linear_depol_ratio'][:]
plt.figure(figsize=(10,4))
plt.contourf(np.ndarray.transpose(backs1),levels, cmap=plt.cm.jet,locator=ticker.LogLocator())
plt.savefig('lindepol.png', dpi = 1000)


"Normalize?"

absback = np.abs(backs1)
min_val = np.min(absback)
max_val = np.max(absback)
# norm_back = (backs1 - min_val)/(max_val - min_val)

# min_val = np.min(norm_back)
# max_val = np.max(norm_back)

# levels = np.linspace(start = min_val, stop = max_val, num = 100)
# plt.figure()
# plt.contour(np.ndarray.transpose(norm_back),levels, cmap=plt.cm.jet)





"""INjection Checker"""
## Choose a height 1. in a profile with no cloud
## 2 in a profile with cloud
## Inject different levels of scattering 

# x = np.linspace(1,100,5)
# injection = max_val/x
# inject = injection[::-1]
# backinj = []
# backinj = backs1
# for i in range(len(x)):
    
#     backinj[:,1500] += inject[i]
#     print(backinj[1,1500])
#     plt.figure()
#     plt.contour(np.ndarray.transpose(backinj),levels, cmap=plt.cm.jet)



""" Calibration Constant """


# plt.figure()
# plt.plot(backs1[100,:])
# x = np.linspace(0,3276,3276)
# z = np.polyfit(x, backs1[100,:],8)
# p = np.poly1d(z)

# #add trendline to plot
# plt.plot(x, p(x))
# w = savgol_filter(backs1[100,:], 101, 2)
# deriv = np.gradient(w,x)
# ave = np.mean(deriv)
# plt.figure()
# plt.plot(deriv, 'red' )
# flat_indices = np.where(np.abs(deriv) < np.abs(ave))[0]


# # prof = backs1[100,:]
# def LargeSpike(prof):
#     length = len(prof)
#     indices = []
#     for i in range(len(prof)):
        
#         if prof[i] > 1e-5:
#             print(i)
#             indices.append(i)
#             print(indices)
#     return indices

# flat = LargeSpike(backs1[100,:])
        
        







