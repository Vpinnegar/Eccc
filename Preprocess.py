# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:51:53 2023

@author: starv
Preprocessing before cloud finding:
    Goal: 1. reduce noise, 2 increase contrast, 3 maintain or improve resolution
1. Reduce Noise
What: decrease noise with increased height. 
How: Have two choices linear and non linear high pass filtering

"""
### Imports ###
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
# from scipy.signal import savgol_filter
from ambiance import Atmosphere
from pyatmos import coesa76
import seaborn as sns
import sys
import scipy.signal as signal
from scipy.signal import savgol_filter
from scipy.signal import lfilter
### Preprocessing before Cloud finding. 
fp = r'E:\MPLNETDATA\CeilL2\2021\06\10\L2_0-20000-0-73009_A20210610.nc'

op = nc.Dataset(fp)
ok = op['attenuated_backscatter_0'][:]
# for i in range(len(ok[0,:])):
prof1 = ok[:,173]
print(len(ok[0,:]))
plt.plot(prof1)
plt.show()
# prof1 = np.delete(prof1, 0)
# prof1 = np.delete(prof1, 0)
# prof1 = np.delete(prof1, 0)
# prof1 = np.delete(prof1, 0)
# prof1 = np.delete(prof1, 0)
# prof1 = np.delete(prof1, 0)
# prof1 = np.delete(prof1, 0)
# prof1 = np.delete(prof1, 0)
o = 999

d, pwel = signal.welch(prof1, o)

plt.semilogy(d, pwel)
plt.xlabel('Altitude')
plt.ylabel('PSD')
plt.grid()
plt.show()


n = 15  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 2
yy = lfilter(b, a, prof1)


plt.plot(yy, linewidth=2, linestyle="-", c="b")  # smooth by filter
from scipy.signal import savgol_filter
w = savgol_filter(prof1, 31, 2)

x = np.linspace(0,511,511)
deriv = np.gradient(w,x)
ave = np.mean(deriv)
plt.figure()
plt.plot(deriv, 'red' )
flat_indices = np.where(np.abs(deriv) < np.abs(ave))[0]
plt.figure()
plt.plot(w, 'black' )
# plt.plot(flat_indices)
plt.figure()



def double_res_averages(data):
    doubleddat = [data[0]]
    
    for i in range(len(data)-1):
        average = (data[i] + data[i + 1]) / 2 
        doubleddat.extend([average,data[i+ 1]])
    return doubleddat


ogdat = [1,2,4,6,8,10]
doubled_data = double_res_averages(ogdat)
print(doubled_data)

prof1 = double_res_averages(prof1)
plt.figure()
plt.plot(prof1)

d, pwel = signal.welch(prof1, o)

plt.semilogy(d, pwel)
plt.xlabel('Altitude')
plt.ylabel('PSD')
plt.grid()
plt.show()


n = 15  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 2
yy = lfilter(b, a, prof1)


plt.plot(yy, linewidth=2, linestyle="-", c="b")  # smooth by filter
from scipy.signal import savgol_filter
w = savgol_filter(prof1, 101, 2)

x = np.linspace(0,1021,1021)
deriv = np.gradient(w,x)
ave = np.mean(deriv)
plt.figure()
plt.plot(deriv, 'red' )
flat_indices = np.where(np.abs(deriv) < np.abs(ave))[0]
plt.figure()
plt.plot(w, 'black' )

