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
        self.ui.pLevel125.setDisabled(True)
        self.ui.pLevel250.setDisabled(True)
        self.ui.pLevel375.setDisabled(True)
        self.ui.pLevel500.setDisabled(True)
        self.ui.pLevel625.setDisabled(True)
        self.ui.pLevel750.setDisabled(True)
        self.ui.pLevel875.setDisabled(True)
        self.ui.pLevel1000.setDisabled(True)

        self.ui.m75.setDisabled(True)
        self.ui.m150.setDisabled(True)
        self.ui.m225.setDisabled(True)
        self.ui.m300.setDisabled(True)
        self.ui.m375.setDisabled(True)
        self.ui.m450.setDisabled(True)
        self.ui.m525.setDisabled(True)
        self.ui.m600.setDisabled(True)


        # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        self.ui.closeButton.clicked.connect(self.close)

        # # Connect the QSlider
        self.ui.powerSlider.valueChanged.connect(self.SetPowerLevel)
        self.ui.timerSlider.valueChanged.connect(self.SetTimerLevel)


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
        if (event == 100):
            self.ui.pLevel1000.setEnabled(True)
            self.ui.pLevel875.setEnabled(True)
            self.ui.pLevel750.setEnabled(True)
            self.ui.pLevel625.setEnabled(True)
            self.ui.pLevel500.setEnabled(True)
            self.ui.pLevel375.setEnabled(True)
            self.ui.pLevel250.setEnabled(True)
            self.ui.pLevel125.setEnabled(True)
        elif(event > 87):
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setEnabled(True)
            self.ui.pLevel750.setEnabled(True)
            self.ui.pLevel625.setEnabled(True)
            self.ui.pLevel500.setEnabled(True)
            self.ui.pLevel375.setEnabled(True)
            self.ui.pLevel250.setEnabled(True)
            self.ui.pLevel125.setEnabled(True)
        elif(event > 75):
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setDisabled(True)
            self.ui.pLevel750.setEnabled(True)
            self.ui.pLevel625.setEnabled(True)
            self.ui.pLevel500.setEnabled(True)
            self.ui.pLevel375.setEnabled(True)
            self.ui.pLevel250.setEnabled(True)
            self.ui.pLevel125.setEnabled(True)
        elif(event > 62):
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setDisabled(True)
            self.ui.pLevel750.setDisabled(True)
            self.ui.pLevel625.setEnabled(True)
            self.ui.pLevel500.setEnabled(True)
            self.ui.pLevel375.setEnabled(True)
            self.ui.pLevel250.setEnabled(True)
            self.ui.pLevel125.setEnabled(True)
        elif(event > 50):
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setDisabled(True)
            self.ui.pLevel750.setDisabled(True)
            self.ui.pLevel625.setDisabled(True)
            self.ui.pLevel500.setEnabled(True)
            self.ui.pLevel375.setEnabled(True)
            self.ui.pLevel250.setEnabled(True)
            self.ui.pLevel125.setEnabled(True)
        elif(event > 37):
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setDisabled(True)
            self.ui.pLevel750.setDisabled(True)
            self.ui.pLevel625.setDisabled(True)
            self.ui.pLevel500.setDisabled(True)
            self.ui.pLevel375.setEnabled(True)
            self.ui.pLevel250.setEnabled(True)
            self.ui.pLevel125.setEnabled(True)
        elif(event > 25):
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setDisabled(True)
            self.ui.pLevel750.setDisabled(True)
            self.ui.pLevel625.setDisabled(True)
            self.ui.pLevel500.setDisabled(True)
            self.ui.pLevel375.setDisabled(True)
            self.ui.pLevel250.setEnabled(True)
            self.ui.pLevel125.setEnabled(True)
        elif(event > 12):
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setDisabled(True)
            self.ui.pLevel750.setDisabled(True)
            self.ui.pLevel625.setDisabled(True)
            self.ui.pLevel500.setDisabled(True)
            self.ui.pLevel375.setDisabled(True)
            self.ui.pLevel250.setDisabled(True)
            self.ui.pLevel125.setEnabled(True)
        else:
            self.ui.pLevel1000.setDisabled(True)
            self.ui.pLevel875.setDisabled(True)
            self.ui.pLevel750.setDisabled(True)
            self.ui.pLevel625.setDisabled(True)
            self.ui.pLevel500.setDisabled(True)
            self.ui.pLevel375.setDisabled(True)
            self.ui.pLevel250.setDisabled(True)
            self.ui.pLevel125.setDisabled(True)
        self.ui.Powerlabel.raise_()

    def SetTimerLevel(self, event):
        self.ui.Timerlabel.setText(str(event))
        if (event == 60):
            self.ui.m600.setEnabled(True)
            self.ui.m525.setEnabled(True)
            self.ui.m450.setEnabled(True)
            self.ui.m375.setEnabled(True)
            self.ui.m300.setEnabled(True)
            self.ui.m225.setEnabled(True)
            self.ui.m150.setEnabled(True)
            self.ui.m75.setEnabled(True)
        elif(event > 52):
            self.ui.m600.setDisabled(True)
            self.ui.m525.setEnabled(True)
            self.ui.m450.setEnabled(True)
            self.ui.m375.setEnabled(True)
            self.ui.m300.setEnabled(True)
            self.ui.m225.setEnabled(True)
            self.ui.m150.setEnabled(True)
            self.ui.m75.setEnabled(True)
        elif(event > 45):
            self.ui.m600.setDisabled(True)
            self.ui.m525.setDisabled(True)
            self.ui.m450.setEnabled(True)
            self.ui.m375.setEnabled(True)
            self.ui.m300.setEnabled(True)
            self.ui.m225.setEnabled(True)
            self.ui.m150.setEnabled(True)
            self.ui.m75.setEnabled(True)
        elif(event > 37):
            self.ui.m600.setDisabled(True)
            self.ui.m525.setDisabled(True)
            self.ui.m450.setDisabled(True)
            self.ui.m375.setEnabled(True)
            self.ui.m300.setEnabled(True)
            self.ui.m225.setEnabled(True)
            self.ui.m150.setEnabled(True)
            self.ui.m75.setEnabled(True)
        elif(event > 30):
            self.ui.m600.setDisabled(True)
            self.ui.m525.setDisabled(True)
            self.ui.m450.setDisabled(True)
            self.ui.m375.setDisabled(True)
            self.ui.m300.setEnabled(True)
            self.ui.m225.setEnabled(True)
            self.ui.m150.setEnabled(True)
            self.ui.m75.setEnabled(True)
        elif(event > 22):
            self.ui.m600.setDisabled(True)
            self.ui.m525.setDisabled(True)
            self.ui.m450.setDisabled(True)
            self.ui.m375.setDisabled(True)
            self.ui.m300.setDisabled(True)
            self.ui.m225.setEnabled(True)
            self.ui.m150.setEnabled(True)
            self.ui.m75.setEnabled(True)
        elif(event > 15):
            self.ui.m600.setDisabled(True)
            self.ui.m525.setDisabled(True)
            self.ui.m450.setDisabled(True)
            self.ui.m375.setDisabled(True)
            self.ui.m300.setDisabled(True)
            self.ui.m225.setDisabled(True)
            self.ui.m150.setEnabled(True)
            self.ui.m75.setEnabled(True)
        elif(event > 7):
            self.ui.m600.setDisabled(True)
            self.ui.m525.setDisabled(True)
            self.ui.m450.setDisabled(True)
            self.ui.m375.setDisabled(True)
            self.ui.m300.setDisabled(True)
            self.ui.m225.setDisabled(True)
            self.ui.m150.setDisabled(True)
            self.ui.m75.setEnabled(True)
        else:
            self.ui.m600.setDisabled(True)
            self.ui.m525.setDisabled(True)
            self.ui.m450.setDisabled(True)
            self.ui.m375.setDisabled(True)
            self.ui.m300.setDisabled(True)
            self.ui.m225.setDisabled(True)
            self.ui.m150.setDisabled(True)
            self.ui.m75.setDisabled(True)







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
