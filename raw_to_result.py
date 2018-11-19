# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Mon Nov 27 12:32:11 2017
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
#from openpyxl import Workbook
#import numpy as np
#import struct
#import os
#from sys import exit
#import os.path
#import math
#import statsmodels.api as sm
#
#
#from fft_3d_plot import fft_3d_plot
#from fft_2d_plot import fft_2d_plot
#from one_chn_plot import one_chn_plot

#from matplotlib.backends.backend_pdf import PdfPages

from dataforplane import dataforplane
from one_chn_result import one_chn_result
from one_chn_gain import one_chn_gain
import pickle

def raw_to_result(alldata, gainfile_path, savefile, apa="ProtoDUNE", step="step001", femb=0, psd=True, env="RT", gain=3, DAC = "FPGADAC", DACvalue = [4,5,6,7,8,9,10,11], stuck_filter = True, hp_fliter=False):
    all_chn_results = []
    for chn in range(128):
    #for chn in range(2):
        one_chn_tp = []
        for tp_fe in [1,0,3,2]:
            yuvdata_in = dataforplane(alldata, apa, femb, tp_fe )
            rmstmp = one_chn_result(yuv_data_in=yuvdata_in, chn=chn, apa=apa, femb=femb, tp=tp_fe, psd=psd, step = step, stuck_filter = stuck_filter, env = env, hp_fliter = hp_fliter)
            gaintmp = one_chn_gain(gainfile_path,chn, tp_fe, env,gain, femb, DAC, DACvalue)
            one_chn_tp.append([rmstmp, gaintmp])
        print "Chn%d has been analyzed"%chn
        all_chn_results.append(one_chn_tp)

    with open(savefile, 'wb') as fp:
        pickle.dump(all_chn_results, fp)

    return all_chn_results

