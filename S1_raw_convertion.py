# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Nov 18 22:58:10 2018
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

def rms_process_chn(path, onedir = "step1", env = "RT", FEMB = "FEMB0",rms_smps =130000, jumbo_flag = False):

####    file_exist = os.path.exists( path + "\\" +onedir + "\\" + FEMB + "rms.xlsx")
####    if (file_exist):
####        os.remove( path + "\\" +onedir + "\\" + FEMB +  "rms.xlsx")
####
    #rms_data_dir = path + "\\" + onedir + "\\" 
    rms_data_dir = path + "/" + onedir + "/" 
    print rms_data_dir 

    for root, dirs, files in os.walk(rms_data_dir):
        break

    alldata = []
    for chip in range(8):
        for onefile in files:
            pos1 = onefile.find(FEMB)
            pos2 = onefile.find("_RMS")
            pos3 = onefile.find("_RMS")
            if (pos1 >= 0 ) and (pos2 >= 0) and (pos3 >= 0):
                chip_num = int(onefile[onefile.find("CHIP")+4])
                if  (chip_num ==chip):
                    rms_data_file = rms_data_dir + onefile
                    print rms_data_file
                    fileinfo  = os.stat(rms_data_file)
                    filelength = fileinfo.st_size
                    print filelength
                    with open(rms_data_file, 'rb') as f:
                        #raw_data = f.read(filelength)
                        raw_data = f.read()

                    print len(raw_data)
                    if ( filelength/2/16 > rms_smps ):
                        smps = rms_smps 
                        #smps = (filelength-1024)/2/16 
                    else:
                        smps = (filelength-1024)/2/16 

                    femb_num = int(onefile[onefile.find("FEMB")+4])
                    chip_num = int(onefile[onefile.find("CHIP")+4])
                    tp = int(onefile[onefile.find("CHIP")+6], 16)%0x3
                    print smps, femb_num, chip_num, tp
                    chn_data = raw_convertor(raw_data, smps, jumbo_flag)
                    alldata.append([femb_num, chip_num, tp, chn_data])
    return alldata 

def raw_convertion( path, gainpath, step_np = ["step001"], env = "RT", femb=0, psd = True, rms_smps =130000, stuck_filter = True, gain = 3, gain_step = "step11", DAC = "FPGADAC", DACvalue = [4,5,6,7,8,9,10,11], jumbo_flag = False, apa="ProtoDUNE", hp_fliter=False):
#gain = 3 --> 25mV/fC
    print "Start......"
    #gainfile_path = gainpath + "\\" +  gain_step + "\\" + "FEMB%d%sgain.xlsx"%(femb,DAC)
    gainfile_path = gainpath + "/" +  gain_step + "/" + "originalFEMB%d%sgain.xlsx"%(femb,DAC)
    print "Gain file path = %s" %gainfile_path
    for step in step_np:
        wb = Workbook()
        FEMBNO=str(femb)
        alldata = rms_process_chn(path, onedir=step, env=env, FEMB = "FEMB"+FEMBNO,rms_smps =rms_smps, jumbo_flag = jumbo_flag )
        print "All rawdata is read"
    ########################################################################################
        #savefile = path +"\\" + "FEMB%d"%femb +  step +  "_" + DAC + "_" + "alldata_result.bin"
        if (hp_fliter == True ):
            savefile = path +"/" + "FEMB%d"%femb +  step +  "_" + DAC + "_" + "alldata_result_flitered.bin"
        else:
            savefile = path +"/" + "FEMB%d"%femb +  step +  "_" + DAC + "_" + "alldata_result_org.bin"
        all_chn_results = raw_to_result(alldata, gainfile_path, savefile, apa=apa, step=step, femb=femb, psd=psd, env=env, gain=gain, DAC = DAC, DACvalue = DACvalue, stuck_filter = stuck_filter, hp_fliter=hp_fliter)
        print "All rawdata have been analysized"
    return all_chn_results


#path = "D:\\fft_code\\"
#raw_convertion( path , stepno_np = [106], env = "RT", femb=0, psd = True, gain = 3, gain_step = "step11")
