from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QTimer


#get the UI from here
from ui_mem_manager_dlg import Ui_Dialog


##################################################
# MemManagerDialog Class - to save or empty memories #
##################################################
class MemManagerDialog (QDialog):

    #SIGNALS
    one_second_signal = pyqtSignal()

    # def __init__(self, st_lst, style_obj, caller_stage='stage1'):
    def __init__(self):        
        super(QDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.selected_blue = ''
        self.selected_cyan = ''

        self.label_blue = "color: rgb(55, 52, 53);\
                           background-color: rgb(32, 145, 235);"
        self.label_cyan = "color: rgb(55, 52, 53);\
                           background-color: rgb(178, 232, 247);"
        self.label_orig = "color: rgb(55, 52, 53);"
        
        # backup received info
    #     self.st_lst = st_lst
    #     self.style = style_obj

    
    #     self.stage1_info = st_lst[0]
    #     self.stage2_info = st_lst[1]
    #     self.stage3_info = st_lst[2]

    #     self.action = 'accept'
    #     self.stage_selected = caller_stage

    #     self.powerUpButtonCnt = 0
    #     self.powerDwnButtonCnt = 0
    #     self.timeUpButtonCnt = 0
    #     self.timeDwnButtonCnt = 0
        
        # get the close event and connect the buttons
    #     self.ui.clearButton.clicked.connect(self.ClearStage)
    #     self.ui.backButton.clicked.connect(self.BackStage)
    #     self.ui.acceptButton.clicked.connect(self.accept)

        self.ui.memaButton.clicked.connect(self.SelectButton_mema)
        self.ui.membButton.clicked.connect(self.SelectButton_memb)
        self.ui.memcButton.clicked.connect(self.SelectButton_memc)
        self.ui.memdButton.clicked.connect(self.SelectButton_memd)        
        self.ui.mem5Button.clicked.connect(self.SelectButton_mem5)
        self.ui.mem6Button.clicked.connect(self.SelectButton_mem6)
        self.ui.mem7Button.clicked.connect(self.SelectButton_mem7)
        self.ui.mem8Button.clicked.connect(self.SelectButton_mem8)        
        self.ui.mem9Button.clicked.connect(self.SelectButton_mem9)
        self.ui.mem10Button.clicked.connect(self.SelectButton_mem10)
        self.ui.mem11Button.clicked.connect(self.SelectButton_mem11)
        self.ui.mem12Button.clicked.connect(self.SelectButton_mem12)        
        self.ui.mem13Button.clicked.connect(self.SelectButton_mem13)
        self.ui.mem14Button.clicked.connect(self.SelectButton_mem14)
        self.ui.mem15Button.clicked.connect(self.SelectButton_mem15)
        self.ui.mem16Button.clicked.connect(self.SelectButton_mem16)        
        self.ui.mem17Button.clicked.connect(self.SelectButton_mem17)
        self.ui.mem18Button.clicked.connect(self.SelectButton_mem18)
        self.ui.mem19Button.clicked.connect(self.SelectButton_mem19)
        self.ui.mem20Button.clicked.connect(self.SelectButton_mem20)

        #     self.ui.stage2Button.clicked.connect(self.SelectStageButton2)
    #     self.ui.stage3Button.clicked.connect(self.SelectStageButton3)

    #     self.ui.freq1Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq2Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq3Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq4Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq5Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq6Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq7Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq8Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq9Button.clicked.connect(self.FrequencyChange)
    #     self.ui.freq10Button.clicked.connect(self.FrequencyChange)        

    #     self.ui.triangularButton.clicked.connect(self.SignalChange)
    #     self.ui.squareButton.clicked.connect(self.SignalChange)
    #     self.ui.sinusoidalButton.clicked.connect(self.SignalChange)

    #     self.ui.powerUpButton.pressed.connect(self.UpPowerPressed)
    #     self.ui.powerUpButton.released.connect(self.UpPowerReleased)
    #     self.ui.powerDwnButton.pressed.connect(self.DwnPowerPressed)
    #     self.ui.powerDwnButton.released.connect(self.DwnPowerReleased)
    #     self.ui.timeUpButton.pressed.connect(self.UpTimePressed)
    #     self.ui.timeUpButton.released.connect(self.UpTimeReleased)        
    #     self.ui.timeDwnButton.pressed.connect(self.DwnTimePressed)
    #     self.ui.timeDwnButton.released.connect(self.DwnTimeReleased)
        
    #     # check enables or disables
    #     if self.stage1_info.GetStageStatus() == 'enable':
    #         self.Stage1GroupChange('enable')
    #     else:
    #         self.Stage1GroupChange('disable')
            
    #     if self.stage2_info.GetStageStatus() == 'enable':
    #         self.Stage2GroupChange('enable')
    #     else:
    #         self.Stage2GroupChange('disable')
        
    #     if self.stage3_info.GetStageStatus() == 'enable':
    #         self.Stage3GroupChange('enable')
    #     else:
    #         self.Stage3GroupChange('disable')

        
    #     # check which was selected, or select the first one
    #     if self.stage_selected == 'stage1':
    #         self.Stage1GroupChange('select')
    #     elif self.stage_selected == 'stage2':
    #         self.Stage2GroupChange('select')
    #     else:
    #         self.Stage3GroupChange('select')


    #     ## activate the 1 second timer it is repetitive
    #     self.t1seg = QTimer()
    #     self.t1seg.timeout.connect(self.TimerOneSec)
    #     self.t1seg.start(1000)

    #     # screen saver timer activation
    #     # self.timer_screensaver = self.t.timeout_screensaver
    #     # self.screensaver_window = True
            
    #     #SIGNALS CONNECTION
    #     # connect through a signal the timer to the update event function
    #     self.one_second_signal.connect(self.UpdateOneSec)
            

    # # one second update signal
    # def TimerOneSec(self):
    #     self.one_second_signal.emit()
        

    # # one second update event function
    # def UpdateOneSec (self):
    #     """ paso un segundo, reviso que tengo que hacer """
    #     # reviso si algun boton sigue presionado
    #     ## Power Buttons
    #     if self.powerUpButtonCnt > 3:
    #         self.PwrUp(10)
    #     elif self.powerUpButtonCnt > 1:
    #         self.PwrUp(5)
    #         self.powerUpButtonCnt += 1
    #     elif self.powerUpButtonCnt == 1:
    #         self.powerUpButtonCnt += 1

    #     if self.powerDwnButtonCnt > 3:
    #         self.PwrDwn(10)
    #     elif self.powerDwnButtonCnt > 1:
    #         self.PwrDwn(5)
    #         self.powerDwnButtonCnt += 1
    #     elif self.powerDwnButtonCnt == 1:
    #         self.powerDwnButtonCnt += 1

    #     ## Time Buttons
    #     if self.timeUpButtonCnt > 3:
    #         self.TimeUp(10)
    #     elif self.timeUpButtonCnt > 1:
    #         self.TimeUp(5)
    #         self.timeUpButtonCnt += 1            
    #     elif  self.timeUpButtonCnt == 1:
    #         self.timeUpButtonCnt += 1

    #     if self.timeDwnButtonCnt > 3:
    #         self.TimeDwn(10)
    #     elif self.timeDwnButtonCnt > 1:
    #         self.TimeDwn(5)
    #         self.timeDwnButtonCnt += 1            
    #     elif self.timeDwnButtonCnt == 1:
    #         self.timeDwnButtonCnt += 1

    #     # check for screensaver activation
    #     # if self.screensaver_window == True:
    #     #     if self.timer_screensaver > 0:
    #     #         self.timer_screensaver -= 1
    #     #     else:
    #     #         self.ScreenSaverDialogScreen()


    
    def SelectButton_mema (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'memaButton':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'memaButton':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.memaDescLabel.setStyleSheet(self.label_orig)
            self.ui.memaOneLabel.setStyleSheet(self.label_orig)
            self.ui.memaTwoLabel.setStyleSheet(self.label_orig)
            self.ui.memaThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'memaButton'
            # go blue on memaButton
            self.ui.memaDescLabel.setStyleSheet(self.label_blue)
            self.ui.memaOneLabel.setStyleSheet(self.label_blue)
            self.ui.memaTwoLabel.setStyleSheet(self.label_blue)
            self.ui.memaThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'memaButton'
            # go cyan on memaButton
            self.ui.memaDescLabel.setStyleSheet(self.label_cyan)
            self.ui.memaOneLabel.setStyleSheet(self.label_cyan)
            self.ui.memaTwoLabel.setStyleSheet(self.label_cyan)
            self.ui.memaThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_memb (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'membButton':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'membButton':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.membDescLabel.setStyleSheet(self.label_orig)
            self.ui.membOneLabel.setStyleSheet(self.label_orig)
            self.ui.membTwoLabel.setStyleSheet(self.label_orig)
            self.ui.membThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'membButton'
            # go blue on membButton
            self.ui.membDescLabel.setStyleSheet(self.label_blue)
            self.ui.membOneLabel.setStyleSheet(self.label_blue)
            self.ui.membTwoLabel.setStyleSheet(self.label_blue)
            self.ui.membThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'membButton'
            # go cyan on membButton
            self.ui.membDescLabel.setStyleSheet(self.label_cyan)
            self.ui.membOneLabel.setStyleSheet(self.label_cyan)
            self.ui.membTwoLabel.setStyleSheet(self.label_cyan)
            self.ui.membThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_memc (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'memcButton':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'memcButton':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.memcDescLabel.setStyleSheet(self.label_orig)
            self.ui.memcOneLabel.setStyleSheet(self.label_orig)
            self.ui.memcTwoLabel.setStyleSheet(self.label_orig)
            self.ui.memcThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'memcButton'
            # go blue on memcButton
            self.ui.memcDescLabel.setStyleSheet(self.label_blue)
            self.ui.memcOneLabel.setStyleSheet(self.label_blue)
            self.ui.memcTwoLabel.setStyleSheet(self.label_blue)
            self.ui.memcThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'memcButton'
            # go cyan on memcButton
            self.ui.memcDescLabel.setStyleSheet(self.label_cyan)
            self.ui.memcOneLabel.setStyleSheet(self.label_cyan)
            self.ui.memcTwoLabel.setStyleSheet(self.label_cyan)
            self.ui.memcThreeLabel.setStyleSheet(self.label_cyan)
        

    def SelectButton_memd (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'memdButton':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'memdButton':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.memdDescLabel.setStyleSheet(self.label_orig)
            self.ui.memdOneLabel.setStyleSheet(self.label_orig)
            self.ui.memdTwoLabel.setStyleSheet(self.label_orig)
            self.ui.memdThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'memdButton'
            # go blue on memdButton
            self.ui.memdDescLabel.setStyleSheet(self.label_blue)
            self.ui.memdOneLabel.setStyleSheet(self.label_blue)
            self.ui.memdTwoLabel.setStyleSheet(self.label_blue)
            self.ui.memdThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'memdButton'
            # go cyan on memdButton
            self.ui.memdDescLabel.setStyleSheet(self.label_cyan)
            self.ui.memdOneLabel.setStyleSheet(self.label_cyan)
            self.ui.memdTwoLabel.setStyleSheet(self.label_cyan)
            self.ui.memdThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem5 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem5Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem5Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem5DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem5OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem5TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem5ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem5Button'
            # go blue on mem5Button
            self.ui.mem5DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem5OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem5TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem5ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem5Button'
            # go cyan on mem5Button
            self.ui.mem5DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem5OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem5TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem5ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem6 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem6Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem6Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem6DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem6OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem6TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem6ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem6Button'
            # go blue on mem6Button
            self.ui.mem6DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem6OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem6TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem6ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem6Button'
            # go cyan on mem6Button
            self.ui.mem6DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem6OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem6TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem6ThreeLabel.setStyleSheet(self.label_cyan)
            

    def SelectButton_mem7 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem7Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem7Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem7DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem7OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem7TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem7ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem7Button'
            # go blue on mem7Button
            self.ui.mem7DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem7OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem7TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem7ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem7Button'
            # go cyan on mem7Button
            self.ui.mem7DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem7OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem7TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem7ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem8 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem8Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem8Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem8DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem8OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem8TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem8ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem8Button'
            # go blue on mem8Button
            self.ui.mem8DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem8OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem8TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem8ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem8Button'
            # go cyan on mem8Button
            self.ui.mem8DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem8OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem8TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem8ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem9 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem9Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem9Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem9DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem9OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem9TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem9ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem9Button'
            # go blue on mem9Button
            self.ui.mem9DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem9OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem9TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem9ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem9Button'
            # go cyan on mem9Button
            self.ui.mem9DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem9OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem9TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem9ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem10 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem10Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem10Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem10DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem10OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem10TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem10ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem10Button'
            # go blue on mem10Button
            self.ui.mem10DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem10OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem10TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem10ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem10Button'
            # go cyan on mem10Button
            self.ui.mem10DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem10OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem10TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem10ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem11 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem11Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem11Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem11DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem11OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem11TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem11ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem11Button'
            # go blue on mem11Button
            self.ui.mem11DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem11OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem11TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem11ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem11Button'
            # go cyan on mem11Button
            self.ui.mem11DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem11OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem11TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem11ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem12 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem12Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem12Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem12DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem12OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem12TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem12ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem12Button'
            # go blue on mem12Button
            self.ui.mem12DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem12OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem12TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem12ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem12Button'
            # go cyan on mem12Button
            self.ui.mem12DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem12OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem12TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem12ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem13 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem13Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem13Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem13DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem13OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem13TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem13ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem13Button'
            # go blue on mem13Button
            self.ui.mem13DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem13OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem13TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem13ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem13Button'
            # go cyan on mem13Button
            self.ui.mem13DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem13OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem13TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem13ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem14 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem14Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem14Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem14DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem14OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem14TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem14ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem14Button'
            # go blue on mem14Button
            self.ui.mem14DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem14OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem14TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem14ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem14Button'
            # go cyan on mem14Button
            self.ui.mem14DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem14OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem14TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem14ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem15 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem15Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem15Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem15DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem15OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem15TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem15ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem15Button'
            # go blue on mem15Button
            self.ui.mem15DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem15OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem15TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem15ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem15Button'
            # go cyan on mem15Button
            self.ui.mem15DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem15OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem15TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem15ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem16 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem16Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem16Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem16DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem16OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem16TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem16ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem16Button'
            # go blue on mem16Button
            self.ui.mem16DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem16OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem16TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem16ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem16Button'
            # go cyan on mem16Button
            self.ui.mem16DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem16OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem16TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem16ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem17 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem17Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem17Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem17DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem17OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem17TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem17ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem17Button'
            # go blue on mem17Button
            self.ui.mem17DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem17OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem17TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem17ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem17Button'
            # go cyan on mem17Button
            self.ui.mem17DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem17OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem17TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem17ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem18 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem18Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem18Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem18DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem18OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem18TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem18ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem18Button'
            # go blue on mem18Button
            self.ui.mem18DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem18OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem18TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem18ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem18Button'
            # go cyan on mem18Button
            self.ui.mem18DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem18OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem18TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem18ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem19 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem19Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem19Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem19DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem19OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem19TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem19ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem19Button'
            # go blue on mem19Button
            self.ui.mem19DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem19OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem19TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem19ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem19Button'
            # go cyan on mem19Button
            self.ui.mem19DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem19OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem19TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem19ThreeLabel.setStyleSheet(self.label_cyan)


    def SelectButton_mem20 (self):
        # first check if we are previusly selected
        unselect = False
        if self.selected_blue == 'mem20Button':
            self.selected_blue = ''
            unselect = True

        if self.selected_cyan == 'mem20Button':
            self.selected_cyan = ''            
            unselect = True

        # go unselected
        if unselect:
            self.ui.mem20DescLabel.setStyleSheet(self.label_orig)
            self.ui.mem20OneLabel.setStyleSheet(self.label_orig)
            self.ui.mem20TwoLabel.setStyleSheet(self.label_orig)
            self.ui.mem20ThreeLabel.setStyleSheet(self.label_orig)
            return

        # check two selections
        if self.selected_blue != '' and self.selected_cyan != '':
            return

        if self.selected_blue == '':
            self.selected_blue = 'mem20Button'
            # go blue on mem20Button
            self.ui.mem20DescLabel.setStyleSheet(self.label_blue)
            self.ui.mem20OneLabel.setStyleSheet(self.label_blue)
            self.ui.mem20TwoLabel.setStyleSheet(self.label_blue)
            self.ui.mem20ThreeLabel.setStyleSheet(self.label_blue)

        elif self.selected_cyan == '':
            self.selected_cyan = 'mem20Button'
            # go cyan on mem20Button
            self.ui.mem20DescLabel.setStyleSheet(self.label_cyan)
            self.ui.mem20OneLabel.setStyleSheet(self.label_cyan)
            self.ui.mem20TwoLabel.setStyleSheet(self.label_cyan)
            self.ui.mem20ThreeLabel.setStyleSheet(self.label_cyan)

            
    # def SelectStageButton2 (self):
    #     self.stage_selected = 'stage2'
    #     self.stage2_info.status = 'enable'
    #     self.Stage2GroupChange('select')

    #     if self.stage1_info.status == 'enable':
    #         self.Stage1GroupChange('enable')

    #     if self.stage3_info.status == 'enable':
    #         self.Stage3GroupChange('enable')

    #     pwr_saved = self.StagesGetSelectedPower()
    #     if pwr_saved < 10:
    #         pwr_saved = 10
    #         self.StagesUpdateSelectedPower(pwr_saved)
            
    #     time_saved = self.StagesGetSelectedTime()        
    #     if time_saved < 1:
    #         time_saved = 1
    #         self.StagesUpdateSelectedTime(time_saved)

    #     self.ui.powerLabel.setText(str(pwr_saved))
    #     self.ui.minutesLabel.setText(str(time_saved))        
    #     self.FrequencyChangeTo(self.stage2_info.GetStageFrequency())
    #     self.SignalChangeTo(self.stage2_info.GetStageSignal())
    #     self.UpdateTotalTime()

        
    # def SelectStageButton3 (self):
    #     self.stage_selected = 'stage3'
    #     self.stage3_info.status = 'enable'
    #     self.Stage3GroupChange('select')

    #     if self.stage1_info.status == 'enable':
    #         self.Stage1GroupChange('enable')

    #     if self.stage2_info.status == 'enable':
    #         self.Stage2GroupChange('enable')

    #     pwr_saved = self.StagesGetSelectedPower()
    #     if pwr_saved < 10:
    #         pwr_saved = 10
    #         self.StagesUpdateSelectedPower(pwr_saved)
            
    #     time_saved = self.StagesGetSelectedTime()
    #     if time_saved < 1:
    #         time_saved = 1
    #         self.StagesUpdateSelectedTime(time_saved)
            
    #     self.ui.powerLabel.setText(str(pwr_saved))
    #     self.ui.minutesLabel.setText(str(time_saved))
    #     self.FrequencyChangeTo(self.stage3_info.GetStageFrequency())
    #     self.SignalChangeTo(self.stage3_info.GetStageSignal())
    #     self.UpdateTotalTime()

            
    # def Stage1GroupChange (self, change_to):
    #     raise_inners = False
        
    #     if change_to == 'enable':
    #         self.ui.stage1MinutesLabel.setText(str(self.stage1_info.timer)+"'")
    #         self.ui.stage1PowerLabel.setText(str(self.stage1_info.power)+"%")
    #         self.ui.stage1Label.setStyleSheet(self.style.stage1_button_enable)
    #         raise_inners = True

    #     if change_to == 'select':
    #         self.ui.stage1MinutesLabel.setText(str(self.stage1_info.timer)+"'")
    #         self.ui.stage1PowerLabel.setText(str(self.stage1_info.power)+"%")
    #         self.ui.stage1Label.setStyleSheet(self.style.stage1_button_select)
    #         raise_inners = True            

    #     if change_to == 'disable':
    #         self.ui.stage1MinutesLabel.setText('')
    #         self.ui.stage1PowerLabel.setText('')            
    #         self.ui.stage1Label.setStyleSheet(self.style.stage1_button_disable)
    #         self.ui.stage1Label.raise_()
            
    #     if raise_inners:
    #         # fix all picture, raise all small pics over background label,
    #         self.ui.stage1MinutesLabel.raise_()
    #         self.ui.stage1PowerLabel.raise_()
    #         self.ui.stage1SignalButton.raise_()
    #         self.ui.stage1FreqButton.raise_()

    #     # then raise transparent button
    #     self.ui.stage1Button.raise_()

        
    # def Stage2GroupChange (self, change_to):
    #     raise_inners = False
        
    #     if change_to == 'enable':
    #         self.ui.stage2MinutesLabel.setText(str(self.stage2_info.timer)+"'")
    #         self.ui.stage2PowerLabel.setText(str(self.stage2_info.power)+"%")
    #         self.ui.stage2Label.setStyleSheet(self.style.stage2_button_enable)
    #         raise_inners = True

    #     if change_to == 'select':
    #         self.ui.stage2MinutesLabel.setText(str(self.stage2_info.timer)+"'")
    #         self.ui.stage2PowerLabel.setText(str(self.stage2_info.power)+"%")
    #         self.ui.stage2Label.setStyleSheet(self.style.stage2_button_select)
    #         raise_inners = True            

    #     if change_to == 'disable':
    #         self.ui.stage2MinutesLabel.setText('')
    #         self.ui.stage2PowerLabel.setText('')            
    #         self.ui.stage2Label.setStyleSheet(self.style.stage2_button_disable)
    #         self.ui.stage2Label.raise_()
            
    #     if raise_inners:
    #         # fix all picture, raise all small pics over background label,
    #         self.ui.stage2MinutesLabel.raise_()
    #         self.ui.stage2PowerLabel.raise_()
    #         self.ui.stage2SignalButton.raise_()
    #         self.ui.stage2FreqButton.raise_()

    #     # then raise transparent button
    #     self.ui.stage2Button.raise_()


    # def Stage3GroupChange (self, change_to):
    #     raise_inners = False
        
    #     if change_to == 'enable':
    #         self.ui.stage3MinutesLabel.setText(str(self.stage3_info.timer)+"'")
    #         self.ui.stage3PowerLabel.setText(str(self.stage3_info.power)+"%")
    #         self.ui.stage3Label.setStyleSheet(self.style.stage3_button_enable)
    #         raise_inners = True

    #     if change_to == 'select':
    #         self.ui.stage3MinutesLabel.setText(str(self.stage3_info.timer)+"'")
    #         self.ui.stage3PowerLabel.setText(str(self.stage3_info.power)+"%")
    #         self.ui.stage3Label.setStyleSheet(self.style.stage3_button_select)
    #         raise_inners = True            

    #     if change_to == 'disable':
    #         self.ui.stage3MinutesLabel.setText('')
    #         self.ui.stage3PowerLabel.setText('')            
    #         self.ui.stage3Label.setStyleSheet(self.style.stage3_button_disable)
    #         self.ui.stage3Label.raise_()
            
    #     if raise_inners:
    #         # fix all picture, raise all small pics over background label,
    #         self.ui.stage3MinutesLabel.raise_()
    #         self.ui.stage3PowerLabel.raise_()
    #         self.ui.stage3SignalButton.raise_()
    #         self.ui.stage3FreqButton.raise_()

    #     # then raise transparent button
    #     self.ui.stage3Button.raise_()

        
    # def SignalDisableAll(self):
    #     self.ui.triangularButton.setStyleSheet(self.style.triangular_90_disable)
    #     self.ui.squareButton.setStyleSheet(self.style.square_90_disable)
    #     self.ui.sinusoidalButton.setStyleSheet(self.style.sinusoidal_90_disable)


    # def SignalChange (self):
    #     sender = self.sender()

    #     if sender.objectName() == 'triangularButton':
    #         self.SignalChangeTo('triangular')

    #     elif sender.objectName() == 'squareButton':
    #         self.SignalChangeTo('square')

    #     elif sender.objectName() == 'sinusoidalButton':
    #         self.SignalChangeTo('sinusoidal')

    #     self.ScreenSaverKick()

        
    # def SignalChangeTo (self, new_signal):
    #     self.SignalDisableAll()
        
    #     if new_signal == 'triangular':
    #         self.ui.triangularButton.setStyleSheet(self.style.triangular_90_enable)

    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1SignalButton.setStyleSheet(self.style.triangular_75_enable)
    #             self.stage1_info.SetStageSignal('triangular')
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2SignalButton.setStyleSheet(self.style.triangular_75_enable)
    #             self.stage2_info.SetStageSignal('triangular')
    #         else:
    #             self.ui.stage3SignalButton.setStyleSheet(self.style.triangular_75_enable)
    #             self.stage3_info.SetStageSignal('triangular')

    #     elif new_signal == 'square':
    #         self.ui.squareButton.setStyleSheet(self.style.square_90_enable)

    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1SignalButton.setStyleSheet(self.style.square_75_enable)
    #             self.stage1_info.SetStageSignal('square')
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2SignalButton.setStyleSheet(self.style.square_75_enable)
    #             self.stage2_info.SetStageSignal('square')
    #         else:
    #             self.ui.stage3SignalButton.setStyleSheet(self.style.square_75_enable)
    #             self.stage3_info.SetStageSignal('square')            

    #     elif new_signal == 'sinusoidal':
    #         self.ui.sinusoidalButton.setStyleSheet(self.style.sinusoidal_90_enable)

    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
    #             self.stage1_info.SetStageSignal('sinusoidal')
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
    #             self.stage2_info.SetStageSignal('sinusoidal')
    #         else:
    #             self.ui.stage3SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
    #             self.stage3_info.SetStageSignal('sinusoidal')
        

    # def FrequencyDisableAll(self):
    #     self.ui.freq1Button.setStyleSheet(self.style.freq1_90_disable)
    #     self.ui.freq2Button.setStyleSheet(self.style.freq2_90_disable)
    #     self.ui.freq3Button.setStyleSheet(self.style.freq3_90_disable)
    #     self.ui.freq4Button.setStyleSheet(self.style.freq4_90_disable)
    #     self.ui.freq5Button.setStyleSheet(self.style.freq5_90_disable)
    #     self.ui.freq6Button.setStyleSheet(self.style.freq6_90_disable)
    #     self.ui.freq7Button.setStyleSheet(self.style.freq7_90_disable)
    #     self.ui.freq8Button.setStyleSheet(self.style.freq8_90_disable)
    #     self.ui.freq9Button.setStyleSheet(self.style.freq9_90_disable)
    #     self.ui.freq10Button.setStyleSheet(self.style.freq10_90_disable)        


    # def FrequencyChange (self):
    #     sender = self.sender()

    #     if sender.objectName() == 'freq1Button':
    #         self.FrequencyChangeTo('freq1')

    #     if sender.objectName() == 'freq2Button':
    #         self.FrequencyChangeTo('freq2')

    #     if sender.objectName() == 'freq3Button':
    #         self.FrequencyChangeTo('freq3')

    #     if sender.objectName() == 'freq4Button':
    #         self.FrequencyChangeTo('freq4')

    #     if sender.objectName() == 'freq5Button':
    #         self.FrequencyChangeTo('freq5')

    #     if sender.objectName() == 'freq6Button':
    #         self.FrequencyChangeTo('freq6')

    #     if sender.objectName() == 'freq7Button':
    #         self.FrequencyChangeTo('freq7')

    #     if sender.objectName() == 'freq8Button':
    #         self.FrequencyChangeTo('freq8')

    #     if sender.objectName() == 'freq9Button':
    #         self.FrequencyChangeTo('freq9')

    #     if sender.objectName() == 'freq10Button':
    #         self.FrequencyChangeTo('freq10')
            
    #     self.ScreenSaverKick()


    # def FrequencyChangeTo (self, new_freq):
    #     self.FrequencyDisableAll()
        
    #     if new_freq == 'freq1':
    #         self.ui.freq1Button.setStyleSheet(self.style.freq1_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq1_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq1_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq1_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq2':
    #         self.ui.freq2Button.setStyleSheet(self.style.freq2_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq2_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq2_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq2_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq3':
    #         self.ui.freq3Button.setStyleSheet(self.style.freq3_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq3_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq3_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq3_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq4':
    #         self.ui.freq4Button.setStyleSheet(self.style.freq4_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq4_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq4_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq4_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq5':
    #         self.ui.freq5Button.setStyleSheet(self.style.freq5_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq5_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq5_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq5_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq6':
    #         self.ui.freq6Button.setStyleSheet(self.style.freq6_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq6_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq6_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq6_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq7':
    #         self.ui.freq7Button.setStyleSheet(self.style.freq7_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq7_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq7_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq7_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq8':
    #         self.ui.freq8Button.setStyleSheet(self.style.freq8_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq8_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq8_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq8_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq9':
    #         self.ui.freq9Button.setStyleSheet(self.style.freq9_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq9_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq9_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq9_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)

    #     if new_freq == 'freq10':
    #         self.ui.freq10Button.setStyleSheet(self.style.freq10_90_enable)
    #         if self.stage_selected == 'stage1':
    #             self.ui.stage1FreqButton.setStyleSheet(self.style.freq10_75_enable)
    #             self.stage1_info.SetStageFrequency(new_freq)
    #         elif self.stage_selected == 'stage2':
    #             self.ui.stage2FreqButton.setStyleSheet(self.style.freq10_75_enable)
    #             self.stage2_info.SetStageFrequency(new_freq)
    #         else:
    #             self.ui.stage3FreqButton.setStyleSheet(self.style.freq10_75_enable)
    #             self.stage3_info.SetStageFrequency(new_freq)
            

    # def UpPowerPressed (self):
    #     self.PwrUp (1)
    #     self.powerUpButtonCnt = 1
    #     # self.ScreenSaverKick()

    # def UpPowerReleased (self):
    #     self.powerUpButtonCnt = 0

    # def DwnPowerPressed (self):
    #     self.PwrDwn(1)
    #     self.powerDwnButtonCnt = 1
    #     # self.ScreenSaverKick()        

    # def DwnPowerReleased (self):
    #     self.powerDwnButtonCnt = 0        

    # def UpTimePressed (self):
    #     self.TimeUp (1)
    #     self.timeUpButtonCnt = 1
    #     # self.ScreenSaverKick()        

    # def UpTimeReleased (self):
    #     self.timeUpButtonCnt = 0        

    # def DwnTimePressed (self):
    #     self.TimeDwn(1)
    #     self.timeDwnButtonCnt = 1
    #     # self.ScreenSaverKick()

    # def DwnTimeReleased (self):
    #     self.timeDwnButtonCnt = 0
    

    # def PwrUp (self, new_pwr):
    #     last_pwr = int(self.ui.powerLabel.text())
    #     if (last_pwr + new_pwr) < 100:
    #         last_pwr += new_pwr
    #     else:
    #         last_pwr = 100

    #     self.ui.powerLabel.setText(str(last_pwr))
    #     self.StagesUpdateSelectedPower(last_pwr)

        
    # def PwrDwn (self, new_pwr):
    #     last_pwr = int(self.ui.powerLabel.text())
    #     if (last_pwr - new_pwr) > 10:
    #         last_pwr -= new_pwr
    #     else:
    #         last_pwr = 10

    #     self.ui.powerLabel.setText(str(last_pwr))
    #     self.StagesUpdateSelectedPower(last_pwr)        

        
    # def TimeUp (self, new_time):
    #     last_time = int(self.ui.minutesLabel.text())
    #     if ((last_time + new_time) < 120):
    #         last_time += new_time
    #     else:
    #         last_time = 120
            
    #     self.ui.minutesLabel.setText(str(last_time))
    #     self.StagesUpdateSelectedTime(last_time)
    #     self.UpdateTotalTime()

        
    # def TimeDwn (self, new_time):
    #     last_time = int(self.ui.minutesLabel.text())
    #     if ((last_time - new_time) > 1):
    #         last_time -= new_time
    #     else:
    #         last_time = 1
            
    #     self.ui.minutesLabel.setText(str(last_time))
    #     self.StagesUpdateSelectedTime(last_time)
    #     self.UpdateTotalTime()
    

    # def StagesUpdateSelectedPower (self, new_pwr):
    #     if self.stage_selected == 'stage1':
    #         self.ui.stage1PowerLabel.setText(str(new_pwr)+'%')
    #         self.stage1_info.SetStagePower(new_pwr)
    #     elif self.stage_selected == 'stage2':
    #         self.ui.stage2PowerLabel.setText(str(new_pwr)+'%')
    #         self.stage2_info.SetStagePower(new_pwr)
    #     else:
    #         self.ui.stage3PowerLabel.setText(str(new_pwr)+'%')
    #         self.stage3_info.SetStagePower(new_pwr)

            
    # def StagesUpdateSelectedTime (self, new_time):
    #     if self.stage_selected == 'stage1':
    #         self.ui.stage1MinutesLabel.setText(str(new_time)+"'")
    #         self.stage1_info.SetStageTimer(new_time)
    #     elif self.stage_selected == 'stage2':
    #         self.ui.stage2MinutesLabel.setText(str(new_time)+"'")
    #         self.stage2_info.SetStageTimer(new_time)
    #     else:
    #         self.ui.stage3MinutesLabel.setText(str(new_time)+"'")
    #         self.stage3_info.SetStageTimer(new_time)

            
    # def StagesGetSelectedPower (self):
    #     if self.stage_selected == 'stage1':
    #         pwr_str = self.ui.stage1PowerLabel.text()
    #         pwr_str = pwr_str[:-1]
    #         pwr_save = int(pwr_str)
    #     elif self.stage_selected == 'stage2':
    #         pwr_str = self.ui.stage2PowerLabel.text()
    #         pwr_str = pwr_str[:-1]
    #         pwr_save = int(pwr_str)
    #     else:
    #         pwr_str = self.ui.stage3PowerLabel.text()
    #         pwr_str = pwr_str[:-1]
    #         pwr_save = int(pwr_str)

    #     return pwr_save

            
    # def StagesGetSelectedTime (self):
    #     if self.stage_selected == 'stage1':
    #         time_str = self.ui.stage1MinutesLabel.text()
    #         time_str = time_str[:-1]
    #         time_save = int(time_str)
    #     elif self.stage_selected == 'stage2':
    #         time_str = self.ui.stage2MinutesLabel.text()
    #         time_str = time_str[:-1]
    #         time_save = int(time_str)
    #     else:
    #         time_str = self.ui.stage3MinutesLabel.text()
    #         time_str = time_str[:-1]
    #         time_save = int(time_str)

    #     return time_save
            
            
    # def ScreenSaverKick (self):
    #     pass

    
    # def ClearStage (self):
    #     first_stage_not_disable = 'stage1'
        
    #     if self.stage_selected == 'stage1':
    #         # check if the other two are disabled
    #         if self.stage2_info.GetStageStatus() != 'disable' or \
    #            self.stage3_info.GetStageStatus() != 'disable':
    #             self.stage1_info.SetStageStatus('disable')
    #             self.Stage1GroupChange('disable')

    #             if self.stage2_info.GetStageStatus() != 'disable':
    #                 self.SelectStageButton2()
    #             else:
    #                 self.SelectStageButton3()

    #     elif self.stage_selected == 'stage2':
    #         # check if the other two are disabled
    #         if self.stage1_info.GetStageStatus() != 'disable' or \
    #            self.stage3_info.GetStageStatus() != 'disable':
    #             self.stage2_info.SetStageStatus('disable')
    #             self.Stage2GroupChange('disable')

    #             if self.stage1_info.GetStageStatus() != 'disable':
    #                 self.SelectStageButton1()
    #             else:
    #                 self.SelectStageButton3()
                    
    #     else:
    #         # check if the other two are disabled
    #         if self.stage1_info.GetStageStatus() != 'disable' or \
    #            self.stage2_info.GetStageStatus() != 'disable':
    #             self.stage3_info.SetStageStatus('disable')
    #             self.Stage3GroupChange('disable')

    #             if self.stage1_info.GetStageStatus() != 'disable':
    #                 self.SelectStageButton1()
    #             else:
    #                 self.SelectStageButton2()


    # def UpdateTotalTime (self):
    #     total_time = 0
    #     if self.stage1_info.GetStageStatus() == 'enable':
    #         total_time += self.stage1_info.GetStageTimer()

    #     if self.stage2_info.GetStageStatus() == 'enable':
    #         total_time += self.stage2_info.GetStageTimer()

    #     if self.stage3_info.GetStageStatus() == 'enable':
    #         total_time += self.stage3_info.GetStageTimer()

    #     self.ui.totalMinutesLabel.setText(str(total_time))
            
        
    # def BackStage (self):
    #     self.action = 'none'
    #     self.accept()
    

        
        
### end of file ###

