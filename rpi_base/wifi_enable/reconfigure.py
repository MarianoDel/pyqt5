# -*- coding: utf-8 -*-
# use python3

import os
import sys
import platform


(distname, version, nid) = platform.linux_distribution(full_distribution_name=1)    
if distname == 'debian':
    if len(sys.argv) < 2:
        os.system('sudo wpa_cli -iwlan0 reconfigure')
        os.system('sleep 1')
        os.system('rfkill block wlan')
        os.system('sleep 2')
        os.system('rfkill unblock wlan')
        print("updating", end="", flush=True)
        for i in range (15):
            os.system('sleep 1')
            print(".", end="", flush=True)

        print("")
        os.system('ifconfig wlan0')
    else:
        os.system('sudo wpa_cli -iwlan0 reconfigure')
        os.system('sleep 1')
        os.system('rfkill block wlan')
        os.system('sleep 2')
        os.system('rfkill unblock wlan')

else:
    print("nothing to done in slackware")


