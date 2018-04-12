# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Mon 19 Mar 2018 11:31:08 PM CET
"""
#import matplotlib
#matplotlib.use('Agg')
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

def readlog(rootpath, APAno, runtime, runno, runtype):
    print rootpath
    #filepath = rootpath + "ProtoDUNEreadme.log"
    filepath = rootpath + "Coldboxreadme.log"

    if os.path.isfile(filepath):
        with open(filepath,"r") as f:
            testruns = []
            onerun = []
            for line in f:
                if (line.find("Begin") >=0 ):
                    if (len(onerun) > 0 ):
                        if (onerun[0].find("Begin") >=0) and (onerun[-1].find("End") < 0):
                            testruns.append(onerun)
                    onerun = []
                    onerun.append(line)
                elif (line.find("End") >=0 ):
                    testruns.append(onerun)
                    onerun = []
                else:
                    onerun.append(line)
            if (onerun[0].find("Begin") >=0) and (onerun[-1].find("End") < 0) :
                testruns.append(onerun)
    else:
        print "%s, file doesn't exist!!!"%file_setadc_rec
        sys.exit()

    return log_parser(testruns, APAno, runtime, runno, runtype)

def log_parser(testruns, APAno, runtime="01_15_2018", runno="01", runtype="chk"):
    for onerun in testruns:
        for oneline in onerun:
            con_a = (oneline.find(runtime) >= 0)
            con_b = (oneline.find("run"+runno+runtype) >= 0)
            if con_a and con_b :
                break
        if con_a and con_b :
            run_reqed = onerun
            break
    if con_a and con_b :
        apainfo = run_reqed[2][0:-1]
        env = run_reqed[3][0:-1]
        run_title =  run_reqed[5][0:-1]
        rtd_info =  run_reqed[6][0:-1]

        for lineno in range(len(run_reqed)):
            if (run_reqed[lineno].find(runtime) > 0) and (run_reqed[lineno].find("run"+runno+runtype) > 0):
                runtype =  run_reqed[lineno-1][0:-1]
                rundir =  run_reqed[lineno][0:-1]
                runtime = run_reqed[lineno+1][0:-1]

                str_alivefembs = run_reqed[lineno-2][0:-1] 
                tmp1 = str_alivefembs.find("[[")
                tmp2 = str_alivefembs.find("]]")
                tmp = str_alivefembs[tmp1+1: (tmp2+1)]
                tmp2 = []
                for i in tmp:
                    if (i == '['):
                        tmp3 = []
                    elif (i == ']'): 
                        tmp2.append(tmp3)
                        tmp3 = []
                    if i in "0123":
                        tmp3.append(int(i))

                badfembs= ""
                for wibno in range(len(tmp2)):
                    for femb in range(4):
                        if femb in tmp2[wibno]:
                            pass
                        else:
                            badfembs = badfembs + ("WIB%d"%(wibno+1) + "FEMB%d"%femb + ", ")

                print "Inactive FEMBs: "
                print badfembs
                break
        return apainfo + " APA#" + str(APAno), env, run_title, rtd_info, runtype, rundir, runtime, badfembs
    else:
        print "Test doesn't exist, exit anyway"
        sys.exit()


