import sys
from PyQt5.QtWidgets import QApplication

"""
        Test for MemManagerDialog

"""

#Here import the UIs or classes that got the UIs
from dlg_mem_manager_cls import MemManagerDialog


####################
# Function Screens #
####################
def TestScreen ():
    
    a = MemManagerDialog()
    
    a.setModal(True)
    a.exec_()

    if a.action == 'accept':
        print('Accept new config')
        print('Config List')        
    else:
        print('Last config')
              
    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
