from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt


#get the UI from here
from ui_memory_dlg import Ui_MemoryDialog


##################################################
# MemoryDialog Class - to save or empty memories #
##################################################
class MemoryDialog (QDialog):


    def __init__(self):
        super(MemoryDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MemoryDialog()
        self.ui.setupUi(self)

        # get the close event and connect the buttons        
        self.ui.saveButton.clicked.connect(self.SaveCurrentConf)
        # self.ui.emptyButton.clicked.connect(self.EmptyCurrentConf)
        self.ui.emptyButton.clicked.connect(self.accept)        


    def SaveCurrentConf (self):
        pass


        
        
### end of file ###

