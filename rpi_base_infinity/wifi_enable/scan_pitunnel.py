# -*- coding: utf-8 -*-
# use python3

import os
import subprocess
import platform

(distname, version, nid) = platform.linux_distribution(full_distribution_name=1)    
if distname == 'debian':
    try:
        output = subprocess.check_output(['sudo','/bin/netstat','-tp'])
    
    except subprocess.CalledProcessError as err:
        output = err
        print(err)
        exit()

    output_str = output.decode('utf-8')
    lines = output_str.split('\n')

    for line in lines:
        if 'ESTABLISHED' in line:
            if 'terminal_monito' in line or 'monitor_device' in line:
                print('ESTABLISHED')
                exit()

else:
    print("nothing to done in slackware")

