# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Thu Nov 23 14:51:55 2017
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
from fft_chn import chn_rfft, chn_rfft_psd, chn_fft, chn_fft_psd

from scipy.optimize import curve_fit

def gaussian(x, a, mean, sigma):
    return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

def all_chn_results_coherent ( all_chn_results, apa40_yuv_f, coherent_chn_np, coh_mode = 1):
    ##coh_mode = 1 --> middle value of chns
    ##coh_mode = 2 --> mean value of chns
    ##coh_mode = 3 --> histogram peak value of chns
    ##coh_mode = 4 --> sum value of chns
    coh_tp_chn_data = []
    for tp_fe in [1,0,3,2]:
        coh_chn_data = []
        for chn in range(128):
            coh_chn = np.where(chn == np.array(coherent_chn_np))
            bad_chn = np.where(chn == np.array(apa40_yuv_f))
            if( len(coh_chn[0])> 0) and ( len(bad_chn[0]) <= 0 ):
                if (all_chn_results[chn][tp_fe][0][8] != "Large" ):
                    ped_mean = all_chn_results[chn][tp_fe][0][5]
                    raw_sub_ped = np.array(all_chn_results[chn][tp_fe][0][1]) - ped_mean
                    coh_chn_data.append([chn,tp_fe,raw_sub_ped])
        coh_num = len(coh_chn_data)
        smps = len(coh_chn_data[0][2])
        coh_noise = []
        coh_noise_raw = []
        for smpsi in range(smps):
            tmpa = []
            coh_sum = 0
            for i in range(coh_num):
                tmpa.append(coh_chn_data[i][2][smpsi])
                coh_sum = coh_sum + coh_chn_data[i][2][smpsi]
            tmpa.sort()
            mid_tmpa = tmpa[len(tmpa)//2 + len(tmpa)%2]
            mean_tmpa = np.mean(tmpa)
            std_tmpa = np.std(tmpa)
            mintmp = int(np.min(tmpa))
            maxtmp = int(np.max(tmpa))

            yhist, xhist = np.histogram(tmpa, bins='sturges' )
            xh_pos = np.where(yhist > 0)[0]
            if ( len(xh_pos) > 0 ):
                xh = xhist[xh_pos]
                yh = yhist[xh_pos]
                yhmax = np.max(yh)
                yhmax_pos = np.where(yh == yhmax)[0]
                max_hist_v_all = xh[yhmax_pos]
                max_hist_v = np.max(max_hist_v_all)
                try:
                    popt, pcov = curve_fit(gaussian, xh, yh)
                    mean_from_fit = popt[1]
                except RuntimeError:
                    mean_from_fit = mean_tmpa
            else:
                max_hist_v = mean_tmpa
                mean_from_fit = mean_tmpa

            if (coh_mode == 1):
                coh_noise.append(mid_tmpa)
            elif(coh_mode == 2):
                coh_noise.append(mean_tmpa)
            elif(coh_mode == 3):
                coh_noise.append(max_hist_v)
            elif(coh_mode == 4):
                coh_noise.append(coh_sum)
            elif(coh_mode == 5):
                coh_noise.append(coh_sum/(coh_num))
            elif(coh_mode == 6): #no use
                coh_noise.append(mean_from_fit)
            else:
                coh_noise.append(mid_tmpa)

            coh_noise_raw.append(tmpa) 

        coh_noise = np.array(coh_noise)

        for i in range(coh_num):
            raw_sub_coh = coh_chn_data[i][2]-coh_noise

            psd = True
            if (psd == True):
                 f1,p1 = chn_rfft_psd(coh_chn_data[i][2], fft_s = 2000, avg_cycle = 50)
                 f2,p2 = chn_rfft_psd(raw_sub_coh, fft_s = 2000, avg_cycle = 50)
                 f3,p3 = chn_rfft_psd(coh_noise, fft_s = 2000, avg_cycle = 50)
            else:
                 f1,p1 = chn_rfft(coh_chn_data[i][2], fft_s = 2000, avg_cycle = 50)
                 f2,p2 = chn_rfft(raw_sub_coh, fft_s = 2000, avg_cycle = 50)
                 f3,p3 = chn_rfft(coh_noise, fft_s = 2000, avg_cycle = 50)
            rms1 = np.std(coh_chn_data[i][2])
            rms2 = np.std(raw_sub_coh)
            rms3 = np.std(coh_noise)
            print "before %.3f, after %.3f, coherent %.3f"%(rms1, rms2, rms3)

            coh_tp_chn_data.append([coh_chn_data[i][0], coh_chn_data[i][1], coh_chn_data[i][2], raw_sub_coh, coh_noise, \
                                    rms1, rms2, rms3, f1, p1, f2, p2, f3, p3])

    tmp = []
    for chn in range(128):
        tmp_2 = []
        for tp_fe in [1,0,3,2]:
            tmp_2.append([])
        tmp.append(tmp_2)

    for tp_fe in [1,0,3,2]:
        for chn in range(128):
            one_chn_tp =  all_chn_results[chn][tp_fe]
            coh_chn = np.where(chn == np.array(coherent_chn_np))
            bad_chn = np.where(chn == np.array(apa40_yuv_f))
            if( len(coh_chn[0])> 0) and ( len(bad_chn[0]) <= 0 ):
                for tmpi in coh_tp_chn_data:
                    if (tmpi[0] ==chn) and (tmpi[1] == tp_fe):
                        one_chn_tp.append(tmpi)
                        tmp[chn][tp_fe] = one_chn_tp
#                        print "coherent for %d, %d"%(tmpi[0], tmpi[1])
            else:
                tmp[chn][tp_fe] = one_chn_tp

    all_chn_results = tmp
    return all_chn_results


#    coh_tmp = [] 
#    coh_chn_np = []
#
#    coh_tmp = [] 
#    coh_chn_np = []
#    for tp_fe in [1,0,3,2]:
#        for chn in range(128):
#            coh_chn = np.where(chn == np.array(apa40_yuv_f))
#            bad_chn = np.where(chn == np.array(apa40_yuv_f))
#            if( len(coh_chn[0])> 0) and ( len(bad_chn[0]) <= 0 ):
#                if (all_chn_results[chn][tp_fe][0][8] != "Large" )
#                    ped_mean = all_chn_results[chn][tp_fe][0][6]
#                    raw_no_ped = np.array(all_chn_results[chn][tp_fe][0][1]) - ped_mean
#            else
#                tmp[chn][tp_fe] = all_chn_results[chn][tp_fe]
#
#
#
#                coh_tmp.append(all_chn_results[chn])
#                coh_chn_np.append(chn)
#
#    for tp_fe in [1,0,3,2]:
#        for chn in coh_chn_np:
#
#
#
#
#    tmp = []
#    for chn in range(128):
#        tmp_2 = []
#        for tp_fe in [1,0,3,2]:
#            tmp_2.append([])
#        tmp.append(tmp_2)
#
#    for chn in range(128):
#        bad_wire = False 
#        bad_chn = np.where(chn == np.array(apa40_yuv_f))
#        if (len(bad_chn[0]) > 0 ):
#            bad_wire = True 
#        else:
#            bad_wire = False 
#
#        for tp_fe in [1,0,3,2]:
#            one_chn_tp =  all_chn_results[chn][tp_fe]
#
#            if (bad_wire == True ):
#                i_array = []
#                for i in range(len(one_chn_tp)):
#                    j_array =[]
#                    for j in range(len(one_chn_tp[i])):
#                        if ( i == 0 ):
#                            if ( j == 2 ):
#                                j_array.append("B" + one_chn_tp[i][j] )
#                            else:
#                                j_array.append( one_chn_tp[i][j] )
#                        else:
#                            j_array.append( one_chn_tp[i][j] )
#                    i_array.append(j_array)
#                tmp[chn][tp_fe] = i_array
#            else:
#                tmp[chn][tp_fe] = one_chn_tp
#    all_chn_results = tmp
#    return all_chn_results

