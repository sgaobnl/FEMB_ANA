# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Mon Jan 22 22:54:26 2018
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
import numpy as np
import os
#from sys import exit
import os.path
import math
import statsmodels.api as sm
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
#from matplotlib.ticker import FuncFormatter
from paras_tp_allchn_pre_coh import paras_tp_allchn_pre_coh
from enc_allchn_pre_coh import enc_allchn_pre_coh
from enc_allchn_pre_coh import sf_enc_allchn_pre_coh 

def plot_color (tp):
    if tp == 0.5:
        clor = 'g'
    if tp == 1.0: 
        clor = 'b'
    if tp == 2.0:
        clor = 'r'
    if tp == 3.0:
        clor = 'm'
    return clor

def allpedplot(ax, all_chn_results, coh_chn_np, tp_np, paras=5, wire_type="All", yrange =[000,4095], ylabel = "ADC output /bin", title = "Pedestal Measurement" ):
    paras_tp_chn = paras_tp_allchn_pre_coh(all_chn_results, coh_chn_np, paras=paras, wire_type=wire_type)
    patch = []
    label = []
    total_chn = len(paras_tp_chn[0])
    print "Pedestal Measurement-->%s wires has %d channels in total"%(wire_type, total_chn)
    for i in range(4):
        total_chn = len(paras_tp_chn[i])
        clor = plot_color(tp_np[i])
        chn_np = np.arange(total_chn)
        ax.scatter( chn_np, paras_tp_chn[i], color = clor)
        ax.plot( chn_np, paras_tp_chn[i], color = clor)
        patch.append( mpatches.Patch(color=clor))
        label.append("%s wire,%.1f$\mu$s"%(wire_type, tp_np[i]))
    ax.legend(patch, label, loc=1, fontsize=12 )
    #ax.tick_params(labelsize="small")
    ax.tick_params(labelsize=8)
    ax.set_xlim([0,total_chn])
    ax.set_ylim(yrange)
    ax.set_ylabel(ylabel, fontsize=12 )
    ax.set_xlabel("FE Channel no.", fontsize=12 )
    ax.set_title(title , fontsize=12 )
    ax.grid()

def allgainplot(ax, all_chn_results,coh_chn_np,  tp_np, paras=9, wire_type="All", yrange =[000,500], ylabel = "Electrons / e-", title = "Gain Measurement" ):
    paras_tp_chn = paras_tp_allchn_pre_coh(all_chn_results, coh_chn_np, paras=paras, wire_type=wire_type)
    patch = []
    label = []
    total_chn = len(paras_tp_chn[0])
    print "Gain Measurement-->%s wires has %d channels in total"%(wire_type, total_chn)
    for i in range(4):
        clor = plot_color(tp_np[i])
        chn_np = np.arange(total_chn)
        ax.scatter( chn_np, paras_tp_chn[i], color = clor)
        ax.plot( chn_np, paras_tp_chn[i], color = clor)
        patch.append( mpatches.Patch(color=clor))
        label.append("%s wire,%.1f$\mu$s,mean=%d e-/bin, std=%d"%(wire_type, tp_np[i], int(np.mean(paras_tp_chn[i])), int(np.std(paras_tp_chn[i])) ))
    ax.legend(patch, label, loc=1, fontsize=12 )
    #ax.tick_params(labelsize="small")
    ax.tick_params(labelsize=8)
    ax.set_xlim([0,total_chn])
    ax.set_ylim(yrange)
    ax.set_ylabel(ylabel, fontsize=12 )
    ax.set_xlabel("FE Channel no.", fontsize=12 )
    ax.set_title(title, fontsize=12  )
    ax.grid()

def allencplot(ax, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="All",  yrange =[000,3000], ylabel = "Electrons / e-", title = "ENC Measurement" ):
    rms_tp_chn = paras_tp_allchn_pre_coh(all_chn_results, coh_chn_np, paras=6, wire_type=wire_type )
    gain_tp_chn = paras_tp_allchn_pre_coh(all_chn_results, coh_chn_np, paras=9, wire_type=wire_type )
    total_chn = len(rms_tp_chn[0])
    print "ENC Measurement --> %s wires has %d channels in total"%(wire_type, total_chn)
    rms_tp_chn = np.resize(rms_tp_chn,[4,total_chn])
    gain_tp_chn = np.resize(gain_tp_chn,[4,total_chn])
    paras_tp_chn = np.array(rms_tp_chn) * np.array(gain_tp_chn)
    patch = []
    label = []
    enc_tp = []
    for i in range(4):
        clor = plot_color(tp_np[i])
        chn_np = np.arange(total_chn)
        ax.scatter( chn_np, paras_tp_chn[i], color = clor)
        ax.plot( chn_np, paras_tp_chn[i], color = clor)
        patch.append( mpatches.Patch(color=clor))
        label.append("%s wires=%d, %.1f$\mu$s,mean=%d e-/bin, std=%d"%(wire_type, total_chn, tp_np[i], int(np.mean(paras_tp_chn[i])), int(np.std(paras_tp_chn[i])) ))
        enc_tp.append( [wire_type, tp_np[i], int(np.mean(paras_tp_chn[i])), int(np.std(paras_tp_chn[i]))] )
    ax.legend(patch, label, loc=1, fontsize=12 )
    #ax.tick_params(labelsize="small")
    ax.tick_params(labelsize=8)
    ax.set_ylim(yrange)
    ax.set_xlim([0,total_chn])
    ax.set_ylabel(ylabel, fontsize=12 )
    #ax.set_xlabel("FE Channel no.", fontsize=12 )
    ax.set_xlabel("Channels of %s wire"%wire_type, fontsize=12 )
    ax.set_title(title , fontsize=12 )
    ax.grid()
    return enc_tp

def allencplot_stuckfree(ax, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="All",  yrange =[000,3000],ylabel = "Electrons / e-", title = "ENC Measurement" ):
    sf_enc_tp = []
    patch = []
    label = []
    for tp_no in [0,1,2,3]:
        clor = plot_color(tp_np[tp_no])

        #chn_enc_np = enc_allchn_pre_coh(all_chn_results, coh_chn_np, tp_no, wire_type=wire_type )
        #chn_np = []
        #enc_np = []
        #for onechn_enc in chn_enc_np:
        #    chn_np.append(onechn_enc[0])
        #    enc_np.append(onechn_enc[1])
        #ax.scatter( chn_np, enc_np, color = clor)

        sf_chn_enc_np = sf_enc_allchn_pre_coh(all_chn_results, coh_chn_np, tp_no, wire_type=wire_type )
        sf_chn_np = []
        sf_enc_np = []
        for sf_onechn_enc in sf_chn_enc_np:
            sf_chn_np.append(sf_onechn_enc[0])
            sf_enc_np.append(sf_onechn_enc[1])
        ax.plot( sf_chn_np, sf_enc_np, color = clor)
        ax.scatter( sf_chn_np, sf_enc_np, color = clor)

        total_chn = len(sf_chn_enc_np)
        print "ENC Measurement --> %s wires has %d channels in total"%(wire_type, total_chn)

        #paras_chn = np.array(rms_chn) * np.array(gain_chn)
        #chn_sf
        sf_mean = np.mean(sf_enc_np)
        sf_std  = np.std(sf_enc_np)
        if (math.isnan(sf_mean) ):
            sf_mean = 0 
        else:
            sf_mean = int(sf_mean)
        if (math.isnan(sf_std) ):
            sf_std = 0 
        else:
            sf_std = int(sf_std)

        patch.append( mpatches.Patch(color=clor))
        label.append("%s wires, SFchn = %d, %.1f$\mu$s, mean=%d e-/bin, std=%d"%(wire_type,total_chn, tp_np[tp_no], sf_mean, sf_std ))
        sf_enc_tp.append( [wire_type, tp_np[tp_no], sf_mean, sf_std] )
    ax.legend(patch, label, loc=1, fontsize=12 )
    #ax.tick_params(labelsize="small")
    ax.tick_params(labelsize=8)
    ax.set_ylim(yrange)
    ax.set_xlim([0,128])
    ax.set_ylabel(ylabel, fontsize=12 )
    #ax.set_xlabel("FE Channel no.", fontsize=12 )
    ax.set_xlabel("Stuck Free Channels of %s wire"%wire_type, fontsize=12 )
    ax.set_title(title , fontsize=12 )
    ax.grid()
    return sf_enc_tp

def all_tp_enc_plot(ax, enc_tp,yrange=[0,3000]):
    print "ENC comparision"
    clor = ['m','g', 'b', 'r']
    mker = ['o','*','^','x','d','+','s','8',"1","2"]
    patch = []
    label = []
    wire_type_np = ["All", "Y", "U", "V"]
    for wire_code in range(4):
        wire_type = wire_type_np[wire_code]
        if (enc_tp[0][0] == wire_type):
            tp_np = []
            encmean = []
            encstd = []
            for i in range(4):
                tp_np.append(enc_tp[i][1])
                encmean.append(enc_tp[i][2] )
                encstd.append(enc_tp[i][3] )
            ax.errorbar(tp_np, encmean, encstd, color = clor[wire_code], marker = mker[wire_code])
            ax.text(0.1*(1),2800-wire_code*150 , "%s:" % (wire_type),                            color = clor[wire_code],fontsize=12)
            ax.text(0.5*(1)-0.1,2800-wire_code*150 , "%d +/- %d" % (int(encmean[0]), int(encstd[0])),color = clor[wire_code],fontsize=12)
            ax.text(0.5*(2)+0.2,2800-wire_code*150 , "%d +/- %d" % (int(encmean[1]), int(encstd[1])),color = clor[wire_code],fontsize=12)
            ax.text(0.5*(4),2800-wire_code*150 , "%d +/- %d" % (int(encmean[2]), int(encstd[2])),color = clor[wire_code],fontsize=12)
            ax.text(0.5*(6),2800-wire_code*150 , "%d +/- %d" % (int(encmean[3]), int(encstd[3])),color = clor[wire_code],fontsize=12)
            patch.append( mpatches.Patch(color = clor[wire_code]))
            label.append("%s wires"%(wire_type ))
#    ax.legend(patch, label, loc=1, fontsize=12 )
    ax.tick_params(labelsize=8)
    ax.set_ylim(yrange)
    ax.set_xlim([0,4])
    ax.set_ylabel("ENC /e-", fontsize=12)
    ax.set_xlabel("Peaking time / ($\mu$s)", fontsize=12)
    ax.set_title("ENC", fontsize=12 )
    ax.grid()

def allfft_05_plot(ax, all_chn_results, coh_chn_np, tp_np, wire_type="All", psd=True, SF = True ):
    f_tp_chn = paras_tp_allchn_pre_coh(all_chn_results, coh_chn_np, paras=3, wire_type=wire_type)
    p_tp_chn = paras_tp_allchn_pre_coh(all_chn_results, coh_chn_np, paras=4, wire_type=wire_type)
    s_tp_chn = paras_tp_allchn_pre_coh(all_chn_results, coh_chn_np, paras=11, wire_type=wire_type)

    total_chn = len(f_tp_chn[0])
    print "FFT-->%s wires has %d channels in total"%(wire_type, total_chn)

    clor = ['m','g', 'b', 'r']
    mker = ['o','*','^','x','d','+','s','8',"1","2"]
    wire_type_np = ["All", "Y", "U", "V"]
    if (wire_type == "All"):
        clor_n = 0
    if (wire_type == "Y"):
        clor_n = 1
    if (wire_type == "U"):
        clor_n = 2
    if (wire_type == "V"):
        clor_n = 3

    for tp in range(1): #0.5us
        SF_chn = 0
        for chn in range(total_chn):
            f = f_tp_chn[tp][chn]
            p = p_tp_chn[tp][chn]
            if ( SF == False ):
                ax.plot(f,p,color=clor[clor_n])
            else:
                if ( s_tp_chn[tp][chn] == "Small"):
                    SF_chn = SF_chn + 1
                    ax.plot(f,p,color=clor[clor_n])
    ax.tick_params(labelsize=8)
    if (SF == True ):
        ax.set_title( "Overlap FFT spectrum plots of  %d %s wires (Tp = 0.5us)"%(SF_chn, wire_type), fontsize=12)
    else:
        ax.set_title( "Overlap FFT spectrum plots of  %d %s wires (Tp = 0.5us)"%(total_chn, wire_type), fontsize=12)
    ax.set_xlim([0,1e6])
    ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0), fontsize=12)
    ax.set_xlabel("Frequency /Hz", fontsize=12)
    if (psd == True):
        ax.set_ylabel("Power Spectral Desity /dB", fontsize=12)
        ax.set_ylim([-80,20])
    else:
        ax.set_ylabel("Amplitude /dB", fontsize=12)
        ax.set_ylim([-40,20])
    ax.grid()


def all_chn_plot_pre_coh (save_encfile, all_chn_results, coh_chn_np,  pp, step,env="RT", femb = 0, psd = True, gain =3):
#################################################
    print "all chn plot --> 1"
    fig0 = plt.figure(figsize=(18,12))
    ax0_0 = plt.subplot2grid((2, 2), (0, 0))
    ax0_1 = plt.subplot2grid((2, 2), (0, 1))
    ax0_2 = plt.subplot2grid((2, 2), (1, 0))
    ax0_3 = plt.subplot2grid((2, 2), (1, 1))
    tp_np = [0.5,1,2,3]
    allpedplot(ax0_0, all_chn_results, coh_chn_np, tp_np, paras=5, wire_type="All", yrange =[000,4100], ylabel = "ADC output /bin", title = "Pedestal Measurement" )
    #allpedplot(ax0_1, all_chn_results, coh_chn_np, tp_np, paras=5, wire_type="Y",   yrange =[000,4100], ylabel = "ADC output /bin", title = "Pedestal Measurement" )
    #allpedplot(ax0_2, all_chn_results, coh_chn_np, tp_np, paras=5, wire_type="U",   yrange =[000,4100], ylabel = "ADC output /bin", title = "Pedestal Measurement" )
    #allpedplot(ax0_3, all_chn_results, coh_chn_np, tp_np, paras=5, wire_type="V",   yrange =[000,4100], ylabel = "ADC output /bin", title = "Pedestal Measurement" )

    fig0.suptitle("%s: FEMB%d, Pedestal Measurement"%(step, femb), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
#    plt.savefig(pp, format='pdf')
    plt.close()

#################################################
    print "all chn plot --> 2"
    fig1 = plt.figure(figsize=(18,12))
    ax1_0 = plt.subplot2grid((2, 2), (0, 0))
    ax1_1 = plt.subplot2grid((2, 2), (0, 1))
    ax1_2 = plt.subplot2grid((2, 2), (1, 0))
    ax1_3 = plt.subplot2grid((2, 2), (1, 1))
    tp_np = [0.5,1,2,3]
    allgainplot(ax1_0, all_chn_results, coh_chn_np, tp_np, paras=9, wire_type="All", yrange =[000,500], ylabel = "Gain / (e-/bin)", title = "Gain Measurement" )
    #allgainplot(ax1_1, all_chn_results, coh_chn_np, tp_np, paras=9, wire_type="Y",   yrange =[000,500], ylabel = "Gain / (e-/bin)", title = "Gain Measurement" )
    #allgainplot(ax1_2, all_chn_results, coh_chn_np, tp_np, paras=9, wire_type="U",   yrange =[000,500], ylabel = "Gain / (e-/bin)", title = "Gain Measurement" )
    #allgainplot(ax1_3, all_chn_results, coh_chn_np, tp_np, paras=9, wire_type="V",   yrange =[000,500], ylabel = "Gain / (e-/bin)", title = "Gain Measurement" )
    fig1.suptitle("%s: FEMB%d, Gain Measurement"%(step, femb), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
#    plt.savefig(pp, format='pdf')
    plt.close()

#################################################
    print "all chn plot --> 3"
    fig2 = plt.figure(figsize=(18,12))
    ax2_0 = plt.subplot2grid((2, 2), (0, 0))
    ax2_1 = plt.subplot2grid((2, 2), (0, 1))
    ax2_2 = plt.subplot2grid((2, 2), (1, 0))
    ax2_3 = plt.subplot2grid((2, 2), (1, 1))
    tp_np = [0.5,1,2,3]
    enc_np_All = allencplot(ax2_0, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="All",  yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    #enc_np_Y   = allencplot(ax2_1, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="Y",  yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    #enc_np_U   = allencplot(ax2_2, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="U",  yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    #enc_np_V   = allencplot(ax2_3, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="V",  yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    fig2.suptitle("%s: FEMB%d, ENC Measurement"%(step, femb), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
#    plt.savefig(pp, format='pdf')
    plt.close()

#################################################
    print "all chn plot --> 4"
    fig3 = plt.figure(figsize=(18,12))
    ax3_0 = plt.subplot2grid((2, 2), (0, 0))
    ax3_1 = plt.subplot2grid((2, 2), (0, 1))
    ax3_2 = plt.subplot2grid((2, 2), (1, 0))
    ax3_3 = plt.subplot2grid((2, 2), (1, 1))
    tp_np = [0.5,1,2,3]

    all_tp_enc_plot(ax3_0, enc_np_All, yrange =[000,3000])
#    all_tp_enc_plot(ax3_0, enc_np_Y  , yrange =[000,3000])
#    all_tp_enc_plot(ax3_0, enc_np_U  , yrange =[000,3000])
#    all_tp_enc_plot(ax3_0, enc_np_V  , yrange =[000,3000])
    allfft_05_plot(ax3_1, all_chn_results, coh_chn_np, tp_np, wire_type="All", psd=True, SF = False )
#    allfft_05_plot(ax3_1, all_chn_results, coh_chn_np, tp_np, wire_type="Y", psd=True, SF = False )
#    allfft_05_plot(ax3_2, all_chn_results, coh_chn_np, tp_np, wire_type="U", psd=True, SF = False )
#    allfft_05_plot(ax3_3, all_chn_results, coh_chn_np, tp_np, wire_type="V", psd=True, SF = False )

    fig3.suptitle("%s: FEMB%d, ENC Measurement & FFT"%(step, femb), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
#    plt.savefig(pp, format='pdf')
    plt.close()

    print "all chn plot --> 5"
    fig2_2 = plt.figure(figsize=(18,12))
    ax2_2_0 = plt.subplot2grid((2, 2), (0, 0))
    ax2_2_1 = plt.subplot2grid((2, 2), (0, 1))
    ax2_2_2 = plt.subplot2grid((2, 2), (1, 0))
    ax2_2_3 = plt.subplot2grid((2, 2), (1, 1))
    tp_np = [0.5,1,2,3]
    enc_np_All = allencplot_stuckfree(ax2_2_0, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="All", yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    #enc_np_Y   = allencplot_stuckfree(ax2_2_1, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="Y", yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    #enc_np_U   = allencplot_stuckfree(ax2_2_2, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="U", yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    #enc_np_V   = allencplot_stuckfree(ax2_2_3, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="V", yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement" )
    fig2_2.suptitle("%s: FEMB%d, ENC Measurement"%(step, femb), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
#    plt.savefig(pp, format='pdf')
    plt.close()

#################################################
    print "all chn plot --> 6"
    fig3_2 = plt.figure(figsize=(18,12))
    ax3_2_0 = plt.subplot2grid((2, 2), (0, 0))
    ax3_2_1 = plt.subplot2grid((2, 2), (0, 1))
    ax3_2_2 = plt.subplot2grid((2, 2), (1, 0))
    ax3_2_3 = plt.subplot2grid((2, 2), (1, 1))
    tp_np = [0.5,1,2,3]

    all_tp_enc_plot(ax3_2_0, enc_np_All, yrange =[000,3000])
#    all_tp_enc_plot(ax3_2_0, enc_np_Y  , yrange =[000,3000])
#    all_tp_enc_plot(ax3_2_0, enc_np_U  , yrange =[000,3000])
#    all_tp_enc_plot(ax3_2_0, enc_np_V  , yrange =[000,3000])
    allfft_05_plot(ax3_2_1, all_chn_results, coh_chn_np, tp_np, wire_type="All", psd=True, SF = True )
    #allfft_05_plot(ax3_2_1, all_chn_results, coh_chn_np, tp_np, wire_type="Y", psd=True, SF = True )
    #allfft_05_plot(ax3_2_2, all_chn_results, coh_chn_np, tp_np, wire_type="U", psd=True, SF = True )
    #allfft_05_plot(ax3_2_3, all_chn_results, coh_chn_np, tp_np, wire_type="V", psd=True, SF = True )

    fig3_2.suptitle("%s: Stuck Free, FEMB%d, ENC Measurement & FFT"%(step, femb), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
#    plt.savefig(pp, format='pdf')
    plt.close()

    print "all chn plot --> 7"
    fig7 = plt.figure(figsize=(18,12))
    ax7_0 = plt.subplot2grid((2, 2), (0, 0))
    ax7_1 = plt.subplot2grid((2, 2), (0, 1))
    ax7_2 = plt.subplot2grid((2, 2), (1, 0))
    ax7_3 = plt.subplot2grid((2, 2), (1, 1))
    tp_np = [0.5,1,2,3]
    allpedplot(ax7_0, all_chn_results, coh_chn_np, tp_np, paras=5, wire_type="All", yrange =[000,4100], ylabel = "ADC output /bin", title = "Pedestal Measurement" )
    tp_np = [0.5,1,2,3]
    allgainplot(ax7_1, all_chn_results, coh_chn_np, tp_np, paras=9, wire_type="All", yrange =[000,500], ylabel = "Gain / (e-/bin)", title = "Gain Measurement" )
    tp_np = [0.5,1,2,3]
    #enc_np_All =          allencplot(ax7_2, all_chn_results, tp_np, paras=6, wire_type="All", yrange =[000,3000], ylabel = "ENC / e-", title = "Noise Measurement (ENC) " )
    enc_np_All = allencplot_stuckfree(ax7_2, all_chn_results, coh_chn_np, tp_np, paras=6, wire_type="All", yrange =[000,3000], ylabel = "ENC /e-", title = "ENC Measurement (Stuck Code Free)" )

    import pickle
    with open(save_encfile, 'wb') as fp:
        pickle.dump(enc_np_All, fp)

    tp_np = [0.5,1,2,3]
    all_tp_enc_plot(ax7_3, enc_np_All  , yrange =[000,3000])


#    all_tp_enc_plot(ax7_3, enc_np_Y  , yrange =[000,3000])
#    all_tp_enc_plot(ax7_3, enc_np_U  , yrange =[000,3000])
#    all_tp_enc_plot(ax7_3, enc_np_V  , yrange =[000,3000])
    fig7.suptitle("Pre coherent noise filter, %s: FEMB%d, Pedestal, Gain, ENC"%(step, femb), fontsize = 20)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    plt.savefig(pp, format='pdf')
    plt.close()

