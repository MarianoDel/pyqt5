# -*- coding: utf-8 -*-
# use python3

import platform
import os
from io import IOBase
import sys


def OpenConfigFile (option, ip_mask, gw, dns):
    try:
        f = open ('/etc/dhcpcd.conf', 'r')
    except:
        print("no dhcpcd.conf found or bad permissions")
        sys.exit(0)

    lines_input = f.readlines()
    f.close()

    # truncate output file
    try:
        f = open ('/etc/dhcpcd.conf', 'w')
    except:
        print("no dhcpcd.conf found or bad permissions")
        sys.exit(0)

    block_found = False
    block_first = 0
    block_last = 0
    line_cnt = 0
    for line in lines_input:        
        if line.startswith('# start kirno lan config block'):
            block_first = line_cnt

        if line.startswith('# end kirno lan config block'):
            block_last = line_cnt

        if block_first != 0 and \
           block_last != 0 and \
           block_last > block_first:
            block_found = True
            print('block found on: ' + str(block_first) + ' to ' + str(block_last))
            break
        else:
            line_cnt += 1


    if block_found == True:
        if option == 'fix':
            for i in range(block_first):
                f.write(lines_input[i])

            # has to be end of file
            f.write('# start kirno lan config block\n')
            f.write('interface eth0\n')
            f.write('static ip_address=' + ip_mask + '\n')
            f.write('static routers=' + gw + '\n')
            f.write('static domain_name_servers=' + dns + ' 8.8.8.8\n')
            f.write('# end kirno lan config block\n')
            f.close()

        elif option == 'dynamic':
            for i in range(block_first):
                f.write(lines_input[i])
            
            f.write('# start kirno lan config block\n')
            f.write('# end kirno lan config block\n')
            f.close()

    else:
        if option == 'fix':
            for line in lines_input:        
                f.write(line)

            # write to the end of file
            f.write('# start kirno lan config block\n')
            f.write('interface eth0\n')
            f.write('static ip_address=' + ip_mask + '\n')
            f.write('static routers=' + gw + '\n')
            f.write('static domain_name_servers=' + dns + ' 8.8.8.8\n')
            f.write('# end kirno lan config block\n')
            f.close()

        elif option == 'dynamic':
            for line in lines_input:        
                f.write(line)

            # write to the end of file
            f.write('# start kirno lan config block\n')
            f.write('# end kirno lan config block\n')
            f.close()

    

if __name__ == "__main__":
    
    # check line arguments
    if len(sys.argv) < 2:
        print("use script [fix] [+settings] or [dynamic]")
        sys.exit(0)

    # check line arguments content
    if sys.argv[1] != 'fix' and \
       sys.argv[1] != 'dynamic':
        print("options are: fix or dynamic")
        sys.exit(0)
    
    # check distro
    (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
    if distname != "debian":
        print("only for debian operation on RPi!")
        print('asked for: ' + sys.argv[1] + ' with settings:')
        for x in range (2, len(sys.argv)):
            print(str(sys.argv[x]))
                  
        sys.exit(0)

    if sys.argv[1] == 'fix':
        if len(sys.argv) != 5:
            print('fix settings error!, settings are [ip/maskbits] [gw] [dns]')
            sys.exit(0)
        else:
            ip_mask = sys.argv[2]
            gw = sys.argv[3]
            dns = sys.argv[4]
            OpenConfigFile('fix', ip_mask, gw, dns)

    elif sys.argv[1] == 'dynamic':
        OpenConfigFile('dynamic', '', '', '')
        
        

    # # change operation bootup

    # splash_dir = ""
    # search_str = ""
    # # correct the stretcher versions
    # if 'stretcher31' in sys.argv[1]:
    #     search_str = 'main31.py'
    #     splash_str = 'stretcher'
    # elif 'stretcher32' in sys.argv[1]:
    #     search_str = 'main32.py'
    #     splash_str = 'stretcher'        
    # else:
    #     search_str = sys.argv[1]
    #     splash_str = sys.argv[1]
        

    # # copy splash screen for boot_up
    # os.system('sudo cp -f ' + splash_dir + 'splash.png /usr/share/plymouth/themes/pix/my_splash.png')
    # print("all operations done!")
    # sys.exit(1)

### end of file ###
