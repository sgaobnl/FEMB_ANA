# -*- coding: utf-8 -*-
"""
File Name: read_mean.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 3/9/2016 7:12:33 PM
Last modified: Sun Nov 12 09:44:18 2017
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
import numpy as np
#import scipy as sp
#import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def gain_plot(sheetname, slope_np, save_path, env = "RT", FEMB = "FEMB0", DAC = "FPGADAC"):
    tp_cs = int(sheetname[0],16)&0x03
    if ( tp_cs == 1 ):
        tp_set = "0.5 us"
    elif ( tp_cs == 0 ):
        tp_set = "1.0 us"
    elif ( tp_cs == 3 ):
        tp_set = "2.0 us"
    elif ( tp_cs == 2 ):
        tp_set = "3.0 us"

    gain_cs =  int(sheetname[1],16) >> 2 
    if ( gain_cs == 0 ):
        gain_set = "4.7 mV/fC"
    elif ( gain_cs == 1 ):
        gain_set = "7.8 mV/fC"
    elif ( gain_cs == 2 ):
        gain_set = "14.0 mV/fC"
    elif ( gain_cs == 3 ):
        gain_set = "25.0 mV/fC"
   
    ylim_value = 1000 
    plt.figure(figsize=(10,6)) 
    chips = 8
    for i in range(chips):
        slope_chip_np = slope_np[i*16:(i+1)*16]
        channel_id_np = np.arange(16*i,16*(i+1),1)
        plt.scatter(channel_id_np, slope_chip_np, color = 'r')
        plt.plot(channel_id_np, slope_chip_np, color = 'b')
        plt.text(16*i+2,ylim_value*0.7,"ASIC%d"%(i+1))
        plt.vlines(16*i,0, ylim_value*0.75, color = 'g')
        
    red_patch = mpatches.Patch(color='b', label=env + ", " + DAC)
    plt.legend(handles=[red_patch])
    plt.text(100,ylim_value*0.85,"Mean=%d"%(np.mean(slope_np)))
    plt.text(100,ylim_value*0.80,"std=%d"%( np.std(slope_np) ))

    plt.ylabel("Gain /  (e-)/(ADC bin)")
    plt.xlabel("Channel")
    plt.ylim([0,ylim_value*1.0])
    plt.xlim([0,128])
    plt.text(15, ylim_value*0.9, "Peaking time = " + tp_set)
    plt.text(15, ylim_value*0.85, "Gain = " + gain_set )
    plt.title("Gain distribution" )
   
    plt.savefig(save_path+ "/" + FEMB + DAC + sheetname +"_gain.png")
    plt.close()

    slope_all_np = []
    for i in range(chips):
        if (i == 0) :
            slope_all_np = slope_np[i*16:(i+1)*16]
        else:
            slope_all_np =np.append(slope_all_np, slope_np[i*16:(i+1)*16])
    plt.hist(slope_all_np)
    plt.title("Gain Histrogram" )
    plt.xlabel("Gain / (e-/ADCbin)")
    plt.ylabel("channel counts")
    plt.savefig(save_path+ "/" + FEMB + DAC + sheetname + "_gainhist.png")
    plt.close()


