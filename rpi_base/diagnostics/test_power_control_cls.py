import sys
from PyQt5.QtWidgets import QApplication


"""
        Test for PowerControlDialog

"""

#Here import the UIs or classes that got the UIs
from power_control_cls import PowerControlDialog

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

        
    def ReadConfigFile (self):
        print ('asked to read config.txt')


    def SaveConfigFile (self):
        print ('asked to write config.txt')
        

        
####################
# Function Screens #
####################
def TestScreen ():
    treat = TreatmentMock()
    a = PowerControlDialog(treat)
    
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
