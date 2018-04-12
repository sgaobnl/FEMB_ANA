# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Oct 29 22:17:34 2017
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
#from openpyxl import Workbook
#import numpy as np
#import struct
import os
#from matplotlib.colors import LogNorm
#import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
import zipfile
from shutil import copyfile
from shutil import move
from shutil import rmtree

path = "/Users/shanshangao/Documents/Share_Windows/Hibay_V2/Rawdata/pd_simu_2/run01/WIB3LNstep30/"

for root, dirs, files in os.walk(path):
    break

for onefile in files:
    if onefile[0:4] == "WIB1" :
        path3 = path
        print path3 +  onefile
        os.rename(path3 + onefile, path3 + onefile[0:3] + "3" + onefile[4:] )
        #os.rename(path3 + onefile, path3 + onefile[0:11] + "0" + onefile[12:] )

#for onedir in dirs:
#    if onedir[0:4] == "WIB2" :
#        for root3, dirs3, files3 in os.walk(path+onedir+"/"):
#            break
#        for onefile in files3:
#            if onefile[0:4] == "WIB2" :
#                path3 = path+onedir+"/"
#                print path3 +  onefile
#                os.rename(path3 + onefile, path3 + onefile[0:3] + "3" + onefile[4:] )

#for onedir in dirs:
#    for root2, dirs2, files2 in os.walk(path+onedir+"/"):
#        break
#    for onedir2 in dirs2:
#        if onedir2 == "WIB1RTstep32" :
#            for root3, dirs3, files3 in os.walk(path+onedir+"/"+onedir2+"/"):
#                break
#            for onefile in files3:
#                if onefile[0] == "\\" :
#                    path3 = path+onedir+"/"+onedir2+"/"
#                    print path3 +  onefile
#                    os.rename(path3 + onefile, path3 + onefile[1:] )




