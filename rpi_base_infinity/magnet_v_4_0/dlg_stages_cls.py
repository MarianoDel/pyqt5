from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QTimer


#get the UI from here
from ui_stages_dlg import Ui_StagesDialog


##################################################
# StagesDialog Class - to save or empty memories #
##################################################
class StagesDialog (QDialog):

    #SIGNALS
    one_second_signal = pyqtSignal()

    def __init__(self, st_lst, style_obj, caller_stage='stage1'):
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
        self.stage_selected = caller_stage

        self.powerUpButtonCnt = 0
        self.powerDwnButtonCnt = 0
        self.timeUpButtonCnt = 0
        self.timeDwnButtonCnt = 0
        
        # get the close event and connect the buttons
        self.ui.clearButton.clicked.connect(self.ClearStage)
        self.ui.backButton.clicked.connect(self.BackStage)
        self.ui.acceptButton.clicked.connect(self.accept)

        self.ui.stage1Button.clicked.connect(self.SelectStageButton1)
        self.ui.stage2Button.clicked.connect(self.SelectStageButton2)
        self.ui.stage3Button.clicked.connect(self.SelectStageButton3)

        self.ui.freq1Button.clicked.connect(self.FrequencyChange)
        self.ui.freq2Button.clicked.connect(self.FrequencyChange)
        self.ui.freq3Button.clicked.connect(self.FrequencyChange)
        self.ui.freq4Button.clicked.connect(self.FrequencyChange)
        self.ui.freq5Button.clicked.connect(self.FrequencyChange)
        self.ui.freq6Button.clicked.connect(self.FrequencyChange)
        self.ui.freq7Button.clicked.connect(self.FrequencyChange)
        self.ui.freq8Button.clicked.connect(self.FrequencyChange)
        self.ui.freq9Button.clicked.connect(self.FrequencyChange)
        self.ui.freq10Button.clicked.connect(self.FrequencyChange)        

        self.ui.triangularButton.clicked.connect(self.SignalChange)
        self.ui.squareButton.clicked.connect(self.SignalChange)
        self.ui.sinusoidalButton.clicked.connect(self.SignalChange)

        self.ui.powerUpButton.pressed.connect(self.UpPowerPressed)
        self.ui.powerUpButton.released.connect(self.UpPowerReleased)
        self.ui.powerDwnButton.pressed.connect(self.DwnPowerPressed)
        self.ui.powerDwnButton.released.connect(self.DwnPowerReleased)
        self.ui.timeUpButton.pressed.connect(self.UpTimePressed)
        self.ui.timeUpButton.released.connect(self.UpTimeReleased)        
        self.ui.timeDwnButton.pressed.connect(self.DwnTimePressed)
        self.ui.timeDwnButton.released.connect(self.DwnTimeReleased)
        
        # check enables or disables
        if self.stage1_info.GetStageStatus() == 'enable':
            self.Stage1GroupChange('enable')
        else:
            self.Stage1GroupChange('disable')
            
        if self.stage2_info.GetStageStatus() == 'enable':
            self.Stage2GroupChange('enable')
        else:
            self.Stage2GroupChange('disable')
        
        if self.stage3_info.GetStageStatus() == 'enable':
            self.Stage3GroupChange('enable')
        else:
            self.Stage3GroupChange('disable')

        
        # check which was selected, or select the first one
        if self.stage_selected == 'stage1':
            self.Stage1GroupChange('select')
        elif self.stage_selected == 'stage2':
            self.Stage2GroupChange('select')
        else:
            self.Stage3GroupChange('select')


        ## activate the 1 second timer it is repetitive
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        # screen saver timer activation
        # self.timer_screensaver = self.t.timeout_screensaver
        # self.screensaver_window = True
            
        #SIGNALS CONNECTION
        # connect through a signal the timer to the update event function
        self.one_second_signal.connect(self.UpdateOneSec)
            

    # one second update signal
    def TimerOneSec(self):
        self.one_second_signal.emit()
        

    # one second update event function
    def UpdateOneSec (self):
        """ paso un segundo, reviso que tengo que hacer """
        # reviso si algun boton sigue presionado
        ## Power Buttons
        if self.powerUpButtonCnt > 3:
            self.PwrUp(10)
        elif self.powerUpButtonCnt > 1:
            self.PwrUp(5)
            self.powerUpButtonCnt += 1
        elif self.powerUpButtonCnt == 1:
            self.powerUpButtonCnt += 1

        if self.powerDwnButtonCnt > 3:
            self.PwrDwn(10)
        elif self.powerDwnButtonCnt > 1:
            self.PwrDwn(5)
            self.powerDwnButtonCnt += 1
        elif self.powerDwnButtonCnt == 1:
            self.powerDwnButtonCnt += 1

        ## Time Buttons
        if self.timeUpButtonCnt > 3:
            self.TimeUp(10)
        elif self.timeUpButtonCnt > 1:
            self.TimeUp(5)
            self.timeUpButtonCnt += 1            
        elif  self.timeUpButtonCnt == 1:
            self.timeUpButtonCnt += 1

        if self.timeDwnButtonCnt > 3:
            self.TimeDwn(10)
        elif self.timeDwnButtonCnt > 1:
            self.TimeDwn(5)
            self.timeDwnButtonCnt += 1            
        elif self.timeDwnButtonCnt == 1:
            self.timeDwnButtonCnt += 1

        # check for screensaver activation
        # if self.screensaver_window == True:
        #     if self.timer_screensaver > 0:
        #         self.timer_screensaver -= 1
        #     else:
        #         self.ScreenSaverDialogScreen()


    
    def SelectStageButton1 (self):
        self.stage_selected = 'stage1'
        self.Stage1GroupChange('select')

        if self.stage2_info.status == 'enable':
            self.Stage2GroupChange('enable')

        if self.stage3_info.status == 'enable':
            self.Stage3GroupChange('enable')

        pwr_saved = self.StagesGetSelectedPower()
        time_saved = self.StagesGetSelectedTime()
        self.ui.powerLabel.setText(str(pwr_saved))
        self.ui.minutesLabel.setText(str(time_saved))        
            

    def SelectStageButton2 (self):
        self.stage_selected = 'stage2'
        self.Stage2GroupChange('select')

        if self.stage1_info.status == 'enable':
            self.Stage1GroupChange('enable')

        if self.stage3_info.status == 'enable':
            self.Stage3GroupChange('enable')

        pwr_saved = self.StagesGetSelectedPower()
        time_saved = self.StagesGetSelectedTime()        
        self.ui.powerLabel.setText(str(pwr_saved))
        self.ui.minutesLabel.setText(str(time_saved))        

        
    def SelectStageButton3 (self):
        self.stage_selected = 'stage3'
        self.Stage3GroupChange('select')

        if self.stage1_info.status == 'enable':
            self.Stage1GroupChange('enable')

        if self.stage2_info.status == 'enable':
            self.Stage2GroupChange('enable')

        pwr_saved = self.StagesGetSelectedPower()
        time_saved = self.StagesGetSelectedTime()        
        self.ui.powerLabel.setText(str(pwr_saved))
        self.ui.minutesLabel.setText(str(time_saved))        

            
    def Stage1GroupChange (self, change_to):
        raise_inners = False
        
        if change_to == 'enable':
            self.ui.stage1MinutesLabel.setText(str(self.stage1_info.timer)+"'")
            self.ui.stage1PowerLabel.setText(str(self.stage1_info.power)+"%")
            self.ui.stage1Label.setStyleSheet(self.style.stage1_button_enable)
            raise_inners = True

        if change_to == 'select':
            self.ui.stage1MinutesLabel.setText(str(self.stage1_info.timer)+"'")
            self.ui.stage1PowerLabel.setText(str(self.stage1_info.power)+"%")
            self.ui.stage1Label.setStyleSheet(self.style.stage1_button_select)
            raise_inners = True            

        if change_to == 'disable':
            self.ui.stage1MinutesLabel.setText('')
            self.ui.stage1PowerLabel.setText('')            
            self.ui.stage1Label.setStyleSheet(self.style.stage1_button_disable)
            self.ui.stage1Label.raise_()
            
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
            self.ui.stage2MinutesLabel.setText(str(self.stage2_info.timer)+"'")
            self.ui.stage2PowerLabel.setText(str(self.stage2_info.power)+"%")
            self.ui.stage2Label.setStyleSheet(self.style.stage2_button_enable)
            raise_inners = True

        if change_to == 'select':
            self.ui.stage2MinutesLabel.setText(str(self.stage2_info.timer)+"'")
            self.ui.stage2PowerLabel.setText(str(self.stage2_info.power)+"%")
            self.ui.stage2Label.setStyleSheet(self.style.stage2_button_select)
            raise_inners = True            

        if change_to == 'disable':
            self.ui.stage2MinutesLabel.setText('')
            self.ui.stage2PowerLabel.setText('')            
            self.ui.stage2Label.setStyleSheet(self.style.stage2_button_disable)
            self.ui.stage2Label.raise_()
            
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
            self.ui.stage3MinutesLabel.setText(str(self.stage3_info.timer)+"'")
            self.ui.stage3PowerLabel.setText(str(self.stage3_info.power)+"%")
            self.ui.stage3Label.setStyleSheet(self.style.stage3_button_enable)
            raise_inners = True

        if change_to == 'select':
            self.ui.stage3MinutesLabel.setText(str(self.stage3_info.timer)+"'")
            self.ui.stage3PowerLabel.setText(str(self.stage3_info.power)+"%")
            self.ui.stage3Label.setStyleSheet(self.style.stage3_button_select)
            raise_inners = True            

        if change_to == 'disable':
            self.ui.stage3MinutesLabel.setText('')
            self.ui.stage3PowerLabel.setText('')            
            self.ui.stage3Label.setStyleSheet(self.style.stage3_button_disable)
            self.ui.stage3Label.raise_()
            
        if raise_inners:
            # fix all picture, raise all small pics over background label,
            self.ui.stage3MinutesLabel.raise_()
            self.ui.stage3PowerLabel.raise_()
            self.ui.stage3SignalButton.raise_()
            self.ui.stage3FreqButton.raise_()

        # then raise transparent button
        self.ui.stage3Button.raise_()

        
    def SignalDisableAll(self):
        self.ui.triangularButton.setStyleSheet(self.style.triangular_90_disable)
        self.ui.squareButton.setStyleSheet(self.style.square_90_disable)
        self.ui.sinusoidalButton.setStyleSheet(self.style.sinusoidal_90_disable)


    def SignalChange (self):
        sender = self.sender()

        if sender.objectName() == 'triangularButton':
            self.SignalChangeTo('triangular')

        elif sender.objectName() == 'squareButton':
            self.SignalChangeTo('square')

        elif sender.objectName() == 'sinusoidalButton':
            self.SignalChangeTo('sinusoidal')

        self.ScreenSaverKick()

        
    def SignalChangeTo (self, new_signal):
        self.SignalDisableAll()
        
        if new_signal == 'triangular':
            self.ui.triangularButton.setStyleSheet(self.style.triangular_90_enable)

            if self.stage_selected == 'stage1':
                self.ui.stage1SignalButton.setStyleSheet(self.style.triangular_75_enable)
                self.stage1_info.SetStageSignal('triangular')
            elif self.stage_selected == 'stage2':
                self.ui.stage2SignalButton.setStyleSheet(self.style.triangular_75_enable)
                self.stage2_info.SetStageSignal('triangular')
            else:
                self.ui.stage3SignalButton.setStyleSheet(self.style.triangular_75_enable)
                self.stage3_info.SetStageSignal('triangular')

        elif new_signal == 'square':
            self.ui.squareButton.setStyleSheet(self.style.square_90_enable)

            if self.stage_selected == 'stage1':
                self.ui.stage1SignalButton.setStyleSheet(self.style.square_75_enable)
                self.stage1_info.SetStageSignal('square')
            elif self.stage_selected == 'stage2':
                self.ui.stage2SignalButton.setStyleSheet(self.style.square_75_enable)
                self.stage2_info.SetStageSignal('square')
            else:
                self.ui.stage3SignalButton.setStyleSheet(self.style.square_75_enable)
                self.stage3_info.SetStageSignal('square')            

        elif new_signal == 'sinusoidal':
            self.ui.sinusoidalButton.setStyleSheet(self.style.sinusoidal_90_enable)

            if self.stage_selected == 'stage1':
                self.ui.stage1SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
                self.stage1_info.SetStageSignal('sinusoidal')
            elif self.stage_selected == 'stage2':
                self.ui.stage2SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
                self.stage2_info.SetStageSignal('sinusoidal')
            else:
                self.ui.stage3SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
                self.stage3_info.SetStageSignal('sinusoidal')
        

    def FrequencyDisableAll(self):
        self.ui.freq1Button.setStyleSheet(self.style.freq1_90_disable)
        self.ui.freq2Button.setStyleSheet(self.style.freq2_90_disable)
        self.ui.freq3Button.setStyleSheet(self.style.freq3_90_disable)
        self.ui.freq4Button.setStyleSheet(self.style.freq4_90_disable)
        self.ui.freq5Button.setStyleSheet(self.style.freq5_90_disable)
        self.ui.freq6Button.setStyleSheet(self.style.freq6_90_disable)
        self.ui.freq7Button.setStyleSheet(self.style.freq7_90_disable)
        self.ui.freq8Button.setStyleSheet(self.style.freq8_90_disable)
        self.ui.freq9Button.setStyleSheet(self.style.freq9_90_disable)
        self.ui.freq10Button.setStyleSheet(self.style.freq10_90_disable)        


    def FrequencyChange (self):
        sender = self.sender()

        if sender.objectName() == 'freq1Button':
            self.FrequencyChangeTo('freq1')

        if sender.objectName() == 'freq2Button':
            self.FrequencyChangeTo('freq2')

        if sender.objectName() == 'freq3Button':
            self.FrequencyChangeTo('freq3')

        if sender.objectName() == 'freq4Button':
            self.FrequencyChangeTo('freq4')

        if sender.objectName() == 'freq5Button':
            self.FrequencyChangeTo('freq5')

        if sender.objectName() == 'freq6Button':
            self.FrequencyChangeTo('freq6')

        if sender.objectName() == 'freq7Button':
            self.FrequencyChangeTo('freq7')

        if sender.objectName() == 'freq8Button':
            self.FrequencyChangeTo('freq8')

        if sender.objectName() == 'freq9Button':
            self.FrequencyChangeTo('freq9')

        if sender.objectName() == 'freq10Button':
            self.FrequencyChangeTo('freq10')
            
        self.ScreenSaverKick()


    def FrequencyChangeTo (self, new_freq):
        self.FrequencyDisableAll()
        
        if new_freq == 'freq1':
            self.ui.freq1Button.setStyleSheet(self.style.freq1_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq1_75_enable)
                self.stage1_info.SetStageFrequency('0.98Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq1_75_enable)
                self.stage2_info.SetStageFrequency('0.98Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq1_75_enable)
                self.stage3_info.SetStageFrequency('0.98Hz')

        if new_freq == 'freq2':
            self.ui.freq2Button.setStyleSheet(self.style.freq2_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq2_75_enable)
                self.stage1_info.SetStageFrequency('1.96Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq2_75_enable)
                self.stage2_info.SetStageFrequency('1.96Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq2_75_enable)
                self.stage3_info.SetStageFrequency('1.96Hz')

        if new_freq == 'freq3':
            self.ui.freq3Button.setStyleSheet(self.style.freq3_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq3_75_enable)
                self.stage1_info.SetStageFrequency('3.92Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq3_75_enable)
                self.stage2_info.SetStageFrequency('3.92Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq3_75_enable)
                self.stage3_info.SetStageFrequency('3.92Hz')

        if new_freq == 'freq4':
            self.ui.freq4Button.setStyleSheet(self.style.freq4_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq4_75_enable)
                self.stage1_info.SetStageFrequency('7.83Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq4_75_enable)
                self.stage2_info.SetStageFrequency('7.83Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq4_75_enable)
                self.stage3_info.SetStageFrequency('7.83Hz')

        if new_freq == 'freq5':
            self.ui.freq5Button.setStyleSheet(self.style.freq5_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq5_75_enable)
                self.stage1_info.SetStageFrequency('11.79Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq5_75_enable)
                self.stage2_info.SetStageFrequency('11.79Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq5_75_enable)
                self.stage3_info.SetStageFrequency('11.79Hz')

        if new_freq == 'freq6':
            self.ui.freq6Button.setStyleSheet(self.style.freq6_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq6_75_enable)
                self.stage1_info.SetStageFrequency('16.67Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq6_75_enable)
                self.stage2_info.SetStageFrequency('16.67Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq6_75_enable)
                self.stage3_info.SetStageFrequency('16.67Hz')

        if new_freq == 'freq7':
            self.ui.freq7Button.setStyleSheet(self.style.freq7_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq7_75_enable)
                self.stage1_info.SetStageFrequency('23.58Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq7_75_enable)
                self.stage2_info.SetStageFrequency('23.58Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq7_75_enable)
                self.stage3_info.SetStageFrequency('23.58Hz')

        if new_freq == 'freq8':
            self.ui.freq8Button.setStyleSheet(self.style.freq8_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq8_75_enable)
                self.stage1_info.SetStageFrequency('30.80Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq8_75_enable)
                self.stage2_info.SetStageFrequency('30.80Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq8_75_enable)
                self.stage3_info.SetStageFrequency('30.80Hz')

        if new_freq == 'freq9':
            self.ui.freq9Button.setStyleSheet(self.style.freq9_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq9_75_enable)
                self.stage1_info.SetStageFrequency('62.64Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq9_75_enable)
                self.stage2_info.SetStageFrequency('62.64Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq9_75_enable)
                self.stage3_info.SetStageFrequency('62.64Hz')

        if new_freq == 'freq10':
            self.ui.freq10Button.setStyleSheet(self.style.freq10_90_enable)
            if self.stage_selected == 'stage1':
                self.ui.stage1FreqButton.setStyleSheet(self.style.freq10_75_enable)
                self.stage1_info.SetStageFrequency('86.22Hz')
            elif self.stage_selected == 'stage2':
                self.ui.stage2FreqButton.setStyleSheet(self.style.freq10_75_enable)
                self.stage2_info.SetStageFrequency('86.22Hz')
            else:
                self.ui.stage3FreqButton.setStyleSheet(self.style.freq10_75_enable)
                self.stage3_info.SetStageFrequency('86.22Hz')
            

    def UpPowerPressed (self):
        self.PwrUp (1)
        self.powerUpButtonCnt = 1
        # self.ScreenSaverKick()

    def UpPowerReleased (self):
        self.powerUpButtonCnt = 0

    def DwnPowerPressed (self):
        self.PwrDwn(1)
        self.powerDwnButtonCnt = 1
        # self.ScreenSaverKick()        

    def DwnPowerReleased (self):
        self.powerDwnButtonCnt = 0        

    def UpTimePressed (self):
        self.TimeUp (1)
        self.timeUpButtonCnt = 1
        # self.ScreenSaverKick()        

    def UpTimeReleased (self):
        self.timeUpButtonCnt = 0        

    def DwnTimePressed (self):
        self.TimeDwn(1)
        self.timeDwnButtonCnt = 1
        # self.ScreenSaverKick()

    def DwnTimeReleased (self):
        self.timeDwnButtonCnt = 0
    

    def PwrUp (self, new_pwr):
        last_pwr = int(self.ui.powerLabel.text())
        if (last_pwr + new_pwr) < 100:
            last_pwr += new_pwr
        else:
            last_pwr = 100

        self.ui.powerLabel.setText(str(last_pwr))
        self.StagesUpdateSelectedPower(last_pwr)

        
    def PwrDwn (self, new_pwr):
        last_pwr = int(self.ui.powerLabel.text())
        if (last_pwr - new_pwr) > 10:
            last_pwr -= new_pwr
        else:
            last_pwr = 10

        self.ui.powerLabel.setText(str(last_pwr))
        self.StagesUpdateSelectedPower(last_pwr)        

        
    def TimeUp (self, new_time):
        last_time = int(self.ui.minutesLabel.text())
        if ((last_time + new_time) < 120):
            last_time += new_time
        else:
            last_time = 120
            
        self.ui.minutesLabel.setText(str(last_time))
        self.StagesUpdateSelectedTime(last_time)

        
    def TimeDwn (self, new_time):
        last_time = int(self.ui.minutesLabel.text())
        if ((last_time - new_time) > 1):
            last_time -= new_time
        else:
            last_time = 1
            
        self.ui.minutesLabel.setText(str(last_time))
        self.StagesUpdateSelectedTime(last_time)        
    

    def StagesUpdateSelectedPower (self, new_pwr):
        if self.stage_selected == 'stage1':
            self.ui.stage1PowerLabel.setText(str(new_pwr)+'%')
            self.stage1_info.SetStagePower(new_pwr)
        elif self.stage_selected == 'stage2':
            self.ui.stage2PowerLabel.setText(str(new_pwr)+'%')
            self.stage2_info.SetStagePower(new_pwr)
        else:
            self.ui.stage3PowerLabel.setText(str(new_pwr)+'%')
            self.stage3_info.SetStagePower(new_pwr)

            
    def StagesUpdateSelectedTime (self, new_time):
        if self.stage_selected == 'stage1':
            self.ui.stage1MinutesLabel.setText(str(new_time)+"'")
            self.stage1_info.SetStageTimer(new_time)
        elif self.stage_selected == 'stage2':
            self.ui.stage2MinutesLabel.setText(str(new_time)+"'")
            self.stage2_info.SetStageTimer(new_time)
        else:
            self.ui.stage3MinutesLabel.setText(str(new_time)+"'")
            self.stage3_info.SetStageTimer(new_time)

            
    def StagesGetSelectedPower (self):
        if self.stage_selected == 'stage1':
            pwr_str = self.ui.stage1PowerLabel.text()
            pwr_str = pwr_str[:-1]
            pwr_save = int(pwr_str)
        elif self.stage_selected == 'stage2':
            pwr_str = self.ui.stage2PowerLabel.text()
            pwr_str = pwr_str[:-1]
            pwr_save = int(pwr_str)
        else:
            pwr_str = self.ui.stage3PowerLabel.text()
            pwr_str = pwr_str[:-1]
            pwr_save = int(pwr_str)

        return pwr_save

            
    def StagesGetSelectedTime (self):
        if self.stage_selected == 'stage1':
            time_str = self.ui.stage1MinutesLabel.text()
            time_str = time_str[:-1]
            time_save = int(time_str)
        elif self.stage_selected == 'stage2':
            time_str = self.ui.stage2MinutesLabel.text()
            time_str = time_str[:-1]
            time_save = int(time_str)
        else:
            time_str = self.ui.stage3MinutesLabel.text()
            time_str = time_str[:-1]
            time_save = int(time_str)

        return time_save
            
            
    def ScreenSaverKick (self):
        pass

    
    def ClearStage (self):
        if self.stage_selected == 'stage1':
            self.stage1_info.SetStageStatus('disable')
            self.Stage1GroupChange('disable')
        elif self.stage_selected == 'stage2':
            self.stage2_info.SetStageStatus('disable')
            self.Stage2GroupChange('disable')
        else:
            self.stage3_info.SetStageStatus('disable')
            self.Stage3GroupChange('disable')


    def BackStage (self):
        self.action = 'none'
        self.accept()
    

        
        
### end of file ###

