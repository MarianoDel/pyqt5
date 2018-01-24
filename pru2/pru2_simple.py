import sys
from PyQt5.QtWidgets import QApplication, QDialog
from pru2_auto import Ui_Dialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
