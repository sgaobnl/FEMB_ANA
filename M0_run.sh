#!/bin/bash
#                                                                                     
####argv[0] M0_raw_process_gain_mac_original.py
####argv[1] date 
####argv[2] run number and test type
####argv[3] env :RT or LN (useless now)
####argv[4] stepXY, X=3(25mV/fC), 1(14mV/fC), Y = 2 (FPGADAC), 4(ASICDAC) 
####argv[5] False
####argv[6] server
python M0_raw_process_gain_mac_original.py 02_20_2019 run01fpg LN step32 True server 

