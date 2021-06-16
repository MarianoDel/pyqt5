# -*- coding: utf-8 -*-
#usar python3
import time

from gpios_qt import *
GpiosInit()


def TestLed():
    # print ("start blinking green led for 10 secs")
    print ("Led green on for 5 secs")
    LedOn()
    time.sleep(5)
    LedOff()
    print ("test led green ended!")

def TestLedToggle():
    # print ("start blinking green led for 10 secs")
    print ("Test Led green toggle")
    LedToggle()
    time.sleep(2)
    LedToggle()    
    # LedOff()
    print ("test led green ended!")
    

def TestBuzzer ():
    print ("Buzzer on for 1 sec")
    BuzzerOn()
    time.sleep(1)
    BuzzerOff()
    print ("test buzzer ended!")    

def TestBuzzerToggle():
    print ("Test Buzzer toggle")
    BuzzerToggle()
    time.sleep(2)
    BuzzerToggle()    
    print ("test Buzzer toggle ended!")
    

##############
# Main Tests #
##############
# GpiosInit()
# TestLedToggle()
TestBuzzerToggle()
# TestBuzzer()
# GpiosCleanUp()
