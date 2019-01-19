# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 10/11/2017 4:34:40 AM
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
import numpy as np
import os
#from sys import exit
import os.path
import math
#import statsmodels.api as sm
#from matplotlib.backends.backend_pdf import PdfPages
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#from matplotlib.ticker import FuncFormatter

def paras_tp_allchn_pre_coh( all_chn_results, coh_chn_np, paras=5, wire_type="All"):
    #paras = 5: ped
    #paras = 6: rms
    #paras = 3: f for FFT
    #paras = 4: p for FFT
    #paras = 7: x for gain
    #paras = 8: y for gain
    #paras = 9: Gain
    #wire_type = "Y": Y wire
    #wire_type = "U": U wire
    #wire_type = "V": V wire
    #wire_type = "A": Any wire
    #paras = 10: chn 
    #paras = 11:  stuck_type
    if paras == 11:
        rms_cs = 0
        par = 8
    elif paras == 10:
        rms_cs = 0
        par = 7
    elif paras <= 6:
        rms_cs = 0
        par = paras
    else:
        rms_cs = 1
        par = paras-6

    paras_tp_chn = []
#    stuck_type = "Small"
    for tp in range(4):
        paras_chn = []
        #for chn in range(128):
        for chn in coh_chn_np:
            one_chn_tp = all_chn_results[chn][tp]
                
            if (wire_type == "All") :
#                if (paras == 6 ):
#                    paras_chn.append(one_chn_tp[2][6])
#                elif (paras == 3 ):
#                    paras_chn.append(one_chn_tp[2][10])
#                elif (paras == 4 ):
#                    paras_chn.append(one_chn_tp[2][11])
#                else:
                paras_chn.append(one_chn_tp[rms_cs][par])
#            elif (  one_chn_tp[0][2]== wire_type ) and (  stuck_free == True ):
#            elif (  one_chn_tp[0][2]== wire_type ) :
#                paras_chn.append(one_chn_tp[rms_cs][par])
        paras_tp_chn.append(paras_chn)

    return paras_tp_chn

