# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Mon Aug  6 15:32:30 2018
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
from matplotlib.backends.backend_pdf import PdfPages
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from apa_mapping import APA_MAP
apamap = APA_MAP()
from femb_position import femb_position
from all_FEMBs_results import All_FEMBs_results
from readlog import readlog
from read_rtds import run_rtds

start = timer()
strdate = sys.argv[1]
strrunno = sys.argv[2]
APAno =  int(sys.argv[3])
jumbo_flag  = ( sys.argv[4] == "True" )
gain = int(sys.argv[5])
tp = int(sys.argv[6])
server_flg = sys.argv[7]
max_limit = 3650
min_limit = 800
#hp_filter  = False
hp_filter  = True 
plot_en = int(sys.argv[8],16)
mode = sys.argv[9]

if mode == "F":
    print "Start run%sdat"%strrunno
    rundir = "run%sdat"%strrunno
else:
    print "Start run%scfg"%strrunno
    rundir = "run%scfg"%strrunno

if (server_flg == "server" ):
    rootpath = "/home/nfs/sbnd/BNL_LD_data/LArIAT/Rawdata/"
    rootpath = "/lariat/data/users/sbnd/BNL_LD_data/LArIAT/Rawdata/"
    #rootpath = "/daqdata/sbnd/BNL_LD_data2/LArIAT/Rawdata/"
    #rootpath = "/Users/shanshangao/tmp/dat0630/Rawdata/"
else:
    rootpath = "/Users/shanshangao/LArIAT/Rawdata/"
path =rootpath + "Rawdata_"+ strdate + "/" 
apamap.APA = "LArIAT"
if mode == "F":
    loginfo = readlog(rootpath=rootpath, APAno=APAno, runtime = strdate, runno = strrunno, runtype = "dat") 
else:
    loginfo = readlog(rootpath=rootpath, APAno=APAno, runtime = strdate, runno = strrunno, runtype = "cfg") 

run_temp = None

save_cycle = 0
result_dir = path + "results/" 
if (os.path.exists(result_dir)):
    pass
else:
    try: 
        os.makedirs(result_dir)
    except OSError:
        print "Error to create a folder"
        exit()

result_pdf = result_dir + "X" + format(plot_en, "02X") + rundir +  "_" + apamap.APA + "_APA" + str(APAno) + '_gain' + str(gain) +  "tp" + str(tp) + "_results" + str(save_cycle)+'.pdf'
result_waveform = result_dir + "X" + format(plot_en, "02X") + rundir +  "_" + apamap.APA + "_APA" + str(APAno) + '_gain' + str(gain) +  "tp" + str(tp) + "_results" + str(save_cycle)+'.png'

pp = PdfPages(result_pdf)

wib_np = [0,1]
feed_freq=500
wibsdata = All_FEMBs_results(path, rundir, apamap.APA, APAno, gain=gain, mode=mode, wib_np = wib_np, tp=tp, jumbo_flag = jumbo_flag, feed_freq = 500, hp_filter=hp_filter)

def oneplt(pp, chns, paras, title, ylabel, xlabel, ylims, xlims, labels):
    fig = plt.figure(figsize=(16,9))
    ax = plt
    for i in range(len(paras)):
        ax.scatter(chns, paras[i], label = labels[i])
        ax.plot( chns, paras[i])

    ax.legend(loc="best", fontsize=16 )

    ax.tick_params(labelsize=20)
    ax.xlim(xlims)
    ax.ylim(ylims)
    ax.ylabel(ylabel, fontsize=20 )
    ax.xlabel(xlabel, fontsize=20 )
    ax.title(title , fontsize=20 )
    ax.grid()
    #plt.show()
    plt.savefig(pp, format='pdf')
    plt.close()

def plots(plot_en, apa_results, loginfo, run_temp,  pp, gain=2, frontpage = False, APAno = 3):
    if (frontpage == True ):
        fig = plt.figure(figsize=(16,9))
        ax = plt
        ax.text(0.4,0.9, "Test Summary", fontsize = 32, color = 'g')
        ax.text(0.05,0.80, "APA no.        : " + loginfo[0], fontsize=20 )
        ax.text(0.05,0.75, "Enviroment     : " + loginfo[1], fontsize=20 )
        ax.text(0.05,0.70, "Description    : " + loginfo[2], fontsize=20 )
        if ( run_temp != None ):
            ax.text(0.05,0.65, "RTDs(TT0206 to TT0200) measured at %s: %3dK, %3dK, %3dK, %3dK, %3dK, %3dK, %3dK "%(run_temp[8],\
                    run_temp[7],run_temp[6],run_temp[5],run_temp[4],run_temp[3],run_temp[2],run_temp[1] ), fontsize=20 )
        else:
            ax.text(0.05,0.65, "Temperature    : " + loginfo[3], fontsize=20 )
        ax.text(0.05,0.60, "Test type      : " + loginfo[4], fontsize=20 )
        ax.text(0.05,0.55, "Rawdata path   : " + loginfo[5], fontsize=20 )
        ax.text(0.05,0.50, "Test started at : " + loginfo[6], fontsize=20 )
        ax.savefig(pp, format='pdf')
        ax.close()
        

    if ( (plot_en&0x01) != 0 ):
        print "Pedestal Measurement"
        chnparas = []
        for chndata in apa_results:
            if chndata[1][0][0] == 'X' or chndata[1][0][0] == 'U' :
                chnparas.append( [int(chndata[1][0][1:]), chndata[6] ])
        chnparas = sorted(chnparas,key=lambda l:l[0], reverse=False)
        chns, paras = zip(*chnparas)
        paras = [paras]

        ylabel = "ADC output /bin"
        xlabel = "Channel No."
        title  = "Pedestal Measurement" 
        xlims = [min(chns),max(chns)]
        ylims = [0,4100]
        labels = ["Pedestal"]
        oneplt(pp, chns, paras, title, ylabel, xlabel, ylims, xlims, labels)

    if ( (plot_en&0x02) != 0 ):
        print "Noise Measurement"
        chnparas = []
        print "wire no, FEMBchn, ASICno, ASICchn, FEMBno, WIBno, RMS(ADC)"
        for chndata in apa_results:
            if chndata[1][0][0] == 'X' or chndata[1][0][0] == 'U' :
                chnparas.append( [int(chndata[1][0][1:]), chndata[7] ])
                if chndata[7] > 20:
                    print chndata[1], (chndata[7])
                if chndata[7] < 1:
                    print chndata[1], (chndata[7])
        chnparas = sorted(chnparas,key=lambda l:l[0], reverse=False)
        chns, paras = zip(*chnparas)
        paras = [paras]

        ylabel = "RMS(ADC) /bin"
        xlabel = "Channel No."
        title  = "Noise Measurement" 
        xlims = [0,len(chns)]
        xlims = [min(chns),max(chns)]
        rmsmax = np.max(paras)
        if rmsmax > 10:
            ymax = 10
        else:
            ymax = 10
        ylims = [0,ymax]
        labels = ["RMS(ADC)"]
        oneplt(pp, chns, paras, title, ylabel, xlabel, ylims, xlims, labels)
        
    if ( (plot_en&0x08) != 0 ):
        print "Noise Measurement After HPF"
        chnparas = []
        print "wire no, FEMBchn, ASICno, ASICchn, FEMBno, WIBno, RMS(ADC)"
        cnt_tmp = 0
        for chndata in apa_results:
            if chndata[1][0][0] == 'X' or chndata[1][0][0] == 'U' :
                chnparas.append( [int(chndata[1][0][1:]), chndata[9] ])
                #if chndata[9] > 10:
                #    print chndata[1], (chndata[9])
                if chndata[9] < 0.9:
                    print chndata[1], (chndata[9])
                    cnt_tmp = cnt_tmp + 1
        print cnt_tmp
        chnparas = sorted(chnparas,key=lambda l:l[0], reverse=False)
        chns, paras = zip(*chnparas)
        paras = [paras]

        ylabel = "RMS(ADC) /bin"
        xlabel = "Channel No."
        title  = "Noise Measurement After HPF" 
        xlims = [0,len(chns)]
        xlims = [min(chns),max(chns)]
        rmsmax = np.max(paras)
        if rmsmax > 10:
            ymax = 10
        else:
            ymax = 10
        ylims = [0,ymax]
        labels = ["RMS(ADC)"]
        oneplt(pp, chns, paras, title, ylabel, xlabel, ylims, xlims, labels)
        

    if ( (plot_en&0x04) != 0 ):
        print "Pulse amplitude"
        chnparas = []
        for chndata in apa_results:
            if chndata[1][0][0] == 'X' or chndata[1][0][0] == 'U' :
                chnparas.append( [int(chndata[1][0][1:]), chndata[11] ])
        chnparas = sorted(chnparas,key=lambda l:l[0], reverse=False)
        chns, para0 = zip(*chnparas)

        chnparas = []
        for chndata in apa_results:
            if chndata[1][0][0] == 'X' or chndata[1][0][0] == 'U' :
                chnparas.append( [int(chndata[1][0][1:]), chndata[6] ])
        chnparas = sorted(chnparas,key=lambda l:l[0], reverse=False)
        chns, para1 = zip(*chnparas)

        chnparas = []
        for chndata in apa_results:
            if chndata[1][0][0] == 'X' or chndata[1][0][0] == 'U' :
                chnparas.append( [int(chndata[1][0][1:]), chndata[12] ])
        chnparas = sorted(chnparas,key=lambda l:l[0], reverse=False)
        chns, para2 = zip(*chnparas)
        paras = [para0, para1, para2]

        ylabel = "ADC /bin"
        xlabel = "Channel No."
        title  = "Pulse Amplitude" 
        xlims = [0,len(chns)]
        xlims = [min(chns),max(chns)]
        ylims = [0,4100]
        labels = ["Positive Amplitude", "Pedestal", "Negative Amplitude"]
        oneplt(pp, chns, paras, title, ylabel, xlabel, ylims, xlims, labels)

plots(plot_en, wibsdata, loginfo, run_temp,   pp, gain, frontpage = True , APAno = APAno )
pp.close()
print "Done, please punch \" Enter \" or \"return\" key !"


