import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#nueva clase que contiene la interface
class Ventana(QMainWindow):
    #metodo constructor
    def __init__(self):
        #inicio un objeto QMainWindow
        QMainWindow.__init__(self)
        #cargo el archivo de interface *.ui
        uic.loadUi("login.ui",self)
        self.setWindowTitle("Nuevo Nombre")

#instanciar aplicacion
app = QApplication(sys.argv)
#creo el objeto de la clase ventana
vent = Ventana()
#mostrar ventana
vent.show()
#ejecutar aplicacion
app.exec_()

