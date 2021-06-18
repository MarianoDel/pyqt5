from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from time import sleep, time
from threading import Timer
from datetime import datetime


#get the UI from here
from ui_treatment_dlg import Ui_TreatmentDialog

from dlg_steps_cls import StepsDialog


For_Test_Send_Commands_To_Console = False

#####################################################
# TreatmentDialog Class - to get the system running #
#####################################################
class TreatmentDialog(QDialog):

    #SIGNALS
    # signal to update in 1 second
    one_second_signal = pyqtSignal()
    sync_signal = pyqtSignal()

    def __init__(self, treat_obj, style_obj, ser_instance, parent=None):
        super(TreatmentDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_TreatmentDialog()
        self.ui.setupUi(self)

        # get the parent reference and data
        self.parent = parent
        self.treat = treat_obj
        self.style = style_obj
        self.s = ser_instance

        self.ui.doneButton.setEnabled(False)
        self.ui.doneButton.setStyleSheet(self.style.ended_label_disable)
        self.ended_label = False
        
        # get the close event and connect the buttons
        self.ui.doneButton.clicked.connect(self.FinishThisDialog)
        self.ui.stop_rsmButton.clicked.connect(self.StopRsmTreatment)
        self.ui.stopButton.clicked.connect(self.StopTreatment)
        self.ui.rsmButton.clicked.connect(self.RsmTreatment)        
        # self.ui.ant1Button.clicked.connect(self.ChannelGetTemp)
        # self.ui.ant2Button.clicked.connect(self.ChannelGetTemp)
        # self.ui.ant3Button.clicked.connect(self.ChannelGetTemp)
        # self.ui.ant4Button.clicked.connect(self.ChannelGetTemp)
        
        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        # progress timer, these ones are qt
        self.progress_timer = QTimer()
        self.init_timer = QTimer()
        self.t1sec = QTimer()
        self.sync_timer = QTimer()

        # progress states machine -SM-
        self.stop_rsm_state = 'stoping'
        self.init_state = 'start'
        

        # CONNECT SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)
        self.sync_signal.connect(self.SendSyncToBoards)
        # self.progress_signal.connect(self.UpdateProgressStopRsmSM)


        ## Default Screen
        self.ui.progressLabel.setText('Session Starting...')
        self.ui.minutesLabel.setText(str(self.treat.treatment_timer) + "'")
        self.ui.powerRedLabel.setText("Red: " + str(self.treat.GetPowerRed()) + "%")
        self.ui.powerIRedLabel.setText("IRed: " + str(self.treat.GetPowerIRed()) + "%")        

        current_signal = self.treat.GetSignal()
        if current_signal == 'cwave':
            self.ui.signalLargeButton.setStyleSheet(self.style.cwave_enable)
            self.ui.signalShortButton.setStyleSheet(self.style.signal_treat_disable)
            self.ui.signalLargeButton.raise_()
            
        elif current_signal == 'inphase':
            self.ui.signalShortButton.setStyleSheet(self.style.inphase_enable)
            self.ui.signalLargeButton.setStyleSheet(self.style.signal_treat_disable)
            self.ui.signalShortButton.raise_()
            
        elif current_signal == 'outphase':
            self.ui.signalShortButton.setStyleSheet(self.style.outphase_enable)
            self.ui.signalLargeButton.setStyleSheet(self.style.signal_treat_disable)
            self.ui.signalShortButton.raise_()

        steps = self.treat.GetSteps()
        if steps == 1:
            self.ui.stepsButton.setStyleSheet(self.style.step1_button_enable)
            self.ui.stepsButton.setText('1')
        elif steps == 2:
            self.ui.stepsButton.setStyleSheet(self.style.step2_button_enable)
            self.ui.stepsButton.setText('2')            
        elif steps == 3:
            self.ui.stepsButton.setStyleSheet(self.style.step3_button_enable)
            self.ui.stepsButton.setText('3')            
        elif steps == 4:
            self.ui.stepsButton.setStyleSheet(self.style.step4_button_enable)
            self.ui.stepsButton.setText('4')            

        self.ui.stopButton.setEnabled(False)
        self.ui.rsmButton.setEnabled(False)
        self.ui.stop_rsmButton.raise_()

        ## for steps calcs
        self.TreatmentStepsCalc ()
        

        
        ## setup antennas icons
        ## url(:/buttons/resources/Stop.png)
        # self.wifi_act_Icon = QIcon(':/buttons/resources/wifi-symbol_act.png')
        # self.wifi_err_Icon = QIcon(':/buttons/resources/wifi-symbol_err.png')
        # self.wifi_disa_Icon = QIcon(':/buttons/resources/wifi-symbol_disa.png')
        # self.wifi_emit_Icon = QIcon(':/buttons/resources/wifi-symbol_emit.png')
        
        ## setup antennas
        # self.antenna_emmiting = False
        # self.AntennasUpdate_UI(False)
            
        ## start the timer
        self.t1sec.timeout.connect(self.TimerOneSec)
        self.t1sec.start(1000)

        ## Effectively start treatment
        self.StartTreatment()


    # def AntennasUpdate_UI (self, emit):
    #     if emit == True:
    #         current_icon = self.wifi_emit_Icon
    #     else:
    #         current_icon = self.wifi_act_Icon

    #     if self.ant.GetActive('ch1') == True:
    #         self.ui.ant1Button.setIcon(current_icon)

    #     if self.ant.GetActive('ch2') == True:
    #         self.ui.ant2Button.setIcon(current_icon)

    #     if self.ant.GetActive('ch3') == True:
    #         self.ui.ant3Button.setIcon(current_icon)

    #     if self.ant.GetActive('ch4') == True:
    #         self.ui.ant4Button.setIcon(current_icon)

            
    def UpdateDateTime(self, new_date_time):
        date_str = ""
        if self.treat.GetLocalization() == 'usa':
            date_str = new_date_time.strftime("%m/%d/%Y - %H:%M")
        elif self.treat.GetLocalization() == 'arg':
            date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")

        self.ui.date_timeLabel.setText(date_str)


    """ Emit a signal to not delay the timer response """
    def TimerOneSec(self):        
        self.one_second_signal.emit()


    """ Emit a signal to not delay the timer response """
    def TimerForSync(self):        
        self.sync_signal.emit()


    def SendSyncToBoards (self):
        self.s.Write('*')
        
        
    def UpdateOneSec (self):
        # do a UI update if its necessary
        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)

        if self.treat.treatment_state == 'START':
            self.UpdateTimerAndLabels()

        if self.treat.treatment_state == 'ENDED':
            self.UpdateEndedLabels()


    def StartTreatment (self):
        print(self.treat.treatment_state)
        if self.treat.treatment_state == 'STOP':
            total_mins = self.treat.GetTreatmentTimer()
            self.ui.remaining_minsLabel.setText(str(total_mins) + "'")
            self.ui.remaining_secsLabel.setText("00''")
            self.treat.remaining_minutes = total_mins
            self.treat.remaining_seconds = 0

            self.init_state = 'clean'
            self.SendStartSM()

            self.treat.treatment_state = 'START'
            self.ui.progressLabel.setText('Session in Progress')
            self.ui.textEdit.append("Starting Treatment...")


    def SendStartSM (self):
        if For_Test_Send_Commands_To_Console == True:
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                print("chf stop treatment\r\n")
            
                self.init_state = 'signal'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'signal':
                to_send = self.treat.GetSignal()
                if to_send != 'cwave':
                    to_send = 'pulsed'
                    # enable sync here!!!

                to_send = "chf signal " + to_send
                self.InsertLocalText(to_send)
                print(to_send)
                
                self.init_state = 'pulse_duration'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'pulse_duration':
                pulse = self.treat.GetPulseDuration()
                if pulse >= 1000:
                    to_send = "chf frequency 1\r\n"
                elif pulse <= 100:
                    to_send = "chf frequency 10\r\n"
                else:
                    to_send = "chf frequency 5\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_red_1'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_1':
                if (self.treat.GetPannelsInTreatment('pannel_a') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch1 power red 00\r\n"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch1 power red " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_ired_1'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_1':
                if (self.treat.GetPannelsInTreatment('pannel_a') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch1 power ired 00\r\n"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch1 power ired " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_red_2'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_2':
                if (self.treat.GetPannelsInTreatment('pannel_b') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch2 power red 00\r\n"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch2 power red " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_ired_2'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_2':
                if (self.treat.GetPannelsInTreatment('pannel_b') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch2 power ired 00\r\n"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch2 power ired " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_red_3'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_3':
                if (self.treat.GetPannelsInTreatment('pannel_c') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch3 power red 00\r\n"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch3 power red " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_ired_3'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_3':
                if (self.treat.GetPannelsInTreatment('pannel_c') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch3 power ired 00\r\n"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch3 power ired " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_red_4'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_4':
                if (self.treat.GetPannelsInTreatment('pannel_d') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch4 power red 00\r\n"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch4 power red " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_ired_4'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_4':
                if (self.treat.GetPannelsInTreatment('pannel_d') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch4 power ired 00\r\n"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch4 power ired " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_red_5'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_5':
                if (self.treat.GetPannelsInTreatment('pannel_e') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch5 power red 00\r\n"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch5 power red " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'power_ired_5'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_5':
                if (self.treat.GetPannelsInTreatment('pannel_e') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch5 power ired 00\r\n"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch5 power ired " + str(power_r) + "\r\n"

                print(to_send)

                self.InsertLocalText(to_send)
                self.init_state = 'start'
                self.init_timer.singleShot(100, self.SendStartSM)
                
            elif self.init_state == 'start':
                self.InsertLocalText("Starting Treatment...")
                print("chf start treatment\r\n")

        else:
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                self.s.Write("chf stop treatment\r\n")
            
                self.init_state = 'signal'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'signal':
                to_send = self.treat.GetSignal()
                if to_send != 'cwave':
                    to_send = 'pulsed'
                    # enable sync here!!!

                to_send = "chf signal " + to_send
                self.InsertLocalText(to_send)                
                self.s.Write(to_send + "\r\n")
                
                self.init_state = 'pulse_duration'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'pulse_duration':
                pulse = self.treat.GetPulseDuration()
                if pulse >= 1000:
                    to_send = "chf frequency 1\r\n"
                elif pulse <= 100:
                    to_send = "chf frequency 10\r\n"
                else:
                    to_send = "chf frequency 5\r\n"

                self.InsertLocalText(to_send)                    
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_red_1'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_1':
                if (self.treat.GetPannelsInTreatment('pannel_a') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch1 power red 00"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch1 power red " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_ired_1'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_1':
                if (self.treat.GetPannelsInTreatment('pannel_a') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch1 power ired 00"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch1 power ired " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_red_2'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_2':
                if (self.treat.GetPannelsInTreatment('pannel_b') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch2 power red 00"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch2 power red " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_ired_2'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_2':
                if (self.treat.GetPannelsInTreatment('pannel_b') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch2 power ired 00"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch2 power ired " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_red_3'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_3':
                if (self.treat.GetPannelsInTreatment('pannel_c') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch3 power red 00"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch3 power red " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_ired_3'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_3':
                if (self.treat.GetPannelsInTreatment('pannel_c') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch3 power ired 00"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch3 power ired " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_red_4'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_4':
                if (self.treat.GetPannelsInTreatment('pannel_d') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch4 power red 00"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch4 power red " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_ired_4'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_4':
                if (self.treat.GetPannelsInTreatment('pannel_d') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch4 power ired 00"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch4 power ired " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_red_5'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_red_5':
                if (self.treat.GetPannelsInTreatment('pannel_e') != True or
                    self.treat.GetPowerRed() == 0):
                    to_send = "ch5 power red 00"
                else:
                    power_r = self.treat.GetPowerRed()
                    to_send = "ch5 power red " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'power_ired_5'
                self.init_timer.singleShot(100, self.SendStartSM)

            elif self.init_state == 'power_ired_5':
                if (self.treat.GetPannelsInTreatment('pannel_e') != True or
                    self.treat.GetPowerIRed() == 0):
                    to_send = "ch5 power ired 00"
                else:
                    power_r = self.treat.GetPowerIRed()
                    to_send = "ch5 power ired " + str(power_r)

                self.InsertLocalText(to_send)
                self.s.Write(to_send + "\r\n")

                self.init_state = 'start'
                self.init_timer.singleShot(100, self.SendStartSM)
                
            elif self.init_state == 'start':
                self.InsertLocalText("Starting Treatment...")
                self.s.Write("chf start treatment\r\n")
                self.parent.SendBuzzerCmd(1)

                """ start a sync timer if signal is not a cwave """
                if self.treat.GetSignal() != 'cwave':
                    ## start the timer
                    self.sync_timer.timeout.connect(self.TimerForSync)
                    
                    pulse = self.treat.GetPulseDuration()
                    if pulse >= 1000:
                        self.sync_timer.start(5000)
                        # to_send = "chf frequency 1\r\n"
                    elif pulse <= 100:
                        self.sync_timer.start(500)
                        # to_send = "chf frequency 10\r\n"
                    else:
                        self.sync_timer.start(1000)
                        # to_send = "chf frequency 5\r\n"
                    

                
    def SendPauseSM (self):
        if For_Test_Send_Commands_To_Console == True:        
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                print("chf stop treatment\r\n")
            
                self.init_state = 'pause'
                self.init_timer.singleShot(100, self.SendPauseSM)

            elif self.init_state == 'pause':
                print("chf stop treatment\r\n")                
                self.InsertLocalText("Pausing Treatment...")

        else:
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                self.s.Write("chf stop treatment\r\n")
            
                self.init_state = 'pause'
                self.init_timer.singleShot(100, self.SendPauseSM)

            elif self.init_state == 'pause':
                self.s.Write("chf stop treatment\r\n")                
                self.InsertLocalText("Pausing Treatment...")
            

            
    def SendResumeSM (self):
        if For_Test_Send_Commands_To_Console == True:        
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                print("chf stop treatment\r\n")
            
                self.init_state = 'resume'
                self.init_timer.singleShot(100, self.SendResumeSM)

            elif self.init_state == 'resume':
                print("chf start treatment\r\n")                
                self.InsertLocalText("Resuming Treatment...")

        else:
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                self.s.Write("chf stop treatment\r\n")
            
                self.init_state = 'resume'
                self.init_timer.singleShot(100, self.SendResumeSM)

            elif self.init_state == 'resume':
                self.s.Write("chf start treatment\r\n")                
                self.InsertLocalText("Resuming Treatment...")
                
            
    def SendStopSM (self):
        if For_Test_Send_Commands_To_Console == True:                
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                print("chf stop treatment\r\n")
            
                self.init_state = 'stop'
                self.init_timer.singleShot(100, self.SendStopSM)

            elif self.init_state == 'stop':
                print("chf stop treatment\r\n")                
                self.InsertLocalText("STOP Treatment")

                self.init_state = 'stop_bips'
                self.init_timer.singleShot(100, self.SendStopSM)
            
            elif self.init_state == 'stop_bips':
                print("buzzer short 3,\r\n")

        else:
            if self.init_state == 'clean':
                # limpio el puerto y luego la configuracion
                self.s.Write("chf stop treatment\r\n")
            
                self.init_state = 'stop'
                self.init_timer.singleShot(100, self.SendStopSM)

            elif self.init_state == 'stop':
                self.s.Write("chf stop treatment\r\n")                
                self.InsertLocalText("STOP Treatment")

                self.init_state = 'stop_bips'
                self.init_timer.singleShot(100, self.SendStopSM)
            
            elif self.init_state == 'stop_bips':
                pass
                # self.s.Write("buzzer short 3,\r\n")


    def SendStopNoBuzzerSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("chf stop treatment\r\n")
            
            self.init_state = 'stop'
            self.init_timer.singleShot(100, self.SendStopSM)

        elif self.init_state == 'stop':
            self.s.Write("chf stop treatment\r\n")                
            self.InsertLocalText("STOP Treatment")

            
    def UpdateTimerAndLabels (self):
        if (self.treat.remaining_minutes > 0 or
            self.treat.remaining_seconds > 0):
            #si quedan minutos todavia
            if self.treat.remaining_seconds > 0:
                self.treat.remaining_seconds -= 1
            else:
                self.treat.remaining_minutes -= 1
                self.treat.remaining_seconds = 59

            #todos los segundos actualizo ui
            self.ui.remaining_minsLabel.setText(str(self.treat.remaining_minutes) + "'")
            self.ui.remaining_secsLabel.setText(str(self.treat.remaining_seconds) + "''")

            ## reviso si necesito activar steps
            if self.TreatmentStepsCheck(self.treat.remaining_minutes) == True:
                if self.treat.steps_pause_in_treatment == True:
                    self.treat.treatment_state = 'PAUSE'
                    self.init_state = 'clean'
                    self.SendPauseSM()
                    self.StepsDialogScreen()
                else:
                    ## only beeps
                    self.parent.SendBuzzerCmd(1)
                    
        else:
            # termino el tratamiento, hago algo parecido al boton stop
            self.treat.treatment_state = 'STOP'
            self.ui.remaining_secsLabel.setText("0''")
            self.ui.textEdit.append("STOP Treatment")
            self.ui.progressLabel.setStyleSheet(self.style.label_blue)
            self.stop_rsm_state = 'ending'
            self.progress_timer.singleShot(300, self.ProgressEndSM)

            self.init_state = 'clean'
            self.SendStopSM()        

            
    def UpdateEndedLabels (self):
        if self.ended_label == True:
            self.ended_label = False
            self.ui.doneButton.setStyleSheet(self.style.ended_label_disable)
        else:
            self.ended_label = True
            self.ui.doneButton.setStyleSheet(self.style.ended_label_enable)
            
        
    def StopRsmTreatment(self):
        if self.treat.treatment_state == 'START':
            self.treat.treatment_state = 'PAUSE'
            self.ui.stop_rsmButton.setEnabled(False)
            self.ui.stop_rsmButton.setStyleSheet(self.style.stop_rsm_disable)
            self.ui.stopButton.raise_()
            self.ui.rsmButton.raise_()

            self.stop_rsm_state = 'pausing'
            self.progress_timer.singleShot(300, self.ProgressStopRsmSM)

            self.init_state = 'clean'
            self.SendPauseSM()

        if self.treat.treatment_state == 'ENDED':
            self.FinishThisDialog()
        
        
    def StopTreatment(self):
        self.stop_rsm_state = 'stoping'
        self.progress_timer.singleShot(300, self.ProgressStopSM)

        self.init_state = 'clean'
        self.SendStopNoBuzzerSM()


    def RsmTreatment(self):
        self.ui.stopButton.setEnabled(False)
        self.ui.rsmButton.setEnabled(False)
        self.ui.stop_rsmButton.raise_()
        self.ui.stop_rsmButton.setStyleSheet(self.style.stop_rsm_enable)

        self.stop_rsm_state = 'resuming'
        self.progress_timer.singleShot(300, self.ProgressRsmSM)

        self.init_state = 'clean'
        self.SendResumeSM()        


    """ posible states from stop_rsmButton pausing, paused """
    def ProgressStopRsmSM(self):
        if self.stop_rsm_state == 'pausing':
            self.ui.progressLabel.setText('Pausing.')
            self.stop_rsm_state = 'pausing1'
            self.progress_timer.singleShot(300, self.ProgressStopRsmSM)

        elif self.stop_rsm_state == 'pausing1':
            self.ui.progressLabel.setText('Pausing..')
            self.stop_rsm_state = 'pausing2'
            self.progress_timer.singleShot(300, self.ProgressStopRsmSM)            

        elif self.stop_rsm_state == 'pausing2':
            self.ui.progressLabel.setText('Pausing...')
            self.stop_rsm_state = 'paused'
            self.progress_timer.singleShot(300, self.ProgressStopRsmSM)            

        elif self.stop_rsm_state == 'paused':
            self.ui.progressLabel.setText('Session Paused')
            self.ui.progressLabel.setStyleSheet(self.style.label_red)
            self.ui.stopButton.setEnabled(True)
            self.ui.rsmButton.setEnabled(True)
            # self.AntennasUpdate_UI(False)


    """ posible states from rsmButton resuming, resumed """
    def ProgressRsmSM(self):
        if self.stop_rsm_state == 'resuming':
            self.ui.progressLabel.setText('Resuming.')
            self.stop_rsm_state = 'resuming1'
            self.progress_timer.singleShot(300, self.ProgressRsmSM)

        elif self.stop_rsm_state == 'resuming1':
            self.ui.progressLabel.setText('Resuming..')
            self.stop_rsm_state = 'resuming2'
            self.progress_timer.singleShot(300, self.ProgressRsmSM)            

        elif self.stop_rsm_state == 'resuming2':
            self.ui.progressLabel.setText('Resuming...')
            self.stop_rsm_state = 'resumed'
            self.progress_timer.singleShot(300, self.ProgressRsmSM)            

        elif self.stop_rsm_state == 'resumed':
            self.ui.progressLabel.setText('Session in Progress')
            self.ui.progressLabel.setStyleSheet(self.style.label_green)
            self.treat.treatment_state = 'START'
            self.ui.stop_rsmButton.setEnabled(True)


    """ posible states from stopButton stoping, stoped """
    def ProgressStopSM(self):
        if self.stop_rsm_state == 'stoping':
            self.ui.progressLabel.setText('Stoping.')
            self.stop_rsm_state = 'stoping1'
            self.progress_timer.singleShot(300, self.ProgressStopSM)

        elif self.stop_rsm_state == 'stoping1':
            self.ui.progressLabel.setText('Stoping..')
            self.stop_rsm_state = 'stoping2'
            self.progress_timer.singleShot(300, self.ProgressStopSM)            

        elif self.stop_rsm_state == 'stoping2':
            self.ui.progressLabel.setText('Stoping...')
            self.stop_rsm_state = 'stoped'
            self.progress_timer.singleShot(300, self.ProgressStopSM)            

        elif self.stop_rsm_state == 'stoped':
            self.treat.treatment_state = 'STOP'
            self.FinishThisDialog()


    """ posible states from the timer ending treatment ending, ended """
    def ProgressEndSM(self):
        if self.stop_rsm_state == 'ending':
            self.ui.progressLabel.setText('Ending Treatment.')
            self.stop_rsm_state = 'ending1'
            self.progress_timer.singleShot(300, self.ProgressEndSM)

        elif self.stop_rsm_state == 'ending1':
            self.ui.progressLabel.setText('Ending Treatment..')
            self.stop_rsm_state = 'ending2'
            self.progress_timer.singleShot(300, self.ProgressEndSM)            

        elif self.stop_rsm_state == 'ending2':
            self.ui.progressLabel.setText('Ending Treatment...')
            self.stop_rsm_state = 'ended'
            self.progress_timer.singleShot(300, self.ProgressEndSM)            

        elif self.stop_rsm_state == 'ended':
            self.ui.progressLabel.setText('Session Finished')
            self.treat.treatment_state = 'ENDED'
            self.ui.doneButton.setEnabled(True)
            self.ui.stop_rsmButton.setStyleSheet(self.style.stop_rsm_rewind)



    #############################
    # Treatment Steps Functions #
    #############################
    def TreatmentStepsCalc (self):
        steps = self.treat.steps_in_treatment
        time = self.treat.GetTreatmentTimer()

        self.step_remaining_m1 = 0
        self.step_remaining_m2 = 0
        self.step_remaining_m3 = 0
        self.step_remaining_stage = 1

        if steps == 4:
            time_lapse = time / steps
            time_m = int(time_lapse)
            self.step_remaining_m1 = time - time_m - 1
            self.step_remaining_m2 = time - 2 * time_m - 1
            self.step_remaining_m3 = time - 3 * time_m - 1

        elif steps == 3:
            time_lapse = time / steps
            time_m = int(time_lapse)
            self.step_remaining_m1 = time - time_m - 1
            self.step_remaining_m2 = time - 2 * time_m - 1

        elif steps == 2:
            time_lapse = time / steps
            time_m = int(time_lapse)
            self.step_remaining_m1 = time - time_m - 1

        else:
            self.step_remaining_stage = 0


    def TreatmentStepsCheck (self, current_minutes):
        if self.step_remaining_stage > 0:
            if (self.step_remaining_stage == 1 and
                current_minutes == self.step_remaining_m1):
                self.step_remaining_stage += 1
                return True

            elif (self.step_remaining_stage == 2 and
                  current_minutes == self.step_remaining_m2):
                self.step_remaining_stage += 1
                return True

            elif (self.step_remaining_stage == 3 and
                  current_minutes == self.step_remaining_m3):
                self.step_remaining_stage += 1
                return True
            
        
            
    ###################################
    # Serial Communications Functions #
    ###################################
    def SerialDataCallback (self, rcv):        
        # print ("serial data callback!")
        self.SerialProcessString(rcv)
                

    def SerialProcessString (self, rcv):
        # self.ui.textEdit.append(rcv)
        # reviso si es un final de tratamiento
        # if rcv.startswith("treat end,") or rcv.startswith("treat err,"):
        if (rcv.startswith("chf") or
            rcv.startswith("ch1") or
            rcv.startswith("ch2") or
            rcv.startswith("ch3") or
            rcv.startswith("ch4") or
            rcv.startswith("ch5") or
            rcv.startswith('*')):
            pass

        # elif rcv.startswith("temp"):
        #     self.ProcessTempString(rcv)

        # elif rcv.startswith("ERROR"):
        #     self.ProcessErrorString(rcv)

        else:
            # el resto de los mensajes los paso directo a la pantalla
            self.InsertForeingText(rcv)
        
    
    
    def InsertLocalText (self, new_text):
        self.ui.textEdit.setTextColor(QColor(255, 0, 0))
        self.ui.textEdit.append(new_text)

        
    def InsertForeingText (self, new_text):
        self.ui.textEdit.setTextColor(QColor(0, 255, 0))
        self.ui.textEdit.append(new_text)
        

    def FinishThisDialog (self):
        # self.t1seg.cancel()
        self.accept()


    ####################################
    # Different Screens Calls are here #
    ####################################
    ## Steps Screen
    def StepsDialogScreen (self):
        ## llamo con referencia al main
        a = StepsDialog(self.parent)        
        a.setModal(True)
        a.exec_()

        ## continue with treatment
        self.treat.treatment_state = 'START'
        self.init_state = 'clean'
        self.SendResumeSM()

        
### end of file ###
