# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Nov 19 10:07:37 2017
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
from matplotlib.backends.backend_pdf import PdfPages
from timeit import default_timer as timer

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

import time
import datetime

def apa_noise(all_chn_results, wiretype="X", sf = False):
    rms_np = []
    for onechn_results in all_chn_results:
        if (onechn_results[2][0] == wiretype ):
            if (sf == False):
                rms_np.append(onechn_results[11])
            else:
                rms_np.append(onechn_results[13])
    rms_np = np.array(rms_np)
    rms = np.mean(rms_np)
    errbar = np.std(rms_np)
    return rms, errbar

def noise_plot(path, time_np, strtime_np, xrms_np, xrms_errbar_np, vrms_np, vrms_errbar_np, urms_np, urms_errbar_np, temper_time_np, temper_femb0_np, temper_femb1_np, temper_femb2_np, temper_femb3_np, gain=3, enc_flg = "False" ):
    plt.figure(figsize=(16,9))
    ax = plt.subplot2grid((1, 1), (0, 0))

    temper_time_np = ( np.array(temper_time_np) - np.min(time_np) ) / 3600.0
    time_np = ( np.array(time_np) - np.min(time_np) ) /3600.0

    xrms_np        = np.array(xrms_np)
    xrms_errbar_np = np.array(xrms_errbar_np)
    vrms_np        = np.array(vrms_np)
    vrms_errbar_np = np.array(vrms_errbar_np)
    urms_np        = np.array(urms_np)
    urms_errbar_np = np.array(urms_errbar_np)

#    temper_femb0_np = ( np.array( temper_femb0_np ) - 873 ) / 2.868 
#    temper_femb1_np = ( np.array( temper_femb1_np ) - 873 ) / 2.868 
#    temper_femb2_np = ( np.array( temper_femb2_np ) - 873 ) / 2.868 
#    temper_femb3_np = ( np.array( temper_femb3_np ) - 873 ) / 2.868 

    if gain ==3:
        encgain = 80
    elif(gain ==2): 
        encgain = 145 

    if enc_flg == True:
        xrms_np        =     xrms_np        * encgain 
        xrms_errbar_np =     xrms_errbar_np * encgain 
        vrms_np        =     vrms_np        * encgain 
        vrms_errbar_np =     vrms_errbar_np * encgain 
        urms_np        =     urms_np        * encgain 
        urms_errbar_np =     urms_errbar_np * encgain 
        yrange = [0,1500]
    else:
        yrange = [0,20]

    clor = ['g','b', 'r']
    mker = ['o','*','^','x','d','+','s','8',"1","2"]
    patch = []
    label = []
    wire_type_np = [ "X", "U", "V"]

    wire_np = [["X plane",xrms_np, xrms_errbar_np], ["V plane",vrms_np, vrms_errbar_np], ["U plane",urms_np, urms_errbar_np]]

    markerno = 0
    for onewire in wire_np:
        ax.errorbar(time_np, onewire[1], onewire[2], color = clor[markerno], marker = mker[markerno])
        patch.append( mpatches.Patch(color = clor[markerno]))
        label.append("ENC of %s"%(onewire[0] ))
        if (markerno  == 0 ):
            runlen = len(time_np)
            for runtmp in range(0,runlen,10):
                ax.text( time_np[runtmp], xrms_np[runtmp]*0.9 , "%s"%strtime_np[runtmp], fontsize=8) 
        markerno = markerno + 1

    ax.legend(patch, label, loc=3, fontsize=12 )
    ax.tick_params(labelsize=12)
    ax.set_ylim(yrange)
    ax.set_xlim([np.min(time_np),np.max(time_np)])
    if enc_flg == True:
        ax.set_ylabel("ENC /e-", fontsize=12)
        ax.set_title("ENC (Gain = 25mV/fC, Tp = 2us) and Temperature", fontsize=12 )
    else:
        ax.set_ylabel("ADC /bin", fontsize=12)
        ax.set_title("Noise Level (Gain = 25mV/fC, Tp = 2us) and Temperature", fontsize=12 )

    ax.set_xlabel("Time / hour", fontsize=12)
    ax.grid()

    ax2 = ax.twinx()
    ax2patch = []
    ax2label = []
    ax2.scatter(temper_time_np, temper_femb0_np, color = 'tab:orange', marker = 'x')
    ax2patch.append( mpatches.Patch(color = 'tab:orange') )
    ax2label.append( "Temperature of TT0907" )
#    ax2.scatter(temper_time_np, temper_femb1_np, color = 'tab:purple', marker = 'x')
#    ax2patch.append( mpatches.Patch(color = 'tab:purple') )
#    ax2label.append( "Temperature on WIB5FEMB1CHIP0" )
#    ax2.scatter(temper_time_np, temper_femb2_np, color = 'tab:brown', marker = 'x')
#    ax2patch.append( mpatches.Patch(color = 'tab:brown') )
#    ax2label.append( "Temperature on WIB5FEMB2CHIP0" )
#    ax2.scatter(temper_time_np, temper_femb3_np, color = 'tab:olive', marker = 'x')
#    ax2patch.append( mpatches.Patch(color = 'tab:olive') )
#    ax2label.append( "Temperature on WIB5FEMB3CHIP0" )
    ax2.legend(ax2patch, ax2label, loc=4, fontsize=12 )

    ax2.plot(temper_time_np, temper_femb0_np, color =  'tab:orange', marker = 'x')
#    ax2.plot(temper_time_np, temper_femb1_np, color =  'tab:purple', marker = 'x')
#    ax2.plot(temper_time_np, temper_femb2_np, color =  'tab:brown', marker = 'x')
#    ax2.plot(temper_time_np, temper_femb3_np, color =  'tab:olive', marker = 'x')
    ax2.set_ylabel('Temperature / $^\circ$C', color='tab:orange', fontsize=12)
    ax2.tick_params('y', colors='tab:orange')
    ax2.set_ylim([-250, 50])
    ax2.set_xlim([np.min(time_np)-1,np.max(time_np)+2])

    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
#    plt.show()
    if enc_flg == True:
        print path+"encnoise.png"
        plt.savefig(path+"M10_encnoise.png", format='png')
    else:
        print path+"adcnoise.png"
        plt.savefig(path+"M10_adcnoise.png", format='png')
    plt.close()


strmonth = sys.argv[1] #"11-12"
strdate = sys.argv[2] #"13-14"
gain = int(sys.argv[3]) #"2"
server_flg = sys.argv[4]

#prepath = "/Volumes/ProtoDUNE/CERN_Test_backup/Rawdata_"
#prepath = "/Users/shanshangao/Documents/Share_Windows/CERN_test_stand/Rawdata/Rawdata_"
if (server_flg == "server" ):
    prepath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Rawdata_"
else:
    #prepath = "/Users/shanshangao/Documents/Share_Windows/CERN_test_stand/Rawdata/Rawdata_"
    prepath = "/Volumes/ProtoDUNE/CERN_Test_backup/Rawdata_"

month_np = []
for tmp in range(0, len(strmonth), 3):
    month_np.append(strmonth[tmp:tmp+2])

date_np = []
for tmp in range(0, len(strdate), 3):
    date_np.append(strdate[tmp:tmp+2])

path_np = []
for onemonth in month_np:
    for onedate in date_np:
        path = prepath + onemonth + "_" + onedate + "_2017"
        path_np.append(path)

runinfo_np = []
temper_info_np = []
for onepath in path_np:
    for root, dirs, files in os.walk(onepath):
        break   
    for rundir in dirs:
        onerunpath = onepath + "/" + rundir
        readmefile = onerunpath + "/" + rundir + "_readme.txt"

        if os.path.isfile(readmefile):
            with open(readmefile, 'r') as f:
                runtime = f.readline()[0:-1]                
                runapa = f.readline()[0:-1]                
                runenv = f.readline()[0:-1]                
                runno = f.readline()[0:-1]                
                runpath = f.readline()[0:-1]                
                runpath = onepath + "/"
                runcode = f.readline()[0:-1]                
                pos = runcode.find("code#")
                timestamp = long( time.mktime(datetime.datetime.strptime(runtime, "%Y-%m-%d %H:%M:%S").timetuple()) )
                if ( runcode[pos+5:pos+7] == "00" ):
                    runinfo_np.append([timestamp, runtime, runapa, runenv, runno, runpath, runcode] )

    for rundir in dirs:
        onerunpath = onepath + "/" + rundir
        readmefile = onerunpath + "/" + "Temperature_record.txt"
        if os.path.isfile(readmefile):
            with open(readmefile, 'r') as f:
                runtime = f.readline()[0:-2]                
                timestamp = long( time.mktime(datetime.datetime.strptime(runtime, "%Y-%m-%d %H:%M:%S").timetuple()) )
                fembno  = f.readline()[0:-1]                
                t_chip0 = f.readline()[0:-1]                
                t_chip1 = f.readline()[0:-1]                
                t_chip2 = f.readline()[0:-1]                
                t_chip3 = f.readline()[0:-1]                
                t_chip4 = f.readline()[0:-1]                
                t_chip5 = f.readline()[0:-1]                
                t_chip6 = f.readline()[0:-1]                
                t_chip7 = f.readline()[0:-1]                
                t_chip0 = t_chip0
                if (t_chip0[0:5] == "chip0"):
                    t_chip0 = [int(t_chip0[6:9]), int(t_chip0[10:13]), int(t_chip0[14:17]), int(t_chip0[18:21]) ] 
                    temper_info_np.append([timestamp, runtime, t_chip0])

runinfo_np = sorted(runinfo_np, key= lambda tup:tup[0])
            
time_np = []
strtime_np = []
xrms_np = []
xrms_errbar_np = []
vrms_np = []
vrms_errbar_np = []
urms_np = []
urms_errbar_np = []

sfxrms_np = []
sfxrms_errbar_np = []
sfvrms_np = []
sfvrms_errbar_np = []
sfurms_np = []
sfurms_errbar_np = []

bias_run = [
            "/Rawdata_11_13_2017/run01",
            "/Rawdata_11_13_2017/run04",
            "/Rawdata_11_15_2017/run16",
            "/Rawdata_11_15_2017/run17",
            "/Rawdata_11_15_2017/run18",
            "/Rawdata_11_15_2017/run19",
            "/Rawdata_11_15_2017/run20",
            "/Rawdata_11_15_2017/run21",
            "/Rawdata_11_15_2017/run27",
            "/Rawdata_11_15_2017/run29", 
            "/Rawdata_11_15_2017/run31", 
            "/Rawdata_11_15_2017/run32", 
#            "/Rawdata_11_15_2017/run34", 
#            "/Rawdata_11_15_2017/run35", 
            "/Rawdata_11_15_2017/run37", 
            "/Rawdata_11_15_2017/run38", 
            "/Rawdata_11_15_2017/run39", 
            "/Rawdata_11_15_2017/run40", 
            "/Rawdata_11_15_2017/run42", 
            "/Rawdata_11_15_2017/run44", 
            "/Rawdata_11_16_2017/run01", 
            "/Rawdata_11_16_2017/run03", 
            "/Rawdata_11_16_2017/run05", 
            "/Rawdata_11_16_2017/run06", 
            "/Rawdata_11_16_2017/run07", 
            "/Rawdata_11_16_2017/run08", 
            "/Rawdata_11_16_2017/run09", 
            "/Rawdata_11_16_2017/run10", 
            "/Rawdata_11_16_2017/run11", 
            "/Rawdata_11_16_2017/run12", 
            "/Rawdata_11_16_2017/run13", 
            "/Rawdata_11_16_2017/run14", 
            "/Rawdata_11_16_2017/run15", 
            "/Rawdata_11_16_2017/run16", 
        ]
for runinfo in runinfo_np :
    runinfo_path = runinfo[5] + runinfo[4] + "/"
    for runroot, rundirs, runfiles in os.walk(runinfo_path):
        break   
    for runfile in runfiles:
        if (runfile.find("gain" + str(gain) + "_results.bin")>=0):
            break

    bias_on = False
    if (runfile.find("gain" + str(gain) + "_results.bin") >= 0):
        for onebias in bias_run:
            if ( runinfo_path.find(onebias) >= 0 ):
                bias_on = True
                break

    if (runfile.find("gain" + str(gain) + "_results.bin") >= 0) and ( bias_on == False) :
        binfile = runinfo_path + runfile
        if os.path.isfile(binfile):
            import pickle
            with open (binfile, 'rb') as fp:
                print binfile
                all_chn_results = pickle.load(fp)

                time_np.append(runinfo[0])
                strtime_np.append(runinfo[1])
                tmp1, tmp2 = apa_noise(all_chn_results, wiretype="X", sf = False)
                xrms_np.append(tmp1)
                xrms_errbar_np.append(tmp2)
                tmp1, tmp2 = apa_noise(all_chn_results, wiretype="V", sf = False)
                vrms_np.append(tmp1)
                vrms_errbar_np.append(tmp2)
                tmp1, tmp2 = apa_noise(all_chn_results, wiretype="U", sf = False)
                urms_np.append(tmp1)
                urms_errbar_np.append(tmp2)
            
                tmp1, tmp2 = apa_noise(all_chn_results, wiretype="X", sf = True)
                sfxrms_np.append(tmp1)
                sfxrms_errbar_np.append(tmp2)
                tmp1, tmp2 = apa_noise(all_chn_results, wiretype="V", sf = True)
                sfvrms_np.append(tmp1)
                sfvrms_errbar_np.append(tmp2)
                tmp1, tmp2 = apa_noise(all_chn_results, wiretype="U", sf = True)
                sfurms_np.append(tmp1)
        else:
            print "ERROR load bin file"
            sys.exit()

temper_info_np =  sorted(temper_info_np, key= lambda tup:tup[0])
temper_time_np = []
temper_femb0_np = []
temper_femb1_np = []
temper_femb2_np = []
temper_femb3_np = []

temper_info_tmp = [ 
                    [ "2017-11-13 12:43:00", 25.6 ],
                    [ "2017-11-13 14:27:00", 26.9 ],
                    [ "2017-11-13 16:28:00", 21.0 ],
                    [ "2017-11-13 17:25:00", 13.9 ],
                    [ "2017-11-13 19:05:00", 0.1  ],
                    [ "2017-11-13 22:37:00", -31  ],
                    [ "2017-11-13 23:01:00", -37,3],
                    [ "2017-11-13 23:58:00", -50  ],
                    [ "2017-11-14 00:37:00", -57.5],
                    [ "2017-11-14 08:49:00", -80.7],
                    [ "2017-11-14 11:01:00", -79  ],
                    [ "2017-11-14 12:01:00", -77.8],
                    [ "2017-11-14 15:47:00", -71.3],
                    [ "2017-11-14 17:59:00", -69  ],
                    [ "2017-11-14 22:18:00", -63.4],
                    [ "2017-11-15 10:07:00", -59.3],
                    [ "2017-11-15 13:48:00", -58.9],
                    [ "2017-11-15 17:07:00", -59.6],
                    [ "2017-11-17 11:00:00", -70  ],
                    [ "2017-11-17 12:00:00", -80  ],
                    [ "2017-11-17 13:00:00", -88  ],
                    [ "2017-11-17 14:00:00", -96  ],
                    [ "2017-11-17 15:00:00", -100 ],
                    [ "2017-11-17 16:00:00", -100 ],
                    [ "2017-11-17 17:00:00", -95  ],
                    [ "2017-11-17 18:00:00", -70  ],
                    [ "2017-11-18 07:00:00", -19  ],
                    [ "2017-11-19 03:00:00", 20   ],
                    ]

temper_info_tmp2 = []
for onetemp in temper_info_tmp:
    temp_time_stamp = long( time.mktime(datetime.datetime.strptime(onetemp[0], "%Y-%m-%d %H:%M:%S").timetuple()) )
    temper_info_tmp2.append([temp_time_stamp, onetemp[0], onetemp[1]])

for one_temper_info in temper_info_tmp2:
    temper_time_np.append(one_temper_info[0]) 
    temper_femb0_np.append(one_temper_info[2])


noise_plot(runinfo[5], time_np, strtime_np, xrms_np, xrms_errbar_np, vrms_np, vrms_errbar_np, urms_np, urms_errbar_np, temper_time_np, temper_femb0_np, temper_femb1_np, temper_femb2_np, temper_femb3_np, gain=gain, enc_flg = True )
noise_plot(runinfo[5], time_np, strtime_np, xrms_np, xrms_errbar_np, vrms_np, vrms_errbar_np, urms_np, urms_errbar_np, temper_time_np, temper_femb0_np, temper_femb1_np, temper_femb2_np, temper_femb3_np, gain=gain, enc_flg = False )

