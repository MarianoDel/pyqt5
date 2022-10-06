import sys
from PyQt5.QtWidgets import QApplication


"""
        Test for DisplayModeDialog

"""

#Here import the UIs or classes that got the UIs
from display_mode_cls import DisplayModeDialog


class TreatmentMock ():
    def __init__(self, localization='usa'):
        self.localization = localization
        self.version = ''

    def SetCurrentVersion (self, version):
        self.current_version = version
        
    def GetCurrentVersion (self):
        return self.current_version

        
####################
# Function Screens #
####################
def TestScreen ():
    treat = TreatmentMock()
    a = DisplayModeDialog(treat)
    
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
