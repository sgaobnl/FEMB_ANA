# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Oct 29 01:17:15 2017
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl


def bad_channels_mapping(wib_ip=1, femb_no=0,env="RT"):

    apa_yuv_bad = [ ] 

    return apa_yuv_bad
#bad channel for 40% APA 
## top
#    if (env == "RT" ):
#        if (wib_ip == 1):
#            if (femb_no== 0) :
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98 ] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98, 48, 14, 39, 44, 30] 
#            elif ( femb_no == 2):
#                apa_yuv_bad = [124,126,127] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [48, 50 ] 

## top
#        elif (wib_ip == 5):
#            if (femb_no== 0) :
#                apa_yuv_bad = [48 ] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 2):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [ ] 
#    else:
#        if (wib_ip == 1):
#            if (femb_no== 0) :
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98 ] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98, 48, 30] 
#            elif ( femb_no == 2):
#                apa_yuv_bad = [124,126, 127] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [48, 50 ] 
#        elif (wib_ip == 5):
#            if (femb_no== 0) :
#                apa_yuv_bad = [48 ] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 2):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [ ] 

#run15
#    if (env == "RT" ):
#        if (wib_ip == 1):
#            if (femb_no== 2) :
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98 ] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98, 48, 14, 39, 44, 30] 
#            elif ( femb_no == 0):
#                apa_yuv_bad = [124,126,127] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [48, 50 ] 
#        elif (wib_ip == 2):
#            if (femb_no== 2) :
#                apa_yuv_bad = [48 ] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 0):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [ ] 
#    else:
#        if (wib_ip == 1):
#            if (femb_no== 2) :
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98 ] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [15, 31, 46, 65, 81, 98, 48, 30] 
#            elif ( femb_no == 0):
#                apa_yuv_bad = [124,126, 127] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [48, 50 ] 
#        elif (wib_ip == 2):
#            if (femb_no== 2) :
#                apa_yuv_bad = [48 ] 
#            elif ( femb_no == 3):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 0):
#                apa_yuv_bad = [ ] 
#            elif ( femb_no == 1):
#                apa_yuv_bad = [ ] 

#    apa_yuv_bad = []
#    if (femb== 0):
#        apa_yuv_bad = []
#    else:
#        apa_yuv_bad = []
#     if femb_no == -1 :
#        if (env == "RT") and ( adcclk=="int"):
#            apa_yuv_bad = [37,40,101,103, 109,110]
#        elif (env == "RT") and ( adcclk=="ext"):
#            apa_yuv_bad = range(32,48,1) + [101,103, 109,110]
#        elif (env == "LN2") and ( adcclk=="int"):
#            apa_yuv_bad = [13,48,101,103,104, 109,110,112, 122, 127,   ]
#        elif (env == "LN2") and ( adcclk=="ext"):
#            apa_yuv_bad = [13,] + range(32,48,1) + [73, 82, 93, 101,118, 122]
#     else:
#        #40% APA
#        if (env == "RT" ):
#            if (femb_no== 0) :
#                #apa_yuv_bad = [48,61,76] #P1 FE & V* ADC
#                #apa_yuv_bad = [13,23,46, 49,54,74,80,97, 105, 47, 73, 75] #P2 FE & P1 ADC --> 150pF
#                apa_yuv_bad = [] #P2 FE & P1 ADC --> 150pF
#            elif ( femb_no == 1):
#                #apa_yuv_bad = [43, 48, 90, 91, 92,95, 112, 113, 114, 115, 116, 117, 118,123,124,125,126]#P1 FE & V* ADC
#                #apa_yuv_bad = [32, 34, 36, 48, 101, 103, 104  ] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = [32, 34, 36, 120, 37, 39, 40, 48, 101, 103, 109, 110 ] #P2 FE & P1 ADC --> 150pF
#                apa_yuv_bad = [] #P2 FE & P1 ADC --> 150pF
#            elif ( femb_no == 2):
#                #apa_yuv_bad = [40, 96, 124, 126, 127]#P1 FE & V* ADC
#                #apa_yuv_bad = [ 124, 126   ]#P1 FE & V* ADC
#                apa_yuv_bad = [] #P2 FE & P1 ADC --> 150pF
#            elif ( femb_no == 3):
#                apa_yuv_bad = [48,3,5,13,16,30,34,36,38,39,45,47,61, 74,76,79,81,93,102,112 ] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = [84,] #P1 FE & V* ADC
#                #apa_yuv_bad = [48,49,95,96,97 ]#COTS ADC
#                apa_yuv_bad = [] #P2 FE & P1 ADC --> 150pF
#        else:
#            if (femb_no== 0) :
#                #apa_yuv_bad = [48,61,76] #P1 FE & V* ADC
#                #apa_yuv_bad = [13,23,46, 49,54,74,80,97, 105, 47, 73, 75] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = [23, 73, 74, 75, 92, 97, 105, 110, 111, 126, 127, 46] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = range(0,16,1) + [23, 73, 74, 75, 92, 97, 105, 110, 111, 126, 127, 46] #P2 FE & P1 ADC --> 150pF
#                apa_yuv_bad = [23, 74, 97, 105] #P2 FE & P1 ADC --> 150pF
#            elif ( femb_no == 1):
#                #apa_yuv_bad = [43, 48, 90, 91, 92,95, 112, 113, 114, 115, 116, 117, 118,123,124,125,126]#P1 FE & V* ADC
#                #apa_yuv_bad = [48, 101, 103 ] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = [32, 34, 36, 120 ] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = [32, 34, 36, 120, 37, 39, 40, 48, 101, 103, 109, 110 ] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = range(1,64,1) + [ 120, 101, 103, 109, 110 ] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = [32,34, 48, 93, 101, 103, 96, 123  ] #P2 FE & P1 ADC --> 150pF
#                apa_yuv_bad = [32,34, 36, 120  ] #P2 FE & P1 ADC --> 150pF
##24, 25, 56, 57, 88, 89, 120,121, 
#            elif ( femb_no == 2):
#                #apa_yuv_bad = [40, 96, 124, 126, 127]#P1 FE & V* ADC
#                #apa_yuv_bad = [ 124, 126   ]#P1 FE & V* ADC
#                #apa_yuv_bad = range(16,32,1) + range(16*4,16*8,1) #P2 FE & P1 ADC --> 150pF
#                apa_yuv_bad = [16, 21, 22, 24] + range(16*4,16*8,1) #P2 FE & P1 ADC --> 150pF
#            elif ( femb_no == 3):
#                #apa_yuv_bad = [84,] #P1 FE & V* ADC
#                #apa_yuv_bad = [ 48,3,5,13,16,30,34,36,38,39,45,47,61, 74,76,79,81,93,102,112 ] #P2 FE & P1 ADC --> 150pF
#                #apa_yuv_bad = [48,49,95,96,97 ]#COTS ADC
#                apa_yuv_bad = [27, 48, 50] + range(64, 91, 1) + [122, 123]   #P2 FE & P1 ADC --> 150pF

