import sys
from PyQt5.QtWidgets import QApplication
from stages_class import Stages
from stylesheet_class import ButtonStyles

"""
        Test for StagesDialog

"""

#Here import the UIs or classes that got the UIs
from dlg_stages_cls import StagesDialog

# class TreatmentMock ():
#     def __init__(self, localization='usa'):
#         self.localization = localization
#         self.triangular_power_limit = 100
#         self.square_power_limit = 50
#         self.sinusoidal_power_limit = 60       
        
#         self.peak_current = 3.6
#         self.resistance065 = 47
#         self.resistance080 = 23.5
#         self.tempcoef065 = 0.2627
#         self.tempcoef080 = 0.2627
#         self.tempamb = 25

        
#     def ReadConfigFile (self):
#         print ('asked to read config.txt')


#     def SaveConfigFile (self):
#         print ('asked to write config.txt')
        

        
####################
# Function Screens #
####################
def TestScreen ():
    stage1 = Stages()
    stage2 = Stages()
    stage3 = Stages()

    stage1.SetStageStatus('enable')
    stage2.SetStageStatus('enable')
    stage3.SetStageStatus('enable')
    
    stages_list = [stage1, stage2, stage3]
    style_obj = ButtonStyles()
    # treat = TreatmentMock()
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
