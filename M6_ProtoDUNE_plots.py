# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sat Nov 18 17:23:37 2017
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
from matplotlib.backends.backend_pdf import PdfPages
from timeit import default_timer as timer

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

from bad_channels_mapping import bad_channels_mapping
from S1_all_chn_results_filter import all_chn_results_filter
from apa_mapping import apa_femb_mapping
from femb_position import femb_position




def APA_sort():
    femb_pos_np = femb_position()
    All_sort, X_sort, V_sort, U_sort = apa_femb_mapping()
    APA_sort = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_sort.append([femb_pos, All_sort])

    APA_X_sort = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_X_sort.append([femb_pos, X_sort])
    
    APA_V_sort = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_V_sort.append([femb_pos, V_sort])
    
    APA_U_sort = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_U_sort.append([femb_pos, U_sort])

    return APA_sort, APA_X_sort, APA_V_sort, APA_U_sort 

def rms_plot(ax, apa_results, sort_np, tp = 1, sf = True, enc_y = [0, 2000], adc_y = [0, 25]):
    rmsadc_np = []
    rmsenc_np = []
    for onefemb in sort_np:
        for femb_result in apa_results:
            if femb_result[0][0] == onefemb[0][0] : #find femb
                print onefemb[0][0]
                break
        if len(onefemb[1]) == 128 :
            wiretype = "ALL"
        elif onefemb[1][0][0][0] == "X" :
            wiretype = "X"   
        elif onefemb[1][0][0][0] == "V" :
            wiretype = "V"  
        elif onefemb[1][0][0][0] == "U" :
            wiretype = "U"
        for chn_info in onefemb[1]: #find chn
            for chn_result in femb_result[1]:
                #if chn_result[0][0] == chn_info[0] :
                if chn_result[0] == chn_info :
                    print chn_result[0] , chn_info 
                    break
            if (sf == True):
                rmsadc_np.append(chn_result[1][tp][3])
                rmsenc_np.append(chn_result[1][tp][3] *chn_result[1][tp][5]  )
            else:                                                       
                rmsadc_np.append(chn_result[1][tp][1])                  
                rmsenc_np.append(chn_result[1][tp][1] *chn_result[1][tp][5]  )

    x_np = np.arange(len(rmsadc_np))
    print len(rmsadc_np)
    rmsadc_np = np.array(rmsadc_np)
    if wiretype == "X":
        color = "g"
    elif wiretype == "U":
        color = "b"
    elif wiretype == "V":
        color = "r"
    else:
        color = "m"

    ax.scatter (x_np, rmsadc_np, color = color)
    ax.plot (x_np, rmsadc_np, color = color)

    ax.show()
    ax.scatter (x_np, rmsenc_np, color = color)
    ax.plot (x_np, rmsenc_np, color = color)

    ax.show()
    ax.close()

start = timer()

print "Start..."

path = "F:/CERN_backup/CERN_test_stand_by1022/Rawdata/Rawdata_1019/run01/"

result_pdfpath = path +  "ProtoDUNE_APA_" + 'results.pdf'
save_cycle = 0
while (os.path.isfile(result_pdfpath)):
    save_cycle = save_cycle + 1
    result_pdfpath = path + "ProtoDUNE_APA_"  + 'results' + str(save_cycle)+'.pdf'
pp = PdfPages(result_pdfpath)

readfile = path + "ProtoDUNE_APA__results.bin"
if os.path.isfile(readfile):
    import pickle
    with open (readfile, 'rb') as fp:
        apa_results = pickle.load(fp)
else:
    print "ProtoDUNE_APA__results.bin doesn't exist"
    exit()


fig = plt.figure(figsize=(16,9))

APA_sort, APA_X_sort, APA_V_sort, APA_U_sort = APA_sort()
rms_plot(plt, apa_results, APA_U_sort, tp = 2, sf = True, enc_y = [0, 2000], adc_y = [0, 25])



