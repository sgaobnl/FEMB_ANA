# -*- coding: utf-8 -*-
"""
File Name: read_rtds.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: Thu Jan 18 14:35:04 2018
Last modified: Thu 08 Feb 2018 03:15:30 AM CET
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


def readrtds(filepath) :# , runtime):
#    filepath = rootpath + "APA2_cooldown_RTDsdata.csv"
    print filepath
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
    else:
        print "RTDs data doesn't exist!!! Ingore anyway"
        temps_data = None
    return temps_data

def run_rtds(filepath, runtime) :
    temps = readrtds(filepath)
    if temps != None :
        runts = time.mktime(datetime.datetime.strptime(runtime[0:16], "%Y-%m-%d %H:%M").timetuple())
    #    print runts
        a = abs(temps[0][0] - runts)
        run_temp = temps[0]
        for i in temps:
            b = abs(i[0] - runts)
            if (b < a):
                a = b
                run_temp = i
    else:
        run_temp = None
    return run_temp
#    print run_temp


#run_rtds(rootpath = './', runtime = '2018-01-15 18:00') 
