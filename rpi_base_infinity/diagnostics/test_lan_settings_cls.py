import sys
from PyQt5.QtWidgets import QApplication


"""
        Test for LanDialog

"""

#Here import the UIs or classes that got the UIs
from lan_settings_cls import LanDialog

        
####################
# Function Screens #
####################
def TestScreen ():
    a = LanDialog()
    
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
