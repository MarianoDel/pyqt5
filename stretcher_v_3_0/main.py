import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from serialcomm import SerialComm
from treatment_class import Treatment
from stylesheet_class import ButtonStyles
from time import sleep, time
from datetime import datetime


#para el timer de 1 segundo
from threading import Timer

#Here import the UIs or the classes that got the UIs
from ui_stretcher import Ui_Dialog
from dlg_first_cls import FirstDialog
from dlg_treat_cls import TreatmentDialog
from dlg_diags_cls import DiagnosticsDialog



"""
    Pruebas con seniales y eventos custom
    http://zetcode.com/gui/pyqt5/eventssignals/
"""

### GLOBALS FOR CONFIGURATION #########
## OS where its run
RUNNING_ON_SLACKWARE = 1
RUNNING_ON_RASP = 0
## Apply power limits to the antennas
USE_POWER_LIMIT = 1
## No calls for debug
NO_CALL_FIRST_DLG = 1

## This Interface Software version
CURRENT_VERSION = "Stretcher_ver_3_1"

### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

    # receivedData = pyqtSignal()
    





##############################
# Dialog Class - Main Window #
##############################
class Dialog(QDialog):

    rcv_signal = pyqtSignal(str)
    powerUpButtonCnt = 0
    powerDwnButtonCnt = 0
    timeUpButtonCnt = 0
    timeDwnButtonCnt = 0
    tempCnt = 0

    #SIGNALS
    # signals para comunicacion 1 seg
    one_second_signal = pyqtSignal()

    
    def __init__(self):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Class Startup Init
        ## Connect up the buttons.
        self.ui.triangularButton.clicked.connect(self.SignalChange)
        self.ui.squareButton.clicked.connect(self.SignalChange)
        self.ui.sinusoidalButton.clicked.connect(self.SignalChange)
        
        self.ui.freq1Button.clicked.connect(self.FrequencyChange)
        self.ui.freq2Button.clicked.connect(self.FrequencyChange)
        self.ui.freq3Button.clicked.connect(self.FrequencyChange)
        self.ui.freq4Button.clicked.connect(self.FrequencyChange)
        self.ui.freq5Button.clicked.connect(self.FrequencyChange)
        self.ui.freq6Button.clicked.connect(self.FrequencyChange)
        
        self.ui.ch1Button.clicked.connect(self.ChannelChange)
        self.ui.ch2Button.clicked.connect(self.ChannelChange)
        self.ui.ch3Button.clicked.connect(self.ChannelChange)

        self.ui.powerUpButton.pressed.connect(self.UpPowerPressed)
        self.ui.powerUpButton.released.connect(self.UpPowerReleased)
        self.ui.powerDwnButton.pressed.connect(self.DwnPowerPressed)
        self.ui.powerDwnButton.released.connect(self.DwnPowerReleased)
        self.ui.timeUpButton.pressed.connect(self.UpTimePressed)
        self.ui.timeUpButton.released.connect(self.UpTimeReleased)        
        self.ui.timeDwnButton.pressed.connect(self.DwnTimePressed)
        self.ui.timeDwnButton.released.connect(self.DwnTimeReleased)

        self.ui.min30Button.clicked.connect(self.TimeSet)
        self.ui.min45Button.clicked.connect(self.TimeSet)
        
        self.ui.startButton.clicked.connect(self.TreatmentScreen)
        self.ui.diagButton.clicked.connect(self.DiagnosticsScreen)

        ## Init treatment object
        self.t = Treatment()
        self.t.SetCurrentVersion(CURRENT_VERSION)

        ## Init stylesheet object
        self.ss = ButtonStyles()
        
        ## Init the default state:
        self.SignalDisableAll()
        self.FrequencyDisableAll()
        self.ui.powerLabel.setText(str(self.t.GetPower()))
        self.ui.minutesLabel.setText(str(self.t.GetTreatmentTimer()))

        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)
        
        # #con el boton lanzo el evento close, que luego llama a closeEvent
        # self.ui.closeButton.clicked.connect(self.close)
        self.ui.textEdit.setText('')

        #creo el evento y lo conecto al slot
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #Envio3 lo dispara

        #creo una senial de prueba y la conecto        
        self.rcv_signal.connect(self.MySignalCallback)

        #self.MyObjCallback la llaman desde otro thread, armo una senial
        #antes de modificar UI

        ## PARA SLACKWARE
        if RUNNING_ON_SLACKWARE:
            self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
        ## PARA RASPBERRY
        if RUNNING_ON_RASP:
            self.s = SerialComm(self.MyObjCallback, '/dev/serial0')
            
        if self.s.port_open == False:
            self.ui.textEdit.append("No serial port found!!!")
            # sys.exit(-1)
            #TODO: agregar un timer que vaya buscando el puerto!!!
        else:
            self.ui.textEdit.append("Serial port open OK!")


        #activo el timer de 1 segundo, la primera vez, luego se autollama
        self.next_call = time()
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()

        #SIGNALS
        # conecto senial del timer a la funcion de Update
        self.one_second_signal.connect(self.UpdateOneSec)

        ### For last call to the first f*** dialog
        if NO_CALL_FIRST_DLG == 0:
            self.FirstDialogScreen()


    def UpdateDateTime(self, new_date_time):
        date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
        self.ui.date_timeLabel.setText(date_str)


    def UpTimePressed (self):
        self.TimeUp (1)
        self.timeUpButtonCnt = 1

        
    def UpTimeReleased (self):
        self.timeUpButtonCnt = 0

        
    def DwnTimePressed (self):
        self.TimeDwn(1)
        self.timeDwnButtonCnt = 1

        
    def DwnTimeReleased (self):
        self.timeDwnButtonCnt = 0

        
    def UpPowerPressed (self):
        self.PwrUp (1)
        self.powerUpButtonCnt = 1

        
    def UpPowerReleased (self):
        self.powerUpButtonCnt = 0

        
    def DwnPowerPressed (self):
        self.PwrDwn(1)
        self.powerDwnButtonCnt = 1

        
    def DwnPowerReleased (self):
        self.powerDwnButtonCnt = 0

        
    def SignalDisableAll(self):
        self.ui.triangularButton.setStyleSheet(self.ss.triangular_disable)
        self.ui.squareButton.setStyleSheet(self.ss.square_disable)
        self.ui.sinusoidalButton.setStyleSheet(self.ss.sinusoidal_disable)
                       

    def SignalChange (self):
        sender = self.sender()

        self.SignalDisableAll()
        
        if sender.objectName() == 'triangularButton':
            self.ui.triangularButton.setStyleSheet(self.ss.triangular_enable)
            self.ui.textEdit.append("tringular signal selected")
            self.t.SetSignal('triangular')

        elif sender.objectName() == 'squareButton':
            self.ui.squareButton.setStyleSheet(self.ss.square_enable)
            self.ui.textEdit.append("square signal selected")            
            self.t.SetSignal('square')

        elif sender.objectName() == 'sinusoidalButton':
            self.ui.sinusoidalButton.setStyleSheet(self.ss.sinusoidal_enable)
            self.ui.textEdit.append("sinusoidal signal selected")            
            self.t.SetSignal('sinusoidal')

        self.CheckForStart()


    def FrequencyDisableAll(self):
        self.ui.freq1Button.setStyleSheet(self.ss.freq1_disable)
        self.ui.freq2Button.setStyleSheet(self.ss.freq2_disable)
        self.ui.freq3Button.setStyleSheet(self.ss.freq3_disable)
        self.ui.freq4Button.setStyleSheet(self.ss.freq4_disable)
        self.ui.freq5Button.setStyleSheet(self.ss.freq5_disable)
        self.ui.freq6Button.setStyleSheet(self.ss.freq6_disable)
        self.t.SetFrequency('None')


    def FrequencyChange (self):
        sender = self.sender()

        self.FrequencyDisableAll()
        
        if sender.objectName() == 'freq1Button':
            self.ui.freq1Button.setStyleSheet(self.ss.freq1_enable)
            self.ui.textEdit.append("7.83Hz selected")
            self.t.SetFrequency('7.83Hz')

        if sender.objectName() == 'freq2Button':
            self.ui.freq2Button.setStyleSheet(self.ss.freq2_enable)
            self.ui.textEdit.append("11.79Hz selected")            
            self.t.SetFrequency('11.79Hz')

        if sender.objectName() == 'freq3Button':
            self.ui.freq3Button.setStyleSheet(self.ss.freq3_enable)
            self.ui.textEdit.append("16.67Hz selected")            
            self.t.SetFrequency('16.67Hz')

        if sender.objectName() == 'freq4Button':
            self.ui.freq4Button.setStyleSheet(self.ss.freq4_enable)
            self.ui.textEdit.append("23.58Hz selected")            
            self.t.SetFrequency('23.58Hz')

        if sender.objectName() == 'freq5Button':
            self.ui.freq5Button.setStyleSheet(self.ss.freq5_enable)
            self.ui.textEdit.append("30.80Hz selected")            
            self.t.SetFrequency('30.80Hz')

        if sender.objectName() == 'freq6Button':
            self.ui.freq6Button.setStyleSheet(self.ss.freq6_enable)
            self.ui.textEdit.append("62.64Hz selected")            
            self.t.SetFrequency('62.64Hz')

        self.CheckForStart()
            
            
    def ChannelChange (self):
        sender = self.sender()

        if sender.objectName() == 'ch1Button':
            if self.t.GetChannelInTreatment('ch1') == False:
                self.ui.ch1Button.setStyleSheet(self.ss.ch_enable)
                self.t.EnableChannelsInTreatment('ch1')
            else:
                self.ui.ch1Button.setStyleSheet(self.ss.ch_disable)
                self.t.DisableChannelsInTreatment('ch1')

        if sender.objectName() == 'ch2Button':
            if self.t.GetChannelInTreatment('ch2') == False:
                self.ui.ch2Button.setStyleSheet(self.ss.ch_enable)
                self.t.EnableChannelsInTreatment('ch2')
            else:
                self.ui.ch2Button.setStyleSheet(self.ss.ch_disable)
                self.t.DisableChannelsInTreatment('ch2')

        if sender.objectName() == 'ch3Button':
            if self.t.GetChannelInTreatment('ch3') == False:
                self.ui.ch3Button.setStyleSheet(self.ss.ch_enable)
                self.t.EnableChannelsInTreatment('ch3')
            else:
                self.ui.ch3Button.setStyleSheet(self.ss.ch_disable)
                self.t.DisableChannelsInTreatment('ch3')

        self.CheckForStart()
        
        
    def TimeSet (self):
        sender = self.sender()
        
        if sender.objectName() == 'min30Button':
            self.ui.minutesLabel.setText('30')
            self.t.SetTreatmentTimer(30)

        elif sender.objectName() == 'min45Button':
            self.ui.minutesLabel.setText('45')
            self.t.SetTreatmentTimer(45)


    def CheckForStart (self):
        if self.CheckCompleteConf() == True:
            self.ui.startButton.setStyleSheet(self.ss.start_enable)
        else:
            self.ui.startButton.setStyleSheet(self.ss.start_disable)


    def CheckCompleteConf (self):
        if (self.t.GetFrequency() != 'None' and
            self.t.GetSignal() != 'None'):
           if (self.t.GetChannelInTreatment('ch1') != False or
               self.t.GetChannelInTreatment('ch2') != False or
               self.t.GetChannelInTreatment('ch3') != False):
               return True
           else:
               return False
        else:
            return False


    def UpdateOneSec (self):
        """ paso un segundo, reviso que tengo que hacer """
        # reviso si algun boton sigue presionado
        ## Power Buttons
        if self.powerUpButtonCnt > 3:
            self.PwrUp(10)
        elif self.powerUpButtonCnt > 1:
            self.PwrUp(5)
            self.powerUpButtonCnt += 1
        elif self.powerUpButtonCnt == 1:
            self.powerUpButtonCnt += 1

        if self.powerDwnButtonCnt > 3:
            self.PwrDwn(10)
        elif self.powerDwnButtonCnt > 1:
            self.PwrDwn(5)
            self.powerDwnButtonCnt += 1
        elif self.powerDwnButtonCnt == 1:
            self.powerDwnButtonCnt += 1

        ## Time Buttons
        if self.timeUpButtonCnt > 3:
            self.TimeUp(10)
        elif self.timeUpButtonCnt > 1:
            self.TimeUp(5)
            self.timeUpButtonCnt += 1            
        elif  self.timeUpButtonCnt == 1:
            self.timeUpButtonCnt += 1

        if self.timeDwnButtonCnt > 3:
            self.TimeDwn(10)
        elif self.timeDwnButtonCnt > 1:
            self.TimeDwn(5)
            self.timeDwnButtonCnt += 1            
        elif self.timeDwnButtonCnt == 1:
            self.timeDwnButtonCnt += 1

        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            # print(date_now)
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)            
            
                            
    def PwrUp (self, new_pwr):
        last_pwr = self.t.GetPower()
        max_pwr = self.t.max_power
        if ((last_pwr + new_pwr) < max_pwr):
            last_pwr += new_pwr
        else:
            last_pwr = max_pwr
            
        self.ui.powerLabel.setText(str(last_pwr))
        self.t.SetPower(last_pwr)

        
    def PwrDwn (self, new_pwr):
        last_pwr = self.t.GetPower()
        min_pwr = self.t.min_power
        if ((last_pwr - new_pwr) > min_pwr):
            last_pwr -= new_pwr
        else:
            last_pwr = min_pwr
            
        self.ui.powerLabel.setText(str(last_pwr))
        self.t.SetPower(last_pwr)

        
    def TimeUp (self, new_time):
        last_time = self.t.GetTreatmentTimer()
        max_time = self.t.max_treatment_timer
        if ((last_time + new_time) < max_time):
            last_time += new_time
        else:
            last_time = max_time
        self.ui.minutesLabel.setText(str(last_time))
        self.t.SetTreatmentTimer(last_time)

        
    def TimeDwn (self, new_time):
        last_time = self.t.GetTreatmentTimer()
        min_time = self.t.min_treatment_timer
        if ((last_time - new_time) > min_time):
            last_time -= new_time
        else:
            last_time = min_time
        self.ui.minutesLabel.setText(str(last_time))
        self.t.SetTreatmentTimer(last_time)

        
    def TimerOneSec(self, lapse):
        """ 
            envio seniales cada 1 segundo y vuelvo a llamar al timer
            se auto llama
        """
        self.next_call = self.next_call + 1
        self.one_second_signal.emit()        
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()        

        
    def MyObjCallback (self, dataread):
        print ("callback called!")
        d = dataread.rstrip()
        self.rcv_signal.emit(d)

        
    def MySignalCallback (self, rcv):
        print ("signal callback!")
        # self.ui.textEdit.append(rcv)
        # reviso si es un final de tratamiento
        # if rcv.startswith("treat end,") or rcv.startswith("treat err,"):
        if rcv.startswith("STOP") or rcv.startswith("finish,"):
        
            if self.t.treatment_state == 'START':
                # termino el tratamiento, hago algo parecido al boton stop
                self.t.treatment_state = 'STOP'
                self.EnableForTreatment()
                self.ui.textEdit.append("Ended or Stopped Treatment")
                # self.s.Write("stop,\r\n")
                sleep(1)

        elif rcv.startswith("temp,"):
            # incremento un contador y lo muestro cada tanto, 10min aprox.
            if self.tempCnt == 0 or self.tempCnt >= 600:
                self.tempCnt = 0
                self.ui.textEdit.append(rcv)

            self.tempCnt = self.tempCnt + 1

        else:
            # el resto de los mensajes los paso directo a la pantalla
            self.ui.textEdit.append(rcv)
                
                          
    #capturo el cierre
    def closeEvent (self, event):
        self.ui.textEdit.append("Closing, Please Wait...")
        self.s.Close()
        sleep(2)
        event.accept()


    ## Initial Screen
    def FirstDialogScreen (self):
        a = FirstDialog()
        a.setModal(True)
        a.exec_()

        
    ## Treatment Screen
    def TreatmentScreen (self):
        if self.CheckCompleteConf() == True:
            a = TreatmentDialog(self.t, self.ss, self.s)
            a.setModal(True)
            a.exec_()
        else:
            self.ui.textEdit.append("Complete all params before start")


    ## DiagnosticsSreen
    def DiagnosticsScreen (self):
        print("diag button presed!!!")
        a = DiagnosticsDialog(self.s, self.t)
        a.setModal(True)
        a.exec_()

        

### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
w = Dialog()
#http://doc.qt.io/qt-5/qt.html#WindowType-enum
w.setWindowFlags(Qt.CustomizeWindowHint)
# w.setWindowFlags(Qt.FramelessWindowHint)
w.show()
sys.exit(app.exec_())


### End of File ###
