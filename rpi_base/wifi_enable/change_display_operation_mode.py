# -*- coding: utf-8 -*-
# use python3

import platform
import os
from io import IOBase
import sys

def GetDistroName (show=False):
    (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
    if show:
        os_text = "--" + distname + version + "-- "
        print("os: " + os_text)

    return distname



if __name__ == "__main__":
    
    # check line arguments
    if len(sys.argv) != 2:
        print("use executable new_operation")
        print("operations are: magnet stretcher light_treatment")        
        sys.exit(0)

    # check line arguments content
    if sys.argv[1] != 'magnet' or \
       sys.argv[1] != 'stretcher' or \
       sys.argv[1] != 'light_treament':
        print("operations are: magnet stretcher light_treatment")
        sys.exit(0)
    
    # check distro
    distro = GetDistroName()
    if distro != "debian":
        print("only for debian operation on RPi!")
        sys.exit(0)

    # change operation bootup
    try:
        f = open ('~/.xsession', 'r')
    except:
        print("no GUI startup file found")
        sys.exit(0)

    lines_input = f.readlines()
    f.close()

    # truncate output file
    try:
        f = open ('~/.xsession', 'w')
    except:
        print("no GUI startup file found")
        sys.exit(0)
    
    for line in lines_input:        
        if line.startswith('exec ') and not sys.argv[1] in line:
            f.write('# ' + line)
        elif line.startswith('# exec ') and sys.argv[1] in line:
            first_e = line.index('e')
            f.write(line[first_e:])
        else:
            f.write(line)

    f.close()
            
    print("all operations done!")

