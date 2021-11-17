# -*- coding: utf-8 -*-
# use python3

import platform
import os
from io import IOBase

def ProcessConfig (origin, destination):
    if isinstance(origin, IOBase) and isinstance(destination, IOBase):
        print('origin and destination ok')
        # check networks
        lines = origin.readlines()
        # net = "OFICINA"
        # net = "linksys_CASA"
        # net = "Fibertel WiFi847 2.4GHz"
        net = "Borist"                                    
        (start, ssid, end) = SearchNetwork(lines, net)            
        print(start)
        print(ssid)
        print(end)
        for i in range(start, end + 1):
            print(lines[i])

        # last check before broke something
        if start != 0 and ssid != 0 and end != 0:
            for i in range(start):
                destination.write(lines[i])

            for i in range(end + 1, len(lines)):
                destination.write(lines[i])

            print("copy done!")

                    
def SearchNetwork (lines, network):
    mynet = '"' + network + '"'
    print("search for: " + mynet)

    cnt = 0
    cnt_net = 0
    cnt_start = 0
    cnt_ssid = 0
    cnt_end_net = 0
    check_first = False
    for line in lines:
        
        if line.startswith('network'):
            cnt_net = cnt

        if mynet in line:
            cnt_start = cnt_net
            cnt_ssid = cnt
            print("line with net is: " + str(cnt_start))
            print("line with ssid is: " + str(cnt_ssid))
            check_first = True

        if check_first:
            if '}' in line:
                cnt_end_net = cnt
                check_first = False
                print("line end is: " + str(cnt_end_net))
                
        cnt += 1


    if cnt_start == cnt_ssid - 1 and cnt_end_net < cnt_ssid + 10:
        return (cnt_start, cnt_ssid, cnt_end_net)
    else:
        return (0, 0, 0)
    
    
    

        
#####################
# Get the OS distro #
#####################
(distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
os_text = "--" + distname + version + "-- "
print("os: " + os_text)

# (system, node, release, version, machine, processor) = platform.uname()
# print("system: " + system)
# print("node: " + node)
# print("release: " + release)
# print("version: " + version)
# print("machine: " + machine)
# print("processor: " + processor)
file1open = 0
file2open = 0
if distname == "Slackware ":
    file1 = open ('/etc/wpa_supplicant.conf', 'r')
    file2 = open ('data.conf', 'a')
    file1open = 1
    file2open = 1    
    ProcessConfig(file1, file2)

    
elif distname == "debian":
    file1 = open ('/etc/wpa_supplicant/wpa_supplicant.conf', 'r')
    file1open = 1
else:
    print("No distribution detected!")

if file1open:
    file1.close()

if file2open:
    file2.close()
