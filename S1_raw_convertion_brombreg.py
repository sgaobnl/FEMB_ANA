# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 1/17/2019 3:06:08 PM
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
from raw_convertor_m import raw_convertor 
from raw_to_result import raw_to_result

def rms_process_chn_bb(path,  wb, step = "step1", gain = 3, env = "RT", FEMB = "FEMB0",rms_smps =130000):
    if path[-1] != "/":
        file_dir = path + "/"
    else:
        file_dir = path 
        
    print path
    for root, dirs, files in os.walk(path):
        break

    for onefile in files:
        if ( onefile.find(step+FEMB) >= 0 ) and ( onefile.find(FEMB) >= 0 ) and ( onefile.find(".bin") >= 0 ) and ( onefile.find("coh_") < 0 ): 
            pos = onefile.find(step+FEMB)
            fe_cfg = onefile[pos + len(step+FEMB)+ 2]
            break
    fe_cfg =  (gain <<2 ) + ((int(fe_cfg,16)) & 0x03)
    print fe_cfg
    filename_np = []
    for tp in range(4):
        filename_np.append(step+FEMB+"_"+ ('{:1X}'.format(tp)) + ('{:1X}'.format(fe_cfg)))

    alldata = []
    for filename in filename_np :
        file_path = file_dir + filename +".bin"
        print "loading %s, take a while"%file_path
        if os.path.isfile(file_path):
            import pickle
            with open (file_path, 'rb') as fp:
                femb_raw = pickle.load(fp)
        else:
            print "file doesn't exist"
            exit()

        femb_num = int(FEMB[-1])
        tp = int(filename[-2])
        for chip in range(8):
            chn_data = femb_raw[chip*16: (chip+1)*16]
            alldata.append([femb_num, chip, tp, chn_data])
    return alldata 

def raw_convertion( path, gainpath, step_np = ["step001"], env = "RT", femb=0, psd = True, rms_smps =130000, stuck_filter = True, gain = 3, gain_step = "step11", DAC = "FPGADAC", DACvalue = [4,5,6,7,8,9,10,11], apa="ProtoDUNE"):
    print "Start......"
    gainfile_path = gainpath + "/" +  gain_step + "/" + "originalFEMB%d%sgain.xlsx"%(femb,DAC)
    print "Gain file path = %s" %gainfile_path
    for step in step_np:
        wb = Workbook()
        FEMBNO=str(femb)
        alldata = rms_process_chn_bb(path, wb, step=step, gain = gain, env=env, FEMB = "FEMB"+FEMBNO, rms_smps =rms_smps )
        print "All rawdata is read"
    ########################################################################################
        savefile = path +"/" + "FEMB%d"%femb +  step +  "_" + DAC + "_" + "alldata_result.bin"
        all_chn_results = raw_to_result(alldata, gainfile_path, savefile, apa=apa, step=step, femb=femb, psd=psd, env=env, gain=gain, DAC = DAC, DACvalue = DACvalue, stuck_filter = stuck_filter)
        print "All rawdata have been analysized"
    return all_chn_results


#path = "D:\\fft_code\\"
#raw_convertion( path , stepno_np = [106], env = "RT", femb=0, psd = True, gain = 3, gain_step = "step11")
