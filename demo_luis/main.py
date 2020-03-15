import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsColorizeEffect, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QPropertyAnimation
from PyQt5.QtGui import QColor

#importo UIs
from ui_demo_luis import Ui_Dialog


#### CLASE DIALOG (ventana principal)
class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        


app = QApplication(sys.argv)
w = Dialog()
w.setWindowFlags(Qt.CustomizeWindowHint)
w.showFullScreen()
w.show()
sys.exit(app.exec_())
