# -*- coding: utf-8 -*-
# use python3

import platform


def GetDistroName ():
    using_distro = False

    try:
        import distro
        using_distro = True
    except ImportError:
        pass

    if using_distro:
        linux_distro = distro.like()
    else:
        linux_distro = platform.linux_distribution()[0]

    return linux_distro    


def GetDistroVersion ():
    using_distro = False

    try:
        import distro
        using_distro = True
    except ImportError:
        pass

    if using_distro:
        linux_distro = distro.version()
    else:
        linux_distro = platform.linux_distribution()[1]

    return linux_distro    


if __name__ == "__main__":
    print('Distro name: ' + GetDistroName())
    print('Distro version: ' + GetDistroVersion())
