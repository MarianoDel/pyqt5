import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor
from serialcomm import SerialComm
from treatment_class import Treatment
from stylesheet_class import ButtonStyles
from time import sleep, time
from datetime import datetime
from antenna_class import AntennaInTreatment


#para el timer de 1 segundo
from threading import Timer


"""
        GUI for Magnet - as a copy from stretcher
        Select if its running on Slackware or Raspberry
        Select the type of date-time
"""

### GLOBALS FOR CONFIGURATION #########
## OS where its run
RUNNING_ON_SLACKWARE = 1
RUNNING_ON_RASP = 0
## Date Time as used in
DATE_TIME_USA = 0
DATE_TIME_ARG = 1
## No call the first Dialog - code empty presentation page -
NO_CALL_FIRST_DLG = 1


from ui_light1 import Ui_Dialog
CURRENT_VERSION = "Light_ver_1_0"

    
from dlg_first_cls import FirstDialog
from dlg_treat_cls import TreatmentDialog
from dlg_diags_cls import DiagnosticsDialog
from dlg_mems_cls import MemoryDialog
from dlg_screen_saver_cls import ScreenSaverDialog

## only for tests
# from dlg_steps_cls import StepsDialog

## init of gpios and steady state
from gpios_qt import *
GpiosInit()

    
### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

    # receivedData = pyqtSignal()
    

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
        ### Time Buttons
        self.ui.min20Button.clicked.connect(self.TimeSet)
        self.ui.min30Button.clicked.connect(self.TimeSet)
        self.ui.min45Button.clicked.connect(self.TimeSet)        
        self.ui.min60Button.clicked.connect(self.TimeSet)
        ### Pannels Buttons
        self.ui.pannelAButton.clicked.connect(self.PannelsSet)
        self.ui.pannelBButton.clicked.connect(self.PannelsSet)
        self.ui.pannelCButton.clicked.connect(self.PannelsSet)
        self.ui.pannelDButton.clicked.connect(self.PannelsSet)
        self.ui.pannelEButton.clicked.connect(self.PannelsSet)
        ### Power Buttons
        self.ui.powerUpRedButton.clicked.connect(self.PowerRed)
        self.ui.powerDwnRedButton.clicked.connect(self.PowerRed)
        self.ui.powerUpIRedButton.clicked.connect(self.PowerIRed)
        self.ui.powerDwnIRedButton.clicked.connect(self.PowerIRed)
        ### Steps Buttons
        self.ui.step1Button.clicked.connect(self.StepsSet)
        self.ui.step2Button.clicked.connect(self.StepsSet)
        self.ui.step3Button.clicked.connect(self.StepsSet)
        self.ui.step4Button.clicked.connect(self.StepsSet)
        self.ui.stepPauseButton.clicked.connect(self.StepsPauseSet)
        ### Pulse Type Buttons
        self.ui.cwaveButton.clicked.connect(self.SignalSet)
        self.ui.inphaseButton.clicked.connect(self.SignalSet)
        self.ui.outphaseButton.clicked.connect(self.SignalSet)
        ### Pulse Duration Buttons operation with pressed
        # self.ui.pulseUpButton.pressed.connect(self.PulseUpPressed)
        # self.ui.pulseUpButton.released.connect(self.PulseUpReleased)        
        # self.ui.pulseDwnButton.pressed.connect(self.PulseDwnPressed)
        # self.ui.pulseDwnButton.released.connect(self.PulseDwnReleased)
        ### Pulse Duration Buttons operation with clicked
        self.ui.pulseUpButton.clicked.connect(self.PulsePressed)
        self.ui.pulseDwnButton.clicked.connect(self.PulsePressed)
        ### Memory Buttons
        self.ui.mem1Button.pressed.connect(self.Memory1Pressed)
        self.ui.mem1Button.released.connect(self.Memory1Released)
        self.ui.mem2Button.pressed.connect(self.Memory2Pressed)
        self.ui.mem2Button.released.connect(self.Memory2Released)
        self.ui.mem3Button.pressed.connect(self.Memory3Pressed)
        self.ui.mem3Button.released.connect(self.Memory3Released)
        ### Start Button
        self.ui.startButton.clicked.connect(self.TreatmentScreen)
        ### Diags Button
        self.ui.diagButton.pressed.connect(self.DiagsPressed)
        self.ui.diagButton.released.connect(self.DiagsReleased)


        ## Init treatment object
        self.t = Treatment()
        self.t.SetCurrentVersion(CURRENT_VERSION)
        if RUNNING_ON_SLACKWARE:
            self.t.SetCurrentSystem('slackware')
        elif RUNNING_ON_RASP:
            self.t.SetCurrentSystem('raspbian')

        if DATE_TIME_USA:
            self.t.SetLocalization('usa')
        elif DATE_TIME_ARG:
            self.t.SetLocalization('arg')
        
        ## Init stylesheet object
        self.ss = ButtonStyles()
        
        ## Init the default state:
        self.SignalDisableAll()
        self.StepsDisableAll()
        self.ui.step1Button.setStyleSheet(self.ss.step1_button_enable)

        ### default for time settings
        self.TimeDisableAll()
        self.t.SetTreatmentTimer(20)
        self.ui.min20Button.setStyleSheet(self.ss.min20_enable)

        self.ui.powerRedLabel.setText(str(self.t.GetPowerRed()) + '%')
        self.ui.powerIRedLabel.setText(str(self.t.GetPowerIRed()) + '%')
        self.ui.pulseDurationLabel.setText(str(self.t.GetPulseDuration()))

        ## to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)
        
        #creo el evento y lo conecto al slot
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #Envio3 lo dispara

        ## connect with serial data rx signal
        self.rcv_signal.connect(self.MySignalCallback)

        ## counters for buttons with press release functionality
        self.pulseUpButtonCnt = 0
        self.pulseDwnButtonCnt = 0
        self.mem1ButtonCnt = 0
        self.mem2ButtonCnt = 0
        self.mem3ButtonCnt = 0
        self.diagButtonCnt = 0

        ## PARA SLACKWARE
        if self.t.GetCurrentSystem() == 'slackware':
            self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
        ## PARA RASPBERRY
        elif self.t.GetCurrentSystem() == 'raspbian':
            self.s = SerialComm(self.MyObjCallback, '/dev/serial0')
            
        # if self.s.port_open == False:
        #     self.ui.textEdit.append("No serial port found!!!")
        #     # sys.exit(-1)
        #     #TODO: agregar un timer que vaya buscando el puerto!!!
        # else:
        #     self.InsertLocalText("Serial port open OK!")
        #     self.InsertLocalTextNoNewLine("\nComm with Power: ")
        #     self.s.Write("keepalive,\r\n")


        ## activate the 1 second timer it is repetitive
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        # screen saver timer activation
        self.timer_screensaver = self.t.timeout_screensaver
        self.screensaver_window = False
            
        #SIGNALS CONNECTION
        # conecto senial del timer a la funcion de Update
        self.one_second_signal.connect(self.UpdateOneSec)

        ## read and update memory buttons
        self.MemoryUpdateLabels()

        ### For last call to the first f*** dialog
        if NO_CALL_FIRST_DLG == 0:
            self.FirstDialogScreen()

        #######################
        # Buzzer Init Things. #
        #######################
        ## create buzzer timer
        self.buzzer_timer = QTimer()
        self.buzzer_state = 'init'
        self.buzzer_how_many = 0
        self.buzzer_on_time = 100
        self.buzzer_off_time = 200

        self.SendBuzzerCmd(1)


    ####################
    # Buzzer Functions #
    ####################
    def SendBuzzerCmd (self, how_many, on_time=100, off_time=200):
        self.buzzer_how_many = how_many
        self.buzzer_on_time = on_time
        self.buzzer_off_time = off_time
        self.buzzer_state = 'init'
        self.BuzzerSM()

        
    def BuzzerSM (self):
        if self.buzzer_state == 'init':
            if self.buzzer_how_many > 0:
                BuzzerOn()
                self.buzzer_how_many -= 1
                self.buzzer_state = 'check_stop'
                self.buzzer_timer.singleShot(self.buzzer_on_time, self.BuzzerSM)

        elif self.buzzer_state == 'check_stop':
            BuzzerOff()
            self.buzzer_state = 'init'
            self.buzzer_timer.singleShot(self.buzzer_off_time, self.BuzzerSM)
            
        


    def UpdateDateTime(self, new_date_time):
        date_str = ""
        if self.t.GetLocalization() == 'usa':
            date_str = new_date_time.strftime("%m/%d/%Y - %H:%M")
        elif self.t.GetLocalization() == 'arg':
            date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
            
        self.ui.date_timeLabel.setText(date_str)

        

    ############################
    # Memory Related Functions #
    ############################
    def Memory1Pressed (self):
        self.mem1ButtonCnt = 1
        self.ScreenSaverKick()
        
    def Memory1Released (self):
        if (self.mem1ButtonCnt > 0 and
            self.mem1ButtonCnt < 3):
            self.mem1ButtonCnt = 0

            #get memory values
            if self.t.mem1_treat_time != 'None':
                ## signal
                self.SignalChangeTo(self.t.mem1_signal)
                ## steps and pause
                steps_str = self.t.mem1_steps
                self.StepsChangeTo(int(steps_str[0]))
                if len(steps_str) > 1 and steps_str[1] == 'P':
                    self.t.steps_pause_in_treatment = True
                    self.ui.stepPauseButton.setStyleSheet(self.ss.step_pause_button_enable)

                ## treatment time
                self.TimeChangeTo(int(self.t.mem1_treat_time))
                ## power red
                self.ui.powerRedLabel.setText(self.t.mem1_power_red)
                self.t.SetPowerRed(int(self.t.mem1_power_red))
                ## power ired
                self.ui.powerIRedLabel.setText(self.t.mem1_power_ired)
                self.t.SetPowerIRed(int(self.t.mem1_power_ired))
                ## pulse duration
                self.ui.pulseDurationLabel.setText(self.t.mem1_pulse_duration)
                self.t.SetPulseDuration(int(self.t.mem1_pulse_duration))
                ## pannels for treatment
                self.MemoryUpdatePannelsFromString (self.t.mem1_pannels)
                self.CheckForStart()

    def Memory1Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem1')


    def Memory2Pressed (self):
        self.mem2ButtonCnt = 1
        self.ScreenSaverKick()
        
    def Memory2Released (self):
        if (self.mem2ButtonCnt > 0 and
            self.mem2ButtonCnt < 3):
            self.mem2ButtonCnt = 0

            #get memory values
            if self.t.mem2_treat_time != 'None':
                ## signal
                self.SignalChangeTo(self.t.mem2_signal)
                ## steps and pause
                steps_str = self.t.mem2_steps
                self.StepsChangeTo(int(steps_str[0]))
                if len(steps_str) > 1 and steps_str[1] == 'P':
                    self.t.steps_pause_in_treatment = True
                    self.ui.stepPauseButton.setStyleSheet(self.ss.step_pause_button_enable)

                ## treatment time
                self.TimeChangeTo(int(self.t.mem2_treat_time))
                ## power red
                self.ui.powerRedLabel.setText(self.t.mem2_power_red)
                self.t.SetPowerRed(int(self.t.mem2_power_red))
                ## power ired
                self.ui.powerIRedLabel.setText(self.t.mem2_power_ired)
                self.t.SetPowerIRed(int(self.t.mem2_power_ired))
                ## pulse duration
                self.ui.pulseDurationLabel.setText(self.t.mem2_pulse_duration)
                self.t.SetPulseDuration(int(self.t.mem2_pulse_duration))
                ## pannels for treatment
                self.MemoryUpdatePannelsFromString (self.t.mem2_pannels)
                self.CheckForStart()

    def Memory2Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem2')


    def Memory3Pressed (self):
        self.mem3ButtonCnt = 1
        self.ScreenSaverKick()
        
    def Memory3Released (self):
        if (self.mem3ButtonCnt > 0 and
            self.mem3ButtonCnt < 3):
            self.mem3ButtonCnt = 0
            
            #get memory values
            if self.t.mem3_treat_time != 'None':
                ## signal
                self.SignalChangeTo(self.t.mem3_signal)
                ## steps and pause
                steps_str = self.t.mem3_steps
                self.StepsChangeTo(int(steps_str[0]))
                if len(steps_str) > 1 and steps_str[1] == 'P':
                    self.t.steps_pause_in_treatment = True
                    self.ui.stepPauseButton.setStyleSheet(self.ss.step_pause_button_enable)

                ## treatment time
                self.TimeChangeTo(int(self.t.mem3_treat_time))
                ## power red
                self.ui.powerRedLabel.setText(self.t.mem3_power_red)
                self.t.SetPowerRed(int(self.t.mem3_power_red))
                ## power ired
                self.ui.powerIRedLabel.setText(self.t.mem3_power_ired)
                self.t.SetPowerIRed(int(self.t.mem3_power_ired))
                ## pulse duration
                self.ui.pulseDurationLabel.setText(self.t.mem3_pulse_duration)
                self.t.SetPulseDuration(int(self.t.mem3_pulse_duration))
                ## pannels for treatment
                self.MemoryUpdatePannelsFromString (self.t.mem3_pannels)
                self.CheckForStart()

    def Memory3Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem3')


    def MemoryUpdatePannelsFromString (self, new_mem_pannels):
        self.PannelsDisableAll()
        for pannel in new_mem_pannels:
            if pannel == 'A':
                self.ui.pannelAButton.setStyleSheet(self.ss.pannel_a_enable)
                self.t.EnablePannelsInTreatment('pannel_a')
            elif pannel == 'B':
                self.ui.pannelBButton.setStyleSheet(self.ss.pannel_b_enable)
                self.t.EnablePannelsInTreatment('pannel_b')
            elif pannel == 'C':
                self.ui.pannelCButton.setStyleSheet(self.ss.pannel_c_enable)
                self.t.EnablePannelsInTreatment('pannel_c')
            elif pannel == 'D':
                self.ui.pannelDButton.setStyleSheet(self.ss.pannel_d_enable)
                self.t.EnablePannelsInTreatment('pannel_d')
            elif pannel == 'E':
                self.ui.pannelEButton.setStyleSheet(self.ss.pannel_e_enable)
                self.t.EnablePannelsInTreatment('pannel_e')

    def MemoryUpdateLabels (self):
        if self.t.mem1_treat_time != 'None':
            self.ui.mem11Label.setText(self.t.mem1_treat_time + 'min - ' + self.t.mem1_steps)
            pannels_power_str = self.t.mem1_pannels + ' - '
            pannels_power_str += self.t.mem1_power_red + '/' + self.t.mem1_power_ired + '%'
            self.ui.mem12Label.setText(pannels_power_str)
            self.ui.mem13Label.setText((self.t.mem1_signal).capitalize())
        else:
            self.ui.mem11Label.setText('Empty')
            self.ui.mem12Label.setText('')
            self.ui.mem13Label.setText('')
        
        if self.t.mem2_treat_time != 'None':
            self.ui.mem21Label.setText(self.t.mem2_treat_time + 'min - ' + self.t.mem2_steps)
            pannels_power_str = self.t.mem2_pannels + ' - '
            pannels_power_str += self.t.mem2_power_red + '/' + self.t.mem2_power_ired + '%'
            self.ui.mem22Label.setText(pannels_power_str)
            self.ui.mem23Label.setText((self.t.mem2_signal).capitalize())
        else:
            self.ui.mem21Label.setText('Empty')
            self.ui.mem22Label.setText('')
            self.ui.mem23Label.setText('')

        if self.t.mem3_treat_time != 'None':
            self.ui.mem31Label.setText(self.t.mem3_treat_time + 'min - ' + self.t.Parse_Steps())
            pannels_power_str = self.t.mem3_pannels + ' - '
            pannels_power_str += self.t.mem3_power_red + '/' + self.t.mem3_power_ired + '%'
            self.ui.mem32Label.setText(pannels_power_str)
            self.ui.mem33Label.setText((self.t.mem3_signal).capitalize())
        else:
            self.ui.mem31Label.setText('Empty')
            self.ui.mem32Label.setText('')
            self.ui.mem33Label.setText('')


            
    def DiagsPressed (self):
        self.diagButtonCnt = 1

        
    def DiagsReleased (self):
        self.diagButtonCnt = 0

        
    #############################
    # Signals Related Functions #
    #############################
    def SignalDisableAll(self):
        self.ui.cwaveButton.setStyleSheet(self.ss.cwave_disable)
        self.ui.inphaseButton.setStyleSheet(self.ss.inphase_disable)
        self.ui.outphaseButton.setStyleSheet(self.ss.outphase_disable)

    def SignalSet (self):
        sender = self.sender()

        if sender.objectName() == 'cwaveButton':
            self.SignalChangeTo('cwave')

        elif sender.objectName() == 'inphaseButton':
            self.SignalChangeTo('inphase')

        elif sender.objectName() == 'outphaseButton':
            self.SignalChangeTo('outphase')

        self.CheckForStart()
        self.ScreenSaverKick()
        
    def SignalChangeTo (self, new_signal):
        self.SignalDisableAll()
        
        if new_signal == 'cwave':
            self.ui.cwaveButton.setStyleSheet(self.ss.cwave_enable)
            self.t.SetSignal('cwave')

        elif new_signal == 'inphase':
            self.ui.inphaseButton.setStyleSheet(self.ss.inphase_enable)
            self.t.SetSignal('inphase')

        elif new_signal == 'outphase':
            self.ui.outphaseButton.setStyleSheet(self.ss.outphase_enable)
            self.t.SetSignal('outphase')
        

    ###########################
    # Steps Related Functions #
    ###########################
    def StepsDisableAll(self):
        self.ui.step1Button.setStyleSheet(self.ss.steps_button_disable)
        self.ui.step2Button.setStyleSheet(self.ss.steps_button_disable)
        self.ui.step3Button.setStyleSheet(self.ss.steps_button_disable)
        self.ui.step4Button.setStyleSheet(self.ss.steps_button_disable)
        self.ui.stepPauseButton.setStyleSheet(self.ss.steps_button_disable)
        self.t.steps_pause_in_treatment = False

    def StepsSet (self):
        sender = self.sender()

        if sender.objectName() == 'step1Button':
            self.StepsChangeTo(1)

        if sender.objectName() == 'step2Button':
            self.StepsChangeTo(2)            

        if sender.objectName() == 'step3Button':
            self.StepsChangeTo(3)            

        if sender.objectName() == 'step4Button':
            self.StepsChangeTo(4)            

        self.CheckForStart()
        self.ScreenSaverKick()

    def StepsChangeTo (self, new_steps):
        self.StepsDisableAll()

        if new_steps == 1:
            self.ui.step1Button.setStyleSheet(self.ss.step1_button_enable)
            self.t.SetSteps(1)

        elif new_steps == 2:
            self.ui.step2Button.setStyleSheet(self.ss.step2_button_enable)
            self.t.SetSteps(2)

        elif new_steps == 3:
            self.ui.step3Button.setStyleSheet(self.ss.step3_button_enable)
            self.t.SetSteps(3)

        elif new_steps == 4:
            self.ui.step4Button.setStyleSheet(self.ss.step4_button_enable)
            self.t.SetSteps(4)
        
    def StepsPauseSet (self):
        if self.t.GetSteps() > 1:
            if self.t.steps_pause_in_treatment == False:
                self.t.steps_pause_in_treatment = True
                self.ui.stepPauseButton.setStyleSheet(self.ss.step_pause_button_enable)
            else:
                self.t.steps_pause_in_treatment = False
                self.ui.stepPauseButton.setStyleSheet(self.ss.steps_button_disable)

        self.ScreenSaverKick()


    #############################
    # Pannels Related Functions #
    #############################
    def PannelsSet (self):
        sender = self.sender()

        if sender.objectName() == 'pannelAButton':
            if self.t.GetPannelsInTreatment('pannel_a') == False:
                self.ui.pannelAButton.setStyleSheet(self.ss.pannel_a_enable)
                self.t.EnablePannelsInTreatment('pannel_a')
            else:
                self.ui.pannelAButton.setStyleSheet(self.ss.pannels_disable)
                self.t.DisablePannelsInTreatment('pannel_a')

        if sender.objectName() == 'pannelBButton':
            if self.t.GetPannelsInTreatment('pannel_b') == False:
                self.ui.pannelBButton.setStyleSheet(self.ss.pannel_b_enable)
                self.t.EnablePannelsInTreatment('pannel_b')
            else:
                self.ui.pannelBButton.setStyleSheet(self.ss.pannels_disable)
                self.t.DisablePannelsInTreatment('pannel_b')

        if sender.objectName() == 'pannelCButton':
            if self.t.GetPannelsInTreatment('pannel_c') == False:
                self.ui.pannelCButton.setStyleSheet(self.ss.pannel_c_enable)
                self.t.EnablePannelsInTreatment('pannel_c')
            else:
                self.ui.pannelCButton.setStyleSheet(self.ss.pannels_disable)
                self.t.DisablePannelsInTreatment('pannel_c')

        if sender.objectName() == 'pannelDButton':
            if self.t.GetPannelsInTreatment('pannel_d') == False:
                self.ui.pannelDButton.setStyleSheet(self.ss.pannel_d_enable)
                self.t.EnablePannelsInTreatment('pannel_d')
            else:
                self.ui.pannelDButton.setStyleSheet(self.ss.pannels_disable)
                self.t.DisablePannelsInTreatment('pannel_d')

        if sender.objectName() == 'pannelEButton':
            if self.t.GetPannelsInTreatment('pannel_e') == False:
                self.ui.pannelEButton.setStyleSheet(self.ss.pannel_e_enable)
                self.t.EnablePannelsInTreatment('pannel_e')
            else:
                self.ui.pannelEButton.setStyleSheet(self.ss.pannels_disable)
                self.t.DisablePannelsInTreatment('pannel_e')
                
        self.CheckForStart()
        self.ScreenSaverKick()        

    def PannelsDisableAll (self):
        self.ui.pannelAButton.setStyleSheet(self.ss.pannels_disable)
        self.t.DisablePannelsInTreatment('pannel_a')

        self.ui.pannelBButton.setStyleSheet(self.ss.pannels_disable)
        self.t.DisablePannelsInTreatment('pannel_b')

        self.ui.pannelCButton.setStyleSheet(self.ss.pannels_disable)
        self.t.DisablePannelsInTreatment('pannel_c')

        self.ui.pannelDButton.setStyleSheet(self.ss.pannels_disable)
        self.t.DisablePannelsInTreatment('pannel_d')

        self.ui.pannelEButton.setStyleSheet(self.ss.pannels_disable)
        self.t.DisablePannelsInTreatment('pannel_e')


    ####################################
    # Treatment Time Related Functions #
    ####################################
    def TimeDisableAll(self):
        self.ui.min20Button.setStyleSheet(self.ss.min20_disable)
        self.ui.min30Button.setStyleSheet(self.ss.min30_disable)
        self.ui.min45Button.setStyleSheet(self.ss.min45_disable)
        self.ui.min60Button.setStyleSheet(self.ss.min60_disable)

    def TimeSet (self):
        sender = self.sender()

        if sender.objectName() == 'min20Button':
            self.TimeChangeTo(20)

        elif sender.objectName() == 'min30Button':
            self.TimeChangeTo(30)

        elif sender.objectName() == 'min45Button':
            self.TimeChangeTo(45)
            
        elif sender.objectName() == 'min60Button':
            self.TimeChangeTo(60)

        self.ScreenSaverKick()

    def TimeChangeTo (self, new_time):
        self.TimeDisableAll()

        if new_time == 20:
            self.t.SetTreatmentTimer(20)
            self.ui.min20Button.setStyleSheet(self.ss.min20_enable)

        elif new_time == 30:
            self.t.SetTreatmentTimer(30)
            self.ui.min30Button.setStyleSheet(self.ss.min30_enable)

        elif new_time == 45:
            self.t.SetTreatmentTimer(45)
            self.ui.min45Button.setStyleSheet(self.ss.min45_enable)            
            
        elif new_time == 60:
            self.t.SetTreatmentTimer(60)
            self.ui.min60Button.setStyleSheet(self.ss.min60_enable)            
            
        
    ###########################
    # Power Related Functions #
    ###########################
    def PowerRed (self):
        sender = self.sender()
        last_pwr = self.t.GetPowerRed()
        max_pwr = self.t.max_power_red

        if sender.objectName() == 'powerUpRedButton':
            if last_pwr == 0:
                last_pwr = 10
            elif ((last_pwr + 5) <= max_pwr):
                last_pwr += 5
            else:
                last_pwr = max_pwr

        if sender.objectName() == 'powerDwnRedButton':                
            if ((last_pwr - 5) >= 10):
                last_pwr -= 5
            else:
                last_pwr = 0

        self.ui.powerRedLabel.setText(str(last_pwr) + '%')
        self.t.SetPowerRed(last_pwr)
        self.CheckForStart()
        self.ScreenSaverKick()        
                
    def PowerIRed (self):
        sender = self.sender()
        last_pwr = self.t.GetPowerIRed()
        max_pwr = self.t.max_power_ired

        if sender.objectName() == 'powerUpIRedButton':
            if last_pwr == 0:
                last_pwr = 10
            elif ((last_pwr + 5) <= max_pwr):
                last_pwr += 5
            else:
                last_pwr = max_pwr

        if sender.objectName() == 'powerDwnIRedButton':                
            if ((last_pwr - 5) >= 10):
                last_pwr -= 5
            else:
                last_pwr = 0

        self.ui.powerIRedLabel.setText(str(last_pwr) + '%')
        self.t.SetPowerIRed(last_pwr)
        self.CheckForStart()        
        self.ScreenSaverKick()        
                    
        
    ####################################
    # Pulse Duration Related Functions #
    ####################################
    ### Operation with pressed
    # def PulseUpPressed (self):
    #     self.PulseUp (1)
    #     self.pulseUpButtonCnt = 1
    #     self.ScreenSaverKick()        
        
    # def PulseUpReleased (self):
    #     self.pulseUpButtonCnt = 0
        
    # def PulseDwnPressed (self):
    #     self.PulseDwn(1)
    #     self.pulseDwnButtonCnt = 1
    #     self.ScreenSaverKick()
        
    # def PulseDwnReleased (self):
    #     self.pulseDwnButtonCnt = 0

    # def PulseUp (self, new_pulse):
    #     last_pulse = self.t.GetPulseDuration()
    #     max_pulse = self.t.pulse_max
    #     if ((last_pulse + new_pulse) < max_pulse):
    #         last_pulse += new_pulse
    #     else:
    #         last_pulse = max_pulse
    #     self.ui.pulseDurationLabel.setText(str(last_pulse))
    #     self.t.SetPulseDuration(last_pulse)
        
    # def PulseDwn (self, new_pulse):
    #     last_pulse = self.t.GetPulseDuration()
    #     min_pulse = self.t.pulse_min
    #     if ((last_pulse - new_pulse) > min_pulse):
    #         last_pulse -= new_pulse
    #     else:
    #         last_pulse = min_pulse
    #     self.ui.pulseDurationLabel.setText(str(last_pulse))
    #     self.t.SetPulseDuration(last_pulse)
    ### Operation with clicked
    def PulsePressed (self):
        sender = self.sender()
        last_pulse = self.t.GetPulseDuration()
        max_pulse = self.t.pulse_max
        min_pulse = self.t.pulse_min        

        if sender.objectName() == 'pulseUpButton':
            if last_pulse < max_pulse:
                last_pulse += 100
            else:
                last_pulse = max_pulse

        if sender.objectName() == 'pulseDwnButton':                
            if (last_pulse > min_pulse):
                last_pulse -= 100
            else:
                last_pulse = min_pulse
        
        self.ui.pulseDurationLabel.setText(str(last_pulse))
        self.t.SetPulseDuration(last_pulse)
        

        

    def CheckForStart (self):
        if (self.CheckCompleteConf() == True and
            self.s.port_open == True):
        # if self.CheckCompleteConf() == True:        
            self.ui.startButton.setStyleSheet(self.ss.start_enable)
        else:
            self.ui.startButton.setStyleSheet(self.ss.start_disable)


    def CheckCompleteConf (self):
        if (self.t.GetPowerRed() != 0 or
            self.t.GetPowerIRed() != 0):
            if (self.t.GetPannelsInTreatment('pannel_a') != False or
                self.t.GetPannelsInTreatment('pannel_b') != False or
                self.t.GetPannelsInTreatment('pannel_c') != False or
                self.t.GetPannelsInTreatment('pannel_d') != False or
                self.t.GetPannelsInTreatment('pannel_e') != False):
                if self.t.GetSignal() != 'None':
                    return True

        return False


    def UpdateOneSec (self):
        """ paso un segundo, reviso que tengo que hacer """
        # reviso si algun boton sigue presionado
        ## Time Buttons
        if self.pulseUpButtonCnt > 3:
            self.PulseUp(200)
        elif self.pulseUpButtonCnt > 1:
            self.PulseUp(25)
            self.pulseUpButtonCnt += 1            
        elif  self.pulseUpButtonCnt == 1:
            self.pulseUpButtonCnt += 1

        if self.pulseDwnButtonCnt > 3:
            self.PulseDwn(200)
        elif self.pulseDwnButtonCnt > 1:
            self.PulseDwn(25)
            self.pulseDwnButtonCnt += 1            
        elif self.pulseDwnButtonCnt == 1:
            self.pulseDwnButtonCnt += 1

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
                                        
        

        
    def TimerOneSec(self):
        self.one_second_signal.emit()        


    #################################
    # Serial Port Related Functions #
    #################################
    def MyObjCallback (self, dataread):
        d = dataread.rstrip()
        self.rcv_signal.emit(d)

    def MySignalCallback (self, rcv):
        self.SerialProcess (rcv)
                        
    def SerialProcess (self, rcv):
        pass
                

            
            
    #capturo el cierre
    def closeEvent (self, event):
        self.s.Close()
        # sleep(2)
        event.accept()

        
####################################
# Different Screens Calls are here #
####################################

    ## Initial Screen
    def FirstDialogScreen (self):
        self.screensaver_window = False
        a = FirstDialog(self.t, self.ss)
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()
        self.screensaver_window = True

        
    ## Treatment Screen
    def TreatmentScreen (self):
        if self.CheckCompleteConf() == True:
            self.screensaver_window = False
                
            self.t.treatment_state = 'STOP'    #para un buen arranque la llamo con estado de stop
            a = TreatmentDialog(self.t, self.ss, self.s, parent=self)
            a.setModal(True)
            a.exec_()

            self.ScreenSaverKick()
            # self.screensaver_window = True

            ## esta es posta, la de arriba para tests
            # if self.s.port_open == True:
            #     self.screensaver_window = False
                
            #     self.t.treatment_state = 'STOP'    #para un buen arranque la llamo con estado de stop
            #     a = TreatmentDialog(self.t, self.ss, self.antennas_connected, self.s, parent=self)
            #     a.setModal(True)
            #     a.exec_()

            #     self.ScreenSaverKick()
            #     self.screensaver_window = True
                

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
            

    ## Steps Screen
    # def StepsDialogScreen (self):
    #     # a = StepsDialog(self.parent)
    #     a = StepsDialog(self)
    #     a.setModal(True)
    #     a.exec_()
        
        

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
