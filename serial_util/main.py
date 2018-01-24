import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_serial import Ui_Dialog
from serialcomm import SerialComm

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
        self.ui.enviar1.clicked.connect(self.Envio1)
        self.ui.enviar2.clicked.connect(self.Envio2)
        self.ui.enviar3.clicked.connect(self.Envio3)

    # def __show__(self):
        self.s = SerialComm(self.MyObjCallBack, '/dev/ttyACM0')
        if self.s.port_open == False:
            self.ui.diag.setText("Sin puerto serie!!!")
            sys.exit(-1)
        else:
            self.ui.diag.setText("puerto serie abierto OK!")


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




app = QApplication(sys.argv)
w = Dialog()
w.show()
sys.exit(app.exec_())
