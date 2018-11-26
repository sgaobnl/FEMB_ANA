# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 11/24/2018 11:01:42 AM
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
import os
from sys import exit
import sys
import os.path
import math
from femb_position import femb_position
from apa_mapping   import APA_MAP
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.mlab as mlab
from matplotlib.backends.backend_pdf import PdfPages
from chn_analysis  import read_rawdata 
from chn_analysis  import read_rawdata_coh 
from chn_analysis  import noise_a_chn 
from chn_analysis  import noise_a_coh 
from fft_chn import chn_rfft_psd
from chn_analysis  import coh_noise_ana
from highpass_filter import hp_flt_applied


def wf_a_asic(rms_rootpath, fpga_rootpath, asic_rootpath,  APAno = 4, \
               rmsrunno = "run01rms", fpgarunno = "run01fpg", asicrunno = "run01asi",\
               wibno=0,  fembno=0, asicno=0, gain="250", tp="05" ,\
               jumbo_flag=False, apa= "ProtoDUNE" ):
    femb_pos_np = femb_position (APAno)
    wibfemb= "WIB"+format(wibno,'02d') + "_" + "FEMB" + format(fembno,'1d') 
    apainfo = None
    for femb_pos in femb_pos_np:
        if femb_pos[1] == wibfemb:
            apainfo = femb_pos
            break

    feset_info = [gain, tp]
    apa_map = APA_MAP()
    apa_map.APA = apa
    apa_map.femb=fembno + wibno*4
    All_sort, X_sort, V_sort, U_sort =  apa_map.apa_femb_mapping()

    rmsdata  = read_rawdata_coh(rms_rootpath, rmsrunno,  wibno,  fembno, 16*asicno, gain, tp, jumbo_flag)

    asic_results =[]
    for chni in range(16):
        chnno = chni + 16*asicno
        wireinfo = None
        for onewire in All_sort:
            if (int(onewire[1]) == chnno):
                wireinfo = onewire
                break
        if fembno == 0:
            apa_femb_loc = [ 
                ["U28",  4, "15"], ["U29",  4, "14"], ["X54",  4, "13"], ["X53",  4, "12"],
                ["X52",  4, "11"], ["X51",  4, "10"], ["X50",  4, "09"], ["X49",  4, "08"],
                ["X48",  4, "07"], ["X47",  4, "06"], ["X46",  4, "05"], ["X45",  4, "04"],
                ["X44",  4, "03"], ["X43",  4, "02"], ["X55",  4, "01"], ["X56",  4, "00"],
                                                                                   
                ["X29",  3, "15"], ["X30",  3, "14"], ["X42",  3, "13"], ["X41",  3, "12"],
                ["X40",  3, "11"], ["X39",  3, "10"], ["X38",  3, "09"], ["X37",  3, "08"],
                ["X36",  3, "07"], ["X35",  3, "06"], ["X34",  3, "05"], ["X33",  3, "04"],
                ["X32",  3, "03"], ["X31",  3, "02"], ["U26",  3, "01"], ["U27",  3, "00"],

                ["V36",  2, "00"], ["V36",  2, "01"], ["U35",  2, "02"], ["V35",  2, "03"],
                ["U34",  2, "04"], ["V34",  2, "05"], ["U33",  2, "06"], ["V33",  2, "07"],
                ["U32",  2, "08"], ["V32",  2, "09"], ["U31",  2, "10"], ["V31",  2, "11"],
                ["U30",  2, "12"], ["V30",  2, "13"], ["U19",  2, "14"], ["V28",  2, "15"],
                                                                                   
                ["U18",  1, "00"], ["V26",  1, "01"], ["U25",  1, "02"], ["V25",  1, "03"],
                ["U24",  1, "04"], ["V24",  1, "05"], ["U23",  1, "06"], ["V23",  1, "07"],
                ["U22",  1, "08"], ["V22",  1, "09"], ["U21",  1, "10"], ["V21",  1, "11"],
                ["U20",  1, "12"], ["V20",  1, "13"], ["V19",  1, "14"], ["V27",  1, "15"],

                ["U08",  7, "15"], ["U10",  7, "14"], ["X26",  7, "13"], ["X25", 7 , "12"],
                ["X24",  7, "11"], ["X23",  7, "10"], ["X22",  7, "09"], ["X21", 7 , "08"],
                ["X20",  7, "07"], ["X19",  7, "06"], ["X18",  7, "05"], ["X17", 7 , "04"],
                ["X16",  7, "03"], ["X15",  7, "02"], ["X11",  7, "01"], ["X10", 7 , "00"],
                                                                                 
                ["X09",  8, "15"], ["X08",  8, "14"], ["X14",  8, "13"], ["X13", 8 , "12"],
                ["X12",  8, "11"], ["X11",  8, "10"], ["X10",  8, "09"], ["X09", 8 , "08"],
                ["X08",  8, "07"], ["X07",  8, "06"], ["X06",  8, "05"], ["X05", 8 , "04"],
                ["X04",  8, "03"], ["X03",  8, "02"], ["U02",  8, "01"], ["U01", 8 , "00"],
                                                                            
                ["V18",  5, "00"], ["V18",  5, "01"], ["U17",  5, "02"], ["V17",  5, "03"], 
                ["U16",  5, "04"], ["V16",  5, "05"], ["U15",  5, "06"], ["V15",  5, "07"], 
                ["U14",  5, "08"], ["V14",  5, "09"], ["U13",  5, "10"], ["V13",  5, "11"], 
                ["U12",  5, "12"], ["V12",  5, "13"], ["U11",  5, "14"], ["V10",  5, "15"], 
                                                                                   
                ["U09",  6, "00"], ["V08",  6, "01"], ["U07",  6, "02"], ["V07",  6, "03"], 
                ["U06",  6, "04"], ["V06",  6, "05"], ["U05",  6, "06"], ["V05",  6, "07"], 
                ["U04",  6, "08"], ["V04",  6, "09"], ["U03",  6, "10"], ["V03",  6, "11"], 
                ["U02",  6, "12"], ["V02",  6, "13"], ["V09",  6, "14"], ["V11",  6, "15"] 
                    ]

            for al in apa_femb_loc:
                if ( int(wireinfo[1]) == (al[1]-1)*16 + int(al[2]) ):
                        wireinfo[0] = al[0]
                        break
        
        chn_noise_paras = noise_a_chn(rmsdata, chnno, fft_en = True)
        rms          =  chn_noise_paras[1]
        ped          =  chn_noise_paras[2]
        hfrms        =  chn_noise_paras[7]
        hfped        =  chn_noise_paras[8]
        sfrms        =  chn_noise_paras[13]
        sfped        =  chn_noise_paras[14]
        unstk_ratio  =  chn_noise_paras[15]
        raw_data     =   chn_noise_paras[3]
        r100us_data     =   chn_noise_paras[4]
        fft_f        =   chn_noise_paras[5]
        fft_p        =   chn_noise_paras[6]
        fft_fl       =   chn_noise_paras[16]
        fft_pl       =   chn_noise_paras[17]
        print [apainfo, APAno, wibno, fembno, asicno, chni, wireinfo]
                             #0         1        2     3       4      5    6    7     8      9     10      11      12           13        14           15     16     17      18 
        asic_results.append([apainfo, APAno, wibno, fembno, asicno, chni, rms ,ped ,hfrms ,hfped ,sfrms ,sfped  ,unstk_ratio, raw_data, r100us_data, fft_f, fft_p, fft_fl, fft_pl, wireinfo])
    return asic_results


def wfcoh_a_asic(rms_rootpath, fpga_rootpath, asic_rootpath,  APAno = 4, \
               rmsrunno = "run01rms", fpgarunno = "run01fpg", asicrunno = "run01asi",\
               wibno=0,  fembno=0, asicno=0, gain="250", tp="05" ,\
               jumbo_flag=False, apa= "ProtoDUNE" ):
    femb_pos_np = femb_position (APAno)
    wibfemb= "WIB"+format(wibno,'02d') + "_" + "FEMB" + format(fembno,'1d') 
    apainfo = None
    for femb_pos in femb_pos_np:
        if femb_pos[1] == wibfemb:
            apainfo = femb_pos
            break

    feset_info = [gain, tp]
    apa_map = APA_MAP()
    apa_map.APA = apa
    All_sort, X_sort, V_sort, U_sort =  apa_map.apa_femb_mapping()

    rmsdata  = read_rawdata_coh(rms_rootpath, rmsrunno,  wibno,  fembno, 16*asicno, gain, tp, jumbo_flag)

    asic_results =[]
    for chni in range(16):
        chnno = chni + 16*asicno
        wireinfo = None
        for onewire in All_sort:
            if (int(onewire[1]) == chnno):
                wireinfo = onewire
                break
        wiretype = wireinfo[0][0]
        print [APAno, wibno, fembno, asicno, chni, wireinfo]
 
        rpath = "/nfs/home/shanshan/coh_study/"
        rpath = "./"
        t_pat = "Test035"
        pre_ana = t_pat + "_ProtoDUNE_CE_characterization_summary" + ".csv"
        ppath = rpath + pre_ana 
        ccs = []
        with open(ppath, 'r') as fp:
            for cl in fp:
                tmp = cl.split(",")
                x = []
                for i in tmp:
                    x.append(i.replace(" ", ""))
                x = x[:-1]
                ccs.append(x)
        ccs_title = ccs[0]
        ccs = ccs[1:]

        asic_ccs = []
        for ci in ccs:
            if (APAno == int(ci[0][1])) and ( int(ci[3]) == wibno )and ( int(ci[4]) == fembno )and ( int(ci[5]) == asicno ):
                asic_ccs.append(ci)

        cohdata ,cohdata_flg = coh_noise_ana(asic_ccs, rmsdata, wiretype = wiretype)

        chn_noise_paras = noise_a_coh(cohdata, cohdata_flg, rmsdata, chnno =chni, fft_en = True, fft_s=2000, fft_avg_cycle=50, wibno=wibno,  fembno=fembno )


        fig = plt.figure(figsize=(32,18))
        axu = []
        axm = []
        axd = []
        axu.append( plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)) 
        axm.append( plt.subplot2grid((3, 3), (1, 0), colspan=3, rowspan=1)) 
        axd.append( plt.subplot2grid((3, 3), (2, 0), colspan=3, rowspan=1)) 
 
#        chn_noise_paras = w_results[chni]
#        wireinfo =  wireinfo[0][0]

        rms =  chn_noise_paras[1]
        ped =  chn_noise_paras[2]
        cohrms =  chn_noise_paras[14]
        cohped =  chn_noise_paras[15]
        postrms =  chn_noise_paras[7]
        postped =  chn_noise_paras[8]

        rawdata = chn_noise_paras[3]
        postdata = chn_noise_paras[9]


        label = wireinfo[0] + "_ASIC" + str(wireinfo[2]) + "_CHN" + wireinfo[3]  
        ped_wf_subplot(axu[0], rawdata[0:1000],  ped,     rms,     t_rate=0.5, title="Waveforms of raw data (2MSPS)", label=label )
        ped_wf_subplot(axm[0], cohdata[0:1000],  cohped,  cohrms , t_rate=0.5, title="Waveforms of coherent noise (2MSPS)", label=label )
        ped_wf_subplot(axd[0], postdata[0:1000], postped, postrms, t_rate=0.5, title="Waveforms of post-filter data (2MSPS)", label=label )


        fig_title = apainfo[0] + "_" + apainfo[1] + "_FE%d_%s"%(wireinfo[2], wiretype)
        plt.tight_layout( rect=[0, 0.05, 1, 0.95])
        fig.suptitle(fig_title, fontsize = 20)
        plt.savefig(out_path + fig_title + "_coh_wf_%s.png"%label, format='png')
        plt.close()
       
    return asic_results



def ped_wf_subplot(ax, data_slice, ped, rms,  t_rate=0.5, title="Waveforms of raw data", label="Waveform" ):
    N = len(data_slice)
    x = np.arange(N) * t_rate
    y = data_slice
    ax.scatter(x, y, marker='.', color ='r', label=label + "\n" + "mean = %d, rms = %2.3f" % (int(ped), rms))
    ax.plot(x, y, color ='b')
   
    ax.set_title(title )
    ax.set_xlim([0,int(N*t_rate)])
#    ax.set_ylim([ped-5*(int(rms+1)),ped+5*(int(rms+1))])
    ax.grid()
    ax.set_ylabel("ADC output / LSB")
    ax.set_xlabel("t / $\mu$s")
    ax.legend(loc=1)

def asic_wf_plot_wire(out_path, asic_results, wiretype = "U"):
    fig = plt.figure(figsize=(32,51))
    axl = []
    axr = []
    for i in range(17):
        axl.append( plt.subplot2grid((17, 2), (i, 0), colspan=1, rowspan=1)) 
        axr.append( plt.subplot2grid((17, 2), (i, 1), colspan=1, rowspan=1)) 
    wi = 0
    for chni in range(16):
        chn_noise_paras = asic_results[chni]
        wireinfo =  chn_noise_paras[19]
        
        APAno =  chn_noise_paras[1]
        #if (wireinfo[0][0] == wiretype):
        if (wireinfo[0][0] != "C"):
            wiretype = wireinfo[0][0] 
            rms =  chn_noise_paras[6]
            ped =  chn_noise_paras[7]
            data_slice = chn_noise_paras[13]
            data_100us_slice = chn_noise_paras[14]
            if ( wi == 0):
                avg_data = np.array(data_slice)
                avg_data_100us_slice = np.array(chn_noise_paras[14])
            else:
                avg_data = avg_data + np.array(data_slice)
                avg_data_100us_slice =avg_data_100us_slice +np.array( chn_noise_paras[14])
            
            apainfo =  chn_noise_paras[0]
            hfrms =  chn_noise_paras[7]
            hfped =  chn_noise_paras[8]
            hfdata_slice = chn_noise_paras[9]
            hfdata_100us_slice = chn_noise_paras[10]
            hflabel = "After HPF:  mean = %d, rms = %2.3f" % (int(hfped), hfrms) 
            sfrms =  chn_noise_paras[10]
            sfped =  chn_noise_paras[11]
            unstk_ratio  =  chn_noise_paras[12]
            label = wireinfo[0] + ", ASIC" + str(wireinfo[2]) + ", CHN" + str(wireinfo[3]) 

            ped_wf_subplot(axl[wi], data_slice[0:2000],         ped,   rms,    t_rate=0.5, title="Waveforms of raw data (2MSPS)", label=label )
            ped_wf_subplot(axr[wi], data_100us_slice,   ped,   rms,    t_rate=100, title="Waveforms of raw data (10kSPS)", label=label )
            wi = wi + 1
    avg_data = avg_data*1.0/wi
    avg_data_100us_slice = avg_data_100us_slice*1.0/wi
    avgped = np.mean(avg_data)
    avgrms = np.std(avg_data)
    avgped100us = np.mean(avg_data_100us_slice)
    avgrms100us = np.std(avg_data_100us_slice)
 
    label = "mean = %d, rms = %2.3f" % (int(avgped), avgrms) 
    ped_wf_subplot(axl[16], avg_data[0:2000],         avgped,   avgrms,    t_rate=0.5, title="Averaging waveforms of %s wires of a FE ASIC(2MSPS)"%wiretype, label=label )
    ped_wf_subplot(axr[16], avg_data_100us_slice,   avgped100us,   avgrms100us,    t_rate=100, title="Averaging waveforms  %s wires of a FE ASIC(2MSPS)"%wiretype, label=label )
 
    fig_title = apainfo[0] + "_" + apainfo[1] + "_FE%d_%s"%(wireinfo[2], wiretype)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    fig.suptitle(fig_title, fontsize = 20)
    plt.savefig(out_path+ fig_title + ".png", format='png')
    plt.close()

def asic_wf_plot_coh(out_path, asic_results, wiretypes = "U", del_chns = [[0,1,0]] ):
    fig = plt.figure(figsize=(32,51))
    axl = []
    axr = []
    for i in range(17):
        axl.append( plt.subplot2grid((17, 2), (i, 0), colspan=1, rowspan=1)) 
        axr.append( plt.subplot2grid((17, 2), (i, 1), colspan=1, rowspan=1)) 
    wi = 0
    for chni in range(16):
        chn_noise_paras = asic_results[chni]
        wireinfo =  chn_noise_paras[19]
        wibno = chn_noise_paras[2] 
        fembno = chn_noise_paras[3] 
        asicno = chn_noise_paras[4] 
        asicchn = chn_noise_paras[5] 
        fembchn = asicno*16 + asicchn
        w_f_ch = [ wibno, fembno, fembchn]
        wiretype = wireinfo[0][0] 
        if (wireinfo[0][0] != "C") and (wiretype in wiretypes) and (not(w_f_ch in del_chns)):
            data_slice = chn_noise_paras[13]
            data_100us_slice = chn_noise_paras[14]
            if ( wi == 0):
                avg_data = np.array(data_slice)
                avg_data_100us_slice = np.array(chn_noise_paras[14])
            else:
                avg_data = avg_data + np.array(data_slice)
                avg_data_100us_slice =avg_data_100us_slice +np.array( chn_noise_paras[14])
            wi = wi + 1
    avg_data = avg_data*1.0/wi
    avg_data_100us_slice = avg_data_100us_slice*1.0/wi
    avgped = np.mean(avg_data)
    avgrms = np.std(avg_data)
    avgped100us = np.mean(avg_data_100us_slice)
    avgrms100us = np.std(avg_data_100us_slice)
 
    wi = 0
    asicrms = []
    for chni in range(16):
        chn_noise_paras = asic_results[chni]
        wireinfo =  chn_noise_paras[19]
        wiretype = wireinfo[0][0] 
        APAno =  chn_noise_paras[1]
        #if (True):
        wibno = chn_noise_paras[2] 
        fembno = chn_noise_paras[3] 
        asicno = chn_noise_paras[4] 
        asicchn = chn_noise_paras[5] 
        fembchn = asicno*16 + asicchn
        w_f_ch = [ wibno, fembno, fembchn]
        if (wireinfo[0][0] != "C") and (wiretype in wiretypes) and (not(w_f_ch in del_chns)):
            wiretype = wireinfo[0][0] 
            data_slice = chn_noise_paras[13]
            rms =  chn_noise_paras[6]
            ped =  chn_noise_paras[7]
            
            apainfo =  chn_noise_paras[0]
            hfrms =  chn_noise_paras[7]
            hfped =  chn_noise_paras[8]
            hfdata_slice = chn_noise_paras[9]
            hfdata_100us_slice = chn_noise_paras[10]
            hflabel = "After HPF:  mean = %d, rms = %2.3f" % (int(hfped), hfrms) 
            sfrms =  chn_noise_paras[10]
            sfped =  chn_noise_paras[11]
            unstk_ratio  =  chn_noise_paras[12]
            label = wireinfo[0] + ", ASIC" + str(wireinfo[2]) + ", CHN" + str(wireinfo[3]) 

            coh_slice = np.array(data_slice[0::200])-np.array(avg_data[0::200])
            ped_wf_subplot(axl[chni], data_slice[0::200],         ped,   rms,    t_rate=0.5, title="Waveforms of raw data (2MSPS)", label=label )
            ped_wf_subplot(axr[chni], coh_slice,     np.mean(coh_slice),   np.std(coh_slice),    t_rate=0.5, title="Waveforms of data after filtering(2MSPS)", label=label )

            #coh_slice = np.array(data_slice[0:2000])-np.array(avg_data[0:2000])
            #ped_wf_subplot(axl[chni], data_slice[0:2000],         ped,   rms,    t_rate=0.5, title="Waveforms of raw data (2MSPS)", label=label )
            #ped_wf_subplot(axr[chni], coh_slice,     np.mean(coh_slice),   np.std(coh_slice),    t_rate=0.5, title="Waveforms of data after filtering(2MSPS)", label=label )

            print ( [ wireinfo[0], str(chn_noise_paras[2]), str(chn_noise_paras[3]), str(chn_noise_paras[4]), str(chn_noise_paras[5]), str(np.std(data_slice[0:2000])), str(np.std(avg_data[0:2000])) , str(np.std(coh_slice)) ] )
            asicrms.append( [ wireinfo[0], str(chn_noise_paras[2]), str(chn_noise_paras[3]), str(chn_noise_paras[4]), str(chn_noise_paras[5]),str(np.std(data_slice[0:2000])), str(np.std(avg_data[0:2000])) , str(np.std(coh_slice)) ] )
            #ped_wf_subplot(axr[wi], data_100us_slice,   ped,   rms,    t_rate=100, title="Waveforms of raw data (10kSPS)", label=label )

    label = "mean = %d, rms = %2.3f" % (int(avgped), avgrms) 
    #ped_wf_subplot(axl[16], avg_data[0:2000],         avgped,   avgrms,    t_rate=0.5, title="Averaging waveforms of %s wires of a FE ASIC(2MSPS)"%wiretype, label=label )
    ped_wf_subplot(axl[16], avg_data[0::200],         avgped,   avgrms,    t_rate=0.5, title="Averaging waveforms of %s wires of a FE ASIC(2MSPS)"%wiretype, label=label )
    #ped_wf_subplot(axr[16], avg_data[0:2000],         avgped,   avgrms,    t_rate=0.5, title="Averaging waveforms of %s wires of a FE ASIC(2MSPS)"%wiretype, label=label )
#    ped_wf_subplot(axr[16], avg_data_100us_slice,   avgped100us,   avgrms100us,    t_rate=100, title="Averaging waveforms  %s wires of a FE ASIC(2MSPS)"%wiretype, label=label )
 
    fig_title = apainfo[0] + "_" + apainfo[1] + "_FE%d_%s"%(wireinfo[2], wiretypes)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    fig.suptitle(fig_title, fontsize = 20)
    plt.savefig(out_path+ fig_title + ".png", format='png')
    plt.close()
    return asicrms


def asic_coh_plot_wire(out_path, asic_results, wiretypes = "U"):
    w_results = []
    wi = 0
    for chni in range(16):
        chn_noise_paras = asic_results[chni]
        wireinfo =  chn_noise_paras[19]
        APAno =  chn_noise_paras[1]
        unstk_ratio  =  chn_noise_paras[12]
        wiretype = wireinfo[0][0] 
        #if (wireinfo[0][0] in  wiretype) :
        if (wireinfo[0][0] != "C") and (wiretype in  wiretypes):
        #    wiretype = wireinfo[0][0] 
            data_slice = chn_noise_paras[13]
            if ( wi == 0):
                avg_data = np.array(data_slice)
            else:
                avg_data = avg_data + np.array(data_slice)
            wi = wi + 1
            w_results.append(asic_results[chni])
 
    coh_data = (avg_data*1.0/wi) 
    coh_data = coh_data - np.mean( coh_data)

    for chni in range(len(w_results)):
        fig = plt.figure(figsize=(32,18))
        axu = []
        axm = []
        axd = []
        for i in range(3):
            axu.append( plt.subplot2grid((3, 3), (0, i), colspan=1, rowspan=1)) 
            axm.append( plt.subplot2grid((3, 3), (1, i), colspan=1, rowspan=1)) 
            axd.append( plt.subplot2grid((3, 3), (2, i), colspan=1, rowspan=1)) 
 
        chn_noise_paras = w_results[chni]
        wireinfo =  chn_noise_paras[19]
        wiretype = wireinfo[0][0] 
        APAno =  chn_noise_paras[1]
        rms =  chn_noise_paras[6]
        ped =  chn_noise_paras[7]
        rawdata = chn_noise_paras[13]
#       chnrmsdata = hp_flt_applied(chnrmsdata, fs = 2000000, passfreq = 500, flt_order = 3)
        rawdata = hp_flt_applied(rawdata, fs = 2000000, passfreq = 500, flt_order = 3)


        unstk_ratio  =  chn_noise_paras[12]
        pos_data = np.array (rawdata) - coh_data
        pos_ped = np.mean(pos_data[0:100000])
        pos_rms = np.std(pos_data[0:100000])
        apainfo =  chn_noise_paras[0]
        label = wireinfo[0] + "_ASIC" + str(wireinfo[2]) + "_CHN" + str(wireinfo[3]  )
        ped_wf_subplot(axu[0], rawdata[0:1000],    ped,   rms,    t_rate=0.5, title="Waveforms of raw data (2MSPS)", label=label )
        ped_wf_subplot(axm[0], coh_data[0:1000],   np.mean(coh_data), np.std(coh_data)  ,    t_rate=0.5, title="Waveforms of coherent noise (2MSPS)", label=label )
        ped_wf_subplot(axd[0], pos_data[0:1000],   pos_ped,   pos_rms,    t_rate=0.5, title="Waveforms of post-filter data (2MSPS)", label=label )

        rf_l, rp_l = chn_rfft_psd(rawdata, fft_s = len(rawdata), avg_cycle = 1)
        cf_l, cp_l = chn_rfft_psd(coh_data, fft_s = len(coh_data), avg_cycle = 1)
        pf_l, pp_l = chn_rfft_psd(pos_data, fft_s = len(pos_data), avg_cycle = 1)

#        ped_wf_subplot(axu[1], rawdata[::200],    ped,   rms,    t_rate=100, title="Waveforms of raw data (10kSPS)", label=label )
#        ped_wf_subplot(axm[1], coh_data[::200],   np.mean(coh_data), np.std(coh_data)  ,    t_rate=100, title="Waveforms of coherent noise (10kSPS)", label=label )
#        ped_wf_subplot(axd[1], pos_data[::200],   pos_ped,   pos_rms,    t_rate=100, title="Waveforms of post-filter data (10kSPS)", label=label )
 
        ped_fft_subplot(axu[1], rf_l, rp_l, maxx=1000000,  title="FFT specturm", label=label, peaks_note = False )
        ped_fft_subplot(axm[1], cf_l, cp_l, maxx=1000000,  title="FFT specturm", label=label, peaks_note = False )
        ped_fft_subplot(axd[1], pf_l, pp_l, maxx=1000000,  title="FFT specturm", label=label, peaks_note = False )

        ped_fft_subplot(axu[2], rf_l, rp_l, maxx=100000,  title="FFT specturm", label=label, peaks_note = False )
        ped_fft_subplot(axm[2], cf_l, cp_l, maxx=100000,  title="FFT specturm", label=label, peaks_note = False )
        ped_fft_subplot(axd[2], pf_l, pp_l, maxx=100000,  title="FFT specturm", label=label, peaks_note = False )

        fig_title = apainfo[0] + "_" + apainfo[1] + "_FE%d_%s"%(wireinfo[2], wiretype)
        plt.tight_layout( rect=[0, 0.05, 1, 0.95])
        fig.suptitle(fig_title, fontsize = 20)
        plt.savefig(out_path + fig_title + "_coh_%s.png"%label, format='png')
        plt.close()


def ped_fft_subplot(ax, f, p, maxx=1000000,  title="FFT specturm", label="FFT", peaks_note = False ):
    ax.set_title(title )
    ax.plot(np.array(f)/1000.0,p,color='r', label=label)
    ax.set_xlim([0,maxx/1000])
    ax.set_xlabel("Frequency /kHz")
    ax.grid()
    psd=True
    if (psd == True):
        ax.set_ylabel("Power Spectral Desity /dB")
        ax.set_ylim([-80,20])
    else:
        ax.set_ylabel("Amplitude /dB")
        ax.set_ylim([-40,20])
    ax.legend(loc='best')


def asic_fft_plot_wire(out_path, asic_results, wiretype = "U"):
    fig = plt.figure(figsize=(32,51))
    axl = []
    axm = []
    axr = []
    for i in range(17):
        axl.append( plt.subplot2grid((17, 3), (i, 0), colspan=1, rowspan=1)) 
        axm.append( plt.subplot2grid((17, 3), (i, 1), colspan=1, rowspan=1)) 
        axr.append( plt.subplot2grid((17, 3), (i, 2), colspan=1, rowspan=1)) 
    wi = 0
    #for chni in range(16):
    for chni in [0]:
        chn_noise_paras = asic_results[chni]
        wireinfo =  chn_noise_paras[19]
        APAno =  chn_noise_paras[1]
        #if (wireinfo[0][0] == wiretype):
        if (wireinfo[0][0] != "C"):
            wiretype = wireinfo[0][0] 
            rms =  chn_noise_paras[6]
            ped =  chn_noise_paras[7]
            f = chn_noise_paras[15]
            p = chn_noise_paras[16]
            fl = chn_noise_paras[17]
            pl = chn_noise_paras[18]
            if ( wi == 0):
                avg_f = np.array(f)
                avg_p = np.array(p)
                avg_fl = np.array(fl)
                avg_pl = np.array(pl)
            else:
                avg_p  = avg_p  + np.array(p)
                avg_pl = avg_pl + np.array(pl)
 
            apainfo =  chn_noise_paras[0]
            label = wireinfo[0] + ", ASIC" + str(wireinfo[2]) + ", CHN" + str(wireinfo[3])
            ped_fft_subplot(axl[wi], f, p, maxx=1000000,  title="FFT specturm", label=label, peaks_note = False )
            ped_fft_subplot(axm[wi], fl, pl, maxx=100000,  title="FFT specturm", label=label, peaks_note = False )
            ped_fft_subplot(axr[wi], fl, pl, maxx=1000,  title="FFT specturm", label=label, peaks_note = False )
            wi = wi + 1

 
    label = wiretype + "_ASIC" + str(wireinfo[2])   
    ped_fft_subplot(axl[16], avg_f, avg_p*1.0/wi, maxx=1000000,  title="FFT specturm", label=label, peaks_note = False )
    ped_fft_subplot(axm[16], avg_fl,avg_pl*1.0/wi, maxx=100000,  title="FFT specturm", label=label, peaks_note = False )
    ped_fft_subplot(axr[16], avg_fl,avg_pl*1.0/wi, maxx=1000,  title="FFT specturm", label=label, peaks_note = False )

    fig_title = apainfo[0] + "_" + apainfo[1] + "_FE%d_%s"%(wireinfo[2], wiretype)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    fig.suptitle(fig_title, fontsize = 20)
    plt.savefig(out_path + fig_title + "FFT.png", format='png')
    plt.close()



def asic_wf_plot(asic_results, wiretype = "U"):
    fig = plt.figure(figsize=(8,28))
    axl = []
    axr = []
    for i in range(7):
        axl.append( plt.subplot2grid((6, 2), (i, 0), colspan=1, rowspan=1)) 
        axr.append( plt.subplot2grid((6, 2), (i, 1), colspan=1, rowspan=1)) 
 
    for chni in range(16):
        chn_noise_paras = asic_results[chni]
        rms =  chn_noise_paras[6]
        ped =  chn_noise_paras[7]
        data_slice = chn_noise_paras[13]
        data_100us_slice = chn_noise_paras[14]
        wireinfo =  chn_noise_paras[19]
        apainfo =  chn_noise_paras[0]

        hfrms =  chn_noise_paras[7]
        hfped =  chn_noise_paras[8]
        hfdata_slice = chn_noise_paras[9]
        hfdata_100us_slice = chn_noise_paras[10]
        hflabel = "After HPF:  mean = %d, rms = %2.3f" % (int(hfped), hfrms) 

        sfrms =  chn_noise_paras[10]
        sfped =  chn_noise_paras[11]
        unstk_ratio  =  chn_noise_paras[12]

        label = "Rawdata: mean = %d, rms = %2.3f" % (int(ped), rms) + "\n" + \
                "Stuck Free: mean = %d, rms = %2.3f, unstuck=%%%d" % (int(sfped), sfrms, int(unstk_ratio*100) )

        wireinfo_str = "Wire" + wireinfo[0] + "_FEMBCHN" + wireinfo[1] 

        ped_wf_subplot(axl[chni], data_slice,          ped,   rms,    t_rate=0.5, title="Waveforms of raw data (2MSPS)", label=label )
        ped_wf_subplot(axr[chni], data_100us_slice,   ped,   rms,    t_rate=100, title="Waveforms of raw data (10kSPS)", label=label )
        break

    feset_str = "\n Gain = 14 mV/fC, Tp = 2.0 $\mu$s; "
    fig.suptitle(apainfo_str , fontsize = 16)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    plt.savefig("./" + apainfo_str + ".png", format='png')
    plt.close()

if __name__ == '__main__':
    APAno = int(sys.argv[1])
    rmsdate = sys.argv[2]
    fpgdate = sys.argv[3]
    asidate = sys.argv[4]
    rmsrunno = sys.argv[5]
    fpgarunno = sys.argv[6]
    asicrunno = sys.argv[7]
    apafolder = sys.argv[8] 
    jumbo_flag = (sys.argv[9] == "True")
    wibno = int(sys.argv[10] )
    fembno = int(sys.argv[11] )
    asicno = int(sys.argv[12] )

    if (apafolder == "APA40"):
        rms_rootpath =  "D:/SBND_40APA/Rawdata/Rawdata_" + rmsdate + "/"
        fpga_rootpath = "D:/SBND_40APA/Rawdata/Rawdata_" + fpgdate + "/"
        asic_rootpath = "D:/SBND_40APA/Rawdata/Rawdata_" + asidate + "/"
        apa = "APA40"
    elif (apafolder != "APA"):
        rms_rootpath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + rmsdate + "/"
        fpga_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + fpgdate + "/"
        asic_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + asidate + "/"
        apa = "ProtoDUNE"
    else:
        rms_rootpath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + rmsdate + "/"
        fpga_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + fpgdate + "/"
        asic_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + asidate + "/"
        rms_rootpath =  "/nfs/sw/shanshan/Rawdata/APA%d/Rawdata_"%APAno + rmsdate + "/"
        fpga_rootpath = "/nfs/sw/shanshan/Rawdata/APA%d/Rawdata_"%APAno + fpgdate + "/"
        asic_rootpath = "/nfs/sw/shanshan/Rawdata/APA%d/Rawdata_"%APAno + asidate + "/"
        rms_rootpath =  "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/run03rms/"
        fpga_rootpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/run03rms/"
        asic_rootpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/run03rms/"
        apa = "ProtoDUNE"
        rms_rootpath =  "/Users/shanshangao/tmp/Rawdata_08_22_2018/"
        fpga_rootpath =  "/Users/shanshangao/tmp/Rawdata_08_22_2018/"
        asic_rootpath =  "/Users/shanshangao/tmp/Rawdata_08_22_2018/"
        apa = "LArIAT"

    out_path = rms_rootpath + "/" + "results/" + "ASIC_" + rmsrunno + "_" + fpgarunno + "_" + asicrunno+"/"
    if (os.path.exists(out_path)):
        pass
    else:
        try: 
            os.makedirs(out_path)
        except OSError:
            print "Can't create a folder, exit"
            exit()


    print "Start..., please wait..."
    print "Result saves at: "
    print out_path 
    gains = ["250", "140"] 
    tps = ["05", "10", "20", "30"]
    gains = [ "140"] 
    gains = [ "078"] 
    gains = [ "250"] 
    tps = [ "20"]

    PCE = rms_rootpath+ rmsrunno + "%s_ASICrms_femb%d_tp%s"%(gains[0],fembno, tps[0]) + ".csv"
    ccs_title = ["wire", "wib", "femb", "asic", "chnno", "RawRMS", "CohRMS", "PostRMS"]
    with open (PCE, 'w') as fp:
        fp.write(",".join(str(i) for i in ccs_title) +  "," + "\n")
 
    #for i in range(5):

    for i in [fembno]:
        wibno = i//4
        fembno = i%4
        for asicno in range(8):
            asic_results = wf_a_asic(rms_rootpath, fpga_rootpath, asic_rootpath,  APAno = APAno, \
                          rmsrunno = rmsrunno, fpgarunno = fpgarunno, asicrunno = asicrunno,\
                          wibno=wibno,  fembno=fembno, asicno=asicno, gain=gains[0], tp=tps[0] ,\
                          jumbo_flag=True, apa= apa )
            if fembno == 0:
                xasics = [2,3,6,7]
                del_chns =[ [0, 0, 107], [0, 0, 109], [0, 0, 125] ] #femb0
            else:
                del_chns =[ [0, 1, 48], [0, 1, 79], [0, 1, 127] ] #femb1
                xasics = [0,1,4,5]
            if (asicno in xasics):
                asicrms = asic_wf_plot_coh(out_path, asic_results, wiretypes = "X", del_chns = del_chns)
                with open (PCE, 'a+') as fp:
                    for x in asicrms:
                        fp.write(",".join(str(i) for i in x) +  "," + "\n")

            else:
                asicrms = asic_wf_plot_coh(out_path, asic_results, wiretypes = "V", del_chns = del_chns)
                with open (PCE, 'a+') as fp:
                    for x in asicrms:
                        fp.write(",".join(str(i) for i in x) +  "," + "\n")

                asicrms = asic_wf_plot_coh(out_path, asic_results, wiretypes = "U", del_chns = del_chns)
                with open (PCE, 'a+') as fp:
                    for x in asicrms:
                        fp.write(",".join(str(i) for i in x) +  "," + "\n")

#            with open (PCE, 'a+') as fp:
#                for x in asicrms:
#                    fp.write(",".join(str(i) for i in x) +  "," + "\n")
    print PCE

#    asic_results = wf_a_asic(rms_rootpath, fpga_rootpath, asic_rootpath,  APAno = APAno, \
#                  rmsrunno = rmsrunno, fpgarunno = fpgarunno, asicrunno = asicrunno,\
#                  wibno=wibno,  fembno=fembno, asicno=asicno, gain=gains[0], tp=tps[0] ,\
#                  jumbo_flag=True, apa= apa )
#########    asicrms = asic_wf_plot_coh(out_path, asic_results, wiretype = "U")
#########    asic_coh_plot_wire(out_path, asic_results, wiretype = "V")
########if asicno in [0,1,4,5]:
########    asic_coh_plot_wire(out_path, asic_results, wiretype = "X")
########else:
########    asic_coh_plot_wire(out_path, asic_results, wiretypes = "UV")
#    asic_coh_plot_wire(out_path, asic_results, wiretypes = "X")
#    asic_coh_plot_wire(out_path, asic_results, wiretypes = "U")
#    asic_coh_plot_wire(out_path, asic_results, wiretypes = "V")

#    asic_wf_plot_coh(out_path, asic_results, wiretype = "U")
#    asic_wf_plot_wire(out_path, asic_results, wiretype = "U")
#    asic_wf_plot_wire(out_path, asic_results, wiretype = "V")
#    asic_wf_plot_wire(out_path, asic_results, wiretype = "X")

#    asic_fft_plot_wire(out_path, asic_results, wiretype = "U")
#    asic_fft_plot_wire(out_path, asic_results, wiretype = "V")
#    asic_fft_plot_wire(out_path, asic_results, wiretype = "X")
    print "Done, please punch \"Eneter\" or \"return\" if necessary! "

 


