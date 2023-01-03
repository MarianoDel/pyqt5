from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QColor, QIcon
from stages_class import Stages
from stylesheet_class import ButtonStyles
from treatment_class import Treatment


#Here import the UIs or classes that got the UIs
from ui_magnet40 import Ui_Dialog



##############################
# Dialog Class - Main Window #
##############################
class Dialog(QDialog):

    #SIGNALS
    # rcv_signal = pyqtSignal(str)
    # one_second_signal = pyqtSignal()

    
    def __init__(self, debug_bool):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Class Startup Init
        ## backup received data
        self.debug_bool = debug_bool
        
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

        self.ui_label_dict = {
            "mema" : [self.ui.memaDescLabel, self.ui.memaOneLabel, self.ui.memaTwoLabel, self.ui.memaThreeLabel],
            "memb" : [self.ui.membDescLabel, self.ui.membOneLabel, self.ui.membTwoLabel, self.ui.membThreeLabel],
            "memc" : [self.ui.memcDescLabel, self.ui.memcOneLabel, self.ui.memcTwoLabel, self.ui.memcThreeLabel],
            "memd" : [self.ui.memdDescLabel, self.ui.memdOneLabel, self.ui.memdTwoLabel, self.ui.memdThreeLabel]
            }

        self.ui_button_dict = {
            "mema" : self.ui.memaButton,
            "memb" : self.ui.membButton,
            "memc" : self.ui.memcButton,
            "memd" : self.ui.memdButton
            }


        ## set styles
        self.label_orig = "color: rgb(55, 52, 53);"

        self.label_disable = "color: rgb(230, 231, 232);"        

        self.mem_button_enable = "background-color: rgb(221, 234, 224);\
                                  border-radius: 20px;\
                                  border:3px solid rgb(55, 52, 53);\
                                  color: rgb(55, 52, 53);"

        self.mem_button_disable = "background-color: rgb(245, 245, 245);\
                                   border-radius: 20px;\
                                   border:3px solid rgb(230, 231, 232);\
                                   color: rgb(230,231,232);"
        
        self.style = ButtonStyles()
        self.t = Treatment()

        self.t.stage1_info = Stages()
        self.t.stage2_info = Stages()
        self.t.stage3_info = Stages()

        self.stage1 = self.t.stage1_info
        self.stage2 = self.t.stage2_info
        self.stage3 = self.t.stage3_info
        
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

        # get memory buttons config        
        # self.MemoryUpdate('mema', [self.t.mema_description,\
        #                            self.t.mema_first_str,\
        #                            self.t.mema_second_str,\
        #                            self.t.mema_third_str])

        # self.MemoryUpdate('memb', [self.t.memb_description,\
        #                            self.t.memb_first_str,\
        #                            self.t.memb_second_str,\
        #                            self.t.memb_third_str])

        # self.MemoryUpdate('memc', [self.t.memc_description,\
        #                            self.t.memc_first_str,\
        #                            self.t.memc_second_str,\
        #                            self.t.memc_third_str])

        # self.MemoryUpdate('memd', [self.t.memd_description,\
        #                            self.t.memd_first_str,\
        #                            self.t.memd_second_str,\
        #                            self.t.memd_third_str])
        
        # self.MemoryButtonStatus('mema', self.t.mema_status)
        # self.MemoryButtonStatus('memb', self.t.memb_status)
        # self.MemoryButtonStatus('memc', self.t.memc_status)
        # self.MemoryButtonStatus('memd', self.t.memd_status)

        self.PopullateFromDict(self.t.mem_instant_dict)

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
            # small buttons change
            self.Stage1InnerSignalChange(self.stage1.GetStageSignal())
            self.Stage1InnerFreqChange(self.stage1.GetStageFrequency())        
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
            # small buttons change
            self.Stage2InnerSignalChange(self.stage2.GetStageSignal())
            self.Stage2InnerFreqChange(self.stage2.GetStageFrequency())        
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
            # small buttons change
            self.Stage3InnerSignalChange(self.stage3.GetStageSignal())
            self.Stage3InnerFreqChange(self.stage3.GetStageFrequency())        
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
        

    def Stage1InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage1SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage1SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage1SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            # todo: go transparent here
            self.ui.stage1SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)


    def Stage2InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage2SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage2SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage2SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            # todo: go transparent here
            self.ui.stage2SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)


    def Stage3InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage3SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage3SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage3SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            # todo: go transparent here
            self.ui.stage3SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
            
            
    def Stage1InnerFreqChange (self, new_freq):
        if new_freq == 'freq1':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq1_75_enable)
        elif new_freq == 'freq2':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq2_75_enable)
        elif new_freq == 'freq3':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq3_75_enable)
        elif new_freq == 'freq4':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq4_75_enable)
        elif new_freq == 'freq5':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq5_75_enable)
        elif new_freq == 'freq6':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq6_75_enable)
        elif new_freq == 'freq7':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq7_75_enable)
        elif new_freq == 'freq8':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq8_75_enable)
        elif new_freq == 'freq9':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq9_75_enable)
        elif new_freq == 'freq10':
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq10_75_enable)
        else:
            # todo: go transparent here
            self.ui.stage1FreqButton.setStyleSheet(self.style.freq10_75_enable)


    def Stage2InnerFreqChange (self, new_freq):
        if new_freq == 'freq1':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq1_75_enable)
        elif new_freq == 'freq2':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq2_75_enable)
        elif new_freq == 'freq3':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq3_75_enable)
        elif new_freq == 'freq4':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq4_75_enable)
        elif new_freq == 'freq5':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq5_75_enable)
        elif new_freq == 'freq6':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq6_75_enable)
        elif new_freq == 'freq7':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq7_75_enable)
        elif new_freq == 'freq8':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq8_75_enable)
        elif new_freq == 'freq9':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq9_75_enable)
        elif new_freq == 'freq10':
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq10_75_enable)
        else:
            # todo: go transparent here
            self.ui.stage2FreqButton.setStyleSheet(self.style.freq10_75_enable)


    def Stage3InnerFreqChange (self, new_freq):
        if new_freq == 'freq1':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq1_75_enable)
        elif new_freq == 'freq2':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq2_75_enable)
        elif new_freq == 'freq3':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq3_75_enable)
        elif new_freq == 'freq4':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq4_75_enable)
        elif new_freq == 'freq5':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq5_75_enable)
        elif new_freq == 'freq6':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq6_75_enable)
        elif new_freq == 'freq7':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq7_75_enable)
        elif new_freq == 'freq8':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq8_75_enable)
        elif new_freq == 'freq9':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq9_75_enable)
        elif new_freq == 'freq10':
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq10_75_enable)
        else:
            # todo: go transparent here
            self.ui.stage3FreqButton.setStyleSheet(self.style.freq10_75_enable)
            

        
    def UpdateTotalTime (self):
        total_time = 0
        if self.stage1.GetStageStatus() == 'enable':
            total_time += self.stage1.GetStageTimer()

        if self.stage2.GetStageStatus() == 'enable':
            total_time += self.stage2.GetStageTimer()

        if self.stage3.GetStageStatus() == 'enable':
            total_time += self.stage3.GetStageTimer()

        self.ui.totalMinutesLabel.setText(str(total_time))


    def PopullateFromDict (self, m_dict):
        for x in m_dict:
            mem_lst = m_dict[x]
            ui_label_lst = self.ui_label_dict[x]
            ui_button = self.ui_button_dict[x]

            ui_label_lst[0].setText(mem_lst[0])
            ui_label_lst[1].setText('1 - ' + mem_lst[1])
            ui_label_lst[2].setText('2 - ' + mem_lst[2])
            ui_label_lst[3].setText('3 - ' + mem_lst[3])
                
            if mem_lst[1] == '' and mem_lst[2] == '' and mem_lst[3] == '':
                ui_label_lst[0].setStyleSheet(self.label_disable)
                ui_label_lst[1].setStyleSheet(self.label_disable)
                ui_label_lst[2].setStyleSheet(self.label_disable)
                ui_label_lst[3].setStyleSheet(self.label_disable)
                ui_button.setStyleSheet(self.mem_button_disable)
            else:
                ui_label_lst[0].setStyleSheet(self.label_orig)
                ui_label_lst[1].setStyleSheet(self.label_orig)
                ui_label_lst[2].setStyleSheet(self.label_orig)
                ui_label_lst[3].setStyleSheet(self.label_orig)
                ui_button.setStyleSheet(self.mem_button_enable)

                
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
            
        # self.ScreenSaverKick()

        
    def MemoryReleased (self):
        sender = self.sender()

        print ('before mem modification')
        print (self.stage1)
        if sender.objectName() == 'memaButton':
            if (self.memaButtonCnt > 0 and
                self.memaButtonCnt < 3):
                self.memaButtonCnt = 0
            
                #get memory values
                if self.t.mema_status != 'enable':
                    self.InsertInfoText("Not much to do with memory!")
                else:
                    self.MemoryToCurrentConf('mema')
                    self.Stage1GroupChange(self.stage1.GetStageStatus())
                    self.Stage2GroupChange(self.stage2.GetStageStatus())
                    self.Stage3GroupChange(self.stage3.GetStageStatus())
                    self.UpdateTotalTime()
                    # self.CheckForStart()

            print ('in mema already modif')
            print (self.stage1)
            print (self.stage2)
            print (self.stage3)            

        if sender.objectName() == 'membButton':
            if (self.membButtonCnt > 0 and
                self.membButtonCnt < 3):
                self.membButtonCnt = 0
            
                #get memory values
                if self.t.memb_status != 'enable':
                    self.InsertInfoText("Not much to do with memory!")
                else:
                    self.MemoryToCurrentConf('memb')
                    self.Stage1GroupChange(self.stage1.GetStageStatus())
                    self.Stage2GroupChange(self.stage2.GetStageStatus())
                    self.Stage3GroupChange(self.stage3.GetStageStatus())
                    self.UpdateTotalTime()
                    # self.CheckForStart()

            print ('in memb already modif')
            print (self.stage1)
            print (self.stage2)
            print (self.stage3)            

        if sender.objectName() == 'memcButton':
            if (self.memcButtonCnt > 0 and
                self.memcButtonCnt < 3):
                self.memcButtonCnt = 0
            
                #get memory values
                if self.t.memc_status != 'enable':
                    self.InsertInfoText("Not much to do with memory!")
                else:
                    self.MemoryToCurrentConf('memc')
                    self.Stage1GroupChange(self.stage1.GetStageStatus())
                    self.Stage2GroupChange(self.stage2.GetStageStatus())
                    self.Stage3GroupChange(self.stage3.GetStageStatus())
                    self.UpdateTotalTime()
                    # self.CheckForStart()

            print ('in memc already modif')
            print (self.stage1)

        if sender.objectName() == 'memdButton':
            if (self.memdButtonCnt > 0 and
                self.memdButtonCnt < 3):
                self.memdButtonCnt = 0
            
                #get memory values
                if self.t.memd_status != 'enable':
                    self.InsertInfoText("Not much to do with memory!")
                else:
                    self.MemoryToCurrentConf('memd')
                    self.Stage1GroupChange(self.stage1.GetStageStatus())
                    self.Stage2GroupChange(self.stage2.GetStageStatus())
                    self.Stage3GroupChange(self.stage3.GetStageStatus())
                    self.UpdateTotalTime()
                    # self.CheckForStart()

            print ('in memd already modif')
            print (self.stage1)


    def MemoryToCurrentConf (self, mem_slot):
        if mem_slot == 'mema':
            stage1_str = self.t.mema_first_str
            stage2_str = self.t.mema_second_str
            stage3_str = self.t.mema_third_str
        elif mem_slot == 'memb':
            stage1_str = self.t.memb_first_str
            stage2_str = self.t.memb_second_str
            stage3_str = self.t.memb_third_str
        elif mem_slot == 'memc':
            stage1_str = self.t.memc_first_str
            stage2_str = self.t.memc_second_str
            stage3_str = self.t.memc_third_str
        elif mem_slot == 'memd':
            stage1_str = self.t.memd_first_str
            stage2_str = self.t.memd_second_str
            stage3_str = self.t.memd_third_str
        else:
            return
            
        (time, signal, power, freq, status) = self.MemoryStringParse(stage1_str)
        if status == 'enable':
            self.stage1.SetStageStatus('enable')
            self.stage1.SetStageTimer(int(time))
            self.stage1.SetStageSignal(signal)
            self.stage1.SetStagePower(int(power))
            freq_index_str = self.stage1.StageFreqValueToIndex(freq)
            self.stage1.SetStageFrequency(freq_index_str)
        else:
            self.stage1.SetStageStatus('disable')

        (time, signal, power, freq, status) = self.MemoryStringParse(stage2_str)
        if status == 'enable':
            self.stage2.SetStageStatus('enable')
            self.stage2.SetStageTimer(int(time))
            self.stage2.SetStageSignal(signal)
            self.stage2.SetStagePower(int(power))
            freq_index_str = self.stage2.StageFreqValueToIndex(freq)
            self.stage2.SetStageFrequency(freq_index_str)
        else:
            self.stage2.SetStageStatus('disable')

        (time, signal, power, freq, status) = self.MemoryStringParse(stage3_str)
        if status == 'enable':
            self.stage3.SetStageStatus('enable')            
            self.stage3.SetStageTimer(int(time))
            self.stage3.SetStageSignal(signal)
            self.stage3.SetStagePower(int(power))
            freq_index_str = self.stage3.StageFreqValueToIndex(freq)
            self.stage3.SetStageFrequency(freq_index_str)
        else:
            self.stage3.SetStageStatus('disable')
            

    def MemoryStringParse (self, mem_str):
        if mem_str == '':
            return ('','','','','disable')

        memory_str = mem_str.split(' ')
        time_str = memory_str[0]
        time_str = time_str[:-1]

        power_str = memory_str[2]
        power_str = power_str[:-1]

        frequency_str = memory_str[3]

        stage_utils = Stages()
        signal_str = stage_utils.StageCharToSignal(memory_str[1])

        return (time_str, signal_str, power_str, frequency_str, 'enable')
        

    def Memory1Config (self):
        if self.CheckCompleteConf() == True:
            self.MemoryScreen('mem1')
        else:
            self.InsertLocalText("Select all parameters first!")

            
    ################################
    # Other Screens Calls are here #
    ################################

    def TreatmentScreen (self):
        if self.debug_bool:
            print("TreatmentScreen called!")
        else:
            print("call the dialog here!!!!")

        
    def MemoryManagerScreen (self):
        if self.debug_bool:
            print("MemoryManagerScreen called!")
        else:
            print("call the dialog here!!!!")
        
    
### End of Dialog ###
### End of File ###
