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
    mem_dict = {
        "mema" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "memb" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "memc" : ["Arm and Leg Inflammatory", "", "", ""],
        "memd" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem5" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem6" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem7" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem8" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem9" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem10" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem11" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem12" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem13" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem14" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem15" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem16" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem17" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem18" : ["Arm and Leg Inflammatory", "25 24 23 22", "", ""],
        "mem19" : ["Arm and Leg Inflammatory", "", "", ""],
        "mem20" : ["Arm and Leg Inflammatory", "", "", ""]
        }

    mem_bkp = mem_dict.copy()
    a = MemManagerDialog(mem_dict)
    
    a.setModal(True)
    a.exec_()

    if a.action == 'accept':
        print('Accept new config')
        print('Config List')        
    else:
        print('Last config')

    print('original mema:')
    print(mem_bkp['mema'])
    print('returned mema:')
    print(mem_dict['mema'])
              
    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
