import sys
from PyQt5.QtWidgets import QApplication


"""
        Test for SecurityDialog

"""

#Here import the UIs or classes that got the UIs
from security_code_cls import SecurityDialog


class SerialMock ():
    def __init__(self, port):
        print ('port on: ' + port)
        self.port_open = True

        
    def Write (self, to_send):
        print ('serial tx -> ' + to_send)

        
    def Read (self, to_read):
        print('serial rx <- ' + to_read)

        
####################
# Function Screens #
####################
def TestScreen ():
    s = SerialMock('serial0')

    a = SecurityDialog(s)

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
