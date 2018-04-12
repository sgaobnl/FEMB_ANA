# -*- coding: utf-8 -*-
"""
File Name: read_mean.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 3/9/2016 7:12:33 PM
Last modified: Tue Nov 21 11:55:48 2017
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

def temp_fit(chip= "chip3"):
#AM27
    
    chip3_y = [35.7, 31.5, 22.2, 15.4, 7.3, -8.8, -19.3, -30.2, -41.7, -51.4, -64.2, -76.9, -82.3, -87.6, -94.6, -102.1, -110.5, -127.4, -135.2, -147.8, -153.1, -156.1, -159.9, -168.8]
    chip3_x = [982, 973, 940, 916, 892, 837, 799, 772, 740, 708, 668, 628, 612, 596, 572, 548, 524, 476, 445, 396, 380, 364, 356, 324 ]
    
    chip4_y = [34.9, 30.8, 20.3, 13.3, 5.2, -12.3, -23.6, -35.7, -44.1, -57.1, -67.1, -77.9, -85.8, -82.8, -97.4, -100.2, -111.3, -121.8, -132.8, -138, -148.8, -156.4, -160.2, -169.4] 
    chip4_x = [985, 975, 940, 910, 884, 825, 788, 764, 735, 700, 668, 636, 612, 588, 572, 564, 524, 500, 460, 444, 406, 380, 364, 340 ]

    chip3_y_r = [-171.8,-140,-130,-100, -90,-75,-65,-50,-40,-30,-20,-10]
    chip3_x_r = [404,516,550,612,628,676,710,772,812,828,868,908 ]

    if (chip == "chip3"):
        x_np = np.array(chip3_x)
        y_np = np.array(chip3_y)
    elif (chip == "chip3_r"):
        x_np = np.array(chip3_x_r)
        y_np = np.array(chip3_y_r)
    else:
        x_np = np.array(chip4_x)
        y_np = np.array(chip4_y)


    cresults = sm.OLS(y_np,sm.add_constant(x_np)).fit()
    cslope = cresults.params[1]
    cconstant = cresults.params[0]


    plt.figure(figsize=(8,6))
    plt.scatter(x_np, y_np,c='r',marker='o')
    cx_plot = np.linspace(300,max(x_np))

    plt.ylabel("Temperature / degree")
    plt.xlabel("Voltage / mV")
    k = len(cx_plot)
    m = max(y_np)
    plt.text(310.0,0.9*m,"Y = (%.3f) * X + (%.2f)"%(cslope,cconstant) )
    plt.title("Linear Fit" )
    plt.plot(cx_plot, cx_plot*cslope + cconstant, 'r')
#    plt.show()
    plt.savefig("./" + chip + "_temp_voltage.png")
    plt.close()

    return cslope, cconstant
#temp_fit(chip = "chip3")
#temp_fit(chip = "chip3_r")
#temp_fit(chip = "chip4")

