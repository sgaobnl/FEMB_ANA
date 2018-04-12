# -*- coding: utf-8 -*-
"""
File Name: read_mean.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 3/9/2016 7:12:33 PM
Last modified: Sun Nov 12 09:44:32 2017
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
import math

def linear_fit_excel(chip_id,chn, x, y, x_min,  x_max, plot_path, plot_en = 0):
    file_path = plot_path + "chip"+str(chip_id)+"_chn"+str(chn)    
    x_tmp = x[x_min:x_max]
    y_tmp = y[x_min:x_max]

    error_fit = False 
    try:
        results = sm.OLS(y_tmp,sm.add_constant(x_tmp)).fit()
    except ValueError:
        print "Gain Error chip%d, chn%d"%(chip_id,chn) 
        error_fit = True 
    if ( error_fit == False ):
        with open( (plot_path + "chip"+str(chip_id)+"_chn"+str(chn) + ".txt"),'w') as f:
            a = str(results.summary())
            f.write(a)
        error_gain = False 
        try:
            slope = results.params[1]
        except IndexError:
            slope = 0
            error_gain = True

        try:
            constant = results.params[0]
        except IndexError:
            constant = 0
    else:
        slope = 0
        constant = 0
        error_gain = True

    if (plot_en == 1):
        plt.figure(figsize=(9,6))
        plt.scatter(x, y)
        x_plot = np.linspace(0,4095)

        plt.ylabel("electrons")
        plt.xlabel("ADC counts")
        k = len(x_plot)
        m = max(y)
        if (error_fit):
            plt.text(0.05*k,0.8*m,"Linear Fit Error" )
        elif (error_gain):
            plt.text(0.05*k,0.8*m,"Gain Error" )
        else:
            plt.text(0.05*k,0.8*m,"Y = (%.2f) * X + (%d)"%(slope,constant) )
        plt.title("Linear Fit(Chip%d Channel%d)"%(chip_id, chn) )
        plt.plot(x_plot, x_plot*slope + constant)

        plt.savefig (file_path+".png")
        plt.close()

    return slope,constant

#adc_np = [540 ,768.0461538 ,1032.625 ,1273.646154 ,1544.625 ,1792.47619
#,2054.796875 ,2301.666667 ,2533.703125 ,2778.609375 ,3045.079365 ,3296.777778
#,3558.96875 ,3808.984375 ,4071.968254 ,4095 ,4095 ,4095 ,4095 ,4095 ,4095 ,4095
#,4095 ,4095 ,4095 ,4095 ,4095 ,4095 ,4092.75 ,4095 ,4095 ,4095 ,4095 ,4095 ,4091.328125
#,4095 ,4095 ,4095 ,4095 ,4095 ,4089.421875 ,4095 ,4087.904762 ,4095 ,4095 ,4095 ,4095
#,4095 ,4095 ,4095 ,4095 ,4086.453125 ,4095 ,4095 ,4095 ,4095 ,4095 ,4095 ,4092.984127
#,4095 ,4095 ,4095 ,4095 ,4095]
#adc_np = [
#float('nan') ,153.734375 ,268.8888889 ,369.625 ,485.7460317 ,605.8571429 ,739.4444444 ,860.265625 
#,978.3968254 ,1101.936508 ,1232.142857 ,1356.625 ,1487.47619 ,1618.65625 ,1749.296875
#,1873.365079 ,2021.1875 ,2148.571429 ,2281.111111 ,2409.761905 ,2521.571429 ,2657.84375 ,2787.52381
#,2909.492063 ,3021.920635 ,3129.671875 ,3276.46875 ,3400.71875 ,3509.796875 ,3646.140625 ,3771.269841 ,3880.285714
#,3914.046875 ,3838.859375 ,3509.21875 ,2876.328125 ,2919.3125 ,2956.125 ,3002.796875 ,3028.634921
#,3078.9375 ,3159.546875 ,3219.828125 ,3224.78125 ,3286.412698 ,3346.8125 ,3425.890625 ,3451.888889
#,3472.328125 ,3459.125 ,3470.380952 ,3558.793651 ,3690.046875 ,3445.953125 ,3553.492063 ,3667.904762
#,3797.238095 ,3848.428571 ,3844.890625 ,3828.460317 ,3831.857143 ,3850.84375 ,3806.857143 ,3960.52381]
#
##
#linear_fit(0,0, adc_np,1,"./")
