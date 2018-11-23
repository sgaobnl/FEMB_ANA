# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Fri Nov 23 11:47:55 2018
"""
import matplotlib
matplotlib.use('Agg')
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
import pickle
from matplotlib.backends.backend_pdf import PdfPages

from apa_plot_out import load_sum
from apa_plot_out import plot0_overall_enc
from apa_plot_out import plot3_overall_gain
from apa_plot_out import plot2_peds
from apa_plot_out import plot1_chns_enc
from apa_plot_out import plot1_chns_enc_1
from apa_plot_out import plot4_chns_gain
from apa_plot_out import dict_filter
from apa_plot_out import dict_del_chn

APAno = int(sys.argv[1])
rmsdate = sys.argv[2]
fpgdate = sys.argv[3]
asidate = sys.argv[4]
rmsrunno = sys.argv[5]
fpgarunno = sys.argv[6]
asicrunno = sys.argv[7]
apafolder = sys.argv[8]

if (apafolder == "SBND"):
#    rms_rootpath =  "D:/Ledge_Study/Rawdata/Rawdata_" + rmsdate + "/"
#    fpga_rootpath = "D:/Ledge_Study/Rawdata/Rawdata_" + fpgdate + "/"
#    asic_rootpath = "D:/Ledge_Study/Rawdata/Rawdata_" + asidate + "/"
    rms_rootpath =  "D:/SBND_40APA/Rawdata/Rawdata_" + rmsdate + "/"
    fpga_rootpath = "D:/SBND_40APA/Rawdata/Rawdata_" + fpgdate + "/"
    asic_rootpath = "D:/SBND_40APA/Rawdata/Rawdata_" + asidate + "/"

elif (apafolder == "APA40"):
    rms_rootpath =  "D:/Rawdata/Rawdata_" + rmsdate + "/"
    fpga_rootpath = "D:/Rawdata/Rawdata_" + fpgdate + "/"
    asic_rootpath = "D:/Rawdata/Rawdata_" + asidate + "/"
elif (apafolder != "APA"):
    rms_rootpath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + rmsdate + "/"
    fpga_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + fpgdate + "/"
    asic_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + asidate + "/"
else:
    rms_rootpath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + rmsdate + "/"
    fpga_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + fpgdate + "/"
    asic_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + asidate + "/"
 
#fembs_on_apa = range(1,21, 1) 
#fembs_on_apa = range(2,3, 1) 
#fembs_on_apa = range(2,3,1) 
loc = int(sys.argv[9])
fembs_on_apa = [loc] 

sum_path = rms_rootpath + "/" + "results/" + "APA%d_"%APAno + rmsrunno + "_" + fpgarunno + "_" + asicrunno +"/"
fn = "APA%d"%APAno + "_" + rmsrunno + "_" + fpgarunno + "_" + asicrunno
orgdicts = load_sum (sum_path, fn + ".allsum")

femb_cs = []
for fembloc in fembs_on_apa:
    if (fembloc <= 10):
        femb_cs.append(["apaloc", "B" + format(APAno, "1d") + format(fembloc, "02d")])
    else:
        femb_cs.append(["apaloc", "A" + format(APAno, "1d") + format(fembloc, "02d")])
#
##if APAno == 3:
##    femb_cs.remove(["apaloc","A308"])  #APA3 B308 has broken FE ASIC
##if APAno == 4: #only at RT
##    femb_cs.remove(["apaloc","B409"])  #APA3 B308 has broken FE ASIC
##    femb_cs.remove(["apaloc","A420"])  #APA3 B308 has broken FE ASIC
#
if loc == 1:
    apa_femb_loc = [ 
                ["U28",  4, "15"], ["U29",  4, "14"], ["X54",  4, "13"], ["X53",  4, "12"],
                ["X52",  4, "11"], ["X51",  4, "10"], ["X50",  4, "09"], ["X49",  4, "08"],
                ["X48",  4, "07"], ["X47",  4, "06"], ["X46",  4, "05"], ["X45",  4, "04"],
                ["X44",  4, "03"], ["X43",  4, "02"], ["X55",  4, "01"], ["X56",  4, "00"],
                                                                                   
                ["X29",  3, "15"], ["X30",  3, "14"], ["X42",  3, "13"], ["X41",  3, "12"],
                ["X40",  3, "11"], ["X39",  3, "10"], ["X38",  3, "09"], ["X37",  3, "08"],
                ["X36",  3, "07"], ["X35",  3, "06"], ["X34",  3, "05"], ["X33",  3, "04"],
                ["X32",  3, "03"], ["X31",  3, "02"], ["U26",  3, "01"], ["U27",  3, "00"],

                ["V36",  2, "00"], ["V36",  2, "01"], ["U35",  2, "02"], ["V35",  2, "03"],
                ["U34",  2, "04"], ["V34",  2, "05"], ["U33",  2, "06"], ["V33",  2, "07"],
                ["U32",  2, "08"], ["V32",  2, "09"], ["U31",  2, "10"], ["V31",  2, "11"],
                ["U30",  2, "12"], ["V30",  2, "13"], ["U19",  2, "14"], ["V28",  2, "15"],
                                                                                   
                ["U18",  1, "00"], ["V26",  1, "01"], ["U25",  1, "02"], ["V25",  1, "03"],
                ["U24",  1, "04"], ["V24",  1, "05"], ["U23",  1, "06"], ["V23",  1, "07"],
                ["U22",  1, "08"], ["V22",  1, "09"], ["U21",  1, "10"], ["V21",  1, "11"],
                ["U20",  1, "12"], ["V20",  1, "13"], ["V19",  1, "14"], ["V27",  1, "15"],

                ["U08",  7, "15"], ["U10",  7, "14"], ["X26",  7, "13"], ["X25", 7 , "12"],
                ["X24",  7, "11"], ["X23",  7, "10"], ["X22",  7, "09"], ["X21", 7 , "08"],
                ["X20",  7, "07"], ["X19",  7, "06"], ["X18",  7, "05"], ["X17", 7 , "04"],
                ["X16",  7, "03"], ["X15",  7, "02"], ["X11",  7, "01"], ["X10", 7 , "00"],
                                                                                 
                ["X09",  8, "15"], ["X08",  8, "14"], ["X14",  8, "13"], ["X13", 8 , "12"],
                ["X12",  8, "11"], ["X11",  8, "10"], ["X10",  8, "09"], ["X09", 8 , "08"],
                ["X08",  8, "07"], ["X07",  8, "06"], ["X06",  8, "05"], ["X05", 8 , "04"],
                ["X04",  8, "03"], ["X03",  8, "02"], ["U02",  8, "01"], ["U01", 8 , "00"],
                                                                            
                ["V18",  5, "00"], ["V18",  5, "01"], ["U17",  5, "02"], ["V17",  5, "03"], 
                ["U16",  5, "04"], ["V16",  5, "05"], ["U15",  5, "06"], ["V15",  5, "07"], 
                ["U14",  5, "08"], ["V14",  5, "09"], ["U13",  5, "10"], ["V13",  5, "11"], 
                ["U12",  5, "12"], ["V12",  5, "13"], ["U11",  5, "14"], ["V10",  5, "15"], 
                                                                                   
                ["U09",  6, "00"], ["V08",  6, "01"], ["U07",  6, "02"], ["V07",  6, "03"], 
                ["U06",  6, "04"], ["V06",  6, "05"], ["U05",  6, "06"], ["V05",  6, "07"], 
                ["U04",  6, "08"], ["V04",  6, "09"], ["U03",  6, "10"], ["V03",  6, "11"], 
                ["U02",  6, "12"], ["V02",  6, "13"], ["V09",  6, "14"], ["V11",  6, "15"] 
            ]
    for ai in range(len(orgdicts)):
        for al in apa_femb_loc:
            if (orgdicts[ai]["fembchn"] == (al[1]-1)*16 + int(al[2]) ):
                    orgdicts[ai]["wire"] = al[0]
                    break
#print orgdicts[0]
#sys.exit()


orgdicts = dict_filter (orgdicts, or_dnf =femb_cs, and_flg=False  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 0, 107]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 0, 109]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 0, 125]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 1,  48]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 1,  79]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 1, 127]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 2, 124]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 2, 126]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 2, 127]  ) 
for i in range(16):
    orgdicts = dict_del_chn (orgdicts, del_chn = [0, 3, 64+i]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 3, 3]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 3, 4]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 3, 48]  ) 
orgdicts = dict_del_chn (orgdicts, del_chn = [0, 3, 50]  ) 
#orgdicts = dict_filter (orgdicts, and_dnf =[["gain","140"], ["tp","20"]], or_flg=False  ) 
#orgdicts = dict_filter (orgdicts, and_dnf =[ ["tp","20"]], or_flg=False  ) 
#orgdicts = dict_filter (orgdicts, and_dnf =[["gain","078"]], and_flg=True  ) 
#orgdicts = dict_filter (orgdicts, and_dnf =[["tp","20"]], and_flg=True  ) 
print len(orgdicts)

fp = sum_path + fn + "femb%d"%loc + ".pdf" 
pp = PdfPages(fp)
print "start...wait a few minutes..."
plot0_overall_enc (pp, orgdicts, title="APA ENC vs. Tp", calitype="fpg_gain", sfhf = "hf" ) 
plot3_overall_gain (pp, orgdicts, title="APA Gain Measurement" ) 

#plot2_peds (pp, orgdicts,title="Pedestals", gs=[ "140"], tp="20"  , loc = loc) 
plot2_peds (pp, orgdicts,title="Pedestals", gs=["250", "140", "078"], tp="20"  , loc = loc) 
plot1_chns_enc_1 (pp, orgdicts, title="APA ENC Distribution",  cali_cs="fpg_gain", rms_cs = "rms", gs=["250", "140", "078", "047"], tp="20", loc=loc )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution",  cali_cs="fpg_gain", rms_cs = "rms",   g="250", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution",  cali_cs="fpg_gain", rms_cs = "rms",   g="140", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution",  cali_cs="fpg_gain", rms_cs = "rms",   g="078", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution",  cali_cs="fpg_gain", rms_cs = "rms",   g="047", fembs_on_apa = fembs_on_apa )  #
#plot4_chns_gain (pp, orgdicts, title="Gain Distribution",  g="250" , fembs_on_apa = fembs_on_apa)  #
#plot4_chns_gain (pp, orgdicts, title="Gain Distribution",  g="140" , fembs_on_apa = fembs_on_apa)  #
#plot4_chns_gain (pp, orgdicts, title="Gain Distribution",  g="078" , fembs_on_apa = fembs_on_apa)  #
#plot4_chns_gain (pp, orgdicts, title="Gain Distribution",  g="047" , fembs_on_apa = fembs_on_apa)  #
##plot2_peds (pp, orgdicts,title="Pedestals", g="250", tp="20"  , fembs_on_apa = fembs_on_apa) 
##print "please wait a few minutes..."
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "X", cali_cs="fpg_gain", rms_cs = "rms",   g="250", fembs_on_apa = fembs_on_apa )  #
##plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "U", cali_cs="fpg_gain", rms_cs = "rms",   g="250", fembs_on_apa = fembs_on_apa )  #
#plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="X", g="250" , fembs_on_apa = fembs_on_apa)  #
##plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="U", g="250" , fembs_on_apa = fembs_on_apa)  #
##
##print "please wait a few minutes..."
##plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "X", cali_cs="fpg_gain", rms_cs = "rms",   g="140", fembs_on_apa = fembs_on_apa )  #
##plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "U", cali_cs="fpg_gain", rms_cs = "rms",   g="140", fembs_on_apa = fembs_on_apa )  #
##plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="X", g="140" , fembs_on_apa = fembs_on_apa)  #
##plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="U", g="140" , fembs_on_apa = fembs_on_apa)  #
##
##print "please wait a few minutes..."
##plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "X", cali_cs="fpg_gain", rms_cs = "rms",   g="078", fembs_on_apa = fembs_on_apa )  #
##plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "U", cali_cs="fpg_gain", rms_cs = "rms",   g="078", fembs_on_apa = fembs_on_apa )  #
##plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="X", g="078" , fembs_on_apa = fembs_on_apa)  #
##plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="U", g="078" , fembs_on_apa = fembs_on_apa)  #
##
##print "please wait a few minutes..."
##plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "X", cali_cs="fpg_gain", rms_cs = "rms",   g="047", fembs_on_apa = fembs_on_apa )  #
##plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "U", cali_cs="fpg_gain", rms_cs = "rms",   g="047", fembs_on_apa = fembs_on_apa )  #
##plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="X", g="047" , fembs_on_apa = fembs_on_apa)  #
##plot4_chns_gain (pp, orgdicts, title="Gain Distribution", wiretype="U", g="047" , fembs_on_apa = fembs_on_apa)  #

#print "please wait a few minutes..."
#plot0_overall_enc (pp, orgdicts, title="APA ENC vs. Tp", calitype="asi_gain", sfhf = "sf" ) 
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "X", cali_cs="fpg_gain", rms_cs = "sfrms", g="250", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "V", cali_cs="fpg_gain", rms_cs = "sfrms", g="250", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "U", cali_cs="fpg_gain", rms_cs = "sfrms", g="250", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "X", cali_cs="fpg_gain", rms_cs = "sfrms", g="140", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "V", cali_cs="fpg_gain", rms_cs = "sfrms", g="140", fembs_on_apa = fembs_on_apa )  #
#plot1_chns_enc (pp, orgdicts, title="APA ENC Distribution", wiretype = "U", cali_cs="fpg_gain", rms_cs = "sfrms", g="140", fembs_on_apa = fembs_on_apa )  #

pp.close()

print fp 
print "Done"

