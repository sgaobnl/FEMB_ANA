# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 1/19/2019 7:48:13 PM
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
import numpy as np

class APA_CAPMAP:
    def femb_cap ( self, fembid=4 ):
        ofc = self.femb_caps[fembid]
        j1_1 = ofc[0::4][::-1]
        j1_3 = ofc[1::4][16:32] + ofc[1::4][0:16]
        j2_1 = ofc[2::4][0:16][::-1] + ofc[2::4][16:32][::-1]
        j2_3 = ofc[3::4]
        chn_caps = j1_1 + j1_3 + j2_1 + j2_3
        return chn_caps

    def __init__(self):
        self.B4_cap = [
        58,10,48,71,
        48,65,48,66,
        48,12,48,72,
        48,66,48,66,
        48,16,48,72,
        48,66,48,68,
        48,16,48,72,
        48,66,48,70,
        48,16,48,72,
        48,66,48,70,
        48,16,48,72,
        48,66,48,70,
        48,16,48,71,
        48,66,48,70,
        66,72,68,72,
        66,72,68,72,
        66,72,68,72,
        68,72,68,72,
        48,72,48,72,
        48,32,48,70,
        48,72,48,72,
        48,66,48,70,
        48,72,48,72,
        48,66,48,72,
        48,72,48,73,
        48,66,48,72,
        48,72,48,72,
        48,66,49,70,
        48,73,49,72,
        48,66,49,70,
        49,73,49,72,
        48,67,49,70,
        ]
        
        self.B3_cap = [
        48,71,48,72,
        48,69,48,71,
        48,72,48,72,
        48,70,48,70,
        48,70,48,72,
        48,70,48,70,
        48,71,48,72,
        48,70,48,70,
        48,72,47,72,
        48,70,48,70,
        48,72,48,72,
        48,71,48,70,
        48,72,48,72,
        49,70,48,70,
        70,72,69,72,
        70,72,69,72,
        70,72,69,72,
        70,72,69,73,
        48,72,48,73,
        48,70,48,70,
        48,72,48,73,
        48,70,48,70,
        48,72,49,73,
        49,70,49,70,
        49,72,49,73,
        50,70,49,70,
        50,72,49,73,
        50,72,50,70,
        50,73,50,73,
        50,72,49,72,
        50,73,49,73,
        50,72,49,72,
        ]
        
        self.B2_cap = [
        48,73,48,72,
        50,72,50,72,
        48,74,49,73,
        48,72,49,72,
        49,73,49,73,
        48,72,49,72,
        48,73,49,72,
        14,70,49,72,
        48,73,49,73,
        14,70,49,72,
        48,73,48,72,
        49,70,49,71,
        49,73,48,72,
        49,70,49,70,
        70,73,12,72,
        70,73,70,72,
        72,73,70,73,
        72,74,70,73,
        48,74,48,73,
        48,72,48,71,
        48,74,48,73,
        49,72,48,70,
        49,74,48,72,
        49,71,48,70,
        49,74,48,70,
        49,71,48,70,
        49,74,48,69,
        49,70,49,70,
        49,74,49,69,
        49,70,49,70,
        50,74,49,69,
        50,71,49,69,
        ]
        
        self.B1_cap = [
        48,69,48,68,
        50,71,48,18,
        50,70,49,68,
        50,71,49,18,
        50,70,48,68,
        50,21,48,18,
        50,70,48,68,
        50,21,48,18,
        49,70,48,68,
        49,20,48,18,
        49,70,49,68,
        49,20,50,18,
        49,69,50,68,
        50,20,50,18,
        20,69,17,69,
        20,69,17,69,
        20,32,17,69,
        20,52,17,69,
        48,69,49,70,
        49,20,49,18,
        49,70,49,69,
        49,20,49,17,
        49,70,49,70,
        50,20,49,17,
        50,70,49,70,
        50,19,49,16,
        50,70,49,70,
        50,20,49,16,
        50,71,49,69,
        50,20,48,16,
        50,71,48,69,
        50,20,56,14,
        ]
        
        self.A4_cap = [
        50,11,48,72,
        47,11,49,14,
        47,12,49,73,
        48,12,49,68,
        48,72,49,72,
        48,13,49,70,
        48,72,49,72,
        48,13,49,71,
        48,72,49,72,
        49,13,49,71,
        49,72,49,72,
        49,13,50,71,
        49,72,50,72,
        49,13,50,70,
        13,72,70,73,
        13,72,70,73,
        13,72,70,73,
        13,72,70,73,
        49,72,49,73,
        50,13,49,71,
        50,72,50,73,
        50,14,50,72,
        50,73,50,73,
        50,14,50,72,
        50,73,50,73,
        50,14,50,72,
        50,73,50,74,
        50,14,51,70,
        50,74,51,73,
        50,14,51,70,
        50,74,51,72,
        50,14,51,70,
        ]
        
        self.A3_cap = [
        49,71,12,70, 
        49,70,12,69, 
        50,72,12,71, 
        50,70,12,68, 
        50,72,12,71, 
        51,70,12,68, 
        50,70,12,71, 
        49,70,12,68, 
        49,71,12,71, 
        49,70,12,12, 
        48,72,12,71, 
        48,70,12,68, 
        48,72,12,70, 
        48,70,12,68, 
        70,72,68,71, 
        70,72,68,71, 
        70,72,68,71, 
        69,72,68,71, 
        48,72,12,71, 
        47,69,12,68, 
        47,69,12,71, 
        47,69,12,68, 
        47,71,12,68, 
        47,69,12,68, 
        47,72,12,72, 
        47,70,12,68, 
        47,72,12,71, 
        47,71,12,68, 
        47,72,12,180,
        48,72,12,12, 
        48,72,12,180,
        48,70,12,12, 
        ]
        
        self.A2_cap = [
        12,180,48,72,
        13,71,49,70, 
        13,73,49,72, 
        13,71,49,71, 
        13,72,48,72, 
        13,71,48,72, 
        13,72,48,72, 
        14,70,48,72, 
        48,72,48,72, 
        48,70,48,71, 
        48,72,48,72, 
        48,70,48,70, 
        48,72,48,72, 
        49,70,48,70, 
        70,72,69,72, 
        70,72,69,72, 
        71,73,70,72, 
        72,74,70,72, 
        48,74,48,72, 
        49,72,48,70, 
        49,74,48,72, 
        49,72,48,70, 
        49,73,48,70, 
        49,71,48,69, 
        49,73,48,68, 
        50,71,48,70, 
        50,74,48,68, 
        50,70,49,70, 
        50,74,49,70, 
        50,71,49,70, 
        50,73,49,70, 
        50,71,48,70, 
        ]
        
        self.A1_cap = [
        48,68,48,11,
        48,69,48,69,
        48,69,48,12,
        48,70,48,69,
        48,68,47,12,
        48,70,48,68,
        48,68,47,12,
        48,70,47,68,
        48,68,47,12,
        48,71,47,68,
        48,68,47,12,
        48,71,48,68,
        48,68,48,12,
        49,71,48,68,
        70,68,69,12,
        69,68,69,12,
        70,68,69,12,
        70,68,68,12,
        48,68,68,12,
        48,70,68,68,
        48,68,68,12,
        48,70,68,68,
        48,68,48,12,
        48,70,48,68,
        48,13,48,12,
        48,70,48,68,
        48,13,48,12,
        48,70,48,68,
        48,13,48,12,
        48,70,48,68,
        48,13,48,12,
        49,70,60,34,
        ]
       
        self.femb_caps = [self.A1_cap, self.A2_cap, self.A3_cap, self.A4_cap, self.B1_cap, self.B2_cap, self.B3_cap, self.B4_cap, ]

#capmap = APA_CAPMAP()
#a = capmap.femb_cap(fembid=4)
#print a
