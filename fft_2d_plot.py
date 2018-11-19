# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Thu Oct 12 11:15:25 2017
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
import numpy as np
import math
#from fft_chn import chn_rfft, chn_rfft_psd, chn_fft, chn_fft_psd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

from paras_tp_allchn import paras_tp_allchn

def fft_2d_oneplot(ax, all_chn_results, pp, wire_type="All", overlap = True, femb = 0, tp = 1, psd = True, step="step001", x_range=[0,1e6], SF=True):
    wire_tp_chn = paras_tp_allchn(all_chn_results, paras=2, wire_type=wire_type)
    f_tp_chn = paras_tp_allchn(all_chn_results, paras=3, wire_type=wire_type)
    p_tp_chn = paras_tp_allchn(all_chn_results, paras=4, wire_type=wire_type)
    s_tp_chn = paras_tp_allchn(all_chn_results, paras=11, wire_type=wire_type)
    rms_tp_chn = paras_tp_allchn(all_chn_results, paras=6, wire_type=wire_type)
    gain_tp_chn = paras_tp_allchn(all_chn_results, paras=9, wire_type=wire_type)
    chnno_tp_chn = paras_tp_allchn(all_chn_results, paras=10, wire_type=wire_type)
    total_chn = len(f_tp_chn[tp])
    rms_tp_chn = np.resize(rms_tp_chn,[4,total_chn])
    gain_tp_chn = np.resize(gain_tp_chn,[4,total_chn])
    enc_tp_chn = np.array(rms_tp_chn) * np.array(gain_tp_chn)
    print "FFT 2D plots --> %s wires has %d channels in total"%(wire_type, total_chn)

    total_chn = len(f_tp_chn[tp])
    for chn in range(total_chn):
        f = f_tp_chn[tp][chn]
        p = p_tp_chn[tp][chn]
        color = 'y' 
        if (wire_tp_chn[tp][chn] == "Y"):
            color = 'g' 
        if (wire_tp_chn[tp][chn] == "U"):
            color = 'b' 
        if (wire_tp_chn[tp][chn] == "V"):
            color = 'r' 
        if ( SF == False):
            ax.plot(f,p,color=color)
            if (overlap):
                pass
            else:
                ax.set_title( "FFT spectrum of a %s wire, chn%d"%(wire_type, chnno_tp_chn[tp][chn]))
                break
        else:
            if ( s_tp_chn[tp][chn] == "Small"):
                ax.plot(f,p,color=color)
                if (overlap):
                    pass
                else:
                    ax.set_title( "FFT spectrum of a %s wire, chn%d"%(wire_type, chnno_tp_chn[tp][chn]) )
                    break
    if (overlap):
        ax.set_title( "Overlap FFT spectrum plot of %s wires"%(wire_type))
        ax.text(20000, 0, "%dchns: mean(ENC) = %de-, std(ENC) = %de-"%(len(enc_tp_chn[tp]),int(np.mean(enc_tp_chn[tp])), int(np.std(enc_tp_chn[tp]))))
        ax.text(20000, -20, "Green: Y wires", color = 'g')
        ax.text(350000, -20, "Blue: U wires", color = 'b')
        ax.text(700000, -20, "Red: V wires", color = 'r')
    ax.set_xlim(x_range)
    ax.grid()
    ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    ax.set_xlabel("Frequency /Hz")
    if (psd == True):
        ax.set_ylabel("Power Spectral Desity /dB")
        ax.set_ylim([-80,20])
    else:
        ax.set_ylabel("Amplitude /dB")
        ax.set_ylim([-40,20])

def fft_2d_plot(all_chn_results, pp, femb = 0, tp = 0, psd = True, step="step001", x_range=[0,1e6], SF=True):
    fig = plt.figure()

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(18, 12))
    fft_2d_oneplot(ax1, all_chn_results, pp, wire_type="All", overlap=True,  femb=femb, tp =tp, psd =psd, step=step, x_range=x_range, SF=SF)
    fft_2d_oneplot(ax2, all_chn_results, pp, wire_type="Y",   overlap=False, femb=femb, tp =tp, psd =psd, step=step, x_range=x_range, SF=SF)
    fft_2d_oneplot(ax3, all_chn_results, pp, wire_type="U",   overlap=False, femb=femb, tp =tp, psd =psd, step=step, x_range=x_range, SF=SF)
    fft_2d_oneplot(ax4, all_chn_results, pp, wire_type="V",   overlap=False, femb=femb, tp =tp, psd =psd, step=step, x_range=x_range, SF=SF)

    if (tp == 0):
        tp_str = "0.5"
    if (tp == 1):
        tp_str = "1.0"
    if (tp == 2):
        tp_str = "2.0"
    if (tp == 3):
        tp_str = "3.0"    

    fig.suptitle("%s: FFT spectrums of FEMB%d when peak time = %s$\mu$s"%(step, femb, tp_str), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])
    plt.savefig(pp, format='pdf')
    plt.close()

