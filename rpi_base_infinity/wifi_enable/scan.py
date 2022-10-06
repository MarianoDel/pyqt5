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



interf_list = []
ip_list = []
output_str = output.decode('utf-8')
lines = output_str.split('\n')
cnt = 0
for line in lines:
    cnt += 1
    if line.startswith('eth'):
        ether = line.split(':')
        ether_str = ether[0]
        interf_list.append(ether_str)
        if 'inet ' in lines[cnt]:
            ip = lines[cnt].split('t')
            ip_str = ip[1]
            ip_str2 = ip_str.split(' ')
            ip_str = ip_str2[1]
            ip_list.append(ip_str)
        else:
            ip_list.append('None')

cnt = 0
for line in lines:
    cnt += 1
    if line.startswith('wlan'):
        ether = line.split(':')
        ether_str = ether[0]
        interf_list.append(ether_str)
        if 'inet ' in lines[cnt]:
            ip = lines[cnt].split('t')
            ip_str = ip[1]
            ip_str2 = ip_str.split(' ')
            ip_str = ip_str2[1]
            ip_list.append(ip_str)
        else:
            ip_list.append('None')

for i in range (len(interf_list)):
    print ('inter: ' + interf_list[i] + ' ip: ' + ip_list[i])

