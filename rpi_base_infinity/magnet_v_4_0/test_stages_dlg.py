import sys
from PyQt5.QtWidgets import QApplication
from stages_class import Stages
from stylesheet_class import ButtonStyles

"""
        Test for StagesDialog

"""

#Here import the UIs or classes that got the UIs
from dlg_stages_cls import StagesDialog


####################
# Function Screens #
####################
def TestScreen ():
    stage1 = Stages()
    stage2 = Stages()
    stage3 = Stages()

    stage1.SetStageTimer(45)
    stage1.SetStagePower(85)
    stage1.SetStageSignal('triangular')
    stage1.SetStageFrequency('freq1')
    stage1.SetStageStatus('enable')

    stage2.SetStageTimer(60)
    stage2.SetStagePower(100)
    stage2.SetStageSignal('square')
    stage2.SetStageFrequency('freq9')
    stage2.SetStageStatus('enable')

    stage3.SetStageTimer(0)
    stage3.SetStagePower(0)
    stage3.SetStageSignal('none')
    stage3.SetStageFrequency('none')
    stage3.SetStageStatus('disable')
    
    stages_list = [stage1, stage2, stage3]
    style_obj = ButtonStyles()
    a = StagesDialog(stages_list, style_obj)
    
    a.setModal(True)
    a.exec_()

    if a.action == 'accept':
        print('Accept new config')
        print('Config List')        
        print(a.st_lst)
    else:
        print('Last config')
        print(stages_list)
              
    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
