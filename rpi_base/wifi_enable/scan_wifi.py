# -*- coding: utf-8 -*-
# use python3

import os
import subprocess
import get_distro

distname = get_distro.GetDistroName()
output = ""
try:
    if distname == "Slackware ":
        output = subprocess.check_output(['/sbin/iwlist','wlan0', 'scan'])
    else:
        output = subprocess.check_output(['sudo','/sbin/iwlist','wlan0', 'scan'])
    
except subprocess.CalledProcessError as err:
    output = err
    print(err)

    
essid_list = []
rssi_list = []
output_str = output.decode('utf-8')
lines = output_str.split('\n')
cnt = 0
for line in lines:
    cnt += 1
    if 'Signal level=' in line:
        rssi = line.split('=')
        rssi_list.append(rssi[2])
    if 'ESSID' in line:
        essid = line.split('"')
        essid_list.append(essid[1])

for i in range(len(essid_list)):
    try:
        print(essid_list[i] + ' signal:' + rssi_list[i])
    except:
        pass

