# -*- coding: utf-8 -*-
#usar python3
# import RPi.GPIO as GPIO
import platform

# import threading
# import time

###########################################
# Seteo Inicial de todos los GPIOs a usar #
###########################################
LED = 6    #green led
BUZZER = 26

(system, node, release, version, machine, processor) = platform.uname()

if machine == 'x86_64':
    print("gpios importing rpi gpio lib")
else:
    import RPi.GPIO as GPIO
    
def GpiosInit():
    if machine == 'x86_64':
        print("gpios init")
    else:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED, GPIO.OUT)
        GPIO.setup(BUZZER, GPIO.OUT)


def GpiosCleanUp():
    if machine == 'x86_64':
        print("gpios cleanup")
    else:
        GPIO.cleanup()

    
#############
# LED Green #
#############
led = 0
def LedOn():
    if machine == 'x86_64':
        print("gpios led on")
        global led
        led = 1
    else:
        GPIO.output(LED, GPIO.LOW)


def LedOff():
    if machine == 'x86_64':
        print("gpios led off")
        global led        
        led = 0
    else:
        GPIO.output(LED, GPIO.HIGH)


def LedIsOn ():
    if machine == 'x86_64':
        if led:
            print("gpios led is on")
        else:
            print("gpios led is off")

        return led
    else:
        if GPIO.input(LED) == 1:
            return 0
        else:
            return 1
            
    
def LedToggle():
    if LedIsOn():
        LedOff()
    else:
        LedOn()

        
# already_toggling = 0
# t = threading.Thread()
# def LedToggleContinous(action):
#     global already_toggling
#     global t

#     if action == 'start':
#         if not already_toggling:
#             already_toggling = 1
#             t = threading.Thread(target=LedBlueToggle_Thread, args=())
#             t.start()
            
#     elif action == 'stop':
#         if already_toggling:
#             t.do_run = False
#             LedBlueOff()
#             already_toggling = 0
#             t.join()


# def LedBlueToggle_Thread():
#     t = threading.currentThread()
#     while getattr(t, "do_run", True):
#         LedBlueOn()
#         time.sleep(1.3)
#         LedBlueOff()
#         time.sleep(0.7)
        
        
##########
# BUZZER #
##########
buzzer = 0
def BuzzerOn():
    if machine == 'x86_64':
        print("gpios buzzer on")
        global buzzer        
        buzzer = 1
    else:
        GPIO.output(BUZZER, GPIO.HIGH)


def BuzzerOff():
    if machine == 'x86_64':
        print("gpios buzzer off")
        global buzzer
        buzzer = 0
    else:
        GPIO.output(BUZZER, GPIO.LOW)


def BuzzerIsOn ():
    if machine == 'x86_64':
        if buzzer:
            print("gpios buzzer is on")
        else:
            print("gpios buzzer is off")

        return buzzer
    else:
        if GPIO.input(BUZZER) == 0:
            return 0
        else:
            return 1

def BuzzerToggle():
    if BuzzerIsOn():
        BuzzerOff()
    else:
        BuzzerOn()
        
# def OnOff_Toggle():
#     if GPIO.input(ON_OFF) == 0:
#         GPIO.output(ON_OFF, GPIO.HIGH)
#     else:
#         GPIO.output(ON_OFF, GPIO.LOW)



# def BuzzerPulse(timer):
#     start_new_thread(BuzzerPulse_Thread, (timer,))


# def BuzzerPulse_Thread(timer):
#     BuzzerOn()
#     time.sleep(timer)
#     BuzzerOff()

    

### end of file ###




    
