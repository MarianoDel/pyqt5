# -*- coding: utf-8 -*-
# use python3

import os
import subprocess

output = ""
try:
    output = subprocess.check_output(['/sbin/ifconfig'])
except subprocess.CalledProcessError as err:
    output = err
    print(err)


output_str = output.decode('utf-8')
lines = output_str.split('\n')
cnt = 0
mac_str = 'None'
ether_str = 'None'
for line in lines:
    cnt += 1
    if line.startswith('eth'):
        ether = line.split(':')
        ether_str = ether[0]

        if 'ether ' in lines[cnt]:
            mac = lines[cnt].split('r')
            mac_str = mac[1]
            mac_str2 = mac_str.split(' ')
            mac_str = mac_str2[1]


print (ether_str + ' ' + mac_str)
