import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from ui_magneto import Ui_Dialog
from serialcomm import SerialComm
from time import sleep

"""
    Pruebas con seniales y eventos custom
    http://zetcode.com/gui/pyqt5/eventssignals/
"""

### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

    # receivedData = pyqtSignal()
    

class Dialog(QDialog):

    rcv_signal = pyqtSignal(str)
    
    def __init__(self):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # # Make some local modifications.
        # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        self.ui.t10.clicked.connect(self.Envio_triangular_10)
        self.ui.t30.clicked.connect(self.Envio_triangular_30)
        self.ui.t60.clicked.connect(self.Envio_triangular_60)
        self.ui.c10.clicked.connect(self.Envio_cuadrada_10)
        self.ui.c30.clicked.connect(self.Envio_cuadrada_30)
        self.ui.c60.clicked.connect(self.Envio_cuadrada_60)
        self.ui.start_treat.clicked.connect(self.Start_Treatment)
        self.ui.stop_treat.clicked.connect(self.Stop_Treatment)
        self.ui.pause_treat.clicked.connect(self.Pause_Treatment)
        self.ui.get_conf.clicked.connect(self.Get_Treatment_Conf)        

        # #con el boton lanzo el evento close, que luego llama a closeEvent
        # self.ui.closeButton.clicked.connect(self.close)

        #creo el evento y lo conecto al slot
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #Envio3 lo dispara

        #creo una senial de prueba y la conecto        
        self.rcv_signal.connect(self.MySignalCallback)

        #self.MyObjCallback la llaman desde otro thread, armo una senial
        #antes de modificar UI
        self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
        if self.s.port_open == False:
            self.ui.label.setText("Sin puerto serie!!!")
            # sys.exit(-1)
            #TODO: agregar un timer que vaya buscando el puerto!!!
        else:
            self.ui.label.setText("puerto serie abierto OK!")

        #customs window flags
        # self.ui.setWindowFlags(Qt.FramelessWindowHint)


    def Envio_triangular_10 (self):
        if (self.s.port_open):
            self.ui.label.setText("Enviando info... duration")
            self.s.Write("duration,00,15,00,1\r\n")
            # sleep(1)
            self.ui.label.setText("Enviando info... signal")            
            self.s.Write("signal,100,100,0000,0049,0001,0001,0049,0000,0000,1\r\n")
            # self.s.Write("signal,070,070,0000,0049,0001,0001,0049,0000,0000,1\r\n")            
            # sleep(1)
            self.ui.label.setText("Enviando info... state")
            self.s.Write("state_of_stage,1,1\r\n")
            # sleep(1)
            self.ui.label.setText("Saving...")            
            self.s.Write("save,01\r\n")
            sleep(1)            
        else:
            self.ui.label.setText("Port not Open!!!")
            
    def Envio_triangular_30 (self):
        if (self.s.port_open):
            self.ui.label.setText("Enviando info... duration")
            self.s.Write("duration,00,15,00,1\r\n")
            # sleep(1)
            self.ui.label.setText("Enviando info... signal")            
            self.s.Write("signal,100,100,0000,0016,0001,0001,0015,0000,0000,1\r\n")
            # self.s.Write("signal,070,070,0000,0016,0001,0001,0015,0000,0000,1\r\n")            
            # sleep(1)
            self.ui.label.setText("Enviando info... state")
            self.s.Write("state_of_stage,1,1\r\n")
            # sleep(1)
            self.ui.label.setText("Saving...")            
            self.s.Write("save,01\r\n")
            sleep(1)            
        else:
            self.ui.label.setText("Port not Open!!!")
            
    def Envio_triangular_60 (self):
        if (self.s.port_open):            
            self.ui.label.setText("Enviando info... duration")
            self.s.Write("duration,00,15,00,1\r\n")
            # sleep(1)
            self.ui.label.setText("Enviando info... signal")            
            self.s.Write("signal,100,100,0000,0007,0001,0001,0007,0000,0000,1\r\n")
            # self.s.Write("signal,070,070,0000,0007,0001,0001,0007,0000,0000,1\r\n")            
            # sleep(1)
            self.ui.label.setText("Enviando info... state")
            self.s.Write("state_of_stage,1,1\r\n")
            # sleep(1)
            self.ui.label.setText("Saving...")            
            self.s.Write("save,01\r\n")
            sleep(1)            
        else:
            self.ui.label.setText("Port not Open!!!")

    def Envio_cuadrada_10 (self):
        if (self.s.port_open):
            self.ui.label.setText("Enviando info... duration")
            self.s.Write("duration,00,15,00,1\r\n")
            # sleep(1)
            self.ui.label.setText("Enviando info... signal")            
            self.s.Write("signal,100,100,0000,0001,0049,0001,0049,0000,0000,1\r\n")
            # self.s.Write("signal,070,070,0000,0001,0049,0001,0049,0000,0000,1\r\n")            
            # sleep(1)
            self.ui.label.setText("Enviando info... state")
            self.s.Write("state_of_stage,1,1\r\n")
            # sleep(1)
            self.ui.label.setText("Saving...")            
            self.s.Write("save,01\r\n")
            sleep(1)            
        else:
            self.ui.label.setText("Port not Open!!!")

    def Envio_cuadrada_30 (self):
        if (self.s.port_open):
            self.ui.label.setText("Enviando info... duration")
            self.s.Write("duration,00,15,00,1\r\n")
            # sleep(1)
            self.ui.label.setText("Enviando info... signal")            
            self.s.Write("signal,100,100,0000,0001,0016,0001,0015,0000,0000,1\r\n")
            # self.s.Write("signal,070,070,0000,0001,0016,0001,0015,0000,0000,1\r\n")            
            # sleep(1)
            self.ui.label.setText("Enviando info... state")
            self.s.Write("state_of_stage,1,1\r\n")
            # sleep(1)
            self.ui.label.setText("Saving...")            
            self.s.Write("save,01\r\n")
            sleep(1)            
        else:
            self.ui.label.setText("Port not Open!!!")
            
    def Envio_cuadrada_60 (self):
        if (self.s.port_open):
            self.ui.label.setText("Enviando info... duration")
            self.s.Write("duration,00,15,00,1\r\n")
            # sleep(1)
            self.ui.label.setText("Enviando info... signal")            
            self.s.Write("signal,100,100,0000,0001,0007,0001,0007,0000,0000,1\r\n")
            # self.s.Write("signal,070,070,0000,0001,0007,0001,0007,0000,0000,1\r\n")            
            # sleep(1)
            self.ui.label.setText("Enviando info... state")
            self.s.Write("state_of_stage,1,1\r\n")
            # sleep(1)
            self.ui.label.setText("Saving...")            
            self.s.Write("save,01\r\n")
            sleep(1)            
        else:
            self.ui.label.setText("Port not Open!!!")

    def Start_Treatment (self):
        if (self.s.port_open):
            self.ui.label.setText("Loading Treatment...")
            self.s.Write("load,01\r\n")
            # sleep(1)
            self.ui.label.setText("Starting Treatment...")            
            self.s.Write("start,\r\n")
            sleep(1)
        else:
            self.ui.label.setText("Port not Open!!!")

    def Stop_Treatment (self):
        if (self.s.port_open):
            self.ui.label.setText("STOP Treatment")
            self.s.Write("stop,\r\n")
            sleep(1)
        else:
            self.ui.label.setText("Port not Open!!!")

    def Pause_Treatment (self):
        if (self.s.port_open):
            self.ui.label.setText("Pausing Treatment...")
            self.s.Write("pause,\r\n")
            sleep(1)
        else:
            self.ui.label.setText("Port not Open!!!")

            
    def Get_Treatment_Conf (self):
        if (self.s.port_open):
            self.ui.label.setText("Getting Conf...")            
            self.s.Write("get all conf\r\n")
            sleep(1)
        else:
            self.ui.label.setText("Port not Open!!!")
            
            

            
    def MyObjCallback (self, dataread):
        print ("callback called!")
        d = dataread[:-1]
        self.rcv_signal.emit(d)


    def MySignalCallback (self, rcv):
        print ("signal callback!")
        self.ui.textEdit.append(rcv)



    #capturo el cierre
    def closeEvent (self, event):
        self.ui.label.setText("Closing, Please Wait...")
        self.s.Close()
        sleep(2)
        event.accept()





app = QApplication(sys.argv)
w = Dialog()
#http://doc.qt.io/qt-5/qt.html#WindowType-enum
w.setWindowFlags(Qt.CustomizeWindowHint)
# w.setWindowFlags(Qt.FramelessWindowHint)
w.show()
sys.exit(app.exec_())
