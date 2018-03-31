import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsColorizeEffect
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QPropertyAnimation
from PyQt5.QtGui import QColor
from ui_lipo2 import Ui_Dialog
from serialcomm import SerialComm
from treatment_class import Treatment
from timers_module import TimeoutCB

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
        self.ui.ch1Button.clicked.connect(self.channel1Button)
        # self.ui.ch2Button.pressed.connect(self.channel2Button)
        self.ui.ch2Button.clicked.connect(self.channel2Button)

        # # Connect the QSlider
        self.ui.powerSlider.valueChanged.connect(self.SetPowerLevel)
        self.ui.timerSlider.valueChanged.connect(self.SetTimerLevel)

        # # Connect Button Treatments
        self.ui.playButton.clicked.connect(self.StartTreatment)
        self.ui.stopButton.clicked.connect(self.StopTreatment)
        self.ui.pauseButton.clicked.connect(self.PauseTreatment)

        # # Connect radioButtons
        self.ui.radioButton_none.clicked.connect(self.SetAlarms)
        self.ui.radioButton_one.clicked.connect(self.SetAlarms)
        self.ui.radioButton_two.clicked.connect(self.SetAlarms)
        self.ui.radioButton_four.clicked.connect(self.SetAlarms)
        


  #      self.ui.enviar2.clicked.connect(self.Envio2)
   #     self.ui.enviar3.clicked.connect(self.Envio3)

#    def __show__(self):
        self.s = SerialComm(self.MyObjCallBack, '/dev/ttyACM0')
        if self.s.port_open == False:
            print ("Sin puerto serie!!!")
            self.ui.ch1Button.setText("NO!")
            self.ui.playButton.setEnabled(False)
            #sys.exit(-1)
        else:
            print ("puerto serie abierto OK!")
            self.ui.ch1Button.setText("OK")

        self.t = Treatment()
        self.timeout_1sec = ContinuousCB(1,self.UpdateOneSec)

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
            
        self.ui.Powerlabel.raise_()    #debiera subir el string para que no quede tapado
        self.t.SetLaserPower('ch1', event)
        self.t.SetLaserPower('ch2', event)
        self.t.SetLaserPower('ch3', event)
        self.t.SetLaserPower('ch4', event)        

        self.t.SetLedPower('ch1', event)
        self.t.SetLedPower('ch2', event)
        self.t.SetLedPower('ch3', event)
        self.t.SetLedPower('ch4', event)        
        
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

        self.SetTimerandAlarms(event, 0)


    #Funcinalidad de Botones de Canales
    def channel1Button(self, event):
        self.ui.ch1Button.setStyleSheet("background-color: red")
        self.s.Write("ch1 buzzer short 3\n")

    def channel2Button(self, event=None):
        # self.ui.ch2Button.setStyleSheet("background-color: red")
        pass
        

    def StopTreatment(self, event=None):
        self.s.Write("ch1 stop treatment\n")

    def PauseTreatment(self, event=None):
        self.s.Write("ch1 stop treatment\n")

    def SetTimerandAlarms (self, new_timer, new_alarms):
        """ me llaman desde el slider del timer o el radiocheck de alarms """
        if (new_timer != 0):
            #me llamaron desde el slider del timer
            self.t.SetTreatmentTimer(new_timer)

        if (new_timer == 0):
            #me llamaron desde los radioButton de alarmas a tarves de SetAlarm
            self.t.SetTreatmentAlarms(new_alarms)

    def SetAlarms(self, event=None):
        dummy = 0
        if self.ui.radioButton_none.isChecked():
            dummy = 0
        if self.ui.radioButton_one.isChecked():
            dummy = 1
        if self.ui.radioButton_two.isChecked():
            dummy = 2
        if self.ui.radioButton_four.isChecked():
            dummy = 4

        self.SetTimerandAlarms(0, dummy)
        
    def StartTreatment(self, event=None):        
        self.effect = QGraphicsColorizeEffect(self.ui.playButton)
        self.ui.playButton.setGraphicsEffect(self.effect)
        self.anim = QPropertyAnimation(self.effect, b"color")
        self.anim.setStartValue(QColor(Qt.blue))
        self.anim.setEndValue(QColor(Qt.darkBlue))
        self.anim.setDuration(1000)
        self.anim.start()

        ch1_new_power = self.t.ConvertPower(self.t.GetLedPower('ch1'))
        self.s.Write("ch1 power led " + str(ch1_new_power) + "\n")

        # #activo el timer de tratamiento
        # self.tratamiento = Timer(self, self.t.GetTreatmentTimer() * 60, self.FinTratamiento)
        # self.tratamiento.start()
        self.timer1 = TimeoutCB(self.t.GetTreatmentTimer() * 60, self.FinTratamiento)

        #timers intermedios
        dummy = self.t.GetTreatmentAlarms()

        if (dummy != 0):
            dummy_t_secs = self.t.GetTreatmentTimer() / (dummy + 1)
            dummy_t_secs = dummy_t_secs * 60
            
            self.objs_timer = list()

            for i in range (dummy):
                 self.objs_timer.append(TimeoutCB(dummy_t_secs * i, self.AlarmaIntermedia))

        self.t.treatment_state = 'RUNNING'
        self.t.treatment_seconds = 0
        self.t.remaining_minutes = self.t.GetTreatmentTimer()
        self.twosecs = 0
        self.s.Write("ch1 start treatment\n")
        self.s.Write("ch1 buzzer short 2\n")


    def FinTratamiento(self):
        self.t.treatment_state = 'ENDED'
        self.s.Write("ch1 buzzer long 3\n")
        self.s.Write("ch1 stop treatment\n")

    def AlarmaIntermedia(self):
        self.s.Write("ch1 buzzer half 2\n")

    def UpdateOneSec(self):
        """ aca tengo que resolver todo lo que se mueve """
        if self.twosecs < 2:
            self.twosecs += 1
        else:
            self.twosecs = 0
        
        if self.t.treatment_state == 'RUNNING':
            self.t.treatment_seconds += 1

            if self.t.treatment_seconds >= 60:
                self.t.treatment_seconds = 0

                if self.t.remaining_minutes > 0:
                    if self.t.treatment_seconds < 60:
                        self.t.treatment_seconds += 1
                    else:
                        self.t.remaining_minutes -= 1
                        self.t.treatment_seconds = 0
                        
                elif self.t.remaining_minutes == 1:
                    self.ui.Timerlabel.setText("60")
                    self.ui.unitlabel.setText("segs.")
                else:
                    self.ui.Timerlabel.setText(str(self.t.treatment_seconds))
                    

            and self.twosecs == 2:
            self.effect = QGraphicsColorizeEffect(self.ui.playButton)
            self.ui.playButton.setGraphicsEffect(self.effect)
            self.anim = QPropertyAnimation(self.effect, b"color")
            self.anim.setStartValue(QColor(Qt.blue))
            self.anim.setEndValue(QColor(Qt.darkBlue))
            self.anim.setDuration(1000)
            self.anim.start()

            

        if self.t.treatment_state == 'ENDED':
            self.ui.Timerlabel.setText(str(self.t.treatment_timer))
            self.ui.unitlabel.setText("minutos")
            self.t.treatment_state = 'ENDED_OK'
        
            
        
        
# QGraphicsColorizeEffect *eEffect= new QGraphicsColorizeEffect(btn);
# btn->setGraphicsEffect(eEffect);
# QPropertyAnimation *paAnimation = new QPropertyAnimation(eEffect,"color");
# paAnimation->setStartValue(QColor(Qt::blue));
# paAnimation->setEndValue(QColor(Qt::red));
# paAnimation->setDuration(1000);
# paAnimation->start();


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
        d = dataread[:-1]
        print (d)
        # self.ui.recibido.setText(d)

    #capturo el cierre
    def closeEvent (self, event):
 #       self.s.Close()
        event.accept()

#### FIN CLASE DIALOG (ventana principal)




app = QApplication(sys.argv)
w = Dialog()
w.setWindowFlags(Qt.CustomizeWindowHint)
w.showFullScreen()
w.show()
sys.exit(app.exec_())
