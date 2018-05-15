import serial
import threading
import time


def ReadBytes(self, cb):
    """
    Loop para leer bytes del puerto serie, hasta un \n (readline) o con timer???
    """

    t = threading.currentThread()
    # i = 0
    while getattr(t, "do_run", True):
    # while True:
        # bytes_to_read = self.ser.inWaiting()
        # if (bytes_to_read > 0):
        #     datar = self.ser.read(bytes_to_read)
        #     cb(datar)
        datar = self.ser.readline()
        cb((datar).decode())
        # cb(unicode(datar))
        # print ("vuelta: ", i)
        # i += 1
        # time.sleep(1)

    print ("closing?\n")



class SerialComm:
    """
    Clase para manejo de puerto serie

    recibe:
    port: nombre o ruta de dispositivo, ej /dev/ttyACM0
    velocidad: ej 9600
    callback: funcion a la que enviar los datos recibidos

    Variables miembro:
    port_open, True o False
    """

    port_open = False

    def __init__(self, callback, port, velocidad=9600):
        """
        Abrir puerto seleccionado
        """
        # print ("piden " + port)
        # print (velocidad)
        # callback()
        try:
            self.ser = serial.Serial(port, velocidad)
            if (self.ser != None):
                print ("Port Open\n")
                self.port_open = True

            #comienzo el thread de lectura
            self.hilo1 = threading.Thread(target=ReadBytes, args=(self, callback))
            self.hilo1.start()
        except:
            print ("Port Not Open\n")

    def Write(self, data):
        self.ser.write(data.encode('utf-8'))

    def Read(self):
        bytes_to_read = self.ser.inWaiting()
        if (bytes_to_read > 0):
            datar = self.ser.read(bytes_to_read)
            return datar

    def Close(self):
        if (self.port_open == True):
            print ("quito thread\n")
            self.port_open = False
            self.hilo1.do_run = False
            self.ser.cancel_read()
            time.sleep(1)
            self.ser.close()
            self.hilo1.join()
