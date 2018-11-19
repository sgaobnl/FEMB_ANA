# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 4/23/2017 9:41:28 AM
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
from openpyxl import Workbook
import numpy as np
import struct
import os
from sys import exit
import os.path
import math
import statsmodels.api as sm

def all_chn_results_filter ( all_chn_results, apa40_yuv_f):
    tmp = []
    for chn in range(128):
        tmp_2 = []
        for tp_fe in [1,0,3,2]:
            tmp_2.append([])
        tmp.append(tmp_2)

    for chn in range(128):
        bad_wire = False 
        bad_chn = np.where(chn == np.array(apa40_yuv_f))
        if (len(bad_chn[0]) > 0 ):
            bad_wire = True 
        else:
            bad_wire = False 

        for tp_fe in [1,0,3,2]:
            one_chn_tp =  all_chn_results[chn][tp_fe]

            if (bad_wire == True ):
                i_array = []
                for i in range(len(one_chn_tp)):
                    j_array =[]
                    for j in range(len(one_chn_tp[i])):
                        if ( i == 0 ):
                            if ( j == 2 ):
                                j_array.append("B" + one_chn_tp[i][j] )
                            else:
                                j_array.append( one_chn_tp[i][j] )
                        else:
                            j_array.append( one_chn_tp[i][j] )
                    i_array.append(j_array)
                tmp[chn][tp_fe] = i_array
            else:
                tmp[chn][tp_fe] = one_chn_tp
    all_chn_results = tmp
    return all_chn_results

