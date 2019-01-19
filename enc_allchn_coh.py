# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 10/10/2017 7:18:31 PM
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

####    def paras_sf_allchn( all_chn_results, coh_chn_np, tp_no,  paras=5, wire_type="All"):
####        #paras = 5: ped
####        #paras = 6: rms
####        #paras = 3: f for FFT
####        #paras = 4: p for FFT
####        #paras = 7: x for gain
####        #paras = 8: y for gain
####        #paras = 9: Gain
####        #wire_type = "Y": Y wire
####        #wire_type = "U": U wire
####        #wire_type = "V": V wire
####        #wire_type = "A": Any wire
####        #paras = 10: chn 
####        if paras == 10:
####            rms_cs = 0
####            par = 7
####        elif paras <= 6:
####            rms_cs = 0
####            par = paras
####        else:
####            rms_cs = 1
####            par = paras-6
####    
####    #    paras_tp_chn = []
####    #    stuck_type = "Small"
####    #    for tp_no in range(4):
####        paras_chn = []
####        #for chn in range(128):
####        for chn in coh_chn_np:
####            one_chn_tp = all_chn_results[chn][tp_no]
####            if (wire_type == "All")  :
####                if (  one_chn_tp[0][2]== "Y" ) or (  one_chn_tp[0][2]== "U" ) or (  one_chn_tp[0][2]== "V" ) :
####                    paras_chn.append(one_chn_tp[rms_cs][par])
####            elif (  one_chn_tp[0][2]== wire_type ) :
####                paras_chn.append(one_chn_tp[rms_cs][par])
####    
####    #        stuck_free = True 
####    #        if ( one_chn_tp[0][8] != stuck_type ):
####    #            stuck_free = False
####    ##        for tmp_tp in range(4):
####    ##            tmp_one_chn_tp = all_chn_results[chn][tmp_tp]
####    ##            if ( tmp_one_chn_tp[0][8] != stuck_type ):
####    ##                stuck_free = False
####    #            
####    #        if (wire_type == "All")  and (  stuck_free == True ):
####    #            paras_chn.append(one_chn_tp[rms_cs][par])
####    #        elif (  one_chn_tp[0][2]== wire_type ) and (  stuck_free == True ):
####    #            paras_chn.append(one_chn_tp[rms_cs][par])
####    #    paras_tp_chn.append(paras_chn)
####    
####    #    return paras_tp_chn
####        return paras_chn

def enc_allchn_coh( all_chn_results, coh_chn_np, tp_no,  wire_type="All"):
    chn_enc_np = []
    #for chn in range(128):
    for chn in coh_chn_np:
        one_chn_tp = all_chn_results[chn][tp_no]

        if (wire_type == "All") and ( one_chn_tp[0][8] != "Large" ):
            enc = one_chn_tp[2][6] * one_chn_tp[1][3]
            chn_enc_np.append([chn, enc])
#        elif (  one_chn_tp[0][2]== wire_type ):
#            enc = one_chn_tp[2][6] * one_chn_tp[1][3]
#            chn_enc_np.append([chn, enc])

    return chn_enc_np

def sf_enc_allchn_coh( all_chn_results, coh_chn_np, tp_no,  wire_type="All"):
    sf_chn_enc_np = []
    stuck_type = "Small"
    #for chn in range(128):
    for chn in coh_chn_np:
        one_chn_tp = all_chn_results[chn][tp_no]
        stuck_free = True 
        if ( one_chn_tp[0][8] != stuck_type ):
            stuck_free = False

        if (wire_type == "All")  and (  stuck_free == True ):
            if (  one_chn_tp[0][2]== "Y" ) or (  one_chn_tp[0][2]== "U" ) or (  one_chn_tp[0][2]== "V" ) :
                enc = one_chn_tp[2][6] * one_chn_tp[1][3]
                sf_chn_enc_np.append([chn, enc])
#        elif (  one_chn_tp[0][2]== wire_type ) and (  stuck_free == True ):
#            enc = one_chn_tp[2][6] * one_chn_tp[1][3]
#            sf_chn_enc_np.append([chn, enc])

    return sf_chn_enc_np

