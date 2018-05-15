import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from ui_serial import Ui_Dialog
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
        self.ui.enviar1.clicked.connect(self.Envio1)
        self.ui.enviar2.clicked.connect(self.Envio2)
        self.ui.enviar3.clicked.connect(self.Envio3)

        #con el boton lanzo el evento close, que luego llama a closeEvent
        self.ui.closeButton.clicked.connect(self.close)

        #creo el evento y lo conecto al slot
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #Envio3 lo dispara

        #creo una senial de prueba y la conecto        
        self.rcv_signal.connect(self.MySignalCallback)

        #self.MyObjCallback la llaman desde otro thread, armo una senial
        #antes de modificar UI
        self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
        if self.s.port_open == False:
            self.ui.diag.setText("Sin puerto serie!!!")
            sys.exit(-1)
        else:
            self.ui.diag.setText("puerto serie abierto OK!")

        #customs window flags
        # self.ui.setWindowFlags(Qt.FramelessWindowHint)


    def Envio1(self, event):
        self.ui.recibido.setText("env 1")
        self.s.Write("boton 1\n")

    def Envio2(self, event):
        self.ui.recibido.setText("env 2")
        self.s.Write("boton 2\n")

    def Envio3(self, event):
        # self.ui.recibido.setText("env 3")
        # self.s.Write("boton 3\n")
        self.s.Close()
        self.c.closeApp.emit()

    def MyObjCallback (self, dataread):
        print ("callback called!")
        d = dataread[:-1]
        self.rcv_signal.emit(d)
        # self.ui.recibido.setText(d)

    def MySignalCallback (self, rcv):
        print ("signal callback!")
        self.ui.recibido.setText(rcv)


    #capturo el cierre
    def closeEvent (self, event):
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
