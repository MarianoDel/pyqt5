import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from serialcomm import SerialComm
from treatment_class import Treatment
from time import sleep, time
from datetime import datetime
import platform

#para el timer de 1 segundo
from threading import Timer

#importo las UIs
from ui_stretcher import Ui_Dialog
from ui_stretcher_diag import Ui_DiagnosticsDialog


"""
    Pruebas con seniales y eventos custom
    http://zetcode.com/gui/pyqt5/eventssignals/
"""

### GLOBALS FOR CONFIGURATION #########
## OS where its run
RUNNING_ON_SLACKWARE = 0
RUNNING_ON_RASP = 1
## Device where the interface is used
USE_FOR_MAGNETO = 0
USE_FOR_STRETCHER = 1
## Apply power limits to the antennas
USE_POWER_LIMIT = 1
## What to do with the Up/Down Button
USE_STRETCHER_UPDOWN_BUTTON = 0
USE_STRETCHER_DIAG_BUTTON = 1
## This Interface Software version
CURRENT_VERSION = "Stretcher ver_2_1"

### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

    # receivedData = pyqtSignal()
    

#####################################################################
# DiagnosticsDialog Class - Secondary window for diagnostics checks #
#####################################################################
class DiagDialog(QDialog):
    def __init__(self, ser_instance):
        super(DiagDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_DiagnosticsDialog()
        self.ui.setupUi(self)

        self.ui.doneButton.clicked.connect(self.accept)

        self.ser = ser_instance

        #activo el timer de 2 segundos, la primera vez, luego se autollama
        if self.ser.port_open == False:
            self.ui.hardwareLabel.setText("No port  ")
            self.ui.firmwareLabel.setText("No port  ")
        else:
            self.ui.hardwareLabel.setText("Waiting...  ")
            self.ui.firmwareLabel.setText("Waiting...  ")
            self.ser.Write("voltage\n")
            # ser_instance.Write("get data\n")
            self.next_call = time()
            self.t3seg = Timer(self.next_call - time(), self.TimerThreeSec, [3]).start()

        #recupero informacion del sistema
        (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
        # print(f"distname: {distname} version: {version} id: {nid}")
        os_text = "--" + distname + version + "-- "
        self.ui.osLabel.setText(os_text)

        (system, node, release, version, machine, processor) = platform.uname()
        # print(f"system: {system}, node: {node}, release: {release}, version: {version}, machine: {machine}, processor: {processor}")
        self.ui.kernelLabel.setText(release)
        self.ui.softLabel.setText(CURRENT_VERSION)

    def TimerThreeSec (self, lapse):
        """ 
            aca tengo que resolver todo lo que se mueve 
            lo hago tipo por estados del programa con treatmet_state
        """
        self.next_call = self.next_call + lapse
        # #esto corre en otro thread entonces mando una senial para hacer update de la interface
        # self.one_second_signal.emit()        
        #antes de volver hago la proxima llamada
        self.t3seg = Timer(self.next_call - time(), self.TimerThreeSec, [3]).start()
        arrow = self.ser.Read()
        print(arrow)
        


    #     self.intfreq = 0

    #     # # # Connect up the buttons.
    #     self.ui.pushButton1.clicked.connect(self.UPFreq)
    #     self.ui.pushButton2.clicked.connect(self.DWNFreq)
    #     self.ui.endButton.clicked.connect(self.accept)


    # def UPFreq (self, event=None):
    #     if (self.intfreq < 10):
    #         self.intfreq += 1

    #     self.changeFreqLabel(self.intfreq)

    # def DWNFreq (self, event=None):
    #     if (self.intfreq > 1):
    #         self.intfreq -= 1

    #     self.changeFreqLabel(self.intfreq)

    # def changeFreqLabel(self, new_f):
    #     self.intfreq = new_f
    #     self.ui.whatfreqLabel.setText(str(self.intfreq))
    
        
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

        # # Make some local modifications.
        # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        self.ui.triangularButton.clicked.connect(self.SignalTriangular)
        self.ui.cuadradaButton.clicked.connect(self.SignalSquare)
        self.ui.senoidalButton.clicked.connect(self.SignalSinusoidal)
        
        self.ui.freq1Button.clicked.connect(self.SetNewFreq)
        self.ui.freq2Button.clicked.connect(self.SetNewFreq)
        self.ui.freq3Button.clicked.connect(self.SetNewFreq)
        self.ui.freq4Button.clicked.connect(self.SetNewFreq)
        self.ui.freq5Button.clicked.connect(self.SetNewFreq)
        self.ui.freq6Button.clicked.connect(self.SetNewFreq)
        
        self.ui.ch1Button.clicked.connect(self.Channel1Enable)
        self.ui.ch2Button.clicked.connect(self.Channel2Enable)
        self.ui.ch3Button.clicked.connect(self.Channel3Enable)

        self.ui.updownButton.clicked.connect(self.StretcherUpOrDown)

        # cambio estas seniales por pressed() released()
        # self.ui.powerUpButton.clicked.connect(self.UpPower)
        # self.ui.powerDwnButton.clicked.connect(self.DwnPower)
        self.ui.powerUpButton.pressed.connect(self.UpPowerPressed)
        self.ui.powerUpButton.released.connect(self.UpPowerReleased)
        self.ui.powerDwnButton.pressed.connect(self.DwnPowerPressed)
        self.ui.powerDwnButton.released.connect(self.DwnPowerReleased)
        self.ui.timeUpButton.pressed.connect(self.UpTimePressed)
        self.ui.timeUpButton.released.connect(self.UpTimeReleased)        
        self.ui.timeDwnButton.pressed.connect(self.DwnTimePressed)
        self.ui.timeDwnButton.released.connect(self.DwnTimeReleased)        

        
        
        self.ui.startButton.clicked.connect(self.Start_Treatment)
        self.ui.stopButton.clicked.connect(self.Stop_Treatment)
        self.ui.pauseButton.clicked.connect(self.Pause_Treatment)


        # Cambios para utilizar el programa con el Magneto
        if USE_FOR_MAGNETO:
            self.ui.ch1Button.setEnabled(False)
            self.ui.ch2Button.setEnabled(False)
            self.ui.ch3Button.setEnabled(False)
            self.ui.updownButton.setEnabled(False)            

        # Fin cambios programa Magneto
        
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

        #incializo el objeto de la sesion/tratamiento
        self.t = Treatment()

        #seteo valores por default
        self.ui.powerLabel.setText(str(self.t.GetPower()) + '%')
        self.ui.minutesLabel.setText(str(self.t.GetTreatmentTimer()))
        self.ui.date_timeLabel.setText("")

        #activo el timer de 1 segundo, la primera vez, luego se autollama
        self.next_call = time()
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()

        #SIGNALS
        # conecto seniales al los metodos
        self.one_second_signal.connect(self.UpdateOneSec)

        #para llevar adelante el date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        date_str = date_now.strftime("%d/%m/%Y - %H:%M")
        self.ui.date_timeLabel.setText(date_str)

        #uso del boton UP/DOWN
        if USE_STRETCHER_UPDOWN_BUTTON:
            self.ui.updownButton.setText("Up / Down")
        elif USE_STRETCHER_DIAG_BUTTON:
            self.ui.updownButton.setText("Diagnostics")
        
        

    # Metodos del modulo / dialogo
    def Channel1Enable (self):
        if (self.ui.ch1Button.isChecked() == True):
            self.t.EnableChannelsInTreatment('ch1')
        else:
            self.t.DisableChannelsInTreatment('ch1')

    def Channel2Enable (self):
        if (self.ui.ch2Button.isChecked() == True):
            self.t.EnableChannelsInTreatment('ch2')
        else:
            self.t.DisableChannelsInTreatment('ch2')

    def Channel3Enable (self):
        if (self.ui.ch3Button.isChecked() == True):
            self.t.EnableChannelsInTreatment('ch3')
        else:
            self.t.DisableChannelsInTreatment('ch3')
            
    def StretcherUpOrDown (self):
        if USE_STRETCHER_UPDOWN_BUTTON:
            self.ui.textEdit.append("Stretcher UP or DOWN")
            if (self.s.port_open):
                self.s.Write("stretcher up\r\n")
            else:
                self.ui.textEdit.append("Port not Open!!!")

        elif USE_STRETCHER_DIAG_BUTTON:
            a = DiagDialog(self.s)
            a.setModal(True)
            # a.changeChannelLabel(sender.text())
            # a.changeLaserLabel(self.t.GetLaserPower(sender.text()))
            # a.changeLEDLabel(self.t.GetLedPower(sender.text()))

            # a.setWindowTitle("Seteo de Potencias")
            a.exec_()

            # new_power = a.ui.whatplaserLabel.text()
            # # print ("canal: " + str(sender.text()) + " potencia: " + new_power)
            # new_power = new_power[:-1]
            # self.t.SetLaserPower(sender.text(), int(new_power))
            

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
        
    def SignalTriangular (self):
        if (self.ui.cuadradaButton.isChecked() == True):
            self.ui.cuadradaButton.toggle()

        if (self.ui.senoidalButton.isChecked() == True):
            self.ui.senoidalButton.toggle()

        if (self.ui.triangularButton.isChecked() != True):
            self.ui.triangularButton.toggle()
            
        self.t.SetSignal('triangular')

    def SignalSquare (self):
        if (self.ui.triangularButton.isChecked() == True):
            self.ui.triangularButton.toggle()

        if (self.ui.senoidalButton.isChecked() == True):
            self.ui.senoidalButton.toggle()

        if (self.ui.cuadradaButton.isChecked() != True):
            self.ui.cuadradaButton.toggle()
            
        self.t.SetSignal('square')

    def SignalSinusoidal (self):
        if (self.ui.triangularButton.isChecked() == True):
            self.ui.triangularButton.toggle()

        if (self.ui.cuadradaButton.isChecked() == True):
            self.ui.cuadradaButton.toggle()
            
        if (self.ui.senoidalButton.isChecked() != True):
            self.ui.senoidalButton.toggle()

        self.t.SetSignal('sinusoidal')

    """
    chequea el boton de frecuencia y guarda el texto del mismo en el objeto treatment
    normalmente 7.83Hz
    """
    def SetNewFreq (self):
        sender = self.sender()
        if (sender.isChecked() != True):
            sender.toggle()

        self.ui.textEdit.append(sender.text() + " selected")
        self.t.SetFrequency(sender.text())

    def Start_Treatment (self):
        if (self.s.port_open):
            if (self.t.treatment_state == 'STOP'):

                #seteo el timer elegido
                # new_t = self.ui.minutesLabel.text()
                # self.t.SetTreatmentTimer(int(new_t))

                #arreglo para cuando seleccionan 1 minuto
                if self.t.GetTreatmentTimer() == 1:
                    self.ui.minutesLabel.setText("59")
                    self.ui.timeStringLabel.setText("seconds")
                    self.t.remaining_seconds = 59
                    self.t.remaining_minutes = 0
                else:
                    self.t.remaining_minutes = self.t.GetTreatmentTimer()
                    self.t.remaining_seconds = 0

                #envio variable dummy para limpiar puerto despues de algun error
                self.s.Write("voltage\r\n")
                sleep(0.1)

                if USE_FOR_STRETCHER:
                    new_signal = self.t.GetSignal()
                    to_send = "signal " + new_signal
                    self.ui.textEdit.append(to_send)
                    self.s.Write(to_send + "\r\n")

                    new_freq = self.t.GetFrequency()
                    new_freq = new_freq.split('Hz')
                    new_freq = new_freq[0]
                    new_freq_f = float(new_freq)
                    if new_freq_f <= 5:
                        to_send = "frequency " + "6.00Hz"
                    elif new_freq_f >= 70:
                        to_send = "frequency " + "65.00Hz"
                    else:
                        to_send = "frequency {:.02f}Hz".format(new_freq_f)

                    
                    self.ui.textEdit.append(to_send)
                    self.s.Write(to_send + "\r\n")

                    new_power = self.t.GetPower()
                    if USE_POWER_LIMIT:
                        if new_signal == 'triangular' or new_signal == 'sinusoidal':
                            new_power = int(new_power * 70 / 100)
                        else:
                            new_power = int(new_power * 50 / 100)

                    to_send = 'power {:03d}'.format(new_power)
                    self.ui.textEdit.append(to_send)
                    self.s.Write(to_send + "\r\n")

                    if (self.t.GetChannelInTreatment('ch1') == True):
                        to_send = "enable channel 1"
                        self.ui.textEdit.append(to_send)
                        self.s.Write(to_send + "\r\n")
                    else:
                        to_send = "disable channel 1"
                        self.ui.textEdit.append(to_send)
                        self.s.Write(to_send + "\r\n")
                    

                    if (self.t.GetChannelInTreatment('ch2') == True):
                        to_send = "enable channel 2"
                        self.ui.textEdit.append(to_send)
                        self.s.Write(to_send + "\r\n")
                    else:
                        to_send = "disable channel 2"
                        self.ui.textEdit.append(to_send)
                        self.s.Write(to_send + "\r\n")
                    

                    if (self.t.GetChannelInTreatment('ch3') == True):
                        to_send = "enable channel 3"
                        self.ui.textEdit.append(to_send)
                        self.s.Write(to_send + "\r\n")
                    else:
                        to_send = "disable channel 3"
                        self.ui.textEdit.append(to_send)
                        self.s.Write(to_send + "\r\n")

                    new_timer = self.t.GetTreatmentTimer()
                    to_send = 'duration,00,{:02d},00,1'.format(new_timer)
                    self.ui.textEdit.append(to_send)
                    self.s.Write(to_send + "\r\n")

                # El magneto combina toda esta info en un solo string
                # magnet_proj.org
                if USE_FOR_MAGNETO:
                    to_send = self.t.GetMagnetoDurationString()
                    self.ui.textEdit.append(to_send)                
                    self.s.Write(to_send + "\r\n")
                    sleep(0.1)
                
                    to_send = self.t.GetMagnetoFreqSignalPowerString()
                    self.ui.textEdit.append(to_send)                
                    self.s.Write(to_send + "\r\n")
                    sleep(0.1)

                    to_send = 'state_of_stage,1,1'
                    self.ui.textEdit.append(to_send)                
                    self.s.Write(to_send + "\r\n")
                    sleep(0.1)                
                # Fin modificacion Magneto
                
                self.ui.textEdit.append("Starting Treatment...")            
                self.s.Write("start,\r\n")
                self.t.treatment_state = 'START'
                self.DisableForTreatment()

        else:
            self.ui.textEdit.append("Port not Open!!!")


    def Stop_Treatment (self):
        if (self.s.port_open):
            if (self.t.treatment_state == 'START'):
                self.t.treatment_state = 'STOP'
                self.EnableForTreatment()
                self.ui.textEdit.append("STOP Treatment")
                self.s.Write("stop,\r\n")
                sleep(1)
        else:
            self.ui.textEdit.append("Port not Open!!!")
            

    def Pause_Treatment (self):
        if (self.s.port_open):
            if (self.t.treatment_state == 'START'):
                self.t.treatment_state = 'PAUSE'
                self.ui.stopButton.setEnabled(False)
                self.ui.pauseButton.setText("RESUME")                
                self.ui.textEdit.append("Pausing Treatment...")
                # self.s.Write("pause,\r\n")
                self.s.Write("pause,1\r\n")                
                sleep(0.1)
            elif (self.t.treatment_state == 'PAUSE'):
                self.t.treatment_state = 'START'
                self.ui.stopButton.setEnabled(True)
                self.ui.pauseButton.setText("PAUSE")
                self.ui.textEdit.append("Resuming Treatment...")
                # self.s.Write("pause,\r\n")
                self.s.Write("pause,0\r\n")                
                sleep(0.1)                
        else:
            self.ui.textEdit.append("Port not Open!!!")            


    def DisableForTreatment (self):
        # deshabilito botones que no se pueden tocar en tratamiento
        self.ui.startButton.setEnabled(False)
        
        self.ui.triangularButton.setEnabled(False)
        self.ui.cuadradaButton.setEnabled(False)
        self.ui.senoidalButton.setEnabled(False)
        
        self.ui.freq1Button.setEnabled(False)
        self.ui.freq2Button.setEnabled(False)
        self.ui.freq3Button.setEnabled(False)
        self.ui.freq4Button.setEnabled(False)
        self.ui.freq5Button.setEnabled(False)
        self.ui.freq6Button.setEnabled(False)

        self.ui.ch1Button.setEnabled(False)
        self.ui.ch2Button.setEnabled(False)
        self.ui.ch3Button.setEnabled(False)

        self.ui.powerUpButton.setEnabled(False)
        self.ui.powerDwnButton.setEnabled(False)
        self.ui.timeUpButton.setEnabled(False)
        self.ui.timeDwnButton.setEnabled(False)

    def EnableForTreatment (self):
        # habilito botones que permiten elegir cosas fuera del tratamiento
        self.ui.startButton.setEnabled(True)
        
        self.ui.triangularButton.setEnabled(True)
        self.ui.cuadradaButton.setEnabled(True)
        self.ui.senoidalButton.setEnabled(True)
        
        self.ui.freq1Button.setEnabled(True)
        self.ui.freq2Button.setEnabled(True)
        self.ui.freq3Button.setEnabled(True)
        self.ui.freq4Button.setEnabled(True)
        self.ui.freq5Button.setEnabled(True)
        self.ui.freq6Button.setEnabled(True)

        # Cambios para utilizar el programa con el Magneto
        if USE_FOR_MAGNETO:
            # self.ui.ch1Button.setEnabled(True)
            # self.ui.ch2Button.setEnabled(True)
            # self.ui.ch3Button.setEnabled(True)
            self.tempCnt = 0
        # Fin cambios para utilizar el programa con el Magneto
        
        if USE_FOR_STRETCHER:
            self.ui.ch1Button.setEnabled(True)
            self.ui.ch2Button.setEnabled(True)
            self.ui.ch3Button.setEnabled(True)


        self.ui.powerUpButton.setEnabled(True)
        self.ui.powerDwnButton.setEnabled(True)
        self.ui.timeUpButton.setEnabled(True)
        self.ui.timeDwnButton.setEnabled(True)
        self.ui.minutesLabel.setText(str(self.t.GetTreatmentTimer()))
        self.ui.timeStringLabel.setText("minutes")


    def UpdateOneSec (self):
        """ paso un segundo, reviso que tengo que hacer """
        #si el tratamiento corre hago update del label
        if self.t.treatment_state == 'START':
            self.UpdateTimerLabel()
        
        # reviso si algun boton sigue presionado

        # botones de potencia
        if self.powerUpButtonCnt > 3:
            self.PwrUp(10)
        elif self.powerUpButtonCnt > 1:
            self.PwrUp(5)

        if self.powerUpButtonCnt >= 1:
            self.powerUpButtonCnt += 1

        if self.powerDwnButtonCnt > 3:
            self.PwrDwn(10)
        elif self.powerDwnButtonCnt > 1:
            self.PwrDwn(5)

        if self.powerDwnButtonCnt >= 1:
            self.powerDwnButtonCnt += 1

        # botones de minutos            
        if self.timeUpButtonCnt > 3:
            self.TimeUp(10)
        elif self.timeUpButtonCnt > 1:
            self.TimeUp(5)

        if self.timeUpButtonCnt >= 1:
            self.timeUpButtonCnt += 1

        if self.timeDwnButtonCnt > 3:
            self.TimeDwn(10)
        elif self.timeDwnButtonCnt > 1:
            self.TimeDwn(5)

        if self.timeDwnButtonCnt >= 1:
            self.timeDwnButtonCnt += 1

        date_now = datetime.today()

        if date_now.minute != self.minutes_last:
            # print(date_now)
            self.minutes_last = date_now.minute
            date_str = date_now.strftime("%d/%m/%Y - %H:%M")
            self.ui.date_timeLabel.setText(date_str)
            

            
            
    def UpdateTimerLabel (self):
        if self.t.remaining_minutes > 0:
            #si quedan minutos todavia
            if self.t.remaining_seconds > 0:
                self.t.remaining_seconds -= 1
            else:
                self.t.remaining_minutes -= 1
                self.t.remaining_seconds = 59

            #todos los segundos actualizo ui
            if self.t.remaining_minutes == 0:
                self.ui.minutesLabel.setText("59")
                self.ui.timeStringLabel.setText("seconds")
            else:
                self.ui.minutesLabel.setText(str('{}:{:02d}'.format(self.t.remaining_minutes, self.t.remaining_seconds)))

        else:
            #estoy en el ultimo minuto ya uso el contador remaining_seconds
            if self.t.remaining_seconds > 0:
                self.t.remaining_seconds -= 1
                self.ui.minutesLabel.setText(str(self.t.remaining_seconds))                
            else:
                # termino el tratamiento, hago algo parecido al boton stop
                self.t.treatment_state = 'STOP'
                self.EnableForTreatment()
                self.ui.textEdit.append("STOP Treatment")
                # self.s.Write("stop,\r\n")
                self.s.Write("finish_ok,\r\n")
                sleep(1)
                
    def PwrUp (self, new_pwr):
        last_pwr = self.t.GetPower()
        if ((last_pwr + new_pwr) < 100):
            last_pwr += new_pwr
        else:
            last_pwr = 100
            
        self.ui.powerLabel.setText(str(last_pwr) + '%')
        self.t.SetPower(last_pwr)

    def PwrDwn (self, new_pwr):
        last_pwr = self.t.GetPower()
        if ((last_pwr - new_pwr) > 10):
            last_pwr -= new_pwr
        else:
            last_pwr = 10
            
        self.ui.powerLabel.setText(str(last_pwr) + '%')
        self.t.SetPower(last_pwr)

    def TimeUp (self, new_time):
        last_time = self.t.GetTreatmentTimer()
        if ((last_time + new_time) < 45):
            last_time += new_time
        else:
            last_time = 45
        self.ui.minutesLabel.setText(str(last_time))
        self.t.SetTreatmentTimer(last_time)

    def TimeDwn (self, new_time):
        last_time = self.t.GetTreatmentTimer()
        if ((last_time - new_time) > 1):
            last_time -= new_time
        else:
            last_time = 1
        self.ui.minutesLabel.setText(str(last_time))
        self.t.SetTreatmentTimer(last_time)

        
    def TimerOneSec(self, lapse):
        """ 
            aca tengo que resolver todo lo que se mueve 
            lo hago tipo por estados del programa con treatmet_state
        """
        self.next_call = self.next_call + 1
        #esto corre en otro thread entonces mando una senial para hacer update de la interface
        self.one_second_signal.emit()        
        #antes de volver hago la proxima llamada
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
