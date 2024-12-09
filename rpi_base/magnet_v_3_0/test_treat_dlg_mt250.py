import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from stylesheet_class import ButtonStyles
from antenna_class import AntennaInTreatment


"""
        Test for TreatmentDialog

"""

#Here import the UIs or classes that got the UIs
from dlg_treat_cls_mt250 import TreatmentDialog


# class to signal time of tests
# class Signaller(QObject):
#     signal = pyqtSignal(str)

#     def trigger(self, msg):
#         print("emitting: {}".format(msg))
#         self.signal.emit(msg)

# def receiver(msg):
#     print("received: {}".format(msg))

# signaller = Signaller()
# signaller.signal.connect(receiver)
# signaller.trigger('hello')
        # # tests progress timer
        # self.tests_progress_timer = QTimer()

        # # CONNECT SIGNALS
        # # connect the timer signal to the Update
        # self.test_timeout = 10    # timeout on 10 secs
        # self.one_second_signal.connect(self.UpdateOneSec)

        # ## start the timer
        # self.tests_progress_timer.timeout.connect(self.TimerOneSec)
        # self.tests_progress_timer.start(1000)

    # """ Emit a signal to not delay the timer response """
    # def TimerOneSec(self):        
    #     self.one_second_signal.emit()

    # def UpdateOneSec (self):
    #     if self.test_timeout > 0:
    #         self.test_timeout -= 1
    #     else:


class TreatmentMock ():
        
    def __init__(self, s_port, localization='usa'):
        
        self.s = s_port
        self.localization = localization
        # self.triangular_power_limit = 100
        self.triangular_power_limit = 50      
        self.square_power_limit = 100
        self.sinusoidal_power_limit = 100
        # self.square_power_limit = 50
        # self.sinusoidal_power_limit = 60
        
        self.peak_current = 3.6
        self.resistance065 = 47
        self.resistance080 = 23.5
        self.tempcoef065 = 0.2627
        self.tempcoef080 = 0.2627
        self.tempamb = 25

        self.treatment_timer = 0
        self.power = 100
        self.signal = 'triangular'
        self.frequency = '7.83Hz'
        # self.frequency = '11.79Hz'
        # self.frequency = '16.67Hz'
        # self.frequency = '23.58Hz'
        # self.frequency = '30.80Hz'
        # self.frequency = '62.64Hz'
        
        self.current_version = 'Magnet MT250 ver 3.1'
        self.treatment_state = 'STOP'
        self.timeout_screensaver = 10    # ten seconds for tests

        # tests progress timer
        self.tests_progress_timer = QTimer()
        self.tests_progress_timer.singleShot(10000, self.Test_Error)


    def GetTreatmentTimer (self):
        my_time = 10
        print ('asked for treatment timer, always return ' + str(my_time))
        return my_time

    def GetSignal (self):
        return self.signal

    def GetFrequency(self):
        return self.frequency

    def GetPower(self):
        return self.power
    
    def GetPowerLimit (self, signal):
        if signal == 'triangular':
            return self.triangular_power_limit
        elif signal == 'square':
            return self.square_power_limit
        else:
            return self.sinusoidal_power_limit

    def GetMagnetoFreqSignalPowerString (self):
        """ 
            Devuelve un string con toda la info combinada para el Magneto viejo 
            "signal,%03d,%03d,0%x%x%d,%04d,%04d,%04d,%04d,%04d,%04d,1\r\n"
            example. signal,100,100,0000,0003,0003,0003,0006,0000,0000,1
        """
        treat = "signal,"

        if self.signal == 'triangular':
            new_power = int(self.triangular_power_limit * self.power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0061,0001,0001,0064,0000,0000,1'
            if self.frequency == '11.79Hz':
                treat += '0040,0001,0001,0043,0000,0000,1'
            if self.frequency == '16.67Hz':
                treat += '0028,0001,0001,0030,0000,0000,1'
            if self.frequency == '23.58Hz':
                treat += '0019,0001,0001,0021,0000,0000,1'
            if self.frequency == '30.80Hz':
                treat += '0014,0001,0001,0016,0000,0000,1'
            if self.frequency == '62.64Hz':
                treat += '0006,0001,0001,0008,0000,0000,1'

        if self.signal == 'sinusoidal':
            new_power = int(self.sinusoidal_power_limit * self.power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0021,0021,0021,0064,0000,0000,1'
            if self.frequency == '11.79Hz':
                treat += '0014,0014,0014,0043,0000,0000,1'
            if self.frequency == '16.67Hz':
                treat += '0010,0010,0010,0030,0000,0000,1'
            if self.frequency == '23.58Hz':
                treat += '0007,0007,0007,0021,0000,0000,1'
            if self.frequency == '30.80Hz':
                treat += '0005,0006,0005,0016,0000,0000,1'
            if self.frequency == '62.64Hz':
                treat += '0003,0002,0003,0008,0000,0000,1'

        if self.signal == 'square':
            new_power = int(self.square_power_limit * self.power / 100)
            if new_power < 10:
                new_power = 10
                
            treat += "{:03d},{:03d},0000,".format(new_power, new_power)

            # rising edge, maintenance, falling edge, stop time 
            if self.frequency == '7.83Hz':
                treat += '0001,0061,0001,0064,0000,0000,1'
            if self.frequency == '11.79Hz':
                treat += '0001,0040,0001,0043,0000,0000,1'
            if self.frequency == '16.67Hz':
                treat += '0001,0028,0001,0030,0000,0000,1'
            if self.frequency == '23.58Hz':
                treat += '0001,0019,0001,0021,0000,0000,1'
            if self.frequency == '30.80Hz':
                treat += '0001,0014,0001,0016,0000,0000,1'
            if self.frequency == '62.64Hz':
                treat += '0001,0006,0001,0008,0000,0000,1'        

        return treat

    def GetMagnetoDurationString (self):
        treat_time = 'duration,00,{:02d},00,1'.format(self.treatment_timer)
        return treat_time
    
    
    # def ReadConfigFile (self):
    #     print ('asked to read config.txt')

    # def SaveConfigFile (self):
    #     print ('asked to write config.txt')

    # def GetCurrentVersion (self):
    #     print ('asked for version: ' + self.current_version)
    #     return self.current_version

    def GetLocalization (self):
        print ('asked for localization: ' + self.localization)
        return self.localization
    
    def SetLocalization (self, locali):
        print ('set localization: ' + locali)
        self.localization = locali

    def Test_Error (self):
        self.s.Read('ERROR(0x021)')
        self.s.Read('STOP')
        self.s.Read('Flushing errors')


class SerialMock ():
    def __init__(self, cb, port):
        self.cb = cb
        print ('port on: ' + port)
        self.port_open = True

    def Write (self, to_send):
        print ('serial tx -> ' + to_send)
        if 'keepalive' in to_send:
            self.Read('OK')
            
        # if 'serial num' in to_send:
        #     self.Read('Device Id: 0xffffffff')

        # if 'voltage' in to_send:
        #     self.Read('High Supply: 211.11V')
        #     self.Read('Low Supply: 45.22V')

        # if 'hard_soft' in to_send:
        #     self.Read('Hardware Version: 2.1\r\n')
        #     self.Read('Software Version: 1.4\r\n')
            
    def Read (self, to_read):
        print('serial rx <- ' + to_read)
        self.cb(to_read)        

    #
    # errores que envia la placa
    #
    # Error_SetString(buff_err, (ERROR_ANTENNA_LOST << 4) | (loop_ch + 1));
    # RPI_Send(buff_err);
    # "ERROR(0x%03X)\r\n"
    # ERROR(0x021)\r\n
    # RPI_Send("STOP\r\n");
    # Wait_ms(1000);
    # RPI_Send("Flushing errors\r\n");

class SignalsCb (QObject):
    rcv_signal = pyqtSignal(str)    

    def __init__(self):
        super(QObject, self).__init__()

    def MyObjCallback (self, readed):
        print ('cb obj called: ' + readed)
        self.rcv_signal.emit(readed)

        
# def MyFuncCallback (readed):
#     print ('cb called: ' + readed)


    
####################
# Function Screens #
####################
def TestScreen ():

    # ## set mocked stages info
    # stage1 = Stages()
    # stage2 = Stages()
    # stage3 = Stages()

    # stage1.SetStageTimer(1)
    # stage1.SetStagePower(85)
    # stage1.SetStageSignal('triangular')
    # stage1.SetStageFrequency('freq1')
    # stage1.SetStageStatus('enable')

    # stage2.SetStageTimer(1)
    # stage2.SetStagePower(100)
    # stage2.SetStageSignal('square')
    # stage2.SetStageFrequency('freq9')
    # stage2.SetStageStatus('enable')

    # stage3.SetStageTimer(1)
    # stage3.SetStagePower(10)
    # stage3.SetStageSignal('sinusoidal')
    # stage3.SetStageFrequency('freq10')
    # stage3.SetStageStatus('enable')
    
    # stages_list = [stage1, stage2, stage3]
    
    ## set mocked antennas
    antennas = AntennaInTreatment()
    #Tunnel 10 inches,020.00,020.00,004.04,065.00,4
    rcv = 'Tunnel 10 inches,020.00,020.00,004.04,065.00,4'
    rcv_list = rcv.split(',')
    antennas.ProcessStringList(rcv_list)

    antennas.setActive('ch1')

    
    scb = SignalsCb()
    serial_obj = SerialMock(scb.MyObjCallback, '/dev/ttyUSB0')
    style_obj = ButtonStyles()
    treat_obj = TreatmentMock(serial_obj, 'usa')
    a = TreatmentDialog(treat_obj, style_obj, antennas, serial_obj, parent=scb)
    a.setModal(True)
    a.exec_()

    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
