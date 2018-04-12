# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Thu Apr 12 15:46:53 2018
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
import numpy as np
import math
from fft_chn import chn_rfft, chn_rfft_psd, chn_fft, chn_fft_psd
from apa_mapping import APA_MAP
from highpass_filter import hp_flt_applied
from highpass_filter import hp_FIR_applied

def one_chn_result(yuv_data_in, chn, apa= "ProtoDUNE", femb = 0, tp = 1, psd = True, step="step001", stuck_filter = True, env = "RT", hp_fliter = False):
    APAMAP = APA_MAP()
    APAMAP.APA = apa
    [yuv_chndata, y_chndata, v_chndata, u_chndata] =yuv_data_in 
    apa_yuv, apa_y, apa_v, apa_u = APAMAP.apa_mapping()

    wire_type = "B"
    y_wire = np.where(chn == np.array(apa_y))
    if (len(y_wire[0]) > 0 ):
        if (apa_y[y_wire[0][0]] == chn):
            wire_type = "Y"
    u_wire = np.where(chn == np.array(apa_u))
    if (len(u_wire[0]) > 0 ):
        if (apa_u[u_wire[0][0]] == chn):
            wire_type = "U"
    v_wire = np.where(chn == np.array(apa_v))
    if (len(v_wire[0]) > 0 ):
        if (apa_v[v_wire[0][0]] == chn):
            wire_type = "V"

    onechn_data = yuv_chndata[chn]

    stuck_type = "Small"
    len_tmp_data = 0 
    if (stuck_filter == True):
        tmp_data = []
        lenonechn_data = len(onechn_data)
        for tmp in onechn_data:
            
            if ( tmp % 64 == 63 ) or ( tmp % 64 == 0 ) or ( tmp % 64 == 1 ) or ( tmp % 64 == 62 )  or ( tmp % 64 == 2 ):
                pass
            else:
                tmp_data.append(tmp)
        len_tmp_data = len(tmp_data)
        #if (len_tmp_data > (lenonechn_data//100)):
        if (len_tmp_data >= 100000 ):
            if (len_tmp_data > lenonechn_data*0.95 ):
                stuck_type = "Small"
            else:
                if (env == "RT"):
                    stuck_type = "Small"
                else:
                    stuck_type = "Middle"

            if (hp_fliter == True ):
                flt_tmp_data = hp_flt_applied(tmp_data, fs = 2000000, passfreq = 1000, flt_order = 3)
                flt_tmp_data = np.array(flt_tmp_data) +  np.mean(tmp_data)
                rms =  np.std(flt_tmp_data[0:100000])
                ped_mean = np.mean(flt_tmp_data[0:100000])
            else:
                rms =  np.std(tmp_data[0:100000])
                ped_mean = np.mean(tmp_data[0:100000])

#            co_onechn_data = tmp_data[0:100000]
        else:
            rms =  np.std(onechn_data)
            ped_mean = np.mean(onechn_data)
            stuck_type = "Large"
#            co_onechn_data = onechn_data[0:100000]

    else:
        rms =  np.std(onechn_data)
        ped_mean = np.mean(onechn_data)
#        co_onechn_data = onechn_data[0:100000]

    if (psd == True):
        if (hp_fliter == True ) and ( len_tmp_data >= 100000 ):
            f,p = chn_rfft_psd(flt_tmp_data, fft_s = 2000, avg_cycle = 50)
            onechn_data = flt_tmp_data
        else:
            f,p = chn_rfft_psd(onechn_data, fft_s = 2000, avg_cycle = 50)
            onechn_data = onechn_data
    else:
        f,p = chn_rfft(onechn_data, fft_s = 2000, avg_cycle = 50)
        onechn_data = onechn_data

    return step, onechn_data[0:100000], wire_type, f, p, ped_mean, rms, chn, stuck_type #, co_onechn_data

