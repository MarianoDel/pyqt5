from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor
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

        # get the close event and connect the buttons
        self.ui.signalButton.clicked.connect(self.accept)
        self.ui.stop_rsmButton.clicked.connect(self.StopRsmTreatment)
        self.ui.stopButton.clicked.connect(self.StopTreatment)
        self.ui.rsmButton.clicked.connect(self.RsmTreatment)        

        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        # to start 1 second timer
        self.next_call = time()
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()

        # progress timer, this one is qt
        self.progress_timer = QTimer()
        self.init_timer = QTimer()

        # progress states machine -SM-
        self.stop_rsm_state = 'stoping'
        self.init_state = 'start'

        # CONNECT SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)
        # self.progress_signal.connect(self.UpdateProgressStopRsmSM)


        ## Default Screen
        self.ui.progressLabel.setText('Session Starting...')
        self.ui.minutesLabel.setText(str(self.treat.treatment_timer) + "'")
        self.ui.powerLabel.setText(str(self.treat.power) + "%")

        current_signal = self.treat.GetSignal()
        if current_signal == 'triangular':
            self.ui.signalButton.setStyleSheet(self.style.triangular_enable)
        elif current_signal == 'square':
            self.ui.signalButton.setStyleSheet(self.style.square_enable)
        elif current_signal == 'sinusoidal':
            self.ui.signalButton.setStyleSheet(self.style.sinusoidal_enable)

        current_frequency = self.treat.GetFrequency()
        if current_frequency == '7.83Hz':
            self.ui.freqButton.setStyleSheet(self.style.freq1_enable)
        elif current_frequency == '11.79Hz':
            self.ui.freqButton.setStyleSheet(self.style.freq2_enable)
        elif current_frequency == '16.67Hz':
            self.ui.freqButton.setStyleSheet(self.style.freq3_enable)
        elif current_frequency == '23.58Hz':
            self.ui.freqButton.setStyleSheet(self.style.freq4_enable)
        elif current_frequency == '30.80Hz':
            self.ui.freqButton.setStyleSheet(self.style.freq5_enable)
        elif current_frequency == '62.64Hz':
            self.ui.freqButton.setStyleSheet(self.style.freq6_enable)

        self.ui.stopButton.setEnabled(False)
        self.ui.rsmButton.setEnabled(False)
        self.ui.stop_rsmButton.raise_()
        ## Effectively start treatment
        self.StartTreatment()

        
    def UpdateDateTime(self, new_date_time):
        date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
        self.ui.date_timeLabel.setText(date_str)


        """ This runs in other thread is a better idea to use a signal to change the UI """
    def TimerOneSec(self, lapse):
        self.next_call = self.next_call + 1        
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        # do a UI update if its necessary
        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)

        if self.treat.treatment_state == 'START':
            self.UpdateTimerAndLabels()


    def StartTreatment (self):
        print(self.treat.treatment_state)
        if (self.treat.treatment_state == 'STOP'):

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
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'signal'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'signal':
            new_signal = self.treat.GetSignal()
            to_send = "signal " + new_signal
            self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'frequency'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'frequency':
            new_freq = self.treat.GetFrequency()
            new_freq = new_freq.split('Hz')
            new_freq = new_freq[0]
            new_freq_f = float(new_freq)
            if new_freq_f <= 5:
                to_send = "frequency " + "6.00Hz"
            elif new_freq_f >= 70:
                to_send = "frequency " + "65.00Hz"
            else:
                to_send = "frequency {:.02f}Hz".format(new_freq_f)

            self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'power'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'power':
            this_signal = self.treat.GetSignal()
            new_power_limit = self.treat.GetPowerLimit(this_signal)
            new_power = self.treat.GetPower()
            new_power = int(new_power * new_power_limit / 100)
            to_send = 'power {:03d}'.format(new_power)
            self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'channel1'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'channel1':
            if (self.treat.GetChannelInTreatment('ch1') == True):
                to_send = "enable channel 1"
                self.s.Write(to_send + "\r\n")                
            else:
                to_send = "disable channel 1"
                self.s.Write(to_send + "\r\n")
                    
            self.InsertLocalText(to_send)
            self.init_state = 'channel2'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'channel2':
            if (self.treat.GetChannelInTreatment('ch2') == True):
                to_send = "enable channel 2"
                self.s.Write(to_send + "\r\n")
            else:
                to_send = "disable channel 2"
                self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'channel3'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'channel3':
            if (self.treat.GetChannelInTreatment('ch3') == True):
                to_send = "enable channel 3"
                self.s.Write(to_send + "\r\n")
            else:
                to_send = "disable channel 3"
                self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'duration'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'duration':
            new_timer = self.treat.GetTreatmentTimer()
            to_send = 'duration,00,{:02d},00,1'.format(new_timer)
            self.s.Write(to_send + "\r\n")

            self.InsertLocalText(to_send)
            self.init_state = 'start'
            self.init_timer.singleShot(100, self.SendStartSM)

        elif self.init_state == 'start':
            self.InsertLocalText("Starting Treatment...")
            self.s.Write("start,\r\n")


    def SendPauseSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'pause'
            self.init_timer.singleShot(100, self.SendPauseSM)

        elif self.init_state == 'pause':
            self.s.Write("pause,1\r\n")                
            self.InsertLocalText("Pausing Treatment...")

            
    def SendResumeSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'resume'
            self.init_timer.singleShot(100, self.SendResumeSM)

        elif self.init_state == 'resume':
            self.s.Write("pause,0\r\n")                
            self.InsertLocalText("Resuming Treatment...")
            
            
    def SendStopSM (self):
        if self.init_state == 'clean':
            # limpio el puerto y luego la configuracion
            self.s.Write("keepalive,\r\n")
            
            self.init_state = 'stop'
            self.init_timer.singleShot(100, self.SendStopSM)

        elif self.init_state == 'stop':
            self.s.Write("stop,\r\n")                
            self.InsertLocalText("STOP Treatment")
            
            
    # def Stop_Treatment (self):
    #     if (self.s.port_open):
    #         if (self.t.treatment_state == 'START'):
    #             self.t.treatment_state = 'STOP'
    #             self.EnableForTreatment()
    #             self.ui.textEdit.append("STOP Treatment")

    #             # limpio el puerto y mando terminacion
    #             self.s.Write("keepalive,\r\n")
    #             sleep(0.1)
    #             self.s.Write("stop,\r\n")
    #             sleep(1)
    #     else:
    #         self.ui.textEdit.append("Port not Open!!!")
            

    # def Pause_Treatment (self):
    #     if (self.s.port_open):
    #         if (self.t.treatment_state == 'START'):
    #             self.t.treatment_state = 'PAUSE'
    #             self.ui.stopButton.setEnabled(False)
    #             self.ui.pauseButton.setText("RESUME")                
    #             self.ui.textEdit.append("Pausing Treatment...")
    #             # limpio el puerto y mando la pausa                
    #             self.s.Write("keepalive,\r\n")
    #             sleep(0.1)
    #             self.s.Write("pause,1\r\n")                
    #             sleep(0.1)
                
    #         elif (self.t.treatment_state == 'PAUSE'):
    #             self.t.treatment_state = 'START'
    #             self.ui.stopButton.setEnabled(True)
    #             self.ui.pauseButton.setText("PAUSE")
    #             self.ui.textEdit.append("Resuming Treatment...")
    #             # limpio el puerto y mando la pausa                
    #             self.s.Write("keepalive,\r\n")
    #             sleep(0.1)
    #             self.s.Write("pause,0\r\n")                
    #             sleep(0.1)                
    #     else:
    #         self.ui.textEdit.append("Port not Open!!!")            

        
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
            
        else:
            # termino el tratamiento, hago algo parecido al boton stop
            self.treat.treatment_state = 'STOP'
            self.ui.textEdit.append("STOP Treatment")
            self.ui.progressLabel.setStyleSheet(self.style.label_blue)
            self.stop_rsm_state = 'ending'
            self.progress_timer.singleShot(300, self.ProgressEndSM)


            # # limpio el puerto y mando terminacion
            # self.s.Write("keepalive,\r\n")
            # sleep(0.1)
            # self.s.Write("finish_ok,\r\n")
            # sleep(1)

    def StopRsmTreatment(self):
        self.treat.treatment_state = 'PAUSE'
        self.ui.stop_rsmButton.setEnabled(False)
        self.ui.stop_rsmButton.setStyleSheet(self.style.stop_rsm_disable)
        self.ui.stopButton.raise_()
        self.ui.rsmButton.raise_()

        self.stop_rsm_state = 'pausing'
        self.progress_timer.singleShot(300, self.ProgressStopRsmSM)

        self.init_state = 'clean'
        self.SendPauseSM()
        
        
    def StopTreatment(self):
        self.stop_rsm_state = 'stoping'
        self.progress_timer.singleShot(300, self.ProgressStopSM)

        self.init_state = 'clean'
        self.SendStopSM()        


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
            self.accept()


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
            self.accept()


    def SerialDataCallback (self, rcv):
        print ("serial data callback!")
        # self.ui.textEdit.append(rcv)
        # reviso si es un final de tratamiento
        # if rcv.startswith("treat end,") or rcv.startswith("treat err,"):
        if rcv.startswith("STOP") or rcv.startswith("finish,"):
        
            if self.treat.treatment_state == 'START':
                # termino el tratamiento, hago algo parecido al boton stop
                self.treat.treatment_state = 'STOP'
                self.InsertLocalText("Ended or Stopped Treatment")
                # self.s.Write("stop,\r\n")
                # sleep(1)
        else:
            # el resto de los mensajes los paso directo a la pantalla
            # self.ui.textEdit.append(rcv)
            self.InsertForeingText(rcv)
                

    def InsertLocalText (self, new_text):
        self.ui.textEdit.setTextColor(QColor(255, 0, 0))
        self.ui.textEdit.append(new_text)

        
    def InsertForeingText (self, new_text):
        self.ui.textEdit.setTextColor(QColor(0, 255, 0))
        self.ui.textEdit.append(new_text)
        


        
### end of file ###
