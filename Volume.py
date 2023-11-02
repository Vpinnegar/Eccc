# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:05:37 2023

@author: starv
"""
import os
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt # import libraries
import pandas as pd # import libraries
import netCDF4 as nc # import libraries
import numpy as np
from matplotlib import cm, ticker

import matplotlib.style as mplstyle
mplstyle.use('fast')
mplstyle.use(['dark_background', 'ggplot', 'fast'])

directory = 'C:/Users/starv/Downloads/Past/'

# Get a list of files in the directory
files = [f for f in os.listdir(directory) if f.endswith('.nc')] 

# Initialize the figure index
current_figure_index = 0

# Function to display the current figure
def display_Volume_figure():
    plt.clf()  # Clear the current figure
    current_file = files[current_figure_index]
    nfile = nc.Dataset(directory + current_file)
    

    # levels = np.linspace(start = 0, stop = 0.00007, num = 100)
    backspol = nfile['p_pol'][:]
    backsxpol = nfile['x_pol'][:]
    volume = backsxpol/(backspol + backsxpol)
    
    
    levels = np.linspace(start = 0, stop = 0.7, num = 50)
    plt.contourf(np.ndarray.transpose(volume), levels, cmap='turbo')
    # plt.imshow()
    plt.title(current_file)
    plt.show()
    
    plt.clf()  # Clear the current figure
    # current_file = files[current_figure_index]
    # nfile = nc.Dataset(directory + current_file)
    

    # levels = np.linspace(start = 0, stop = 0.00007, num = 200)
    # backs1 = nfile['beta_att'][:]
    
    # new_bins = len(backs1[0,:])//7
    # reducedarray = np.zeros((360,new_bins))
    # for ii in range(360):
    #     for i in range(new_bins):
    #         start_index = i*7
    #         end_index = (i+1)*7
    #         reducedarray[ii,i] = np.mean(backs1[ii,start_index:end_index])
    # levels = np.linspace(start = 0, stop = 0.00007, num = 100)
    # plt.contour(np.ndarray.transpose(reducedarray),levels, cmap=plt.cm.jet)
    # # plt.imshow()
    # plt.title(current_file)
    # plt.show()
    
    plt.clf()  # Clear the current figure
    # current_file = files[current_figure_index]
    # nfile = nc.Dataset(directory + current_file)
    

    levels = np.linspace(start = 0, stop = 0.7, num = 50)
    backs1 = nfile['linear_depol_ratio'][:]
    
    
    plt.contourf(np.ndarray.transpose(backs1),levels, cmap='turbo')
    # plt.imshow()
    plt.title(current_file)
    plt.show()

# Display the first figure
display_Volume_figure()

while True:
    user_input = input("Press 'n' for next, 'p' for previous, or 'q' to quit: ")
    
    if user_input == 'n':
        current_figure_index = (current_figure_index + 1) % len(files)
        display_Volume_figure()
    elif user_input == 'p':
        current_figure_index = (current_figure_index - 1) % len(files)
        display_Volume_figure()
    elif user_input == 'q':
        break

print("Exiting the figure viewer.")