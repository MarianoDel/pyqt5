import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from serialcomm import SerialComm
from treatment_class import Treatment
from stylesheet_class import ButtonStyles
from time import sleep, time
from datetime import datetime
from get_distro import GetDistroName as get_distro_name
from get_distro import GetDistroVersion as get_distro_version


#para el timer de 1 segundo
from threading import Timer


"""
        GUI for Stretcher
        Select if its running on Slackware or Raspberry
        Select the type of date-time
        Select the version of the GUI:
            - 3.2 have two more buttons for up-dwn auto or manual
            - 3.1 original
"""

### GLOBALS FOR CONFIGURATION #########
## What version of UI we must run
RUN_VER_3_2 = 1
RUN_VER_3_1 = 0
## No call the first Dialog - code empty presentation page -
NO_CALL_FIRST_DLG = 0
## For debug mock serial port instance
# DEBUG_MOCK_SERIAL_INSTANCE = True
DEBUG_MOCK_SERIAL_INSTANCE = False


#Here import the UIs or the classes that got the UIs
if RUN_VER_3_2:
    from ui_stretcher32 import Ui_Dialog
    CURRENT_VERSION = "Stretcher_ver_3_2"
elif RUN_VER_3_1:
    from ui_stretcher31 import Ui_Dialog
    CURRENT_VERSION = "Stretcher_ver_3_1"
else:
    print('Please select the UI version to run!!!')
    CURRENT_VERSION = "Stretcher_unknown"
    sys.exit()

if DEBUG_MOCK_SERIAL_INSTANCE == True:
    from  serialcomm_mock import SerialCommMock

    
from dlg_treat_cls import TreatmentDialog
from diagnostics_cls import DiagnosticsDialog
from dlg_mems_cls import MemoryDialog
from first_dialog_cls import FirstDialog
from screen_saver_cls import ScreenSaverDialog
from wifi_enable_cls import WiFiDialog

#get the code for manager
from wifi_thread_manager import WiFiThreadManager


### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

    

##############################
# Dialog Class - Main Window #
##############################
class Dialog(QDialog):

    #SIGNALS
    rcv_signal = pyqtSignal(str)
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

        if RUN_VER_3_2:
            self.ui.upDwnAutoButton.clicked.connect(self.UpDwnStretcherChange)
            self.ui.upDwnButton.clicked.connect(self.UpDwnStretcherChange)
        
        self.ui.powerUpButton.pressed.connect(self.UpPowerPressed)
        self.ui.powerUpButton.released.connect(self.UpPowerReleased)
        self.ui.powerDwnButton.pressed.connect(self.DwnPowerPressed)
        self.ui.powerDwnButton.released.connect(self.DwnPowerReleased)
        self.ui.timeUpButton.pressed.connect(self.UpTimePressed)
        self.ui.timeUpButton.released.connect(self.UpTimeReleased)        
        self.ui.timeDwnButton.pressed.connect(self.DwnTimePressed)
        self.ui.timeDwnButton.released.connect(self.DwnTimeReleased)

        self.ui.mem1Button.pressed.connect(self.Memory1Pressed)
        self.ui.mem1Button.released.connect(self.Memory1Released)
        self.ui.mem2Button.pressed.connect(self.Memory2Pressed)
        self.ui.mem2Button.released.connect(self.Memory2Released)
        self.ui.mem3Button.pressed.connect(self.Memory3Pressed)
        self.ui.mem3Button.released.connect(self.Memory3Released)
        
        self.ui.min30Button.clicked.connect(self.TimeSet)
        self.ui.min45Button.clicked.connect(self.TimeSet)
        
        self.ui.startButton.clicked.connect(self.TreatmentScreen)
        # self.ui.diagButton.clicked.connect(self.DiagnosticsScreen)
        self.ui.diagButton.pressed.connect(self.DiagsPressed)
        self.ui.diagButton.released.connect(self.DiagsReleased)

        # connect wifi button
        self.ui.wifiButton.clicked.connect(self.WifiScreen)

        ## Init treatment object
        self.t = Treatment()

        self.distro = self.GetDistroName(True)
        print (self.distro)        
        
        self.t.SetCurrentVersion(CURRENT_VERSION)
        self.t.SetCurrentSystem(self.distro)
                
        ## Init stylesheet object
        self.ss = ButtonStyles()
        
        ## Init the default state:
        self.SignalDisableAll()
        self.FrequencyDisableAll()
        self.ui.powerLabel.setText(str(self.t.GetPower()))
        self.ui.minutesLabel.setText(str(self.t.GetTreatmentTimer()))

        if RUN_VER_3_2:
            self.t.SetUpDwnStretcher(True)
            self.ui.upDwnButton.setStyleSheet(self.ss.ch_disable)
            self.ui.upDwnAutoButton.setStyleSheet(self.ss.ch_enable)
        

        ## to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)
        
        # #con el boton lanzo el evento close, que luego llama a closeEvent
        # self.ui.closeButton.clicked.connect(self.close)
        self.ui.textEdit.setText('')

        #creo el evento y lo conecto al slot
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #Envio3 lo dispara

        ## connect with serial data rx signal
        self.rcv_signal.connect(self.MySignalCallback)

        ## counters for buttons with press release functionality
        self.powerUpButtonCnt = 0
        self.powerDwnButtonCnt = 0
        self.timeUpButtonCnt = 0
        self.timeDwnButtonCnt = 0
        self.mem1ButtonCnt = 0
        self.mem2ButtonCnt = 0
        self.mem3ButtonCnt = 0
        self.diagButtonCnt = 0
        self.upDwnButtonCnt = 0

        if DEBUG_MOCK_SERIAL_INSTANCE == True:
            self.s = SerialCommMock(self.MyObjCallback, '/dev/ttyUSB0')
        else:
            ## PARA SLACKWARE
            if self.t.GetCurrentSystem() == 'Slackware ':
                # self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
                self.s = SerialComm(self.MyObjCallback, '/dev/ttyUSB0')
            ## PARA RASPBERRY
            elif self.t.GetCurrentSystem() == 'debian':
                self.s = SerialComm(self.MyObjCallback, '/dev/serial0')
            
        if self.s.port_open == False:
            self.ui.textEdit.append("No serial port found!!!")
            # sys.exit(-1)
            #TODO: agregar un timer que vaya buscando el puerto!!!
        else:
            self.InsertLocalText("Serial port open OK!")
            self.InsertLocalTextNoNewLine("\nComm with Power: ")
            self.s.Write("keepalive,\r\n")


        ## setup antennas icons
        ## url(:/buttons/resources/Stop.png)
        self.wifi_act_Icon = QIcon(':/buttons/resources/wifi-symbol_act.png')
        self.wifi_err_Icon = QIcon(':/buttons/resources/wifi-symbol_err.png')
        self.wifi_disa_Icon = QIcon(':/buttons/resources/wifi-symbol_disa.png')
        self.wifi_emit_Icon = QIcon(':/buttons/resources/wifi-symbol_emit.png')

        # start manager background process
        self.wifi_manager_cnt = 2
        self.MyThread = WiFiThreadManager()
        self.MyThread.start()

        ## activate the 1 second timer it is repetitive
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        # screen saver timer activation
        self.timer_screensaver = self.t.timeout_screensaver
        self.screensaver_window = True
            
        #SIGNALS CONNECTION
        # conecto senial del timer a la funcion de Update
        self.one_second_signal.connect(self.UpdateOneSec)

        ## read and update memory buttons
        self.UpdateMemLabels()

        ### For last call to the first f*** dialog
        if NO_CALL_FIRST_DLG == 0:
            self.FirstDialogScreen()


    def GetDistroName (self, show=False):
        distname = get_distro_name()
        version = get_distro_version()
        if show:
            os_text = "--" + distname + version + "-- "
            print("os: " + os_text)

        return distname
            

    def UpdateDateTime(self, new_date_time):
        date_str = ""
        if self.t.GetLocalization() == 'usa':
            date_str = new_date_time.strftime("%m/%d/%Y - %H:%M")
        elif self.t.GetLocalization() == 'arg':
            date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
            
        self.ui.date_timeLabel.setText(date_str)


    def UpTimePressed (self):
        self.TimeUp (1)
        self.timeUpButtonCnt = 1
        self.ScreenSaverKick()

        
    def UpTimeReleased (self):
        self.timeUpButtonCnt = 0

        
    def DwnTimePressed (self):
        self.TimeDwn(1)
        self.timeDwnButtonCnt = 1
        self.ScreenSaverKick()

        
    def DwnTimeReleased (self):
        self.timeDwnButtonCnt = 0

        
    def UpPowerPressed (self):
        self.PwrUp (1)
        self.powerUpButtonCnt = 1
        self.ScreenSaverKick()

        
    def UpPowerReleased (self):
        self.powerUpButtonCnt = 0

        
    def DwnPowerPressed (self):
        self.PwrDwn(1)
        self.powerDwnButtonCnt = 1
        self.ScreenSaverKick()

        
    def DwnPowerReleased (self):
        self.powerDwnButtonCnt = 0

        
    def Memory1Pressed (self):
        self.mem1ButtonCnt = 1
        self.ScreenSaverKick()

        
    def Memory1Released (self):
        if (self.mem1ButtonCnt > 0 and
            self.mem1ButtonCnt < 3):
            self.mem1ButtonCnt = 0
            
            #get memory values
            if self.t.mem1_treat_time == 'None':
                self.InsertLocalText("Not much to do with memory1!")
            else:
                self.SignalChangeTo(self.t.mem1_signal)
                self.FrequencyChangeTo(self.t.mem1_frequency)
                self.ui.minutesLabel.setText(self.t.mem1_treat_time)
                self.t.SetTreatmentTimer(int(self.t.mem1_treat_time))
                self.ui.powerLabel.setText(self.t.mem1_power)
                self.t.SetPower(int(self.t.mem1_power))
                self.CheckForStart()


    def Memory1Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem1')
        else:
            self.InsertLocalText("Select all parameters first!")


    def Memory2Pressed (self):
        self.mem2ButtonCnt = 1
        self.ScreenSaverKick()
        
        
    def Memory2Released (self):
        if (self.mem2ButtonCnt > 0 and
            self.mem2ButtonCnt < 3):
            self.mem2ButtonCnt = 0
            
            #get memory values
            if self.t.mem2_treat_time == 'None':
                self.InsertLocalText("Not much to do with memory2!")
            else:
                self.SignalChangeTo(self.t.mem2_signal)
                self.FrequencyChangeTo(self.t.mem2_frequency)
                self.ui.minutesLabel.setText(self.t.mem2_treat_time)
                self.t.SetTreatmentTimer(int(self.t.mem2_treat_time))
                self.ui.powerLabel.setText(self.t.mem2_power)
                self.t.SetPower(int(self.t.mem2_power))
                self.CheckForStart()


    def Memory2Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem2')
        else:
            self.InsertLocalText("Select all parameters first!")


    def Memory3Pressed (self):
        self.mem3ButtonCnt = 1
        self.ScreenSaverKick()

        
    def Memory3Released (self):
        if (self.mem3ButtonCnt > 0 and
            self.mem3ButtonCnt < 3):
            self.mem3ButtonCnt = 0
            
            #get memory values
            if self.t.mem3_treat_time == 'None':
                self.InsertLocalText("Not much to do with memory3!")
            else:
                self.SignalChangeTo(self.t.mem3_signal)
                self.FrequencyChangeTo(self.t.mem3_frequency)
                self.ui.minutesLabel.setText(self.t.mem3_treat_time)
                self.t.SetTreatmentTimer(int(self.t.mem3_treat_time))
                self.ui.powerLabel.setText(self.t.mem3_power)
                self.t.SetPower(int(self.t.mem3_power))
                self.CheckForStart()


    def Memory3Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem3')
        else:
            self.InsertLocalText("Select all parameters first!")


    def DiagsPressed (self):
        self.diagButtonCnt = 1

        
    def DiagsReleased (self):
        self.diagButtonCnt = 0

            
    def SignalDisableAll(self):
        self.ui.triangularButton.setStyleSheet(self.ss.triangular_disable)
        self.ui.squareButton.setStyleSheet(self.ss.square_disable)
        self.ui.sinusoidalButton.setStyleSheet(self.ss.sinusoidal_disable)
                       

    def SignalChange (self):
        sender = self.sender()

        if sender.objectName() == 'triangularButton':
            self.SignalChangeTo('triangular')

        elif sender.objectName() == 'squareButton':
            self.SignalChangeTo('square')

        elif sender.objectName() == 'sinusoidalButton':
            self.SignalChangeTo('sinusoidal')

        self.CheckForStart()
        self.ScreenSaverKick()

        
    def SignalChangeTo (self, new_signal):
        self.SignalDisableAll()
        
        if new_signal == 'triangular':
            self.ui.triangularButton.setStyleSheet(self.ss.triangular_enable)
            self.InsertLocalText("tringular signal selected")
            self.t.SetSignal('triangular')

        elif new_signal == 'square':
            self.ui.squareButton.setStyleSheet(self.ss.square_enable)
            self.InsertLocalText("square signal selected")            
            self.t.SetSignal('square')

        elif new_signal == 'sinusoidal':
            self.ui.sinusoidalButton.setStyleSheet(self.ss.sinusoidal_enable)
            self.InsertLocalText("sinusoidal signal selected")            
            self.t.SetSignal('sinusoidal')
        

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

        if sender.objectName() == 'freq1Button':
            self.FrequencyChangeTo('7.83Hz')

        if sender.objectName() == 'freq2Button':
            self.FrequencyChangeTo('11.79Hz')

        if sender.objectName() == 'freq3Button':
            self.FrequencyChangeTo('16.67Hz')

        if sender.objectName() == 'freq4Button':
            self.FrequencyChangeTo('23.58Hz')

        if sender.objectName() == 'freq5Button':
            self.FrequencyChangeTo('30.80Hz')

        if sender.objectName() == 'freq6Button':
            self.FrequencyChangeTo('62.64Hz')

        self.CheckForStart()
        self.ScreenSaverKick()


    def FrequencyChangeTo (self, new_freq):
        self.FrequencyDisableAll()
        
        if new_freq == '7.83Hz':
            self.ui.freq1Button.setStyleSheet(self.ss.freq1_enable)
            self.InsertLocalText("7.83Hz selected")
            self.t.SetFrequency('7.83Hz')

        if new_freq == '11.79Hz':
            self.ui.freq2Button.setStyleSheet(self.ss.freq2_enable)
            self.InsertLocalText("11.79Hz selected")            
            self.t.SetFrequency('11.79Hz')

        if new_freq == '16.67Hz':
            self.ui.freq3Button.setStyleSheet(self.ss.freq3_enable)
            self.InsertLocalText("16.67Hz selected")            
            self.t.SetFrequency('16.67Hz')

        if new_freq == '23.58Hz':
            self.ui.freq4Button.setStyleSheet(self.ss.freq4_enable)
            self.InsertLocalText("23.58Hz selected")            
            self.t.SetFrequency('23.58Hz')

        if new_freq == '30.80Hz':
            self.ui.freq5Button.setStyleSheet(self.ss.freq5_enable)
            self.InsertLocalText("30.80Hz selected")            
            self.t.SetFrequency('30.80Hz')

        if new_freq == '62.64Hz':
            self.ui.freq6Button.setStyleSheet(self.ss.freq6_enable)
            self.InsertLocalText("62.64Hz selected")            
            self.t.SetFrequency('62.64Hz')

            
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
        self.ScreenSaverKick()

        
    def UpDwnStretcherChange (self):
        sender = self.sender()

        if sender.objectName() == 'upDwnAutoButton':
            if self.t.GetUpDwnStretcher() == True:
                self.t.SetUpDwnStretcher(False)
                self.ui.upDwnButton.setStyleSheet(self.ss.ch_enable)
                self.ui.upDwnAutoButton.setStyleSheet(self.ss.ch_disable)                

                if self.s.port_open == True:
                    self.s.Write("stretcher autoup off\r\n")
                else:
                    self.InsertLocalText("Serial Port Not Open!")

            else:
                self.t.SetUpDwnStretcher(True)
                self.ui.upDwnButton.setStyleSheet(self.ss.ch_disable)
                self.ui.upDwnAutoButton.setStyleSheet(self.ss.ch_enable)

                if self.s.port_open == True:
                    self.s.Write("stretcher autoup on\r\n")
                else:
                    self.InsertLocalText("Serial Port Not Open!")

        if sender.objectName() == 'upDwnButton':
            if self.t.GetUpDwnStretcher() == False and \
               self.upDwnButtonCnt == 0:
                if self.s.port_open == True:
                    self.s.Write("stretcher up\r\n")
                    self.upDwnButtonCnt = 1
                else:
                    self.InsertLocalText("Serial Port Not Open!")

        self.ScreenSaverKick()
                    
        
    def TimeSet (self):
        sender = self.sender()
        
        if sender.objectName() == 'min30Button':
            self.ui.minutesLabel.setText('30')
            self.t.SetTreatmentTimer(30)

        elif sender.objectName() == 'min45Button':
            self.ui.minutesLabel.setText('45')
            self.t.SetTreatmentTimer(45)

        self.ScreenSaverKick()        


    def CheckForStart (self):
        if (self.CheckCompleteConf() == True and
            self.s.port_open == True):
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

        if self.mem1ButtonCnt > 3:
            self.mem1ButtonCnt = 0
            self.Memory1Config()
        elif self.mem1ButtonCnt > 0:
            self.mem1ButtonCnt += 1

        if self.mem2ButtonCnt > 3:
            self.mem2ButtonCnt = 0
            self.Memory2Config()
        elif self.mem2ButtonCnt > 0:
            self.mem2ButtonCnt += 1

        if self.mem3ButtonCnt > 3:
            self.mem3ButtonCnt = 0
            self.Memory3Config()
        elif self.mem3ButtonCnt > 0:
            self.mem3ButtonCnt += 1

        if self.diagButtonCnt > 5:
            self.diagButtonCnt = 0
            self.DiagnosticsScreen()
        elif self.diagButtonCnt > 0:
            self.diagButtonCnt += 1

        #button debouncing
        if self.upDwnButtonCnt:
            self.upDwnButtonCnt -= 1

        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            # print(date_now)
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)

        # check for screensaver activation
        if self.screensaver_window == True:
            if self.timer_screensaver > 0:
                self.timer_screensaver -= 1
            else:
                self.ScreenSaverDialogScreen()

        # check for wifi manager
        if self.wifi_manager_cnt == 0:
            self.wifi_manager_cnt = 2
            self.UpdateTwoSec()
        else:
            self.wifi_manager_cnt -= 1
            
                            
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

        
    def TimerOneSec(self):
        self.one_second_signal.emit()        

        
    def MyObjCallback (self, dataread):
        d = dataread.rstrip()
        self.rcv_signal.emit(d)

        
    def MySignalCallback (self, rcv):
        print ("signal callback!")
        self.InsertForeingText(rcv)
                

    def InsertLocalText (self, new_text):
        self.ui.textEdit.setTextColor(QColor(255, 0, 0))
        self.ui.textEdit.append(new_text)

        
    def InsertLocalTextNoNewLine (self, new_text):
        self.ui.textEdit.setTextColor(QColor(255, 0, 0))
        # new_text = new_text.rsplit('\r\n')
        self.ui.textEdit.insertPlainText(new_text)
        
        
    def InsertForeingText (self, new_text):
        self.ui.textEdit.setTextColor(QColor(0, 255, 0))
        self.ui.textEdit.append(new_text)

        
    def InsertForeingTextNoNewLine (self, new_text):
        self.ui.textEdit.setTextColor(QColor(0, 255, 0))
        self.ui.textEdit.insertPlainText(new_text)
        

    def UpdateMemLabels (self):
        if self.t.mem1_treat_time != 'None':
            self.ui.mem11Label.setText(self.t.mem1_treat_time + 'min')
            self.ui.mem12Label.setText(self.t.mem1_frequency + ' - ' + self.t.mem1_power + '%')
            self.ui.mem13Label.setText((self.t.mem1_signal).capitalize())
        else:
            self.ui.mem11Label.setText('Empty')
            self.ui.mem12Label.setText('')
            self.ui.mem13Label.setText('')
        
        if self.t.mem2_treat_time != 'None':
            self.ui.mem21Label.setText(self.t.mem2_treat_time + 'min')
            self.ui.mem22Label.setText(self.t.mem2_frequency + ' - ' + self.t.mem2_power + '%')
            self.ui.mem23Label.setText((self.t.mem2_signal).capitalize())
        else:
            self.ui.mem21Label.setText('Empty')
            self.ui.mem22Label.setText('')
            self.ui.mem23Label.setText('')

        if self.t.mem3_treat_time != 'None':
            self.ui.mem31Label.setText(self.t.mem3_treat_time + 'min')
            self.ui.mem32Label.setText(self.t.mem3_frequency + ' - ' + self.t.mem3_power + '%')
            self.ui.mem33Label.setText((self.t.mem3_signal).capitalize())
        else:
            self.ui.mem31Label.setText('Empty')
            self.ui.mem32Label.setText('')
            self.ui.mem33Label.setText('')
            

    def UpdateTwoSec (self):
        new_status = self.MyThread.GetStatus()

        if new_status == 'NO CONN':
            self.ui.wifiButton.setIcon(self.wifi_disa_Icon)
        elif new_status == 'IP':
            self.ui.wifiButton.setIcon(self.wifi_err_Icon)
        elif new_status == 'PING':
            self.ui.wifiButton.setIcon(self.wifi_act_Icon)
        elif new_status == 'TUNNEL':
            self.ui.wifiButton.setIcon(self.wifi_emit_Icon)

            
    #capturo el cierre
    def closeEvent (self, event):
        self.ui.textEdit.append("Closing, Please Wait...")
        self.s.Close()
        # sleep(2)
        event.accept()

        
####################################
# Different Screens Calls are here #
####################################

    ## Initial Screen
    def FirstDialogScreen (self):
        self.screensaver_window = False
        a = FirstDialog('stretcher', self.t.GetLocalization(), self.t.timeout_screensaver)
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()
        self.screensaver_window = True

        
    ## Treatment Screen
    def TreatmentScreen (self):
        if self.CheckCompleteConf() == True:
            if self.s.port_open == True:
                self.screensaver_window = False
                
                self.t.treatment_state = 'STOP'    #para un buen arranque la llamo con estado de stop
            
                a = TreatmentDialog(self.t, self.ss, self.s, parent=self)
                a.setModal(True)
                a.exec_()

                self.ScreenSaverKick()
                self.screensaver_window = True
                
            else:
                self.InsertLocalText("Serial Port Not Open!")
                
        else:
            # self.ui.textEdit.append("Complete all params before start")
            self.InsertLocalText("Complete all params before start")


    ## DiagnosticsSreen
    def DiagnosticsScreen (self):
        self.screensaver_window = False
        
        a = DiagnosticsDialog(self.s, self.t, parent=self)
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()
        self.screensaver_window = True
        # fuerzo un update de fecha y hora cuando vuelvo de diagnostico
        date_now = datetime.today()
        self.UpdateDateTime(date_now)            


    ## MemoryScreen
    def MemoryScreen (self, which_mem):
        self.screensaver_window = False

        a = MemoryDialog(self.ss, which_mem)
        a.setModal(True)
        a.exec_()

        if a.action == 'save':
            self.t.MoveCurrentConfToMem(which_mem)
            self.t.SaveConfigFile()
            self.UpdateMemLabels()
        
        if a.action == 'empty':
            self.t.EmptyMem(which_mem)
            self.t.SaveConfigFile()
            self.UpdateMemLabels()            

        self.ScreenSaverKick()
        self.screensaver_window = True

        
    ## ScreenSaver
    def ScreenSaverDialogScreen (self):
        a = ScreenSaverDialog()
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()

    def ScreenSaverKick (self):
        self.timer_screensaver = self.t.timeout_screensaver

    ## wifi screen
    def WifiScreen (self):
        self.screensaver_window = False
        a = WiFiDialog()
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()
        self.screensaver_window = True
        

### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
w = Dialog()
#http://doc.qt.io/qt-5/qt.html#WindowType-enum
w.setWindowFlags(Qt.CustomizeWindowHint)
# w.setWindowFlags(Qt.FramelessWindowHint)
print('Starting stretcher app...')
w.show()
sys.exit(app.exec_())


### End of File ###
