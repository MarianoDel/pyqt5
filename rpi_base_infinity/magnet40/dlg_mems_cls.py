from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt


#get the UI from here
from ui_memory_dlg import Ui_MemoryDialog
# get Dialog classes from here
from wifi_keyboard_cls import KeyboardDialog


##################################################
# MemoryDialog Class - to save or empty memories #
##################################################
class MemoryDialog (QDialog):


    def __init__(self, which_mem, stage_lst):
        super(MemoryDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MemoryDialog()
        self.ui.setupUi(self)

        # save the getted data
        self.stage_lst = stage_lst
        
        # get the close event and connect the buttons        
        self.ui.editButton.clicked.connect(self.EditName)
        self.ui.acceptButton.clicked.connect(self.SaveCurrentConf)        
        self.ui.emptyButton.clicked.connect(self.EmptyName)
        self.ui.backButton.clicked.connect(self.accept)

        # answer to parent what to do
        self.action = 'back'

        if which_mem == 'mema':
            self.ui.memButton.setText('A')
        elif which_mem == 'memb':
            self.ui.memButton.setText('B')
        elif which_mem == 'memc':
            self.ui.memButton.setText('C')
        else:
            self.ui.memButton.setText('D')
        
        self.ui.memDescLabel.setText(self.stage_lst[0])
        self.ui.memOneLabel.setText('1 - ' + self.stage_lst[1])
        self.ui.memTwoLabel.setText('2 - ' + self.stage_lst[2])
        self.ui.memThreeLabel.setText('3 - ' + self.stage_lst[3])
        

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

                
    def SaveCurrentConf (self):
        self.action = 'save'
        self.accept()


    def EmptyName (self):
        self.ui.memDescLabel.setText('')
        self.stage_lst[0] = ''
        

    def EditName (self):
        pass_str = self.KeyboardScreen("Last name: ", self.ui.memDescLabel.text())
        self.ui.memDescLabel.setText(pass_str)
        self.stage_lst[0] = pass_str


    ####################
    # Function Screens #
    ####################
    def KeyboardScreen (self, conf, last):
        a = KeyboardDialog(conf, last)
        a.setModal(True)
        a.exec_()
        return a.answer
        
### end of file ###

