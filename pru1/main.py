# always seem to need this
import sys, os

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import ui_pru

#virtualkeyboard
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

# create class for our Raspberry Pi GUI
class Dialog(QDialog, ui_pru.Ui_Dialog):
   # access variables inside of the UI's file
   def sliderValue(self):
      print ("Slider moved")

   def pressedButton(self):
      print ("Pressed!")
      
   def __init__(self):
      super(self.__class__, self).__init__()
      self.setupUi(self) # gets defined in the UI file

      ### Hooks to for buttons
      self.pushButton.clicked.connect(lambda: self.pressedButton())
      self.verticalSlider.valueChanged.connect(lambda: self.sliderValue())
   
# I feel better having one of these
def main():
   # a new app instance
   app = QApplication(sys.argv)
   form = Dialog()
   form.show()
   # without this, the script exits immediately.
   sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
   main()

