import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_first import Ui_firstDialog
from ui_modal import Ui_modalDialog

class MDialog(QDialog):
    def __init__(self):
        super(MDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_modalDialog()
        self.ui.setupUi(self)

        # # # Make some local modifications.
        # # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        # #
        # # # Connect up the buttons.
        # self.ui.pushButton.clicked.connect(self.LaunchSecond)
        # # self.ui.cancelButton.clicked.connect(self.reject)

    def isChecked(self):
        return self.ui.checkBox.isChecked()

    def changeLabel(self, new_string):
        self.ui.parentLabel.setText("me enviarion: " + new_string)

        
class FDialog(QDialog):
    def __init__(self):
        super(FDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_firstDialog()
        self.ui.setupUi(self)

        # # Make some local modifications.
        # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        self.ui.pushButton.clicked.connect(self.LaunchSecond)
        # self.ui.cancelButton.clicked.connect(self.reject)

    def LaunchSecond (self):
        self.ui.touchLabel.setText("??")
        a = MDialog()
        a.setModal(True)
        a.changeLabel("gil!")
        a.exec_()
        istouched = a.isChecked()
        if istouched == True:
            self.ui.touchLabel.setText("Alguien metio el dedo!")
        else:
            self.ui.touchLabel.setText("Nadie toco nada")
        


        
app = QApplication(sys.argv)
w = FDialog()
w.show()
sys.exit(app.exec_())
