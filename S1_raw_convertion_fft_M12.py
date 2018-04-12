# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sat Dec  2 18:43:21 2017
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
import numpy as np
import struct
import os
from sys import exit
import os.path
import math
#import statsmodels.api as sm
from raw_convertor_m import raw_convertor 
#from raw_to_result_fft_M12 import raw_to_result
from fft_chn import chn_rfft
from fft_chn import chn_rfft_psd
from fft_chn import chn_fft
from fft_chn import chn_fft_psd
import pickle

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

from scipy import signal
from apa_mapping import apa_mapping


from scipy import signal
#def highpass_filter(pre_flt_data, fs = 2000000, flt_stopfreq = 500, flt_passfreq = 600, flt_order = 1001):
#  # High-pass filter
#  nyquist_rate = fs / 2.0
#  desired = (0, 0, 1, 1)
#  bands = (0, flt_stopfreq, flt_passfreq, nyquist_rate)
#  flt_coefs = signal.firls(flt_order, bands, desired, nyq=nyquist_rate)
#  # Apply high-pass filter
#  post_flt_data = signal.filtfilt(flt_coefs, [1], pre_flt_data)
#  return flt_coefs, post_flt_data
#def highpass_filter(pre_flt_data, fs = 2000000, flt_stopfreq = 500, flt_passfreq = 600, flt_order = 1001):
#  # bandstop filter
#  nyquist_rate = fs / 2.0
#  wn = [flt_stopfreq/nyquist_rate, flt_passfreq/nyquist_rate]
#  a,b = signal.butter(2, wn, 'bandstop')
#  # Apply high-pass filter
#  post_flt_data = signal.filtfilt(a, b, pre_flt_data)
#  return post_flt_data, a, b

def highpass_filter(fs = 2000000, flt_stopfreq = 300, flt_passfreq = 600, flt_order = 1):
  # High-pass filter
  nyquist_rate = fs / 2.0
  desired = (0, 0, 1, 1)
  bands = (0, flt_stopfreq, flt_passfreq, nyquist_rate)
  flt_coefs = signal.firls(flt_order, bands, desired, nyq=nyquist_rate)
  freq, response = signal.freqz(flt_coefs)
  #print flt_coefs[300:700]
  return freq, response
  # Apply high-pass filter
#  post_flt_data = signal.filtfilt(flt_coefs, [1], pre_flt_data)
#  return flt_coefs, post_flt_data

def butter_hp_flt(fs = 2000000, passfreq = 500, flt_order = 3):
  # bandstop filter
  nyquist_rate = fs / 2.0
  wn = passfreq/nyquist_rate
  b, a = signal.butter(N=flt_order, Wn=wn, btype='highpass')
  return b, a

def butter_bandstop_flt(fs = 2000000, stopfreq = 300, passfreq = 600, flt_order = 2):
  # bandstop filter
  nyquist_rate = fs / 2.0
  wn = [stopfreq/nyquist_rate, passfreq/nyquist_rate]
  b, a = signal.butter(N=flt_order, Wn=wn, btype='bandstop')
  return b, a

def fft_process_chn(path, onedir = "step1", env = "RT", runno = "run01" , FEMB = "FEMB0", chns = [0], jumbo_flag = False, FEset = "_1E_", one_chn_flg = False):
    rms_data_dir = path + "/" + runno + "/" + onedir + "/" 
    for root, dirs, files in os.walk(rms_data_dir):
        break
    psum = None
    chip_np = []
    for chni in chns:
        chiptmp = chni // 16
        if ( len(np.where(np.array(chip_np) == chiptmp)[0]) == 0 ):
            chip_np.append(chiptmp)

    fs = 2000000.0
    for chip in chip_np:
        for onefile in files:
            pos1 = onefile.find(FEMB)
            pos2 = onefile.find("_RMS")
            pos3 = onefile.find(FEset)
            if (pos1 >= 0 ) and (pos2 >= 0) and (pos3 >= 0):
                chip_num = int(onefile[onefile.find("CHIP")+4])
                if  (chip_num ==chip):
                    rms_data_file = rms_data_dir + onefile
                    fileinfo  = os.stat(rms_data_file)
                    filelength = fileinfo.st_size
                    print rms_data_file
                    with open(rms_data_file, 'rb') as f:
                        raw_data = f.read()
                    smps = (filelength-1024)/2/16 

                    femb_num = int(onefile[onefile.find("FEMB")+4])
                    chip_num = int(onefile[onefile.find("CHIP")+4])
                    tp = int(onefile[onefile.find("CHIP")+6])
                    chn_data = raw_convertor(raw_data, smps, jumbo_flag)
                    chipchn0 = chip * 16
                    for chni in range(16):
                        curchn = chipchn0 + chni
                        if ( len(np.where( np.array(chns) == curchn )[0] ) == 1 ):
                            print "curchn%d"%curchn
                            savefile = rms_data_dir + "FFT_chn_%X"%chni + onefile[0: pos3] + "_FFT" +  onefile[pos3+4:] 
                            onechndata = chn_data[chni]
                            fft_s = 400000
                            smp_data = onechndata
                            cycle = int(len(smp_data) / fft_s )
                            psd = True
                            if (psd == True):
                                f,p = chn_fft_psd(smp_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
                            else:
                                f,p = chn_fft(smp_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 

                            if (type(psum) == type(None)):
                                f,p = chn_fft_psd(smp_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
                                psum = np.array(p)
                            else:
                                psum =psum +  np.array(p)
                            onefilepng = onefile
                            break
    if (one_chn_flg == True):
        t_np = np.linspace (0, 100000*0.5, 100000/100)
        rawmean = np.mean(smp_data)
        rawrms  = np.std(smp_data)
        rms_info =[ np.array(smp_data[:100000:100])-rawmean, rawmean, rawrms,'r' ]

        hpassfreq = 500
        hflt_order =3
        b,a = butter_hp_flt(fs, hpassfreq, hflt_order)
        hw, hh = signal.freqz(b,a, worN= int(fs/2))
        hp_paras = [hpassfreq, hflt_order, hw, abs(hh)]
        hp_flt_data = signal.filtfilt(b,a, smp_data)
        hf,hp = chn_fft_psd(hp_flt_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
        hmean = np.mean(hp_flt_data)
        hrms  = np.std(hp_flt_data)
        h_info =[ np.array(hp_flt_data[:100000:100])-hmean, hmean, hrms, 'g' ]

        ppassfreq = 1000
        pflt_order =3
        b,a = butter_hp_flt(fs, ppassfreq, pflt_order)
        pw, ph = signal.freqz(b,a, worN= int(fs/2))
        pp_paras = [ppassfreq, pflt_order, pw, abs(ph)]
        ps_flt_data = signal.filtfilt(b,a, smp_data)
        pf,pp = chn_fft_psd(ps_flt_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
        pmean = np.mean(ps_flt_data)
        prms  = np.std(ps_flt_data)
        p_info =[ np.array(ps_flt_data[:100000:100])-pmean, pmean, prms, 'b' ]

#        pstopfreq = 10
#        ppassfreq = 1000
#        pflt_order = 1
#        b,a = butter_bandstop_flt(fs, pstopfreq, ppassfreq, pflt_order)
#        pw, ph = signal.freqz(b,a, worN= int(fs/2))
#        pp_paras = [pstopfreq, ppassfreq, pflt_order, pw, abs(ph)]
#        ps_flt_data = signal.filtfilt(b,a, smp_data)
#        pf,pp = chn_fft_psd(ps_flt_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
#        pmean = np.mean(ps_flt_data)
#        prms  = np.std(ps_flt_data)
#        p_info =[ np.array(ps_flt_data[:100000:100])-pmean, pmean, prms ]
#
        flt_info = [hp_paras, pp_paras]

        chnfft_process_plot(path, runno, onedir, onefilepng, curchn, f, p, hf, hp, pf, pp, rms_info, h_info, p_info, t_np, flt_info,  FEset, fs)
        return smp_data, f, p, hf, hp, pf, pp
    else:
        return f, psum
    
def fft_process_chn_wib(path, onedir = "step1", env = "RT", runno = "run01" , chns = [0], jumbo_flag = False):
    femb_np = [ "FEMB0", "FEMB1", "FEMB2", "FEMB3" ]
    #femb_np = [ "FEMB0" ]
    psum = None
    for FEMB in femb_np:
        f,p = fft_process_chn(path, onedir, env, runno, FEMB, chns, jumbo_flag)
        if (type(psum) == type(None)):
            psum = np.array(p)
        else:
            psum =psum +  np.array(p)
    return f, psum

def fft_process_chn_apa(path, onedir = "step1", env = "RT", runno = "run01" , chns = [0], jumbo_flag = False):
    wib_np = [ "WIB1", "WIB2", "WIB3", "WIB4" , "WIB5" ]
    #wib_np = [ "WIB1" ]
    psum = None
    for wib in wib_np:
        f,p = fft_process_chn_wib(path, wib+onedir, env, runno, chns, jumbo_flag)
        if (type(psum) == type(None)):
            psum = np.array(p)
        else:
            psum =psum +  np.array(p)
    return f, psum

def fft_process_plot(path, runno, f, psum):
    plot_data_dir = path + "/" + runno + "/" 
    plt.figure(figsize=(16,9))
    ax = plt.subplot2grid((1, 1), (0, 0))
    ax.plot(f,psum,color='b')
    ax.set_xlim([0,1000])
    ax.set_xlabel("Frequency /Hz")
    ax.grid()
    psd = True
    if (psd == True):
        ax.set_ylabel("Power Spectral Desity /dB")
    else:
        ax.set_ylabel("Amplitude /dB")
    ax.set_title( "FFT specturms")
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    plt.savefig( plot_data_dir + "SUMFFT_" + runno + ".png", format = "png" )
    plt.close()
    #plt.show()

def histogram_pedstals ( ax, chndata, chnmean, chnrms, color):
    ax.hist(chndata, normed=1, color=color)
    ped_mean = chnmean
    rms = chnrms
    ax.text(0, 0.08, "%.3f +/- %.3f" % (ped_mean, rms))
    ax.set_ylabel("Normalized counts")
    ax.set_xlabel("ADC output/ (bin)")
    ax.set_ylim([0, 0.1])
    ax.tick_params(labelsize="small")
    ax.set_title("Normalized Histogram")

def ax2_plots(ax2_array, chndata_np):
    for i in range(len(chndata_np)):
        histogram_pedstals (ax2_array[i], chndata_np[i][0], chndata_np[i][1],chndata_np[i][2],chndata_np[i][3])

def chnfft_process_plot(path, runno, onedir, onefile, curchn, f, p, hf, hp, pf, pp, rms_info, h_info, p_info, t_np,flt_info,  FEset = "_1E_", fs = 2000000.0):
    plot_data_dir = path + "/" + runno + "/" 
    plt.figure(figsize=(16,12))

    ax1 = plt.subplot2grid((4, 4), (0, 0), colspan=2, rowspan=2)
    ax2_1 = plt.subplot2grid((4, 4), (0, 2))
    ax2_2 = plt.subplot2grid((4, 4), (0, 3))
    ax2_3 = plt.subplot2grid((4, 4), (1, 2))
    ax2_4 = plt.subplot2grid((4, 4), (1, 3))
    ax2_array = [ax2_1, ax2_2, ax2_3, ax2_4]
    ax3 = plt.subplot2grid((4, 4), (2, 0), colspan=2, rowspan=2)
    ax4 = plt.subplot2grid((4, 4), (2, 2), colspan=2, rowspan=2)

#    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax1.plot(f,p,color='r', label = 'Raw FFT: RMS=%.3f'%rms_info[2] )
    ax1.plot(hf,hp,color='g', label = 'Highpass 1 FFT: RMS=%.3f'%h_info[2] )
    ax1.plot(pf,pp,color='b', label = 'Highpass 2 FFT: RMS=%.3f'%p_info[2])
    #ax1.plot(pf,pp,color='b', label = 'Bandstop FFT')

    hp_paras = flt_info[0] 
    #ax1.plot(hp_paras[2], 20*np.log10(hp_paras[3]), color='g', label = 'HighPass: >%dHz pass, order=%d'%(hp_paras[0],hp_paras[1]))
    ax1.plot( (fs*0.5/np.pi)*hp_paras[2], 20*np.log10(hp_paras[3]), color='g', label = 'HighPass Filter: >=%dHz pass'%hp_paras[0], linestyle='--')
    pp_paras = flt_info[1] 
    ax1.plot( (fs*0.5/np.pi)*pp_paras[2], 20*np.log10(pp_paras[3]), color='b', label = 'HighPass Filter: >=%dHz pass'%pp_paras[0], linestyle='--')
    #ax1.plot(pp_paras[3], 20*np.log10(pp_paras[4]), color='b', label = 'Bandstop: stop=%dHz, start=%dHz, order=%d'%(pp_paras[0],pp_paras[1],pp_paras[2]))
    #ax1.plot( (fs*0.5/np.pi)*pp_paras[3], 20*np.log10(pp_paras[4]), color='b', label = 'Bandstop Filter', linestyle='--')

    ax1.legend(loc='best')
    ax1.set_ylim([-80,40])
    ax1.text( 100, -75, "RawMean=%4.3f, FLT1_Mean = %4.3f, FTL2_Mean = %4.3f"%(rms_info[1],h_info[1],p_info[1]) )
    ax1.text( 100, -70,  "RawRMS=%4.3f, FLT1_RMS = %4.3f, FTL2_RMS = %4.3f"%(rms_info[2],h_info[2],p_info[2]) )
    ax1.set_xlim([0,1000])
    ax1.set_xlabel("Frequency /Hz")
    ax1.grid()
    psd = True
    if (psd == True):
        ax1.set_ylabel("Power Spectral Desity /dB")
    else:
        ax1.set_ylabel("Amplitude /dB")
    ax1.set_title( "FFT specturms")

    chndata_np = [rms_info, h_info, p_info]
    ax2_plots(ax2_array, chndata_np)
#    ax2.legend(loc='best')

    ax3.plot(t_np,rms_info[0],color='r', label = 'Raw FFT: RMS=%.3f'%rms_info[2]    )
    ax3.plot(t_np,h_info[0],color='g', label = 'Highpass 1 FFT: RMS=%.3f'%h_info[2] )
    ax3.plot(t_np,p_info[0],color='b', label = 'Highpass 2 FFT: RMS=%.3f'%p_info[2] )
    ax3.set_xlabel("Time / ms")
    ax3.set_ylabel("(Rawdata - Pedestal) / ADC bin")
    ax3.legend(loc='best')

    hp_paras = flt_info[0] 
    #ax1.plot(hp_paras[2], 20*np.log10(hp_paras[3]), color='g', label = 'HighPass: >%dHz pass, order=%d'%(hp_paras[0],hp_paras[1]))
    #ax4.plot( (fs*0.5/np.pi)*hp_paras[2], 20*np.log10(hp_paras[3]), color='g', label = 'HighPass Filter')
    ax4.plot( (fs*0.5/np.pi)*hp_paras[2], 20*np.log10(hp_paras[3]), color='g', label = 'HighPass 1 Filter: >=%dHz pass'%hp_paras[0], linestyle='--')
    pp_paras = flt_info[1] 
    ax4.plot( (fs*0.5/np.pi)*pp_paras[2], 20*np.log10(pp_paras[3]), color='b', label = 'HighPass 2 Filter: >=%dHz pass'%pp_paras[0], linestyle='--')
    #ax1.plot(pp_paras[3], 20*np.log10(pp_paras[4]), color='b', label = 'Bandstop: stop=%dHz, start=%dHz, order=%d'%(pp_paras[0],pp_paras[1],pp_paras[2]))
    #ax4.plot( (fs*0.5/np.pi)*pp_paras[3], 20*np.log10(pp_paras[4]), color='b', label = 'Bandstop Filter')
    ax4.legend(loc='best')
    ax4.set_xlim([0,1000])
    ax4.set_ylabel("Power Spectral Desity /dB")
    ax4.set_xlabel("Frequency /Hz")

#    hp_paras = flt_info[0] 
#    ax4.plot(hp_paras[2], 20*np.log10(hp_paras[3]), color='g', label = 'HighPass: >%dHz pass, order=%d'%(hp_paras[0],hp_paras[1]))
#    pp_paras = flt_info[1] 
#    ax4.plot(pp_paras[3], 20*np.log10(pp_paras[4]), color='b', label = 'Bandstop: stop=%dHz, start=%dHz, order=%d'%(pp_paras[0],pp_paras[1],pp_paras[2]))
#    ax4.set_xlabel("Frequency /Hz")
#    ax4.set_ylabel("Gain")
#    ax4.set_title( "Filter Performance")
##    ax4.plot(f,p,color='r', label = 'Raw FFT' )
#    ax4.plot(hf,hp,color='g', label = 'Highpass FFT')
#    ax4.plot(pf,pp,color='b', label = 'Bandstop FFT')
#    ax4.legend(loc='best')
#    ax4.set_ylim([-80,40])
#    ax4.text( 100, -75, "RawMean=%3f, HPMean = %3f, BPMean = %3f"%(rms_info[1],h_info[1],p_info[1]) )
#    ax4.text( 100, -70,  "RawRMS=%3f, HPRMS = %3f, BPRMS = %3f"%(rms_info[2],h_info[2],p_info[2]) )
#    ax4.set_xlim([0,1000000])
#    ax4.set_xlabel("Frequency /Hz")
#    ax4.grid()
#    psd = True
#    if (psd == True):
#        ax4.set_ylabel("Power Spectral Desity /dB")
#    else:
#        ax4.set_ylabel("Amplitude /dB")
#    ax4.set_title( "FFT specturms")

    plt.tight_layout( rect=[0, 0.05, 1, 0.95])

    rmspos = onefile.find("_RMS")
    plt.savefig( plot_data_dir + "CHN_%d"%curchn + FEset + runno + onedir + onefile[0: rmspos] + "_FFT" +  onefile[rmspos+4:-4]  + ".png", format = "png" )
    plt.close()
    #plt.show()



                        #with open(savefile, 'wb') as fp:
                        #    pickle.dump(onechndata, fp)

####                        smp_data = onechndata
####                        print len(smp_data)
####                        fs = 2000000.0
####                        fft_s = 400000
####                        cycle = int(len(smp_data) / fft_s )
####                        print cycle
####
####                        smp_mean = np.mean(smp_data)
####                        smp_rms  = np.std(smp_data)
####                        print "MEAN%f,RMS%f"%(smp_mean,smp_rms)
####                        #flt_coefs, post_flt_data = highpass_filter(pre_flt_data = smp_data, fs = 2000000, flt_stopfreq = 100, flt_passfreq = 500, flt_order = 2001)
####                        post_flt_data, a, b = highpass_filter(pre_flt_data = smp_data, fs = 2000000, flt_stopfreq = 100, flt_passfreq = 400, flt_order = 2001)
####                        print "MEAN%f,RMS%f"%(np.mean(post_flt_data),np.std(post_flt_data))
####                        #print "MEAN%f,RMS%f"%(np.mean(flt_coefs),np.std(flt_coefs))
####
####                        psd = True
####                        if (psd == True):
####                            f,p = chn_fft_psd(smp_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
#####                            f1,p1 = chn_fft_psd(flt_coefs, fs = fs, fft_s=len(flt_coefs) , avg_cycle =1) 
#####                            f2,p2 = chn_fft_psd(post_flt_data, fs = fs, fft_s=len(post_flt_data) , avg_cycle =1) 
####                            f2,p2 = chn_fft_psd(post_flt_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
####                        else:
####                            f,p = chn_fft(smp_data, fs = fs, fft_s=fft_s , avg_cycle =cycle) 
####
####                        if (chni == 0 ):
####                            psum = np.array(p)
####                        else:
####                            print psum[0:10]
####                            print p[0:10]
####                            psum =psum +  np.array(p)
####                            print psum[0:10]
####
####                        w, h = signal.freqz(b, a, worN=1000)
####                        plt.figure(figsize=(16,9))
####                        ax = plt.subplot2grid((1, 1), (0, 0))
####                        ax.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = 10" )
####                        ax.set_xlim([0,10000])
####                        plt.tight_layout( rect=[0, 0.05, 1, 0.95])
####                        plt.savefig( rms_data_dir + "Filter_chn_%X"%chni +onefile[0: pos3] + "_FFT" +  onefile[pos3+4:] + ".png", format = "png" )
####                        plt.close()
####
####
####
####                        plt.figure(figsize=(16,9))
####                        ax = plt.subplot2grid((1, 1), (0, 0))
####                        ax.plot(f,p,color='r')
####                        if (chni == 4) :
####                            ax.plot(f,psum,color='b')
#####                        ax.plot(f1,p1,color='b')
####                        ax.plot(f2,p2,color='g')
####                        #patch.append( mpatches.Patch(color=clor))
####                        #label.append("%s wire, Chn%d, %.1f$\mu$s"%(wire_type, chn, tp_np[i]))
####                        #ax4.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
####                        #ax.set_xlim([0,fs/2])
####                        ax.set_xlim([0,1000])
####                        ax.set_xlabel("Frequency /Hz")
####
####                        ax.grid()
####                        if (psd == True):
####                            ax.set_ylabel("Power Spectral Desity /dB")
#####                            ax.set_ylim([-80,20])
####                        else:
####                            ax.set_ylabel("Amplitude /dB")
####                            ax.set_ylim([-40,20])
####                        #ax.legend(patch, label, loc=2, fontsize = 12 )
####                        ax.set_title( "FFT specturms of Chn0x0%x"%(chni))
####
####                        plt.tight_layout( rect=[0, 0.05, 1, 0.95])
####
####                        plt.savefig( rms_data_dir + "FFT_chn_%X"%chni +onefile[0: pos3] + "_FFT" +  onefile[pos3+4:] + ".png", format = "png" )
####                        plt.close()
####                        #plt.show()




    #return alldata 

#def raw_convertion( path, gainpath, step_np = ["step001"], env = "RT", femb=0, psd = True, rms_smps =130000, stuck_filter = True, gain = 3, gain_step = "step11", DAC = "FPGADAC", DACvalue = [4,5,6,7,8,9,10,11], jumbo_flag = False, apa="ProtoDUNE"):
##gain = 3 --> 25mV/fC
#    print "Start......"
#    #gainfile_path = gainpath + "\\" +  gain_step + "\\" + "FEMB%d%sgain.xlsx"%(femb,DAC)
#    gainfile_path = gainpath + "/" +  gain_step + "/" + "originalFEMB%d%sgain.xlsx"%(femb,DAC)
#    print "Gain file path = %s" %gainfile_path
#    for step in step_np:
#        wb = Workbook()
#        FEMBNO=str(femb)
#        alldata = rms_process_chn(path, onedir=step, env=env, FEMB = "FEMB"+FEMBNO, jumbo_flag = jumbo_flag )
#        print "All rawdata is read"
#    ########################################################################################
#        #savefile = path +"\\" + "FEMB%d"%femb +  step +  "_" + DAC + "_" + "alldata_result.bin"
#        savefile = path +"/" + "FEMB%d"%femb +  step +  "_" + DAC + "_" + "alldata_result.bin"
#        all_chn_results = raw_to_result(alldata, gainfile_path, savefile, apa=apa, step=step, femb=femb, psd=psd, env=env, gain=gain, DAC = DAC, DACvalue = DACvalue, stuck_filter = stuck_filter)
#        print "All rawdata have been analysized"
#    return all_chn_results
#

#path = "D:\\fft_code\\"
#raw_convertion( path , stepno_np = [106], env = "RT", femb=0, psd = True, gain = 3, gain_step = "step11")
