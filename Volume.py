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
# mplstyle.use('fast')
# mplstyle.use(['dark_background', 'ggplot', 'fast'])

directory = os.path.expanduser("~/Desktop/VictoriaPhD/Code/Past/")
# print(os.listdir(directory))
# Get a list of files in the directory
files = [f for f in os.listdir(directory) if f.endswith('.nc')] 

# Initialize the figure index
current_figure_index = 0
plt.rcParams['figure.dpi'] = 800
# Function to display the current figure
def display_Volume_figure():
    plt.clf()  # Clear the current figure
    # plt.figure(figsize=(10,4))
    current_file = files[current_figure_index]
    # plt.title(current_file)
    nfile = nc.Dataset(directory + current_file)
    # # plt.subplot(2,1,1)

    # levels = np.linspace(start = 0, stop = 0.00007, num = 100)
    backspol = nfile['p_pol'][:]
    backsxpol = nfile['x_pol'][:]
    backs1 = nfile['beta_att'][:]
    volume = backsxpol/(backspol + backsxpol)
    threshold = 0.4925
    threshold2 = 0.20
    threshold3 = 0.10
    threshold4 = 0.023
    mask1 = volume > threshold
    volume[mask1] = 0
    backs1[mask1] = 0
    mask4 = volume < threshold4
    volume[mask4] = 0
    backs1[mask4] = 0
    mask2 = volume > threshold2
    volume[mask2] = 0
    backs1[mask2] = 0
    # levels = np.linspace(start = 0, stop = 0.7, num = 70)
    # plt.contourf(np.ndarray.transpose(volume), levels, cmap='turbo')
    # # plt.imshow()
    
    # plt.show()
    
    # plt.clf()  # Clear the current figure
    plt.figure(figsize=(10,4))
    # current_file = files[current_figure_index]
    # nfile = nc.Dataset(directory + current_file)
    

    levels = np.linspace(start = 0, stop = 0.00008, num = 1000)
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
    
    # plt.clf()  # Clear the current figure
    # current_file = files[current_figure_index]
    # nfile = nc.Dataset(directory + current_file)
    

    # levels = np.linspace(start = 0, stop = 0.7, num = 200)
    # backs1 = nfile['linear_depol_ratio'][:]
    plt.yticks([0,1000,2000,3000],['0','5','10','15'])
    # cb.set_yticks([0,100,200,300,399])
    # plt.yticklabels()
    plt.ylabel("Altitude (Km)")
    
    # plt.subplot(2,1,2)
    contour = plt.contourf(np.ndarray.transpose(backs1),levels,locator=ticker.LogLocator(),  cmap= 'turbo')
    
    plt.colorbar()
    # mask2 = volume > threshold2
    # volume[mask2] = -1
    # mask3 = volume > threshold3
    
    # volume[mask3] = 3
    # highlight_values = [-1]
    # highlight_colors = ['black']
    
    # for value,color in zip(highlight_values, highlight_colors):
    #     plt.contour(np.ndarray.transpose(volume),levels=[value], colors=color)
    
    
    # plt.imshow()
    plt.title(current_file)
    # plt.tight_layout()
    head, sep, tail = current_file.partition('.')
    plt.savefig(os.path.expanduser(os.path.join("~/Desktop/VictoriaPhD/Figures", f"plot_{head}.png")), dpi=800)
    print("Yeah")
    plt.show()

# Display the first figure
display_Volume_figure()
for i in range(len(files)):
    try:
        current_figure_index = (current_figure_index + 1) % len(files)
        display_Volume_figure()
    except Exception:
        print(current_figure_index)
        continue
# while True:
#     user_input = input("Press 'n' for next, 'p' for previous, or 'q' to quit: ")
    
#     if user_input == 'n':
#         current_figure_index = (current_figure_index + 1) % len(files)
#         display_Volume_figure()
#     elif user_input == 'p':
#         current_figure_index = (current_figure_index - 1) % len(files)
#         display_Volume_figure()
#     elif user_input == 'q':
#         break

# print("Exiting the figure viewer.")