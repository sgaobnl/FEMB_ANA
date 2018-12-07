# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 12/4/2018 2:39:51 PM
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
import struct
import os
from sys import exit
from path import path

p = "D:/SBND_40APA/Share_data/Rawdata_11_20_2018/run01fpg/"
#sp = ["WIB00step02", "WIB00step12", "WIB00step22", "WIB00step32"] 
sp = [ "WIB00step12"] 

for ip in sp:
    pp = path(p + ip + "/")
    for f in ["*FPGADAC1A*","*FPGADAC1B*","*FPGADAC1C*","*FPGADAC1D*","*FPGADAC1E*","*FPGADAC1F*"] :
        files = pp.walkfiles(f)
        for fi in files:
            #print fi
            fi.remove()
