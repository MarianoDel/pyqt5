import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QColor, QIcon
from stages_class import Stages
from stylesheet_class import ButtonStyles

"""
        Test for StagesDialog

"""

#Here import the UIs or classes that got the UIs
from ui_magnet40 import Ui_Dialog


##############################
# Dialog Class - Main Window #
##############################
class Dialog(QDialog):

    #SIGNALS
    # rcv_signal = pyqtSignal(str)
    # one_second_signal = pyqtSignal()

    
    def __init__(self):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Class Startup Init
        ## Connect up the buttons.
        self.ui.stage1Button.clicked.connect(self.SelectStage)
        self.ui.stage2Button.clicked.connect(self.SelectStage)
        self.ui.stage3Button.clicked.connect(self.SelectStage)

        self.ui.startButton.clicked.connect(self.TreatmentScreen)
        self.ui.memManagerButton.clicked.connect(self.MemoryManagerScreen)

        self.ui.memaButton.pressed.connect(self.MemoryPressed)
        self.ui.memaButton.released.connect(self.MemoryReleased)
        self.ui.membButton.pressed.connect(self.MemoryPressed)
        self.ui.membButton.released.connect(self.MemoryReleased)
        self.ui.memcButton.pressed.connect(self.MemoryPressed)
        self.ui.memcButton.released.connect(self.MemoryReleased)
        self.ui.memdButton.pressed.connect(self.MemoryPressed)
        self.ui.memdButton.released.connect(self.MemoryReleased)

        self.style = ButtonStyles()

        self.stage1 = Stages()
        self.stage2 = Stages()
        self.stage3 = Stages()

        self.stage1.SetStageTimer(45)
        self.stage1.SetStagePower(85)
        self.stage1.SetStageSignal('triangular')
        self.stage1.SetStageFrequency('freq1')
        self.stage1.SetStageStatus('enable')

        self.stage2.SetStageTimer(55)
        self.stage2.SetStagePower(100)
        self.stage2.SetStageSignal('square')
        self.stage2.SetStageFrequency('freq9')
        self.stage2.SetStageStatus('enable')

        self.stage3.SetStageTimer(0)
        self.stage3.SetStagePower(0)
        self.stage3.SetStageSignal('none')
        self.stage3.SetStageFrequency('none')
        self.stage3.SetStageStatus('disable')

        self.Stage1GroupChange(self.stage1.GetStageStatus())
        self.Stage2GroupChange(self.stage2.GetStageStatus())
        self.Stage3GroupChange(self.stage3.GetStageStatus())

        self.UpdateTotalTime()

        self.MemoryUpdate('mema', ['Arm and Leg Inflammatory', "45' T 85% 7.83Hz", '', ''])
        self.MemoryUpdate('memb', ['Arm and Leg Inflammatory', "45' T 85% 7.83Hz", '', ''])
        self.MemoryUpdate('memc', ['Arm and Leg Inflammatory', "45' T 85% 7.83Hz", '', ''])
        self.MemoryUpdate('memd', ['Arm and Leg Inflammatory', "45' T 85% 7.83Hz", '', ''])
        self.MemoryButtonStatus('mema', 'enable')
        self.MemoryButtonStatus('memb', 'disable')
        self.MemoryButtonStatus('memc', 'disable')
        self.MemoryButtonStatus('memd', 'enable')

        self.ui.textEdit.setText('')
        self.InsertColorText("No serial port found!!!", 'blue')
        self.InsertLocalText("Serial port open OK!")
        self.InsertForeingText("No serial port found!!!")

        self.AntennaButtonsUpdate (['enable', 'dis', 'dis', 'dis'], ['CH1\nTunnel 10"', '', '', ''])

        
    def SelectStage (self):
        sender = self.sender()

        if sender.objectName() == 'stage1Button':
            print('Stage 1 selected for config')

        if sender.objectName() == 'stage2Button':
            print('Stage 2 selected for config')
            
        if sender.objectName() == 'stage3Button':
            print('Stage 3 selected for config')


    def Stage1GroupChange (self, change_to):
        raise_inners = False
        
        if change_to == 'enable':
            self.ui.stage1MinutesLabel.setText(str(self.stage1.GetStageTimer())+"'")
            self.ui.stage1PowerLabel.setText(str(self.stage1.GetStagePower())+"%")
            self.ui.stage1Label.setStyleSheet(self.style.stage1_button_enable)
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
            self.ui.stage2MinutesLabel.setText(str(self.stage2.GetStageTimer())+"'")
            self.ui.stage2PowerLabel.setText(str(self.stage2.GetStagePower())+"%")
            self.ui.stage2Label.setStyleSheet(self.style.stage2_button_enable)
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
            self.ui.stage3MinutesLabel.setText(str(self.stage3.GetStageTimer())+"'")
            self.ui.stage3PowerLabel.setText(str(self.stage3.GetStagePower())+"%")
            self.ui.stage3Label.setStyleSheet(self.style.stage3_button_enable)
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
        

    def UpdateTotalTime (self):
        total_time = 0
        if self.stage1.GetStageStatus() == 'enable':
            total_time += self.stage1.GetStageTimer()

        if self.stage2.GetStageStatus() == 'enable':
            total_time += self.stage2.GetStageTimer()

        if self.stage3.GetStageStatus() == 'enable':
            total_time += self.stage3.GetStageTimer()

        self.ui.totalMinutesLabel.setText(str(total_time))


    def MemoryUpdate (self, mem, str_lst):
        if mem == 'mema':
            self.ui.memaDescLabel.setText(str_lst[0])
            self.ui.memaOneLabel.setText('1 - ' + str_lst[1])
            self.ui.memaTwoLabel.setText('2 - ' + str_lst[2])
            self.ui.memaThreeLabel.setText('3 - ' + str_lst[3])            

        if mem == 'memb':
            self.ui.membDescLabel.setText(str_lst[0])
            self.ui.membOneLabel.setText('1 - ' + str_lst[1])
            self.ui.membTwoLabel.setText('2 - ' + str_lst[2])
            self.ui.membThreeLabel.setText('3 - ' + str_lst[3])            

        if mem == 'memc':
            self.ui.memcDescLabel.setText(str_lst[0])
            self.ui.memcOneLabel.setText('1 - ' + str_lst[1])
            self.ui.memcTwoLabel.setText('2 - ' + str_lst[2])
            self.ui.memcThreeLabel.setText('3 - ' + str_lst[3])            

        if mem == 'memd':
            self.ui.memdDescLabel.setText(str_lst[0])
            self.ui.memdOneLabel.setText('1 - ' + str_lst[1])
            self.ui.memdTwoLabel.setText('2 - ' + str_lst[2])
            self.ui.memdThreeLabel.setText('3 - ' + str_lst[3])            

            
    def MemoryButtonStatus (self, mem, status):
        if mem == 'mema':
            if status == 'enable':
                self.ui.memaButton.setStyleSheet(self.style.mem_90_button_enable)
            else:
                self.ui.memaButton.setStyleSheet(self.style.mem_90_button_disable)

        if mem == 'memb':
            if status == 'enable':
                self.ui.membButton.setStyleSheet(self.style.mem_90_button_enable)
            else:
                self.ui.membButton.setStyleSheet(self.style.mem_90_button_disable)

        if mem == 'memc':
            if status == 'enable':
                self.ui.memcButton.setStyleSheet(self.style.mem_90_button_enable)
            else:
                self.ui.memcButton.setStyleSheet(self.style.mem_90_button_disable)

        if mem == 'memd':
            if status == 'enable':
                self.ui.memdButton.setStyleSheet(self.style.mem_90_button_enable)
            else:
                self.ui.memdButton.setStyleSheet(self.style.mem_90_button_disable)


    def AntennaProcessInnerName (self, ant_str):
        ant_name = ''
        list_cntr = 0
        ant_list = ant_str.split(' ')
        for inner in ant_list:
            if list_cntr < 3:
                if len(inner) < 8:
                    ant_name += inner + '\n'
                    list_cntr += 1

        if len(ant_name) > 1:
            ant_name = ant_name[:-1]

        return ant_name
            
            
    def AntennaProcessName (self, channel):
        ant_name = 'unknow'
        ant_ch = '1'
        
        if channel == 'ch1':
            ant_name = self.AntennaProcessInnerName(self.antennas_connected.name_ch1)
            ant_ch = '1'

        if channel == 'ch2':
            ant_name = self.AntennaProcessInnerName(self.antennas_connected.name_ch2)
            ant_ch = '2'            

        if channel == 'ch3':
            ant_name = self.AntennaProcessInnerName(self.antennas_connected.name_ch3)
            ant_ch = '3'            

        if channel == 'ch4':
            ant_name = self.AntennaProcessInnerName(self.antennas_connected.name_ch4)
            ant_ch = '4'            
            
        if ant_name != 'unknow':
            ant_str = 'CH' + ant_ch + '\n' + ant_name
        else:
            ant_str = 'CH' + ant_ch + '\n' + \
                      'R: ' + self.antennas_connected.GetRString(channel) + '\n' + \
                      'L: ' + self.antennas_connected.GetLString(channel) + '\n' + \
                      'I: ' + self.antennas_connected.GetIString(channel) + '\n'

        return ant_str

    
    def AntennaUpdate (self):
        self.antennatimeout_finish = True
        
        if self.antennas_connected.GetActive('ch1') == True:
            self.ui.ch1Button.setStyleSheet(self.style.ch_enable)
            ant_str = self.AntennaProcessName('ch1')
            self.ui.ch1Button.setText(ant_str)
        else:
            self.ui.ch1Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch1Button.setText("CH1")

        if self.antennas_connected.GetActive('ch2') == True:
            self.ui.ch2Button.setStyleSheet(self.style.ch_enable)
            ant_str = self.AntennaProcessName('ch2')
            self.ui.ch2Button.setText(ant_str)
        else:
            self.ui.ch2Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch2Button.setText("CH2")

        if self.antennas_connected.GetActive('ch3') == True:
            self.ui.ch3Button.setStyleSheet(self.style.ch_enable)
            ant_str = self.AntennaProcessName('ch3')
            self.ui.ch3Button.setText(ant_str)
        else:
            self.ui.ch3Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch3Button.setText("CH3")

        if self.antennas_connected.GetActive('ch4') == True:
            self.ui.ch4Button.setStyleSheet(self.style.ch_enable)
            ant_str = self.AntennaProcessName('ch4')
            self.ui.ch4Button.setText(ant_str)
        else:
            self.ui.ch4Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch4Button.setText("CH4")


    def AntennaButtonsUpdate (self, status_lst, names_lst):        
        if status_lst[0] == 'enable':
            self.ui.ch1Button.setStyleSheet(self.style.ch_enable)
            self.ui.ch1Button.setText(names_lst[0])
        else:
            self.ui.ch1Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch1Button.setText("CH1")

        if status_lst[1] == 'enable':
            self.ui.ch2Button.setStyleSheet(self.style.ch_enable)
            self.ui.ch2Button.setText(names_lst[1])
        else:
            self.ui.ch2Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch2Button.setText("CH2")

        if status_lst[2] == 'enable':
            self.ui.ch3Button.setStyleSheet(self.style.ch_enable)
            self.ui.ch3Button.setText(names_lst[2])
        else:
            self.ui.ch3Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch3Button.setText("CH3")

        if status_lst[3] == 'enable':
            self.ui.ch4Button.setStyleSheet(self.style.ch_enable)
            self.ui.ch4Button.setText(names_lst[3])
        else:
            self.ui.ch4Button.setStyleSheet(self.style.ch_disable)
            self.ui.ch4Button.setText("CH4")
            

    def InsertColorText (self, new_text, color='red', plain=False):
        if color == 'red':
            # self.ui.textEdit.setTextColor(QColor(255, 0, 0))
            self.ui.textEdit.setTextColor(QColor(237, 50, 55))            

        if color == 'blue':
            # self.ui.textEdit.setTextColor(QColor(0, 0, 255))
            self.ui.textEdit.setTextColor(QColor(62, 64, 149))

        if color == 'green':
            # self.ui.textEdit.setTextColor(QColor(0, 255, 0))
            self.ui.textEdit.setTextColor(QColor(0, 168, 89))

        if plain:
            self.ui.textEdit.insertPlainText(new_text)
        else:
            self.ui.textEdit.append(new_text)

            
    def InsertLocalText (self, new_text):
        self.InsertColorText(new_text, 'red')

        
    def InsertInfoText (self, new_text):
        self.InsertColorText(new_text, 'blue')
        

    def InsertLocalTextNoNewLine (self, new_text):
        self.InsertColorText(new_text, 'red', True)
        
        
    def InsertForeingText (self, new_text):
        self.InsertColorText(new_text, 'green')

        
    def InsertForeingTextNoNewLine (self, new_text):
        self.InsertColorText(new_text, 'green', True)


    def MemoryPressed (self):
        sender = self.sender()

        if sender.objectName() == 'memaButton':
            self.memaButtonCnt = 1

        if sender.objectName() == 'membButton':
            self.membButtonCnt = 1

        if sender.objectName() == 'memcButton':
            self.memcButtonCnt = 1

        if sender.objectName() == 'memdButton':
            self.memdButtonCnt = 1
            
        self.ScreenSaverKick()

        
    def MemoryReleased (self):
        sender = self.sender()

        if sender.objectName() == 'memaButton':
            if (self.memaButtonCnt > 0 and
                self.memaButtonCnt < 3):
                self.memaButtonCnt = 0
            
                #get memory values
                if self.t.mem1_treat_time == 'None':
                    self.InsertInfoText("Not much to do with memory!")
                else:
                    self.MemoryToCurrentConf('mema')
                    self.CheckForStart()


        if sender.objectName() == 'membButton':
            self.membButtonCnt = 1

        if sender.objectName() == 'memcButton':
            self.memcButtonCnt = 1

        if sender.objectName() == 'memdButton':
            self.memdButtonCnt = 1


    def MemoryToCurrentConf (self, mem_slot):
        if mem_slot == 'mema':
            timer1 = self.t.mema_signal
            power1 = self.t.mema_power
            signal1 = self.t.mema_signal
            freq1 = self.t.mema_frequency
            status1 = self.t.mema_status

            timer2 = self.t.mema_signal
            power2 = self.t.mema_power
            signal2 = self.t.mema_signal
            freq2 = self.t.mema_frequency
            status2 = self.t.mema_status
            
            timer3 = self.t.mema_signal
            power3 = self.t.mema_power
            signal3 = self.t.mema_signal
            freq3 = self.t.mema_frequency
            status3 = self.t.mema_status
            
        elif mem_slot == 'memb':
            timer = self.t.memb_signal
            power = self.t.memb_power
            signal = self.t.memb_signal
            freq = self.t.memb_frequency
            status = self.t.memb_status
        elif mem_slot == 'memc':
            timer = self.t.memc_signal
            power = self.t.memc_power
            signal = self.t.memc_signal
            freq = self.t.memc_frequency
            status = self.t.memc_status
        elif mem_slot == 'memd':
            timer = self.t.memd_signal
            power = self.t.memd_power
            signal = self.t.memd_signal
            freq = self.t.memd_frequency
            status = self.t.memd_status
        else:
            return
            
        
            
        self.stage1.SetStageTimer(45)
        self.stage1.SetStagePower(85)
        self.stage1.SetStageSignal('triangular')
        self.stage1.SetStageFrequency('freq1')
        self.stage1.SetStageStatus('enable')

        self.stage2.SetStageTimer(55)
        self.stage2.SetStagePower(100)
        self.stage2.SetStageSignal('square')
        self.stage2.SetStageFrequency('freq9')
        self.stage2.SetStageStatus('enable')

        self.stage3.SetStageTimer(0)
        self.stage3.SetStagePower(0)
        self.stage3.SetStageSignal('none')
        self.stage3.SetStageFrequency('none')
        self.stage3.SetStageStatus('disable')

        self.SignalChangeTo(self.t.mem1_signal)
        self.FrequencyChangeTo(self.t.mem1_frequency)
        self.ui.minutesLabel.setText(self.t.mem1_treat_time)
        self.t.SetTreatmentTimer(int(self.t.mem1_treat_time))
        self.ui.powerLabel.setText(self.t.mem1_power)
        self.t.SetPower(int(self.t.mem1_power))


    def Memory1Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem1')
        else:
            self.InsertLocalText("Select all parameters first!")
        
    ################################
    # Other Screens Calls are here #
    ################################

    def TreatmentScreen (self):
        print("TreatmentScreen called!")

        
    def MemoryManagerScreen (self):
        print("MemoryManagerScreen called!")
        
    
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
w = Dialog()
# w.setWindowFlags(Qt.CustomizeWindowHint)
# w.setWindowFlags(Qt.FramelessWindowHint)
print('Starting magnet app...')
w.show()
sys.exit(app.exec_())

### End of File ###
