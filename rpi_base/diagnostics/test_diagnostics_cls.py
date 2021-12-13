import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, QObject


"""
        Test for DiagnosticsDialog

"""

#Here import the UIs or classes that got the UIs
from diagnostics_cls import DiagnosticsDialog

class SerialMock ():
    def __init__(self, cb, port):
        self.cb = cb
        print ('port on: ' + port)
        self.port_open = True

    def Write (self, to_send):
        print ('serial tx -> ' + to_send)
        if 'keepalive' in to_send:
            self.Read('OK')

        if 'serial num' in to_send:
            self.Read('Device Id: 0xffffffff')

        if 'voltage' in to_send:
            self.Read('High Supply: 211.11V')
            self.Read('Low Supply: 45.22V')

        if 'hard_soft' in to_send:
            self.Read('Hardware Version: 2.1\r\n')
            self.Read('Software Version: 1.4\r\n')
            
    def Read (self, to_read):
        print('serial rx <- ' + to_read)
        self.cb(to_read)        


class TestingClass (QObject):
    rcv_signal = pyqtSignal(str)
    
    def __init__(self):
        super(QObject, self).__init__()        

    def MyObjCallback (self, readed):
        print (readed)
        self.rcv_signal.emit(readed)


class TreatmentMock ():
    def __init__(self, localization='usa'):
        self.localization = localization
        self.triangular_power_limit = 100
        self.square_power_limit = 50
        self.sinusoidal_power_limit = 60       
        
        self.peak_current = 3.6
        self.resistance065 = 47
        self.resistance080 = 23.5
        self.tempcoef065 = 0.2627
        self.tempcoef080 = 0.2627
        self.tempamb = 25

        self.current_version = 'Stretcher_ver_3_2'

    def ReadConfigFile (self):
        print ('asked to read config.txt')

    def SaveConfigFile (self):
        print ('asked to write config.txt')

    def GetCurrentVersion (self):
        print ('asked for version: ' + self.current_version)
        return self.current_version

    def GetLocalization (self):
        print ('asked for localization: ' + self.localization)
        return self.localization
    
    def SetLocalization (self, locali):
        print ('set localization: ' + locali)
        self.localization = locali

        
####################
# Function Screens #
####################
def TestScreen ():
    localization = 'usa'
    # localization = 'arg'
    test = TestingClass()
    treat = TreatmentMock(localization)
    s = SerialMock(test.MyObjCallback, '/dev/ttyACM0')
    # a = DiagnosticsDialog(self.s, self.t, parent=self)
    a = DiagnosticsDialog (s, treat, test)
    # print('testing callback')
    # s.Read('cb test')
    
    a.setModal(True)
    a.exec_()
    print('new localization is: ' + a.localization + ' saved localization: ' + treat.GetLocalization())

    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
