import sys
from PyQt5.QtWidgets import QApplication

"""
        Test for MemManagerDialog

"""

#Here import the UIs or classes that got the UIs
from dlg_mems_cls import MemoryDialog


####################
# Function Screens #
####################
def TestScreen ():

    str_lst = ["Arm and Leg Inflammatory", "", "", ""]
    memory = 'mema'
    a = MemoryDialog(memory, str_lst)
    
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
