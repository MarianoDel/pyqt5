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


    
####################
# Function Screens #
####################
def TestScreen ():
    localization = 'usa'
    # localization = 'arg'
    test = TestingClass()
    s = SerialMock(test.MyObjCallback, '/dev/ttyACM0')
    # a = DiagnosticsDialog(self.s, self.t, parent=self)
    a = DiagnosticsDialog ('Stretcher ver 3.1', localization, s, test)
    # print('testing callback')
    # s.Read('cb test')
    
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
