# -*- coding: utf-8 -*-
"""
File Name: read_rtds.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: Thu Jan 18 14:35:04 2018
Last modified: Sun 01 Apr 2018 03:05:15 PM CEST
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl


import numpy as np
import struct
import os
from sys import exit
import sys
import os.path
import time
import datetime


def readrtds() :# , runtime):
    filepath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/APA4_cooldown_Raw.csv"
    filepath2 =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/APA4_cooldown_RTDdata.csv"

    if os.path.isfile(filepath2):
        print filepath2
        os.remove(filepath2)
    if os.path.isfile(filepath):
        with open(filepath,"r") as f:
            temps_data = []
            onetemps = []
            i = 0
            for line in f:
                if line[0:4] == "2018" :
                    unit_np = line.split(",")
                    ts = unit_np[0][0:16]
                    tstamp = time.mktime(datetime.datetime.strptime(ts, "%Y/%m/%d %H:%M").timetuple())
                    tt0200 = int(float( unit_np[1] ))
                    tt0201 = int(float( unit_np[2] ))
                    tt0202 = int(float( unit_np[3] ))
                    tt0203 = int(float( unit_np[4] ))
                    tt0204 = int(float( unit_np[5] ))
                    tt0205 = int(float( unit_np[6] ))
                    tt0206 = int(float( unit_np[7] ))
                    onetemps = [tstamp, tt0200, tt0201, tt0202, tt0203, tt0204, tt0205, tt0206,ts[0:16]]
                    if ( temps_data == [] ):
                        temps_data.append(onetemps)
                    else:
                        if (temps_data[-1][0] == onetemps[0] ) or ( onetemps[1] > 350 ):
                            pass
                        else:
                            temps_data.append(onetemps)
                            with open(filepath2,"a+") as f2:
                                f2.write(line)

    else:
        print "RTDs data doesn't exist!!! Ingore anyway"
        temps_data = None
    return temps_data

readrtds() 
