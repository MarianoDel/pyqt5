from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from stages_class import Stages
from stylesheet_class import ButtonStyles
from treatment_class import Treatment
from antenna_class import AntennaInTreatment
from datetime import datetime
import copy


#Here import the UIs or classes that got the UIs
from ui_magnet40 import Ui_Dialog
from dlg_treat_cls import TreatmentDialog
from dlg_mem_manager_cls import MemManagerDialog
from dlg_stages_cls import StagesDialog
from diagnostics_cls import DiagnosticsDialog
from screen_saver_cls import ScreenSaverDialog
from wifi_enable_cls import WiFiDialog
from dlg_mems_cls import MemoryDialog

#get the code for manager
from wifi_thread_manager import WiFiThreadManager


##############################
# Dialog Class - Main Window #
##############################
class Dialog(QDialog):

    #SIGNALS
    one_second_signal = pyqtSignal()
    
    def __init__(self, debug_bool, ser_instance, treat_instance, parent=None):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Class Startup Init
        ## backup received data
        self.debug_bool = debug_bool
        self.s = ser_instance
        self.parent = parent
        if self.debug_bool:
            self.t = Treatment()
        else:
            self.t = treat_instance
        
        ## Connect up the buttons.
        self.ui.stage1Button.clicked.connect(self.StagesConfScreen)
        self.ui.stage2Button.clicked.connect(self.StagesConfScreen)
        self.ui.stage3Button.clicked.connect(self.StagesConfScreen)

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

        self.ui.ch1Button.clicked.connect(self.AntennaNameChange)
        # self.ui.ch2Button.clicked.connect(self.ChannelChange)    #for tests
        self.ui.ch2Button.clicked.connect(self.AntennaNameChange)
        self.ui.ch3Button.clicked.connect(self.AntennaNameChange)
        self.ui.ch4Button.clicked.connect(self.AntennaNameChange)

        self.ui.diagButton.pressed.connect(self.DiagsPressed)
        self.ui.diagButton.released.connect(self.DiagsReleased)

        # connect wifi button
        self.ui.wifiButton.clicked.connect(self.WifiScreen)
        
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

        self.start_enable = "background-image: url(:/buttons/resources/Play.png);\
                             background-color: rgb(0, 168, 89);\
                             background-repeat:no-repeat;\
                             background-position: center center;\
                             border-radius: 20px;\
                             border:3px solid rgb(55, 52, 53);"

        self.start_disable = "background-image: url(:/buttons/resources/Play.png);\
                              background-color: rgb(245, 245, 245);\
                              background-repeat:no-repeat;\
                              background-position: center center;\
                              border-radius: 20px;\
                              border:3px solid rgb(230, 231, 232);"
        
        self.style = ButtonStyles()

        # do not backup current stages info on treatment instance
        # self.t.stage1_info = Stages()
        # self.t.stage2_info = Stages()
        # self.t.stage3_info = Stages()
        # self.stage1 = self.t.stage1_info
        # self.stage2 = self.t.stage2_info
        # self.stage3 = self.t.stage3_info

        # current stages info
        self.stage1 = Stages()
        self.stage2 = Stages()
        self.stage3 = Stages()        
        # default stages config
        self.stage1.SetStageTimer(30)
        self.stage1.SetStagePower(70)
        self.stage1.SetStageSignal('sinusoidal')
        self.stage1.SetStageFrequency('freq4')
        self.stage1.SetStageStatus('enable')

        self.stage2.SetStageTimer(0)
        self.stage2.SetStagePower(0)
        self.stage2.SetStageSignal('')
        self.stage2.SetStageFrequency('')
        self.stage2.SetStageStatus('disable')

        self.stage3.SetStageTimer(0)
        self.stage3.SetStagePower(0)
        self.stage3.SetStageSignal('none')
        self.stage3.SetStageFrequency('none')
        self.stage3.SetStageStatus('disable')

        self.Stage1GroupChange(self.stage1.GetStageStatus())
        self.Stage2GroupChange(self.stage2.GetStageStatus())
        self.Stage3GroupChange(self.stage3.GetStageStatus())

        self.UpdateTotalTime()

        # CONNECT SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)

        ## to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        ## Memory things and timed counters
        self.lastButtonChecked = ''
        self.memButtonCnt = 0
        self.diagButtonCnt = 0
        self.PopullateFromDict(self.t.mem_instant_dict)

        ## Activity Information
        self.ui.textEdit.setText('')
        if self.s.port_open:
            self.InsertInfoText('Serial Port Open: OK')
            self.InsertInfoText('')
            self.InsertInfoTextNoNewLine('Communication with power: ')
            self.s.Write('keepalive\r\n')
        else:
            self.InsertInfoText('Serial Port Not Found!!!')

        ### Ask for know antennas
        if self.s.port_open == True:
            self.s.Write('get_antenna,\r\n')

        ## Init Antennas connected
        self.antennas_connected = AntennaInTreatment()

        # screen saver timer activation
        # self.timer_screensaver = 10      
        self.timer_screensaver = self.t.timeout_screensaver
        self.screensaver_window = True
        
        ## setup antennas icons
        ## url(:/buttons/resources/Stop.png)
        self.wifi_act_Icon = QIcon(':/buttons/resources/wifi-symbol_act.png')
        self.wifi_err_Icon = QIcon(':/buttons/resources/wifi-symbol_err.png')
        self.wifi_disa_Icon = QIcon(':/buttons/resources/wifi-symbol_disa.png')
        self.wifi_emit_Icon = QIcon(':/buttons/resources/wifi-symbol_emit.png')

        # start manager background process
        self.wifi_manager_cnt = 2
        self.MyThread = WiFiThreadManager()
        self.MyThread.start()
            
        ## activate the 1 second timer it is repetitive
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        ## instanciate the antennas timer timeout
        self.antennatimeout = QTimer()
        self.antennatimeout_finish = True
            
        
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
            # small buttons change
            self.Stage1InnerSignalChange('disable')
            self.Stage1InnerFreqChange('disable')
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
            # small buttons change
            self.Stage2InnerSignalChange('disable')
            self.Stage2InnerFreqChange('disable')
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
            # small buttons change
            self.Stage3InnerSignalChange('disable')
            self.Stage3InnerFreqChange('disable')
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
            self.ui.stage1SignalButton.setStyleSheet(self.style.signal_75_disable)


    def Stage2InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage2SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage2SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage2SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            self.ui.stage2SignalButton.setStyleSheet(self.style.signal_75_disable)


    def Stage3InnerSignalChange (self, new_signal):
        if new_signal == 'triangular':
            self.ui.stage3SignalButton.setStyleSheet(self.style.triangular_75_enable)
        elif new_signal == 'square':
            self.ui.stage3SignalButton.setStyleSheet(self.style.square_75_enable)
        elif new_signal == 'sinusoidal':
            self.ui.stage3SignalButton.setStyleSheet(self.style.sinusoidal_75_enable)
        else:
            self.ui.stage3SignalButton.setStyleSheet(self.style.signal_75_disable)
            
            
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
            self.ui.stage1FreqButton.setStyleSheet(self.style.signal_75_disable)


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
            self.ui.stage2FreqButton.setStyleSheet(self.style.signal_75_disable)


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
            self.ui.stage3FreqButton.setStyleSheet(self.style.signal_75_disable)
            
        
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

                
    # def MemoryUpdate (self, mem, str_lst):
    #     if mem == 'mema':
    #         self.ui.memaDescLabel.setText(str_lst[0])
    #         self.ui.memaOneLabel.setText('1 - ' + str_lst[1])
    #         self.ui.memaTwoLabel.setText('2 - ' + str_lst[2])
    #         self.ui.memaThreeLabel.setText('3 - ' + str_lst[3])            

    #     if mem == 'memb':
    #         self.ui.membDescLabel.setText(str_lst[0])
    #         self.ui.membOneLabel.setText('1 - ' + str_lst[1])
    #         self.ui.membTwoLabel.setText('2 - ' + str_lst[2])
    #         self.ui.membThreeLabel.setText('3 - ' + str_lst[3])            

    #     if mem == 'memc':
    #         self.ui.memcDescLabel.setText(str_lst[0])
    #         self.ui.memcOneLabel.setText('1 - ' + str_lst[1])
    #         self.ui.memcTwoLabel.setText('2 - ' + str_lst[2])
    #         self.ui.memcThreeLabel.setText('3 - ' + str_lst[3])            

    #     if mem == 'memd':
    #         self.ui.memdDescLabel.setText(str_lst[0])
    #         self.ui.memdOneLabel.setText('1 - ' + str_lst[1])
    #         self.ui.memdTwoLabel.setText('2 - ' + str_lst[2])
    #         self.ui.memdThreeLabel.setText('3 - ' + str_lst[3])            

            
    # def MemoryButtonStatus (self, mem, status):
    #     if mem == 'mema':
    #         if status == 'enable':
    #             self.ui.memaButton.setStyleSheet(self.style.mem_90_button_enable)
    #         else:
    #             self.ui.memaButton.setStyleSheet(self.style.mem_90_button_disable)

    #     if mem == 'memb':
    #         if status == 'enable':
    #             self.ui.membButton.setStyleSheet(self.style.mem_90_button_enable)
    #         else:
    #             self.ui.membButton.setStyleSheet(self.style.mem_90_button_disable)

    #     if mem == 'memc':
    #         if status == 'enable':
    #             self.ui.memcButton.setStyleSheet(self.style.mem_90_button_enable)
    #         else:
    #             self.ui.memcButton.setStyleSheet(self.style.mem_90_button_disable)

    #     if mem == 'memd':
    #         if status == 'enable':
    #             self.ui.memdButton.setStyleSheet(self.style.mem_90_button_enable)
    #         else:
    #             self.ui.memdButton.setStyleSheet(self.style.mem_90_button_disable)


    ###########################
    # One Second Timer signal #
    ###########################
    def TimerOneSec(self):
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        """ one second gone, check if its something to do """
        if self.memButtonCnt > 3:
            self.memButtonCnt = 0
            print('go to configure ' + self.lastButtonChecked)
            self.MemoryScreen(self.lastButtonChecked)
            self.lastButtonChecked = ''            
        elif self.memButtonCnt > 0:
            self.memButtonCnt += 1

        if self.diagButtonCnt > 5:
            self.diagButtonCnt = 0
            self.DiagnosticsScreen()
        elif self.diagButtonCnt > 0:
            self.diagButtonCnt += 1

        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            # print(date_now)
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)

        # check for screensaver activation
        if self.screensaver_window == True:
            if self.timer_screensaver > 0:
                self.timer_screensaver -= 1
            else:
                self.ScreenSaverDialogScreen()

        # check for wifi manager
        if self.wifi_manager_cnt == 0:
            self.wifi_manager_cnt = 2
            self.UpdateTwoSec()
        else:
            self.wifi_manager_cnt -= 1


    def UpdateDateTime(self, new_date_time):
        date_str = ""
        if self.t.GetLocalization() == 'usa':
            date_str = new_date_time.strftime("%m/%d/%Y - %H:%M")
        elif self.t.GetLocalization() == 'arg':
            date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
            
        self.ui.date_timeLabel.setText(date_str)


    def UpdateTwoSec (self):
        new_status = self.MyThread.GetStatus()

        if new_status == 'NO CONN':
            self.ui.wifiButton.setIcon(self.wifi_disa_Icon)
        elif new_status == 'IP':
            self.ui.wifiButton.setIcon(self.wifi_err_Icon)
        elif new_status == 'PING':
            self.ui.wifiButton.setIcon(self.wifi_act_Icon)
        elif new_status == 'TUNNEL':
            self.ui.wifiButton.setIcon(self.wifi_emit_Icon)

            
    #############################
    # Antenna related Functions #
    #############################
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

        self.CheckForStart()


    def AntennaNameChange (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1Button':
            if self.antennas_connected.GetActive('ch1') == True and \
               self.antennas_connected.name_ch1 != 'unknow':
                if 'L: ' in self.ui.ch1Button.text():
                    ant_str = self.AntennaProcessName('ch1')
                else:
                    ant_str = 'CH1\n' + \
                              'R: ' + self.antennas_connected.GetRString('ch1') + '\n' + \
                              'L: ' + self.antennas_connected.GetLString('ch1') + '\n' + \
                              'I: ' + self.antennas_connected.GetIString('ch1') + '\n'

                self.ui.ch1Button.setText(ant_str)

        if sender.objectName() == 'ch2Button':
            if self.antennas_connected.GetActive('ch2') == True and \
               self.antennas_connected.name_ch2 != 'unknow':
                if 'L: ' in self.ui.ch2Button.text():
                    ant_str = self.AntennaProcessName('ch2')
                else:
                    ant_str = 'CH2\n' + \
                              'R: ' + self.antennas_connected.GetRString('ch2') + '\n' + \
                              'L: ' + self.antennas_connected.GetLString('ch2') + '\n' + \
                              'I: ' + self.antennas_connected.GetIString('ch2') + '\n'

                self.ui.ch2Button.setText(ant_str)

        if sender.objectName() == 'ch3Button':
            if self.antennas_connected.GetActive('ch3') == True and \
               self.antennas_connected.name_ch3 != 'unknow':
                if 'L: ' in self.ui.ch3Button.text():
                    ant_str = self.AntennaProcessName('ch3')
                else:
                    ant_str = 'CH3\n' + \
                              'R: ' + self.antennas_connected.GetRString('ch3') + '\n' + \
                              'L: ' + self.antennas_connected.GetLString('ch3') + '\n' + \
                              'I: ' + self.antennas_connected.GetIString('ch3') + '\n'

                self.ui.ch3Button.setText(ant_str)

        if sender.objectName() == 'ch4Button':
            if self.antennas_connected.GetActive('ch4') == True and \
               self.antennas_connected.name_ch4 != 'unknow':
                if 'L: ' in self.ui.ch4Button.text():
                    ant_str = self.AntennaProcessName('ch4')
                else:
                    ant_str = 'CH4\n' + \
                              'R: ' + self.antennas_connected.GetRString('ch4') + '\n' + \
                              'L: ' + self.antennas_connected.GetLString('ch4') + '\n' + \
                              'I: ' + self.antennas_connected.GetIString('ch4') + '\n'

                self.ui.ch4Button.setText(ant_str)
        
        self.ScreenSaverKick()
            

    def InsertColorText (self, new_text, color='red', plain=False):
        if color == 'red':
            self.ui.textEdit.setTextColor(QColor(237, 50, 55))            

        if color == 'blue':
            self.ui.textEdit.setTextColor(QColor(62, 64, 149))

        if color == 'green':
            self.ui.textEdit.setTextColor(QColor(0, 168, 89))

        if plain:
            self.ui.textEdit.insertPlainText(new_text)
        else:
            self.ui.textEdit.append(new_text)

            
    def InsertLocalText (self, new_text):
        self.InsertColorText(new_text, 'red')

        
    def InsertInfoText (self, new_text):
        self.InsertColorText(new_text, 'blue')

        
    def InsertInfoTextNoNewLine (self, new_text):
        self.InsertColorText(new_text, 'blue', True)
        

    def InsertLocalTextNoNewLine (self, new_text):
        self.InsertColorText(new_text, 'red', True)
        
        
    def InsertForeingText (self, new_text):
        self.InsertColorText(new_text, 'green')

        
    def InsertForeingTextNoNewLine (self, new_text):
        self.InsertColorText(new_text, 'green', True)


    def MemoryPressed (self):
        sender = self.sender()

        button_name = sender.objectName()
        button_sel = button_name.split('B')
        button_sel = button_sel[0]

        self.lastButtonChecked = button_sel
        self.memButtonCnt = 1
        self.ScreenSaverKick()


    """ function for tests, generates the required antenna strings """
    def ChannelChange (self):
        sender = self.sender()

        if sender.objectName() == 'ch2Button':
            # test ch1 with name
            ant_str = "Tunnel 12 inches fucker!,020.00,020.00,004.04,065.00,1\r"
            self.SerialProcess(ant_str)
            # test ch1 no name
            # ant_str = "ch1,020.00,020.00,004.04,065.00,1\r"
            # self.SerialProcess(ant_str)
            # test ch2 with name
            # ant_str = "Tunnel 12 inches fucker!,020.00,020.00,004.04,065.00,2\r"
            # self.SerialProcess(ant_str)
            # test ch2 no name
            # ant_str = "ch2,020.00,020.00,004.04,065.00,2\r"
            # self.SerialProcess(ant_str)
            # test ch3 with name
            ant_str = "Tunnel 12 inches fucker!,020.00,020.00,004.04,065.00,3\r"
            self.SerialProcess(ant_str)
            # test ch3 no name
            # ant_str = "ch3,020.00,020.00,004.04,065.00,3\r"
            # self.SerialProcess(ant_str)
            # test ch4 with name
            ant_str = "estoesTunnel 10 inches,020.00,020.00,004.04,065.00,4\r"
            self.SerialProcess(ant_str)            
            
        if sender.objectName() == 'ch3Button':
            ant_str = "antenna none\r"
            self.SerialProcess(ant_str)

        if sender.objectName() == 'ch4Button':
            pass


    def SerialProcess (self, rcv):
        show_message = True
        if rcv.startswith("antenna none"):
            self.antennas_connected.Flush()
            self.AntennaUpdate()

        # check if its antenna connection
        #Tunnel 12 inches,020.00,020.00,004.04,065.00,1
        #ch2,020.00,020.00,004.04,065.00,2
        #Tunnel 10 inches,020.00,020.00,004.04,065.00,4

        rcv_list = rcv.split(',')
        if len(rcv_list) == 6:
            print("antenna string getted")

            rcv_channel = rcv_list[5].rsplit('\r')
            if rcv_channel[0] >= '1' and rcv_channel[0] <= '4':
                if self.antennatimeout_finish == True:
                    self.antennatimeout_finish = False
                    self.antennatimeout.singleShot(500, self.AntennaUpdate)
                    self.antennas_connected.Flush()
                else:
                    print("QTimer is active")

                self.antennas_connected.ProcessStringList(rcv_list)

        if rcv.startswith("new antenna ch1"):
            self.ui.ch1Button.setStyleSheet(self.style.ch_getting)
            self.ui.ch1Button.setText("CH1\ngetting\nparams")
            show_message = False

        if rcv.startswith("new antenna ch2"):
            self.ui.ch2Button.setStyleSheet(self.style.ch_getting)
            self.ui.ch2Button.setText("CH2\ngetting\nparams")
            show_message = False            

        if rcv.startswith("new antenna ch3"):
            self.ui.ch3Button.setStyleSheet(self.style.ch_getting)
            self.ui.ch3Button.setText("CH3\ngetting\nparams")
            show_message = False            

        if rcv.startswith("new antenna ch4"):
            self.ui.ch4Button.setStyleSheet(self.style.ch_getting)
            self.ui.ch4Button.setText("CH4\ngetting\nparams")
            show_message = False

        if rcv.startswith("temp,"):
            show_message = False
            
        if show_message:
            self.InsertForeingText(rcv)        

            
    def MemoryReleased (self):
        sender = self.sender()

        button_name = sender.objectName()
        button_sel = button_name.split('B')
        button_sel = button_sel[0]

        if self.memButtonCnt > 0 and \
           self.memButtonCnt < 3:
            
            self.memButtonCnt = 0

            #get memory values
            mem_lst = self.t.mem_instant_dict[button_sel]
            if mem_lst[1] == '' and mem_lst[2] == '' and mem_lst[3] == '':
                self.InsertInfoText("Not much to do with memory!")
            else:
                self.MemoryToCurrentConf(mem_lst[1], mem_lst[2], mem_lst[3])
                self.Stage1GroupChange(self.stage1.GetStageStatus())
                self.Stage2GroupChange(self.stage2.GetStageStatus())
                self.Stage3GroupChange(self.stage3.GetStageStatus())
                self.UpdateTotalTime()
                self.CheckForStart()            


    def MemoryToCurrentConf (self, stage1_str, stage2_str, stage3_str):
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
        

    def DiagsPressed (self):
        self.diagButtonCnt = 1

        
    def DiagsReleased (self):
        self.diagButtonCnt = 0

        
    def SerialDataCallback (self, rcv):        
        # print ("serial data callback!")
        # print (rcv)
        self.SerialProcess(rcv)


    def CheckForStart (self):
        if self.CheckCompleteConf() == True and \
           self.s.port_open == True:
            self.ui.startButton.setStyleSheet(self.start_enable)
        else:
            self.ui.startButton.setStyleSheet(self.start_disable)

            
    def CheckCompleteConf (self):
        stages_in = False
        channels_in = False

        if self.stage1.GetStageStatus() == 'enable' or \
           self.stage2.GetStageStatus() == 'enable' or \
           self.stage3.GetStageStatus() == 'enable':
            stages_in = True

        if self.antennas_connected.GetActive('ch1') != False or \
           self.antennas_connected.GetActive('ch2') != False or \
           self.antennas_connected.GetActive('ch3') != False or \
           self.antennas_connected.GetActive('ch4') != False:
            channels_in = True
                                               
        if stages_in and channels_in:
            return True        

        return False
    
    
    ################################
    # Other Screens Calls are here #
    ################################

    ## Treatment Screen
    def TreatmentScreen (self):
        if self.debug_bool:
            print("TreatmentScreen called!")
            return
        
        if self.CheckCompleteConf() == True:
            if self.s.port_open == True:
                self.screensaver_window = False
                
                self.t.treatment_state = 'STOP'    #para un buen arranque la llamo con estado de stop
                stages_lst = [self.stage1, self.stage2, self.stage3]
                # a = TreatmentDialog(self.t, self.ss, self.antennas_connected, self.s, parent=self)
                a = TreatmentDialog(stages_lst, self.t, self.style, self.antennas_connected, self.s, self.parent)
                a.setModal(True)
                a.exec_()

                self.ScreenSaverKick()
                self.screensaver_window = True
                
            else:
                self.InsertInfoText("Serial Port Not Open!")
        else:
            self.InsertInfoText("Complete all params before start")


    ## DiagnosticsSreen
    def DiagnosticsScreen (self):
        if self.debug_bool:
            print("DiagnosticsScreen called!")
            return

        self.screensaver_window = False
        
        a = DiagnosticsDialog(self.s, self.t, parent=self.parent)
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()
        self.screensaver_window = True
        # fuerzo un update de fecha y hora cuando vuelvo de diagnostico
        date_now = datetime.today()
        self.UpdateDateTime(date_now)            
            
        
    ## MemoryScreen
    def MemoryScreen (self, which_mem):
        if self.debug_bool:
            print("MemoryScreen called!")
            return

        self.screensaver_window = False

        # send a list of the current config
        # ['Arm and Leg Inflammatory', "15' S 35% 7.83Hz", '', '']
        stage_new_lst = ['',\
                         self.stage1.StageDataToStr(),\
                         self.stage2.StageDataToStr(),\
                         self.stage3.StageDataToStr()]
        
        a = MemoryDialog(which_mem, stage_new_lst)
        a.setModal(True)
        a.exec_()

        if a.action == 'save':
            self.t.mem_instant_dict[which_mem] = stage_new_lst
            print(self.t.mem_instant_dict)
            self.PopullateFromDict(self.t.mem_instant_dict)

            ## backup instant mems to all mems
            for x in self.t.mem_instant_dict:
                self.t.mem_all_dict[x] = self.t.mem_instant_dict[x]

            ## save data on backup file
            self.t.SaveConfigFile()

        self.CheckForStart()
        self.ScreenSaverKick()
        self.screensaver_window = True
        
            
    ## ScreenSaver
    def ScreenSaverDialogScreen (self):
        a = ScreenSaverDialog()
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()

        
    def ScreenSaverKick (self):
        self.timer_screensaver = self.t.timeout_screensaver
            

    ## wifi screen
    def WifiScreen (self):
        if self.debug_bool:
            print("WifiScreen called!")
            return

        self.screensaver_window = False
        a = WiFiDialog()
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()
        self.screensaver_window = True
        

    ## Memory Manager Screen
    def MemoryManagerScreen (self):
        if self.debug_bool:
            print("MemoryManagerScreen called!")
            return

        mem_for_conf = self.t.mem_all_dict.copy()

        self.screensaver_window = False
        a = MemManagerDialog(mem_for_conf)
        a.setModal(True)
        a.exec_()
        
        if a.action == 'accept':
            print('Accept new config')
            self.t.mem_all_dict = mem_for_conf

            ## change data on instant mems
            for x in self.t.mem_instant_dict:
                self.t.mem_instant_dict[x] = self.t.mem_all_dict[x]

            ## show changes on instant mems
            self.PopullateFromDict(self.t.mem_instant_dict)

            ## save data on backup file
            self.t.SaveConfigFile()
            
        else:
            print('Last config its still valid')

        self.ScreenSaverKick()
        self.screensaver_window = True

        
    ## Stages Configuration Screen
    def StagesConfScreen (self):
        sender = self.sender()
        
        if self.debug_bool:
            print("Stages Configuration Screen called!")

            if sender.objectName() == 'stage1Button':
                print('Stage 1 selected for config')

            if sender.objectName() == 'stage2Button':
                print('Stage 2 selected for config')
            
            if sender.objectName() == 'stage3Button':
                print('Stage 3 selected for config')

            return 

        button_sel = sender.objectName()
        button_name = button_sel.split('B')
        button_name = button_name[0]
        stages_list = [self.stage1, self.stage2, self.stage3]
        s1_copy = copy.copy(self.stage1)
        s2_copy = copy.copy(self.stage2)
        s3_copy = copy.copy(self.stage3)
        stages_copy = [s1_copy, s2_copy, s3_copy]
        localization = self.t.GetLocalization()
        a = StagesDialog(stages_copy, self.style, localization, button_name)
    
        a.setModal(True)
        a.exec_()

        if a.action == 'accept':
            print('Accept new config')
            print('Config List')
            print(a.st_lst)

            self.stage1 = a.st_lst[0]
            self.stage2 = a.st_lst[1]
            self.stage3 = a.st_lst[2]
            self.Stage1GroupChange(self.stage1.GetStageStatus())
            self.Stage2GroupChange(self.stage2.GetStageStatus())
            self.Stage3GroupChange(self.stage3.GetStageStatus())
            self.UpdateTotalTime()
            
        else:
            print('Last config is still valid')
            print(stages_list)
            print('No implemented config')
            print(a.st_lst)

        self.CheckForStart()
            
    
### End of Dialog ###
### End of File ###
