# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Fri Sep 21 12:37:12 2018
"""

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
from matplotlib.backends.backend_pdf import PdfPages
from timeit import default_timer as timer

#from bad_channels_mapping import bad_channels_mapping
#from S1_all_chn_results_filter import all_chn_results_filter
from apa_mapping import APA_MAP
apamap = APA_MAP()
from femb_position import femb_position
from raw_convertor_m import raw_convertor_peak
from highpass_filter import hp_flt_applied
from highpass_filter import hp_FIR_applied

def All_FEMBs_results(path, rundir,  APA="ProtoDUNE", APAno =1,  gain=3, mode=0, wib_np = [0,1,2,3,4], tp=2, jumbo_flag = True, feed_freq = 500, hp_filter = False, t_no = 1):
    apamap.APA = APA
    runpath = path + rundir + "/"
    start = timer()
    for root, dirs, files in os.walk(runpath):
        break

    alldata = []
    allresult = []
    for wib in wib_np:
        wibinfo_rt = "WIB" + format(wib,"02d") + "step" + str(gain) + str(mode)  
        path_wib_rt = runpath + wibinfo_rt + "/"
        wibinfo_ln = "WIB" + format(wib,"02d") + "step" + str(gain) + str(mode)  
        path_wib_ln = runpath + wibinfo_ln + "/"
        missing_wib = False
        if os.path.isdir(path_wib_rt):
            wibinfo = wibinfo_rt
            path_wib = path_wib_rt
            #print "%s"%path_wib
        elif os.path.isdir(path_wib_ln):
            wibinfo = wibinfo_ln
            path_wib = path_wib_ln
            #print "%s"%path_wib
        else:
            path_wib = path_wib_ln
            print "%s, path doesn't exist!!!"%path_wib
            missing_wib = True

        if (missing_wib == False):
            for root1, dirs1, rawfiles in os.walk(path_wib):
                break
            print("APAno",APAno)
            femb_pos_np = femb_position(APAno)
            #print("femb_pos_np",femb_pos_np)
            apa_femb_loc, X_sort, V_sort, U_sort = apamap.apa_femb_mapping_pd()
            for rawfile in rawfiles:
                rawfilep = path_wib + rawfile
                #print("rawfilep",rawfilep)
                if (rawfilep.find(".bin") >= 0 ) and (rawfilep.find(wibinfo) >=0) :
                    wib  = int( rawfilep[(rawfilep.find("WIB") + 3):(rawfilep.find("WIB") + 5)])
                    femb = int( rawfilep[rawfilep.find("FEMB") + 4])
                    chip = int( rawfilep[rawfilep.find("CHIP") + 4])
                    filetp = int( rawfilep[rawfilep.find("CHIP") + 6])
                    if os.path.isfile(rawfilep) and (filetp==tp) :
                        with open(rawfilep, 'rb') as f:
                            raw_data = f.read()                
                            len_file = len(raw_data) 
                        for apa_loc in femb_pos_np:
                            if (apa_loc[1] == "WIB" + format(wib,"02d") + "_" + "FEMB" + str(femb) ):
                                break
                        smps = (len_file-1024)/2/16 
                        if (smps > 100000 ):
                            smps = 100000
                        elif (smps > 20000 ):
                            smps = 20000
                        elif (smps > 10000 ):
                            smps = 10000
                        else:
                            pass
                        chn_data, feed_loc, chn_peakp, chn_peakn = raw_convertor_peak(raw_data, smps, jumbo_flag)
                        for chn in range(16):
                            fembchn = chip*16+chn
                            for apa_info in apa_femb_loc:
                                if int(apa_info[1]) == fembchn :
                                    break

                            rms_data = []
                            for oneloc in feed_loc[0:-1]:
                                rms_data = rms_data + chn_data[chn][oneloc+100: oneloc+feed_freq]

                            if (hp_filter == True ):
                                flt_tmp_data = hp_flt_applied(chn_data[chn], fs = 2000000, passfreq = 1000, flt_order = 2)
                                flt_tmp_data = np.array(flt_tmp_data) + np.mean(rms_data)
                                rms_data_tmp = [] 
                                for oneloc in feed_loc[0:-1]:
                                    rms_data_tmp = rms_data_tmp + (flt_tmp_data[oneloc+100: oneloc+feed_freq].tolist() )
                                rms_data = rms_data_tmp
                                chn_full_data = flt_tmp_data
                            else:
                                rms_data = rms_data 
                                chn_full_data = chn_data[chn]

                            rms_data_raw = rms_data 

                            rms_len = len(rms_data)
                            raw_rms0  = np.std (rms_data[0: int(rms_len/2)])
                            raw_rms1  = np.std (rms_data[int(rms_len/2): rms_len])
                            if (raw_rms0 < raw_rms1):
                                rms_data = rms_data[0: int(rms_len/2)]
                            else:
                                rms_data = rms_data[ int(rms_len/2): rms_len ]
                            raw_mean = np.mean(rms_data)
                            raw_rms  = np.std (rms_data)
 
                            sf_raw_rms = []
                            for tmp in rms_data:
                                if ( tmp % 64 == 63 ) or ( tmp % 64 == 0 ) or ( tmp % 64 == 1 ) or ( tmp % 64 == 62 )  or ( tmp % 64 == 2 ):
                                    pass
                                else:
                                    sf_raw_rms.append(tmp)
                            if (len(sf_raw_rms) > 2 ):
                                sf_mean = np.mean(sf_raw_rms)
                                sf_rms  = np.std(sf_raw_rms)
                            else:
                                sf_rms = raw_rms
                                sf_mean = raw_mean
                            sf_ratio = (len(sf_raw_rms))*1.0/(len(rms_data) )

                            chn_peakp_avg = np.mean(chn_peakp[chn])
                            chn_peakn_avg = np.mean(chn_peakn[chn])
                            alldata.append( [apa_loc, apa_info, wib, femb, chip, \
                                             chn, raw_mean, raw_rms, sf_mean, sf_rms, \
                                             sf_ratio, chn_peakp_avg, chn_peakn_avg, rms_data_raw, chn_full_data, \
                                             feed_loc, chn_peakp[chn], chn_peakn[chn] ] )

                            pulsemax_data = np.max(chn_full_data[feed_loc[0]:feed_loc[0]+100])
                            pulsemax_data_loc =np.where ( chn_full_data[feed_loc[0]:feed_loc[0]+100] == pulsemax_data)
                            ppeak_oft_feed = pulsemax_data_loc[0][0] 

                            pulsemin_data = np.min(chn_full_data[feed_loc[0]:feed_loc[0]+100])
                            pulsemin_data_loc =np.where ( chn_full_data[feed_loc[0]:feed_loc[0]+100] == pulsemin_data)
                            npeak_oft_feed = pulsemin_data_loc[0][0]

                            allresult.append( [apa_loc[0], apa_loc[1], apa_info[0], apa_info[1], apa_info[2], apa_info[3], \
                                               wib, femb, chip, chn, \
                                               raw_mean, raw_rms, len(rms_data), \
                                               sf_mean, sf_rms, len(sf_raw_rms), sf_ratio, \
                                               chn_peakp_avg, chn_peakn_avg, ppeak_oft_feed, npeak_oft_feed ] )
            print "time passed = %d"% (timer()-start)

    import pickle
    resultpath = path + "results/" + rundir + "/" 

    if (os.path.exists(resultpath)):
        pass
    else:
        try: 
            os.makedirs(resultpath)
        except OSError:
            print "Error to create a folder"
            exit()

    savefile = resultpath +  apamap.APA + "_APA" + str(APAno) + '_gain' + str(gain) + "_tp" + str(tp) + '_results.bin'
    if (os.path.isfile(savefile)): 
        pass
    else:
        with open(savefile, "wb") as fp:
            pickle.dump(allresult, fp)

    if gain == 3:
        str_gain = 25.0
        egain = 78 
    elif gain == 1:
        str_gain = 14.0 
        egain = 145 
    elif gain == 2:
        str_gain = 7.8 
        egain = 250
    elif gain == 0:
        str_gain = 4.7 
        egain = 425
    
    if tp == 3:
        str_tp = 2.0
    elif tp == 1:
        str_tp = 3.0 
    elif tp == 2:
        str_tp = 0.5 
    elif tp == 0:
        str_tp = 1.0 
    
    item_n = ["APA_LOC", "WIB_FEMB", "Wire", "FEMBchn(0-127)", "FEMBasic(1-8)", "ASICchn(0-15)", \
              "WIB(0-4)", "FEMB(0-4)", "ASIC(0-7)", "ASICchn(0-15)", \
              "Baseline (Raw data) \ bin", "RMS(raw data) \ bin", "Sample count (raw data)", \
              "Baseline (SF data) \ bin", "RMS(SF data) \ bin", "Sample count (SF data)", "SF ratio", \
              "Pos_Amplitude \ bin", "Neg_Amplitude \ bin", "1st_PPeak_LOC \ bin", "1st_NPeak_LOC \ bin", \
              "Gain \ mV/fC", "Shape Time / us", "Inverted gain \ e-/bin" ]
    
    fe_paras = [str_gain, str_tp, egain]
    strdate_pos =resultpath.find("Rawdata_")
    strdate =resultpath[strdate_pos: strdate_pos+18]
    csvfile = resultpath + "Test" + format(t_no, "03d") + "_" + strdate + "_" + rundir + "_" + apamap.APA + "_APA" + str(APAno) + '_gain' + str(gain) + "_tp" + str(tp) + '_results.csv'
    
    with open (csvfile, 'w') as fp:
        fp.write(",".join(str(i) for i in item_n) + "," + "\n")
        for x in allresult:
            fp.write(",".join(str(i) for i in x) + ","  + ",".join(str(i) for i in fe_paras) + "," + "\n")


    return alldata

