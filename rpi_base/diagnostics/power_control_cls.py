from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject


#get the UI from here
from power_control_ui import Ui_PowerControlDialog


##############################################################
# PowerControlDialog Class - to set the system power control #
##############################################################
class PowerControlDialog(QDialog):
    def __init__(self, treatment_instance):
        super(PowerControlDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_PowerControlDialog()
        self.ui.setupUi(self)

        # get the close event and connect the other buttons
        self.ui.doneButton.clicked.connect(self.FinishThisDialog)
        self.ui.triangUpButton.clicked.connect(self.triangUpBtn)
        self.ui.triangDwnButton.clicked.connect(self.triangDwnBtn)
        self.ui.squareUpButton.clicked.connect(self.squareUpBtn)
        self.ui.squareDwnButton.clicked.connect(self.squareDwnBtn)
        self.ui.sinusUpButton.clicked.connect(self.sinusUpBtn)
        self.ui.sinusDwnButton.clicked.connect(self.sinusDwnBtn)

        ## this ones must be getted from config.txt file or passed as object arguments
        self.t = treatment_instance
        self.trianglimit = self.t.triangular_power_limit
        self.squarelimit = self.t.square_power_limit
        self.sinuslimit = self.t.sinusoidal_power_limit
        self.peak = self.t.peak_current
        self.resistance065 = self.t.resistance065
        self.resistance080 = self.t.resistance080
        self.tempcoef065 = self.t.tempcoef065
        self.tempcoef080 = self.t.tempcoef080
        self.tempamb = self.t.tempamb
        

        ## first run
        self.ui.triangLimitLabel.setText(str(self.trianglimit) + "%")
        self.ui.squareLimitLabel.setText(str(self.squarelimit) + "%")
        self.ui.sinusLimitLabel.setText(str(self.sinuslimit) + "%")
        self.UpdateTriang()
        self.UpdateSquare()
        self.UpdateSinus()
        

    def triangUpBtn (self):
        if self.trianglimit < 100:
            self.trianglimit += 1

        self.ui.triangLimitLabel.setText(str(self.trianglimit) + "%")
        self.UpdateTriang()

    def triangDwnBtn (self):
        if self.trianglimit > 10:
            self.trianglimit -= 1

        self.ui.triangLimitLabel.setText(str(self.trianglimit) + "%")
        self.UpdateTriang()

    def squareUpBtn (self):
        if self.squarelimit < 100:
            self.squarelimit += 1

        self.ui.squareLimitLabel.setText(str(self.squarelimit) + "%")
        self.UpdateSquare()

    def squareDwnBtn (self):
        if self.squarelimit > 10:
            self.squarelimit -= 1

        self.ui.squareLimitLabel.setText(str(self.squarelimit) + "%")
        self.UpdateSquare()

    def sinusUpBtn (self):
        if self.sinuslimit < 100:
            self.sinuslimit += 1

        self.ui.sinusLimitLabel.setText(str(self.sinuslimit) + "%")
        self.UpdateSinus()

    def sinusDwnBtn (self):
        if self.sinuslimit > 10:
            self.sinuslimit -= 1

        self.ui.sinusLimitLabel.setText(str(self.sinuslimit) + "%")
        self.UpdateSinus()        


    def UpdateTriang (self):
        i = 0.01 * self.peak * self.trianglimit
        i = i * 0.4083
        self.ui.triangCurrLabel.setText("{0:.3f}".format(i))

        p065 = i * i * self.resistance065
        p080 = i * i * self.resistance080        
        self.ui.triangPwr065Label.setText("{0:.1f}".format(p065))
        self.ui.triangPwr080Label.setText("{0:.1f}".format(p080))

        t065 = p065 * self.tempcoef065 + self.tempamb
        t080 = p080 * self.tempcoef080 + self.tempamb
        self.ui.triangTemp065Label.setText(str(int(t065)))
        self.ui.triangTemp080Label.setText(str(int(t080)))
        

    def UpdateSquare (self):
        i = 0.01 * self.peak * self.squarelimit
        i = i * 0.7071
        self.ui.squareCurrLabel.setText("{0:.3f}".format(i))

        p065 = i * i * self.resistance065
        p080 = i * i * self.resistance080        
        self.ui.squarePwr065Label.setText("{0:.1f}".format(p065))
        self.ui.squarePwr080Label.setText("{0:.1f}".format(p080))

        t065 = p065 * self.tempcoef065 + self.tempamb
        t080 = p080 * self.tempcoef080 + self.tempamb
        self.ui.squareTemp065Label.setText(str(int(t065)))
        self.ui.squareTemp080Label.setText(str(int(t080)))
        

    def UpdateSinus (self):
        i = 0.01 * self.peak * self.sinuslimit
        i = i * 0.5
        self.ui.sinusCurrLabel.setText("{0:.3f}".format(i))

        p065 = i * i * self.resistance065
        p080 = i * i * self.resistance080
        self.ui.sinusPwr065Label.setText("{0:.1f}".format(p065))
        self.ui.sinusPwr080Label.setText("{0:.1f}".format(p080))

        t065 = p065 * self.tempcoef065 + self.tempamb 
        t080 = p080 * self.tempcoef080 + self.tempamb
        self.ui.sinusTemp065Label.setText(str(int(t065)))
        self.ui.sinusTemp080Label.setText(str(int(t080)))
        

    def FinishThisDialog (self):
        self.t.triangular_power_limit = self.trianglimit
        self.t.square_power_limit = self.squarelimit
        self.t.sinusoidal_power_limit = self.sinuslimit
        
        self.t.SaveConfigFile()
        self.accept()
        

        
### end of file ###
