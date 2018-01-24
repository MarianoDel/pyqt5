import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_imagedialog import Ui_ImageDialog

class ImageDialog(QDialog, Ui_ImageDialog):
    def __init__(self):
        super(ImageDialog, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # # Make some local modifications.
        # self.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        # self.okButton.clicked.connect(self.accept)
        # self.cancelButton.clicked.connect(self.reject)

app = QApplication(sys.argv)
w = ImageDialog()
w.show()
sys.exit(app.exec_())
