import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, QObject
from stages_class import Stages
from stylesheet_class import ButtonStyles
from antenna_class import AntennaInTreatment


"""
        Test for TreatmentDialog

"""

#Here import the UIs or classes that got the UIs
from dlg_treat_cls import TreatmentDialog


class TreatmentMock ():
    def __init__(self, localization='usa'):
        self.localization = localization
        self.triangular_power_limit = 100
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

        self.current_version = 'Magnet_ver_4_0'

        self.stage_current_dict = {
            'stage1' : "15' S 35% 7.83Hz",
            'stage2' : "15' S 35% 7.83Hz",
            'stage3' : "15' S 35% 7.83Hz"
            }

        self.treatment_state = 'STOP'
        

    def GetTreatmentTimer (self):
        my_time = 10
        print ('asked for treatment timer, always return ' + str(my_time))
        return my_time

    
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


class SerialMock ():
    def __init__(self, cb, port):
        self.cb = cb
        print ('port on: ' + port)
        self.port_open = True

    def Write (self, to_send):
        print ('serial tx -> ' + to_send)
        if 'keepalive' in to_send:
            self.Read('OK')

        # if 'get_antenna,' in to_send:
        #     self.Read('')
            
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

    ## set mocked stages info
    stage1 = Stages()
    stage2 = Stages()
    stage3 = Stages()

    stage1.SetStageTimer(1)
    stage1.SetStagePower(85)
    stage1.SetStageSignal('triangular')
    stage1.SetStageFrequency('freq1')
    stage1.SetStageStatus('enable')

    stage2.SetStageTimer(1)
    stage2.SetStagePower(100)
    stage2.SetStageSignal('square')
    stage2.SetStageFrequency('freq9')
    stage2.SetStageStatus('enable')

    stage3.SetStageTimer(1)
    stage3.SetStagePower(10)
    stage3.SetStageSignal('sinusoidal')
    stage3.SetStageFrequency('freq10')
    stage3.SetStageStatus('enable')
    
    stages_list = [stage1, stage2, stage3]
    
    ## set mocked antennas
    antennas = AntennaInTreatment()
    #Tunnel 10 inches,020.00,020.00,004.04,065.00,4
    rcv = 'Tunnel 10 inches,020.00,020.00,004.04,065.00,4'
    rcv_list = rcv.split(',')
    antennas.ProcessStringList(rcv_list)

    
    style_obj = ButtonStyles()
    treat_obj = TreatmentMock()
    scb = SignalsCb()
    serial_obj = SerialMock(scb.MyObjCallback, '/dev/ttyUSB0')
    a = TreatmentDialog(stages_list, treat_obj, style_obj, antennas, serial_obj, parent=scb)
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
