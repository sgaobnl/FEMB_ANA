# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sat Jun  9 10:53:08 2018
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl

import openpyxl as px
import numpy as np
import statsmodels.api as sm
import sys


class APA_MAP:
    def mapping_rd (self  ):
        vW = px.load_workbook(self.path)
        vp = vW.get_sheet_by_name(name = 'Mapping')
        va=[]
        vi = 0
        for row in vp.iter_rows():
            if vi >= 2:
                vb = []
                for k in row:
                    vb.append(str(k.internal_value))
                va.append(vb)
            vi = vi + 1
        return va

    def apa_femb_mapping(self):
        if (self.APA == "ProtoDUNE"):
            apa_femb_loc = [ 
                            #wire   #FEMBchn  #FEMBasic # ASICchn
                            ["X01", "031", 2, "15"], ["X03", "030", 2, "14"], ["X05", "029", 2, "13"], ["X07", "028", 2, "12"],
                            ["X09", "027", 2, "11"], ["X11", "026", 2, "10"], ["V01", "025", 2, "09"], ["V03", "024", 2, "08"],
                            ["V05", "023", 2, "07"], ["V07", "022", 2, "06"], ["V09", "021", 2, "05"], ["U01", "020", 2, "04"],
                            ["U03", "019", 2, "03"], ["U05", "018", 2, "02"], ["U07", "017", 2, "01"], ["U09", "016", 2, "00"],

                            ["X13", "015", 1, "15"], ["X15", "014", 1, "14"], ["X17", "013", 1, "13"], ["X19", "012", 1, "12"],
                            ["X21", "011", 1, "11"], ["X23", "010", 1, "10"], ["V11", "009", 1, "09"], ["V13", "008", 1, "08"],
                            ["V15", "007", 1, "07"], ["V17", "006", 1, "06"], ["V19", "005", 1, "05"], ["U11", "004", 1, "04"],
                            ["U13", "003", 1, "03"], ["U15", "002", 1, "02"], ["U17", "001", 1, "01"], ["U19", "000", 1, "00"],
    
                            ["X02", "048", 4, "00"], ["X04", "049", 4, "01"], ["X06", "050", 4, "02"], ["X08", "051", 4, "03"],
                            ["X10", "052", 4, "04"], ["X12", "053", 4, "05"], ["V02", "054", 4, "06"], ["V04", "055", 4, "07"],
                            ["V06", "056", 4, "08"], ["V08", "057", 4, "09"], ["V10", "058", 4, "10"], ["U02", "059", 4, "11"],
                            ["U04", "060", 4, "12"], ["U06", "061", 4, "13"], ["U08", "062", 4, "14"], ["U10", "063", 4, "15"],

                            ["X14", "032", 3, "00"], ["X16", "033", 3, "01"], ["X18", "034", 3, "02"], ["X20", "035", 3, "03"],
                            ["X22", "036", 3, "04"], ["X24", "037", 3, "05"], ["V12", "038", 3, "06"], ["V14", "039", 3, "07"],
                            ["V16", "040", 3, "08"], ["V18", "041", 3, "09"], ["V20", "042", 3, "10"], ["U12", "043", 3, "11"],
                            ["U14", "044", 3, "12"], ["U16", "045", 3, "13"], ["U18", "046", 3, "14"], ["U20", "047", 3, "15"],
                            
                            ["X26", "096", 7, "00"], ["X28", "097", 7, "01"], ["X30", "098", 7, "02"], ["X32", "099", 7, "03"], 
                            ["X34", "100", 7, "04"], ["X36", "101", 7, "05"], ["V22", "102", 7, "06"], ["V24", "103", 7, "07"], 
                            ["V26", "104", 7, "08"], ["V28", "105", 7, "09"], ["V30", "106", 7, "10"], ["U22", "107", 7, "11"], 
                            ["U24", "108", 7, "12"], ["U26", "109", 7, "13"], ["U28", "110", 7, "14"], ["U30", "111", 7, "15"], 

                            ["X38", "112", 8, "00"], ["X40", "113", 8, "01"], ["X42", "114", 8, "02"], ["X44", "115", 8, "03"], 
                            ["X46", "116", 8, "04"], ["X48", "117", 8, "05"], ["V32", "118", 8, "06"], ["V34", "119", 8, "07"], 
                            ["V36", "120", 8, "08"], ["V38", "121", 8, "09"], ["V40", "122", 8, "10"], ["U32", "123", 8, "11"], 
                            ["U34", "124", 8, "12"], ["U36", "125", 8, "13"], ["U38", "126", 8, "14"], ["U40", "127", 8, "15"], 
                            
                            ["X25", "079", 5, "15"], ["X27", "078", 5, "14"], ["X29", "077", 5, "13"], ["X31", "076", 5, "12"],
                            ["X33", "075", 5, "11"], ["X35", "074", 5, "10"], ["V21", "073", 5, "09"], ["V23", "072", 5, "08"],
                            ["V25", "071", 5, "07"], ["V27", "070", 5, "06"], ["V29", "069", 5, "05"], ["U21", "068", 5, "04"],
                            ["U23", "067", 5, "03"], ["U25", "066", 5, "02"], ["U27", "065", 5, "01"], ["U29", "064", 5, "00"],

                            ["X37", "095", 6, "15"], ["X39", "094", 6, "14"], ["X41", "093", 6, "13"], ["X43", "092", 6, "12"],
                            ["X45", "091", 6, "11"], ["X47", "090", 6, "10"], ["V31", "089", 6, "09"], ["V33", "088", 6, "08"],
                            ["V35", "087", 6, "07"], ["V37", "086", 6, "06"], ["V39", "085", 6, "05"], ["U31", "084", 6, "04"],
                            ["U33", "083", 6, "03"], ["U35", "082", 6, "02"], ["U37", "081", 6, "01"], ["U39", "080", 6, "00"]
                        ]
        elif (self.APA == "LArIAT" ):
            va = self.mapping_rd ( )
            va_femb = []
            for vb in va:
                if int(vb[9]) == self.femb :
                    va_femb.append(vb)
            apa_femb_loc = []
            for chn in range(128):
                for vb in va_femb:
                    if int(vb[8]) == chn:
                        if (vb[1].find("Co")) >= 0 : #collection wire
                            chninfo = [ "X" + vb[0], vb[8], int(vb[6]), int(vb[7]), int(vb[9]), int(vb[10])]
                        elif (vb[1].find("In")) >= 0 : #induction wire
                            chninfo = [ "U" + vb[0], vb[8], int(vb[6]), int(vb[7]), int(vb[9]), int(vb[10])]
                        apa_femb_loc.append(chninfo)
            for chn in range(128):
                fl_w = True
                fl_i = 0
                for tmp in apa_femb_loc:
                    if int(tmp[1]) == chn:
                        fl_w = False
                        break
                if (fl_w):
                    chninfo = [ "V" + format(fl_i, "03d"), format(chn, "03d"), chn//16 , format(chn%15, "02d"), apa_femb_loc[0][4], apa_femb_loc[0][5]]
                    apa_femb_loc.append(chninfo)
                    fl_i = fl_i + 1

        elif (self.APA == "APA40" ):
            apa_femb_loc = [ 
                            ["X28", "031", 2, "15"], ["X27", "030", 2, "14"], ["X26", "029", 2, "13"], ["X25", "028", 2, "12"],
                            ["X24", "027", 2, "11"], ["X23", "026", 2, "10"], ["X22", "025", 2, "09"], ["X21", "024", 2, "08"],
                            ["X20", "023", 2, "07"], ["X19", "022", 2, "06"], ["X18", "021", 2, "05"], ["X17", "020", 2, "04"],
                            ["X16", "019", 2, "03"], ["X15", "018", 2, "02"], ["U04", "017", 2, "01"], ["U03", "016", 2, "00"],
                            ["U02", "015", 1, "15"], ["U01", "014", 1, "14"], ["X14", "013", 1, "13"], ["X13", "012", 1, "12"],
                            ["X12", "011", 1, "11"], ["X11", "010", 1, "10"], ["X10", "009", 1, "09"], ["X09", "008", 1, "08"],
                            ["X08", "007", 1, "07"], ["X07", "006", 1, "06"], ["X06", "005", 1, "05"], ["X05", "004", 1, "04"],
                            ["X04", "003", 1, "03"], ["X03", "002", 1, "02"], ["X02", "001", 1, "01"], ["X01", "000", 1, "00"],

                            ["V10", "048", 4, "00"], ["U12", "049", 4, "01"], ["V11", "050", 4, "02"], ["U13", "051", 4, "03"],
                            ["V12", "052", 4, "04"], ["U14", "053", 4, "05"], ["V13", "054", 4, "06"], ["U15", "055", 4, "07"],
                            ["V14", "056", 4, "08"], ["U16", "057", 4, "09"], ["V15", "058", 4, "10"], ["U17", "059", 4, "11"],
                            ["V16", "060", 4, "12"], ["U18", "061", 4, "13"], ["V17", "062", 4, "14"], ["V18", "063", 4, "15"],
                            ["V01", "032", 3, "00"], ["V02", "033", 3, "01"], ["V03", "034", 3, "02"], ["U05", "035", 3, "03"],
                            ["V04", "036", 3, "04"], ["U06", "037", 3, "05"], ["V05", "038", 3, "06"], ["U07", "039", 3, "07"],
                            ["V06", "040", 3, "08"], ["U08", "041", 3, "09"], ["V07", "042", 3, "10"], ["U09", "043", 3, "11"],
                            ["V08", "044", 3, "12"], ["U10", "045", 3, "13"], ["V09", "046", 3, "14"], ["U11", "047", 3, "15"],

                            ["X42", "079", 5, "15"], ["X41", "078", 5, "14"], ["X40", "077", 5, "13"], ["X39", "076", 5, "12"],
                            ["X38", "075", 5, "11"], ["X37", "074", 5, "10"], ["X36", "073", 5, "09"], ["X35", "072", 5, "08"],
                            ["X34", "071", 5, "07"], ["X33", "070", 5, "06"], ["X32", "069", 5, "05"], ["X31", "068", 5, "04"],
                            ["X30", "067", 5, "03"], ["X29", "066", 5, "02"], ["U20", "065", 5, "01"], ["U19", "064", 5, "00"],
                            ["U22", "095", 6, "15"], ["U21", "094", 6, "14"], ["X56", "093", 6, "13"], ["X55", "092", 6, "12"],
                            ["X54", "091", 6, "11"], ["X53", "090", 6, "10"], ["X52", "089", 6, "09"], ["X51", "088", 6, "08"],
                            ["X50", "087", 6, "07"], ["X49", "086", 6, "06"], ["X48", "085", 6, "05"], ["X47", "084", 6, "04"],
                            ["X46", "083", 6, "03"], ["X45", "082", 6, "02"], ["X44", "081", 6, "01"], ["X43", "080", 6, "00"],

                            ["V19", "096", 7, "00"], ["U23", "097", 7, "01"], ["V20", "098", 7, "02"], ["U24", "099", 7, "03"], 
                            ["V21", "100", 7, "04"], ["U25", "101", 7, "05"], ["V22", "102", 7, "06"], ["U26", "103", 7, "07"], 
                            ["V23", "104", 7, "08"], ["U27", "105", 7, "09"], ["V24", "106", 7, "10"], ["U28", "107", 7, "11"], 
                            ["V25", "108", 7, "12"], ["U29", "109", 7, "13"], ["V26", "110", 7, "14"], ["V27", "111", 7, "15"], 
                            ["V28", "112", 8, "00"], ["V29", "113", 8, "01"], ["V30", "114", 8, "02"], ["U30", "115", 8, "03"], 
                            ["V31", "116", 8, "04"], ["U31", "117", 8, "05"], ["V32", "118", 8, "06"], ["U32", "119", 8, "07"], 
                            ["V33", "120", 8, "08"], ["U33", "121", 8, "09"], ["V34", "122", 8, "10"], ["U34", "123", 8, "11"], 
                            ["V35", "124", 8, "12"], ["U35", "125", 8, "13"], ["V36", "126", 8, "14"], ["U36", "127", 8, "15"] 
                        ]


        All_sort = []
        X_sort = []
        V_sort = []
        U_sort = []
        for i in range(128):
            for chn in apa_femb_loc:
                if int(chn[1][0:3]) == i :
                    All_sort.append(chn)
    
            for chn in apa_femb_loc:
                if chn[0][0] == "X" and int(chn[0][1:3]) == i :
                    X_sort.append(chn)
            for chn in apa_femb_loc:
                if chn[0][0] == "V" and int(chn[0][1:3]) == i :
                    V_sort.append(chn)
    
            for chn in apa_femb_loc:
                if chn[0][0] == "U" and int(chn[0][1:3]) == i :
                    U_sort.append(chn)

#        print "APA is " + self.APA + ",LArIAT FEMB no is %d"%self.femb 
        return All_sort, X_sort, V_sort, U_sort
    
    def apa_mapping(self):
        apa_yuv = []
        apa_y = []
        apa_u = []
        apa_v = []
        All_sort, X_sort, V_sort, U_sort = self.apa_femb_mapping()
        for onewire in All_sort:
            apa_yuv.append(int(onewire[1]))
    
        for onewire in X_sort:
            if onewire[0][0] == "X":
                apa_y.append(int(onewire[1]))
        for onewire in V_sort:
            if onewire[0][0] == "V":
                apa_v.append(int(onewire[1]))
        for onewire in U_sort:
            if onewire[0][0] == "U":
                apa_u.append(int(onewire[1]))
        return apa_yuv, apa_y, apa_u, apa_v

    def __init__(self):
        self.APA = 'LArIAT'
        self.femb = 4
        self.path = "./LArIAT_Pin_Mapping_06052018.xlsx"
 

#apa = APA_MAP()
#a = apa.apa_femb_mapping()
#print len(a[0]), len(a[1]), len(a[2]), len(a[3])
