# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Sep 23 00:35:47 2018
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
from matplotlib.backends.backend_pdf import PdfPages
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from apa_mapping import APA_MAP
apamap = APA_MAP()
from femb_position import femb_position
from all_FEMBs_results import All_FEMBs_results
from readlog import readlog
from read_rtds import run_rtds

def APA_sort(APAno = 1):
    femb_pos_np = femb_position(APAno)
    All_sort, X_sort, V_sort, U_sort = apamap.apa_femb_mapping_pd()
    APA_sort_all = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_sort_all.append([femb_pos, All_sort])

    APA_X_sort = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_X_sort.append([femb_pos, X_sort])
    
    APA_V_sort = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_V_sort.append([femb_pos, V_sort])
    
    APA_U_sort = []
    for apa_slot in range(1,21,1):
        for femb_pos in femb_pos_np:
            if int(femb_pos[0][2:4]) ==  apa_slot :
                break
        APA_U_sort.append([femb_pos, U_sort])

    return APA_sort_all, APA_X_sort, APA_V_sort, APA_U_sort 

def plots(plt, plot_en, apa_results, loginfo, run_temp, sort_np, pp, gain=2, max_limit=15, min_limit=5, frontpage = False, APAno = 3, r_wfm = "./"):
    fembinfo = []

    if gain == 3:
        egain = 80
    if gain == 1:
        egain = 145
    if gain == 2:
        egain = 250
    if gain == 0:
        egain = 425

    for onefemb_loc in range(20): 
        ped_np         = []
        rms_np         = []
        sf_ped_np      = []
        sf_rms_np      = []
        sf_ratio_np    = []
        chn_peakp_avg  = []
        chn_peakn_avg  = []
        chn_wave       = []
        chn_pedwave       = []
        chn_peakp_ped  = []
        chn_peakn_ped  = []
        chnwib_np      = []
        chnfemb_np     = []
        chnasic_np     = []
        chnchn_np      = []
        chnwire_np     = []

        onefemb = sort_np[onefemb_loc]
        #if ( onefemb[0][1].find("WIB2_FEMB0") >= 0 ) or ( onefemb[0][1].find("WIB2_FEMB2") >= 0 ):
        if (True) :
            if len(onefemb[1]) == 128 :
                wiretype = "ALL"
                color = "m"
            elif onefemb[1][0][0][0] == "X" :
                wiretype = "X"   
                color = "g"
            elif onefemb[1][0][0][0] == "V" :
                wiretype = "V"  
                color = "b"
            elif onefemb[1][0][0][0] == "U" :
                wiretype = "U"
                color = "r"
       
            for chn_info in onefemb[1]: #find chn
                for chndata in apa_results:
                    if (onefemb[0][0] == chndata[0][0] ) and (chn_info[0:4] == chndata[1][0:4]) :
                        chnwire_np.append(chn_info[0][0])
                        chnwib_np.append(chndata[2])
                        chnfemb_np.append(chndata[3])
                        chnasic_np.append(chndata[4])
                        chnchn_np.append(chndata[5])
                        ped_np.append(chndata[6])
                        rms_np.append(chndata[7])
                        sf_ped_np.append(chndata[8])
                        sf_rms_np.append(chndata[9])
                        sf_ratio_np.append(chndata[10])
                        chn_peakp_avg.append(chndata[11] -  chndata[6])
                        chn_peakn_avg.append(chndata[12] -  chndata[6])
                        #chn_wave.append(chndata[14][ chndata[15][1] : chndata[15][1]+100])
                        smp_length = len(chndata[13])
                        #chn_wave.append(chndata[14][ chndata[15][2] : chndata[15][2]+100])
                        chn_wave.append(chndata[14][ chndata[15][0] : chndata[15][2]+10000]) #full waveform with calibration pulse
                        chn_pedwave.append(chndata[13][ chndata[15][0] : chndata[15][2]+10000]) #detector signals & pedestal
                        chn_peakp_ped.append(chndata[11])
                        chn_peakn_ped.append(chndata[12])


        fembinfo.append([onefemb_loc, np.array(ped_np)        , np.array(rms_np)        , np.array(sf_ped_np)     , np.array(sf_rms_np)     , \
                    np.array(sf_ratio_np)   , np.array(chn_peakp_avg), np.array(chn_peakn_avg), chn_wave      , np.array(chn_peakp_ped) , \
                    np.array(chn_peakn_ped) , chnwib_np     , chnfemb_np    , chnasic_np    , chnchn_np, chnwire_np, chn_pedwave    ] )

    for fembloc in range(20):
        ped_np         = fembinfo[fembloc][1]
        chnsum = len(ped_np)
        if chnsum != 0:
            break
    total_chn = chnsum*20

    if (frontpage == True ):
        fig = plt.figure(figsize=(16,9))
        ax = plt
        #ax.tight_layout( rect=[0, 0.05, 1, 0.95])
        ax.text(0.4,0.9, "Test Summary", fontsize = 32, color = 'g')
        ax.text(0.05,0.80, "APA no.        : " + loginfo[0], fontsize=16 )
        ax.text(0.05,0.75, "Enviroment     : " + loginfo[1], fontsize=16 )
        ax.text(0.05,0.70, "Description    : " + loginfo[2], fontsize=16 )
        if ( run_temp != None ):
            ax.text(0.05,0.65, "RTDs(TT0206 to TT0200) measured at %s: %3dK, %3dK, %3dK, %3dK, %3dK, %3dK, %3dK "%(run_temp[8],\
                    run_temp[7],run_temp[6],run_temp[5],run_temp[4],run_temp[3],run_temp[2],run_temp[1] ), fontsize=16 )
        else:
            ax.text(0.05,0.65, "Temperature    : " + loginfo[3], fontsize=16 )
        ax.text(0.05,0.60, "Test type      : " + loginfo[4], fontsize=16 )
        ax.text(0.05,0.55, "Rawdata path   : " + loginfo[5], fontsize=16 )
        ax.text(0.05,0.50, "Test started at : " + loginfo[6], fontsize=16 )
        if (len(loginfo[7]) > 5 ):
            ax.text( (total_chn/40.0),300, "Inactive FEMBs : " + loginfo[7] )
        ax.savefig(pp, format='pdf')
        ax.close()

    if ( (plot_en&0x01) != 0 ):
    #plot pedestal        
        fig = plt.figure(figsize=(16,9))
        ax = plt
        ped_np = np.array(ped_np)
        chn_peakp_ped = np.array( chn_peakp_ped )
        patch = []
        label = []
        title = "%s plane: Pedestal Measurement " % wiretype
        ylabel = "ADC output /bin"
        print "Pedestal Measurement-->%s wires has %d channels in total"%(wiretype, total_chn)

        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            if len(ped_np)!= 0:
                ped_label = "Pedestal / ADC bin"
                y_np = ped_np
                ax.scatter( chn_np, y_np)
                ax.plot( chn_np, y_np)

                if (fembloc < 10 ):
                    ax.text (chn_np[0], 100, "B" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                else:
                    ax.text (chn_np[0], 100, "A" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                ax.text (chn_np[0], 3800, "Alive", color = 'g' )
                ax.text (chn_np[0], 3600, "WIB%d"%(chnwib_np[0]+1 ), color = 'g'  )
                ax.text (chn_np[0], 3400, "FEMB%d"%(chnfemb_np[0]), color = 'g'  )
            else:
                ax.text (chn_np[0], 3800, "Dead", color = 'r' )
#                ax.text (chn_np[0], 3500, "WIB%d"%(chnwib_np[0] ), color = 'r'  )
#                ax.text (chn_np[0], 3200, "FEMB%d"%(chnfemb_np[0]), color = 'r'  )

#        patch.append( mpatches.Patch(color=color))
#        label.append(ped_label)
#        ax.legend(patch, label, loc=1, fontsize=18 )
        ax.tick_params(labelsize=24)
        ax.xlim([0,total_chn])
        ax.ylim([0,4100])
        ax.text( (total_chn/40.0),450, "Test started at : " + loginfo[6] )
        if (len(loginfo[7]) > 5 ):
            ax.text( (total_chn/40.0),300, "Inactive FEMBs : " + loginfo[7] )
        ax.ylabel(ylabel, fontsize=18 )
        ax.xlabel("APA %s Channel No."%wiretype, fontsize=18 )
        ax.title(title , fontsize=18 )
        ax.grid()
        #ax.tight_layout( rect=[0, 0.05, 1, 0.95])
        ax.savefig(pp, format='pdf')
        ax.close()

    if ( (plot_en&0x02) != 0 ):
    #plot  pulse amplitude       
        fig = plt.figure(figsize=(16,9))
        ax = plt
        chn_peakp_avg = np.array( chn_peakp_avg )
        chn_peakn_avg = np.array( chn_peakn_avg )
        patch = []
        label = []
        title = "%s plane Pulse Amplitude " %wiretype
        ylabel = "ADC output /bin"
        print "Pulse Amplitude-->%s wires has %d channels in total"%(wiretype, total_chn)

        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            if len(ped_np)!= 0:
                for i in range(2):
                    if ( i == 0 ):
                        color = 'm'
                        ped_label = "Positive Pulse Amplitude / ADC bin"
                        y_np = chn_peakp_avg 
                    elif ( i == 1 ):
                        color = 'b'
                        ped_label = "Negative Pulse Amplitude / ADC bin"
                        y_np = chn_peakn_avg 

                    ax.scatter( chn_np, y_np)
                    ax.plot( chn_np, y_np)

                if (fembloc < 10 ):
                    ax.text (chn_np[0], -1800, "B" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                else:
                    ax.text (chn_np[0], -1800, "A" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                ax.text (chn_np[0], 2800, "Alive", color = 'g' )
                ax.text (chn_np[0], 2600, "WIB%d"%(chnwib_np[0]+1 ), color = 'g'  )
                ax.text (chn_np[0], 2400, "FEMB%d"%(chnfemb_np[0]), color = 'g'  )
            else:
                ax.text (chn_np[0], 2800, "Dead", color = 'r' )
#                ax.text (chn_np[0], 2500, "WIB%d"%(chnwib_np[0] ), color = 'r'  )
#                ax.text (chn_np[0], 2200, "FEMB%d"%(chnfemb_np[0]), color = 'r'  )
#        patch.append( mpatches.Patch(color='m'))
#        label.append(ped_label)
#        patch.append( mpatches.Patch(color='b'))
#        label.append(ped_label)
#        ax.legend(patch, label, loc=1, fontsize=18 )
        ax.tick_params(labelsize=24)
        ax.xlim([0,total_chn])
        ax.ylim([-2000,3000])
        ax.text( (total_chn/40.0),-1500, "Test started at  : " + loginfo[6] )
        if (len(loginfo[7]) > 5 ):
            ax.text( (total_chn/40.0),300, "Inactive FEMBs : " + loginfo[7] )
 
        ax.ylabel(ylabel, fontsize=18 )
        ax.xlabel("APA %s Channel No."%wiretype, fontsize=18 )
        ax.title(title , fontsize=18 )
        ax.grid()
        ax.tight_layout( rect=[0, 0.05, 1, 0.95])
        ax.savefig(pp, format='pdf')
        ax.close()
    
    if ( (plot_en&0x04) != 0 ):
    ####plot  pulse  wave      
        #title = "%s planes: Pulse Waveform Overlap of %d wires"%( wiretype, total_chn)
        #title = "Pulse Waveform Overlap of %d wires"%(total_chn)
        ylabel = "ADC output /bin"

        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]
            chnwire_np     = fembinfo[fembloc][15]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            cs_chns = [176 ,476 ,618 ,634 ,639 ,1343 ,1344 ,2000 ,2084 ,2291 ,2438 ,2440 ,2462 ,2467]
            #cs_chns =range(500,700,1)
            #cs_chns =range(2560)
            if len(ped_np)!= 0:
                for achn in cs_chns:
                    if (achn in chn_np): 
                        chn = achn - chnsum * fembloc
                        #if (achn in chn_np) and (sf_rms_np[chn] > 20):
                        if (achn in chn_np) :
                            print achn, rms_np[chn],sf_rms_np[chn]
                            fig = plt.figure(figsize=(12,8))
                            ax = plt
                            y_np = np.array(chn_wave[chn])
                            y_max = np.max(y_np)
                            smps_np = np.arange(len(chn_wave[chn])) 
                            x_np = smps_np * 0.5
                            ax.scatter( x_np, y_np)
                            ax.plot( x_np, y_np)
                            ax.scatter( x_np, y_np)
                            ax.plot( x_np, y_np)
                            ax.xlim([0,np.max(x_np)])
                            ax.tick_params(labelsize=16)
                            ax.ylim([000,4100])
                            ax.ylabel(ylabel, fontsize=16 )
                            ax.xlabel("Time / us", fontsize=16 )
                            title = "APA" + str(APAno) + "_" + "TPC%04d_"%achn + "_" + chnwire_np[chn] + "_LOC" + str(fembloc) + "WIB%d"%chnwib_np[chn] + "FEMB%d"%chnfemb_np[chn] + "CHN%d"%chn  
                            ax.title(title , fontsize=16 )
                            ax.grid()
                            ax.tight_layout( rect=[0, 0.05, 1, 0.95])
                            r_wfm = result_dir + title + '_gain' + str(gain) +  "tp" + str(tp) +'.png'
                            ax.savefig(r_wfm, format='png')
                            ax.close()
  
    if ( (plot_en&0x80) != 0 ):
        ylabel = "ADC output /bin"
        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]
            chnwire_np     = fembinfo[fembloc][15]
            chn_pedwave  = fembinfo[fembloc][16]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            #cs_chns = [176 ,476 ,618 ,634 ,639 ,1343 ,1344 ,2000 ,2084 ,2291 ,2438 ,2440 ,2462 ,2467]
            #cs_chns =range(500,700,1)
            cs_chns =range(2560)
            if len(ped_np)!= 0:
                for achn in cs_chns:
                    if (achn in chn_np): 
                        chn = achn - chnsum * fembloc
                        #if (achn in chn_np) and (sf_rms_np[chn] > 20):
                        max_sample = np.max(chn_pedwave[chn])
                        min_sample = np.max(chn_pedwave[chn])
                        set_amp = 200
                        if ( (max_sample - ped_np[chn]) > set_amp ):
                            pos = np.where(chn_pedwave[chn] == max_sample)[0][0]
                        elif ( abs(min_sample - ped_np[chn]) > set_amp ):
                            pos = np.where(chn_pedwave[chn] == min_sample)[0][0]
                        else:
                            pos = -1

                        if (achn in chn_np) and ( pos>=100 ):
                            print achn, rms_np[chn],sf_rms_np[chn]
                            fig = plt.figure(figsize=(16,9))
                            ax = plt
                            plot_wave = chn_pedwave[chn][pos-100, pos+100]
                            y_np = np.array(plot_wave)
                            y_max = np.max(y_np)
                            smps_np = np.arange(len(plot_wave)) 
                            x_np = smps_np * 0.5
                            ax.scatter( x_np, y_np)
                            ax.plot( x_np, y_np)
                            ax.scatter( x_np, y_np)
                            ax.plot( x_np, y_np)
                            ax.xlim([0,np.max(x_np)])
                            ax.tick_params(labelsize=20)
                            ax.ylim([000,4100])
                            ax.ylabel(ylabel, fontsize=20 )
                            ax.xlabel("Time / us", fontsize=20 )
                            title = "APA" + str(APAno) + "_" + "TPC%04d_"%achn + "_" + chnwire_np[chn] + "_LOC" + str(fembloc) + "WIB%d"%chnwib_np[chn] + "FEMB%d"%chnfemb_np[chn] + "CHN%d"%chn  
                            ax.title("Detector Signal Waveform \n" + title , fontsize=16 )
                            ax.grid()
                            ax.tight_layout( rect=[0, 0.05, 1, 0.95])
                            r_wfm = result_dir + title + '_gain' + str(gain) +  "tp" + str(tp) +'.png'
                            ax.savefig(r_wfm, format='png')
                            ax.close()
    
    if ( (plot_en&0x08) != 0 ):
    ##rms pedestal        
        fig = plt.figure(figsize=(16,9))
        ax = plt
    
        rms_np = np.array(rms_np)
        sf_rms_np = np.array(sf_rms_np)
        patch = []
        label = []
        title = "%s plane: Noise Measurement" %wiretype
        ylabel = "%s plane: RMS noise / e-"%wiretype
        print "Noise Measurement-->%s wires has %d channels in total"%(wiretype, total_chn)

        label_flag = True
        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]
            chnwire_np      = fembinfo[fembloc][15]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            if len(ped_np)!= 0:
                #color = 'b'
                plabel = "RMS Noise / e-"
                y_np = rms_np*egain
                sf_y_np = sf_rms_np*egain
                for i in range(len(chn_np)):
                    if (sf_y_np[i] >=1000 ):
                        print "%d, %d, %d, %d, %d, %d, %s, %d, %d"%(chn_np[i], chnwib_np[i], chnfemb_np[i], i, chnasic_np[i], chnchn_np[i], chnwire_np[i], sf_y_np[i], y_np[i])
                    elif (sf_y_np[i] <350 ):
                        print "%d, %d, %d, %d, %d, %d, %s, %d, %d"%(chn_np[i], chnwib_np[i], chnfemb_np[i], i, chnasic_np[i], chnchn_np[i], chnwire_np[i], sf_y_np[i], y_np[i])

                xchn_np = []
                xy_np = []
                vchn_np = []
                vy_np = []
                uchn_np = []
                uy_np = []
                for i in range(len(chn_np)):
                    if chnwire_np[i] == "X" :
                        xchn_np.append(chn_np[i])
                        xy_np.append(y_np[i])
                        color = 'g'
                    elif chnwire_np[i] == "V" :
                        vchn_np.append(chn_np[i])
                        vy_np.append(y_np[i])
                        color = 'b'
                    elif chnwire_np[i] == "U" :
                        uchn_np.append(chn_np[i])
                        uy_np.append(y_np[i])
                        color = 'r'
 
                if (label_flag):
                    ax.plot( xchn_np, xy_np, color='g', label = "X wire")
                    ax.plot( vchn_np, vy_np, color='b', label = "V wire")
                    ax.plot( uchn_np, uy_np, color='r', label = "U wire")
                    label_flag = False
                else:
                    ax.plot( xchn_np, xy_np, color='g')
                    ax.plot( vchn_np, vy_np, color='b')
                    ax.plot( uchn_np, uy_np, color='r')
 
                ax.scatter(xchn_np, xy_np,color='g', marker='.')
                ax.scatter(vchn_np, vy_np,color='b', marker='.')
                ax.scatter(uchn_np, uy_np,color='r', marker='.')

#                for i in range(len(chn_np)):
#                    if chnwire_np[i] == "X" :
#                        color = 'g'
#                    elif chnwire_np[i] == "V" :
#                        color = 'b'
#                    elif chnwire_np[i] == "U" :
#                        color = 'r'
#                    ax.scatter( [chn_np[i]], [y_np[i]], color = color, marker = '.')
                if (fembloc < 10 ):
                    ax.text (chn_np[0], 100, "B" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                else:
                    ax.text (chn_np[0], 100, "A" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                ax.text (chn_np[0]+2, 1900, "Alive", color = 'g' )
                ax.text (chn_np[0]+2, 1800, "WIB%d"%(chnwib_np[0]+1 ), color = 'g'  )
                ax.text (chn_np[0]+2, 1700, "FEMB%d"%(chnfemb_np[0]), color = 'g'  )
                ax.vlines(chn_np[0], 0, 5000, color='m', linestyles="dotted", linewidth=0.8)
#                print "APA_LOC"+(format(fembloc+1, "2d"))
            else:
                ax.text (chn_np[0], 4800, "Dead", color = 'r' )
#                ax.text (chn_np[0], 4400, "WIB%d"%(chnwib_np[0] ), color = 'r'  )
#                ax.text (chn_np[0], 4000, "FEMB%d"%(chnfemb_np[0]), color = 'r'  )

#        patch.append( mpatches.Patch(color=color))
#        label.append(plabel)
#        ax.legend(patch, label, loc=1, fontsize=18 )
        ax.tick_params(labelsize=24)
        ax.xlim([0,total_chn])
        ax.ylim([0,2000])
        ax.legend(loc=6)
        ax.text( (total_chn/40.0),4100, "Test started at  : " + loginfo[6] )
        if (len(loginfo[7]) > 5 ):
            ax.text( (total_chn/40.0),300, "Inactive FEMBs : " + loginfo[7] )
 
        ax.ylabel(ylabel, fontsize=24 )
        ax.xlabel("APA %s Channel No."%wiretype, fontsize=24 )
        ax.title(title , fontsize=24 )
#        ax.grid()
        ax.tight_layout( rect=[0, 0.05, 1, 0.95])
        ax.savefig(pp, format='pdf')
        ax.close()

    
    if ( (plot_en&0x10) != 0 ):
    ##rms pedestal        
        fig = plt.figure(figsize=(16,9))
        ax = plt
    
        rms_np = np.array(rms_np)
        sf_rms_np = np.array(sf_rms_np)
        patch = []
        label = []
        title = "%s plane: Noise Measurement" %wiretype
        ylabel = "%s plane: RMS noise / e-"%wiretype
        print "Noise Measurement-->%s wires has %d channels in total"%(wiretype, total_chn)

        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            if len(ped_np)!= 0:
                for i in range(2):
                    if ( i == 0 ):
                        color = 'm'
                        plabel0 = "RMS Noise / e-"
                        y_np = rms_np*egain
                    elif ( i == 1 ):
                        color = 'b'
                        plabel1 = "SF RMS Noise / e-"
                        y_np = sf_rms_np*egain
                    ax.scatter( chn_np, y_np, color = color)
                    ax.plot( chn_np, y_np, color = color)

                if (fembloc < 10 ):
                    ax.text (chn_np[0], 100, "B" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                else:
                    ax.text (chn_np[0], 100, "A" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )

                ax.text (chn_np[0], 1900, "Alive", color = 'g' )
                ax.text (chn_np[0], 1800, "WIB%d"%(chnwib_np[0]+1 ), color = 'g'  )
                ax.text (chn_np[0], 1700, "FEMB%d"%(chnfemb_np[0]), color = 'g'  )
            else:
                ax.text (chn_np[0], 4800, "Dead", color = 'r' )
                #ax.text (chn_np[0], 4400, "WIB%d"%(chnwib_np[0] ), color = 'r'  )
                #ax.text (chn_np[0], 4000, "FEMB%d"%(chnfemb_np[0]), color = 'r'  )

        patch.append( mpatches.Patch(color='m'))
        label.append(plabel0)
        patch.append( mpatches.Patch(color='b'))
        label.append(plabel1)
        ax.legend(patch, label, loc=1, fontsize=18 )
        ax.tick_params(labelsize=24)
        ax.xlim([0,total_chn])
        ax.ylim([0,2000])
        ax.text( (total_chn/40.0),700, "Test started at  : " + loginfo[6] )
        if (len(loginfo[7]) > 5 ):
            ax.text( (total_chn/40.0),300, "Inactive FEMBs : " + loginfo[7] )
 
        ax.ylabel(ylabel, fontsize=18 )
        ax.xlabel("APA %s Channel No."%wiretype, fontsize=18 )
        ax.title(title , fontsize=18 )
        ax.grid()
        ax.tight_layout( rect=[0, 0.05, 1, 0.95])
        ax.savefig(pp, format='pdf')
        ax.close()
   
#    if ( (plot_en&0x80) != 0 ):
#    ##rms pedestal        
#        for fembloc in range(20):
#            fig = plt.figure(figsize=(16,9))
#            ax = plt
#    
#            rms_np = np.array(rms_np)
#            sf_rms_np = np.array(sf_rms_np)
#            patch = []
#            label = []
#            title = "%s plane: Noise Measurement" %wiretype
#            ylabel = "%s plane: RMS noise / e-"%wiretype
#
#            ped_np         = fembinfo[fembloc][1]
#            rms_np         = fembinfo[fembloc][2]
#            sf_ped_np      = fembinfo[fembloc][3]
#            sf_rms_np      = fembinfo[fembloc][4]
#            sf_ratio_np    = fembinfo[fembloc][5]
#            chn_peakp_avg  = fembinfo[fembloc][6]
#            chn_peakn_avg  = fembinfo[fembloc][7]
#            chn_wave       = fembinfo[fembloc][8]
#            chn_peakp_ped  = fembinfo[fembloc][9]
#            chn_peakn_ped  = fembinfo[fembloc][10]
#            chnwib_np      = fembinfo[fembloc][11]
#            chnfemb_np     = fembinfo[fembloc][12]
#            chnasic_np     = fembinfo[fembloc][13]
#            chnchn_np      = fembinfo[fembloc][14]
#
#            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
#            if len(ped_np)!= 0:
#                for i in range(2):
#                    if ( i == 0 ):
#                        color = 'm'
#                        plabel0 = "RMS Noise / e-"
#                        y_np = rms_np*egain
#                    elif ( i == 1 ):
#                        color = 'b'
#                        plabel1 = "SF RMS Noise / e-"
#                        y_np = sf_rms_np*egain
#                    ax.scatter( chn_np, y_np, color = color)
#                    ax.plot( chn_np, y_np, color = color)
#
#                if (fembloc < 10 ):
#                    ax.text (chn_np[0], 100, "B" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
#                else:
#                    ax.text (chn_np[0], 100, "A" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
#
#                ax.text (chn_np[0], 1800, "Alive", color = 'g' )
#                ax.text (chn_np[0], 1600, "WIB%d"%(chnwib_np[0]+1 ), color = 'g'  )
#                ax.text (chn_np[0], 1400, "FEMB%d"%(chnfemb_np[0]), color = 'g'  )
#            else:
#                ax.text (chn_np[0], 1800, "Dead", color = 'r' )
##                ax.text (chn_np[0], 4400, "WIB%d"%(chnwib_np[0] ), color = 'r'  )
##                ax.text (chn_np[0], 4000, "FEMB%d"%(chnfemb_np[0]), color = 'r'  )
#
#            patch.append( mpatches.Patch(color='m'))
#            label.append(plabel0)
#            patch.append( mpatches.Patch(color='b'))
#            label.append(plabel1)
#            ax.legend(patch, label, loc=1, fontsize=18 )
#            ax.tick_params(labelsize=24)
#            ax.xlim([chn_np[0], chn_np[-1] ])
#            ax.ylim([0,2000])
#            ax.ylabel(ylabel, fontsize=18 )
#            ax.xlabel("APA %s Channel No."%wiretype, fontsize=18 )
#            ax.title(title , fontsize=18 )
#            ax.grid()
#            ax.tight_layout( rect=[0, 0.05, 1, 0.95])
#            ax.savefig(pp, format='pdf')
#            ax.close()
   
    if ( (plot_en&0x20) != 0 ):
    #stuck code ratio pedestal        
        fig = plt.figure(figsize=(16,9))
        ax = plt
    
        sf_ratio_np = np.array(sf_ratio_np)
        patch = []
        label = []
        title = "%s plane: Ratio between SF Samples and All Samples(%d)" %(wiretype, smp_length )
        ylabel = "Ratio"
        print "Ratio between SF Samples and All Samples "

        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            if len(ped_np)!= 0:
                color = 'b'
                plabel = "Ratio"
                y_np = sf_ratio_np
                ax.scatter( chn_np, y_np, color = color)
                ax.plot( chn_np, y_np, color = color)

                if (fembloc < 10 ):
                    ax.text (chn_np[0], 0.05, "B" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                else:
                    ax.text (chn_np[0], 0.05, "A" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )

                ax.text (chn_np[0], 0.40, "Alive", color = 'g' )
                ax.text (chn_np[0], 0.35, "WIB%d"%(chnwib_np[0]+1 ), color = 'g'  )
                ax.text (chn_np[0], 0.30, "FEMB%d"%(chnfemb_np[0]), color = 'g'  )
            else:
                ax.text (chn_np[0], 0.40, "Dead", color = 'r' )

        patch.append( mpatches.Patch(color=color))
        label.append(plabel)
        ax.legend(patch, label, loc=1, fontsize=18 )
        ax.tick_params(labelsize=24)
        ax.xlim([0,total_chn])
        ax.ylim([0,1])

        ax.text( (total_chn/20.0),0.20, "Test started at  : " + loginfo[6] )
        if (len(loginfo[7]) > 5 ):
            ax.text( (total_chn/40.0),300, "Inactive FEMBs : " + loginfo[7] )
 
        ax.ylabel(ylabel, fontsize=18 )
        ax.xlabel("APA %s Channel No."%wiretype, fontsize=18 )
        ax.title(title , fontsize=18 )
        ax.grid()
        ax.tight_layout( rect=[0, 0.05, 1, 0.95])
        ax.savefig(pp, format='pdf')
        ax.close()

    if ( (plot_en&0x40) != 0 ):
    #plot pedestal        
        fig = plt.figure(figsize=(16,9))
        ax = plt
        ped_np = np.array(ped_np)
        chn_peakp_ped = np.array( chn_peakp_ped )
        patch = []
        label = []
        title = "%s plane: Pedestal Measurement Mod(64)" % wiretype
        ylabel = "ADC output /bin"
        print "Pedestal Measurement-->%s wires has %d channels in total"%(wiretype, total_chn)

        for fembloc in range(20):
            ped_np         = fembinfo[fembloc][1]
            rms_np         = fembinfo[fembloc][2]
            sf_ped_np      = fembinfo[fembloc][3]
            sf_rms_np      = fembinfo[fembloc][4]
            sf_ratio_np    = fembinfo[fembloc][5]
            chn_peakp_avg  = fembinfo[fembloc][6]
            chn_peakn_avg  = fembinfo[fembloc][7]
            chn_wave       = fembinfo[fembloc][8]
            chn_peakp_ped  = fembinfo[fembloc][9]
            chn_peakn_ped  = fembinfo[fembloc][10]
            chnwib_np      = fembinfo[fembloc][11]
            chnfemb_np     = fembinfo[fembloc][12]
            chnasic_np     = fembinfo[fembloc][13]
            chnchn_np      = fembinfo[fembloc][14]

            chn_np = range(chnsum * fembloc, chnsum * (fembloc+1),1)
            if len(ped_np)!= 0:
                ped_label = "(Pedestal Mod(64)) / ADC bin"
                y_np = ped_np%64
                ax.scatter( chn_np, y_np)
                ax.plot( chn_np, y_np)

                if (fembloc < 10 ):
                    ax.text (chn_np[0], 5, "B" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )
                else:
                    ax.text (chn_np[0], 5, "A" + format(APAno, "1d") + format(fembloc+1, "02d"), color = 'b' )

                ax.text (chn_np[0], 60, "Alive", color = 'g' )
                ax.text (chn_np[0], 55, "WIB%d"%(chnwib_np[0]+1 ), color = 'g'  )
                ax.text (chn_np[0], 50, "FEMB%d"%(chnfemb_np[0]), color = 'g'  )
            else:
                ax.text (chn_np[0], 60, "Dead", color = 'r' )
#                ax.text (chn_np[0], 0.35, "WIB%d"%(chnwib_np[0] ), color = 'r'  )
#                ax.text (chn_np[0], 0.30, "FEMB%d"%(chnfemb_np[0]), color = 'r'  )

#        patch.append( mpatches.Patch(color=color))
#        label.append(ped_label)
#        ax.legend(patch, label, loc=1, fontsize=18 )
        ax.tick_params(labelsize=24)
        ax.xlim([0,total_chn])
        ax.ylim([0,64])
        if ( run_temp != None ):
            ax.text( (total_chn/20.0),60, "RTDs(TT0206 to TT0200) measured at %s: %3dK, %3dK, %3dK, %3dK, %3dK, %3dK, %3dK "%(run_temp[8],\
                    run_temp[7],run_temp[6],run_temp[5],run_temp[4],run_temp[3],run_temp[2],run_temp[1] ) )
        else:
            ax.text( (total_chn/20.0),60, "Temperature : " + loginfo[3]  )
        ax.text( (total_chn/20.0),55, "Test started at  : " + loginfo[6] )
        if (len(loginfo[7]) > 5 ):
            ax.text( (total_chn/40.0),300, "Inactive FEMBs : " + loginfo[7] )
 
        ax.ylabel(ylabel, fontsize=18 )
        ax.xlabel("APA %s Channel No."%wiretype, fontsize=18 )
        ax.title(title , fontsize=18 )
        ax.grid()
        ax.tight_layout( rect=[0, 0.05, 1, 0.95])
        ax.savefig(pp, format='pdf')
        ax.close()

#read index file
start = timer()
gain = int(sys.argv[1])
tp = int(sys.argv[2])
max_limit = 3000
min_limit = 500
hp_filter  = False
plot_en = 0x7B


index_f = "./tests_index.csv"
tindexs = []
with open(index_f, 'r') as fp:
    for cl in fp:
        tindexs.append ( cl.split(","))

tindexs = tindexs[1:]
tmp = []
for i in tindexs:
    it = []
    for j in i:
        it.append(j.replace(" ", ""))
    tmp.append(it)
tindexs = tmp

for tn in tindexs:
    if (tn[0][0] == "#"): #valid test
        print tn
        t_no =int( tn[0][1:])
        strdate = tn[1] + "_2018" 
        apas_chk = [ format( int(tn[13].split("-")[0]), "02d") ,
                     format( int(tn[14].split("-")[0]), "02d") , 
                     format( int(tn[15].split("-")[0]), "02d") , 
                     format( int(tn[16].split("-")[0]), "02d") , 
                     format( int(tn[17].split("-")[0]), "02d") , 
                     format( int(tn[18].split("-")[0]), "02d") , 
                     ]
        for i in range(len(apas_chk)):
            APAno = i + 1
            if (int(apas_chk[i]) == 0 ):
                print tn
                print "Test#%d for APA#%d doesn't exist"%(t_no, APAno)
                continue
            else:
                strrunno = apas_chk[i]
                env = "LAr"
                server_flg = tn[19]

                print "Start run%schk"%strrunno
                rundir = "run%schk"%strrunno
                if (server_flg.find("rs" )>=0):
                    rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/" + "APA" + format(APAno, '1d') + "/"
                elif (server_flg.find("sw" )>=0):
                    rootpath = "/nfs/sw/shanshan/Rawdata/" + "APA" + format(APAno, '1d') + "/"
                else:
                    rootpath = "/Users/shanshangao/Documents/Share_Windows/CERN_test_stand/Rawdata/APA3/"
                path =rootpath + "Rawdata_"+ strdate + "/" 
                
                apamap.APA = "ProtoDUNE"
                loginfo = readlog(rootpath=rootpath, APAno=APAno, runtime = strdate, runno = strrunno, runtype = "chk") 
                run_temp = None
                
                save_cycle = 0
                result_dir = path + "results/" 
                if (os.path.exists(result_dir)):
                    pass
                else:
                    try: 
                        os.makedirs(result_dir)
                    except OSError:
                        print "Error to create a folder"
                        exit()
                
                result_pdf = result_dir + "Test" + format(t_no, "03d") + "X" + format(plot_en, "02X") + rundir +  "_" + apamap.APA + "_APA" + str(APAno) + '_gain' + str(gain) +  "tp" + str(tp) + "_results" + '.pdf'
                result_waveform = result_dir + "X" + format(plot_en, "02X") + rundir +  "_" + apamap.APA + "_APA" + str(APAno) + '_gain' + str(gain) +  "tp" + str(tp) + "_results"+ '.png'
                
                pp = PdfPages(result_pdf)
                mode = 0
                wib_np = [0,1,2,3,4]
                jumbo_flag = False
                feed_freq=500
                wibsdata = All_FEMBs_results(path, rundir, apamap.APA, APAno, gain=gain, mode=mode, wib_np = wib_np, tp=tp, jumbo_flag = jumbo_flag, feed_freq = 500, hp_filter=hp_filter, t_no = t_no)
                fig = plt.figure(figsize=(16,9))
                APA_sort_all, APA_X_sort, APA_V_sort, APA_U_sort = APA_sort(APAno)
                plots(plt, plot_en, wibsdata, loginfo, run_temp,  APA_sort_all,   pp, gain, max_limit, min_limit, frontpage = True , APAno = APAno, r_wfm = result_waveform)
                pp.close()
                
print "Done, please punch \" Enter \" or \"return\" key !"
