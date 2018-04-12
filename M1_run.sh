#!/bin/bash
#        argv[0],   argv[1], argv[2], argv[3], argv[4], argv[5], argv[6],  argv[7],  argv[8], argv[9]
#        filename,  rmsdate, rmsrun , strenv,  rmsstep, gainrun, gainstep, gaindate, jumbo_flag, server  
#python M1_tmp.py 01_15_2018 02rms RT 31 02fpg 32 01_15_2018 False, server &
python M1_raw_to_final_results_run_original.py 04_12_2018 01rms LN 31 01fpg 32 04_12_2018 False, server &

