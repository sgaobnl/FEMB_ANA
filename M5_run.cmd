::#!/bin/bash
::#        argv[0],   argv[1], argv[2], argv[3], argv[4], argv[5],  argv[6],  argv[7],  argv[8], argv[9],  argv[10], argv[11], argv[12], argv[13]
::#        filename,  rmsdate, rmsrun , rmsstep, strenv,  gaindate, gainrun,  gainstep, jumbo_flag, server, mode,    apa_type, wiretype, regulator_cs
::#python M5_raw_to_final_results_brombreg.py "01_18_2018" 01bbm 38 LN "01_16_2018" 04fpg 32 False, server 2 ProtoDUNE U A &
::#python M5_raw_to_final_results_brombreg.py "01_18_2018" 01bbm 38 LN "01_16_2018" 04fpg 32 False, server 2 ProtoDUNE V A &
::#python M5_raw_to_final_results_brombreg.py "01_18_2018" 01bbm 38 LN "01_16_2018" 04fpg 32 False, server 2 ProtoDUNE X A &
::
::
python M5_raw_to_final_results_brombreg.py "01_17_2019" 01bbm 38 RT "01_17_2018" 02fpg 32 True Win 2 APA40 U A &
::python M5_raw_to_final_results_brombreg.py "01_17_2019" 01bbm 38 RT "01_17_2018" 02fpg 32 True Win 2 APA40 V A &
::python M5_raw_to_final_results_brombreg.py "01_17_2019" 01bbm 38 RT "01_17_2018" 02fpg 32 True Win 2 APA40 X A &

::
::
::#python M5_raw_to_final_results_brombreg.py "11_17" 23 38 LN "11_15" 43 32 False, server 2 ProtoDUNE U L &
::#python M5_raw_to_final_results_brombreg.py "11_17" 23 38 LN "11_15" 43 32 False, server 2 ProtoDUNE V L &
::#python M5_raw_to_final_results_brombreg.py "11_17" 23 38 LN "11_15" 43 32 False, server 2 ProtoDUNE X L &
::#python M5_raw_to_final_results_brombreg.py "11_17" 23 38 LN "11_15" 43 32 False, server 2 ProtoDUNE U R &
::#python M5_raw_to_final_results_brombreg.py "11_17" 23 38 LN "11_15" 43 32 False, server 2 ProtoDUNE V R &
::#python M5_raw_to_final_results_brombreg.py "11_17" 23 38 LN "11_15" 43 32 False, server 2 ProtoDUNE X R &

#
#
