# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Thu Jul 19 22:37:47 2018
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
import sys
import os.path
import math

import multiprocessing as mp
from chn_plot_out import plot_a_chn
from apa_mapping import APA_MAP
apamap = APA_MAP()



if __name__ == '__main__':
    APAno = int(sys.argv[1])
    rmsdate = sys.argv[2]
    fpgdate = sys.argv[3]
    asidate = sys.argv[4]
    rmsrunno = sys.argv[5]
    fpgarunno = sys.argv[6]
    asicrunno = sys.argv[7]
    apafolder = sys.argv[8]
    tpcchn_no  = int(sys.argv[9])

    tpcinfo = apamap.mapping_rd()
    for onechn in tpcinfo:
        if int(onechn[0]) == int(tpcchn_no):
            wibno  = int(onechn[10])
            fembno = int(onechn[9]) % 4
            chnno  = int(onechn[8])

    #if (apafolder == "APA40"):
    if (apafolder == "LArIAT"):
        rms_rootpath =  "/Users/shanshangao/tmp/dat0630/Rawdata/Rawdata_" + rmsdate + "/"
        fpga_rootpath = "/Users/shanshangao/tmp/dat0630/Rawdata/Rawdata_" + fpgdate + "/"
        asic_rootpath = "/Users/shanshangao/tmp/dat0630/Rawdata/Rawdata_" + asidate + "/"
        
    elif (apafolder != "APA"):
        rms_rootpath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + rmsdate + "/"
        fpga_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + fpgdate + "/"
        asic_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + asidate + "/"

    from timeit import default_timer as timer
    s0= timer()
    print "Start...please wait..."
    
    gains = ["140"] 
    tps = [  "20"]
    #jumbo_flag = True
    jumbo_flag = False
    wib_femb_chns = [  
                        #wib(0-4), femb(0-3), chn(0~127)
                        #[0, 2, 120   ],
                        [wibno, fembno, chnno]
                    ]    
    
    for wfc in wib_femb_chns:
        wibno = wfc[0]
        fembno = wfc[1]
        chnno = wfc[2]
        out_path = rms_rootpath + "/" + "results/" + "TPC%d_"%tpcchn_no + rmsrunno 
        #if (os.path.exists(out_path)):
        #    pass
        #else:
        #    try: 
        #        os.makedirs(out_path)
        #    except OSError:
        #        print "Can't create a folder, exit"
        #        exit()
        mps = []
        for gain in gains: 
            for tp in tps:
                 ana_a_chn_args = (out_path, rms_rootpath, asic_rootpath, asic_rootpath, APAno, rmsrunno, fpgarunno, asicrunno, wibno, fembno, chnno, gain, tp, jumbo_flag)
                 p = mp.Process(target=plot_a_chn, args=ana_a_chn_args)
                 mps.append(p)
        for p in mps:
            p.start()
        for p in mps:
            p.join()
        print "time passed %d seconds"%(timer() - s0)
    print "DONE"
