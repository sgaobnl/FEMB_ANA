# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Fri 25 May 2018 05:27:42 AM CEST
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
from temperature import temp_fit
from readlog import readlog
from read_rtds import run_rtds


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

def noise_plot(path, chkruns_cs, time_np, strtime_np, xrms_np, xrms_errbar_np, vrms_np, vrms_errbar_np, urms_np, urms_errbar_np, \
               temperrtdts_np, temperrtd0_np, temperrtd1_np, temperrtd2_np, temperrtd3_np, temperrtd4_np, temperrtd5_np, temperrtd6_np,\
               temper_time_np, temper_femb0_np, temper_femb1_np, temper_femb2_np, temper_femb3_np, \
               gain=3, tp=2,  enc_flg = True, sf_flg = False ):

    plt.figure(figsize=(12,8))
    ax = plt.subplot2grid((1, 1), (0, 0))

    rtd_time_np = ( np.array(temperrtdts_np) - np.min(time_np) ) / 3600.0
    if FE_temper_flg == True :
        temper_time_np = ( np.array(temper_time_np) - np.min(time_np) ) / 3600.0
    time_np = ( np.array(time_np) - np.min(time_np) ) /3600.0

    xrms_np        = np.array(xrms_np)
    xrms_errbar_np = np.array(xrms_errbar_np)
    vrms_np        = np.array(vrms_np)
    vrms_errbar_np = np.array(vrms_errbar_np)
    urms_np        = np.array(urms_np)
    urms_errbar_np = np.array(urms_errbar_np)

    if (FE_temper_flg == True ):
        deg_per_mv, cconstant = temp_fit ()
        temper_femb0_np = (( np.array( temper_femb0_np ) * deg_per_mv ) + cconstant ) 
        temper_femb1_np = (( np.array( temper_femb1_np ) * deg_per_mv ) + cconstant ) 
        temper_femb2_np = (( np.array( temper_femb2_np ) * deg_per_mv ) + cconstant ) 
        temper_femb3_np = (( np.array( temper_femb3_np ) * deg_per_mv ) + cconstant ) 

    if gain == 3:
        if tp ==1 : #0.5us
            egain = 83
            strtp = "0.5"
        elif tp ==0 : #1.0us
            egain = 78
            strtp = "1.0"
        elif tp ==3 : #2.0us
            egain = 77
            strtp = "2.0"
        else: #3.0us
            egain = 76
            strtp = "3.0"
    if gain == 2:
        egain = 145
    if gain == 1:
        egain = 250
    if gain == 0:
        egain = 425

    if enc_flg == True:
        xrms_np        =     xrms_np        * egain 
        xrms_errbar_np =     xrms_errbar_np * egain 
        vrms_np        =     vrms_np        * egain 
        vrms_errbar_np =     vrms_errbar_np * egain 
        urms_np        =     urms_np        * egain 
        urms_errbar_np =     urms_errbar_np * egain 
        yrange = [0,2000]
    else:
        yrange = [0,20]

    clor = ['g','b', 'r']
    mker = ['o','*','^','x','d','+','s','8',"1","2"]
    patch = []
    label = []
    wire_type_np = [ "X", "U", "V"]

    wire_np = [["X plane",xrms_np, xrms_errbar_np], ["V plane",vrms_np, vrms_errbar_np], ["U plane",urms_np, urms_errbar_np]]
    minxrms = np.min(xrms_np)
    minxrms_pos = np.where(xrms_np == minxrms)[0][0]
    minvrms = np.min(vrms_np)
    minvrms_pos = np.where(vrms_np == minvrms)[0][0]
    minurms = np.min(urms_np)
    minurms_pos = np.where(urms_np == minurms)[0][0]

    markerno = 0
    ax2 = ax.twinx()
    ax2patch = []
    ax2label = []
#    ax2.plot(rtd_time_np, temperrtd0_np, color = 'tab:orange' )
#    ax2.plot(rtd_time_np, temperrtd1_np, color = 'tab:orange' )
#    ax2.plot(rtd_time_np, temperrtd2_np, color = 'tab:orange' )
#    ax2.plot(rtd_time_np, temperrtd3_np, color = 'tab:orange' )
#    ax2.plot(rtd_time_np, temperrtd4_np, color = 'tab:orange' )
#    ax2.plot(rtd_time_np, temperrtd5_np, color = 'tab:orange' )
    ax2.plot(rtd_time_np, temperrtd6_np, color = 'tab:orange' )
#    ax2.scatter(rtd_time_np, temperrtd0_np, color = 'b',           marker = '1', label = "TT0200 (K)")
#    ax2.scatter(rtd_time_np, temperrtd1_np, color = 'g',           marker = '2', label = "TT0201 (K)")
#    ax2.scatter(rtd_time_np, temperrtd2_np, color = 'c',           marker = '4', label = "TT0202 (K)")
#    ax2.scatter(rtd_time_np, temperrtd3_np, color = 'm',           marker = '8', label = "TT0203 (K)")
#    ax2.scatter(rtd_time_np, temperrtd4_np, color = 'y',           marker = 's', label = "TT0204 (K)")
#    ax2.scatter(rtd_time_np, temperrtd5_np, color = 'tab:orange',  marker = '+', label = "TT0205 (K)")
    ax2.scatter(rtd_time_np, temperrtd6_np, color = 'r',           marker = '+', label = "RTD TT0206 (K)")
    ax2.legend(loc = 1, fontsize=16 )

    if (FE_temper_flg == True):
        ax2.scatter(temper_time_np, temper_femb0_np, color = 'tab:orange', marker = 'x')
        ax2patch.append( mpatches.Patch(color = 'tab:orange') )
        ax2label.append( "Temperature on WIB5FEMB0" )
        ax2.scatter(temper_time_np, temper_femb1_np, color = 'tab:purple', marker = 'x')
        ax2patch.append( mpatches.Patch(color = 'tab:purple') )
        ax2label.append( "Temperature on WIB5FEMB1" )
        ax2.scatter(temper_time_np, temper_femb2_np, color = 'tab:brown', marker = 'x')
        ax2patch.append( mpatches.Patch(color = 'tab:brown') )
        ax2label.append( "Temperature on WIB5FEMB2" )
        ax2.scatter(temper_time_np, temper_femb3_np, color = 'tab:olive', marker = 'x')
        ax2patch.append( mpatches.Patch(color = 'tab:olive') )
        ax2label.append( "Temperature on WIB5FEMB3" )
        ax2.legend(ax2patch, ax2label, loc=4, fontsize=16 )
    
        ax2.plot(temper_time_np, temper_femb0_np, color =  'tab:orange', marker = 'x')
        ax2.plot(temper_time_np, temper_femb1_np, color =  'tab:purple', marker = 'x')
        ax2.plot(temper_time_np, temper_femb2_np, color =  'tab:brown', marker = 'x')
        ax2.plot(temper_time_np, temper_femb3_np, color =  'tab:olive', marker = 'x')
    ax2.set_ylabel('Temperature / K', color='tab:orange', fontsize=16)
    ax2.tick_params('y',labelsize=16, colors='tab:orange')
    ax2.set_ylim([-50, 350])
    ax2.set_xlim([np.min(time_np)-1,np.max(time_np)+2])


    for onewire in wire_np:
        ax.errorbar(time_np, onewire[1], onewire[2], color = clor[markerno], marker = mker[markerno])
        if enc_flg == True:
            if (onewire[0][0] == "X" ):
                ax.text( time_np[minxrms_pos]*0.65, yrange[1]*0.88, "X plane lowest noise = %d$\pm$%d e$^-$"%(onewire[1][minxrms_pos], onewire[2][minxrms_pos]), color = clor[markerno], fontsize=16) 
            elif (onewire[0][0] == "U" ):                                                                                                          
                ax.text( time_np[minxrms_pos]*0.65, yrange[1]*0.76, "U plane lowest noise = %d$\pm$%d e$^-$"%(onewire[1][minurms_pos], onewire[2][minurms_pos]), color = clor[markerno], fontsize=16) 
            elif (onewire[0][0] == "V" ):                                                                                                          
                ax.text( time_np[minxrms_pos]*0.65, yrange[1]*0.82, "V plane lowest noise = %d$\pm$%d e$^-$"%(onewire[1][minvrms_pos], onewire[2][minvrms_pos]), color = clor[markerno], fontsize=16) 

        patch.append( mpatches.Patch(color = clor[markerno]))
        label.append("ENC of %s"%(onewire[0] ))
#        if (markerno  == 0 ):
#            ax.text( time_np[0], yrange[1]*0.95 , "$\leftarrow$%s"%strtime_np[0], fontsize=10) 
#            runlen = len(time_np)
    #        for runtmp in range(1,runlen,1):
    #            if (strtime_np[runtmp][0:10] != strtime_np[runtmp-1][0:10] ):
    #                ax.text( time_np[runtmp], yrange[1]*0.95 , "$\leftarrow$%s"%strtime_np[runtmp], fontsize=10) 
        markerno = markerno + 1

    ax.legend(patch, label, loc=3, fontsize=16 )
    ax.tick_params(labelsize=16)
    ax.set_ylim(yrange)
    ax.set_xlim([np.min(time_np),np.max(time_np)])
    if enc_flg == True:
        ax.set_ylabel("ENC / e$^-$", fontsize=16)
        ax.set_title("ENC (Gain = 25mV/fC, Tp = %s$\mu$s) vs. Temperature"%strtp, fontsize=16 )
    else:
        ax.set_ylabel("ADC /bin", fontsize=16)
        ax.set_title("Noise", fontsize=16 )

    ax.set_xlabel("Time / hour", fontsize=16)
    ax.grid()


    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    if enc_flg == True:
        if (sf_flg == True):
            pngfile =  "APA" + "gain" + str(gain) + "tp" + str(tp) + "sf_encnoise.png"
            plt.savefig(path+pngfile, format='png')
        else:
            pngfile =  "APA" + "gain" + str(gain) + "tp" + str(tp) + "encnoise.png"
            print path+ pngfile
            plt.savefig(path+ pngfile, format='png')
    else:
        pngfile =  "APA" + "gain" + str(gain) + "tp" + str(tp) + "adcnoise.png"
        plt.savefig(path+pngfile, format='png')
    plt.close()

strmonths = sys.argv[1] #"11-12"
strdates = sys.argv[2] #"13-14"
gain = int(sys.argv[3]) #"2"
tp = int(sys.argv[4])
APAno = int(sys.argv[5])
server_flg = sys.argv[6]
stryear = sys.argv[7] #"2018"
FE_temper_flg = ( sys.argv[8] == True )

if (server_flg == "server" ):
    #rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/"
    rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA2/"
else:
    rootpath = "/Users/shanshangao/Documents/Share_Windows/CERN_test_stand/Rawdata/"
prepath = rootpath + "Rawdata_"
rtdsfile = rootpath + "APA2_cooldown_RTDsdata.csv" 

month_np = []
for tmp in range(0, len(strmonths), 3):
    month_np.append(strmonths[tmp:tmp+2])

date_np = []
for tmp in range(0, len(strdates), 3):
    date_np.append(strdates[tmp:tmp+2])

rundatepaths = []
for onemonth in month_np:
    for onedate in date_np:
        rundate = onemonth + "_" + onedate + "_" + "2018"
        rundatepaths.append(rundate)

chkruns = []
tmpdirs = []
temper_info_np =[]
for rundate in rundatepaths:
    resultpath = prepath + rundate + "/results/"
    for root, dirs, files in os.walk(resultpath):
        break   
    for chkdir in dirs:
        if (chkdir.find("chk") > 0 ):
            strrunno = chkdir[3:5]
            loginfo = readlog(rootpath=rootpath, APAno=APAno, runtime = rundate, runno = strrunno, runtype = "chk") 
            run_temp = run_rtds(filepath=rtdsfile, runtime =loginfo[6]) 
            chkrun_ts = long( time.mktime(datetime.datetime.strptime(loginfo[6], "%Y-%m-%d %H:%M:%S").timetuple()) )
            chkruns.append( [resultpath, chkdir, loginfo, run_temp, chkrun_ts] ) 

    rundatepath = prepath + rundate  
    for root, dirs, files in os.walk(rundatepath):
        break   
    for tmpdir in dirs:
        if (tmpdir.find("tmp") > 0 ):
            tmpdirs.append(root + '/' + tmpdir)
    for tmpdir in tmpdirs:
        readmefile = tmpdir + "/" + "Temperature_record.txt"
        if (os.path.isfile(readmefile)) and (FE_temper_flg == True) :
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
                if (t_chip0[0:5] == "chip0"):
                    t_chip0 = [int(t_chip0[6:9]), int(t_chip0[10:13]), int(t_chip0[14:17]), int(t_chip0[18:21]), "chip0" ] 
                if (t_chip1[0:5] == "chip1"):
                    t_chip1 = [int(t_chip1[6:9]), int(t_chip1[10:13]), int(t_chip1[14:17]), int(t_chip1[18:21]), "chip1" ] 
                if (t_chip2[0:5] == "chip2"):
                    t_chip2 = [int(t_chip2[6:9]), int(t_chip2[10:13]), int(t_chip2[14:17]), int(t_chip2[18:21]), "chip2" ] 
                if (t_chip3[0:5] == "chip3"):
                    t_chip3 = [int(t_chip3[6:9]), int(t_chip3[10:13]), int(t_chip3[14:17]), int(t_chip3[18:21]), "chip3" ] 
                if (t_chip4[0:5] == "chip4"):
                    t_chip4 = [int(t_chip4[6:9]), int(t_chip4[10:13]), int(t_chip4[14:17]), int(t_chip4[18:21]), "chip4" ] 
                if (t_chip5[0:5] == "chip5"):
                    t_chip5 = [int(t_chip5[6:9]), int(t_chip5[10:13]), int(t_chip5[14:17]), int(t_chip5[18:21]), "chip5" ] 
                if (t_chip6[0:5] == "chip6"):
                    t_chip6 = [int(t_chip6[6:9]), int(t_chip6[10:13]), int(t_chip6[14:17]), int(t_chip6[18:21]), "chip6" ] 
                if (t_chip7[0:5] == "chip7"):
                    t_chip7 = [int(t_chip7[6:9]), int(t_chip7[10:13]), int(t_chip7[14:17]), int(t_chip7[18:21]), "chip7" ] 

                if ( (t_chip0[4] == "chip0") and (t_chip1[4] == "chip1") and (t_chip2[4] == "chip2") and (t_chip3[4] == "chip3") 
                   and (t_chip4[4] == "chip4") and (t_chip5[4] == "chip5") and (t_chip6[4] == "chip6") and (t_chip7[4] == "chip7") ):
                    t_femb0 = (t_chip0[0] + t_chip1[0] + t_chip2[0] + t_chip3[0] + t_chip4[0] + t_chip5[0] + t_chip6[0] + t_chip7[0])/8.0
                    t_femb1 = (t_chip0[1] + t_chip1[1] + t_chip2[1] + t_chip3[1] + t_chip4[1] + t_chip5[1] + t_chip6[1] + t_chip7[1])/8.0
                    t_femb2 = (t_chip0[2] + t_chip1[2] + t_chip2[2] + t_chip3[2] + t_chip4[2] + t_chip5[2] + t_chip6[2] + t_chip7[2])/8.0
                    t_femb3 = (t_chip0[3] + t_chip1[3] + t_chip2[3] + t_chip3[3] + t_chip4[3] + t_chip5[3] + t_chip6[3] + t_chip7[3])/8.0

                    t_femb = [int(t_femb0), int(t_femb1), int(t_femb2), int(t_femb3)]

                    temper_info_np.append([timestamp, runtime, t_femb])

chkruns =  sorted(chkruns, key= lambda tup:tup[4])

#runinfo_np = []
#runinfo_np.append([timestamp, runtime, runapa, runenv, runno, runpath, runcode] )

chkruns_cs = []
time_np = []
temperrtdts_np = []
temperrtd0_np = []
temperrtd1_np = []
temperrtd2_np = []
temperrtd3_np = []
temperrtd4_np = []
temperrtd5_np = []
temperrtd6_np = []
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

del_run = [

            ["Rawdata_01_15_2018",  "run01chk",] ,
            ["Rawdata_01_15_2018",  "run02chk",] ,
            ["Rawdata_01_15_2018",  "run03chk",] ,
            ["Rawdata_01_15_2018",  "run04chk",] ,
            ["Rawdata_01_15_2018",  "run05chk",] ,
            ["Rawdata_01_15_2018",  "run06chk",] ,
            ["Rawdata_01_16_2018",  "run10chk",] ,
            ["Rawdata_01_17_2018",  "run10chk",] ,
            ["Rawdata_01_17_2018",  "run11chk",] ,
            ["Rawdata_01_17_2018",  "run12chk",] ,
            ["Rawdata_01_18_2018",  "run03chk",] ,
            ["Rawdata_01_18_2018",  "run04chk",] ,
            ["Rawdata_01_18_2018",  "run05chk",] ,

#            ["Rawdata_02_06_2018",  "run13chk",] ,
#            ["Rawdata_02_06_2018",  "run19chk",] ,
#            ["Rawdata_02_07_2018",  "run03chk",] ,
#            ["Rawdata_02_07_2018",  "run04chk",] ,
#            ["Rawdata_02_07_2018",  "run05chk",] ,
#            ["Rawdata_02_07_2018",  "run06chk",] ,
        ]


for chkrun in chkruns:
    chkrunpath = chkrun[0] + chkrun[1] + "/"
    for runroot, rundirs, runfiles in os.walk(chkrunpath):
        break   
    for runfile in runfiles:
        filepat = "gain" + str(gain) + "_tp" + str(tp) + "_results.bin"
        if (runfile.find(filepat)>=0):
            break

    binfile = chkrunpath + runfile
    del_on = False
    if (runfile.find(filepat) >= 0):
        for onebias in del_run:
            if ( binfile.find(onebias[0] ) >= 0 ) and ( binfile.find(onebias[1] ) >= 0 ):
                del_on = True
                break

    if (runfile.find(filepat) >= 0) and ( del_on == False) :
        if os.path.isfile(binfile):
            import pickle
            with open (binfile, 'rb') as fp:
                print binfile
                chkruns_cs.append(chkrun)
                all_chn_results = pickle.load(fp)
                runts = time.mktime(datetime.datetime.strptime(chkrun[2][6], "%Y-%m-%d %H:%M:%S").timetuple())
                time_np.append(runts)
                temperrtdts_np.append(chkrun[3][0] ) 
                temperrtd0_np.append(chkrun[3][1] ) 
                temperrtd1_np.append(chkrun[3][2] ) 
                temperrtd2_np.append(chkrun[3][3] ) 
                temperrtd3_np.append(chkrun[3][4] ) 
                temperrtd4_np.append(chkrun[3][5] ) 
                temperrtd5_np.append(chkrun[3][6] ) 
                temperrtd6_np.append(chkrun[3][7] ) 
                strtime_np.append(chkrun[2][6])
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
                sfurms_errbar_np.append(tmp2)
        else:
            print binfile
            print "ERROR load bin file"
            sys.exit()


temper_time_np = []
temper_femb0_np = []
temper_femb1_np = []
temper_femb2_np = []
temper_femb3_np = []
if (FE_temper_flg == True):
    temper_info_np =  sorted(temper_info_np, key= lambda tup:tup[0])
    for one_temper_info in temper_info_np:
        temper_time_np.append(one_temper_info[0]) 
        temper_femb0_np.append(one_temper_info[2][0])
        temper_femb1_np.append(one_temper_info[2][1])
        temper_femb2_np.append(one_temper_info[2][2])
        temper_femb3_np.append(one_temper_info[2][3])

noise_plot(rootpath, chkruns_cs, time_np, strtime_np, xrms_np, xrms_errbar_np, vrms_np, vrms_errbar_np, urms_np, urms_errbar_np, \
           temperrtdts_np, temperrtd0_np, temperrtd1_np, temperrtd2_np, temperrtd3_np, temperrtd4_np, temperrtd5_np, temperrtd6_np,\
           temper_time_np, temper_femb0_np, temper_femb1_np, temper_femb2_np, temper_femb3_np, \
           gain=3, tp=tp,  enc_flg = True, sf_flg = False )


