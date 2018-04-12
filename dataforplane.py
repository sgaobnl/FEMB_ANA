# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sat Nov 18 18:55:00 2017
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
#import struct
from apa_mapping import apa_mapping

def dataforplane (alldata, apa="ProtoDUNE", femb = 0, tp = 1 ):
    apa_yuv, apa_y, apa_v, apa_u = apa_mapping(apa=apa)
    yuv_chndata = []
    for yuv_chn in apa_yuv:
        for onedata in alldata:
            if (onedata[0] == femb ):#femb
                if ( onedata[1] == (yuv_chn//16) ):#chip
                    if (onedata[2] == tp ): #tp
                        yuv_chndata.append(onedata[3][yuv_chn%16])

    y_chndata = []
    for y_chn in apa_y:
        for onedata in alldata:
            if (onedata[0] == femb ):#femb
                if ( onedata[1] == (y_chn//16) ):#chip
                    if (onedata[2] == tp ): #tp
                        y_chndata.append(onedata[3][y_chn%16])
    u_chndata = []
    for u_chn in apa_u:
        for onedata in alldata:
            if (onedata[0] == femb ):#femb
                if ( onedata[1] == (u_chn//16) ):#chip
                    if (onedata[2] == tp ): #tp
                        u_chndata.append(onedata[3][u_chn%16])
    v_chndata = []
    for v_chn in apa_v:
        for onedata in alldata:
            if (onedata[0] == femb ):#femb
                if ( onedata[1] == (v_chn//16) ):#chip
                    if (onedata[2] == tp ): #tp
                        v_chndata.append(onedata[3][v_chn%16])
    return yuv_chndata, y_chndata, v_chndata, u_chndata

