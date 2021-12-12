# -*- coding: utf-8 -*-
# use python3

import platform
import os
from io import IOBase
import sys



#####################
# Get the OS distro #
#####################
def CheckCurrentDistro ():
    (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
    os_text = "--" + distname + version + "-- "
    print("os: " + os_text)

    check = False
    file1open = 0
    if distname == "Slackware ":
        file1 = open ('/etc/wpa_supplicant.conf', 'r')
        file1open = 1
        # ProcessConfig(file1, file2)
        check = True
    
    elif distname == "debian":
        file1 = open ('/etc/wpa_supplicant/wpa_supplicant.conf', 'r')
        file1open = 1
        check = True
        
    else:
        print("No distribution detected!")

    return (file1, distname, check)


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
    
    
    
if __name__ == "__main__":
    
    # check line arguments
    if len(sys.argv) != 3:
        print("use executable ssid pass")
        sys.exit(0)
        
    # check distro
    (wpa_file, distro, checked) = CheckCurrentDistro()
    if checked == False:
        sys.exit(0)

    # create a backup file
    if distro == "Slackware ":
        wpa_backup = open ('/etc/wpa_supplicant.bkp', 'w')
    elif distro == "debian":
        wpa_backup = open ('/etc/wpa_supplicant/wpa_supplicant.bkp', 'w')
    else:
        print("no backup file creation")
        sys.exit(0)

    
    # check if ssid is already there
    if not isinstance(wpa_file, IOBase):
        sys.exit(0)

    lines = wpa_file.readlines()
    (start, ssid, end) = SearchNetwork(lines, sys.argv[1])
    if start != 0 and ssid != 0 and end != 0:
        for i in range(start, end + 1):
            print(lines[i])

    # backup origin file
    for i in range(len(lines)):
        wpa_backup.write(lines[i])

    wpa_backup.close()

    # truncate origin file and copy/append new ssid
    # close and open to truncate
    wpa_file.close()
    if distro == "Slackware ":
        wpa_file = open ('/etc/wpa_supplicant.conf', 'w')
    elif distro == "debian":
        wpa_file = open ('/etc/wpa_supplicant/wpa_supplicant.conf', 'w')
    else:
        print("no truncate file creation")
        sys.exit(0)
    
    if start != 0 and ssid != 0 and end != 0:
        # remove present ssid
        for i in range(start):
            wpa_file.write(lines[i])

        for i in range(end + 1, len(lines)):
            wpa_file.write(lines[i])

        print("copy done!")
        
    else:
        print("copy all!")
        for i in range(len(lines)):
            wpa_file.write(lines[i])
        
    # create the new ssid
    wpa_file.write("\n")    
    wpa_file.write("network={\n")
    ssid_str = '        ssid=' + '"' + sys.argv[1] + '"' + '\n'
    wpa_file.write(ssid_str)
    psk_str = '        psk=' + '"' + sys.argv[2] + '"' + '\n'
    wpa_file.write(psk_str)
    wpa_file.write('        key_mgmt=WPA-PSK\n')
    wpa_file.write('}\n')    
    wpa_file.close()
    print("all done!")

    sys.exit(1)
        
