#!/usr/bin/python3
import time
import sys
from serialcomm import SerialComm


def c (d):
    print ("esto es mi callback")
    print (d)



s = SerialComm(c, '/dev/ttyACM0')
if s.port_open == False:
    print ("error en puerto")
    sys.exit(-1)
else:
    print ("todo OK?")

s.Write("Prueba dos con Maximo\n")

### si uso el thread no va esto
time.sleep(3)
print ("quito obj")
# data = s.Read()
# print (data)
s.Close()
