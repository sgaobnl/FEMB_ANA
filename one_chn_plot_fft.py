# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Fri Nov 24 19:21:55 2017
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
 

def histogram_pedstals ( ax, chn, chndata, tp):
    clor = plot_color(tp)
    ax.hist(chndata[0][1], normed=1, color = clor)
    ped_mean = chndata[0][5]
    rms = chndata[0][6]
    ax.text(int(ped_mean)-int(rms)*2, 0.04, "%.1f$\mu$s: %.3f +/- %.3f" % (tp, ped_mean, rms), fontsize=10)
    ax.set_ylabel("Normalized counts", fontsize=10)
    ax.set_xlabel("ADC output/ (bin)", fontsize=10)
    ax.set_ylim([0, 0.05])
    ax.tick_params(labelsize="small")
    ax.set_title("Normalized Histogram of chn%d with (Tp = %.1f$\mu$s)"%(chn, tp), fontsize=10 )

def linear_fit_chn(ax, chn, x, y, tp, DACvalue=[1,2,3,4]):
    tmp_x = []
    tmp_y = []
    for onedac in DACvalue:
        tmp_x.append(x[onedac])
        tmp_y.append(y[onedac])

    error_fit = False 
    try:
        results = sm.OLS(tmp_y,sm.add_constant(tmp_x)).fit()
    except ValueError:
        print "Gain Error chn%d"%(chn) 
        error_fit = True 
    if ( error_fit == False ):
        error_gain = False 
        try:
            slope = results.params[1]
        except IndexError:
            slope = 0
            error_gain = True
        try:
            constant = results.params[0]
        except IndexError:
            constant = 0
    else:
        slope = 0
        constant = 0
        error_gain = True

    clor = plot_color(tp)

    ax.scatter(x, y, color = clor)
    x_plot = np.linspace(0,4096)
    ax.plot(x_plot, x_plot*slope + constant, color = clor)

    return slope, constant, error_fit, error_gain

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

def ax1_plot(ax1, one_chn_tp, chn, tp_np, wire_type, fs = 2000000, yrange=[000,4100], stuck_type_np=["Small","Small","Small","Small"]):
    patch = []
    label = []
    t = 1000000.0/fs #us
    Nsps = 100000
    for i in range(4):
        clor = plot_color(tp_np[i])
        tmp_Nsps = len(one_chn_tp[i][0][1])
        if (  tmp_Nsps > Nsps ):
            x_np = np.arange(Nsps)
            y_np = one_chn_tp[i][0][1][0:Nsps:100]
            x_np = x_np[0:tmp_Nsps:100]
        else:
            x_np = np.arange(tmp_Nsps)
            y_np = one_chn_tp[i][0][1][0:tmp_Nsps:100]
            x_np = x_np[0:tmp_Nsps:100]

        x_np = x_np*t
        ax1.scatter(x_np, y_np, color = clor)
        ax1.plot(x_np, y_np, color = clor)
        patch.append( mpatches.Patch(color=clor))
        label.append("%s wire, Chn%d, %.1f$\mu$s, Stuck=%s"%(wire_type, chn, tp_np[i], stuck_type_np[i]))

    ax1.legend(patch, label, loc=2, fontsize = 12 )
    ax1.set_xlim([0,max(x_np)])
#    ax1.set_ylim(yrange)
    ax1.grid()
    ax1.set_ylabel("ADC output / bin")
    ax1.set_xlabel("t / $\mu$s")
    ax1.set_title("Pedestal waveforms of chn%d"%(chn) )

def ax2_plots(ax2_array, one_chn_tp, chn, tp_np, wire_type):
    for i in range(4):
        histogram_pedstals (ax2_array[i], chn, one_chn_tp[i], tp_np[i] )

def ax3_plot(ax3, one_chn_tp, chn, tp_np, wire_type, DACvalue=[1,2,3,4]): 
    patch = []
    label = []
    ymax = 0
    fit_result_np = []
    for i in range(4):
        ped = one_chn_tp[i][0][5]
        x = one_chn_tp[i][1][1]
        x = np.array(x)-ped
        y = one_chn_tp[i][1][2]
        if ( ymax < max(y)):
            ymax = max(y)


        clor = plot_color(tp_np[i])
        fit_result = linear_fit_chn(ax3, chn, x, y, tp_np[i], DACvalue)
        patch.append( mpatches.Patch(color=clor))
        if (fit_result[2] == True):
            label.append("%s wire, Chn%d, %.1f$\mu$s, Linear Fit Error"%(wire_type, chn, tp_np[i]))
        else:
            label.append("%s wire, Chn%d, %.1f$\mu$s, Y=(%.2f)*X + (%d)"%(wire_type, chn, tp_np[i], fit_result[0], fit_result[1]))
        fit_result_np.append(fit_result)

    ax3.legend(patch, label, loc=0, fontsize = 12 )
    ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax3.set_xlim([0,4096])
    ax3.set_ylim([0,1e6])
    ax3.set_ylabel("Electrons /e-")
    ax3.set_xlabel("ADC output / bin")
    ax3.set_title("Linear Fit(chn%d)"%(chn) )
    ax3.grid()
    return fit_result_np

def ax4_plot(ax4, one_chn_tp, chn, tp_np, wire_type, fs = 2000000, psd = True, avg_cycle=100):
    patch = []
    label = []
    rms_np = []
    for i in range(4):
        f = one_chn_tp[i][0][3]
        p = one_chn_tp[i][0][4]
        rms = one_chn_tp[i][0][6]
        #fft_data = one_chn_tp[i][0][1]
        #if (psd == True):
        #    f,p,rms = chn_rfft_psd(fft_data, fs = fs, fft_s = 5000, avg_cycle=avg_cycle)
        #else:
        #    f,p,rms = chn_rfft(fft_data, fs = fs, fft_s = 5000, avg_cycle=avg_cycle)
        rms_np.append(rms)

        clor = plot_color(tp_np[i])
        ax4.plot(f,p,color=clor)

        patch.append( mpatches.Patch(color=clor))
        label.append("%s wire, Chn%d, %.1f$\mu$s"%(wire_type, chn, tp_np[i]))

    ax4.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    #ax4.set_xlim([0,fs/2])
    ax4.set_xlim([0,1000])
    ax4.set_xlabel("Frequency /Hz")
    ax4.grid()
    if (psd == True):
        ax4.set_ylabel("Power Spectral Desity /dB")
        ax4.set_ylim([-80,20])
    else:
        ax4.set_ylabel("Amplitude /dB")
        ax4.set_ylim([-40,20])
    ax4.legend(patch, label, loc=2, fontsize = 12 )

    ax4.set_title( "FFT specturms of Chn%d"%(chn))

def ax5_linear_fit(chn, x, y, tp, DACvalue = [1,2,3,4]):
    tmp_x = []
    tmp_y = []
    for onedac in DACvalue:
        tmp_x.append(x[onedac])
        tmp_y.append(y[onedac])

    error_fit = False 
    try:
        results = sm.OLS(tmp_y,sm.add_constant(tmp_x)).fit()
    except ValueError:
        print "Gain Error chn%d"%(chn) 
        error_fit = True 
    if ( error_fit == False ):
        error_gain = False 
        try:
            slope = results.params[1]
        except IndexError:
            slope = 0
            error_gain = True
        try:
            constant = results.params[0]
        except IndexError:
            constant = 0
    else:
        slope = 0
        constant = 0
        error_gain = True
    return slope, constant, error_fit, error_gain

def ax5_plot(plt, one_chn_tp, chn, tp_np, wire_type, yrange=[0,3000]):
    enc_np = []
    mker = ['o','*','^','x','d','+','s','8',"1","2"]
    for i in range(4):
        x = one_chn_tp[i][1][1]
        y = one_chn_tp[i][1][2]
        fit_result = ax5_linear_fit(chn, x, y, tp_np[i])
        enc = one_chn_tp[i][0][6] * fit_result[0] 
        enc_np.append(enc)
        clor = plot_color(tp_np[i])
        plt.scatter([tp_np[i]], [enc], color = clor, marker = mker[i] )
        plt.text(tp_np[i], 1500, "%d"%int(enc), fontsize=10)
    plt.plot(tp_np,enc_np, color = 'c')
    plt.ylim(yrange)
    plt.xlim([0,4])
    plt.ylabel("ENC /e-", fontsize=10)
    plt.xlabel("Peaking time / ($\mu$s)", fontsize=10)
    plt.tick_params(labelsize="small")
    plt.title("ENC comparision", fontsize=10 )
    plt.grid()

def one_chn_plot (all_chn_results, chn,  pp, step,env="RT", femb = 0, psd = True, gain =3, DACvalue=[1,2,3,4]):
    one_chn_tp = []
    stuck_type_np = []
    for tp in [0,1,2,3]: #0.5,1.0,2.0,30.
        one_chn_tp.append(all_chn_results[chn][tp])
        stuck_type_np.append(all_chn_results[chn][tp][0][8])

    fig = plt.figure(figsize=(18,12))

    ax1 = plt.subplot2grid((4, 4), (0, 0), colspan=2, rowspan=2)
    ax2_1 = plt.subplot2grid((4, 4), (0, 2))
    ax2_2 = plt.subplot2grid((4, 4), (0, 3))
    ax2_3 = plt.subplot2grid((4, 4), (1, 2))
    ax2_4 = plt.subplot2grid((4, 4), (1, 3))
    ax2_array = [ax2_1, ax2_2, ax2_3, ax2_4]
    ax3 = plt.subplot2grid((4, 4), (2, 0), colspan=2, rowspan=2)
    ax4 = plt.subplot2grid((4, 4), (2, 2), colspan=2, rowspan=2)

    wire_type=one_chn_tp[0][0][2]
    tp_np = [0.5,1,2,3]

    ax1_plot(ax1, one_chn_tp, chn, tp_np, wire_type, fs=2000000, yrange=[000, 4100], stuck_type_np=stuck_type_np ) 
    ax2_plots(ax2_array, one_chn_tp, chn, tp_np, wire_type)
    ax3_plot(ax3, one_chn_tp, chn, tp_np, wire_type, DACvalue) 
    ax4_plot(ax4, one_chn_tp, chn, tp_np, wire_type, fs = 2000000, psd = True, avg_cycle=100)

    fig.suptitle("%s: FEMB%dChn%d, %s wire"%(step, femb, chn, wire_type), fontsize = 28)
    plt.tight_layout( rect=[0, 0.05, 1, 0.95])

    plt.axes([0.77, 0.32, .18, .12])
    ax5_plot(plt, one_chn_tp, chn, tp_np, wire_type, yrange=[0,3000])

    plt.savefig(pp, format='pdf')
    plt.close()

