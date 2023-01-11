from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from time import sleep, time
from threading import Timer
from datetime import datetime


#get the UI from here
from ui_treatment_dlg import Ui_TreatmentDialog


#####################################################
# TreatmentDialog Class - to get the system running #
#####################################################
class TreatmentDialog(QDialog):

    #SIGNALS
    # signal to update in 1 second
    one_second_signal = pyqtSignal()
    # progress_signal = pyqtSignal()

    def __init__(self, stages_lst, treat_obj, style_obj, ant_obj, ser_instance, parent=None):
        super(TreatmentDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_TreatmentDialog()
        self.ui.setupUi(self)

        # get the parent reference and data
        self.parent = parent
        self.stages_lst = stages_lst
        self.treat = treat_obj
        self.style = style_obj
        self.ant = ant_obj
        self.s = ser_instance
        
        # get the close event and connect the buttons
        self.ui.doneButton.clicked.connect(self.FinishThisDialog)
        self.ui.stop_rsmButton.clicked.connect(self.StopRsmTreatment)
        self.ui.stopButton.clicked.connect(self.StopTreatment)
        self.ui.rsmButton.clicked.connect(self.RsmTreatment)        
        self.ui.ant1Button.clicked.connect(self.ChannelGetTemp)
        self.ui.ant2Button.clicked.connect(self.ChannelGetTemp)
        self.ui.ant3Button.clicked.connect(self.ChannelGetTemp)
        self.ui.ant4Button.clicked.connect(self.ChannelGetTemp)
        
        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        # progress timer, these ones are qt
        self.progress_timer = QTimer()
        self.init_timer = QTimer()
        self.t1sec = QTimer()
        self.change_timer = QTimer()        

        # progress states machine -SM-
        self.stop_rsm_state = 'stoping'
        self.init_state = 'start'
        self.change_state = ''

        ## setup temperatures
        self.temp_ch1_str = ''
        self.temp_ch2_str = ''
        self.temp_ch3_str = ''
        self.temp_ch4_str = ''

        self.tempLabelCntr = 0
        self.ui.tempLabel.setText('')

        self.style_bkg_enable = "background-color: rgb(191, 211, 199);\
                                 border-radius: 20px;\
                                 border:3px solid rgb(191, 211, 199);"
        
        self.style_bkg_disable = "background-color: rgba(255, 255, 255, 0);\
                                  border:0px"

        self.style_pwrlabel_enable = "color: rgb(237, 50, 55);"
        
        self.style_pwrlabel_disable = "color: rgb(234, 197, 218);"

        self.style_minlabel_enable = "color: rgb(55, 52, 53);"

        self.style_minlabel_disable = "color: rgb(230, 231, 232);"

        self.style_signal_disable = "background-color: rgb(245, 245, 245);\
                                     border-radius: 20px;\
                                     border:3px solid rgb(230, 231, 232);"

        
        self.ui.doneButton.setEnabled(False)
        self.ui.doneButton.setText('')
        
        # CONNECT SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)
        # self.progress_signal.connect(self.UpdateProgressStopRsmSM)


        ## Default Screen
        self.stage1_info = self.stages_lst[0]
        self.stage2_info = self.stages_lst[1]
        self.stage3_info = self.stages_lst[2]
        
        self.ui.progressLabel.setText('Session Starting...')
        # stage1
        self.ui.stage1MinutesLabel.setText(str(self.stage1_info.GetStageTimer()) + "'")
        self.ui.stage1PowerLabel.setText(str(self.stage1_info.GetStagePower()) + "%")
        self.Stage1InnerSignalChange(self.stage1_info.GetStageSignal())
        self.Stage1InnerFreqChange(self.stage1_info.GetStageFrequency())
        # stage2
        self.ui.stage2MinutesLabel.setText(str(self.stage2_info.GetStageTimer()) + "'")
        self.ui.stage2PowerLabel.setText(str(self.stage2_info.GetStagePower()) + "%")
        self.Stage2InnerSignalChange(self.stage2_info.GetStageSignal())
        self.Stage2InnerFreqChange(self.stage2_info.GetStageFrequency())
        # stage3
        self.ui.stage3MinutesLabel.setText(str(self.stage3_info.GetStageTimer()) + "'")
        self.ui.stage3PowerLabel.setText(str(self.stage3_info.GetStagePower()) + "%")
        self.Stage3InnerSignalChange(self.stage3_info.GetStageSignal())
        self.Stage3InnerFreqChange(self.stage3_info.GetStageFrequency())

        self.ui.stage1BkgButton.lower()
        self.ui.stage2BkgButton.lower()
        self.ui.stage3BkgButton.lower()
            
        # self.ui.stage1MinutesLabel.raise_()
        # self.ui.stage1PowerLabel.raise_()
        # self.ui.stage1SignalButton.raise_()        
        # self.ui.stage1FreqButton.raise_()

        # self.ui.stage2MinutesLabel.raise_()
        # self.ui.stage2PowerLabel.raise_()
        # self.ui.stage2SignalButton.raise_()
        # self.ui.stage2FreqButton.raise_()

        self.ui.stage3MinutesLabel.raise_()
        self.ui.stage3PowerLabel.raise_()
        self.ui.stage3SignalButton.raise_()
        self.ui.stage3FreqButton.raise_()
        
        # current_signal = self.treat.GetSignal()
        # if current_signal == 'triangular':
        #     self.ui.signalButton.setStyleSheet(self.style.triangular_enable)
        # elif current_signal == 'square':
        #     self.ui.signalButton.setStyleSheet(self.style.square_enable)
        # elif current_signal == 'sinusoidal':
        #     self.ui.signalButton.setStyleSheet(self.style.sinusoidal_enable)

        # current_frequency = self.treat.GetFrequency()
        # if current_frequency == '7.83Hz':
        #     self.ui.freqButton.setStyleSheet(self.style.freq1_enable)
        # elif current_frequency == '11.79Hz':
        #     self.ui.freqButton.setStyleSheet(self.style.freq2_enable)
        # elif current_frequency == '16.67Hz':
        #     self.ui.freqButton.setStyleSheet(self.style.freq3_enable)
        # elif current_frequency == '23.58Hz':
        #     self.ui.freqButton.setStyleSheet(self.style.freq4_enable)
        # elif current_frequency == '30.80Hz':
        #     self.ui.freqButton.setStyleSheet(self.style.freq5_enable)
        # elif current_frequency == '62.64Hz':
        #     self.ui.freqButton.setStyleSheet(self.style.freq6_enable)

        self.ui.stopButton.setEnabled(False)
        self.ui.rsmButton.setEnabled(False)
        self.ui.stop_rsmButton.raise_()

        ## show the stages as config
        if self.stage1_info.GetStageStatus() == 'enable':
            self.StageBkgButtonEnable('stage1')
        elif self.stage2_info.GetStageStatus() == 'enable':
            self.StageBkgButtonEnable('stage2')
        else:
            self.StageBkgButtonEnable('stage3')

        if self.stage1_info.GetStageStatus() == 'enable':
            self.Stage1ChangeStatus('enable')
        else:
            self.Stage1ChangeStatus('disable')

        if self.stage2_info.GetStageStatus() == 'enable':
            self.Stage2ChangeStatus('enable')
        else:
            self.Stage2ChangeStatus('disable')

        if self.stage3_info.GetStageStatus() == 'enable':
            self.Stage3ChangeStatus('enable')
        else:
            self.Stage3ChangeStatus('disable')
            
        ## setup antennas icons
        ## url(:/buttons/resources/Stop.png)
        self.wifi_act_Icon = QIcon(':/buttons/resources/wifi-symbol_act.png')
        self.wifi_err_Icon = QIcon(':/buttons/resources/wifi-symbol_err.png')
        self.wifi_disa_Icon = QIcon(':/buttons/resources/wifi-symbol_disa.png')
        self.wifi_emit_Icon = QIcon(':/buttons/resources/wifi-symbol_emit.png')
        
        ## setup antennas
        self.antenna_emmiting = False
        self.AntennasUpdate_UI(False)
            
        ## start the timer
        self.t1sec.timeout.connect(self.TimerOneSec)
        self.t1sec.start(1000)

        ## Effectively start treatment
        self.StartTreatment()


    def Stage1ChangeStatus (self, new_status):
        if new_status == 'disable':
            self.Stage1InnerSignalChange('disable')
            self.Stage1InnerFreqChange('disable')
            self.ui.stage1MinutesLabel.setStyleSheet(self.style_minlabel_disable)
            self.ui.stage1PowerLabel.setStyleSheet(self.style_pwrlabel_disable)
        elif new_status == 'enable':
            self.Stage1InnerSignalChange(self.stage1_info.GetStageSignal())
            self.Stage1InnerFreqChange(self.stage1_info.GetStageFrequency())
            self.ui.stage1MinutesLabel.setStyleSheet(self.style_minlabel_enable)
            self.ui.stage1PowerLabel.setStyleSheet(self.style_pwrlabel_enable)


    def Stage2ChangeStatus (self, new_status):
        if new_status == 'disable':
            self.Stage2InnerSignalChange('disable')
            self.Stage2InnerFreqChange('disable')
            self.ui.stage2MinutesLabel.setStyleSheet(self.style_minlabel_disable)
            self.ui.stage2PowerLabel.setStyleSheet(self.style_pwrlabel_disable)
        elif new_status == 'enable':
            self.Stage2InnerSignalChange(self.stage2_info.GetStageSignal())
            self.Stage2InnerFreqChange(self.stage2_info.GetStageFrequency())
            self.ui.stage2MinutesLabel.setStyleSheet(self.style_minlabel_enable)
            self.ui.stage2PowerLabel.setStyleSheet(self.style_pwrlabel_enable)


    def Stage3ChangeStatus (self, new_status):
        if new_status == 'disable':
            self.Stage3InnerSignalChange('disable')
            self.Stage3InnerFreqChange('disable')
            self.ui.stage3MinutesLabel.setStyleSheet(self.style_minlabel_disable)
            self.ui.stage3PowerLabel.setStyleSheet(self.style_pwrlabel_disable)
        elif new_status == 'enable':
            self.Stage3InnerSignalChange(self.stage3_info.GetStageSignal())
            self.Stage3InnerFreqChange(self.stage3_info.GetStageFrequency())
            self.ui.stage3MinutesLabel.setStyleSheet(self.style_minlabel_enable)
            self.ui.stage3PowerLabel.setStyleSheet(self.style_pwrlabel_enable)
            

    def StageBkgButtonEnable (self, which_stage):
        if which_stage == 'stage1':
            self.ui.stage1BkgButton.setStyleSheet(self.style_bkg_enable)
            self.ui.stage2BkgButton.setStyleSheet(self.style_bkg_disable)
            self.ui.stage3BkgButton.setStyleSheet(self.style_bkg_disable)

        if which_stage == 'stage2':            
            self.ui.stage1BkgButton.setStyleSheet(self.style_bkg_disable)
            self.ui.stage2BkgButton.setStyleSheet(self.style_bkg_enable)
            self.ui.stage3BkgButton.setStyleSheet(self.style_bkg_disable)

        if which_stage == 'stage3':
            self.ui.stage1BkgButton.setStyleSheet(self.style_bkg_disable)
            self.ui.stage2BkgButton.setStyleSheet(self.style_bkg_disable)
            self.ui.stage3BkgButton.setStyleSheet(self.style_bkg_enable)

            
    def Stage1InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage1SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage1SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage1SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            # self.ui.stage1SignalButton.setStyleSheet(self.style.signal_75_disable)
            self.ui.stage1SignalButton.setStyleSheet(self.style_signal_disable)            


    def Stage2InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage2SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage2SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage2SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            # self.ui.stage2SignalButton.setStyleSheet(self.style.signal_75_disable)
            self.ui.stage2SignalButton.setStyleSheet(self.style_signal_disable)            


    def Stage3InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage3SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage3SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage3SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            # self.ui.stage3SignalButton.setStyleSheet(self.style.signal_75_disable)
            self.ui.stage3SignalButton.setStyleSheet(self.style_signal_disable)            
            
            
    def Stage1InnerFreqChange (self, new_freq):
        if new_freq == 'freq1':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq1_75_enable)
        elif new_freq == 'freq2':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq2_75_enable)
        elif new_freq == 'freq3':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq3_75_enable)
        elif new_freq == 'freq4':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq4_75_enable)
        elif new_freq == 'freq5':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq5_75_enable)
        elif new_freq == 'freq6':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq6_75_enable)
        elif new_freq == 'freq7':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq7_75_enable)
        elif new_freq == 'freq8':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq8_75_enable)
        elif new_freq == 'freq9':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq9_75_enable)
        elif new_freq == 'freq10':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq10_75_enable)
        else:
            # self.ui.stage1FreqButton.setStyleSheet(self.style.signal_75_disable)
            self.ui.stage1FreqButton.setStyleSheet(self.style_signal_disable)            


    def Stage2InnerFreqChange (self, new_freq):
        if new_freq == 'freq1':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq1_75_enable)
        elif new_freq == 'freq2':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq2_75_enable)
        elif new_freq == 'freq3':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq3_75_enable)
        elif new_freq == 'freq4':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq4_75_enable)
        elif new_freq == 'freq5':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq5_75_enable)
        elif new_freq == 'freq6':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq6_75_enable)
        elif new_freq == 'freq7':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq7_75_enable)
        elif new_freq == 'freq8':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq8_75_enable)
        elif new_freq == 'freq9':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq9_75_enable)
        elif new_freq == 'freq10':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq10_75_enable)
        else:
            # self.ui.stage2FreqButton.setStyleSheet(self.style.signal_75_disable)
            self.ui.stage2FreqButton.setStyleSheet(self.style_signal_disable)            


    def Stage3InnerFreqChange (self, new_freq):
        if new_freq == 'freq1':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq1_75_enable)
        elif new_freq == 'freq2':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq2_75_enable)
        elif new_freq == 'freq3':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq3_75_enable)
        elif new_freq == 'freq4':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq4_75_enable)
        elif new_freq == 'freq5':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq5_75_enable)
        elif new_freq == 'freq6':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq6_75_enable)
        elif new_freq == 'freq7':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq7_75_enable)
        elif new_freq == 'freq8':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq8_75_enable)
        elif new_freq == 'freq9':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq9_75_enable)
        elif new_freq == 'freq10':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq10_75_enable)
        else:
            # self.ui.stage3FreqButton.setStyleSheet(self.style.signal_75_disable)
            self.ui.stage3FreqButton.setStyleSheet(self.style_signal_disable)            


    def AntennasUpdate_UI (self, emit):
        if emit == True:
            current_icon = self.wifi_emit_Icon
        else:
            current_icon = self.wifi_act_Icon

        if self.ant.GetActive('ch1') == True:
            self.ui.ant1Button.setIcon(current_icon)

        if self.ant.GetActive('ch2') == True:
            self.ui.ant2Button.setIcon(current_icon)

        if self.ant.GetActive('ch3') == True:
            self.ui.ant3Button.setIcon(current_icon)

        if self.ant.GetActive('ch4') == True:
            self.ui.ant4Button.setIcon(current_icon)

            
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


    def UpdateOneSec (self):
        # do a UI update if its necessary
        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)

        if self.treat.treatment_state == 'START':
            if self.CheckForStageChange() != True:
                self.UpdateTimerAndLabels()

        if self.treat.treatment_state == 'ENDED':
            self.UpdateEndedLabels()


    def StartTreatment (self):
        print(self.treat.treatment_state)
        if self.treat.treatment_state == 'STOP':
            total_mins = 0
            active_stages = 0
            seconds_stage1 = 0
            seconds_stage2 = 0
            seconds_stage3 = 0            
            if self.stages_lst[0].GetStageStatus() == 'enable':
                t = self.stages_lst[0].GetStageTimer()
                total_mins += t
                seconds_stage1 = t * 60

            if self.stages_lst[1].GetStageStatus() == 'enable':
                t = self.stages_lst[1].GetStageTimer()
                total_mins += t
                seconds_stage2 = t * 60

            if self.stages_lst[2].GetStageStatus() == 'enable':
                t = self.stages_lst[2].GetStageTimer()
                total_mins += t
                seconds_stage3 = t * 60

            # total_mins got it
            stages_to_change = ['', '', '']
            seconds_to_change = [0, 0, 0]            
            seconds_accum = 0
            index = 0
            total_secs = total_mins * 60
            if seconds_stage1:
                seconds_accum += seconds_stage1
                seconds_to_change[index] = total_secs - seconds_accum
                stages_to_change[index] = 'stage1'
                index += 1
                
            if seconds_stage2:
                seconds_accum += seconds_stage2
                seconds_to_change[index] = total_secs - seconds_accum
                stages_to_change[index] = 'stage2'                
                index += 1

            if seconds_stage3:
                seconds_accum += seconds_stage3
                seconds_to_change[index] = total_secs - seconds_accum
                stages_to_change[index] = 'stage3'                

            self.seconds_to_change = seconds_to_change
            self.stages_to_change = stages_to_change
            self.stage_changes = index
            self.current_index = 0
            print(self.seconds_to_change)
            print(self.stages_to_change)
            print(self.stage_changes)
            
            self.ui.remaining_minsLabel.setText(str(total_mins) + "'")
            self.ui.remaining_secsLabel.setText("00''")
            self.treat.remaining_minutes = total_mins
            self.treat.remaining_seconds = 0

            self.init_state = 'clean'
            self.SendStartSM()

            self.treat.treatment_state = 'START'
            self.ui.progressLabel.setText('Session in Progress')


    def SendStartSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'signal'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'signal':
            # check which stage info to send
            if self.stages_to_change[self.current_index] == 'stage1':
                to_send = self.GetMagnetoFreqSignalPowerString(self.stages_lst[0], self.treat)
            elif self.stages_to_change[self.current_index] == 'stage2':
                to_send = self.GetMagnetoFreqSignalPowerString(self.stages_lst[1], self.treat)
            elif self.stages_to_change[self.current_index] == 'stage3':
                to_send = self.GetMagnetoFreqSignalPowerString(self.stages_lst[2], self.treat)
            else:
                print ('Fatal error, no good stage to send on StartSM - signal!!!')
                return
                
            self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'duration'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'duration':
            # check which stage info to send
            if self.stages_to_change[self.current_index] == 'stage1':
                to_send = self.GetMagnetoDurationString(self.stages_lst[0].GetStageTimer())
            elif self.stages_to_change[self.current_index] == 'stage2':
                to_send = self.GetMagnetoDurationString(self.stages_lst[1].GetStageTimer())                
            elif self.stages_to_change[self.current_index] == 'stage3':
                to_send = self.GetMagnetoDurationString(self.stages_lst[2].GetStageTimer())                
            else:
                print ('Fatal error, no good stage to send on StartSM - duration!!!')
                return

            self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'state_of_stage'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'state_of_stage':
            to_send = "state_of_stage,1,1"
            self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'start'
            self.init_timer.singleShot(100, self.SendStartSM)
                
        elif self.init_state == 'start':
            self.InsertInfoText("Starting Treatment...")
            self.s.Write("start,\r\n")
            

    def SendPauseSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'pause'
            self.init_timer.singleShot(100, self.SendPauseSM)

        elif self.init_state == 'pause':
            self.s.Write("pause,1\r\n")                
            self.InsertInfoText("Pausing Treatment...")

            
    def SendResumeSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'resume'
            self.init_timer.singleShot(100, self.SendResumeSM)

        elif self.init_state == 'resume':
            self.s.Write("pause,0\r\n")                
            self.InsertInfoText("Resuming Treatment...")
                
            
    # def SendStopSM (self, how_many_bips=3):
    def SendStopSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'stop'
            self.init_timer.singleShot(100, self.SendStopSM)

        elif self.init_state == 'stop':
            self.s.Write("stop,\r\n")                
            self.InsertInfoText("STOP Treatment")

            self.init_state = 'stop_bips'
            self.init_timer.singleShot(100, self.SendStopSM)
            
        elif self.init_state == 'stop_bips':
            # self.s.Write("buzzer short {d},\r\n".format(how_many_bips))
            self.s.Write("buzzer short 3,\r\n")            


    def SendStopNoBuzzerSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'stop'
            self.init_timer.singleShot(100, self.SendStopNoBuzzerSM)

        elif self.init_state == 'stop':
            self.s.Write("stop,\r\n")                
            self.InsertInfoText("STOP Treatment")

            
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

            if self.antenna_emmiting == True:
                self.antenna_emmiting = False
                self.AntennasUpdate_UI(False)
            else:
                self.antenna_emmiting = True
                self.AntennasUpdate_UI(True)

            if self.tempLabelCntr > 0:
                self.tempLabelCntr -= 1
            else:
                self.ui.tempLabel.setText('')
            
        else:
            # termino el tratamiento, hago algo parecido al boton stop
            self.treat.treatment_state = 'STOP'
            self.ui.remaining_secsLabel.setText("0''")
            self.ui.progressLabel.setStyleSheet(self.style.label_blue)
            self.stop_rsm_state = 'ending'
            self.progress_timer.singleShot(300, self.ProgressEndSM)

            self.init_state = 'clean'
            self.SendStopSM()        

            
    def UpdateEndedLabels (self):
        if self.ui.doneButton.text() == '':
            self.ui.doneButton.setText('Tap to return to a previous screen')
        else:
            self.ui.doneButton.setText('')
            
        
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


    """ possible states from stop_rsmButton pausing, paused """
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
            self.AntennasUpdate_UI(False)


    """ possible states from rsmButton resuming, resumed """
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


    """ possible states from stopButton stoping, stoped """
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
    

    ##############################
    # Change of Stages Functions #
    ##############################
    def CheckForStageChange (self):
        change_is_needed = False
        if self.current_index < self.stage_changes:
            remain_secs = self.treat.remaining_minutes * 60 + self.treat.remaining_seconds
            if remain_secs <= self.seconds_to_change[self.current_index] and \
               self.seconds_to_change[self.current_index] != 0:
                self.current_index += 1
                print('go to change ' + self.stages_to_change[self.current_index] + \
                      'remain secs: ' + str(remain_secs))

                # change the bkg button to the current stage
                self.StageBkgButtonEnable(self.stages_to_change[self.current_index])
                self.init_state = 'clean'
                self.SendStopNoBuzzerSM()

                self.treat.treatment_state = 'CHANGING'
                self.change_state = self.stages_to_change[self.current_index]                
                self.change_timer.singleShot(200, self.SendStartChangingStages)                
                change_is_needed = True

        return change_is_needed


    def SendStartChangingStages (self):
        if self.change_state == 'stage1' or \
           self.change_state == 'stage2' or \
           self.change_state == 'stage3':
            # first check the end of previus process
            if self.init_state != 'stop' or self.treat.treatment_state != 'CHANGING':
                print ('error waiting for know state before change stages!!!')
                return

            # change to next stage
            self.init_state = 'clean'
            self.SendStartSM()

            self.change_state = 'change_done'
            self.change_timer.singleShot(200, self.SendStartChangingStages)

        elif self.change_state == 'change_done':
            self.treat.treatment_state = 'START'
        else:
            print('No good stage to change to!!!')


        
    ####################
    # Serial Functions #
    ####################    
    def SerialDataCallback (self, rcv):        
        print ("serial data callback!")
        self.SerialProcessString(rcv)
                

    def SerialProcessString (self, rcv):
        # self.ui.textEdit.append(rcv)
        # reviso si es un final de tratamiento
        # if rcv.startswith("treat end,") or rcv.startswith("treat err,"):
        if rcv.startswith("STOP") or rcv.startswith("finish,"):
        
            if self.treat.treatment_state == 'START':
                # termino el tratamiento, hago algo parecido al boton stop
                self.treat.treatment_state = 'STOP'
                self.InsertLocalText("Ended or Stopped Treatment")
                self.ui.progressLabel.setStyleSheet(self.style.label_red)
                self.stop_rsm_state = 'ending'
                self.progress_timer.singleShot(300, self.ProgressEndSM)

        elif rcv.startswith("temp"):
            self.ProcessTempString(rcv)

        elif rcv.startswith("ERROR"):
            self.ProcessErrorString(rcv)

        elif rcv.startswith("new antenna ch"):
            pass
            
        else:
            # el resto de los mensajes los paso directo a la pantalla
            # self.ui.textEdit.append(rcv)
            self.InsertForeingText(rcv)
        
    
    # temp,055.00,1\r
    def ProcessTempString(self, temp_str):
        temp_list = temp_str.split(',')
        if len(temp_list) < 3:
            return

        try:
            temp_ch = float(temp_list[1])
            temp_ch_str = str(temp_ch)

            if temp_list[2].startswith('1'):
                self.temp_ch1_str = temp_ch_str

            if temp_list[2].startswith('2'):
                self.temp_ch2_str = temp_ch_str

            if temp_list[2].startswith('3'):
                self.temp_ch3_str = temp_ch_str

            if temp_list[2].startswith('4'):
                self.temp_ch4_str = temp_ch_str

        except:
            print('Noisy Line for floats values')


    # ERROR(0x054)\r
    def ProcessErrorString(self, error_str):
        error_list = error_str.split('x')
        if len(error_list) < 2:
            return
        
        error_ch = error_list[1]
        error_type = error_ch[1]
        error_channel = error_ch[2]
        print('Error in ch' + error_channel)
        self.InsertForeingText(error_str)

        current_icon = self.wifi_err_Icon

        if error_channel.startswith('1') and self.ant.GetActive('ch1') == True:
            self.ant.SetActiveStatus('ch1', False)
            self.ui.ant1Button.setIcon(current_icon)

        if error_channel.startswith('2') and self.ant.GetActive('ch2') == True:
            self.ant.SetActiveStatus('ch2', False)
            self.ui.ant2Button.setIcon(current_icon)

        if error_channel.startswith('3') and self.ant.GetActive('ch3') == True:
            self.ant.SetActiveStatus('ch3', False)
            self.ui.ant3Button.setIcon(current_icon)

        if error_channel.startswith('4') and self.ant.GetActive('ch4') == True:
            self.ant.SetActiveStatus('ch4', False)
            self.ui.ant4Button.setIcon(current_icon)
            
            
    def ChannelGetTemp (self):
        sender = self.sender()

        if sender.objectName() == 'ant1Button':
            self.ui.tempLabel.setText('CH1 Temp: ' + self.temp_ch1_str + 'C')
            self.tempLabelCntr = 3

        if sender.objectName() == 'ant2Button':
            self.ui.tempLabel.setText('CH2 Temp: ' + self.temp_ch2_str + 'C')
            self.tempLabelCntr = 3            

        if sender.objectName() == 'ant3Button':
            self.ui.tempLabel.setText('CH3 Temp: ' + self.temp_ch3_str + 'C')
            self.tempLabelCntr = 3            

        if sender.objectName() == 'ant4Button':
            # ant_str = "temp,055.00,1\r"
            # self.SerialProcessString(ant_str)
            # ant_str = "ERROR(0x54)\r"
            # self.SerialProcessString(ant_str)
            self.ui.tempLabel.setText('CH4 Temp: ' + self.temp_ch4_str + 'C')
            self.tempLabelCntr = 3            
            

    #######################
    # Text Edit Functions #
    #######################
    def InsertColorText (self, new_text, color='red'):
        if color == 'red':
            self.ui.textEdit.setTextColor(QColor(237, 50, 55))            

        if color == 'blue':
            self.ui.textEdit.setTextColor(QColor(62, 64, 149))

        if color == 'green':
            self.ui.textEdit.setTextColor(QColor(0, 168, 89))

        self.ui.textEdit.append(new_text)
        
            
    def InsertLocalText (self, new_text):
        self.InsertColorText(new_text, 'red')

        
    def InsertInfoText (self, new_text):
        self.InsertColorText(new_text, 'blue')

        
    def InsertForeingText (self, new_text):
        self.InsertColorText(new_text, 'green')


    def FinishThisDialog (self):
        # self.t1seg.cancel()
        self.accept()


    #######################################################
    # String Utils Functions - Convert Treatments strings #
    #######################################################
    def GetMagnetoFreqSignalPowerString (self, stage_obj, treat_obj):
        """ 
            Devuelve un string con toda la info combinada para el Magneto viejo 
            Incluye las nuevas 10 frecuencias
            "signal,%03d,%03d,0%x%x%d,%04d,%04d,%04d,%04d,%04d,%04d,1\r\n"
            example. signal,100,100,0000,0003,0003,0003,0006,0000,0000,1
        """        
        treat = "signal,"

        signal = stage_obj.GetStageSignal()
        power = stage_obj.GetStagePower()
        frequency = stage_obj.GetStageFrequency()

        if signal == 'square':
            new_power = int(treat_obj.square_power_limit * power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time
            if frequency == 'freq1':    #0.98Hz
                treat += '0001,0498,0001,0500,0000,0000,1'
            if frequency == 'freq2':    #1.96Hz
                treat += '0001,0253,0001,0255,0000,0000,1'
            if frequency == 'freq3':    #3.92Hz
                treat += '0001,0125,0001,0128,0000,0000,1'
            if frequency == 'freq4':    #7.83Hz
                treat += '0001,0061,0001,0064,0000,0000,1'
            if frequency == 'freq5':    #11.79Hz
                treat += '0001,0040,0001,0043,0000,0000,1'
            if frequency == 'freq6':    #16.67Hz
                treat += '0001,0028,0001,0030,0000,0000,1'
            if frequency == 'freq7':    #23.58Hz
                treat += '0001,0019,0001,0021,0000,0000,1'
            if frequency == 'freq8':    #30.80Hz
                treat += '0001,0014,0001,0016,0000,0000,1'
            if frequency == 'freq9':    #62.64Hz
                treat += '0001,0006,0001,0008,0000,0000,1'
            if frequency == 'freq10':    #86.22Hz
                treat += '0001,0004,0001,0006,0000,0000,1'
                

        if signal == 'triangular':
            new_power = int(treat_obj.triangular_power_limit * power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if frequency == 'freq1':    #0.98Hz
                treat += '0498,0001,0001,0500,0000,0000,1'
            if frequency == 'freq2':    #1.96Hz
                treat += '0253,0001,0001,0255,0000,0000,1'
            if frequency == 'freq3':    #3.92Hz
                treat += '0125,0001,0001,0128,0000,0000,1'
            if frequency == 'freq4':    #7.83Hz
                treat += '0061,0001,0001,0064,0000,0000,1'
            if frequency == 'freq5':    #11.79Hz
                treat += '0040,0001,0001,0043,0000,0000,1'
            if frequency == 'freq6':    #16.67Hz
                treat += '0028,0001,0001,0030,0000,0000,1'
            if frequency == 'freq7':    #23.58Hz
                treat += '0019,0001,0001,0021,0000,0000,1'
            if frequency == 'freq8':    #30.80Hz
                treat += '0014,0001,0001,0016,0000,0000,1'
            if frequency == 'freq9':    #62.64Hz
                treat += '0006,0001,0001,0008,0000,0000,1'
            if frequency == 'freq10':    #86.22Hz
                treat += '0004,0001,0001,0006,0000,0000,1'

        if signal == 'sinusoidal':
            new_power = int(treat_obj.sinusoidal_power_limit * power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if frequency == 'freq1':    #0.98Hz
                treat += '0166,0166,0166,0500,0000,0000,1'
            if frequency == 'freq2':    #1.96Hz
                treat += '0085,0085,0085,0255,0000,0000,1'
            if frequency == 'freq3':    #3.92Hz
                treat += '0042,0042,0042,0128,0000,0000,1'
            if frequency == 'freq4':    #7.83Hz
                treat += '0021,0021,0021,0064,0000,0000,1'
            if frequency == 'freq5':    #11.79Hz
                treat += '0014,0014,0014,0043,0000,0000,1'
            if frequency == 'freq6':    #16.67Hz
                treat += '0010,0010,0010,0030,0000,0000,1'
            if frequency == 'freq7':    #23.58Hz
                treat += '0007,0007,0007,0021,0000,0000,1'
            if frequency == 'freq8':    #30.80Hz
                treat += '0005,0006,0005,0016,0000,0000,1'
            if frequency == 'freq9':    #62.64Hz
                treat += '0003,0002,0003,0008,0000,0000,1'
            if frequency == 'freq10':    #86.22Hz
                treat += '0002,0002,0002,0006,0000,0000,1'

        return treat


    def GetMagnetoDurationString (self, timer):
        treat_time = 'duration,00,{:02d},00,1'.format(timer)
        return treat_time
    
### end of file ###
