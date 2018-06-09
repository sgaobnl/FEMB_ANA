#!/bin/bash
#        argv[0],   argv[1], argv[2], argv[3], argv[4], argv[5], argv[6],  argv[7],  argv[8], argv[9]
#        filename,  rmsdate, rmsrun , strenv,  rmsstep, gainrun, gainstep, gaindate, jumbo_flag, server  
python M1_raw_to_final_results_run_original.py 06_05_2018 01rms LN 31 01fpg 32 06_05_2018 False, server 1 &
python M1_raw_to_final_results_run_original.py 06_05_2018 01rms LN 31 01fpg 32 06_05_2018 False, server 2 &
python M1_raw_to_final_results_run_original.py 06_05_2018 01rms LN 31 01fpg 32 06_05_2018 False, server 3 &
python M1_raw_to_final_results_run_original.py 06_05_2018 01rms LN 31 01fpg 32 06_05_2018 False, server 4 &
python M1_raw_to_final_results_run_original.py 06_05_2018 01rms LN 31 01fpg 32 06_05_2018 False, server 5 &
python M1_raw_to_final_results_run_original.py 06_05_2018 01rms LN 31 01fpg 32 06_05_2018 False, server 6 &


