# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Aug 26 23:08:10 2018
"""
import matplotlib
#matplotlib.use('Agg')
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

def read_wib_log(rootpath):
    filepath = rootpath + "WIB_lins_chk.log"
    if os.path.isfile(filepath):
        with open(filepath,"r") as f:
            testruns = []
            onerun = []
            for line in f:
                if (line.find("##Begin") >=0 ):
                    if (len(onerun) > 10 ):
                        testruns.append(onerun)
                    onerun = []
                else:
                    onerun.append(line)
    else:
        print "%s, file doesn't exist!!!"%file_setadc_rec
        sys.exit()
    return testruns

def read_cv_log(testruns, ts = "BNL_check_time", con = "BNL_WIB1_FEMB0_AM36V", tbegin="2018-07-23 20:31:02", tlast=100, ip = "192.168.100.11"):
    tt = []
    vv = []
    ii = []
    tbs = long( time.mktime(datetime.datetime.strptime(tbegin, "%Y-%m-%d %H:%M:%S").timetuple()) )
    for a in testruns:
        tss = [] 
        for b in range(len(a )):
            if a[b].find(ts )>= 0:
                tss.append(b) 
        twd = tss[1]-tss[0]

        tip = 0
        for b in range(len(a )):
            if a[b].find("BNL_WIB1_IP") >= 0:
                if a[b].find(ip) >= 0:
                    tip = b

        tts = 0
        for b in a[tip-1:tip-1+twd]:
            if b.find(ts) >= 0:
                tpos = b.find(">>")
                tstr = b[tpos+3:tpos+3+19]
                tts = long( time.mktime(datetime.datetime.strptime(tstr, "%Y-%m-%d %H:%M:%S").timetuple()) )

            if b.find (con) >= 0:
                vpos = b.find ("V : " )
                v = float(b[vpos+4 : vpos+9])
                ipos = b.find ("V, " )
                i = float(b[ipos+3 : ipos+8])
        if (tts > tbs) and (tts < (tbs+tlast)):
            tt.append([tts])
            vv.append([v])
            ii.append([i])
    ii = np.array(ii)/2.0
    return tt, vv, ii 


rootpath = "/Users/shanshangao/tmp/"
testruns =  read_wib_log(rootpath)
ts = "BNL_check_time"
#tbegin="2018-08-24 15:40:00"
tbegin="2018-08-24 15:58:00"
ip = "192.168.100.11"
tlast=510
con = "BNL_WIB1_FEMB0_AM36V"
tcv36_0 = read_cv_log(testruns, ts, con, tbegin, tlast, ip)
con = "BNL_WIB1_FEMB1_AM36V"
tcv36_1 = read_cv_log(testruns, ts, con, tbegin, tlast, ip)
con = "BNL_WIB1_FEMB2_AM36V"
tcv36_2 = read_cv_log(testruns, ts, con, tbegin, tlast, ip)
con = "BNL_WIB1_FEMB3_AM36V"
tcv36_3 = read_cv_log(testruns, ts, con, tbegin, tlast, ip)
ip = "192.168.100.12"
con = "BNL_WIB1_FEMB0_AM36V"
tcv36_4 = read_cv_log(testruns, ts, con, tbegin, tlast, ip)

plt.figure(figsize=(16,3))
label = "WIB0FEMB0_2.5V"
tbs = long( time.mktime(datetime.datetime.strptime(tbegin, "%Y-%m-%d %H:%M:%S").timetuple()) )
xp = (np.array(tcv36_0[0]) - tbs)/60.0
plt.plot(xp, tcv36_0[2])
plt.scatter(xp, tcv36_0[2], label=label)


plt.text(0, -0.2 , "$\leftarrow$%s"%tbegin, fontsize=16) 

label = "WIB0FEMB1_2.5V"
xp = (np.array(tcv36_1[0]) - tbs)/60.0
plt.plot(xp, tcv36_1[2])
plt.scatter(xp, tcv36_1[2], label=label)

label = "WIB0FEMB2_2.5V"
xp = (np.array(tcv36_2[0]) - tbs)/60.0
plt.plot(xp, tcv36_2[2])
plt.scatter(xp, tcv36_2[2], label=label)

label = "WIB0FEMB3_2.5V"
xp = (np.array(tcv36_3[0]) - tbs)/60.0
plt.plot(xp, tcv36_3[2])
plt.scatter(xp, tcv36_3[2], label=label)

label = "WIB1FEMB0_2.5V"
xp = (np.array(tcv36_4[0]) - tbs)/60.0
plt.plot(xp, tcv36_4[2])
plt.scatter(xp, tcv36_4[2], label=label)

plt.legend(loc="best", fontsize=16 )
plt.tick_params(labelsize=20)
plt.xlim([0, tlast/60])
plt.ylim([-0.5,2])
ylabel = "Current / A "
plt.ylabel(ylabel, fontsize=20 )
xlabel = "Time / minute "
plt.xlabel(xlabel, fontsize=20 )
title = "Currents of 2.5V"
plt.title(title , fontsize=20 )
plt.grid()

plt.show()
plt.close()


