import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from ui_lipo2 import Ui_Dialog
#from serialcomm import SerialComm

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        # # Make some local modifications.
        # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        self.ui.closeButton.clicked.connect(self.close)

        # # Connect the QSlider
        self.ui.verticalSlider.valueChanged.connect(self.SetPowerLevel)


  #      self.ui.enviar2.clicked.connect(self.Envio2)
   #     self.ui.enviar3.clicked.connect(self.Envio3)

    # def __show__(self):
#        self.s = SerialComm(self.MyObjCallBack, '/dev/ttyACM0')
 #       if self.s.port_open == False:
  #          self.ui.diag.setText("Sin puerto serie!!!")
   #         sys.exit(-1)
    #    else:
     #       self.ui.diag.setText("puerto serie abierto OK!")

## Funciones del Modulo
    def SetPowerLevel(self, event):
        self.ui.Powerlabel.setText(str(event) + "%")
        self.ui.Powerlabel.raise_()
        # print ("nuevo valor slider: " + str(event))

    def Envio1(self, event):
        self.ui.recibido.setText("env 1")
        self.s.Write("boton 1\n")

    def Envio2(self, event):
        self.ui.recibido.setText("env 2")
        self.s.Write("boton 2\n")

    def Envio3(self, event):
        self.ui.recibido.setText("env 3")
        self.s.Write("boton 3\n")

    def MyObjCallBack (self, dataread):
        print ("callback called!")
        d = dataread[:-1]
        self.ui.recibido.setText(d)

    #capturo el cierre
    def closeEvent (self, event):
 #       self.s.Close()
        event.accept()





app = QApplication(sys.argv)
w = Dialog()
w.setWindowFlags(Qt.CustomizeWindowHint)
w.showFullScreen()
w.show()
sys.exit(app.exec_())
