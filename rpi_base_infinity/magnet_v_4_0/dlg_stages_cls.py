from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt


#get the UI from here
from ui_stages_dlg import Ui_StagesDialog


##################################################
# StagesDialog Class - to save or empty memories #
##################################################
class StagesDialog (QDialog):


    def __init__(self, st_lst, style_obj):
        super(StagesDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_StagesDialog()
        self.ui.setupUi(self)

        # backup received info
        self.st_lst = st_lst
        self.style = style_obj
        
        self.stage1_info = st_lst[0]
        self.stage2_info = st_lst[1]
        self.stage3_info = st_lst[2]

        self.action = 'accept'
        
        # get the close event and connect the buttons        
        self.ui.clearButton.clicked.connect(self.ClearStage)
        self.ui.backButton.clicked.connect(self.BackStage)
        self.ui.acceptButton.clicked.connect(self.accept)

        self.ui.stage1Button.clicked.connect(self.SelectStageButton1)
        self.ui.stage2Button.clicked.connect(self.SelectStageButton2)
        self.ui.stage3Button.clicked.connect(self.SelectStageButton3)

        # check which was selected, or select the first one
        self.Stage1GroupChange('enable')
        self.Stage2GroupChange('enable')
        self.Stage3GroupChange('select')

        self.ui.stage1SignalButton.raise_()
        self.ui.stage1FreqButton.raise_()
        

        

    def SelectStageButton1 (self):
        self.Stage1GroupChange('select')

        if self.stage2_info.status == 'enable':
            self.Stage2GroupChange('enable')

        if self.stage3_info.status == 'enable':
            self.Stage3GroupChange('enable')

        print('stage1 button!')

    def SelectStageButton2 (self):
        self.Stage2GroupChange('select')

        if self.stage1_info.status == 'enable':
            self.Stage1GroupChange('enable')

        if self.stage3_info.status == 'enable':
            self.Stage3GroupChange('enable')

        print('stage2 button!')

    def SelectStageButton3 (self):
        self.Stage3GroupChange('select')

        if self.stage1_info.status == 'enable':
            self.Stage1GroupChange('enable')

        if self.stage2_info.status == 'enable':
            self.Stage2GroupChange('enable')

        print('stage3 button!')

            
    def Stage1GroupChange (self, change_to):
        raise_inners = False
        
        if change_to == 'enable':
            self.ui.stage1Label.setStyleSheet(self.style.stage1_button_enable)
            raise_inners = True

        if change_to == 'select':
            self.ui.stage1Label.setStyleSheet(self.style.stage1_button_select)
            raise_inners = True            

        if change_to == 'disable':
            self.ui.stage1Label.setStyleSheet(self.style.stage1_button_disable)
            
        if raise_inners:
            # fix all picture, raise all small pics over background label,
            self.ui.stage1MinutesLabel.raise_()
            self.ui.stage1PowerLabel.raise_()
            self.ui.stage1SignalButton.raise_()
            self.ui.stage1FreqButton.raise_()

        # then raise transparent button
        self.ui.stage1Button.raise_()

        
    def Stage2GroupChange (self, change_to):
        raise_inners = False
        
        if change_to == 'enable':
            self.ui.stage2Label.setStyleSheet(self.style.stage2_button_enable)
            raise_inners = True

        if change_to == 'select':
            self.ui.stage2Label.setStyleSheet(self.style.stage2_button_select)
            raise_inners = True            

        if change_to == 'disable':
            self.ui.stage2Label.setStyleSheet(self.style.stage2_button_disable)
            
        if raise_inners:
            # fix all picture, raise all small pics over background label,
            self.ui.stage2MinutesLabel.raise_()
            self.ui.stage2PowerLabel.raise_()
            self.ui.stage2SignalButton.raise_()
            self.ui.stage2FreqButton.raise_()

        # then raise transparent button
        self.ui.stage2Button.raise_()


    def Stage3GroupChange (self, change_to):
        raise_inners = False
        
        if change_to == 'enable':
            self.ui.stage3Label.setStyleSheet(self.style.stage3_button_enable)
            raise_inners = True

        if change_to == 'select':
            self.ui.stage3Label.setStyleSheet(self.style.stage3_button_select)
            raise_inners = True            

        if change_to == 'disable':
            self.ui.stage3Label.setStyleSheet(self.style.stage3_button_disable)
            
        if raise_inners:
            # fix all picture, raise all small pics over background label,
            self.ui.stage3MinutesLabel.raise_()
            self.ui.stage3PowerLabel.raise_()
            self.ui.stage3SignalButton.raise_()
            self.ui.stage3FreqButton.raise_()

        # then raise transparent button
        self.ui.stage3Button.raise_()
        
            
    def ClearStage (self):
        print('clearing selected stage')
        self.SelectStageButton2()


    def BackStage (self):
        self.action = 'none'
        self.accept()
    

        
        
### end of file ###

