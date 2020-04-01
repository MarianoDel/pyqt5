from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt


#get the UI from here
from ui_memory_dlg import Ui_MemoryDialog


##################################################
# MemoryDialog Class - to save or empty memories #
##################################################
class MemoryDialog (QDialog):


    def __init__(self, style_obj, which_mem):
        super(MemoryDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MemoryDialog()
        self.ui.setupUi(self)

        # get references
        self.style = style_obj
                
        # get the close event and connect the buttons        
        self.ui.saveButton.clicked.connect(self.SaveCurrentConf)
        self.ui.emptyButton.clicked.connect(self.EmptyCurrentConf)
        self.ui.backButton.clicked.connect(self.accept)

        # answer to parent what to do
        self.action = 'back'

        if which_mem == 'mem1':
            self.ui.memButton.setStyleSheet(self.style.mem1_button_enable)
            self.ui.memButton.setText('I')
        elif which_mem == 'mem2':
            self.ui.memButton.setStyleSheet(self.style.mem2_button_enable)
            self.ui.memButton.setText('II')            
        else:
            self.ui.memButton.setStyleSheet(self.style.mem3_button_enable)
            self.ui.memButton.setText('III')
        


    def SaveCurrentConf (self):
        self.action = 'save'
        self.accept()


    def EmptyCurrentConf (self):
        self.action = 'empty'
        self.accept()
    

        
        
### end of file ###

