#!/bin/bash
#        argv[0],   argv[1], argv[2], argv[3], argv[4], argv[5], argv[6],  argv[7],  argv[8], argv[9], argv[10]
#        filename, months, dates,  gain tp APAno  server_flag  stryear  FE_temper_flg
python M9_ProtoDUNE_cooldown.py "01" "15-16-17-18-19" 3 0 2 server 2018 False &
python M9_ProtoDUNE_cooldown.py "01" "15-16-17-18-19" 3 1 2 server 2018 False &
python M9_ProtoDUNE_cooldown.py "01" "15-16-17-18-19" 3 2 2 server 2018 False &
python M9_ProtoDUNE_cooldown.py "01" "15-16-17-18-19" 3 3 2 server 2018 False &
#python M9_ProtoDUNE_cooldown.py "03" "20-21" 3 2 4 server 2018 False &
#python M9_ProtoDUNE_cooldown.py "02" "06-07" 3 1 2 server 2018 False &
#python M9_ProtoDUNE_cooldown.py "02" "06-07" 3 2 2 server 2018 False &
#python M9_ProtoDUNE_cooldown.py "02" "06-07" 3 3 2 server 2018 False &
