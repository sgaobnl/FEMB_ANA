# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 1/17/2019 3:05:07 PM
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl

import matplotlib
matplotlib.use('Agg')

from openpyxl import Workbook
import numpy as np
import struct
import os
from sys import exit
import os.path
import math
from matplotlib.backends.backend_pdf import PdfPages
from S1_raw_convertion_brombreg import raw_convertion 
from timeit import default_timer as timer

from one_chn_plot_coh_filter import one_chn_plot_coh_filter
from one_chn_plot import one_chn_plot
from fft_3d_plot import fft_3d_plot
from fft_2d_plot import fft_2d_plot
from all_chn_plot import all_chn_plot
from all_chn_plot_pre_coh import all_chn_plot_pre_coh
from all_chn_plot_coh import all_chn_plot_coh
from bad_channels_mapping import bad_channels_mapping
from S1_all_chn_results_filter import all_chn_results_filter
from S1_all_chn_results_coherent import all_chn_results_coherent
from apa_mapping import APA_MAP
apa_map = APA_MAP()

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
intcoh_mode = int(sys.argv[10])
apa = sys.argv[11]
wire_type = sys.argv[12]
regulators = sys.argv[13]

All_chns, X_chns, V_chns, U_chns = apa_map.apa_mapping()

if ( (wire_type == "X") or (wire_type == "Y") ):
    coh_chn_np = sorted(X_chns)
elif (wire_type == "V") :
    coh_chn_np = sorted(V_chns)
elif (wire_type == "U") :
    coh_chn_np = sorted(U_chns)
else:
    #coh_chn_np = sorted(All_chns)
    coh_chn_np = All_chns
    print coh_chn_np

coh_chn_num = len(coh_chn_np)
if ( regulators == "A") :
    coh_chn_np = coh_chn_np 
elif ( regulators == "L") :
    coh_chn_np = coh_chn_np[0: coh_chn_num//2]
elif ( regulators == "R") :
    coh_chn_np = coh_chn_np[coh_chn_num//2 : coh_chn_num] 
elif ( regulators == "C") :
    coh_chn_np = coh_chn_np[16:32] 
    print coh_chn_np

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

#femb_set = strenv + "step"
femb_set = "step"

if (server_flg == "server" ):
    path_raw = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Rawdata_"+ rmsstrdate + "/" 
    path_gain = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Rawdata_"+ gainstrdate + "/" 
else:
    path_raw = "D:/SBND_40APA/Rawdata/Rawdata_" + rmsstrdate + "/" 
    path_gain = "D:/SBND_40APA/Rawdata/Rawdata_" + gainstrdate + "/"

step_info = [ 
              [[rmsstrstep],[0,1,2,3],strenv, "WIB00"+femb_set+gainstrstep, gain, dac_np, DAC_cs, "run" + rmsstrrun, "run" + gainstrrun, "WIB00"+femb_set, intcoh_mode], 
            ]

psd = True

for step_one_info in step_info:
    path = path_raw + step_one_info[7] 
    #path = path_raw  
    gainpath = path_gain + step_one_info[8] 
    rms_step = step_one_info[9] 
    gain = step_one_info[4] 
    DACvalue =step_one_info[5] 
    DAC = step_one_info[6]
    env = step_one_info[2] 
    coh_mode = step_one_info[10] 
    ##coh_mode = 1 --> middle value of chns
    ##coh_mode = 2 --> mean value of chns
    ##coh_mode = 3 --> histogram peak value of chns
    ##coh_mode = 4 --> sum value of chns
    ##coh_mode = 5 --> sum value of chns/ chns number

    print env
    step_np = []
    for i in step_one_info[0]:
        step_np.append ( rms_step + i )
    
    for femb in step_one_info[1]:
        gain_step = step_one_info[3] #RT
        for step in step_np:
            result_pdfpath = path + "/" + "coh_" + "%d"%(coh_chn_np[0]) +"_FEMB%d"%femb + step + "_" + DAC + "_" + "mode" + "%d"%coh_mode + '_results.pdf'
            
            save_cycle = 0
            while (os.path.isfile(result_pdfpath)):
                save_cycle = save_cycle + 1
                result_pdfpath = path + "/" + "coh_" + "%d"%(coh_chn_np[0]) + "_FEMB%d"%femb + step + "_" + DAC + "_" + "mode" + "%d"%coh_mode + "_results" + str(save_cycle)+'.pdf'
            print result_pdfpath
            pp = PdfPages(result_pdfpath)
            
            #raw data processing or import processed result
            print "raw data processing or import processed result"
#            readfile = path +"/" + "FEMB%d"%femb +  step +  "_" + DAC + "_"+ "alldata_result.bin"
#            if os.path.isfile(readfile):
#                import pickle
#                with open (readfile, 'rb') as fp:
#                    all_chn_results = pickle.load(fp)
#            else:
            if (True):
                all_chn_results = raw_convertion( path, gainpath, step_np = [step], env = env, femb=femb, psd = psd, rms_smps =100000, stuck_filter = True, \
                            gain = gain, gain_step = gain_step, DAC = DAC, DACvalue = DACvalue, apa= apa )
            print "time cost = %.3f seconds"%(timer()-start)

            wib_ip = int(rms_step[3])
            apa40_yuv_f = bad_channels_mapping(wib_ip = wib_ip, femb_no=femb, env=env)
            all_chn_results = all_chn_results_filter ( all_chn_results, apa40_yuv_f )

            save_cohfile = path +"/" + "coh_" + "%d"%(coh_chn_np[0]) + "FEMB%d"%femb +  step +  "_" + DAC + "_"+ "mode" + "%d"%coh_mode + "alldata_result.bin"
            valid_coh_chn_np = []
            for vchn in coh_chn_np:
                tmp = np.where(vchn == np.array(apa40_yuv_f))
                if (len(tmp[0]) <= 0 ):
                    t05 =  all_chn_results[vchn][0][0][8]
                    t10 =  all_chn_results[vchn][1][0][8]
                    t20 =  all_chn_results[vchn][2][0][8]
                    t30 =  all_chn_results[vchn][3][0][8]
                    if ( t05 != "Large" ) and ( t10 != "Large" ) and ( t20 != "Large" ) and ( t30 != "Large" ):
                        valid_coh_chn_np.append(vchn)

            if (len(valid_coh_chn_np) < 2):
                print "ERROR: there is not enough channels to caculation coherent noise"
                exit()
            else:
                print valid_coh_chn_np

            if os.path.isfile(save_cohfile):
                import pickle
                with open (save_cohfile, 'rb') as fp:
                    all_chn_results = pickle.load(fp)
            else:
                all_chn_results = all_chn_results_coherent ( all_chn_results,apa40_yuv_f, valid_coh_chn_np, coh_mode = coh_mode )
                import pickle
                with open(save_cohfile, 'wb') as fp:
                    pickle.dump(all_chn_results, fp)

            
            print "Plots start..."
            #for vchn in valid_coh_chn_np:
            #    print vchn, len(all_chn_results[vchn]) , len(all_chn_results[vchn][0]) , len(all_chn_results[vchn][1]) , len(all_chn_results[vchn][2]) , len(all_chn_results[vchn][3])

            pre_encfile = path +"/" + "pre__coh_" + "%d"%(coh_chn_np[0]) + "FEMB%d"%femb +  step +  "_" + DAC + "_"+ "mode" + "%d"%coh_mode + ".enc"
            post_encfile = path +"/" + "post_coh_" + "%d"%(coh_chn_np[0]) + "FEMB%d"%femb +  step +  "_" + DAC + "_"+ "mode" + "%d"%coh_mode + ".enc"

            all_chn_plot_pre_coh (pre_encfile, all_chn_results, valid_coh_chn_np, pp, step, env, femb, psd, gain)
            all_chn_plot_coh     (post_encfile, all_chn_results, valid_coh_chn_np, pp, step, env, femb, psd, gain)
            print "time cost = %.3f seconds"%(timer()-start)
           
           
            for chn in valid_coh_chn_np:
                one_chn_plot_coh_filter (all_chn_results, chn,  pp, step, env, femb, psd, gain, DACvalue=DACvalue)
                print "time cost = %.3f seconds"%(timer()-start)

            for chn in valid_coh_chn_np:
                one_chn_plot (all_chn_results, chn,  pp, step, env, femb, psd, gain, DACvalue=DACvalue)
                print "time cost = %.3f seconds"%(timer()-start)

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
            print "time cost = %.3f seconds"%(timer()-start)
          
            pp.close()
    print "DONE"

