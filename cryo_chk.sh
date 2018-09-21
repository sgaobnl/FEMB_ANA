
#!/bin/bash
##         argv[0]                  argv[1]        argv[2] argv[3] argv[4] argv[5] argv[6] argv[7]  argv[8]  argv[9]  argv[10]  argv[11]
##                                  mon_date_year, run_no, APAno,    env,  gain,    tp,    server,  max_rms, min_rms  hp_flt    plot_en
#python  M8_ProtoDUNE_coldbox.py     "08_30_2018"    "01"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"  & 
#python  M8_ProtoDUNE_coldbox.py     "08_23_2018"    "01"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "08_23_2018"    "01"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "08_23_2018"    "01"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "08_23_2018"    "02"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "08_23_2018"    "01"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   

#python  M8_ProtoDUNE_coldbox.py     "08_27_2018"    "01"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_10_2018"    "01"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1F"   
#python  M8_ProtoDUNE_coldbox.py     "09_10_2018"    "02"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1F"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "02"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "01"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "01"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "02"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "01"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "01"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   

#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "03"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "02"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "03"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "03"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "02"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "02"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "03"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   

#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   


#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "07"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "03"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#

#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "04"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "07"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "05"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   


#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "08"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "06"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "07"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "07"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "07"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_13_2018"    "07"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "03"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "03"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   


#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   


#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "01"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "01"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "01"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "01"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "01"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   


#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "02"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "02"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "02"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "02"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "02"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_17_2018"    "02"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_18_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_18_2018"    "01"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_18_2018"    "02"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_18_2018"    "02"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_18_2018"    "03"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_18_2018"    "03"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "01"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   


#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "03"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "03"     3       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "04"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "02"     5       "LN"   3       3     "server"    3650       800     "False"    "0x7B"   


#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "03"     1       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "03"     2       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "03"     4       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "05"     5       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "03"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   
#python  M8_ProtoDUNE_coldbox.py     "09_19_2018"    "04"     6       "LN"   1       3     "server"    3650       800     "False"    "0x7B"   

#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     3       "LN"   1       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     4       "LN"   1       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     5       "LN"   1       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   

#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     1       "LN"   3       3     "server"    3650       800     "False"    "0x84"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "02"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   

#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_15_2018"    "01"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   



#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "03"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "03"     5       "LN"   1       3     "server"    3650       800     "False"    "0x1B"   

#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "01"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_14_2018"    "03"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   




#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     1       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     2       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     3       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     4       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     5       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   
#python  M8_ProtoDUNE_coldbox.py     "09_16_2018"    "02"     6       "LN"   3       3     "server"    3650       800     "False"    "0x1B"   






