import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from serialcomm import SerialComm
from treatment_class import Treatment
from stylesheet_class import ButtonStyles
from time import sleep, time
from datetime import datetime
import platform
import os

#para el timer de 1 segundo
from threading import Timer

#importo las UIs
from ui_stretcher import Ui_Dialog
# from ui_stretcher_diag import Ui_DiagnosticsDialog
# from ui_stretcher_rtc import Ui_RtcDialog


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
## what to do with the info
USE_RTC_STRING_FOR_PRINT = 0
USE_RTC_STRING_FOR_COMMAND = 1
## This Interface Software version
CURRENT_VERSION = "Stretcher ver_3_1"

### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

    # receivedData = pyqtSignal()
    

##################################################
# RtcDialog Class - to set the RTC on the system #
##################################################
# class RtcDialog(QDialog):
#     def __init__(self, ser_instance):
#         super(RtcDialog, self).__init__()

#         # Set up the user interface from Designer.
#         self.ui = Ui_RtcDialog()
#         self.ui.setupUi(self)

#         self.ui.doneButton.clicked.connect(self.accept)

#         self.ui.UpButton.clicked.connect(self.UpBtn)
#         self.ui.DwnButton.clicked.connect(self.DwnBtn)

#         self.ui.dayButton.clicked.connect(self.ChangeFocusDay)
#         self.ui.monthButton.clicked.connect(self.ChangeFocusMonth)
#         self.ui.yearButton.clicked.connect(self.ChangeFocusYear)
#         self.ui.hourButton.clicked.connect(self.ChangeFocusHour)
#         self.ui.minuteButton.clicked.connect(self.ChangeFocusMinute)
#         self.new_focus = "DAY"


#     def UpBtn (self, event=None):
#         day = int(self.ui.dayButton.text())
#         month = int(self.ui.monthButton.text())
#         year = int(self.ui.yearButton.text())
#         hour = int(self.ui.hourButton.text())
#         minute = int(self.ui.minuteButton.text())

#         if self.new_focus == "DAY":
#             if day < 31:
#                 day += 1

#         if self.new_focus == "MONTH":
#             if month < 12:
#                 month += 1

#         if self.new_focus == "YEAR":
#             if year < 99:
#                 year += 1
                
#         if self.new_focus == "HOUR":
#             if hour < 23:
#                 hour += 1

#         if self.new_focus == "MINUTE":
#             if minute < 59:
#                 minute += 1
                
#         self.UpdateNumbers(day, month, year, hour, minute)

        
#     def DwnBtn (self, event=None):
#         day = int(self.ui.dayButton.text())
#         month = int(self.ui.monthButton.text())
#         year = int(self.ui.yearButton.text())
#         hour = int(self.ui.hourButton.text())
#         minute = int(self.ui.minuteButton.text())
        
#         if self.new_focus == "DAY":
#             if day > 1:
#                 day -= 1

#         if self.new_focus == "MONTH":
#             if month > 1:
#                 month -= 1

#         if self.new_focus == "YEAR":
#             if year > 0:
#                 year -= 1
                
#         if self.new_focus == "HOUR":
#             if hour > 0:
#                 hour -= 1

#         if self.new_focus == "MINUTE":
#             if minute > 0:
#                 minute -= 1

#         self.UpdateNumbers(day, month, year, hour, minute)
        

#     def ChangeFocusDay (self):
#         self.ClearFocus()
#         self.new_focus = "DAY"
#         self.ui.dayButton.setStyleSheet("background-color: rgb(170, 170, 255);\
#                                          border: 0px;")


#     def ChangeFocusMonth (self):
#         self.ClearFocus()
#         self.new_focus = "MONTH"
#         self.ui.monthButton.setStyleSheet("background-color: rgb(170, 170, 255);\
#                                           border: 0px;")


#     def ChangeFocusYear (self):
#         self.ClearFocus()
#         self.new_focus = "YEAR"
#         self.ui.yearButton.setStyleSheet("background-color: rgb(170, 170, 255);\
#                                           border: 0px;")


#     def ChangeFocusHour (self):
#         self.ClearFocus()
#         self.new_focus = "HOUR"
#         self.ui.hourButton.setStyleSheet("background-color: rgb(170, 170, 255);\
#                                           border: 0px;")


#     def ChangeFocusMinute (self):
#         self.ClearFocus()
#         self.new_focus = "MINUTE"
#         self.ui.minuteButton.setStyleSheet("background-color: rgb(170, 170, 255);\
#                                             border: 0px;")

        
#     def ClearFocus (self):
#         self.ui.dayButton.setStyleSheet("background-color: rgb(255, 170, 255);\
#                                          border: 0px;")
#         self.ui.monthButton.setStyleSheet("background-color: rgb(255, 170, 255);\
#                                           border: 0px;")
#         self.ui.yearButton.setStyleSheet("background-color: rgb(255, 170, 255);\
#                                           border: 0px;")
#         self.ui.hourButton.setStyleSheet("background-color: rgb(255, 170, 255);\
#                                           border: 0px;")
#         self.ui.minuteButton.setStyleSheet("background-color: rgb(255, 170, 255);\
#                                             border: 0px;")


#     def UpdateNumbers (self, d, m, y, h, mm):
#         self.ui.dayButton.setText("{0:02d}".format(d))
#         self.ui.monthButton.setText("{0:02d}".format(m))
#         self.ui.yearButton.setText("{0:02d}".format(y))
#         self.ui.hourButton.setText("{0:02d}".format(h))
#         self.ui.minuteButton.setText("{0:02d}".format(mm))
#         # self.ui.dayButton.setText(f"{d:02d}")
#         # self.ui.monthButton.setText(f"{m:02d}")
#         # self.ui.yearButton.setText(f"{y:02d}")
#         # self.ui.hourButton.setText(f"{h:02d}")
#         # self.ui.minuteButton.setText(f"{mm:02d}")
        
### End of RtcDialog ###


#####################################################################
# DiagnosticsDialog Class - Secondary window for diagnostics checks #
#####################################################################
# class DiagDialog(QDialog):
#     def __init__(self, ser_instance):
#         super(DiagDialog, self).__init__()

#         # Set up the user interface from Designer.
#         self.ui = Ui_DiagnosticsDialog()
#         self.ui.setupUi(self)

#         self.ui.doneButton.clicked.connect(self.accept)

#         self.ser = ser_instance

#         #activo el timer de 2 segundos, la primera vez, luego se autollama
#         if self.ser.port_open == False:
#             self.ui.hardwareLabel.setText("No port  ")
#             self.ui.firmwareLabel.setText("No port  ")
#         else:
#             self.ui.hardwareLabel.setText("Waiting...  ")
#             self.ui.firmwareLabel.setText("Waiting...  ")
#             self.ser.Write("voltage\n")
#             # ser_instance.Write("get data\n")
#             self.next_call = time()
#             self.t3seg = Timer(self.next_call - time(), self.TimerThreeSec, [3]).start()

#         #recupero informacion del sistema
#         (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
#         # print(f"distname: {distname} version: {version} id: {nid}")
#         os_text = "--" + distname + version + "-- "
#         self.ui.osLabel.setText(os_text)

#         (system, node, release, version, machine, processor) = platform.uname()
#         # print(f"system: {system}, node: {node}, release: {release}, version: {version}, machine: {machine}, processor: {processor}")
#         self.ui.kernelLabel.setText(release)
#         self.ui.softLabel.setText(CURRENT_VERSION)

#     def TimerThreeSec (self, lapse):
#         """ 
#             aca tengo que resolver todo lo que se mueve 
#             lo hago tipo por estados del programa con treatmet_state
#         """
#         self.next_call = self.next_call + lapse
#         # #esto corre en otro thread entonces mando una senial para hacer update de la interface
#         # self.one_second_signal.emit()        
#         #antes de volver hago la proxima llamada
#         self.t3seg = Timer(self.next_call - time(), self.TimerThreeSec, [3]).start()
#         arrow = self.ser.Read()
#         print(arrow)
        


#     #     self.intfreq = 0

#     #     # # # Connect up the buttons.
#     #     self.ui.pushButton1.clicked.connect(self.UPFreq)
#     #     self.ui.pushButton2.clicked.connect(self.DWNFreq)
#     #     self.ui.endButton.clicked.connect(self.accept)


#     # def UPFreq (self, event=None):
#     #     if (self.intfreq < 10):
#     #         self.intfreq += 1

#     #     self.changeFreqLabel(self.intfreq)

#     # def DWNFreq (self, event=None):
#     #     if (self.intfreq > 1):
#     #         self.intfreq -= 1

#     #     self.changeFreqLabel(self.intfreq)

#     # def changeFreqLabel(self, new_f):
#     #     self.intfreq = new_f
#     #     self.ui.whatfreqLabel.setText(str(self.intfreq))
    
        
### End of DiagnosticsDialog ###


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
        
        # self.ui.startButton.clicked.connect(self.Start_Treatment)
    #     self.ui.stopButton.clicked.connect(self.Stop_Treatment)
    #     self.ui.pauseButton.clicked.connect(self.Pause_Treatment)

        ## Init treatment object
        self.t = Treatment()

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
        
    #     # #con el boton lanzo el evento close, que luego llama a closeEvent
    #     # self.ui.closeButton.clicked.connect(self.close)
    #     self.ui.textEdit.setText('')

    #     #creo el evento y lo conecto al slot
    #     self.c = Communicate()
    #     self.c.closeApp.connect(self.close) #Envio3 lo dispara

    #     #creo una senial de prueba y la conecto        
    #     self.rcv_signal.connect(self.MySignalCallback)

    #     #self.MyObjCallback la llaman desde otro thread, armo una senial
    #     #antes de modificar UI

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

    ############
    # Old Code #
    ############
    # """
    # chequea el boton de frecuencia y guarda el texto del mismo en el objeto treatment
    # normalmente 7.83Hz
    # """
    # def SetNewFreq (self):
    #     sender = self.sender()
    #     if (sender.isChecked() != True):
    #         sender.toggle()

    #     self.ui.textEdit.append(sender.text() + " selected")
    #     self.t.SetFrequency(sender.text())


    # def SignalEnableButton(self, button):
    #     if button == 'triangular':
    #         self.ui.triangularButton.setStyleSheet(self.ss.triangular_enable)
            
    #     elif button == 'square':
    #         self.ui.squareButton.setStyleSheet(self.ss.square_enable)
            
    #     elif button == 'sinusoidal':
    #         self.ui.sinusoidalButton.setStyleSheet(self.ss.sinusoidal_enable)


    # def FrequencyEnableButton(self, button):
    #     if button == 'freq1':
    #         self.ui.freq1Button.setStyleSheet(self.ss.freq1_enable)

    #     elif button == 'freq2':
    #         self.ui.freq2Button.setStyleSheet(self.ss.freq2_enable)

    #     elif button == 'freq3':
    #         self.ui.freq3Button.setStyleSheet(self.ss.freq3_enable)

    #     elif button == 'freq4':
    #         self.ui.freq4Button.setStyleSheet(self.ss.freq4_enable)

    #     elif button == 'freq5':
    #         self.ui.freq5Button.setStyleSheet(self.ss.freq5_enable)

    #     elif button == 'freq6':
    #         self.ui.freq6Button.setStyleSheet(self.ss.freq6_enable)

    # def StretcherUpOrDown (self):
    #     if USE_STRETCHER_UPDOWN_BUTTON:
    #         self.ui.textEdit.append("Stretcher UP or DOWN")
    #         if (self.s.port_open):
    #             self.s.Write("stretcher up\r\n")
    #         else:
    #             self.ui.textEdit.append("Port not Open!!!")

    #     elif USE_STRETCHER_DIAG_BUTTON:
    #         a = DiagDialog(self.s)
    #         a.setModal(True)
    #         # a.changeChannelLabel(sender.text())
    #         # a.changeLaserLabel(self.t.GetLaserPower(sender.text()))
    #         # a.changeLEDLabel(self.t.GetLedPower(sender.text()))

    #         # a.setWindowTitle("Seteo de Potencias")
    #         a.exec_()

    #     elif USE_STRETCHER_RTC_BUTTON:
    #         a = RtcDialog(self.s)
    #         a.setModal(True)

    #         date_now = datetime.today()
    #         a.ui.dayButton.setText(date_now.strftime("%d"))
    #         a.ui.monthButton.setText(date_now.strftime("%m"))
    #         a.ui.yearButton.setText(date_now.strftime("%y"))

    #         a.ui.hourButton.setText(date_now.strftime("%H"))
    #         a.ui.minuteButton.setText(date_now.strftime("%M"))            

    #         a.exec_()
    #         new_day = a.ui.dayButton.text()
    #         new_month = a.ui.monthButton.text()
    #         new_year = a.ui.yearButton.text()
    #         new_hour = a.ui.hourButton.text()
    #         new_minute = a.ui.minuteButton.text()
    #         # print(f"{new_day}/{new_month}/{new_year} {new_hour}:{new_minute}")
    #         myCmd = "sudo date -s {0}/{1}/20{2} {3}:{4}".format(new_day, new_month, new_year, new_hour, new_minute)
    #         if USE_RTC_STRING_FOR_PRINT:
    #             print(myCmd)
    #         elif USE_RTC_STRING_FOR_COMMAND:
    #             os.system(myCmd)

    ############
    # New Code #
    ############
    def SignalDisableAll(self):
        self.ui.triangularButton.setStyleSheet(self.ss.triangular_disable)
        self.ui.squareButton.setStyleSheet(self.ss.square_disable)
        self.ui.sinusoidalButton.setStyleSheet(self.ss.sinusoidal_disable)
                       

    def SignalChange (self):
        sender = self.sender()

        self.SignalDisableAll()
        
        if sender.objectName() == 'triangularButton':
            self.ui.triangularButton.setStyleSheet(self.ss.triangular_enable)
            self.t.SetSignal('triangular')

        elif sender.objectName() == 'squareButton':
            self.ui.squareButton.setStyleSheet(self.ss.square_enable)
            self.t.SetSignal('square')

        elif sender.objectName() == 'sinusoidalButton':
            self.ui.sinusoidalButton.setStyleSheet(self.ss.sinusoidal_enable)            
            self.t.SetSignal('sinusoidal')


    def FrequencyDisableAll(self):
        self.ui.freq1Button.setStyleSheet(self.ss.freq1_disable)
        self.ui.freq2Button.setStyleSheet(self.ss.freq2_disable)
        self.ui.freq3Button.setStyleSheet(self.ss.freq3_disable)
        self.ui.freq4Button.setStyleSheet(self.ss.freq4_disable)
        self.ui.freq5Button.setStyleSheet(self.ss.freq5_disable)
        self.ui.freq6Button.setStyleSheet(self.ss.freq6_disable)


    def FrequencyChange (self):
        sender = self.sender()

        self.FrequencyDisableAll()
        
        if sender.objectName() == 'freq1Button':
            self.ui.freq1Button.setStyleSheet(self.ss.freq1_enable)
            self.t.SetFrequency('7.83Hz')

        if sender.objectName() == 'freq2Button':
            self.ui.freq2Button.setStyleSheet(self.ss.freq2_enable)
            self.t.SetFrequency('11.79Hz')

        if sender.objectName() == 'freq3Button':
            self.ui.freq3Button.setStyleSheet(self.ss.freq3_enable)
            self.t.SetFrequency('16.67Hz')

        if sender.objectName() == 'freq4Button':
            self.ui.freq4Button.setStyleSheet(self.ss.freq4_enable)
            self.t.SetFrequency('23.58Hz')

        if sender.objectName() == 'freq5Button':
            self.ui.freq5Button.setStyleSheet(self.ss.freq5_enable)
            self.t.SetFrequency('30.80Hz')

        if sender.objectName() == 'freq6Button':
            self.ui.freq6Button.setStyleSheet(self.ss.freq6_enable)
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
                
        
    def TimeSet (self):
        sender = self.sender()
        
        if sender.objectName() == 'min30Button':
            self.ui.minutesLabel.setText('30')
            self.t.SetTreatmentTimer(30)

        elif sender.objectName() == 'min45Button':
            self.ui.minutesLabel.setText('45')
            self.t.SetTreatmentTimer(45)

        


    # def Start_Treatment (self):
    #     if (self.s.port_open):
    #         if (self.t.treatment_state == 'STOP'):

    #             #seteo el timer elegido
    #             # new_t = self.ui.minutesLabel.text()
    #             # self.t.SetTreatmentTimer(int(new_t))

    #             #arreglo para cuando seleccionan 1 minuto
    #             if self.t.GetTreatmentTimer() == 1:
    #                 self.ui.minutesLabel.setText("59")
    #                 self.ui.timeStringLabel.setText("seconds")
    #                 self.t.remaining_seconds = 59
    #                 self.t.remaining_minutes = 0
    #             else:
    #                 self.t.remaining_minutes = self.t.GetTreatmentTimer()
    #                 self.t.remaining_seconds = 0

    #             # limpio el puerto y luego la configuracion
    #             self.s.Write("keepalive,\r\n")
    #             sleep(0.1)

    #             new_signal = self.t.GetSignal()
    #             to_send = "signal " + new_signal
    #             self.ui.textEdit.append(to_send)
    #             self.s.Write(to_send + "\r\n")

    #             new_freq = self.t.GetFrequency()
    #             new_freq = new_freq.split('Hz')
    #             new_freq = new_freq[0]
    #             new_freq_f = float(new_freq)
    #             if new_freq_f <= 5:
    #                 to_send = "frequency " + "6.00Hz"
    #             elif new_freq_f >= 70:
    #                 to_send = "frequency " + "65.00Hz"
    #             else:
    #                 to_send = "frequency {:.02f}Hz".format(new_freq_f)

                    
    #             self.ui.textEdit.append(to_send)
    #             self.s.Write(to_send + "\r\n")

    #             new_power = self.t.GetPower()
    #             if USE_POWER_LIMIT:
    #                 if new_signal == 'triangular' or new_signal == 'sinusoidal':
    #                     new_power = int(new_power * 70 / 100)
    #                 else:
    #                     new_power = int(new_power * 50 / 100)

    #             to_send = 'power {:03d}'.format(new_power)
    #             self.ui.textEdit.append(to_send)
    #             self.s.Write(to_send + "\r\n")

    #             if (self.t.GetChannelInTreatment('ch1') == True):
    #                 to_send = "enable channel 1"
    #                 self.ui.textEdit.append(to_send)
    #                 self.s.Write(to_send + "\r\n")
    #             else:
    #                 to_send = "disable channel 1"
    #                 self.ui.textEdit.append(to_send)
    #                 self.s.Write(to_send + "\r\n")
                    

    #             if (self.t.GetChannelInTreatment('ch2') == True):
    #                 to_send = "enable channel 2"
    #                 self.ui.textEdit.append(to_send)
    #                 self.s.Write(to_send + "\r\n")
    #             else:
    #                 to_send = "disable channel 2"
    #                 self.ui.textEdit.append(to_send)
    #                 self.s.Write(to_send + "\r\n")
                    

    #             if (self.t.GetChannelInTreatment('ch3') == True):
    #                 to_send = "enable channel 3"
    #                 self.ui.textEdit.append(to_send)
    #                 self.s.Write(to_send + "\r\n")
    #             else:
    #                 to_send = "disable channel 3"
    #                 self.ui.textEdit.append(to_send)
    #                 self.s.Write(to_send + "\r\n")

    #             new_timer = self.t.GetTreatmentTimer()
    #             to_send = 'duration,00,{:02d},00,1'.format(new_timer)
    #             self.ui.textEdit.append(to_send)
    #             self.s.Write(to_send + "\r\n")
                
    #             self.ui.textEdit.append("Starting Treatment...")
    #             self.s.Write("start,\r\n")
    #             self.t.treatment_state = 'START'
    #             self.DisableForTreatment()

    #     else:
    #         self.ui.textEdit.append("Port not Open!!!")


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


    # def DisableForTreatment (self):
    #     # deshabilito botones que no se pueden tocar en tratamiento
    #     self.ui.startButton.setEnabled(False)
        
    #     self.ui.triangularButton.setEnabled(False)
    #     self.ui.cuadradaButton.setEnabled(False)
    #     self.ui.senoidalButton.setEnabled(False)
        
    #     self.ui.freq1Button.setEnabled(False)
    #     self.ui.freq2Button.setEnabled(False)
    #     self.ui.freq3Button.setEnabled(False)
    #     self.ui.freq4Button.setEnabled(False)
    #     self.ui.freq5Button.setEnabled(False)
    #     self.ui.freq6Button.setEnabled(False)

    #     self.ui.ch1Button.setEnabled(False)
    #     self.ui.ch2Button.setEnabled(False)
    #     self.ui.ch3Button.setEnabled(False)

    #     self.ui.powerUpButton.setEnabled(False)
    #     self.ui.powerDwnButton.setEnabled(False)
    #     self.ui.timeUpButton.setEnabled(False)
    #     self.ui.timeDwnButton.setEnabled(False)

    # def EnableForTreatment (self):
    #     # habilito botones que permiten elegir cosas fuera del tratamiento
    #     self.ui.startButton.setEnabled(True)
        
    #     self.ui.triangularButton.setEnabled(True)
    #     self.ui.cuadradaButton.setEnabled(True)
    #     self.ui.senoidalButton.setEnabled(True)
        
    #     self.ui.freq1Button.setEnabled(True)
    #     self.ui.freq2Button.setEnabled(True)
    #     self.ui.freq3Button.setEnabled(True)
    #     self.ui.freq4Button.setEnabled(True)
    #     self.ui.freq5Button.setEnabled(True)
    #     self.ui.freq6Button.setEnabled(True)

    #     self.ui.ch1Button.setEnabled(True)
    #     self.ui.ch2Button.setEnabled(True)
    #     self.ui.ch3Button.setEnabled(True)

    #     self.ui.powerUpButton.setEnabled(True)
    #     self.ui.powerDwnButton.setEnabled(True)
    #     self.ui.timeUpButton.setEnabled(True)
    #     self.ui.timeDwnButton.setEnabled(True)
    #     self.ui.minutesLabel.setText(str(self.t.GetTreatmentTimer()))
    #     self.ui.timeStringLabel.setText("minutes")


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
            
            
    # def UpdateTimerLabel (self):
    #     if self.t.remaining_minutes > 0:
    #         #si quedan minutos todavia
    #         if self.t.remaining_seconds > 0:
    #             self.t.remaining_seconds -= 1
    #         else:
    #             self.t.remaining_minutes -= 1
    #             self.t.remaining_seconds = 59

    #         #todos los segundos actualizo ui
    #         if self.t.remaining_minutes == 0:
    #             self.ui.minutesLabel.setText("59")
    #             self.ui.timeStringLabel.setText("seconds")
    #         else:
    #             self.ui.minutesLabel.setText(str('{}:{:02d}'.format(self.t.remaining_minutes, self.t.remaining_seconds)))

    #     else:
    #         #estoy en el ultimo minuto ya uso el contador remaining_seconds
    #         if self.t.remaining_seconds > 0:
    #             self.t.remaining_seconds -= 1
    #             self.ui.minutesLabel.setText(str(self.t.remaining_seconds))                
    #         else:
    #             # termino el tratamiento, hago algo parecido al boton stop
    #             self.t.treatment_state = 'STOP'
    #             self.EnableForTreatment()
    #             self.ui.textEdit.append("STOP Treatment")

    #             # limpio el puerto y mando terminacion
    #             self.s.Write("keepalive,\r\n")
    #             sleep(0.1)
    #             self.s.Write("finish_ok,\r\n")
    #             sleep(1)
                
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
        d = dataread[:-1]
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
