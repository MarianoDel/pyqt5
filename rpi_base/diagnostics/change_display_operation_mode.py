# -*- coding: utf-8 -*-
# use python3

import get_distro
import os
from io import IOBase
import sys


def GetDistroName (show=False):
    distname = get_distro.GetDistroName()
    version = get_distro.GetDistroVersion()
    if show:
        os_text = "--" + distname + version + "-- "
        print("os: " + os_text)

    return distname



if __name__ == "__main__":
    
    # check line arguments
    if len(sys.argv) != 2:
        print("use executable new_operation")
        print("options are: magnet magnet_mt250 stretcher31 stretcher32 light_treat")
        sys.exit(0)

    # check line arguments content
    if sys.argv[1] != 'magnet' and \
       sys.argv[1] != 'magnet_mt250' and \
       sys.argv[1] != 'stretcher31' and \
       sys.argv[1] != 'stretcher32' and \
       sys.argv[1] != 'light_treat':
        print("options are: magnet magnet_mt250 stretcher31 stretcher32 light_treat")
        sys.exit(0)
    
    # check distro
    distro = GetDistroName()
    if distro != "debian":
        print("only for debian operation on RPi!")
        sys.exit(0)

    # change operation bootup
    try:
        f = open ('.xsession', 'r')
    except:
        print("no GUI startup file found")
        sys.exit(0)

    lines_input = f.readlines()
    f.close()

    # truncate output file
    try:
        f = open ('.xsession', 'w')
    except:
        print("no GUI startup file found")
        sys.exit(0)

    splash_dir = ""
    search_str = ""
    # correct the stretcher versions
    if 'stretcher31' in sys.argv[1]:
        search_str = 'main31.py'
        splash_str = 'stretcher'
    elif 'stretcher32' in sys.argv[1]:
        search_str = 'main32.py'
        splash_str = 'stretcher'        
    elif 'magnet_mt250' in sys.argv[1]:
        search_str = 'main_mt250.py'
        splash_str = 'magnet'
    else:
        search_str = sys.argv[1]
        splash_str = sys.argv[1]
        
    for line in lines_input:        
        if line.startswith('exec ') and not search_str in line:
            f.write('# ' + line)
        elif line.startswith('# exec ') and search_str in line:
            first_e = line.index('e')
            f.write(line[first_e:])
        else:
            f.write(line)

        if splash_str in line:            
            forslash = line.split('/')
            splash_dir = '/' + forslash[4] + '/' + forslash[5] + '/' + forslash[6] + '/'
            
            # print("splash dir: " + splash_dir)
            

    f.close()

    # copy splash screen for boot_up
    os.system('sudo cp -f ' + splash_dir + 'splash.png /usr/share/plymouth/themes/pix/my_splash.png')
    print("all operations done!")
    sys.exit(1)

