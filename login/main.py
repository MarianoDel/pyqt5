#con este metodo puedo tomar control de los widgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow

class LoginDialog(QMainWindow):
    def __init__(self):
        super(LoginDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # # Make some local modifications.
        # self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        # self.ui.okButton.clicked.connect(self.accept)
        # self.ui.cancelButton.clicked.connect(self.reject)

app = QApplication(sys.argv)
w = LoginDialog()
w.show()
sys.exit(app.exec_())
