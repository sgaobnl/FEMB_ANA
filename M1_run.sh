#!/bin/bash
#        argv[0],   argv[1], argv[2], argv[3], argv[4], argv[5], argv[6],  argv[7],  argv[8], argv[9]
#        filename,  rmsdate, rmsrun , strenv,  rmsstep, gainrun, gainstep, gaindate, jumbo_flag, server  
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB00" 0 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB00" 1 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB00" 2 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB01" 1 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB01" 2 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB01" 3 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB02" 1 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB02" 2 &
python M1_raw_to_final_results_run_original.py 02_20_2019 01rms LN 31 01fpg 32 02_20_2019 True server "WIB02" 3 &

