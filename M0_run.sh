#!/bin/bash
#                                                                                    APAno 
####argv[0] M0_raw_process_gain_mac_original.py
####argv[1] date 
####argv[2] run number and test type
####argv[3] env :RT or LN (useless now)
####argv[4] stepXY, X=3(25mV/fC), 1(14mV/fC), Y = 2 (FPGADAC), 4(ASICDAC) 
####argv[5] False
####argv[6] server
####argv[7]  APA no
python M0_raw_process_gain_mac_original.py 06_05_2018 run01fpg LN step32 False server 1      &
python M0_raw_process_gain_mac_original.py 06_05_2018 run01fpg LN step32 False server 2      &
python M0_raw_process_gain_mac_original.py 06_05_2018 run01fpg LN step32 False server 3      &
python M0_raw_process_gain_mac_original.py 06_05_2018 run01fpg LN step32 False server 4      &
python M0_raw_process_gain_mac_original.py 06_05_2018 run01fpg LN step32 False server 5      &
python M0_raw_process_gain_mac_original.py 06_05_2018 run01fpg LN step32 False server 6      &

