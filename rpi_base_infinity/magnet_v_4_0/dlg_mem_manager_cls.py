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
    def __init__(self, mem_dict):
        super(QDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # backup received data
        self.mem_dict = mem_dict

        self.action = 'back'

        # styles
        self.selected_blue = ''
        self.selected_cyan = ''

        self.label_blue = "color: rgb(55, 52, 53);\
                           background-color: rgb(32, 145, 235);"
        self.label_cyan = "color: rgb(55, 52, 53);\
                           background-color: rgb(178, 232, 247);"
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
        
        self.action_button_disable = "background-color: rgb(245, 245, 245);\
                                      border-radius: 20px;\
                                      border:3px solid rgb(230, 231, 232);\
                                      color: rgb(230,231,232);"

        self.action1_button_enable = "background-color: rgb(232, 175, 181);\
                                      border-radius: 20px;\
                                      border:3px solid rgb(55, 52, 53);\
                                      color: rgb(55, 52, 53);"

        self.action2_button_enable = "background-color: rgb(233, 245, 235);\
                                      border-radius: 20px;\
                                      border:3px solid rgb(55, 52, 53);\
                                      color: rgb(55, 52, 53);"

        self.action3_button_enable = "background-color: rgb(191, 211, 199);\
                                      border-radius: 20px;\
                                      border:3px solid rgb(55, 52, 53);\
                                      color: rgb(55, 52, 53);"

        self.ui.action1Button.setText('None')
        self.ui.action1Button.setStyleSheet(self.action_button_disable)

        # connect up buttons
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

        self.ui.action1Button.clicked.connect(self.Action1Button)
        self.ui.action2Button.clicked.connect(self.Action2Button)
        self.ui.action3Button.clicked.connect(self.Action3Button)
        

        self.ui_label_dict = {
            "mema" : [self.ui.memaDescLabel, self.ui.memaOneLabel, self.ui.memaTwoLabel, self.ui.memaThreeLabel],
            "memb" : [self.ui.membDescLabel, self.ui.membOneLabel, self.ui.membTwoLabel, self.ui.membThreeLabel],
            "memc" : [self.ui.memcDescLabel, self.ui.memcOneLabel, self.ui.memcTwoLabel, self.ui.memcThreeLabel],
            "memd" : [self.ui.memdDescLabel, self.ui.memdOneLabel, self.ui.memdTwoLabel, self.ui.memdThreeLabel],
            "mem5" : [self.ui.mem5DescLabel, self.ui.mem5OneLabel, self.ui.mem5TwoLabel, self.ui.mem5ThreeLabel],
            "mem6" : [self.ui.mem6DescLabel, self.ui.mem6OneLabel, self.ui.mem6TwoLabel, self.ui.mem6ThreeLabel],
            "mem7" : [self.ui.mem7DescLabel, self.ui.mem7OneLabel, self.ui.mem7TwoLabel, self.ui.mem7ThreeLabel],
            "mem8" : [self.ui.mem8DescLabel, self.ui.mem8OneLabel, self.ui.mem8TwoLabel, self.ui.mem8ThreeLabel],
            "mem9" : [self.ui.mem9DescLabel, self.ui.mem9OneLabel, self.ui.mem9TwoLabel, self.ui.mem9ThreeLabel],
            "mem10" : [self.ui.mem10DescLabel, self.ui.mem10OneLabel, self.ui.mem10TwoLabel, self.ui.mem10ThreeLabel],
            "mem11" : [self.ui.mem11DescLabel, self.ui.mem11OneLabel, self.ui.mem11TwoLabel, self.ui.mem11ThreeLabel],
            "mem12" : [self.ui.mem12DescLabel, self.ui.mem12OneLabel, self.ui.mem12TwoLabel, self.ui.mem12ThreeLabel],
            "mem13" : [self.ui.mem13DescLabel, self.ui.mem13OneLabel, self.ui.mem13TwoLabel, self.ui.mem13ThreeLabel],
            "mem14" : [self.ui.mem14DescLabel, self.ui.mem14OneLabel, self.ui.mem14TwoLabel, self.ui.mem14ThreeLabel],
            "mem15" : [self.ui.mem15DescLabel, self.ui.mem15OneLabel, self.ui.mem15TwoLabel, self.ui.mem15ThreeLabel],
            "mem16" : [self.ui.mem16DescLabel, self.ui.mem16OneLabel, self.ui.mem16TwoLabel, self.ui.mem16ThreeLabel],
            "mem17" : [self.ui.mem17DescLabel, self.ui.mem17OneLabel, self.ui.mem17TwoLabel, self.ui.mem17ThreeLabel],
            "mem18" : [self.ui.mem18DescLabel, self.ui.mem18OneLabel, self.ui.mem18TwoLabel, self.ui.mem18ThreeLabel],
            "mem19" : [self.ui.mem19DescLabel, self.ui.mem19OneLabel, self.ui.mem19TwoLabel, self.ui.mem19ThreeLabel],
            "mem20" : [self.ui.mem20DescLabel, self.ui.mem20OneLabel, self.ui.mem20TwoLabel, self.ui.mem20ThreeLabel]
            }

        self.ui_button_dict = {
            "mema" : self.ui.memaButton,
            "memb" : self.ui.membButton,
            "memc" : self.ui.memcButton,
            "memd" : self.ui.memdButton,
            "mem5" : self.ui.mem5Button,
            "mem6" : self.ui.mem6Button,
            "mem7" : self.ui.mem7Button,
            "mem8" : self.ui.mem8Button,
            "mem9" : self.ui.mem9Button,
            "mem10" : self.ui.mem10Button,
            "mem11" : self.ui.mem11Button,
            "mem12" : self.ui.mem12Button,
            "mem13" : self.ui.mem13Button,
            "mem14" : self.ui.mem14Button,
            "mem15" : self.ui.mem15Button,
            "mem16" : self.ui.mem16Button,
            "mem17" : self.ui.mem17Button,
            "mem18" : self.ui.mem18Button,
            "mem19" : self.ui.mem19Button,
            "mem20" : self.ui.mem20Button
            }
        
        self.PopullateFromDict (self.mem_dict)

    
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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
        
        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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
            
        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()

        
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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()
        

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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()


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
            self.CheckForActionsButtons()
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

        self.CheckForActionsButtons()


    def CheckForActionsButtons (self):
        if self.selected_blue !=  '' and self.selected_cyan != '':
            # copy blue over cyan or swap
            self.ui.helpLabel.setText('Copy blue over cyan or swap blue and cyan')
            self.ui.action1Button.setText('Copy blue\non cyan')
            self.ui.action2Button.setText('Swap blue\nand cyan')
        elif self.selected_blue != '':
            # clear mem or wait to select cyan
            self.ui.helpLabel.setText('Clear memory slot or pick another')
            self.ui.action1Button.setText('Clear\nmemory')
            self.ui.action2Button.setText('Back')
            self.ui.action1Button.setStyleSheet(self.action1_button_enable)
        elif self.selected_cyan != '':
            # clear mem or wait to select blue again
            self.ui.helpLabel.setText('Clear memory slot or pick another')
            self.ui.action1Button.setText('Clear\nmemory')
            self.ui.action2Button.setText('Back')
            self.ui.action1Button.setStyleSheet(self.action1_button_enable)
        else:
            self.ui.helpLabel.setText('Pick a memory slot')
            self.ui.action1Button.setText('None')
            self.ui.action2Button.setText('Back')
            self.ui.action3Button.setText('Save!')
            self.ui.action1Button.setStyleSheet(self.action_button_disable)


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
                

    def Action1Button (self):
        if self.ui.action1Button.text() == 'None':
            return

        elif self.ui.action1Button.text() == 'Clear\nmemory':
            if self.selected_blue != '':
                print("clearing mem blue")
                button_sel = self.selected_blue.split('B')
                button_sel = button_sel[0]

                self.mem_dict[button_sel] = ['','','','']
                self.PopullateFromDict(self.mem_dict)
                self.selected_blue = ''
                
            elif self.selected_cyan != '':
                print("clearing mem cyan")
                button_sel = self.selected_cyan.split('B')
                button_sel = button_sel[0]                

                self.mem_dict[button_sel] = ['','','','']
                self.PopullateFromDict(self.mem_dict)
                self.selected_cyan = ''
                
            else:
                print("error no blue or cyan selected!!!!!")

        elif self.ui.action1Button.text() == 'Copy blue\non cyan':
            if self.selected_blue != '' and self.selected_cyan != '':
                print("copy blue on cyan")
                button_blue = self.selected_blue.split('B')
                button_cyan = self.selected_cyan.split('B')
                button_blue = button_blue[0]
                button_cyan = button_cyan[0]

                self.mem_dict[button_cyan] = self.mem_dict[button_blue]
                self.PopullateFromDict(self.mem_dict)
                self.selected_blue = ''
                self.selected_cyan = ''                
            else:
                print("error no blue and cyan to copy!!!!!")


    def Action2Button (self):
        if self.ui.action2Button.text() == 'None':
            return

        elif self.ui.action2Button.text() == 'Back':
            print("go back to main")            
            self.accept()

        elif self.ui.action2Button.text() == 'Swap blue\nand cyan':
            if self.selected_blue != '' and self.selected_cyan != '':
                print("swap blue on cyan")
                button_blue = self.selected_blue.split('B')
                button_cyan = self.selected_cyan.split('B')
                button_blue = button_blue[0]
                button_cyan = button_cyan[0]

                mem_lst = self.mem_dict[button_cyan]
                self.mem_dict[button_cyan] = self.mem_dict[button_blue]
                self.mem_dict[button_blue] = mem_lst
                
                self.PopullateFromDict(self.mem_dict)
                self.selected_blue = ''
                self.selected_cyan = ''                
            else:
                print("error no blue and cyan to swap!!!!!")

                
    def Action3Button (self):
        self.action = 'accept'
        self.accept()
                

        
### end of file ###

