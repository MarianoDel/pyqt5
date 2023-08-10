import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, QObject

"""
        Test for Main Dialog

"""

#Here import the UIs or classes that got the UIs
from dlg_main_cls import Dialog


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

        
def MyFuncCallback (readed):
    print ('cb called: ' + readed)
    

class SignalsCb (QObject):
    rcv_signal = pyqtSignal(str)    

    def __init__(self):
        super(QObject, self).__init__()

    def MyObjCallback (self, readed):
        print ('cb obj called: ' + readed)
        self.rcv_signal.emit(readed)
        

class TreatmentMock ():

    def __init__(self):
        self.system = 'Slackware '
    
    def GetCurrentSystem(self):
        print('someone asked for system: ' + self.system)
        return self.system

    
####################
# Function Screens #
####################
def TestScreen ():

    scb = SignalsCb()

    # s = SerialMock(MyFuncCallback, '/dev/ttyACM0')
    s = SerialMock(scb.MyObjCallback, '/dev/ttyACM0')    
    
    debug = True
    treat = TreatmentMock()
    a = Dialog(debug, s, treat, parent=scb)
    a.setModal(True)
    a.exec_()
              
    sys.exit(0)


### End of Dialog ###
############
# Test App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
