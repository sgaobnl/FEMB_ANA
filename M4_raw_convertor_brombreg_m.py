# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: 1/17/2019 4:50:54 PM
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
from openpyxl import Workbook
import numpy as np
import struct
import os
from sys import exit
import os.path
import copy

def rawto32chn(onepkgdata, i, chn_data):
    if (onepkgdata[i] == 0xface ) or (onepkgdata[i] == 0xfeed ):
        if (onepkgdata[i] == 0xface ):
            pre = 0x00000
        elif(onepkgdata[i] == 0xfeed ):
            pre = 0x10000
        chn_data[7].append( pre + ((onepkgdata[i+1] & 0X0FFF)<<0 ))
        chn_data[6].append( pre + ((onepkgdata[i+2] & 0X00FF)<<4)+ ((onepkgdata[i+1] & 0XF000) >> 12))
        chn_data[5].append( pre + ((onepkgdata[i+3] & 0X000F)<<8) +((onepkgdata[i+2] & 0XFF00) >> 8 ))
        chn_data[4].append( pre + ((onepkgdata[i+3] & 0XFFF0)>>4 ))

        chn_data[3].append( pre + ( onepkgdata[i+3+1] & 0X0FFF)<<0 )
        chn_data[2].append( pre + ((onepkgdata[i+3+2] & 0X00FF)<<4) + ((onepkgdata[i+3+1] & 0XF000) >> 12))
        chn_data[1].append( pre + ((onepkgdata[i+3+3] & 0X000F)<<8) + ((onepkgdata[i+3+2] & 0XFF00) >> 8 ))
        chn_data[0].append( pre + ((onepkgdata[i+3+3] & 0XFFF0)>>4) )

        chn_data[15].append(pre +  ((onepkgdata[i+6+1] & 0X0FFF)<<0 ))
        chn_data[14].append(pre +  ((onepkgdata[i+6+2] & 0X00FF)<<4 )+ ((onepkgdata[i+6+1] & 0XF000) >> 12))
        chn_data[13].append(pre +  ((onepkgdata[i+6+3] & 0X000F)<<8 )+ ((onepkgdata[i+6+2] & 0XFF00) >> 8 ))
        chn_data[12].append(pre +  ((onepkgdata[i+6+3] & 0XFFF0)>>4 ))

        chn_data[11].append(pre +  ((onepkgdata[i+9+1] & 0X0FFF)<<0 ))
        chn_data[10].append(pre +  ((onepkgdata[i+9+2] & 0X00FF)<<4 )+ ((onepkgdata[i+9+1] & 0XF000) >> 12))
        chn_data[9].append( pre +  ((onepkgdata[i+9+3] & 0X000F)<<8 )+ ((onepkgdata[i+9+2] & 0XFF00) >> 8 ))
        chn_data[8].append( pre +  ((onepkgdata[i+9+3] & 0XFFF0)>>4 ))


        chn_data[23].append(pre +  ((onepkgdata[12+i+1] & 0X0FFF)<<0 ))
        chn_data[22].append(pre +  ((onepkgdata[12+i+2] & 0X00FF)<<4)    +((onepkgdata[12+i+1] & 0XF000) >> 12))
        chn_data[21].append(pre +  ((onepkgdata[12+i+3] & 0X000F)<<8)    +((onepkgdata[12+i+2] & 0XFF00) >> 8 ))
        chn_data[20].append(pre +  ((onepkgdata[12+i+3] & 0XFFF0)>>4 ))

        chn_data[19].append(pre +  ( onepkgdata[12+i+3+1] & 0X0FFF)<<0 )
        chn_data[18].append(pre +  ((onepkgdata[12+i+3+2] & 0X00FF)<<4) + ((onepkgdata[12+i+3+1] & 0XF000) >> 12))
        chn_data[17].append(pre +  ((onepkgdata[12+i+3+3] & 0X000F)<<8) + ((onepkgdata[12+i+3+2] & 0XFF00) >> 8 ))
        chn_data[16].append(pre +  ((onepkgdata[12+i+3+3] & 0XFFF0)>>4) )

        chn_data[31].append(pre +  ((onepkgdata[12+i+6+1] & 0X0FFF)<<0 ))
        chn_data[30].append(pre +  ((onepkgdata[12+i+6+2] & 0X00FF)<<4 )+ ((onepkgdata[12+i+6+1] & 0XF000) >> 12))
        chn_data[29].append(pre +  ((onepkgdata[12+i+6+3] & 0X000F)<<8 )+ ((onepkgdata[12+i+6+2] & 0XFF00) >> 8 ))
        chn_data[28].append(pre +  ((onepkgdata[12+i+6+3] & 0XFFF0)>>4 ))

        chn_data[27].append(pre +  ((onepkgdata[12+i+9+1] & 0X0FFF)<<0 ))
        chn_data[26].append(pre +  ((onepkgdata[12+i+9+2] & 0X00FF)<<4 )+ ((onepkgdata[12+i+9+1] & 0XF000) >> 12))
        chn_data[25].append(pre +  ((onepkgdata[12+i+9+3] & 0X000F)<<8 )+ ((onepkgdata[12+i+9+2] & 0XFF00) >> 8 ))
        chn_data[24].append(pre +  ((onepkgdata[12+i+9+3] & 0XFFF0)>>4 ))

        cycle_del = False
    else:
        print "ERROR"
        exit()
        cycle_del = True
    i = i + 25 
    return chn_data, i ,cycle_del

def raw_convertor_brombreg(path, step,  fe_cfg_r, femb_np=[0,1,2,3],chip_np=[0,2,4,6], cycle = 100, jumbo_flag=True):
    if (jumbo_flag == True):
        #pkg_len = 0x1E06/2
        pkg_len = 0x1DC0/2
    else:
        pkg_len = 0x406/2

    wib_cycle_femb_chip = []
    for cycle_no in range(cycle):
        print "cycle#%d"%cycle_no
        cycle_del = False
        cycle_femb_chip = []
        for femb in femb_np:
            if (not cycle_del):
                femb_chip = []
                for chip in chip_np:
                    if (not cycle_del):
                        filename = step + "_FEMB" + str(femb) + "CHIP" + str(chip) + "_" + fe_cfg_r + "_" + format(cycle_no, "04d") +".bin"
                        #print filename
                        file_path = path + filename
                        chn_data = []
                        for i in range(32):
                            chn_data.append([])
                        with open(file_path, 'rb') as f:
                            raw_data = f.read()                
                            len_file = len(raw_data) 
                            dataNtuple =struct.unpack_from(">%dH"%(len_file//2),raw_data)
                            for addr in range(0,len(dataNtuple) - pkg_len,pkg_len):
                                pkg_cnt0 = (((long(dataNtuple[addr]) << 16 )+ long(dataNtuple[addr+1])) + 1 ) & 0xFFFFFFFF
                                pkg_cnt1 = ((long(dataNtuple[addr+pkg_len]) << 16 )+ long(dataNtuple[addr+1+pkg_len])) &0xFFFFFFFF
                                if (pkg_cnt0 != pkg_cnt1):
                                    print "%s: UDP package size is not right! discard cycle_no#%d"%(filename,cycle_no)
                                    cycle_del = True
                                    break

                                onepkgdata = dataNtuple[addr : addr + pkg_len]
                                print hex(addr),  hex(addr + pkg_len)

                                for i in range(8,pkg_len,1):
                                    if (onepkgdata[i] == 0xface ) or (onepkgdata[i] == 0xfeed ):
                                        print hex(onepkgdata[i]), hex(onepkgdata[i+1]), hex(onepkgdata[i+2]), hex(onepkgdata[i+3])
                                        break

                                while i < (len(onepkgdata)-25) :
                                    chn_data, i ,cycle_del =  rawto32chn(onepkgdata, i, chn_data)
                            for smp in range(len(chn_data[0])):
                                if ((chn_data[0][smp] & 0x10000) == 0x10000): # feed align
                                    break
                        chipdata = [chip,chn_data,smp]
                        femb_chip.append(chipdata)
                        smp_0 =femb_chip[0][2] 
                        for tmp in femb_chip:
                            if (smp_0 != tmp[2] ):
                                print " first 'feed' is unsynced! discard cycle#%d"%cycle_no
                                i = 0
                                for tmpx in femb_chip:
                                    print "chip%d first feed address: %d"%(i,tmpx[2])
                                    i = i + 2
                                cycle_del = True
                                break
                    else:
                        break

                fembdata = [femb,femb_chip]
                cycle_femb_chip.append(fembdata)
            else:
                break
        if (not cycle_del ):
            cycledata = [cycle_no,cycle_femb_chip]
            wib_cycle_femb_chip.append(cycledata)

    return wib_cycle_femb_chip

def femb_raw(wib_cycle_femb_chip, femb=0, sync_chns=128):
    femb_rawdata = []
    for chn in range(sync_chns):
        chndata = []
        chipx2 = (chn//32)*2
        chipchn = chn%32
        for cycledata in wib_cycle_femb_chip:
            for fembdata in cycledata[1]: #cycle_femb_chip
                if fembdata[0] == femb :
                    for chipdata in fembdata[1] :
                        if chipdata[0] == chipx2:
                            for sdata in chipdata[1][chipchn]:
                                chndata.append(sdata & 0x0FFFF ) #clear feed info
        femb_rawdata.append(chndata)
    return femb_rawdata

import sys
rmsstrdate = sys.argv[1] #
rmsstrrun = sys.argv[2]  #
strenv = sys.argv[3]
rmsstrstep = sys.argv[4]
cycle = int(sys.argv[5])
jumbo_flag = sys.argv[6]
server_flg = sys.argv[7]

if (jumbo_flag == "True"):
    jumbo_flag = True
else:
    jumbo_flag = False

if (server_flg == "server" ):
    datepath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA3/Rawdata_"+ rmsstrdate + "/" 
else:
    datepath = "/Users/shanshangao/Documents/Share_Windows/CERN_test_stand/Rawdata/Rawdata_"+ rmsstrdate + "/" 
datepath = "D:/SBND_40APA/Rawdata/Rawdata_" + rmsstrdate + "/"

#femb_set = strenv+"step" +rmsstrstep
femb_set = "step" +rmsstrstep
run_no = "run" + rmsstrrun
rawpath = datepath + run_no + "/"
step_np =[ "WIB00"+femb_set]
chip_np=[0,2,4,6]
femb_np=[0,1,2,3]

for step in step_np:
    path = rawpath
    #path = rawpath + step + "/"
    print path
    for root, dirs, files in os.walk(path):
        break

    for onefile in files:
        if ( onefile.find("_0000.bin") >= 0 ) and ( onefile.find("FEMB0CHIP0") >= 0 ) :
            pos = onefile.find("FEMB0CHIP0")
            fe_cfg = onefile[pos+12]
            break

    for femb in range(4):
        for tp_no in ["0","1","2","3"]:
            fe_cfg_r = "%X"%(int(tp_no) + 0x08) + fe_cfg
            wib_cycle_femb_chip = raw_convertor_brombreg(path, step,  fe_cfg_r, femb_np,chip_np, cycle, jumbo_flag)
            femb_rawdata = femb_raw(wib_cycle_femb_chip, femb, sync_chns=128)
            
            import pickle
            savefile = rawpath + step + "FEMB"+ str(femb)+"_" +  fe_cfg_r + ".bin"
            with open(savefile, 'wb') as fp:
                pickle.dump(femb_rawdata, fp)
    
