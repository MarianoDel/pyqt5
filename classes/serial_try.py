import time
import serial

print ("Starting program")

ser = serial.Serial('/dev/ttyACM0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
print ("go to sleep")
time.sleep(1)
try:
    ser.write(('Hello World\r\n').encode('utf-8'))
    ser.write(('Serial Communication Using Raspberry Pi\r\n').encode('utf-8'))
    ser.write(('By: Embedded Laboratory\r\n').encode('utf-8'))
    print ('Data Echo Mode Enabled')
    while True:
        if ser.inWaiting() > 0:
            data = ser.read()
            print (data)

except KeyboardInterrupt:
    print ("Exiting Program")

except:
    print ("Error Occurs, Exiting Program", sys.exc_info()[0])

finally:
    ser.close()
    pass
