# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Mon 22 Jan 2018 05:28:20 PM CET
"""
import matplotlib
matplotlib.use('Agg')

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
#from openpyxl import Workbook
import numpy as np
import struct
import os
from sys import exit
import os.path
import math
#from matplotlib.backends.backend_pdf import PdfPages
from S1_raw_convertion_fft_M12 import fft_process_chn 
from S1_raw_convertion_fft_M12 import fft_process_chn_wib
from S1_raw_convertion_fft_M12 import fft_process_chn_apa 
from S1_raw_convertion_fft_M12 import fft_process_plot 
from timeit import default_timer as timer

#from one_chn_plot import one_chn_plot
#from fft_3d_plot import fft_3d_plot
#from fft_2d_plot import fft_2d_plot
#from all_chn_plot import all_chn_plot
#from bad_channels_mapping import bad_channels_mapping
#from S1_all_chn_results_filter import all_chn_results_filter

start = timer()

print "Start..."

import sys
rmsstrdate = sys.argv[1] #
rmsstrrun = sys.argv[2]  #
rmsstrstep = sys.argv[3]
strenv = sys.argv[4]
gainstrdate = sys.argv[5] #
gainstrrun = sys.argv[6]  #
gainstrstep =  sys.argv[7]
jumbo_flag = sys.argv[8]
server_flg = sys.argv[9]
apa = sys.argv[10]
chn= int(sys.argv[11])
FEMB = sys.argv[12]
WIB = sys.argv[13]
FEset = sys.argv[14]

if (gainstrstep[1] == "2" ):
    DAC_cs = "FPGADAC"
elif (gainstrstep[1] == "4" ):
    DAC_cs = "ASICDAC"

if (gainstrstep[0] == "3" ):
    gain = 3
    dac_np = [1,2,3,4]
elif (gainstrstep[0] == "1" ):
    gain = 2
    dac_np = [3,4,5,6,7]

if (jumbo_flag == "True"):
    jumbo_flag = True
else:
    jumbo_flag = False

femb_set = strenv + "step"

if (server_flg == "server" ):
    path_raw = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Rawdata_"+ rmsstrdate + "/" 
    path_gain = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Rawdata_"+ gainstrdate + "/" 
else:
    path_raw = "/Users/shanshangao/Documents/Share_Windows/CERN_test_stand/Rawdata/Rawdata_"+ rmsstrdate + "/" 
    path_gain = "/Users/shanshangao/Documents/Share_Windows/CERN_test_stand/Rawdata/Rawdata_"+ gainstrdate + "/"

from apa_mapping import apa_mapping

apa_yuv, apa_y, apa_v, apa_u = apa_mapping()

#chn= 83
#FEMB = "FEMB0"
#WIB = "WIB1"
#FEset = "_1E_"
print path_raw
print "run" + rmsstrrun
print WIB+femb_set+rmsstrstep

fft_process_chn(path_raw, onedir = WIB+femb_set+rmsstrstep, env = strenv, runno = "run" + rmsstrrun, FEMB = FEMB, chns = [chn], jumbo_flag = jumbo_flag, FEset = FEset, one_chn_flg = True)

#fft_process_chn(path, onedir = "step1", env = "RT", runno = "run01" , FEMB = "FEMB0", chns = [0], jumbo_flag = False, FEset = "_1E_", one_chn_flg = False)
#fft_process_chn_apa(path_raw, onedir = femb_set+rmsstrstep, env = strenv, runno = "run" + rmsstrrun,  chns = sorted(apa_u), jumbo_flag = jumbo_flag)
#f, psum = fft_process_chn_apa(path_raw, onedir = femb_set+rmsstrstep, env = strenv, runno = "run" + rmsstrrun,  chns = sorted(apa_u), jumbo_flag = jumbo_flag)
#fft_process_plot(path_raw, runno = "run" + rmsstrrun, f=f, psum=psum)
#fft_process_chn(path_raw, onedir = "WIB1"+femb_set+rmsstrstep, env = strenv, runno = "run" + rmsstrrun, FEMB = "FEMB0", chns = sorted(apa_u), jumbo_flag = jumbo_flag)
#fft_process_chn_wib(path_raw, onedir = "WIB1"+femb_set+rmsstrstep, env = strenv, runno = "run" + rmsstrrun,  chns = sorted(apa_u), jumbo_flag = jumbo_flag)
#fft_process_chn_apa(path_raw, onedir = "WIB1"+femb_set+rmsstrstep, env = strenv, runno = "run" + rmsstrrun,  chns = sorted(apa_u), jumbo_flag = jumbo_flag)


#step_info = [ 
#              [[rmsstrstep],[0,1,2,3],strenv, "WIB1"+femb_set+gainstrstep, gain, dac_np, DAC_cs, "run" + rmsstrrun, "run" + gainstrrun, "WIB1"+femb_set], 
#              [[rmsstrstep],[0,1,2,3],strenv, "WIB2"+femb_set+gainstrstep, gain, dac_np, DAC_cs, "run" + rmsstrrun, "run" + gainstrrun, "WIB2"+femb_set], 
#              [[rmsstrstep],[0,1,2,3],strenv, "WIB3"+femb_set+gainstrstep, gain, dac_np, DAC_cs, "run" + rmsstrrun, "run" + gainstrrun, "WIB3"+femb_set], 
#              [[rmsstrstep],[0,1,2,3],strenv, "WIB4"+femb_set+gainstrstep, gain, dac_np, DAC_cs, "run" + rmsstrrun, "run" + gainstrrun, "WIB4"+femb_set], 
#              [[rmsstrstep],[0,1,2,3],strenv, "WIB5"+femb_set+gainstrstep, gain, dac_np, DAC_cs, "run" + rmsstrrun, "run" + gainstrrun, "WIB5"+femb_set], 
#            ]
#
#psd = True
#
#for step_one_info in step_info:
#    path = path_raw + step_one_info[7] 
#    gainpath = path_gain + step_one_info[8] 
#    rms_step = step_one_info[9] 
#    gain = step_one_info[4] 
#    DACvalue =step_one_info[5] 
#    DAC = step_one_info[6]
#    env = step_one_info[2] 
#    step_np = []
#    print gainpath
##    exit()
#    for i in step_one_info[0]:
#        step_np.append ( rms_step + i )
#    
#    for femb in step_one_info[1]:
#        gain_step = step_one_info[3] #RT
#        for step in step_np:
#            #result_pdfpath = path + "\\" "FEMB%d"%femb + step + "_" + DAC + "_" + 'results.pdf'
#            result_pdfpath = path + "/" + "FEMB%d"%femb + step + "_" + DAC + "_" + 'results.pdf'
#            
#            save_cycle = 0
#            while (os.path.isfile(result_pdfpath)):
#                save_cycle = save_cycle + 1
#                #result_pdfpath = path + "\\" + "FEMB%d"%femb +  step + "_" + DAC + "_"  + 'results' + str(save_cycle)+'.pdf'
#                result_pdfpath = path + "/" + "FEMB%d"%femb +  step + "_" + DAC + "_"  + 'results' + str(save_cycle)+'.pdf'
#            print result_pdfpath
#            pp = PdfPages(result_pdfpath)
#            
#            
#            #raw data processing or import processed result
#            print "raw data processing or import processed result"
#            #readfile = path +"\\" + "FEMB%d"%femb +  step +  "_" + DAC + "_"+ "alldata_result.bin"
#            readfile = path +"/" + rms_step +  "FEMB%d"%femb +  step +  "_" + DAC + "_"+ "alldata_result_org.bin"
#            if os.path.isfile(readfile):
#                import pickle
#                with open (readfile, 'rb') as fp:
#                    all_chn_results = pickle.load(fp)
#            else:
#                all_chn_results = raw_convertion( path, gainpath, step_np = [step], env = env, femb=femb, psd = psd, rms_smps =100000, stuck_filter = True, \
#                            gain = gain, gain_step = gain_step, DAC = DAC, DACvalue = DACvalue, jumbo_flag = jumbo_flag, apa=apa)
#            print "time cost = %.3f seconds"%(timer()-start)
#
#            wib_ip = int(rms_step[3])
#            print wib_ip
#            apa40_yuv_f = bad_channels_mapping(wib_ip = wib_ip, femb_no=femb, env=env)
#            all_chn_results = all_chn_results_filter ( all_chn_results, apa40_yuv_f )
#            
#            print "Plots start..."
#            all_chn_plot (all_chn_results, pp, step, env, femb, psd, gain)
#            print "time cost = %.3f seconds"%(timer()-start)
#           
#           
#            for chn in range(128):
#                one_chn_plot (all_chn_results, chn,  pp, step, env, femb, psd, gain, DACvalue=DACvalue)
#                print "time cost = %.3f seconds"%(timer()-start)
#
#            x_range = [0, 1e6]
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 0, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 1, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 2, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 3, psd=psd, step=step, x_range=x_range, SF=True)
#            print "time cost = %.3f seconds"%(timer()-start)
#            
#            fft_3d_plot(all_chn_results, pp, femb = femb, tp = 0, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_3d_plot(all_chn_results, pp, femb = femb, tp = 1, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_3d_plot(all_chn_results, pp, femb = femb, tp = 2, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_3d_plot(all_chn_results, pp, femb = femb, tp = 3, psd=psd, step=step, x_range=x_range, SF=True)
#            print "time cost = %.3f seconds"%(timer()-start)
#            
#            x_range = [0, 2e5]
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 0, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 1, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 2, psd=psd, step=step, x_range=x_range, SF=True)
#            fft_2d_plot(all_chn_results, pp, femb = femb, tp = 3, psd=psd, step=step, x_range=x_range, SF=True)
#            print "time cost = %.3f seconds"%(timer()-start)
#          
#            pp.close()
#    print "DONE"
#
