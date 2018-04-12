#!/bin/bash
#        argv[0],   argv[1], argv[2], argv[3], argv[4], argv[5], argv[6],  argv[7],  argv[8], argv[9], argv[10]
#        filename,  rmsdate, rmsrun , rmsstep, strenv,  gaindate, gainrun, gainstep, jumbo_flag, server apa_type 
#python M14_raw_to_final_results_run_filtered.py "01_17_2018" 05rms 31 LN "01_16_2018" 05fpg 32 False server ProtoDUNE &
python M14_raw_to_final_results_run_filtered.py "01_17_2018" 06rms 31 LN "01_16_2018" 05fpg 32 False server ProtoDUNE &
python M14_raw_to_final_results_run_filtered.py "01_17_2018" 07rms 31 LN "01_16_2018" 05fpg 32 False server ProtoDUNE &
python M14_raw_to_final_results_run_filtered.py "01_16_2018" 04rms 31 LN "01_16_2018" 05fpg 32 False server ProtoDUNE &
python M14_raw_to_final_results_run_filtered.py "01_16_2018" 05rms 31 LN "01_16_2018" 05fpg 32 False server ProtoDUNE &
#python M14_raw_to_final_results_run_filtered.py "11_15" 41 31 LN "11_15" 43 32 False server ProtoDUNE &
#python M14_raw_to_final_results_run_filtered.py "11_15" 26 31 LN "11_15" 43 32 False server ProtoDUNE &
