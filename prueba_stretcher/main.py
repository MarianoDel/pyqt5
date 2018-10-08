import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from ui_stretcher import Ui_Dialog
from serialcomm import SerialComm
from treatment_class import Treatment
from time import sleep, time

#para el timer de 1 segundo
from threading import Timer


"""
    Pruebas con seniales y eventos custom
    http://zetcode.com/gui/pyqt5/eventssignals/
"""

### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

    # receivedData = pyqtSignal()
    

class Dialog(QDialog):

    rcv_signal = pyqtSignal(str)
    powerUpButtonCnt = 0
    powerDwnButtonCnt = 0
    timeUpButtonCnt = 0
    timeDwnButtonCnt = 0

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
        
        self.ui.freq10Button.clicked.connect(self.Freq_10)
        self.ui.freq30Button.clicked.connect(self.Freq_30)
        self.ui.freq60Button.clicked.connect(self.Freq_60)
        
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
        self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
        if self.s.port_open == False:
            self.ui.textEdit.append("Sin puerto serie!!!")
            # sys.exit(-1)
            #TODO: agregar un timer que vaya buscando el puerto!!!
        else:
            self.ui.textEdit.append("puerto serie abierto OK!")

        #incializo el objeto de la sesion/tratamiento
        self.t = Treatment()

        #seteo valores por default
        self.ui.powerLabel.setText(str(self.t.GetPower()) + '%')
        self.ui.minutesLabel.setText(str(self.t.GetTreatmentTimer()))        

        #activo el timer de 1 segundo, la primera vez, luego se autollama
        self.next_call = time()
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()

        #SIGNALS
        # conecto seniales al los metodos
        self.one_second_signal.connect(self.UpdateOneSec)

        
        

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
        self.ui.textEdit.append("Stretcher UP or DOWN")
        if (self.s.port_open):
            self.s.Write("stretcher up\r\n")
        else:
            self.ui.textEdit.append("Port not Open!!!")

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

    def Freq_10 (self):
        if (self.ui.freq30Button.isChecked() == True):
            self.ui.freq30Button.toggle()

        if (self.ui.freq60Button.isChecked() == True):
            self.ui.freq60Button.toggle()

        if (self.ui.freq10Button.isChecked() != True):
            self.ui.freq10Button.toggle()
            
        self.t.SetFrequency('10Hz')

    def Freq_30 (self):
        if (self.ui.freq10Button.isChecked() == True):
            self.ui.freq10Button.toggle()

        if (self.ui.freq60Button.isChecked() == True):
            self.ui.freq60Button.toggle()

        if (self.ui.freq30Button.isChecked() != True):
            self.ui.freq30Button.toggle()
            
        self.t.SetSignal('30Hz')

    def Freq_60 (self):
        if (self.ui.freq10Button.isChecked() == True):
            self.ui.freq10Button.toggle()

        if (self.ui.freq30Button.isChecked() == True):
            self.ui.freq30Button.toggle()
            
        if (self.ui.freq60Button.isChecked() != True):
            self.ui.freq60Button.toggle()

        self.t.SetSignal('60Hz')

    def Start_Treatment (self):
        if (self.s.port_open):
            if (self.t.treatment_state == 'STOP'):
                self.t.treatment_state = 'START'
                self.DisableForTreatment()

                new_signal = self.t.GetSignal()
                to_send = "signal " + new_signal
                self.ui.textEdit.append(to_send)
                self.s.Write(to_send + "\r\n")

                new_freq = self.t.GetFrequency()
                to_send = "frequency " + new_freq
                self.ui.textEdit.append(to_send)
                self.s.Write(to_send + "\r\n")

                new_power = self.t.GetPower()
                to_send = 'power {:03d}'.format(new_power)
                self.ui.textEdit.append(to_send)
                self.s.Write(to_send + "\r\n")

                if (self.t.GetChannelInTreatment('ch1') == True):
                    to_send = "enable channel 1"
                    self.ui.textEdit.append(to_send)
                    self.s.Write(to_send + "\r\n")

                if (self.t.GetChannelInTreatment('ch2') == True):
                    to_send = "enable channel 2"
                    self.ui.textEdit.append(to_send)
                    self.s.Write(to_send + "\r\n")

                if (self.t.GetChannelInTreatment('ch3') == True):
                    to_send = "enable channel 3"
                    self.ui.textEdit.append(to_send)
                    self.s.Write(to_send + "\r\n")

                new_timer = self.t.GetTreatmentTimer()
                to_send = "duration,00," + str(new_timer) + ",00,1"
                self.ui.textEdit.append(to_send)
                self.s.Write(to_send + "\r\n")
                
                self.ui.textEdit.append("Starting Treatment...")            
                self.s.Write("start,\r\n")

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
                self.ui.textEdit.append("Pausing Treatment...")
                self.s.Write("pause,\r\n")
                sleep(1)
            elif (self.t.treatmet_state == 'PAUSE'):
                self.t.treatmet_state = 'START'
                self.ui.textEdit.append("Resuming Treatment...")
                self.s.Write("pause,\r\n")
                sleep(1)                
        else:
            self.ui.textEdit.append("Port not Open!!!")            


    def DisableForTreatment (self):
        #deshabilito botones que no se pueden tocar en tratamiento
        self.ui.triangularButton.setEnabled(False)
        self.ui.cuadradaButton.setEnabled(False)
        self.ui.senoidalButton.setEnabled(False)
        
        self.ui.freq10Button.setEnabled(False)
        self.ui.freq30Button.setEnabled(False)
        self.ui.freq60Button.setEnabled(False)

        self.ui.ch1Button.setEnabled(False)
        self.ui.ch2Button.setEnabled(False)
        self.ui.ch3Button.setEnabled(False)

        self.ui.powerUpButton.setEnabled(False)
        self.ui.powerDwnButton.setEnabled(False)
        self.ui.timeUpButton.setEnabled(False)
        self.ui.timeDwnButton.setEnabled(False)

    def EnableForTreatment (self):
        #deshabilito botones que no se pueden tocar en tratamiento
        self.ui.triangularButton.setEnabled(True)
        self.ui.cuadradaButton.setEnabled(True)
        self.ui.senoidalButton.setEnabled(True)
        
        self.ui.freq10Button.setEnabled(True)
        self.ui.freq30Button.setEnabled(True)
        self.ui.freq60Button.setEnabled(True)

        self.ui.ch1Button.setEnabled(True)
        self.ui.ch2Button.setEnabled(True)
        self.ui.ch3Button.setEnabled(True)

        self.ui.powerUpButton.setEnabled(True)
        self.ui.powerDwnButton.setEnabled(True)
        self.ui.timeUpButton.setEnabled(True)
        self.ui.timeDwnButton.setEnabled(True)

    def UpdateOneSec (self):
        """ paso un segundo, reviso que tengo que hacer """
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
        if ((last_time - new_time) > 0):
            last_time -= new_time
        else:
            last_time = 0
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
        self.ui.textEdit.append(rcv)
        
    #capturo el cierre
    def closeEvent (self, event):
        self.ui.textEdit.append("Closing, Please Wait...")
        self.s.Close()
        sleep(2)
        event.accept()

    ###### FIN CLASS DIALOG


app = QApplication(sys.argv)
w = Dialog()
#http://doc.qt.io/qt-5/qt.html#WindowType-enum
w.setWindowFlags(Qt.CustomizeWindowHint)
# w.setWindowFlags(Qt.FramelessWindowHint)
w.show()
sys.exit(app.exec_())
