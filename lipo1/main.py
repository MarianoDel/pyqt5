import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsColorizeEffect, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QPropertyAnimation
from PyQt5.QtGui import QColor
from serialcomm import SerialComm
from treatment_class import Treatment
from timers_module import TimeoutCB

#importo UIs
from ui_lipo2 import Ui_Dialog
from ui_power import Ui_powerDialog
from ui_freq import Ui_freqDialog

#para el timer de 1 segundo
from threading import Timer
from time import time
from datetime import datetime

#### CLASE PDIALOG (ventana secundaria de seteo potencia)
class PDialog(QDialog):
    def __init__(self):
        super(PDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_powerDialog()
        self.ui.setupUi(self)

        self.intlaser = 0
        self.intled = 0

        # # # Connect up the buttons.
        self.ui.pushButton1.clicked.connect(self.UPLaser)
        self.ui.pushButton2.clicked.connect(self.DWNLaser)
        self.ui.pushButton3.clicked.connect(self.UPLED)
        self.ui.pushButton4.clicked.connect(self.DWNLED)
        # self.ui.pushButton1.pressed.connect(self.UPLaser)
        # self.ui.pushButton2.pressed.connect(self.DWNLaser)
        # self.ui.pushButton3.pressed.connect(self.UPLED)
        # self.ui.pushButton4.pressed.connect(self.DWNLED)        
        
        # # self.ui.cancelButton.clicked.connect(self.reject)
        self.ui.endButton.clicked.connect(self.accept)


    def changeChannelLabel(self, new_string):
        self.ui.whatchLabel.setText(new_string)

    def changeLaserLabel(self, new_p):
        self.intlaser = new_p
        self.ui.whatplaserLabel.setText(str(self.intlaser) + "%")

    def changeLEDLabel(self, new_p):
        self.intled = new_p
        self.ui.whatpledLabel.setText(str(self.intled) + "%")

    def UPLaser (self, event=None):
        if (self.intlaser < (100 - 5)):
            self.intlaser += 5
        else:
            self.intlaser = 100

        self.changeLaserLabel(self.intlaser)

    def DWNLaser (self, event=None):
        if (self.intlaser > 5):
            self.intlaser -= 5
        else:
            self.intlaser = 0

        self.changeLaserLabel(self.intlaser)

    def UPLED (self, event=None):
        if (self.intled < (100 - 5)):
            self.intled += 5
        else:
            self.intled = 100

        self.changeLEDLabel(self.intled)

    def DWNLED (self, event=None):
        if (self.intled > 5):
            self.intled -= 5
        else:
            self.intled = 0

        self.changeLEDLabel(self.intled)
#### FIN CLASE PDIALOG (ventana secundaria de seteo potencia)            

#### CLASE FDIALOG (ventana secundaria de seteo de frecuencia)
class FDialog(QDialog):
    def __init__(self):
        super(FDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_freqDialog()
        self.ui.setupUi(self)

        self.intfreq = 0

        # # # Connect up the buttons.
        self.ui.pushButton1.clicked.connect(self.UPFreq)
        self.ui.pushButton2.clicked.connect(self.DWNFreq)
        self.ui.endButton.clicked.connect(self.accept)


    def UPFreq (self, event=None):
        if (self.intfreq < 10):
            self.intfreq += 1

        self.changeFreqLabel(self.intfreq)

    def DWNFreq (self, event=None):
        if (self.intfreq > 1):
            self.intfreq -= 1

        self.changeFreqLabel(self.intfreq)

    def changeFreqLabel(self, new_f):
        self.intfreq = new_f
        self.ui.whatfreqLabel.setText(str(self.intfreq))
        

#### FIN CLASE FDIALOG (ventana secundaria de seteo de frecuencia)            


#### CLASE DIALOG (ventana principal)
class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        ##### DEFINES FOR CONFIGURATION #####
        # tipo de sistema donde corre el programa
        self.define_SO = 'Slackware'
        # self.define_SO = 'Raspbian'

        # uso interface de 2 o 3 botones
        # self.define_3_buttons = True
        self.define_3_buttons = False

        # es en equipo de 4 o de 8 pads
        # self.define_8_pads = False
        self.define_8_pads = True
        ##### END OF DEFINES FOR CONFIGURATION #####        
                
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


        # # Connect up the buttons.
        # self.ui.ch1Button.clicked.connect(self.channel1Button)
        # self.ui.ch2Button.clicked.connect(self.channel2Button)
        # self.ui.ch3Button.clicked.connect(self.channel3Button)
        # self.ui.ch4Button.clicked.connect(self.channel4Button)
        self.ui.ch1Button.clicked.connect(self.SetNewChannelPower)
        self.ui.ch2Button.clicked.connect(self.SetNewChannelPower)
        self.ui.ch3Button.clicked.connect(self.SetNewChannelPower)
        self.ui.ch4Button.clicked.connect(self.SetNewChannelPower)

        if self.define_8_pads:
            self.ui.ch5Button.clicked.connect(self.SetNewChannelPower)
            self.ui.ch6Button.clicked.connect(self.SetNewChannelPower)
            self.ui.ch7Button.clicked.connect(self.SetNewChannelPower)
            self.ui.ch8Button.clicked.connect(self.SetNewChannelPower)

        self.ui.powerUPButton.clicked.connect(self.SetPowerUP)
        self.ui.powerDWNButton.clicked.connect(self.SetPowerDWN)
        
        self.ui.minUPButton.clicked.connect(self.SetTimerUP)
        self.ui.minDWNButton.clicked.connect(self.SetTimerDWN)
        
        # # Connect Button Treatments
        if self.define_3_buttons:
            self.ui.pauseButton.clicked.connect(self.PauseTreatment)
        self.ui.playButton.clicked.connect(self.StartTreatment)
        self.ui.stopButton.clicked.connect(self.StopTreatment)


        # # Connect alarms Buttons
        self.ui.alarmButton_none.clicked.connect(self.SetAlarms)
        self.ui.alarmButton_one.clicked.connect(self.SetAlarms)
        self.ui.alarmButton_two.clicked.connect(self.SetAlarms)
        self.ui.alarmButton_four.clicked.connect(self.SetAlarms)

        # # Connect signals Buttons
        self.ui.cwaveButton.clicked.connect(self.SetCWAVE)
        self.ui.pulsedButton.clicked.connect(self.SetPULSED)
        self.ui.modulatedButton.clicked.connect(self.SetMODULATED)
        self.ui.freqButton.clicked.connect(self.SetFREQUENCY)

        # self.ui.enviar2.clicked.connect(self.Envio2)
        # self.ui.enviar3.clicked.connect(self.Envio3)

        if self.define_SO == 'Slackware':
            self.s = SerialComm(self.MyObjCallBack, '/dev/ttyACM0')
        elif self.define_SO == 'Raspbian':
            self.s = SerialComm(self.MyObjCallBack, '/dev/serial0')
            
        if self.s.port_open == False:
            print ("Sin puerto serie!!!")
            # self.ui.ch1Button.setText("NO!")
            self.ui.playButton.setEnabled(False)
            #sys.exit(-1)
        else:
            print ("puerto serie abierto OK!")
            # self.ui.ch1Button.setText("OK")
            #Me comunico con la placa para ponerla en stand-by
            self.s.Write("chf stop treatment\n")
            self.s.Write("chf buzzer short 1\n")


        if self.define_3_buttons:
            self.ui.pauseButton.setEnabled(False)

        if self.define_8_pads == False:
            self.ui.ch5Button.setEnabled(False)
            self.ui.ch6Button.setEnabled(False)
            self.ui.ch7Button.setEnabled(False)
            self.ui.ch8Button.setEnabled(False)
            self.ui.freqButton.setEnabled(False)
        
        self.t = Treatment()
        self.t.treatment_state = 'ENDED_OK'

        #activo el timer de 1 segundo
        self.next_call = time()
        self.t1seg = Timer(self.next_call - time(), self.UpdateOneSec, [1]).start()

#        self.timeout_1sec = ContinuousCB(1,self.UpdateOneSec)
        self.stopb_closeui = 0
        self.playcolors = 0
        self.ui.alarmButton_none.toggle()

        # self.st = QWidget.styleSheet(self.ui.playButton)
        # print (self.st)
        # self.ui.Timerlabel.raise_()    #debiera subir el string para que no quede tapado
        # self.ui.Powerlabel.raise_()    #debiera subir el string para que no quede tapado
        self.SetPowerLevel(100)
        self.SetTimerLevel(30)

        #SIGNALS
        # conecto seniales al los metodos
        self.one_second_signal.connect(self.UpdateInterfaceSlot)
        self.intermediate_timer_signal.connect(self.UpdateTimerSlot)        

        
########################
# Funciones del Modulo #
########################

    def SetPowerUP(self, event=None):
        general_power = self.t.GetGeneralPower()
        
        if (general_power < (100 - 5)):
            general_power += 5
        else:
            general_power = 100

        self.SetPowerLevel(general_power)

    def SetPowerDWN(self, event=None):
        general_power = self.t.GetGeneralPower()
        
        if (general_power > 5):
            general_power -= 5

        self.SetPowerLevel(general_power)

    def SetTimerUP(self, event=None):
        if self.t.treatment_state != 'RUNNING':
            time = int(self.ui.Timerlabel.text())
            if time < 60:
                time += 1

            self.SetTimerLevel(time)

            
    def SetTimerDWN(self, event=None):
        if self.t.treatment_state != 'RUNNING':
            time = int(self.ui.Timerlabel.text())
            if time > 1:
                time -= 1

            self.SetTimerLevel(time)

            
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
        self.t.SetGeneralPower(event)

        if self.t.treatment_state == 'RUNNING':
            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch1'))
            self.s.Write("ch1 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch1'))
            self.s.Write("ch1 power laser " + str(ch_new_power) + "\n")

            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch2'))
            self.s.Write("ch2 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch2'))
            self.s.Write("ch2 power laser " + str(ch_new_power) + "\n")

            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch3'))
            self.s.Write("ch3 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch3'))
            self.s.Write("ch3 power laser " + str(ch_new_power) + "\n")

            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch4'))
            self.s.Write("ch4 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch4'))
            self.s.Write("ch4 power laser " + str(ch_new_power) + "\n")

            if self.define_8_pads:
                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch5'))
                self.s.Write("ch5 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch5'))
                self.s.Write("ch5 power laser " + str(ch_new_power) + "\n")

                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch6'))
                self.s.Write("ch6 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch6'))
                self.s.Write("ch6 power laser " + str(ch_new_power) + "\n")

                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch7'))
                self.s.Write("ch7 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch7'))
                self.s.Write("ch7 power laser " + str(ch_new_power) + "\n")

                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch8'))
                self.s.Write("ch8 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch8'))
                self.s.Write("ch8 power laser " + str(ch_new_power) + "\n")

            
        
    def SetTimerLevel(self, event):
        if self.t.treatment_state != 'RUNNING':
            self.ui.Timerlabel.setText(str(event))
            self.SetTimerandAlarms(event, 0)
            
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

        self.ui.Timerlabel.raise_()    #debiera subir el string para que no quede tapado



    #Funcinalidad de Botones de Canales
    def SetCWAVE (self, event=None):
        self.t.signal = 'cwave'
        self.ui.freqButton.setEnabled(False)

    def SetPULSED (self, event=None):
        self.t.signal = 'pulsed'
        self.ui.freqButton.setEnabled(True)        

    def SetMODULATED (self, event=None):
        self.t.signal = 'modulated'
        self.ui.freqButton.setEnabled(True)

    def SetFREQUENCY (self, event=None):
        a = FDialog()
        a.setModal(True)
        if self.t.frequency == 0:
            a.changeFreqLabel(10)
        else:
            a.changeFreqLabel(int(self.t.frequency))
            
        a.setWindowTitle("Seteo de Frecuencia")
        a.exec_()
        new_f = a.intfreq
        if new_f == 10:
            self.t.frequency = 0
        else:
            self.t.frequency = new_f

        if self.t.treatment_state == 'RUNNING':
            self.s.Write("chf frequency " + str(self.t.frequency) + "\n")
        

    """
    chequea el boton de frecuencia y guarda el texto del mismo en el objeto treatment
    normalmente 7.83Hz
    """
    def SetNewChannelPower (self, event=None):
        sender = self.sender()

        a = PDialog()
        a.setModal(True)
        a.changeChannelLabel(sender.text())
        a.changeLaserLabel(self.t.GetLaserPower(sender.text()))
        a.changeLEDLabel(self.t.GetLedPower(sender.text()))

        a.setWindowTitle("Seteo de Potencias")
        a.exec_()

        new_power = a.ui.whatplaserLabel.text()
        # print ("canal: " + str(sender.text()) + " potencia: " + new_power)
        new_power = new_power[:-1]
        self.t.SetLaserPower(sender.text(), int(new_power))

        new_power = a.ui.whatpledLabel.text()
        # print (new_power)        
        new_power = new_power[:-1]
        self.t.SetLedPower(sender.text(), int(new_power))

        if self.t.treatment_state == 'RUNNING':
            ch_new_power = self.t.ConvertPower(self.t.GetLedPower(sender.text()))
            self.s.Write(str(sender.text()).lower() + " power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower(sender.text()))
            self.s.Write(str(sender.text()).lower() + " power laser " + str(ch_new_power) + "\n")
        
        
    #silent ending con el boton STOP
    def StopTreatment(self, event=None):
        self.s.Write("chf stop treatment\n")

        if self.t.treatment_state == 'RUNNING':
            self.t.treatment_state = 'ENDED'

        if self.t.treatment_state != 'RUNNING':
            if self.stopb_closeui > 5:
                self.close()
            elif self.stopb_closeui > 4: 
                self.stopb_closeui += 1
                self.ui.stopButton.setText(" !! ?? !!")
            else:
                self.stopb_closeui += 1
                
                

    def PauseTreatment(self, event=None):
        if self.define_3_buttons:
            if self.t.treatment_state == 'PAUSED':
                self.t.treatment_state = 'RUNNING'
                self.s.Write("chf start treatment\n")
                self.ui.playButton.setEnabled(True)
            else:
                self.s.Write("chf stop treatment\n")
                self.t.treatment_state = 'PAUSED'
                self.ui.playButton.setEnabled(False)
        else:
            if self.t.treatment_state == 'PAUSED':
                self.t.treatment_state = 'RUNNING'
                self.s.Write("chf start treatment\n")
            else:
                self.s.Write("chf stop treatment\n")
                self.t.treatment_state = 'PAUSED'


        
    def StartTreatment(self, event=None):
        #limpio contador de STOP cuando se toca play
        self.stopb_closeui = 0
        #solo ejecuto si no estaba corriendo
        if self.t.treatment_state == 'ENDED_OK':
            #mando signal type
            self.s.Write("chf signal " + self.t.signal + "\n")
            # print (self.t.signal)

            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch1'))
            self.s.Write("ch1 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch1'))
            self.s.Write("ch1 power laser " + str(ch_new_power) + "\n")

            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch2'))
            self.s.Write("ch2 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch2'))
            self.s.Write("ch2 power laser " + str(ch_new_power) + "\n")

            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch3'))
            self.s.Write("ch3 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch3'))
            self.s.Write("ch3 power laser " + str(ch_new_power) + "\n")

            ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch4'))
            self.s.Write("ch4 power led " + str(ch_new_power) + "\n")
            ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch4'))
            self.s.Write("ch4 power laser " + str(ch_new_power) + "\n")

            if self.define_8_pads:
                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch5'))
                self.s.Write("ch5 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch5'))
                self.s.Write("ch5 power laser " + str(ch_new_power) + "\n")

                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch6'))
                self.s.Write("ch6 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch6'))
                self.s.Write("ch6 power laser " + str(ch_new_power) + "\n")

                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch7'))
                self.s.Write("ch7 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch7'))
                self.s.Write("ch7 power laser " + str(ch_new_power) + "\n")

                ch_new_power = self.t.ConvertPower(self.t.GetLedPower('ch8'))
                self.s.Write("ch8 power led " + str(ch_new_power) + "\n")
                ch_new_power = self.t.ConvertPower(self.t.GetLaserPower('ch8'))
                self.s.Write("ch8 power laser " + str(ch_new_power) + "\n")
            

            ##timers intermedios
            for i in range(len(self.intermediate_timer_list)):
                self.intermediate_timer_list[i] = 0
                
            dummy = self.t.GetTreatmentAlarms()

            if (dummy != 0):
                dummy_t_secs = (self.t.GetTreatmentTimer() * 60)/ (dummy + 1)
                dummy_t_secs = dummy_t_secs
            
                for i in range (dummy):
                    self.intermediate_timer_list[i] = dummy_t_secs * (i + 1)

            ##fin timers intermedios

            #arreglo para cuando seleccionan 1 minuto
            if self.t.GetTreatmentTimer() == 1:
                # self.ui.timerSlider.setValue(0)    #esto me cambia el label
                self.ui.Timerlabel.setText("59")
                self.ui.unitlabel.setText("segundos")
                self.t.remaining_seconds = 59
                self.t.remaining_minutes = 0
            else:
                self.t.remaining_minutes = self.t.GetTreatmentTimer()
                self.t.remaining_seconds = 0


            self.s.Write("chf frequency " + str(self.t.frequency) + "\n")                
            self.s.Write("chf start treatment\n")
            self.s.Write("chf buzzer short 2\n")
            if self.define_3_buttons:
                self.ui.pauseButton.setEnabled(True)
                
            self.ui.cwaveButton.setEnabled(False)
            self.ui.pulsedButton.setEnabled(False)
            self.ui.modulatedButton.setEnabled(False)
            self.TreatmentColors()
            self.t.treatment_state = 'RUNNING'
            if self.define_3_buttons == False:
                self.ui.playButton.setText("      PAUSE");


        # puedo estar usando el programa de 2 botones
        elif self.define_3_buttons == False:
            if self.t.treatment_state == 'RUNNING' and self.ui.playButton.text() == '      PAUSE':
                self.PauseTreatment()
                self.ui.playButton.setText("   PLAY again")
            else:
                self.PauseTreatment()
                self.ui.playButton.setText("      PAUSE")


            
    def SetAlarms(self, event=None):
        dummy = 0
        if self.ui.alarmButton_none.isChecked():
            dummy = 0
        if self.ui.alarmButton_one.isChecked():
            dummy = 1
        if self.ui.alarmButton_two.isChecked():
            dummy = 2
        if self.ui.alarmButton_four.isChecked():
            dummy = 4

        #self.SetTimerandAlarms(0, dummy)
        self.t.SetTreatmentAlarms(dummy)
        
            

    def SetTimerandAlarms (self, new_timer, new_alarms):
        """ me llaman desde el slider del timer o de los botones de las alarmas """
        #if (new_timer != 0):
            #me llamaron desde el slider del timer
        self.t.SetTreatmentTimer(new_timer)

        #if (new_timer == 0):
            #me llamaron desde los Button de alarmas a traves de SetAlarm
            #self.t.SetTreatmentAlarms(new_alarms)

            
    def FinTratamiento(self):
        self.t.treatment_state = 'ENDED'
        self.s.Write("chf buzzer long 3\n")
        self.s.Write("chf stop treatment\n")


    def AlarmaIntermedia(self):
        """ la hago sonar solamente si esta corriendo, sino no suena """
        #puede trear problemas con el PAUSE
        # if self.t.treatment_state == 'RUNNING':
        #     self.s.Write("ch1 buzzer half 2\n")
        self.intermediate_timer_signal.emit()


    def UpdateOneSec(self, lapse):
        """ 
            aca tengo que resolver todo lo que se mueve 
            lo hago tipo por estados del programa con treatmet_state
        """
        self.next_call = self.next_call + 1
        #esto corre en otro thread entonces mando una senial para hacer update de la interface
        self.one_second_signal.emit()        
        #antes de volver hago la proxima llamada
        self.t1seg = Timer(self.next_call - time(), self.UpdateOneSec, [1]).start()        

        
    def UpdateInterfaceSlot (self):
        if self.t.treatment_state == 'RUNNING':

            if self.t.remaining_minutes > 0:
                #si quedan minutos todavia
                if self.t.remaining_seconds > 0:
                    self.t.remaining_seconds -= 1
                else:
                    self.t.remaining_minutes -= 1
                    self.t.remaining_seconds = 59

                #todos los segundos actualizo ui
                if self.t.remaining_minutes == 0:
                    # self.ui.timerSlider.setValue(0)
                    self.ui.Timerlabel.setText("59")
                    self.ui.unitlabel.setText("segundos")
                else:
                    # self.ui.Timerlabel.setText(str(self.t.remaining_minutes) + ":" + str(self.t.remaining_seconds))
                    self.ui.Timerlabel.setText(str('{}:{:02d}'.format(self.t.remaining_minutes, self.t.remaining_seconds)))
                    # self.ui.timerSlider.setValue(self.t.remaining_minutes)

            else:
                #estoy en el ultimo minuto ya uso el contador remaining_seconds
                if self.t.remaining_seconds > 0:
                    self.t.remaining_seconds -= 1
                else:
                    self.FinTratamiento()

                self.ui.Timerlabel.setText(str(self.t.remaining_seconds))
                #o me quedo esperando en cero el fin del tratamiento                

            #timers de alarmas intermedias
            local_remaining_secs = self.t.remaining_minutes * 60 + self.t.remaining_seconds
            for i in range(len(self.intermediate_timer_list)):
                if self.intermediate_timer_list[i] != 0 and self.intermediate_timer_list[i] > local_remaining_secs:
                    self.intermediate_timer_list[i] = 0
                    # print ("timer intermedio en segundos: %s", str(local_remaining_secs))
                    self.AlarmaIntermedia()
                    
                #final de update de tiempos

            #update de efetos
            if self.playcolors > 4:
                self.ui.playButton.setStyleSheet("background-color: rgb(114, 159, 207);")
                self.playcolors = 0
            elif self.playcolors > 3:
                self.ui.playButton.setStyleSheet("background-color: rgb(52, 101, 164);")
                self.playcolors += 1
            elif self.playcolors > 2:
                self.ui.playButton.setStyleSheet("background-color: rgb(32, 74, 135);")
                self.playcolors += 1
            elif self.playcolors > 1:
                self.ui.playButton.setStyleSheet("background-color: rgb(92, 53, 102);")
                self.playcolors += 1
            elif self.playcolors > 0:
                self.ui.playButton.setStyleSheet("background-color: rgb(117, 80, 123);")
                self.playcolors += 1
            else:
                self.ui.playButton.setStyleSheet("background-color: rgb(173, 127, 168);")
                self.playcolors += 1
                
                                
        #fin del tratamiento por timer o confirmacion de stop
        if self.t.treatment_state == 'ENDED':
            # self.ui.Timerlabel.setText(str(self.t.treatment_timer))
            # self.ui.timerSlider.setValue(self.t.treatment_timer)
            self.SetTimerLevel(self.t.treatment_timer)
            self.ui.unitlabel.setText("minutos")
            self.t.treatment_state = 'ENDED_OK'
            self.ui.cwaveButton.setEnabled(True)
            self.ui.pulsedButton.setEnabled(True)
            self.ui.modulatedButton.setEnabled(True)
            self.DefaultColors()
            if self.define_3_buttons:
                self.ui.pauseButton.setEnabled(False)
            else:
                self.ui.playButton.setText("       PLAY")


        
    def UpdateTimerSlot (self):
        if self.t.treatment_state == 'RUNNING':
            self.s.Write("chf buzzer half 2\n")
        

    def TreatmentColors (self):
        s_dummy = "QSlider::groove:vertical {\
                    background: red;\
                    position: absolute;\
                    left: 4px; right: 4px;\
                    border: 1px solid #bbb;\
                    border-radius: 4px;}\
                    QSlider::handle:vertical {\
                    height: 30px;\
                    background:rgb(84, 10, 82);\
                    margin: 0 -4px;\
                    border: 1px solid #777;\
                    border-radius: 4px;}\
                    QSlider::add-page:vertical {\
                    background:rgb(233, 31, 153);}\
                    QSlider::sub-page:vertical {\
                    background: pink;}"

        # self.ui.timerSlider.setStyleSheet(s_dummy)
        # self.ui.powerSlider.setStyleSheet(s_dummy)

        #self.ui es un puntero a mi objeto dialog, pero el propio dialogo es self        
        s_dummy = "background-color: rgb(173, 127, 168);"
        self.setStyleSheet(s_dummy)

    def DefaultColors (self):
        # s_dummy = "QSlider::groove:vertical {\
        #             background: red;\
        #             position: absolute;\
        #             left: 4px; right: 4px;\
        #             border: 1px solid #bbb;\
        #             border-radius: 4px;}\
        #             QSlider::handle:vertical {\
        #             height: 30px;\
        #             background: green;\
        #             margin: 0 -4px;\
        #             border: 1px solid #777;\
        #             border-radius: 4px;}\
        #             QSlider::add-page:vertical {\
        #             background:white;}\
        #             QSlider::sub-page:vertical {\
        #             background: pink;}"

        s_dummy = "QSlider::groove:vertical {\
                    background: red;\
                    position: absolute;\
                    left: 4px; right: 4px;\
                    border: 1px solid #bbb;\
                    border-radius: 4px;}\
                    QSlider::handle:vertical {\
                    height:30px;\
                    background: rgb(13, 10, 61);\
                    margin: 0 -4px;\
                    border: 1px solid #777;\
                    border-radius: 4px;}\
                    QSlider::add-page:vertical {\
                    background: rgb(32, 74, 135);}\
                    QSlider::sub-page:vertical {\
                    background: rgb(110, 202, 206);}"
                            
        # self.ui.timerSlider.setStyleSheet(s_dummy)
        # self.ui.powerSlider.setStyleSheet(s_dummy)

        #self.ui es un puntero a mi objeto dialog, pero el propio dialogo es self
        s_dummy = "background-color: rgb(85, 170, 127);"
        self.setStyleSheet(s_dummy)


        
# QGraphicsColorizeEffect *eEffect= new QGraphicsColorizeEffect(btn);
# btn->setGraphicsEffect(eEffect);
# QPropertyAnimation *paAnimation = new QPropertyAnimation(eEffect,"color");
# paAnimation->setStartValue(QColor(Qt::blue));
# paAnimation->setEndValue(QColor(Qt::red));
# paAnimation->setDuration(1000);
# paAnimation->start();
    #atributos generales del la clase Dialog()
    #SIGNALS
    # signals para comunicacion 1 seg
    one_second_signal = pyqtSignal()
    intermediate_timer_signal = pyqtSignal()
    intermediate_timer_list = [0, 0, 0, 0]

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
